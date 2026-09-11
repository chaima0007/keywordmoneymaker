"""
Agent SIGNAL_DETECTOR — Détection de Signaux Faibles Concurrentiels
Identifie les patterns non-évidents dans les comportements concurrents.
"Ce recrutement + ce brevet + cette acquisition = nouveau produit dans 4 mois."
Alimente SENTINEL + ECHO + NEXUS dans CompeteIQ.
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
INTEL_DIR    = PROJECT_ROOT / "competitive_intel"
OUTPUT_DIR   = PROJECT_ROOT / "signals"

SIGNAL_SOURCES = """
Sources de signaux faibles à analyser :
• Offres d'emploi : profils recrutés → direction produit/tech/go-to-market
• Brevets déposés : domaines technologiques investis en secret
• Domaines enregistrés : nouveaux produits en préparation (nommage)
• Posts LinkedIn des fondateurs/dirigeants : communication sur la vision
• Changelog et release notes : priorités produit réelles
• Conférences et webinars : positionnement voulu vs actuel
• Avis G2/Capterra récents : frustrations clients = opportunités de conquête
• Partenariats technologiques annoncés : direction d'intégration
• Acquisitions : capacités manquantes comblées
• Levées de fonds : runway, ambitions, nouvelle phase
"""

PATTERNS_CONNUS = """
Patterns prédictifs connus :
• 10+ recrutements IA en 30 jours → feature IA dans 6-9 mois
• Acquisition d'un outil analytics → pivot vers data-driven en 12 mois
• Baisse de prix soudaine → pression VC sur la croissance OR nouveau concurrent puissant
• Recrutement massif CSM/Support → churn élevé non communiqué
• Chef de produit ex-concurrent recruté → feature copying en cours
• Conférence utilisateurs annoncée → nouvelle offre majeure imminent
• Réduction d'effectifs + repositionnement messaging → pivot de survie
"""


async def detect_signals(
    competitor: str,
    contexte_recent: str = "",
    horizons_mois: list[int] | None = None,
) -> dict:
    if horizons_mois is None:
        horizons_mois = [1, 3, 6]

    params = {"competitor": competitor.lower().strip(), "context": contexte_recent[:100].lower()}
    cached = cache.get("signal_detector", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    contexte_block = f"\nContexte récent connu : {contexte_recent}" if contexte_recent else ""

    prompt = f"""Tu es SIGNAL_DETECTOR, spécialiste des signaux faibles en intelligence concurrentielle.
Tu analyses les comportements non-évidents de concurrents pour prédire leurs mouvements futurs.

Concurrent analysé : "{competitor}"{contexte_block}

{SIGNAL_SOURCES}

{PATTERNS_CONNUS}

Génère une analyse de signaux faibles en JSON strict :

{{
  "concurrent": "{competitor}",
  "date": "{datetime.now().strftime('%Y-%m-%d')}",
  "score_activite": 7,
  "tendance_globale": "expansion|consolidation|pivot|declin|stable",

  "signaux_detectes": [
    {{
      "signal": "Description du signal observable",
      "source": "linkedin|brevets|recrutement|changelog|g2|presse|conference",
      "force": "fort|moyen|faible",
      "pattern_associe": "Quel pattern connu ça active",
      "interpretation": "Ce que ça signifie concrètement",
      "action_recommandee": "Ce que nous devons faire"
    }}
  ],

  "predictions": [
    {{
      "horizon_mois": 3,
      "prediction": "Action probable",
      "probabilite": 75,
      "signaux_supports": ["signal 1", "signal 2"],
      "impact_sur_nous": "elevé|moyen|faible",
      "preparation_recommandee": "Ce que nous devons préparer maintenant"
    }}
  ],

  "opportunites_immediates": [
    {{
      "description": "Opportunité de conquête ou de différenciation",
      "fenetre_action": "jours|semaines|mois",
      "clients_cibles": "Segment de clients à cibler maintenant",
      "argument": "Message à utiliser"
    }}
  ],

  "alerte_niveau": "critique|haute|normale|surveillance",
  "recommandation_executive": "1 phrase pour le CEO — action à prendre cette semaine"
}}

Sois analytique et précis. Évite les généralités. Réponds UNIQUEMENT avec le JSON."""

    print(f"\n📡 SIGNAL_DETECTOR — {competitor}")
    content = ""
    try:
        async with asyncio.timeout(55):
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
        cache.set("signal_detector", params, json.dumps(data), ttl_hours=24)
        alerte = data.get("alerte_niveau", "?")
        score  = data.get("score_activite", "?")
        signaux = len(data.get("signaux_detectes", []))
        print(f"  ✅ {competitor} — alerte : {alerte} | activité : {score}/10 | {signaux} signal(s)")
        return data
    except json.JSONDecodeError:
        print(f"  ⚠️  JSON invalide pour {competitor}")
        return {}


async def scan_all_competitors(
    competitors: list[str] | None = None,
    contextes: dict[str, str] | None = None,
) -> list[dict]:
    if not competitors:
        intel_files = sorted(INTEL_DIR.glob("competitors_*.json"), reverse=True)
        if intel_files:
            raw = json.loads(intel_files[0].read_text(encoding="utf-8"))
            competitors = [d["nom"] for d in raw if "nom" in d]
        else:
            competitors = ["Salesforce", "HubSpot", "Klue", "Crayon"]

    contextes = contextes or {}
    print(f"\n{'='*60}")
    print(f"  SIGNAL_DETECTOR — Scan de {len(competitors)} concurrent(s)")
    print(f"{'='*60}")

    results = await asyncio.gather(
        *[detect_signals(c, contextes.get(c, "")) for c in competitors],
        return_exceptions=True,
    )

    data = [r for r in results if isinstance(r, dict) and r]
    data.sort(
        key=lambda x: {"critique": 4, "haute": 3, "normale": 2, "surveillance": 1}.get(
            x.get("alerte_niveau", ""), 0
        ),
        reverse=True,
    )

    if data:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        out = OUTPUT_DIR / f"signals_{date_str}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        md = [f"# Signaux Faibles — {date_str}\n"]
        for d in data:
            alerte = d.get("alerte_niveau", "?")
            icon = {"critique": "🔴", "haute": "🟠", "normale": "🟡", "surveillance": "🟢"}.get(alerte, "⚪")
            md.append(f"## {icon} {d['concurrent']} — {alerte.upper()}")
            md.append(f"**{d.get('recommandation_executive', '')}**\n")
            for s in d.get("signaux_detectes", [])[:3]:
                md.append(f"- **{s.get('signal','')}** → {s.get('interpretation','')}")
            md.append("")

        md_out = OUTPUT_DIR / f"signals_{date_str}.md"
        md_out.write_text("\n".join(md), encoding="utf-8")
        print(f"\n  ✅ {len(data)} analyses | {out.name}")

    return data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(detect_signals(sys.argv[1], " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""))
    else:
        asyncio.run(scan_all_competitors())
