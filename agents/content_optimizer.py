"""
Agent 3 — Surveillance et optimisation du contenu
Analyse le contenu HTML, détecte les faiblesses SEO et applique les corrections.
"""

import asyncio
import os
from pathlib import Path
from typing import Optional
from claude_agent_sdk import query, ClaudeAgentOptions

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
MAX_FILE_SIZE = 5_000_000  # 5 MB
IGNORE_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".mypy_cache", "agents"}


async def optimize_content(file_path: str) -> Optional[str]:
    try:
        path = Path(file_path).resolve()

        # Protection path traversal — fichier doit être dans PROJECT_ROOT
        if not str(path).startswith(str(PROJECT_ROOT)):
            print(f"❌ Chemin invalide (hors du projet) : {file_path}")
            return None
        if not path.exists() or not path.is_file():
            print(f"❌ Fichier introuvable : {path}")
            return None
        if path.stat().st_size > MAX_FILE_SIZE:
            print(f"❌ Fichier trop volumineux (>{MAX_FILE_SIZE/1e6}MB) : {path.name}")
            return None
        if path.suffix.lower() not in {".html", ".htm"}:
            print(f"❌ Type non supporté : {path.suffix}")
            return None
    except Exception as e:
        print(f"❌ Validation du chemin : {e}")
        return None

    prompt = f"""
Tu es un expert SEO on-page. Analyse et optimise le fichier HTML suivant :
Fichier : {path}

Effectue ces actions dans l'ordre :
1. **Lire** le fichier avec Read
2. **Audit SEO on-page** :
   - Title (< 60 chars, keyword en début, unique)
   - Meta description (150-160 chars, CTA, keyword)
   - H1 unique, < 60 chars, pas de <br> dedans
   - Hiérarchie H1→H2→H3 correcte
   - Schema.org : SoftwareApplication, FAQPage si applicable, BreadcrumbList
   - Hreflang : présent pour toutes les langues supportées
   - Open Graph : og:image 1200x630px présent
   - Twitter Cards : twitter:image présent
   - Alt text et aria-label sur tous les éléments visuels (emojis inclus)
   - Core Web Vitals : recommandations lazy loading, optimisation images
   - E-E-A-T : sources, auteur, date, signaux d'autorité
3. **Score SEO** /100 avec détail par critère
4. **Appliquer corrections** avec Edit (priorité haute seulement)
5. **Rapport** : liste des changements et justifications
"""

    filename = path.name
    print(f"\n⚙️  Optimisation : {filename}\n{'='*60}")

    try:
        async with asyncio.timeout(120):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=["Read", "Edit"]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            print(block.text)
    except asyncio.TimeoutError:
        print(f"❌ Timeout : optimisation de {filename} >120s")
        return None
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")
        return None

    print(f"\n✅ Optimisation terminée : {filename}")
    return str(path)


async def optimize_all() -> None:
    html_files = [
        f for f in PROJECT_ROOT.rglob("*.html")
        if not any(part in IGNORE_DIRS for part in f.parts)
    ]

    if not html_files:
        print("❌ Aucun fichier HTML trouvé dans le projet.")
        return

    print(f"🔎 {len(html_files)} fichier(s) HTML détecté(s)")
    for path in html_files:
        await optimize_content(str(path))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        asyncio.run(optimize_content(sys.argv[1]))
    else:
        asyncio.run(optimize_all())
