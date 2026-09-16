#!/usr/bin/env python3
"""La base unique de l'Empire — engendrée, jamais écrite à la main.

POURQUOI CE FICHIER EXISTE
--------------------------
Tout ce qui a été perdu l'a été pour une seule raison : **ça n'existait qu'à un seul
endroit**. Le site La Loi Avec Moi (Next.js, 13 routes, 34 modèles de courriers) : un
dossier de session, aucun dépôt distant, disparu. Le code v0.2 du 06/09 : même cause,
même résultat. Et à l'inverse, deux « bases uniques de propriété » ont été créées à trois
minutes d'écart par deux sessions qui s'ignoraient.

Une chose qui n'est qu'à un endroit est en sursis. Une chose qui est à deux endroits sans
que personne ne les compare finit par diverger. **Ce script mesure les deux.**

CE QU'IL FAIT
-------------
Il engendre `codex/BASE/INVENTAIRE.md` à partir de ce qui existe RÉELLEMENT :
  · les dépôts git clonés localement — branche, dernier commit, travail non poussé ;
  · les registres tenus dans ce dépôt — agents, routines, erreurs, rapports, débats ;
  · le relevé du Drive (`codex/BASE/drive-snapshot.json`).

Et pour chaque projet, il répond à **la seule question qui compte** :
**combien d'endroits le gardent ?** Drive · GitHub · local. Un seul = alerte.

CE QU'IL NE FAIT PAS
--------------------
Il n'interroge pas le Drive : aucune session ne peut le faire depuis un script. Il lit un
relevé, et **il dit son âge**. Un relevé vieux ment en silence — c'est pourquoi sa date est
affichée en tête de l'inventaire plutôt qu'enfouie.

Il ne compare pas les CONTENUS entre les trois emplacements. Il compte les emplacements.
Dire qu'un même document diverge entre Drive et dépôt demanderait de lire les deux ; ce
n'est pas fait, et ce n'est donc pas affirmé.

Usage :  python3 scripts/inventorier.py            (engendre)
         python3 scripts/inventorier.py --verifier  (échoue si l'inventaire a dérivé)
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BASE = RACINE / "codex" / "BASE"
SNAPSHOT = BASE / "drive-snapshot.json"
SORTIE = BASE / "INVENTAIRE.md"
RACINE_CLONES = RACINE.parent

# Âge au-delà duquel le relevé Drive cesse d'être digne de confiance.
JOURS_AVANT_PEREMPTION = 30


def _git(depot: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def depots_locaux() -> list[dict]:
    depots = []
    for chemin in sorted(RACINE_CLONES.iterdir()):
        if not (chemin / ".git").exists():
            continue
        distant = _git(chemin, "remote", "get-url", "origin")
        nom = distant.rstrip("/").split("/")[-1].removesuffix(".git") if distant else chemin.name
        non_pousse = _git(chemin, "log", "--oneline", "@{u}..HEAD") if _git(
            chemin, "rev-parse", "--abbrev-ref", "@{u}") else ""
        depots.append({
            "nom": nom,
            "chemin": str(chemin),
            "distant": distant or "AUCUN DÉPÔT DISTANT",
            "branche": _git(chemin, "rev-parse", "--abbrev-ref", "HEAD"),
            "dernier": _git(chemin, "log", "-1", "--format=%h %cd", "--date=short"),
            "sale": bool(_git(chemin, "status", "--porcelain")),
            "non_pousse": len(non_pousse.splitlines()) if non_pousse else 0,
        })
    return depots


def registres() -> list[tuple[str, str]]:
    def compte(motif: str, filtre=lambda p: True) -> int:
        return sum(1 for p in RACINE.glob(motif) if filtre(p))

    lignes = [
        (".claude/agents/", f"{compte('.claude/agents/*.md')} rôles"),
        ("codex/rapports/", f"{compte('codex/rapports/*.md', lambda p: not p.name.startswith(('README', '_')))} rapports déposés"),
    ]
    for f in (".claude/BASE-ERREURS.md", "🔴 ERREURS.md", "codex/ROUTINES.md",
              "codex/A-DECIDER.md", "codex/DEBATS.md", "codex/CONSIGNE-N1.md",
              "codex/agents-correspondance.md", "codex/PROMPT-MAITRE-CHAINE.md"):
        chemin = RACINE / f
        lignes.append((f, f"{len(chemin.read_text(encoding='utf-8').splitlines())} lignes"
                       if chemin.exists() else "**ABSENT**"))
    return lignes


def couverture(depots: list[dict], drive: dict) -> list[dict]:
    """Pour chaque projet : combien d'emplacements le gardent."""
    par_projet: dict[str, dict] = {}
    for d in drive["dossiers"]:
        p = d["projet"]
        par_projet.setdefault(p, {"drive": 0, "github": False, "local": False, "distant": ""})
        par_projet[p]["drive"] += 1
    for r in depots:
        # Le nom du dépôt sert de clé de projet ; « keywordmoneymaker » héberge Caelum.
        cle = {"keywordmoneymaker": "caelum", "TEST": "competeiq"}.get(r["nom"], r["nom"])
        e = par_projet.setdefault(cle, {"drive": 0, "github": False, "local": False, "distant": ""})
        e["local"] = True
        e["github"] = r["distant"] != "AUCUN DÉPÔT DISTANT"
        e["distant"] = r["distant"]
    resultat = []
    for nom, e in sorted(par_projet.items()):
        n = (1 if e["drive"] else 0) + (1 if e["github"] else 0) + (1 if e["local"] else 0)
        resultat.append({"projet": nom, **e, "emplacements": n})
    return resultat


def engendrer() -> str:
    drive = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    depots = depots_locaux()
    couv = couverture(depots, drive)

    releve = datetime.strptime(drive["releve_le"], "%Y-%m-%d").date()
    age = (date.today() - releve).days
    peremption = (f"⚠️ **Relevé Drive vieux de {age} jours** — au-delà de "
                  f"{JOURS_AVANT_PEREMPTION}, il ne fait plus foi."
                  if age > JOURS_AVANT_PEREMPTION
                  else f"Relevé Drive du **{drive['releve_le']}** ({age} j).")

    l = ["# INVENTAIRE — la base unique de l'Empire", "",
         "> **FICHIER ENGENDRÉ — ne pas éditer à la main.**",
         "> `python3 scripts/inventorier.py` le régénère ; la CI échoue s'il a dérivé.", "",
         f"Engendré le **{date.today().isoformat()}**. {peremption}", "",
         "---", "", "## 1. COUVERTURE — combien d'endroits gardent chaque projet", "",
         "C'est la seule question qui compte. Tout ce qui a été perdu n'existait qu'à un endroit.", "",
         "| Projet | Drive | GitHub | Local | Emplacements |", "|---|---|---|---|---|"]

    for c in couv:
        marque = {3: "✅ 3", 2: "🟠 2", 1: "🔴 **1 — EN SURSIS**", 0: "—"}[c["emplacements"]]
        l.append(f"| {c['projet']} | {c['drive'] or '—'} dossier(s) | "
                 f"{'oui' if c['github'] else '—'} | {'oui' if c['local'] else '—'} | {marque} |")

    seuls = [c["projet"] for c in couv if c["emplacements"] == 1]
    l += ["", (f"🔴 **{len(seuls)} projet(s) à un seul emplacement** : "
               + ", ".join(seuls) + ". Une chose qui n'est qu'à un endroit est en sursis."
               if seuls else "✅ Aucun projet à un seul emplacement."), ""]

    l += ["## 2. DÉPÔTS GIT CLONÉS ICI", "",
          "| Dépôt | Branche | Dernier commit | Non poussé | Arbre |", "|---|---|---|---|---|"]
    for r in depots:
        np = f"🔴 **{r['non_pousse']} commit(s)**" if r["non_pousse"] else "—"
        l.append(f"| `{r['nom']}` | {r['branche']} | {r['dernier']} | {np} | "
                 f"{'modifié' if r['sale'] else 'propre'} |")

    l += ["", "## 3. DOSSIERS DRIVE", "", "| Dossier | Rôle | Projet |", "|---|---|---|"]
    for d in drive["dossiers"]:
        l.append(f"| {d['titre']} | {d['role']} | {d['projet']} |")

    l += ["", "## 4. REGISTRES TENUS DANS CE DÉPÔT", "", "| Registre | Volume |", "|---|---|"]
    for nom, vol in registres():
        l.append(f"| `{nom}` | {vol} |")

    l += ["", "---", "",
          "## CE QUE CET INVENTAIRE NE DIT PAS", "",
          "Il **compte les emplacements**, il ne compare pas les **contenus**. Deux copies d'un même",
          "document peuvent avoir divergé sans que rien ici ne le signale : le dire demanderait de",
          "lire les deux, ce qui n'est pas fait — et n'est donc pas affirmé.", "",
          "Il ne voit du Drive que ce que le relevé contient. Le nombre de documents par dossier",
          "n'est pas relevé. **Un inventaire honnête dit où il est aveugle.**", ""]
    return "\n".join(l)


def main() -> int:
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument("--verifier", action="store_true")
    args = a.parse_args()

    if not SNAPSHOT.exists():
        print(f"::error::Relevé Drive absent ({SNAPSHOT.relative_to(RACINE)}).")
        return 1

    texte = engendrer()
    if args.verifier:
        if not SORTIE.exists() or SORTIE.read_text(encoding="utf-8") != texte:
            print("::error::L'inventaire a dérivé. Relance "
                  "« python3 scripts/inventorier.py » et commite le résultat.")
            return 1
        print("  ✅ INVENTAIRE — à jour")
        return 0

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(texte, encoding="utf-8")
    print(f"  🔨 {SORTIE.relative_to(RACINE)} engendré — {len(texte.splitlines())} lignes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
