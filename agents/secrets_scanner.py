"""
Agent Sécurité 2 — Détection de secrets et fuites de données
Scanne le dépôt git (historique inclus) pour trouver des clés API,
mots de passe, tokens et données personnelles accidentellement commités.
Patterns étendus suite à l'audit expert sécurité.
"""

import asyncio
import logging
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

SECRETS_PATTERNS = {
    "Clé API générique":        r'(?i)(?:api[_-]?key|apikey)\s*[=:]\s*["\']([A-Za-z0-9_\-]{20,})["\']',
    "Token Bearer":             r'(?i)bearer\s+([A-Za-z0-9\-_\.]{20,})',
    "Clé AWS Access":           r'(?i)(AKIA|ASIA)[A-Z0-9]{16}',
    "Secret AWS":               r'(?i)aws[_-]?secret[_-]?access[_-]?key\s*[=:]\s*["\']?([A-Za-z0-9+/]{40})',
    "Clé Anthropic":            r'(?i)anthropic[_-]?api[_-]?key\s*[=:]\s*["\']?(sk-ant-[A-Za-z0-9\-]{40,})',
    "Clé OpenAI":               r'(?i)(?:openai[_-]?api[_-]?key|OPENAI_API_KEY)\s*[=:]\s*["\']?(sk-[A-Za-z0-9]{40,})',
    "Token GitHub":             r'(?i)(?:gh[pousr]_[A-Za-z0-9]{36}|github[_-]?token\s*[=:]\s*["\']?[A-Za-z0-9_]{20,})',
    "Clé Stripe":               r'(?i)(?:sk|pk)_(?:test|live)_[A-Za-z0-9]{24,}',
    "Twilio SID":               r'(?i)(?:AC[a-z0-9]{32}|twilio[_-]?(?:account[_-]?sid|auth[_-]?token)\s*[=:]\s*["\']?[A-Za-z0-9]{32,})',
    "SendGrid":                 r'SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}',
    "Firebase/GCP":             r'(?:AIza[0-9A-Za-z_\-]{35})',
    "Slack Token":              r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[A-Za-z0-9\-_]{32}',
    "Clé privée":               r'-----BEGIN (?:RSA |EC |DSA |OPENSSH |PKCS8 )?PRIVATE KEY-----',
    "Mot de passe":             r'(?i)(?:password|passwd|pwd)\s*[=:]\s*["\']([^\s"\']{8,})["\']',
    "URL avec credentials":     r'(?i)(?:https?|ftp)://[A-Za-z0-9_\-\.]{3,}:[A-Za-z0-9_\-\.!$&]{4,}@[A-Za-z0-9\-\.]{4,}',
    "JWT Token":                r'eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}',
    "Webhook URL secret":       r'(?i)webhook[_-]?(?:url|secret)\s*[=:]\s*["\']?(https://[^\s"\']+)',
    "Email exposé":             r'\b[A-Za-z0-9._%+-]{3,}@[A-Za-z0-9.-]{3,}\.[A-Z|a-z]{2,}\b',
}

IGNORE_DIRS  = {".git", ".venv", "__pycache__", "node_modules", ".mypy_cache", "dist", "build"}
IGNORE_FILES = {"uv.lock", "poetry.lock", "package-lock.json"}
SAFE_EMAILS  = {"noreply@anthropic.com", "retrouvetonsmile@gmail.com"}
# Valeurs placeholder (faux positifs)
PLACEHOLDER_VALUES = {
    "your_anthropic_api_key_here", "your_composio_api_key_here",
    "your_linkedin_token_here", "your_api_key_here", "example", "changeme",
    "placeholder", "dummy", "test", "xxxx",
}
MAX_FILE_SIZE = 10_000_000  # 10 MB

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
REPORTS_DIR  = PROJECT_ROOT / "security_reports"


def is_placeholder(value: str) -> bool:
    v = value.lower().strip()
    return any(p in v for p in PLACEHOLDER_VALUES) or len(v) < 8


def scan_file(filepath: str) -> list[dict]:
    findings = []
    try:
        stat = os.stat(filepath)
        if stat.st_size > MAX_FILE_SIZE:
            logger.warning(f"Fichier trop grand, ignoré : {filepath}")
            return findings

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            for secret_type, pattern in SECRETS_PATTERNS.items():
                try:
                    matches = re.findall(pattern, line)
                    if not matches:
                        continue

                    match_val = matches[0] if isinstance(matches[0], str) else (matches[0][-1] if matches[0] else "")

                    if secret_type == "Email exposé" and match_val in SAFE_EMAILS:
                        continue
                    if is_placeholder(match_val):
                        continue

                    findings.append({
                        "file": filepath,
                        "line": i,
                        "type": secret_type,
                        "snippet": line.strip()[:120],
                    })
                except re.error as e:
                    logger.error(f"Regex invalide [{secret_type}]: {e}")
                    continue

    except UnicodeDecodeError:
        logger.debug(f"Encodage non-UTF8 : {filepath}")
    except PermissionError:
        logger.warning(f"Accès refusé : {filepath}")
    except Exception as e:
        logger.error(f"Erreur scan {filepath}: {type(e).__name__}: {e}")
    return findings


def scan_git_history() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--oneline", "--diff-filter=A", "-p",
             "--", "*.env", "*.key", "*.pem", "*.p12"],
            capture_output=True, text=True, cwd=str(PROJECT_ROOT), timeout=30
        )
        return result.stdout.splitlines() if result.stdout else []
    except subprocess.TimeoutExpired:
        logger.warning("git history scan timeout")
        return []
    except Exception as e:
        logger.warning(f"git history scan failed: {e}")
        return []


def generate_report(all_findings: list[dict]) -> str:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = REPORTS_DIR / f"secrets_scan_{date_str}.md"

    critical = [f for f in all_findings if f["type"] != "Email exposé"]
    info     = [f for f in all_findings if f["type"] == "Email exposé"]

    lines = [
        "# Rapport Scan — Secrets & Fuites de Données",
        f"Date : {date_str}  |  Projet : {PROJECT_ROOT}\n",
        "## Résumé",
        f"- **Secrets critiques détectés : {len(critical)}**",
        f"- Emails exposés : {len(info)}\n",
    ]

    if critical:
        lines.append("## ⚠️ Secrets Critiques\n")
        for f in critical:
            rel = os.path.relpath(f["file"], str(PROJECT_ROOT))
            lines += [
                f"### {f['type']}",
                f"- Fichier : `{rel}` — Ligne {f['line']}",
                f"- Extrait : `{f['snippet']}`",
                "- **Action : supprimer, révoquer et renouveler immédiatement**\n",
            ]
    else:
        lines.append("## ✅ Aucun secret critique détecté\n")

    if info:
        lines.append("## ℹ️ Emails détectés\n")
        seen: set[str] = set()
        for f in info:
            m = re.search(SECRETS_PATTERNS["Email exposé"], f["snippet"])
            if m and m.group(0) not in seen:
                seen.add(m.group(0))
                rel = os.path.relpath(f["file"], str(PROJECT_ROOT))
                lines.append(f"- `{m.group(0)}` dans `{rel}` ligne {f['line']}")

    lines += [
        "\n## Recommandations",
        "1. Utiliser un fichier `.env` (jamais commité) pour toutes les clés",
        "2. `.env` et `*.key` dans `.gitignore`",
        "3. Utiliser `gitleaks` en pre-commit hook",
        "4. Révoquer tout secret exposé dans l'historique git",
        "5. Gestionnaire de secrets en production (Vault, AWS Secrets Manager)",
    ]

    try:
        report_path.write_text("\n".join(lines), encoding="utf-8")
    except (OSError, IOError) as e:
        logger.error(f"Échec sauvegarde rapport : {e}")
    return str(report_path)


async def main():
    logging.basicConfig(level=logging.WARNING)
    print(f"\n🔍 Scan de secrets — {PROJECT_ROOT}\n{'='*60}")
    all_findings: list[dict] = []
    scanned = 0

    for root, dirs, files in os.walk(str(PROJECT_ROOT)):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname in IGNORE_FILES:
                continue
            findings = scan_file(os.path.join(root, fname))
            all_findings.extend(findings)
            scanned += 1

    print(f"📁 {scanned} fichiers scannés")

    git_lines = scan_git_history()
    if git_lines:
        print("⚠️  Historique git : fichiers sensibles détectés dans des commits passés")

    report_path = generate_report(all_findings)
    critical = [f for f in all_findings if f["type"] != "Email exposé"]

    if critical:
        print(f"\n🚨 {len(critical)} secret(s) critique(s) trouvé(s) !")
        for f in critical:
            rel = os.path.relpath(f["file"], str(PROJECT_ROOT))
            print(f"   ├── [{f['type']}] {rel}:{f['line']}")
    else:
        print("\n✅ Aucun secret critique détecté")

    print(f"\n📄 Rapport : {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
