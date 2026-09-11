#!/usr/bin/env python3
"""
audit_code_sur.py — Contrôle « code sûr et non pollué » (défensif uniquement).
================================================================================
Cinq contrôles indépendants, exécutables hors ligne, sans dépendance externe :

  1. SECRETS      — aucune clé/token en dur dans le dépôt (les .example sont ignorés).
  2. DÉPENDANCES  — déclarées, épinglées, sans source exotique (git+http, URL directe).
  3. ACTIONS CI   — actions GitHub épinglées par SHA (une étiquette mobile peut être
                    réécrite par un attaquant : c'est le vecteur d'attaque n°1 du CI).
  4. CODE À RISQUE— exécution de contenu distant (curl|bash, eval/exec sur données
                    téléchargées, pickle distant, shell=True avec variable).
  5. LICENCES     — les dépendances doivent être sous licence permissive connue ;
                    toute licence copyleft forte est SIGNALÉE (contamine un code fermé).

HONNÊTETÉ : ce script détecte des motifs connus. Il ne remplace ni pip-audit (CVE
publiées) ni une revue humaine. Ce qu'il ne peut pas vérifier est déclaré, jamais
supposé conforme. Aucune action offensive, aucune tentative d'intrusion.

Sortie : rapport lisible + code 1 si un contrôle BLOQUANT échoue (utilisable en CI).
Usage  : python3 scripts/audit_code_sur.py [--json]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}
# Fichiers d'exemple : des placeholders y sont normaux et attendus.
FICHIERS_EXEMPLE = re.compile(r"(\.example$|\.sample$|_example\.|\.md$)")

# ── 1. SECRETS ───────────────────────────────────────────────────────────────
# Motifs de credentials réels (préfixes documentés publiquement par les éditeurs).
MOTIFS_SECRETS = [
    ("clé Anthropic",      re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("clé OpenAI",         re.compile(r"\bsk-[A-Za-z0-9]{32,}\b")),
    ("token GitHub",       re.compile(r"\b(ghp|gho|ghs|ghu|github_pat)_[A-Za-z0-9_]{20,}")),
    ("clé AWS",            re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("clé Google",         re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("token Slack",        re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}")),
    ("clé privée",         re.compile(r"-----BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("clé Stripe live",    re.compile(r"\b(sk|rk)_live_[A-Za-z0-9]{20,}\b")),
    ("mot de passe en dur", re.compile(r"(?i)(password|passwd|mot_de_passe)\s*[=:]\s*[\"'][^\"'\s]{8,}[\"']")),
]
# Valeurs manifestement factices : à ne pas signaler.
PLACEHOLDER = re.compile(r"(?i)(your_|xxx|placeholder|exemple|example|changeme|à_remplir|dummy|fake|test_?key)")

# ── 5. LICENCES ──────────────────────────────────────────────────────────────
LICENCES_PERMISSIVES = {"MIT", "APACHE-2.0", "APACHE 2.0", "BSD-2-CLAUSE", "BSD-3-CLAUSE",
                        "BSD", "ISC", "PYTHON-2.0", "PSF", "UNLICENSE", "CC0-1.0", "ZLIB"}
LICENCES_COPYLEFT_FORT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "AGPL", "GPL", "SSPL-1.0", "SSPL"}

# ── 4. CODE À RISQUE ─────────────────────────────────────────────────────────
MOTIFS_RISQUE = [
    ("exécution d'un script téléchargé (curl|bash)",
     re.compile(r"curl[^\n|]{0,120}\|\s*(sudo\s+)?(ba)?sh")),
    ("exécution d'un script téléchargé (wget|sh)",
     re.compile(r"wget[^\n|]{0,120}\|\s*(sudo\s+)?(ba)?sh")),
    ("eval/exec sur du contenu téléchargé",
     re.compile(r"(?s)(eval|exec)\s*\(\s*[^)]{0,200}(requests\.get|urlopen|urlretrieve|fetch\()")),
    ("désérialisation pickle d'une source distante",
     re.compile(r"(?s)pickle\.loads?\s*\(\s*[^)]{0,200}(requests\.get|urlopen)")),
    ("shell=True avec une variable (injection de commande)",
     re.compile(r"subprocess\.[a-z_]+\([^)]{0,200}shell\s*=\s*True[^)]{0,200}\)")),
    ("désactivation de la vérification TLS",
     re.compile(r"(verify\s*=\s*False|CURLOPT_SSL_VERIFYPEER\s*,\s*(0|false)|rejectUnauthorized:\s*false)")),
]


def fichiers_du_depot():
    for base, dirs, noms in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for n in noms:
            p = os.path.join(base, n)
            if os.path.getsize(p) > 2_000_000:      # binaires/gros fichiers : hors périmètre texte
                continue
            yield p


def lire(p):
    try:
        with open(p, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


def controle_secrets():
    trouves = []
    for p in fichiers_du_depot():
        rel = os.path.relpath(p, ROOT)
        if FICHIERS_EXEMPLE.search(rel):
            continue
        contenu = lire(p)
        for nom, motif in MOTIFS_SECRETS:
            for m in motif.finditer(contenu):
                extrait = m.group(0)
                if PLACEHOLDER.search(extrait):
                    continue
                ligne = contenu[:m.start()].count("\n") + 1
                trouves.append({"fichier": rel, "ligne": ligne, "type": nom,
                                "extrait": extrait[:12] + "…"})   # jamais le secret entier
    return {"controle": "secrets", "bloquant": True, "anomalies": trouves,
            "resume": f"{len(trouves)} secret(s) potentiel(s) en dur"}


def controle_dependances():
    anomalies, deps = [], []
    py = os.path.join(ROOT, "pyproject.toml")
    if os.path.exists(py):
        contenu = lire(py)
        bloc = re.search(r"dependencies\s*=\s*\[(.*?)\]", contenu, re.DOTALL)
        if bloc:
            for ligne in re.findall(r"[\"']([^\"']+)[\"']", bloc.group(1)):
                deps.append(ligne)
                if re.search(r"(git\+|https?://|file://)", ligne):
                    anomalies.append({"dependance": ligne,
                                      "risque": "source non-PyPI (dépôt/URL directe) — provenance à vérifier à la main"})
                elif not re.search(r"[=><~!]=?\s*\d", ligne):
                    anomalies.append({"dependance": ligne,
                                      "risque": "version non contrainte — une mise à jour malveillante entrerait sans revue"})
    lock = os.path.join(ROOT, "uv.lock")
    verrou = "uv.lock présent (versions figées)" if os.path.exists(lock) else "AUCUN fichier de verrouillage"
    if not os.path.exists(lock):
        anomalies.append({"dependance": "(global)", "risque": "aucun lockfile : builds non reproductibles"})
    return {"controle": "dependances", "bloquant": False, "anomalies": anomalies,
            "resume": f"{len(deps)} dépendance(s) déclarée(s) · {verrou} · {len(anomalies)} point(s) d'attention"}


def controle_actions_ci():
    anomalies, total = [], 0
    wf = os.path.join(ROOT, ".github", "workflows")
    if not os.path.isdir(wf):
        return {"controle": "actions_ci", "bloquant": False, "anomalies": [],
                "resume": "aucun workflow GitHub Actions"}
    for n in sorted(os.listdir(wf)):
        if not n.endswith((".yml", ".yaml")):
            continue
        contenu = lire(os.path.join(wf, n))
        for m in re.finditer(r"uses:\s*([^\s@]+)@([^\s#]+)", contenu):
            total += 1
            action, ref = m.group(1), m.group(2)
            if action.startswith("./"):
                continue                                   # action locale : pas de tiers
            if not re.fullmatch(r"[0-9a-f]{40}", ref):
                anomalies.append({"workflow": n, "action": f"{action}@{ref}",
                                  "risque": "référence mobile (étiquette/branche) : le code exécuté peut changer sans votre accord"})
    return {"controle": "actions_ci", "bloquant": False, "anomalies": anomalies,
            "resume": f"{total} action(s) tierce(s) · {len(anomalies)} non épinglée(s) par SHA"}


def controle_code_risque():
    trouves = []
    for p in fichiers_du_depot():
        rel = os.path.relpath(p, ROOT)
        if not rel.endswith((".py", ".js", ".ts", ".sh", ".yml", ".yaml", ".html")):
            continue
        if rel.startswith("scripts/audit_code_sur.py"):     # ce fichier contient les motifs eux-mêmes
            continue
        contenu = lire(p)
        for nom, motif in MOTIFS_RISQUE:
            for m in motif.finditer(contenu):
                trouves.append({"fichier": rel,
                                "ligne": contenu[:m.start()].count("\n") + 1,
                                "motif": nom})
    return {"controle": "code_a_risque", "bloquant": True, "anomalies": trouves,
            "resume": f"{len(trouves)} motif(s) d'exécution/transport à risque"}


def controle_licences():
    """Licences des dépendances INSTALLÉES (si l'environnement est disponible).
    Sans environnement installé, le contrôle est déclaré NON EXÉCUTÉ — jamais « conforme »."""
    try:
        from importlib import metadata
    except ImportError:
        return {"controle": "licences", "bloquant": False, "anomalies": [],
                "resume": "NON EXÉCUTÉ (importlib.metadata indisponible)", "execute": False}
    attendues = []
    py = os.path.join(ROOT, "pyproject.toml")
    if os.path.exists(py):
        bloc = re.search(r"dependencies\s*=\s*\[(.*?)\]", lire(py), re.DOTALL)
        if bloc:
            attendues = [re.split(r"[=><~!\[]", d)[0].strip()
                         for d in re.findall(r"[\"']([^\"']+)[\"']", bloc.group(1))]
    anomalies, examinees = [], 0
    for nom in attendues:
        try:
            md = metadata.metadata(nom)
        except Exception:
            anomalies.append({"paquet": nom, "licence": "?",
                              "risque": "paquet non installé ici — licence NON VÉRIFIÉE (à contrôler avant usage)"})
            continue
        examinees += 1
        lic = (md.get("License") or "").strip()
        if not lic or lic.upper() in {"UNKNOWN", "NONE"}:
            classifiers = md.get_all("Classifier") or []
            lic = next((c.split("::")[-1].strip() for c in classifiers if c.startswith("License ::")), "")
        norm = lic.upper().strip()
        if any(c in norm for c in LICENCES_COPYLEFT_FORT):
            anomalies.append({"paquet": nom, "licence": lic,
                              "risque": "copyleft fort : peut obliger à publier VOTRE code — à valider avant diffusion"})
        elif not any(p in norm for p in LICENCES_PERMISSIVES):
            anomalies.append({"paquet": nom, "licence": lic or "(vide)",
                              "risque": "licence non reconnue comme permissive — à lire à la main"})
    return {"controle": "licences", "bloquant": False, "anomalies": anomalies, "execute": True,
            "resume": f"{examinees}/{len(attendues)} paquet(s) examiné(s) · {len(anomalies)} à vérifier"}


def main():
    resultats = [controle_secrets(), controle_dependances(), controle_actions_ci(),
                 controle_code_risque(), controle_licences()]
    bloquants = [r for r in resultats if r["bloquant"] and r["anomalies"]]

    if "--json" in sys.argv:
        print(json.dumps({"resultats": resultats, "verdict": "ROUGE" if bloquants else "VERT"},
                         ensure_ascii=False, indent=2))
        return 1 if bloquants else 0

    print("═" * 72)
    print("  AUDIT « CODE SÛR ET NON POLLUÉ » — contrôle défensif")
    print("═" * 72)
    for r in resultats:
        etat = "❌" if (r["bloquant"] and r["anomalies"]) else ("⚠️ " if r["anomalies"] else "✅")
        print(f"\n{etat} {r['controle'].upper()} — {r['resume']}")
        for a in r["anomalies"][:15]:
            detail = " · ".join(f"{k}: {v}" for k, v in a.items())
            print(f"     – {detail}")
        if len(r["anomalies"]) > 15:
            print(f"     … et {len(r['anomalies']) - 15} autre(s)")
    print("\n" + "─" * 72)
    if bloquants:
        print("  VERDICT : ❌ ROUGE — corriger les contrôles bloquants avant de pousser.")
    else:
        print("  VERDICT : ✅ VERT sur les contrôles bloquants (secrets, code à risque).")
        print("  Rappel honnête : ceci détecte des motifs connus ; pip-audit (CVE) et")
        print("  une relecture humaine restent nécessaires avant d'intégrer du code tiers.")
    print("─" * 72)
    return 1 if bloquants else 0


if __name__ == "__main__":
    sys.exit(main())
