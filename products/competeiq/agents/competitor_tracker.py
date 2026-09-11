"""
Agent COMPETITOR_TRACKER — Moteur de Surveillance Concurrentielle
Analyse un concurrent en profondeur : pricing, features, messaging,
recrutement, signaux de mouvement. Alimente SENTINEL + PRISM + ORACLE.
"""

import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "competitive_intel"

COMPETITORS_DEFAULT = [
    "Salesforce",
    "HubSpot",
    "Klue",
    "Crayon",
    "Kompyte",
]


async def track_competitor(
    competitor: str,
    secteur: str = "SaaS B2B intelligence concurrentielle",
    langue: str = "fr",
) -> dict:
    params = {"competitor": competitor.lower().strip(), "secteur": secteur[:80].lower()}
    cached = cache.get("competitor_tracker", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    prompt = f"""Tu es COMPETITOR_TRACKER, expert en intelligence concurrentielle B2B.
Analyse le concurrent "{competitor}" dans le secteur : {secteur}.

Génère une fiche de renseignement complète en JSON strict avec cette structure :

{{
  "nom": "{competitor}",
  "date_analyse": "{datetime.now().strftime('%Y-%m-%d')}",
  "niveau_menace": "critique|elevee|moderee|faible",
  "score_menace": 7,
  "resume_executif": "2 phrases max — ce que le dirigeant doit savoir",

  "positionnement": {{
    "proposition_valeur": "...",
    "segment_cible": "...",
    "differenciateur_cle": "...",
    "faiblesse_principale": "..."
  }},

  "pricing": {{
    "modele": "freemium|abonnement|usage|entreprise|sur_devis",
    "fourchette": "Ex: 99€-499€/mois",
    "plan_entree": "...",
    "plan_principal": "...",
    "plan_entreprise": "...",
    "tendance": "hausse|stable|baisse",
    "dernier_changement": "description si connu"
  }},

  "features_cles": [
    {{"nom": "...", "maturite": "GA|beta|roadmap", "avantage_vs_nous": true}}
  ],

  "signaux_recents": [
    {{
      "type": "recrutement|produit|prix|partenariat|acquisition|financement|communication",
      "description": "...",
      "date_estimee": "...",
      "impact": "eleve|moyen|faible",
      "interpretation": "ce que ça signifie pour nous"
    }}
  ],

  "recrutement": {{
    "volume_offres": "0-10|10-50|50+",
    "profils_recherches": ["ex: ingénieur IA", "commercial enterprise"],
    "signal": "expansion|consolidation|pivot|stable"
  }},

  "opportunites_vs_eux": [
    "Argument de différenciation 1",
    "Argument de différenciation 2",
    "Argument de différenciation 3"
  ],

  "objections_probables": [
    {{"objection": "...", "reponse_recommandee": "..."}}
  ],

  "prediction_6_mois": {{
    "action_probable": "...",
    "probabilite": 70,
    "impact_si_confirme": "..."
  }},

  "battle_card_punch": "1 phrase assassine pour contrer ce concurrent en vente"
}}

Réponds UNIQUEMENT avec le JSON valide. Sois précis et basé sur des réalités marché connues."""

    print(f"\n🔍 COMPETITOR_TRACKER — {competitor}\n{'─'*50}")
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
    except asyncio.TimeoutError:
        print(f"  ❌ Timeout — {competitor}")
        return {}
    except Exception as e:
        print(f"  ❌ {type(e).__name__}: {e}")
        return {}

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        data = json.loads(content)
        cache.set("competitor_tracker", params, json.dumps(data), ttl_hours=48)
        print(f"  ✅ {competitor} — menace : {data.get('niveau_menace','?')} | score : {data.get('score_menace','?')}/10")
        return data
    except json.JSONDecodeError:
        print(f"  ⚠️  JSON invalide pour {competitor}")
        return {"nom": competitor, "erreur": "parsing_failed", "contenu_brut": content[:300]}


async def track_all(
    competitors: list[str] | None = None,
    secteur: str = "SaaS B2B intelligence concurrentielle",
) -> list[dict]:
    competitors = competitors or COMPETITORS_DEFAULT
    print(f"\n{'='*60}")
    print(f"  COMPETITOR_TRACKER — Analyse de {len(competitors)} concurrent(s)")
    print(f"{'='*60}")

    results = await asyncio.gather(
        *[track_competitor(c, secteur) for c in competitors],
        return_exceptions=True,
    )

    data = [r for r in results if isinstance(r, dict) and r and "erreur" not in r]
    data.sort(key=lambda x: x.get("score_menace", 0), reverse=True)

    if data:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")

        # Fichier JSON complet
        json_path = OUTPUT_DIR / f"competitors_{date_str}.json"
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        # Résumé exécutif Markdown
        md_lines = [f"# Radar Concurrentiel — {date_str}\n"]
        for d in data:
            icon = {"critique": "🔴", "elevee": "🟠", "moderee": "🟡", "faible": "🟢"}.get(
                d.get("niveau_menace", ""), "⚪"
            )
            md_lines.append(f"## {icon} {d['nom']} — {d.get('score_menace','?')}/10")
            md_lines.append(f"**{d.get('resume_executif', '')}**\n")
            if d.get("prediction_6_mois"):
                p = d["prediction_6_mois"]
                md_lines.append(f"*Prédiction 6 mois ({p.get('probabilite','?')}%)* : {p.get('action_probable','')}\n")
            if d.get("battle_card_punch"):
                md_lines.append(f"> ⚔️  {d['battle_card_punch']}\n")

        md_path = OUTPUT_DIR / f"radar_{date_str}.md"
        md_path.write_text("\n".join(md_lines), encoding="utf-8")
        print(f"\n  ✅ {len(data)}/{len(competitors)} fiches | {json_path.name} + {md_path.name}")

    return data


if __name__ == "__main__":
    competitors_arg = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(track_all(competitors_arg))
