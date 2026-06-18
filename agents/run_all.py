"""
Orchestrateur — Lance tous les agents en séquence avec gestion d'erreurs.
Usage : uv run python agents/run_all.py
"""

import asyncio
import sys
import traceback
from pathlib import Path

# Ajouter le répertoire agents au path Python
sys.path.insert(0, str(Path(__file__).parent))

from keyword_analyzer import analyze_keyword
from report_generator import generate_report
from content_optimizer import optimize_all
from linkedin_cv_agent import main as linkedin_cv_main


async def run_agent_safe(name: str, coro) -> bool:
    print(f"\n{'━'*60}")
    print(f"{name}")
    print(f"{'━'*60}")
    try:
        async with asyncio.timeout(300):
            await coro
        print(f"✅ {name} — Succès")
        return True
    except asyncio.TimeoutError:
        print(f"❌ {name} — Timeout (>5 min)")
        return False
    except Exception as e:
        print(f"❌ {name} — Erreur : {type(e).__name__}: {e}")
        traceback.print_exc()
        return False


async def main():
    print("🚀 KeywordMoneyMaker — Lancement des agents\n")

    results = {
        "Agent 1 — Analyse des mots-clés": await run_agent_safe(
            "AGENT 1 — Analyse des mots-clés",
            analyze_keyword("générateur d'articles SEO", "fr")
        ),
        "Agent 2 — Génération du rapport": await run_agent_safe(
            "AGENT 2 — Génération du rapport",
            generate_report()
        ),
        "Agent 3 — Optimisation du contenu": await run_agent_safe(
            "AGENT 3 — Optimisation du contenu",
            optimize_all()
        ),
        "Agent 4 — LinkedIn & CV": await run_agent_safe(
            "AGENT 4 — Documentation LinkedIn & CV",
            linkedin_cv_main()
        ),
    }

    print("\n" + "="*60)
    print("RÉSUMÉ FINAL")
    print("="*60)
    passed = sum(1 for v in results.values() if v)
    for name, success in results.items():
        print(f"{'✅' if success else '❌'} {name}")
    print(f"\n{passed}/{len(results)} agents réussis")
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    asyncio.run(main())
