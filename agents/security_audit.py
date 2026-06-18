"""
Agent Sécurité 1 — Audit de vulnérabilités du code
Scanne le projet à la recherche de failles : XSS, injection, secrets exposés,
mauvaises configurations, dépendances vulnérables.
"""

import asyncio
import os
import subprocess
from datetime import datetime
from claude_agent_sdk import query, ClaudeAgentOptions

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "security_reports")


async def run_audit() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = os.path.join(REPORTS_DIR, f"audit_{date_str}.md")

    prompt = f"""
Tu es un expert en cybersécurité offensive et défensive (OWASP, SANS Top 25).

Effectue un audit de sécurité complet du projet situé dans : {PROJECT_ROOT}

Utilise les outils disponibles pour :

1. **Lire tous les fichiers du projet** (HTML, Python, JSON, config)
2. **Détecter les vulnérabilités critiques** :
   - XSS (Cross-Site Scripting) dans le HTML/JS
   - Injection (SQL, commande, code)
   - Secrets et clés API exposés dans le code
   - Informations sensibles dans les commentaires
   - Dépendances avec CVE connues
   - Mauvaises configurations de sécurité
   - CORS trop permissifs
   - Absence d'en-têtes de sécurité (CSP, HSTS, X-Frame-Options)
   - Formulaires sans protection CSRF
   - Données personnelles exposées
3. **Classer chaque faille** par criticité : CRITIQUE / HAUTE / MOYENNE / FAIBLE / INFO
4. **Proposer un correctif précis** pour chaque vulnérabilité
5. **Générer un rapport Markdown** et le sauvegarder dans : {report_path}

Format du rapport :
# Rapport d'Audit Sécurité — {date_str}
## Résumé Exécutif (score de sécurité /100)
## Vulnérabilités par criticité
## Plan de remédiation priorisé
## Bonnes pratiques recommandées
"""

    print(f"\n🔐 Audit de sécurité en cours...\n{'='*60}")
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Write"],
        ),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)

    print(f"\n✅ Rapport sauvegardé : {report_path}")
    return report_path


if __name__ == "__main__":
    asyncio.run(run_audit())
