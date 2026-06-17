"""
Agent 3 — Surveillance et optimisation du contenu
Analyse le contenu existant, détecte les faiblesses SEO et applique les corrections.
"""

import asyncio
import os
from claude_code_sdk import query, ClaudeCodeOptions


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")


async def optimize_content(file_path: str) -> None:
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
        print(f"❌ Fichier introuvable : {abs_path}")
        return

    prompt = f"""
Tu es un expert SEO on-page et copywriter. Analyse et optimise le fichier suivant :

Fichier : {abs_path}

Effectue les actions suivantes dans l'ordre :

1. **Lecture** — Lis le fichier avec l'outil Read
2. **Audit SEO** — Identifie :
   - Balises title, meta description, H1-H6 manquantes ou non optimisées
   - Densité de mots-clés (trop faible ou trop élevée)
   - Contenu trop court ou mal structuré
   - Liens internes manquants
   - Textes alternatifs d'images absents
   - Appels à l'action (CTA) faibles ou absents
3. **Score SEO** — Note le contenu /100 avec détail par critère
4. **Optimisation** — Applique les corrections prioritaires directement dans le fichier avec Edit :
   - Améliore les titres et meta descriptions
   - Renforce les CTAs
   - Ajoute les attributs manquants
5. **Rapport de modifications** — Liste ce qui a été changé et pourquoi

Sois précis, efficace et concentre-toi sur les changements à fort impact SEO.
"""

    filename = os.path.basename(file_path)
    print(f"\n⚙️  Optimisation : {filename}\n{'='*60}")

    async for message in query(
        prompt=prompt,
        options=ClaudeCodeOptions(
            allowed_tools=["Read", "Edit"],
        ),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)

    print(f"\n✅ Optimisation terminée : {filename}")


async def optimize_all() -> None:
    html_files = []
    for root, _, files in os.walk(PROJECT_ROOT):
        if ".git" in root or "agents" in root:
            continue
        for f in files:
            if f.endswith((".html", ".htm")):
                html_files.append(os.path.join(root, f))

    if not html_files:
        print("❌ Aucun fichier HTML trouvé dans le projet.")
        return

    print(f"🔎 {len(html_files)} fichier(s) HTML détecté(s)")
    for path in html_files:
        await optimize_content(path)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        asyncio.run(optimize_content(sys.argv[1]))
    else:
        asyncio.run(optimize_all())
