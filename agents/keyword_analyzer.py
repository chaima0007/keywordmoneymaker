"""
Agent 1 — Analyse automatique des mots-clés
Analyse un mot-clé cible : volume, concurrence, potentiel SEO, mots-clés associés.
"""

import asyncio
from claude_code_sdk import query, ClaudeCodeOptions


async def analyze_keyword(keyword: str, langue: str = "fr") -> None:
    prompt = f"""
Tu es un expert SEO. Analyse le mot-clé suivant pour une stratégie de contenu rentable :

Mot-clé cible : "{keyword}"
Langue cible  : {langue}

Fournis une analyse complète :
1. **Potentiel de trafic** — estimation du volume mensuel et de la difficulté
2. **Intention de recherche** — informationnelle, transactionnelle ou navigationnelle
3. **Mots-clés associés** — 10 variations longue traîne à cibler
4. **Analyse de la concurrence** — type de pages qui rankent (blogs, e-commerce, etc.)
5. **Recommandation de contenu** — type d'article, angle, longueur idéale
6. **Potentiel de monétisation** — affiliation, publicité, lead gen, etc.
7. **Score global** — /10 avec justification

Présente les résultats de façon structurée et actionnable.
"""
    print(f"\n🔍 Analyse du mot-clé : '{keyword}' [{langue}]\n{'='*60}")
    async for message in query(
        prompt=prompt,
        options=ClaudeCodeOptions(
            allowed_tools=[],  # Pas d'accès fichiers — analyse pure
        ),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)


async def main():
    keywords = [
        ("gagner de l'argent en ligne", "fr"),
        ("make money with SEO", "en"),
        ("générateur d'articles SEO", "fr"),
    ]
    for keyword, langue in keywords:
        await analyze_keyword(keyword, langue)
        print()


if __name__ == "__main__":
    asyncio.run(main())
