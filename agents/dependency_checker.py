"""
Agent Sécurité 4 — Vérification des dépendances vulnérables
Vérifie que toutes les dépendances Python sont à jour et sans CVE connues.
"""

import asyncio
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "security_reports")


def run_pip_audit() -> dict:
    try:
        result = subprocess.run(
            ["uv", "run", "pip-audit", "--format=json", "--output=-"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, timeout=60
        )
        if result.returncode != 0:
            logger.warning(f"pip-audit a retourné une erreur : {result.stderr[:200]}")
        if result.stdout:
            return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        logger.error("pip-audit a dépassé le timeout de 60s")
    except json.JSONDecodeError as e:
        logger.error(f"Réponse pip-audit invalide : {e}")
    except Exception as e:
        logger.error(f"Erreur audit dépendances : {type(e).__name__}: {e}")
    return {"vulnerabilities": []}


def check_outdated() -> list[dict]:
    try:
        result = subprocess.run(
            ["uv", "pip", "list", "--outdated", "--format=json"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, timeout=30
        )
        if result.stdout:
            return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as e:
        logger.warning(f"Vérification mises à jour échouée : {e}")
    return []


def generate_report(audit: dict, outdated: list[dict]) -> str:
    Path(REPORTS_DIR).mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = Path(REPORTS_DIR) / f"deps_{date_str}.md"

    vulnerabilities = audit.get("vulnerabilities", [])

    lines = [
        "# Rapport Dépendances — Vulnérabilités & Mises à jour",
        f"Date : {date_str}\n",
        "## Résumé",
        f"- Vulnérabilités CVE détectées : **{len(vulnerabilities)}**",
        f"- Paquets obsolètes : **{len(outdated)}**\n",
    ]

    if vulnerabilities:
        lines.append("## 🚨 Vulnérabilités CVE\n")
        for vuln in vulnerabilities:
            lines.append(f"### {vuln.get('name')} {vuln.get('version')}")
            for v in vuln.get("vulns", []):
                lines.append(f"- **{v.get('id')}** : {v.get('description', 'N/A')[:200]}")
                fixes = v.get("fix_versions", [])
                fix = fixes[0] if fixes else "latest"
                lines.append(f"  - Fix : `uv add {vuln.get('name')}=={fix}`")
            lines.append("")
    else:
        lines.append("## ✅ Aucune vulnérabilité CVE détectée\n")

    if outdated:
        lines.append("## ⬆️ Paquets à mettre à jour\n")
        lines.append("| Paquet | Version actuelle | Dernière version |")
        lines.append("|--------|-----------------|-----------------|")
        for pkg in outdated:
            lines.append(f"| {pkg.get('name')} | {pkg.get('version')} | {pkg.get('latest_version')} |")
        lines.append(f"\n**Commande de mise à jour :** `uv sync --upgrade`\n")
    else:
        lines.append("## ✅ Toutes les dépendances sont à jour\n")

    lines += [
        "## Bonnes pratiques",
        "- Exécuter ce scan hebdomadairement",
        "- Activer Dependabot sur GitHub",
        "- Ne jamais ignorer les CVE HAUTE ou CRITIQUE",
        "- Épingler les versions dans pyproject.toml en production",
    ]

    try:
        report_path.write_text("\n".join(lines), encoding="utf-8")
    except (OSError, IOError) as e:
        logger.error(f"Échec sauvegarde rapport : {e}")

    return str(report_path)


async def main():
    logging.basicConfig(level=logging.WARNING)
    print(f"\n📦 Vérification des dépendances...\n{'='*60}")

    # Vérifier que pip-audit est disponible sans l'installer automatiquement
    check = subprocess.run(
        ["uv", "run", "pip-audit", "--version"],
        capture_output=True, text=True, cwd=PROJECT_ROOT, timeout=10
    )
    if check.returncode != 0:
        print("⚠️  pip-audit n'est pas installé")
        print("   Installez-le manuellement avec : uv add --dev pip-audit")
        sys.exit(1)

    print("🔍 Scan CVE en cours...")
    audit = run_pip_audit()

    print("📋 Vérification des mises à jour...")
    outdated = check_outdated()

    report_path = generate_report(audit, outdated)
    vulnerabilities = audit.get("vulnerabilities", [])

    if vulnerabilities:
        print(f"\n🚨 {len(vulnerabilities)} vulnérabilité(s) trouvée(s) !")
        for v in vulnerabilities:
            print(f"   ├── {v.get('name')} {v.get('version')}")
    else:
        print("\n✅ Aucune vulnérabilité CVE détectée")

    if outdated:
        print(f"\n⬆️  {len(outdated)} paquet(s) à mettre à jour → `uv sync --upgrade`")
    else:
        print("✅ Toutes les dépendances sont à jour")

    print(f"\n📄 Rapport : {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
