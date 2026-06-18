"""
Agent SOURCE_VALIDATOR — Validation de Fiabilité des Sources
Avant qu'une information entre dans la base de compétitive intelligence,
SOURCE_VALIDATOR la soumet à 7 critères de fiabilité.
Zéro donnée non vérifiée dans le système.
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
OUTPUT_DIR   = PROJECT_ROOT / "sources_validees"

# Hiérarchie de fiabilité des sources (1=le plus fiable)
SOURCE_TIERS = {
    "tier1_primaire": [
        "Site officiel de l'entreprise",
        "Communiqué de presse officiel",
        "Rapport annuel / 10-K / Documents SEC/AMF",
        "Interview dirigeant dans presse économique (Figaro, Challenges, Les Echos, FT, WSJ)",
        "Annonce officielle produit / changelog public",
        "Brevet déposé (INPI, USPTO, EPO)",
        "Offre d'emploi publiée officiellement",
    ],
    "tier2_secondaire": [
        "Article de presse tech reconnue (TechCrunch, The Verge, 01net, ZDNet)",
        "Étude de marché d'analyste (Gartner, Forrester, IDC)",
        "Avis clients vérifiés (G2, Capterra, Trustpilot — avec profils réels)",
        "Post LinkedIn vérifié du fondateur ou dirigeant",
        "Crunchbase / PitchBook (données de financement)",
    ],
    "tier3_indicatif": [
        "Forum Reddit / Hacker News (signal, pas fait)",
        "Tweet / post X sans source secondaire",
        "Article blog non-signé",
        "Rumeur secteur / bouche-à-oreille",
        "Donnée Wikipedia sans citation",
    ],
    "tier4_exclure": [
        "Source anonyme non vérifiable",
        "Donnée générée par IA sans référence",
        "Contenu marketing de l'entreprise concurrente elle-même (biaisé)",
        "Statistique sans méthodologie",
        "Information datant de plus de 18 mois dans secteur tech",
    ],
}

CRITERES_VALIDATION = """
7 critères de fiabilité à évaluer :
1. ORIGINE : Source primaire ou secondaire ? Identifiable ?
2. DATE : Information datée ? Moins de 12 mois ?
3. AUTEUR : Auteur identifié ? Expert reconnu ? Conflit d'intérêt ?
4. VÉRIFIABILITÉ : Peut-on vérifier indépendamment ?
5. COHÉRENCE : Cohérente avec d'autres sources connues ?
6. PRÉCISION : Chiffres sourcés ou estimations vagues ?
7. BIAIS : L'émetteur a-t-il un intérêt à déformer l'info ?
"""


async def valider_source(
    information: str,
    source_declaree: str = "",
    url_ou_reference: str = "",
) -> dict:
    params = {"info": information[:150].lower(), "source": source_declaree[:80].lower()}
    cached = cache.get("source_validator", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    tiers_str = json.dumps(SOURCE_TIERS, ensure_ascii=False, indent=2)
    ref_block = f"\nURL/Référence : {url_ou_reference}" if url_ou_reference else ""

    prompt = f"""Tu es SOURCE_VALIDATOR, expert en vérification d'information et fact-checking.
Ton rôle : protéger la base de données competitive intelligence contre les informations non fiables.

Information à valider : "{information}"
Source déclarée      : "{source_declaree or 'Non précisée'}"{ref_block}

Hiérarchie des sources :
{tiers_str}

{CRITERES_VALIDATION}

Évalue cette information et génère un rapport JSON :
{{
  "information": "{information[:100]}",
  "source_declaree": "{source_declaree or 'inconnue'}",
  "tier_source": "tier1|tier2|tier3|tier4",
  "score_fiabilite": 8,
  "verdict": "VALIDE|CONDITIONNEL|REJETE",

  "criteres": {{
    "origine": {{"score": 8, "commentaire": "..."}},
    "date": {{"score": 7, "commentaire": "..."}},
    "auteur": {{"score": 6, "commentaire": "..."}},
    "verificabilite": {{"score": 9, "commentaire": "..."}},
    "coherence": {{"score": 7, "commentaire": "..."}},
    "precision": {{"score": 8, "commentaire": "..."}},
    "biais": {{"score": 6, "commentaire": "..."}}
  }},

  "points_forts": ["Ce qui rend cette info crédible"],
  "points_faibles": ["Ce qui fragilise cette info"],

  "sources_de_verification": [
    "Source alternative où vérifier cette info (sans URL inventée — titre/auteur/publication)"
  ],

  "formulation_recommandee": "Comment reformuler cette info si CONDITIONNEL (avec les nuances appropriées)",
  "a_utiliser_avec": "CERTITUDE|PRUDENCE|SPECULATION",
  "raison_rejet": "Seulement si REJETE — pourquoi cette info ne peut pas entrer en base"
}}

Réponds UNIQUEMENT avec le JSON. Sois rigoureux — une fausse information en competitive intel peut coûter cher."""

    print(f"\n🔎 SOURCE_VALIDATOR — '{information[:50]}...' ")
    content = ""
    try:
        async with asyncio.timeout(45):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except asyncio.TimeoutError:
        print("  ❌ Timeout")
        return {}
    except Exception as e:
        print(f"  ❌ {type(e).__name__}: {e}")
        return {}

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]

    try:
        data = json.loads(content.strip())
        cache.set("source_validator", params, json.dumps(data), ttl_hours=12)

        verdict = data.get("verdict", "?")
        score   = data.get("score_fiabilite", "?")
        tier    = data.get("tier_source", "?")
        icon    = {"VALIDE": "✅", "CONDITIONNEL": "⚠️", "REJETE": "❌"}.get(verdict, "?")

        print(f"  {icon} {verdict} | Score: {score}/10 | {tier}")
        if verdict == "REJETE":
            print(f"  Raison: {data.get('raison_rejet','')}")
        elif verdict == "CONDITIONNEL":
            print(f"  Reformulation: {data.get('formulation_recommandee','')[:80]}")

        return data
    except json.JSONDecodeError:
        print("  ⚠️  JSON invalide")
        return {}


async def valider_rapport_concurrent(rapport_path: str) -> dict:
    """Valide toutes les affirmations clés d'un rapport concurrent."""
    path = Path(rapport_path)
    if not path.exists():
        print(f"❌ Fichier introuvable : {rapport_path}")
        return {}

    try:
        if path.suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                data = data[0]
            infos = []
            if data.get("pricing", {}).get("fourchette"):
                infos.append((f"Pricing {data['nom']}: {data['pricing']['fourchette']}", "Site officiel présumé", ""))
            for s in data.get("signaux_recents", [])[:3]:
                infos.append((s.get("description", ""), "Signal détecté", ""))
            if data.get("prediction_6_mois", {}).get("action_probable"):
                infos.append((data["prediction_6_mois"]["action_probable"], "Prédiction IA interne", ""))
        else:
            contenu = path.read_text(encoding="utf-8")
            lignes  = [l.strip() for l in contenu.split("\n") if l.strip() and not l.startswith("#")]
            infos   = [(l[:200], "Rapport interne", "") for l in lignes[:5]]
    except Exception as e:
        print(f"❌ Erreur lecture : {e}")
        return {}

    if not infos:
        print("⚠️  Aucune affirmation extractible du rapport.")
        return {}

    print(f"\n{'='*60}")
    print(f"  SOURCE_VALIDATOR — Validation de {len(infos)} affirmation(s)")
    print(f"  Fichier : {path.name}")
    print(f"{'='*60}")

    results = await asyncio.gather(
        *[valider_source(info, src, ref) for info, src, ref in infos],
        return_exceptions=True,
    )

    validations = [r for r in results if isinstance(r, dict) and r]
    valides    = sum(1 for v in validations if v.get("verdict") == "VALIDE")
    condis     = sum(1 for v in validations if v.get("verdict") == "CONDITIONNEL")
    rejetes    = sum(1 for v in validations if v.get("verdict") == "REJETE")

    score_moyen = round(
        sum(v.get("score_fiabilite", 0) for v in validations) / max(len(validations), 1), 1
    )

    print(f"\n📊 Bilan : ✅{valides} ⚠️{condis} ❌{rejetes} | Score moyen: {score_moyen}/10")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    out = OUTPUT_DIR / f"validation_{path.stem}_{date_str}.json"
    out.write_text(
        json.dumps({"fichier": str(path), "validations": validations, "score_moyen": score_moyen}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✅ Rapport validation : {out}")
    return {"valides": valides, "condis": condis, "rejetes": rejetes, "score_moyen": score_moyen}


if __name__ == "__main__":
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        asyncio.run(valider_rapport_concurrent(sys.argv[1]))
    elif len(sys.argv) > 1:
        info = " ".join(sys.argv[1:])
        asyncio.run(valider_source(info))
    else:
        asyncio.run(valider_source(
            "Salesforce a augmenté ses prix de 12% sur l'offre Enterprise en Q1 2026",
            "Article Les Echos — Janvier 2026",
        ))
