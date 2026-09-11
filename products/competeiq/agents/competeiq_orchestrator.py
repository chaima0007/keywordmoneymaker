"""
Agent COMPETEIQ_ORCHESTRATOR — Chef de Guerre de l'Intelligence Concurrentielle
Lance toute la pipeline en séquence optimisée :
1. competitor_tracker   → fiches JSON par concurrent
2. signal_detector      → signaux faibles + prédictions
3. battle_card_generator→ battle cards commerciales
4. Rapport exécutif consolidé
Durée totale estimée : 3-5 minutes pour 5 concurrents.
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache
from competitor_tracker     import track_all
from signal_detector        import scan_all_competitors
from battle_card_generator  import generate_battle_card

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "intelligence_reports"


async def _executive_report(
    competitors_data: list[dict],
    signals_data: list[dict],
    battle_card_paths: list[str],
) -> str:
    signals_index = {d["concurrent"]: d for d in signals_data if "concurrent" in d}

    summary_parts = []
    for c in competitors_data[:5]:
        nom    = c.get("nom", "?")
        menace = c.get("niveau_menace", "?")
        score  = c.get("score_menace", "?")
        resume = c.get("resume_executif", "")
        sig    = signals_index.get(nom, {})
        alerte = sig.get("alerte_niveau", "?")
        reco   = sig.get("recommandation_executive", "")
        summary_parts.append(
            f"- {nom} | menace:{menace} score:{score}/10 alerte:{alerte}\n"
            f"  Résumé: {resume}\n"
            f"  Action: {reco}"
        )

    prompt = f"""Tu es COMPETEIQ_ORCHESTRATOR, directeur de l'intelligence concurrentielle.
Date du rapport : {datetime.now().strftime('%d %B %Y')}

Données compilées sur {len(competitors_data)} concurrent(s) :
{chr(10).join(summary_parts)}

Battle cards générées : {len(battle_card_paths)} fichiers

Rédige un rapport exécutif de direction en français (600-800 mots) avec :

# RAPPORT EXÉCUTIF — INTELLIGENCE CONCURRENTIELLE
## Situation Globale du Marché
## Les 3 Menaces Prioritaires Cette Semaine
## Opportunités de Conquête Immédiates
## Ce Que Nos Commerciaux Doivent Savoir Aujourd'hui
## Décisions Recommandées au COMEX (top 3)
## Horizon 90 Jours — Ce Qui Va Changer

Sois direct, factuel, sans jargon inutile. Chaque recommandation doit être actionnable dans les 7 prochains jours."""

    content = ""
    try:
        async with asyncio.timeout(60):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception):
        content = "Rapport automatique indisponible. Voir les données JSON dans competitive_intel/."
    return content


async def run(
    competitors: list[str] | None = None,
    secteur: str = "SaaS B2B intelligence concurrentielle",
    skip_cache: bool = False,
) -> str:
    if skip_cache:
        cache.invalidate("competitor_tracker")
        cache.invalidate("signal_detector")
        cache.invalidate("battle_card")

    cache.purge_expired()
    cs = cache.stats()

    print(f"\n{'█'*60}")
    print(f"  COMPETEIQ_ORCHESTRATOR — Mission Intelligence")
    print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M')} | Cache: {cs['valid']} entrées")
    print(f"{'█'*60}")

    wall_start = time.perf_counter()

    # ── ÉTAPE 1 : Surveillance concurrentielle ──
    print(f"\n{'─'*60}")
    print(f"  [1/4] COMPETITOR_TRACKER — Fiches concurrents")
    print(f"{'─'*60}")
    t0 = time.perf_counter()
    competitors_data = await track_all(competitors, secteur)
    print(f"  → {round(time.perf_counter()-t0,1)}s | {len(competitors_data)} fiches")

    if not competitors_data:
        print("❌ Aucune donnée concurrentielle. Abandon.")
        return ""

    # ── ÉTAPE 2 : Signaux faibles (en parallèle avec données déjà collectées) ──
    print(f"\n{'─'*60}")
    print(f"  [2/4] SIGNAL_DETECTOR — Signaux faibles")
    print(f"{'─'*60}")
    t0 = time.perf_counter()
    competitor_names = [d["nom"] for d in competitors_data]
    signals_data = await scan_all_competitors(competitor_names)
    print(f"  → {round(time.perf_counter()-t0,1)}s | {len(signals_data)} analyses")

    # ── ÉTAPE 3 : Battle cards (parallèle sur toutes les fiches) ──
    print(f"\n{'─'*60}")
    print(f"  [3/4] BATTLE_CARD_GENERATOR — Armes commerciales")
    print(f"{'─'*60}")
    t0 = time.perf_counter()
    bc_results = await asyncio.gather(
        *[generate_battle_card(d) for d in competitors_data],
        return_exceptions=True,
    )
    bc_paths = [r for r in bc_results if isinstance(r, str) and r]
    print(f"  → {round(time.perf_counter()-t0,1)}s | {len(bc_paths)} battle cards")

    # ── ÉTAPE 4 : Rapport exécutif ──
    print(f"\n{'─'*60}")
    print(f"  [4/4] RAPPORT EXÉCUTIF — Synthèse direction")
    print(f"{'─'*60}")
    t0 = time.perf_counter()
    rapport = await _executive_report(competitors_data, signals_data, bc_paths)
    print(rapport)
    print(f"  → {round(time.perf_counter()-t0,1)}s")

    # ── SAUVEGARDE ──
    wall = round(time.perf_counter() - wall_start, 1)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")

    full_output = {
        "date": date_str,
        "duree_secondes": wall,
        "concurrents_analyses": len(competitors_data),
        "battle_cards_generees": len(bc_paths),
        "signaux_detectes": sum(len(s.get("signaux_detectes", [])) for s in signals_data),
        "concurrent_top_menace": competitors_data[0]["nom"] if competitors_data else None,
        "rapport_executif": rapport,
    }

    report_path = OUTPUT_DIR / f"intelligence_report_{date_str}.json"
    report_path.write_text(json.dumps(full_output, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = OUTPUT_DIR / f"intelligence_report_{date_str}.md"
    md_path.write_text(
        f"# Rapport Intelligence Concurrentielle\n"
        f"*{date_str} | {wall}s | {len(competitors_data)} concurrents*\n\n"
        f"{rapport}",
        encoding="utf-8",
    )

    print(f"\n{'█'*60}")
    print(f"  Mission terminée en {wall}s")
    print(f"  {len(competitors_data)} fiches | {len(signals_data)} signaux | {len(bc_paths)} battle cards")
    print(f"  Rapport : {md_path}")
    print(f"{'█'*60}")
    return str(md_path)


if __name__ == "__main__":
    competitors_arg = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(run(competitors_arg))
