"""
Orchestrateur — Lance tous les agents avec cache + parallélisme.
Mode rapide (défaut) : agents indépendants en parallèle, cache 24h.
Mode séquentiel     : uv run python agents/run_all.py --sequential
"""

import asyncio
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import cache_manager as cache
from keyword_analyzer import analyze_keyword
from report_generator import generate_report
from content_optimizer import optimize_all
from linkedin_cv_agent import main as linkedin_cv_main


async def run_agent_safe(name: str, coro) -> bool:
    print(f"\n{'━'*60}\n{name}\n{'━'*60}")
    t0 = time.perf_counter()
    try:
        async with asyncio.timeout(300):
            await coro
        print(f"✅ {name} — {round(time.perf_counter()-t0, 1)}s")
        return True
    except asyncio.TimeoutError:
        print(f"❌ {name} — Timeout (>5 min)")
        return False
    except Exception as e:
        print(f"❌ {name} — {type(e).__name__}: {e}")
        traceback.print_exc()
        return False


async def run_parallel_mode():
    """Agents indépendants lancés simultanément."""
    from parallel_runner import run_parallel
    tasks = [
        ("AGENT 1 — Mots-clés",    analyze_keyword("générateur d'articles SEO", "fr")),
        ("AGENT 2 — Rapport",       generate_report()),
    ]
    results_map = await run_parallel(tasks, global_timeout=300)
    ok = sum(1 for r in results_map.values() if r["status"] == "ok")

    # Agents séquentiels (dépendent de fichiers générés par les autres)
    r3 = await run_agent_safe("AGENT 3 — Optimisation", optimize_all())
    r4 = await run_agent_safe("AGENT 4 — LinkedIn & CV", linkedin_cv_main())

    total = len(tasks) + 2
    passed = ok + (1 if r3 else 0) + (1 if r4 else 0)
    return passed, total


async def run_sequential_mode():
    tasks = [
        ("AGENT 1 — Mots-clés",    analyze_keyword("générateur d'articles SEO", "fr")),
        ("AGENT 2 — Rapport",       generate_report()),
        ("AGENT 3 — Optimisation",  optimize_all()),
        ("AGENT 4 — LinkedIn & CV", linkedin_cv_main()),
    ]
    results = [await run_agent_safe(name, coro) for name, coro in tasks]
    return sum(results), len(results)


async def main():
    sequential = "--sequential" in sys.argv

    cs = cache.stats()
    purged = cache.purge_expired()
    print(f"🚀 KeywordMoneyMaker — {'Séquentiel' if sequential else 'Parallèle + Cache'}")
    print(f"📦 Cache : {cs['valid']} entrée(s) valide(s)")
    if purged:
        print(f"🧹 {purged} entrée(s) expirée(s) purgée(s)")
    print()

    wall_start = time.perf_counter()
    if sequential:
        passed, total = await run_sequential_mode()
    else:
        passed, total = await run_parallel_mode()

    wall = round(time.perf_counter() - wall_start, 1)
    print(f"\n{'='*60}\nRÉSUMÉ FINAL — {wall}s\n{'='*60}")
    print(f"{passed}/{total} agents réussis")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    asyncio.run(main())
