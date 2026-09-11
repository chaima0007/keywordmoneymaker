"""
Agent DECISION_SIMULATOR — 50 Simulations Avant Chaque Décision
Prend une décision business, stratégique ou technique et génère
50 scénarios en variant les hypothèses clés. Retient uniquement
les conclusions robustes qui survivent à la majorité des scénarios.
Zéro décision sans validation multi-angles.
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from statistics import mean, stdev

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "simulations"

N_SIMULATIONS_DEFAULT = 50


async def _generate_scenarios(decision: str, contexte: str, n: int) -> list[dict]:
    """Génère N scénarios distincts en variant les hypothèses."""
    prompt = f"""Tu es un expert en analyse de décision et simulation de scénarios.
Décision à évaluer : "{decision}"
Contexte : {contexte}

Génère exactement {n} scénarios distincts pour tester cette décision.
Varie les hypothèses : marché favorable/défavorable, ressources disponibles/limitées,
concurrents actifs/passifs, timing bon/mauvais, adoption rapide/lente, etc.

Réponds en JSON :
{{
  "decision": "{decision}",
  "scenarios": [
    {{
      "id": 1,
      "nom": "Scénario court (5 mots max)",
      "hypotheses": {{
        "marche": "favorable|neutre|défavorable",
        "ressources": "abondantes|normales|limitées",
        "concurrence": "faible|normale|forte",
        "timing": "optimal|normal|mauvais",
        "adoption": "rapide|normale|lente"
      }},
      "probabilite": 0.08,
      "resultat": "succès|echec|mitige",
      "impact_revenu": "+30%|-20%|+5%",
      "risque_principal": "Description courte du risque clé",
      "recommandation": "go|no-go|go-conditionnel"
    }}
  ]
}}

Les probabilités doivent sommer à 1.0.
Répartis : ~40% scénarios favorables, ~35% neutres, ~25% défavorables.
Réponds UNIQUEMENT avec le JSON valide."""

    content = ""
    try:
        async with asyncio.timeout(90):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception) as e:
        print(f"  ⚠️  Erreur génération scénarios : {e}")
        return []

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]

    try:
        data = json.loads(content.strip())
        return data.get("scenarios", [])
    except json.JSONDecodeError:
        return []


async def _analyze_robustness(decision: str, scenarios: list[dict]) -> dict:
    """Analyse statistique des 50 scénarios pour extraire les conclusions robustes."""
    if not scenarios:
        return {}

    go_count    = sum(1 for s in scenarios if s.get("recommandation") == "go")
    nogo_count  = sum(1 for s in scenarios if s.get("recommandation") == "no-go")
    cond_count  = sum(1 for s in scenarios if s.get("recommandation") == "go-conditionnel")
    total       = len(scenarios)

    succes_rate = sum(1 for s in scenarios if s.get("resultat") == "succès") / total
    echec_rate  = sum(1 for s in scenarios if s.get("resultat") == "echec") / total

    prob_ponderee_go = sum(
        s.get("probabilite", 1/total)
        for s in scenarios
        if s.get("recommandation") == "go"
    )

    risques = [s.get("risque_principal", "") for s in scenarios if s.get("risque_principal")]
    risques_str = "\n".join(f"- {r}" for r in risques[:15])

    prompt = f"""Tu es expert en analyse de risque et aide à la décision.

Décision analysée : "{decision}"
Résultats de {total} simulations :
- GO      : {go_count} ({round(go_count/total*100)}%)
- NO-GO   : {nogo_count} ({round(nogo_count/total*100)}%)
- GO COND.: {cond_count} ({round(cond_count/total*100)}%)
- Taux succès : {round(succes_rate*100)}%
- Taux échec  : {round(echec_rate*100)}%
- Probabilité pondérée GO : {round(prob_ponderee_go*100)}%

Principaux risques identifiés :
{risques_str}

Génère une analyse de robustesse JSON :
{{
  "verdict_final": "GO|NO-GO|GO-CONDITIONNEL",
  "confiance": 78,
  "seuil_go": "GO si confiance > 65% recommandé",
  "conditions_go": ["Condition 1 à réunir avant d'agir", "Condition 2"],
  "risques_critiques": ["Risque qui apparaît dans >30% des scénarios"],
  "protections_recommandees": ["Plan B si scénario X", "Limite de perte acceptable"],
  "meilleur_timing": "Immédiat|3 mois|6 mois|Attendre signal X",
  "facteur_succes_cle": "La 1 chose qui détermine si GO réussit",
  "phrase_direction": "Synthèse en 1 phrase pour le COMEX"
}}

Réponds UNIQUEMENT avec le JSON."""

    content = ""
    try:
        async with asyncio.timeout(40):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception):
        return {
            "verdict_final": "GO-CONDITIONNEL",
            "confiance": round(prob_ponderee_go * 100),
            "phrase_direction": f"Décision nécessite validation manuelle ({go_count}/{total} scénarios favorables)",
        }

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    try:
        result = json.loads(content.strip())
        result["stats_brutes"] = {
            "total_scenarios": total,
            "go": go_count, "no_go": nogo_count, "conditionnel": cond_count,
            "taux_succes_pct": round(succes_rate * 100),
            "taux_echec_pct": round(echec_rate * 100),
        }
        return result
    except json.JSONDecodeError:
        return {}


async def simulate(
    decision: str,
    contexte: str = "",
    n: int = N_SIMULATIONS_DEFAULT,
) -> dict:
    params = {"decision": decision[:150].lower(), "n": n}
    cached = cache.get("decision_simulator", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    if not contexte:
        contexte = "Caelum Partners — agence digitale IA, Bruxelles. Clients B2B. Revenus : prestations + SaaS."

    print(f"\n{'='*60}")
    print(f"  DECISION_SIMULATOR — {n} simulations")
    print(f"  Décision : {decision[:60]}{'...' if len(decision)>60 else ''}")
    print(f"{'='*60}")

    t0 = time.perf_counter()
    print(f"\n⏳ Génération de {n} scénarios...")
    scenarios = await _generate_scenarios(decision, contexte, n)

    if not scenarios:
        print("❌ Impossible de générer les scénarios.")
        return {}

    print(f"✅ {len(scenarios)} scénarios générés en {round(time.perf_counter()-t0,1)}s")

    print("\n🔬 Analyse de robustesse...")
    analysis = await _analyze_robustness(decision, scenarios)

    verdict = analysis.get("verdict_final", "?")
    confiance = analysis.get("confiance", 0)
    icon = {"GO": "✅", "NO-GO": "❌", "GO-CONDITIONNEL": "⚠️"}.get(verdict, "?")

    print(f"\n{icon} VERDICT : {verdict} (confiance : {confiance}%)")
    print(f"📌 {analysis.get('phrase_direction','')}")
    if analysis.get("conditions_go"):
        print("\nConditions requises :")
        for c in analysis["conditions_go"]:
            print(f"  → {c}")
    if analysis.get("risques_critiques"):
        print("\nRisques critiques :")
        for r in analysis["risques_critiques"]:
            print(f"  ⚠️  {r}")

    result = {
        "decision": decision,
        "contexte": contexte,
        "n_simulations": len(scenarios),
        "date": datetime.now().isoformat(),
        "duree_s": round(time.perf_counter() - t0, 1),
        "analyse": analysis,
        "scenarios": scenarios,
    }

    cache.set("decision_simulator", params, json.dumps(result), ttl_hours=24)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    safe = decision[:40].replace(" ", "_")
    path = OUTPUT_DIR / f"sim_{safe}_{date_str}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = OUTPUT_DIR / f"sim_{safe}_{date_str}.md"
    md_content = (
        f"# Simulation — {decision[:60]}\n"
        f"*{len(scenarios)} scénarios | {date_str}*\n\n"
        f"## Verdict : {icon} {verdict} (confiance {confiance}%)\n\n"
        f"**{analysis.get('phrase_direction','')}**\n\n"
    )
    if analysis.get("conditions_go"):
        md_content += "## Conditions requises\n" + "\n".join(f"- {c}" for c in analysis["conditions_go"]) + "\n\n"
    if analysis.get("risques_critiques"):
        md_content += "## Risques critiques\n" + "\n".join(f"- ⚠️  {r}" for r in analysis["risques_critiques"]) + "\n\n"
    if analysis.get("protections_recommandees"):
        md_content += "## Protections\n" + "\n".join(f"- {p}" for p in analysis["protections_recommandees"]) + "\n\n"
    md_content += f"## Stats brutes\n```json\n{json.dumps(analysis.get('stats_brutes',{}), indent=2)}\n```\n"
    md_path.write_text(md_content, encoding="utf-8")

    print(f"\n✅ Rapport : {md_path}")
    return result


async def simulate_batch(decisions: list[tuple[str, str]]) -> list[dict]:
    """Lance plusieurs simulations en parallèle."""
    print(f"\n⚡ DECISION_SIMULATOR BATCH — {len(decisions)} décisions")
    results = await asyncio.gather(
        *[simulate(d, c) for d, c in decisions],
        return_exceptions=True,
    )
    return [r for r in results if isinstance(r, dict) and r]


if __name__ == "__main__":
    decision_arg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else (
        "Lancer une offre CompeteIQ à 149€/mois en ciblant les startups Series A belges"
    )
    asyncio.run(simulate(decision_arg))
