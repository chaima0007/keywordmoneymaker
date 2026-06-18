"""
Agent BATTLE_CARD_GENERATOR — Générateur de Battle Cards Commerciales
Prend les données du competitor_tracker et génère des battle cards
prêtes à l'emploi pour les équipes commerciales.
Alimente FORGE dans CompeteIQ.
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
OUTPUT_DIR   = PROJECT_ROOT / "battle_cards"

NOTRE_PRODUIT = {
    "nom": "CompeteIQ",
    "promesse": "Savoir ce que font vos concurrents avant qu'ils le fassent — 9 agents IA, alertes <2h",
    "differenciateurs": [
        "9 agents IA spécialisés vs dashboard de veille généraliste",
        "Alertes en moins de 2 heures vs rapports hebdomadaires",
        "RÉSOLVEUR génère un plan de réponse en 30 secondes",
        "Battle cards auto-générées et mises à jour en continu",
        "Simulateur d'impact de scénarios concurrentiels",
    ],
    "clients_cibles": "Équipes commerciales B2B, Directions Marketing, CEO startups Series A+",
    "prix_entree": "149€/mois — essai 14 jours gratuit",
}


async def generate_battle_card(competitor_data: dict) -> str:
    if not competitor_data or "nom" not in competitor_data:
        return ""

    nom = competitor_data["nom"]
    params = {"competitor": nom.lower(), "version": "v2"}
    cached = cache.get("battle_card", params)
    if cached:
        return cached

    data_str = json.dumps(competitor_data, ensure_ascii=False, indent=2)

    prompt = f"""Tu es BATTLE_CARD_GENERATOR, expert en enablement commercial B2B.
Tu crées des battle cards percutantes pour aider les commerciaux à gagner face à la concurrence.

Notre produit : {json.dumps(NOTRE_PRODUIT, ensure_ascii=False)}

Données concurrentielles sur {nom} :
{data_str}

---

# BATTLE CARD — {nom.upper()}
*Mise à jour : {datetime.now().strftime('%d/%m/%Y')}*

---

## ⚡ PITCH EN 30 SECONDES
Une phrase pour se différencier immédiatement de {nom} en réunion client.

## 🎯 QUAND VOUS RENCONTREZ {nom.upper()}
Signaux d'alerte : comment reconnaître qu'un prospect compare avec {nom}.

## ✅ NOS AVANTAGES FACE À EUX
| Ce que {nom} offre | Ce que nous offrons | Avantage |
|---|---|---|
(Tableau 4-5 lignes, très concret, chiffres si possible)

## ❌ LEURS FAIBLESSES — NE PAS ATTAQUER, RÉVÉLER
3 failles de {nom} à faire découvrir au prospect par des questions ouvertes.
Pour chaque faille : la question à poser, la réponse attendue, notre bénéfice.

## 🛡️ OBJECTIONS ET RÉPONSES
Pour chaque objection probable du prospect :

**"[Objection]"**
→ *Réponse :* [Réfutation empathique + preuve + redirection]

## 💀 MOTS ET PHRASES À ÉVITER
Ce que ne jamais dire face à un prospect qui compare avec {nom}.

## 🏆 ARGUMENT DÉCISIF (CLOSING)
La phrase finale qui fait basculer le deal en notre faveur.

## 📊 MÉTRIQUES DE RÉFÉRENCE
Chiffres clés à avoir en tête pour cette compétition.

## 🚨 SIGNAUX D'ALERTE — LE PROSPECT PART CHEZ EUX
Comportements qui indiquent que le prospect penche vers {nom} + action à prendre immédiatement.

---
*Battle card générée par FORGE — CompeteIQ | Confidentiel usage interne*"""

    print(f"\n⚔️  BATTLE_CARD — {nom}")
    content = ""
    try:
        async with asyncio.timeout(75):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except asyncio.TimeoutError:
        print(f"  ❌ Timeout — {nom}")
        return ""
    except Exception as e:
        print(f"  ❌ {type(e).__name__}: {e}")
        return ""

    if content:
        cache.set("battle_card", params, content, ttl_hours=72)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        safe = nom.lower().replace(" ", "_")[:30]
        path = OUTPUT_DIR / f"battlecard_{safe}_{date_str}.md"
        path.write_text(content, encoding="utf-8")
        print(f"  ✅ Battle card : {path.name}")
        return str(path)
    return ""


async def generate_from_tracker_output(json_path: str | None = None) -> list[str]:
    """Charge les données du competitor_tracker et génère toutes les battle cards."""
    if json_path:
        p = Path(json_path)
    else:
        files = sorted(INTEL_DIR.glob("competitors_*.json"), reverse=True)
        if not files:
            print("❌ Aucun fichier competitors_*.json trouvé. Lance d'abord competitor_tracker.py")
            return []
        p = files[0]

    print(f"\n{'='*60}")
    print(f"  BATTLE_CARD_GENERATOR — Chargement : {p.name}")
    print(f"{'='*60}")

    try:
        competitors_data = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"❌ Erreur lecture : {e}")
        return []

    print(f"  {len(competitors_data)} concurrent(s) chargés")
    results = await asyncio.gather(
        *[generate_battle_card(d) for d in competitors_data],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n  ✅ {len(paths)}/{len(competitors_data)} battle cards générées dans battle_cards/")
    return paths


async def generate_single(competitor_name: str) -> str:
    """Génère une battle card pour un concurrent en important d'abord ses données."""
    from competitor_tracker import track_competitor
    print(f"\n🔄 Import données pour {competitor_name}...")
    data = await track_competitor(competitor_name)
    if not data:
        return ""
    return await generate_battle_card(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(generate_single(sys.argv[1]))
    else:
        asyncio.run(generate_from_tracker_output())
