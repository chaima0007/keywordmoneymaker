"""
Lance les trois agents en séquence.
Usage : python agents/run_all.py
"""

import asyncio
from keyword_analyzer import analyze_keyword
from report_generator import generate_report
from content_optimizer import optimize_all
from linkedin_cv_agent import main as linkedin_cv_main


async def main():
    print("🚀 KeywordMoneyMaker — Lancement des agents\n")

    print("━" * 60)
    print("AGENT 1 — Analyse des mots-clés")
    print("━" * 60)
    await analyze_keyword("générateur d'articles SEO", "fr")

    print("\n" + "━" * 60)
    print("AGENT 2 — Génération du rapport")
    print("━" * 60)
    await generate_report()

    print("\n" + "━" * 60)
    print("AGENT 3 — Optimisation du contenu")
    print("━" * 60)
    await optimize_all()

    print("\n" + "━" * 60)
    print("AGENT 4 — Documentation LinkedIn & CV")
    print("━" * 60)
    await linkedin_cv_main()

    print("\n✅ Tous les agents ont terminé.")


if __name__ == "__main__":
    asyncio.run(main())
