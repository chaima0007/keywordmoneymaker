"""
Agent Sécurité 2 — Détection de secrets et fuites de données
Scanne le dépôt git (historique inclus) pour trouver des clés API,
mots de passe, tokens et données personnelles accidentellement commités.
"""

import asyncio
import os
import re
import subprocess
from datetime import datetime

SECRETS_PATTERNS = {
    "Clé API générique":      r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']?([A-Za-z0-9_\-]{16,})',
    "Token Bearer":           r'(?i)bearer\s+([A-Za-z0-9\-_\.]{20,})',
    "Clé AWS":               r'(?i)(AKIA|ASIA)[A-Z0-9]{16}',
    "Secret AWS":            r'(?i)aws[_-]?secret[_-]?access[_-]?key\s*[=:]\s*["\']?([A-Za-z0-9+/]{40})',
    "Clé Anthropic":         r'(?i)anthropic[_-]?api[_-]?key\s*[=:]\s*["\']?(sk-ant-[A-Za-z0-9\-]{40,})',
    "Clé OpenAI":            r'(?i)(openai[_-]?api[_-]?key|OPENAI_API_KEY)\s*[=:]\s*["\']?(sk-[A-Za-z0-9]{40,})',
    "Mot de passe":          r'(?i)(password|passwd|pwd|mot[_-]?de[_-]?passe)\s*[=:]\s*["\']?([^\s"\']{8,})',
    "Token GitHub":          r'(?i)(gh[pousr]_[A-Za-z0-9]{36}|github[_-]?token\s*[=:]\s*["\']?[A-Za-z0-9_]{20,})',
    "Clé privée":            r'-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----',
    "Email exposé":          r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "URL avec credentials":  r'(?i)(https?|ftp)://[^:@\s]+:[^:@\s]+@[^\s]+',
    "JWT Token":             r'eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+',
    "Clé Stripe":            r'(?i)(sk|pk)_(test|live)_[A-Za-z0-9]{24,}',
    "Webhook URL":           r'(?i)webhook[_-]?url\s*[=:]\s*["\']?(https://[^\s"\']+)',
}

IGNORE_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".mypy_cache"}
IGNORE_FILES = {"uv.lock", "poetry.lock", "package-lock.json"}
SAFE_EMAILS = {"noreply@anthropic.com", "retrouvetonsmile@gmail.com"}

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "security_reports")


def scan_file(filepath: str) -> list[dict]:
    findings = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            for secret_type, pattern in SECRETS_PATTERNS.items():
                matches = re.findall(pattern, line)
                if matches:
                    match_val = matches[0] if isinstance(matches[0], str) else matches[0][-1]
                    if secret_type == "Email exposé" and match_val in SAFE_EMAILS:
                        continue
                    findings.append({
                        "file": filepath,
                        "line": i,
                        "type": secret_type,
                        "snippet": line.strip()[:120],
                    })
    except Exception:
        pass
    return findings


def scan_git_history() -> list[str]:
    """Cherche des secrets dans l'historique git."""
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--oneline", "--diff-filter=A", "-p", "--", "*.env", "*.key", "*.pem"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        return result.stdout.splitlines() if result.stdout else []
    except Exception:
        return []


def generate_report(all_findings: list[dict]) -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = os.path.join(REPORTS_DIR, f"secrets_scan_{date_str}.md")

    critical = [f for f in all_findings if f["type"] not in ("Email exposé",)]
    info = [f for f in all_findings if f["type"] == "Email exposé"]

    lines = [
        f"# Rapport de Scan — Secrets & Fuites de Données",
        f"Date : {date_str}  |  Projet : {PROJECT_ROOT}\n",
        f"## Résumé",
        f"- Fichiers scannés : voir ci-dessous",
        f"- **Secrets critiques détectés : {len(critical)}**",
        f"- Emails exposés : {len(info)}",
        f"- Historique git : analysé\n",
    ]

    if critical:
        lines.append("## ⚠️ Secrets Critiques\n")
        for f in critical:
            rel = os.path.relpath(f["file"], PROJECT_ROOT)
            lines.append(f"### {f['type']}")
            lines.append(f"- Fichier : `{rel}` — Ligne {f['line']}")
            lines.append(f"- Extrait : `{f['snippet']}`")
            lines.append(f"- **Action requise : supprimer, révoquer et renouveler immédiatement**\n")
    else:
        lines.append("## ✅ Aucun secret critique détecté\n")

    if info:
        lines.append("## ℹ️ Emails détectés\n")
        seen = set()
        for f in info:
            email_match = re.search(SECRETS_PATTERNS["Email exposé"], f["snippet"])
            if email_match:
                email = email_match.group(0)
                if email not in seen:
                    seen.add(email)
                    rel = os.path.relpath(f["file"], PROJECT_ROOT)
                    lines.append(f"- `{email}` dans `{rel}` ligne {f['line']}")

    lines.append("\n## Recommandations\n")
    lines.append("1. Utiliser un fichier `.env` (jamais commité) pour toutes les clés")
    lines.append("2. Ajouter `.env` et `*.key` dans `.gitignore`")
    lines.append("3. Utiliser `git-secrets` ou `gitleaks` en pre-commit hook")
    lines.append("4. Révoquer immédiatement tout secret exposé dans l'historique git")
    lines.append("5. Utiliser un gestionnaire de secrets (Vault, AWS Secrets Manager)")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return report_path


async def main():
    print(f"\n🔍 Scan de secrets — {PROJECT_ROOT}\n{'='*60}")
    all_findings = []
    scanned = 0

    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname in IGNORE_FILES:
                continue
            fpath = os.path.join(root, fname)
            findings = scan_file(fpath)
            all_findings.extend(findings)
            scanned += 1

    print(f"📁 {scanned} fichiers scannés")

    git_history = scan_git_history()
    if git_history:
        print(f"⚠️  Historique git : des fichiers sensibles ont été détectés dans les commits passés")

    report_path = generate_report(all_findings)

    critical = [f for f in all_findings if f["type"] not in ("Email exposé",)]
    if critical:
        print(f"\n🚨 {len(critical)} secret(s) critique(s) trouvé(s) !")
        for f in critical:
            rel = os.path.relpath(f["file"], PROJECT_ROOT)
            print(f"   ├── [{f['type']}] {rel}:{f['line']}")
    else:
        print("\n✅ Aucun secret critique détecté dans le code source")

    print(f"\n📄 Rapport complet : {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
