"""
Agent Sécurité 3 — Durcissement actif du code
Applique automatiquement les protections de sécurité :
- En-têtes HTTP de sécurité dans le HTML
- Protection XSS, Clickjacking, MIME sniffing
- Content Security Policy (CSP)
- Création du .gitignore sécurisé
- Création du fichier .env.example
"""

import asyncio
import os
from claude_agent_sdk import query, ClaudeAgentOptions

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


async def harden_project() -> None:
    prompt = f"""
Tu es un expert en sécurité web. Durcis le projet situé dans : {PROJECT_ROOT}

Effectue les actions suivantes dans l'ordre :

**1. Lire le fichier HTML principal** avec Read sur {PROJECT_ROOT}/keywordmoneymaker-index.html

**2. Ajouter les meta-tags de sécurité** dans le <head> si absents :
```html
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-XSS-Protection" content="1; mode=block">
<meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
<meta http-equiv="Permissions-Policy" content="geolocation=(), microphone=(), camera=()">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self';">
```

**3. Vérifier et corriger** tout attribut `target="_blank"` sans `rel="noopener noreferrer"`

**4. Créer un fichier .gitignore sécurisé** dans {PROJECT_ROOT}/.gitignore avec :
- .env, .env.*, *.env
- *.key, *.pem, *.p12, *.pfx
- secrets.*, credentials.*
- __pycache__/, .venv/, .mypy_cache/
- security_reports/ (ne pas commiter les rapports de vulnérabilités)
- *.log
- .DS_Store, Thumbs.db

**5. Créer un fichier .env.example** dans {PROJECT_ROOT}/.env.example montrant la structure
sans aucune vraie valeur :
```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
COMPOSIO_API_KEY=your_composio_api_key_here
LINKEDIN_ACCESS_TOKEN=your_linkedin_token_here
```

**6. Rapport final** : liste ce qui a été modifié/créé et le score de sécurité avant/après.
"""

    print(f"\n🛡️  Durcissement de sécurité en cours...\n{'='*60}")
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Write", "Glob"],
        ),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)

    print("\n✅ Durcissement terminé")


if __name__ == "__main__":
    asyncio.run(harden_project())
