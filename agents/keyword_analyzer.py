"""
Agent 1 — Analyse automatique des mots-clés
Analyse un mot-clé cible : volume, concurrence, potentiel SEO, mots-clés associés,
Core Web Vitals, E-E-A-T, SERP composition, gap analysis.
"""

import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

VALID_LANGUAGES = {"fr", "en", "es", "de", "it", "pt", "nl", "ar", "zh", "ja", "ko", "ru", "tr", "pl"}


async def analyze_keyword(keyword: str, langue: str = "fr") -> None:
    if not keyword or len(keyword.strip()) < 2:
        print("❌ Mot-clé invalide (trop court)")
        return
    if langue not in VALID_LANGUAGES:
        print(f"⚠️ Langue '{langue}' non reconnue, utilisation de 'fr'")
        langue = "fr"

    keyword_safe = keyword.replace('"', '\\"').replace('\n', ' ').strip()

    prompt = f"""
Tu es un expert SEO senior (OWASP, Google Quality Rater Guidelines). Analyse le mot-clé suivant pour une stratégie de contenu rentable :

Mot-clé cible : "{keyword_safe}"
Langue cible  : {langue}

Fournis une analyse complète et actionnable :
1. **Potentiel de trafic** — volume mensuel desktop/mobile, saisonnalité, CPC moyen
2. **Intention de recherche** — micro-intents (informationnelle, transactionnelle, navigationnelle, commercial investigation), query modifiers (best, comparison, 2026, local, DIY...)
3. **SERP Composition** — % blogs / e-commerce / actualités / featured snippets / vidéos dans le top 10
4. **10 mots-clés longue traîne** — avec volume, KD et priorité
5. **Analyse de la concurrence** — DA/PA des top 3, gap analysis (ce qu'ils manquent), profil de backlinks
6. **E-E-A-T requis** — niveau d'expertise, citations, sources, avis attendus pour ranker
7. **Core Web Vitals** — LCP/CLS/FID moyens des top concurrents, impact sur le ranking
8. **Recommandation de contenu** — format, structure H1-H6, longueur, schema markup recommandé
9. **Potentiel de monétisation** — affiliation, publicité, lead gen, programmes spécifiques avec commissions
10. **Score global** — /10 avec justification et plan d'action 90 jours

Présente les résultats de façon structurée avec des tableaux Markdown.
"""
    print(f"\n🔍 Analyse du mot-clé : '{keyword_safe}' [{langue}]\n{'='*60}")
    try:
        async with asyncio.timeout(60):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            print(block.text)
    except asyncio.TimeoutError:
        print(f"❌ Timeout : l'analyse du mot-clé '{keyword_safe}' a dépassé 60 secondes")
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse : {type(e).__name__}: {e}")


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
