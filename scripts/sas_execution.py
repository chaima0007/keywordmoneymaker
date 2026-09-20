#!/usr/bin/env python3
"""Contrôle d'exécution du sas — le code fait-il vraiment ce qu'il prétend.

Deux phases, et la distinction entre les deux est tout l'intérêt du contrôle.

PHASE 1 — INSTALLATION, RÉSEAU OUVERT, OBSERVÉE.
Il faut bien télécharger les dépendances. Cette phase n'est PAS isolée et le
rapport le dit. Ce qu'on en retire : la liste de ce que la brique DÉCLARE aller
chercher, lue dans ses manifestes. Une brique qui déclare trois dépendances et
une brique qui en déclare huit cents ne présentent pas le même risque.

PHASE 2 — TESTS, RÉSEAU COUPÉ.
Les tests de la brique tournent dans « unshare -n -r » : espace de noms réseau
neuf et vide, aucune interface hors « lo ». Vérifié : github.com n'est plus
résolvable à l'intérieur. Tout ce que le code tente de joindre échoue et LAISSE
UNE TRACE — c'est précisément ce qu'on veut lire.

CE QUE CETTE ISOLATION N'EST PAS, et il faut le dire :
« unshare -n » isole le RÉSEAU, pas le système de fichiers ni les processus.
Un code hostile peut encore lire et écrire hors de son dossier. Ce contrôle
répond à « que tente-t-elle de joindre » et « fonctionne-t-elle sans réseau »,
pas à « est-elle inoffensive ». Pour cela il faut un vrai bac à sable —
NVIDIA/OpenShell (B-01) fait exactement ça, et c'est une des raisons de
l'avoir mise au registre.

Usage :
    python3 scripts/sas_execution.py <url> [<commit>]
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DELAI_CLONE = 240
DELAI_INSTALL = 600
DELAI_TESTS = 420

# Motifs qui trahissent un échec DÛ au réseau coupé, et non un vrai échec.
# Motifs qui trahissent une ABSENCE D'OUTILLAGE chez nous, et non un défaut du
# code examiné. Confondre les deux ferait condamner une brique saine : constaté
# le 2026-09-20 sur loopx, déclarée « ÉCHOUE » parce que pytest manquait ICI.
OUTILLAGE_ABSENT = re.compile(
    r"(No module named [\w.]+|command not found|: not found|"
    r"executable file not found|cannot find package|no such file or directory: )",
    re.IGNORECASE)

ECHEC_RESEAU = re.compile(
    r"(Temporary failure in name resolution|Name or service not known|"
    r"nodename nor servname|Network is unreachable|Connection refused|"
    r"getaddrinfo|ENOTFOUND|EAI_AGAIN|Could not resolve host|"
    r"Max retries exceeded|ConnectionError|dial tcp)", re.IGNORECASE)


def _courir(cmd: list[str], cwd: Path, delai: int, env: dict | None = None) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                           timeout=delai, env=env)
        return r.returncode, (r.stdout + r.stderr)[-6000:]
    except subprocess.TimeoutExpired:
        return 124, f"DÉLAI DÉPASSÉ après {delai}s"
    except FileNotFoundError as e:
        return 127, f"outil absent : {e}"


def _isole(cmd: list[str]) -> list[str]:
    """Enveloppe une commande dans un espace de noms réseau vide."""
    return ["unshare", "-n", "-r", "--"] + cmd


def detecter(depot: Path) -> dict:
    """Quel écosystème, et que déclare-t-elle aller chercher."""
    eco: dict = {"type": None, "declare": {}, "commande_install": None, "commande_tests": None}

    if (depot / "pyproject.toml").exists() or (depot / "requirements.txt").exists():
        eco["type"] = "python"
        noms: list[str] = []
        req = depot / "requirements.txt"
        if req.exists():
            noms = [l.split("==")[0].split(">")[0].split("[")[0].strip()
                    for l in req.read_text(errors="replace").splitlines()
                    if l.strip() and not l.startswith("#")]
        pyp = depot / "pyproject.toml"
        if pyp.exists():
            texte = pyp.read_text(errors="replace")
            bloc = re.search(r"dependencies\s*=\s*\[(.*?)\]", texte, re.S)
            if bloc:
                noms += re.findall(r'"([A-Za-z0-9_.\-]+)', bloc.group(1))
        eco["declare"] = {"paquets": sorted(set(n for n in noms if n))}
        eco["commande_install"] = ["python3", "-m", "pip", "install", "-q", "-e", "."]
        eco["harnais"] = ["python3", "-m", "pip", "install", "-q", "pytest"]
        eco["commande_tests"] = ["python3", "-m", "pytest", "-x", "-q", "--no-header"]

    elif (depot / "go.mod").exists():
        eco["type"] = "go"
        mod = (depot / "go.mod").read_text(errors="replace")
        eco["declare"] = {"modules": re.findall(r"^\s+([\w.\-/]+)\s+v", mod, re.M)}
        eco["commande_install"] = ["go", "mod", "download"]
        eco["commande_tests"] = ["go", "test", "./...", "-count=1", "-short"]

    elif (depot / "Cargo.toml").exists():
        eco["type"] = "rust"
        eco["commande_install"] = ["cargo", "fetch", "--quiet"]
        eco["commande_tests"] = ["cargo", "test", "--offline", "--quiet"]

    elif (depot / "package.json").exists():
        eco["type"] = "node"
        paquet = json.loads((depot / "package.json").read_text(errors="replace"))
        eco["declare"] = {
            "dependances": sorted(paquet.get("dependencies", {})),
            "dev": sorted(paquet.get("devDependencies", {})),
        }
        eco["commande_install"] = ["npm", "install", "--silent", "--no-audit", "--no-fund"]
        eco["commande_tests"] = ["npm", "test", "--silent"]

    return eco


def examiner(url: str, commit: str | None = None) -> dict:
    racine = Path(tempfile.mkdtemp(prefix="sas-exec-"))
    r: dict = {"url": url, "commit": commit, "ecosysteme": None, "declare": {},
               "install": None, "tests": None, "verdict": None, "motif": None,
               "tentatives_reseau": []}
    try:
        depot = racine / "d"
        code, sortie = _courir(["git", "clone", "--quiet", url, str(depot)], racine, DELAI_CLONE)
        if code != 0:
            r["verdict"] = "NE CONCLUT PAS"
            r["motif"] = f"clone impossible : {sortie.strip()[:200]}"
            return r
        if commit:
            _courir(["git", "checkout", "--quiet", commit], depot, 60)
        sha = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"],
                             capture_output=True, text=True)
        r["commit"] = sha.stdout.strip()

        eco = detecter(depot)
        r["ecosysteme"] = eco["type"]
        r["declare"] = eco["declare"]
        if not eco["type"]:
            r["verdict"] = "NE CONCLUT PAS"
            r["motif"] = "aucun manifeste reconnu (pyproject, go.mod, Cargo.toml, package.json)"
            return r

        # PHASE 1 — réseau ouvert, non isolée, et le rapport le dit.
        env = dict(os.environ, HOME=str(racine / "home"), PIP_DISABLE_PIP_VERSION_CHECK="1")
        (racine / "home").mkdir(exist_ok=True)
        code, sortie = _courir(eco["commande_install"], depot, DELAI_INSTALL, env)
        r["install"] = {"code": code, "extrait": sortie[-1500:]}

        # Le harnais de test s'installe en phase 1, réseau ouvert. C'est du
        # montage, pas de l'exécution du code examiné — et sans lui la phase 2
        # ne mesure rien.
        if eco.get("harnais"):
            hc, hs = _courir(eco["harnais"], depot, DELAI_INSTALL, env)
            r["harnais"] = {"code": hc, "extrait": hs[-600:]}

        # PHASE 2 — réseau COUPÉ.
        code, sortie = _courir(_isole(eco["commande_tests"]), depot, DELAI_TESTS, env)
        r["tests"] = {"code": code, "extrait": sortie[-2500:]}
        r["tentatives_reseau"] = sorted(set(m.group(0) for m in ECHEC_RESEAU.finditer(sortie)))

        manques = sorted(set(m.group(0).strip() for m in OUTILLAGE_ABSENT.finditer(sortie)))
        if code == 0:
            r["verdict"] = "FONCTIONNE"
            r["motif"] = "les tests du projet passent, réseau coupé"
        elif r["tentatives_reseau"]:
            r["verdict"] = "NE CONCLUT PAS"
            r["motif"] = ("les tests échouent EN TENTANT DE JOINDRE LE RÉSEAU : "
                          + ", ".join(r["tentatives_reseau"][:3])
                          + ". Ce n'est pas un échec du code, c'est un besoin de réseau "
                            "qu'il faut connaître avant de l'assembler.")
        elif code == 127 or manques:
            r["verdict"] = "NE CONCLUT PAS"
            r["motif"] = ("OUTILLAGE ABSENT CHEZ NOUS, pas un défaut de la brique : "
                          + ", ".join(manques[:3] or [sortie.strip()[:120]]))
        elif code == 124:
            r["verdict"] = "NE CONCLUT PAS"
            r["motif"] = f"délai dépassé ({DELAI_TESTS}s)"
        else:
            r["verdict"] = "ÉCHOUE"
            r["motif"] = f"les tests du projet échouent (code {code}), sans tentative réseau"
    finally:
        shutil.rmtree(racine, ignore_errors=True)
    return r


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    r = examiner(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    marque = {"FONCTIONNE": "✅", "ÉCHOUE": "🔴", "NE CONCLUT PAS": "⏸"}[r["verdict"]]
    print(f"\n─── {r['url']}")
    print(f"  commit      : {r['commit']}")
    print(f"  écosystème  : {r['ecosysteme']}")
    for cle, valeur in (r["declare"] or {}).items():
        print(f"  déclare     : {len(valeur)} {cle} — {', '.join(valeur[:6])}"
              + (" …" if len(valeur) > 6 else ""))
    if r["install"]:
        print(f"  install     : code {r['install']['code']} (RÉSEAU OUVERT, non isolé)")
    if r["tests"]:
        print(f"  tests       : code {r['tests']['code']} (RÉSEAU COUPÉ, unshare -n)")
    if r["tentatives_reseau"]:
        print(f"  a tenté de joindre le réseau : {', '.join(r['tentatives_reseau'])}")
    print(f"  {marque} {r['verdict']} — {r['motif']}")
    if r["tests"] and r["tests"]["code"] != 0:
        print("  ── extrait ──")
        for ligne in r["tests"]["extrait"].strip().splitlines()[-12:]:
            print(f"     {ligne}")


if __name__ == "__main__":
    main()
