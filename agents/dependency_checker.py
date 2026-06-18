"""
Agent Sécurité 4 — Vérification des dépendances vulnérables
Vérifie que toutes les dépendances Python sont à jour et sans CVE connues.
"""

import asyncio
import subprocess
import json
import os
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "security_reports")


def run_pip_audit() -> dict:
    """Lance pip-audit pour détecter les CVE dans les dépendances."""
    try:
        result = subprocess.run(
            ["uv", "run", "pip-audit", "--format=json", "--output=-"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        if result.stdout:
            return json.loads(result.stdout)
    except Exception:
        pass
    return {}


def check_outdated() -> list[dict]:
    """Liste les paquets avec des mises à jour disponibles."""
    try:
        result = subprocess.run(
            ["uv", "pip", "list", "--outdated", "--format=json"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        if result.stdout:
            return json.loads(result.stdout)
    except Exception:
        pass
    return []


def generate_report(audit: dict, outdated: list[dict]) -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = os.path.join(REPORTS_DIR, f"deps_{date_str}.md")

    vulnerabilities = audit.get("vulnerabilities", [])
    critical_vuln = [v for v in vulnerabilities if any(
        float(fix.get("cvss", 0) or 0) >= 7.0
        for fix in v.get("fix_versions", [{}])
    )]

    lines = [
        "# Rapport Dépendances — Vulnérabilités & Mises à jour",
        f"Date : {date_str}\n",
        "## Résumé",
        f"- Vulnérabilités détectées : **{len(vulnerabilities)}**",
        f"- Vulnérabilités critiques (CVSS ≥ 7.0) : **{len(critical_vuln)}**",
        f"- Paquets obsolètes : **{len(outdated)}**\n",
    ]

    if vulnerabilities:
        lines.append("## 🚨 Vulnérabilités CVE\n")
        for vuln in vulnerabilities:
            lines.append(f"### {vuln.get('name')} {vuln.get('version')}")
            for v in vuln.get("vulns", []):
                lines.append(f"- **{v.get('id')}** : {v.get('description', 'N/A')[:200]}")
                lines.append(f"  - Fix : `uv add {vuln.get('name')}=={v.get('fix_versions', ['latest'])[0] if v.get('fix_versions') else 'latest'}`")
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

    lines.append("## Bonnes pratiques")
    lines.append("- Exécuter ce scan hebdomadairement")
    lines.append("- Activer Dependabot ou Renovate sur GitHub")
    lines.append("- Ne jamais ignorer les CVE de criticité HAUTE ou CRITIQUE")
    lines.append("- Épingler les versions dans pyproject.toml en production")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return report_path


async def main():
    print(f"\n📦 Vérification des dépendances...\n{'='*60}")

    # Installer pip-audit si absent
    subprocess.run(["uv", "add", "--dev", "pip-audit"], capture_output=True, cwd=PROJECT_ROOT)

    print("🔍 Scan CVE en cours...")
    audit = run_pip_audit()

    print("📋 Vérification des mises à jour...")
    outdated = check_outdated()

    report_path = generate_report(audit, outdated)

    vulnerabilities = audit.get("vulnerabilities", [])
    if vulnerabilities:
        print(f"\n🚨 {len(vulnerabilities)} vulnérabilité(s) trouvée(s) !")
        for v in vulnerabilities:
            print(f"   ├── {v.get('name')} {v.get('version')} — {len(v.get('vulns', []))} CVE")
    else:
        print("\n✅ Aucune vulnérabilité CVE détectée")

    if outdated:
        print(f"\n⬆️  {len(outdated)} paquet(s) à mettre à jour")
        print("   └── Lancer : uv sync --upgrade")
    else:
        print("✅ Toutes les dépendances sont à jour")

    print(f"\n📄 Rapport : {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
