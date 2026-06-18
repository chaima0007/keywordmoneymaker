"""
Agent PARALLEL — Orchestrateur Parallèle Ultra-Rapide
Lance plusieurs agents simultanément via asyncio.gather().
Sans parallélisme : 9 agents × 60s = 9 minutes.
Avec parallélisme  : 9 agents en même temps = ~90 secondes.
"""

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from cache_manager import stats as cache_stats, purge_expired


async def _run(name: str, coro, results: dict) -> None:
    start = time.perf_counter()
    try:
        result = await coro
        elapsed = round(time.perf_counter() - start, 1)
        results[name] = {"status": "ok", "result": result, "elapsed": elapsed}
        print(f"  ✅ {name:<30} {elapsed}s")
    except asyncio.TimeoutError:
        elapsed = round(time.perf_counter() - start, 1)
        results[name] = {"status": "timeout", "result": None, "elapsed": elapsed}
        print(f"  ⏱️  {name:<30} TIMEOUT ({elapsed}s)")
    except Exception as e:
        elapsed = round(time.perf_counter() - start, 1)
        results[name] = {"status": "error", "result": None, "elapsed": elapsed, "error": str(e)}
        print(f"  ❌ {name:<30} {type(e).__name__}: {e}")


async def run_parallel(tasks: list[tuple[str, object]], global_timeout: int = 300) -> dict:
    """
    tasks = [("Nom Agent", coroutine), ...]
    Retourne un dict {nom: {status, result, elapsed}}
    """
    results: dict = {}
    print(f"\n🚀 PARALLEL RUNNER — {len(tasks)} agent(s)\n{'='*50}")
    wall_start = time.perf_counter()

    try:
        async with asyncio.timeout(global_timeout):
            await asyncio.gather(*[_run(name, coro, results) for name, coro in tasks])
    except asyncio.TimeoutError:
        print(f"\n⏱️  Timeout global ({global_timeout}s) atteint")

    wall = round(time.perf_counter() - wall_start, 1)
    ok = sum(1 for r in results.values() if r["status"] == "ok")
    ko = len(results) - ok
    print(f"\n{'='*50}")
    print(f"⏱️  Temps total : {wall}s  |  ✅ {ok} succès  |  ❌ {ko} échec(s)")

    sequential_estimate = sum(r["elapsed"] for r in results.values())
    if sequential_estimate > 0:
        gain = round(sequential_estimate - wall, 1)
        print(f"💡 Gain vs séquentiel : ~{gain}s économisées ({round(gain/sequential_estimate*100)}%)")

    return results


async def run_keyword_batch(keywords: list[str], langue: str = "fr") -> dict:
    """Lance l'analyse de plusieurs mots-clés en parallèle."""
    from keyword_analyzer import analyze_keyword
    tasks = [(f"Keyword: {kw}", analyze_keyword(kw, langue)) for kw in keywords]
    return await run_parallel(tasks, global_timeout=120)


async def run_full_suite(
    keyword: str = "générateur articles seo ia",
    outreach_persona: str = "entrepreneur_solo",
    niche_tendances: str = "SEO et monétisation de contenu",
) -> dict:
    """Lance tous les agents non-bloquants en parallèle."""
    from keyword_analyzer import analyze_keyword
    from report_generator import generate_report
    from trend_radar import detect_trends
    from emotion_analyzer import analyze_emotions
    from cold_outreach_agent import generate_sequence

    tasks = [
        ("Keyword Analyzer",  analyze_keyword(keyword)),
        ("Rapport Hebdo",     generate_report()),
        ("Radar Tendances",   detect_trends(niche_tendances)),
        ("Emotion Analyzer",  analyze_emotions()),
        ("Cold Outreach",     generate_sequence(outreach_persona)),
    ]
    return await run_parallel(tasks, global_timeout=180)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "suite"

    purge_expired()
    cs = cache_stats()
    print(f"📦 Cache : {cs['valid']} entrée(s) valide(s) / {cs['total']} total")

    if mode == "keywords":
        kws = sys.argv[2:] if len(sys.argv) > 2 else [
            "générateur articles ia",
            "outil seo automatique",
            "contenu ia google penalisation",
        ]
        asyncio.run(run_keyword_batch(kws))
    else:
        asyncio.run(run_full_suite())
