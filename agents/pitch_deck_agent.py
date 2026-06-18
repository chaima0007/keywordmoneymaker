"""
Agent 8 — Générateur de Pitch Deck & Mémo Investisseur
Analyse les métriques du projet et génère un pitch deck complet
pour lever des fonds, convaincre des partenaires ou décrocher des clients B2B.
"""

import asyncio
import os
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "pitch"


async def generate_pitch(
    montant_recherche: str = "150 000€",
    type_investisseur: str = "business angel / seed fund",
    usage_fonds: str = "développement produit, acquisition clients, recrutement"
) -> str:
    prompt = f"""
Tu es un expert en fundraising, pitch investisseur et storytelling startup (YC, Station F, BPI).

Génère un pitch deck complet pour KeywordMoneyMaker basé sur ces informations réelles du projet :

**Le produit :**
- Plateforme SaaS IA qui génère 50+ articles SEO optimisés/mois
- Pipeline automatisé : 8h de travail → 3 minutes par article
- 4 agents IA autonomes (analyse mots-clés, rapports, optimisation, LinkedIn/CV)
- 19 langues supportées dès le lancement
- Sécurité renforcée (score 2/9 → 9/9), stack moderne (Python, Claude SDK, Composio)
- Modèle freemium 3 niveaux : 0€ / 99€ / 199€/mois
- Potentiel utilisateur Premium : 15 000€+/mois en revenus passifs SEO

**La fondatrice :**
- Experte en Communication · Vente · Empathie
- A conçu, développé et lancé le produit en solo
- Vision : rendre le SEO et la monétisation de contenu accessibles sans expertise technique

**Le contexte :**
- Marché SEO mondial : 80B$ en 2026, croissance +15%/an
- Boom IA generative : 60% des marketeurs utilisent désormais l'IA pour le contenu
- Opportunité : marché FR/EU sous-servi par les solutions américaines

**Levée de fonds :**
- Montant recherché : {montant_recherche}
- Type d'investisseur cible : {type_investisseur}
- Usage des fonds : {usage_fonds}

---

Génère le pitch deck complet avec ces 12 slides :

## SLIDE 1 — PROBLEM (La douleur)
Une slide qui fait mal — chiffres + histoire émotionnelle

## SLIDE 2 — SOLUTION (Le "Aha moment")
En une phrase : ce que fait le produit et pourquoi c'est différent

## SLIDE 3 — PRODUCT DEMO (Le produit en 3 bullets)
3 fonctionnalités clés avec leur bénéfice utilisateur, pas technique

## SLIDE 4 — MARKET SIZE (TAM / SAM / SOM)
Chiffres credibles, marché adressable réaliste

## SLIDE 5 — BUSINESS MODEL (Comment on gagne de l'argent)
Freemium, pricing, LTV estimée, CAC estimé, payback period

## SLIDE 6 — TRACTION (Preuves de momentum)
Métriques actuelles, early adopters, signaux marché

## SLIDE 7 — WHY NOW (Pourquoi maintenant)
3 vents favorables : macro-trend IA + régulation + comportement

## SLIDE 8 — COMPETITION (Positionnement compétitif)
Matrice 2x2 ou tableau comparatif — ce que les concurrents ne font pas

## SLIDE 9 — GO-TO-MARKET (Comment on acquiert les clients)
Canaux, CAC estimé, stratégie de contenu (SEO eating the market)

## SLIDE 10 — TEAM (La fondatrice)
Pourquoi elle est la bonne personne pour ce problème — empathie + tech + vente

## SLIDE 11 — FINANCIALS (Projections 3 ans)
Tableau : ARR, MRR, clients, marge brute — scénario conservateur + optimiste

## SLIDE 12 — THE ASK (Ce qu'on demande)
{montant_recherche} — usage détaillé, milestones à 12 mois, ce qu'on offre

---

Pour chaque slide :
- **Titre accrocheur** (pas "Business Model", mais "Chaque article = une rente")
- **Contenu** (bullets, chiffres, visuels suggérés)
- **Message clé** à retenir (1 phrase que l'investisseur doit répéter à ses collègues)
- **Note de présentation** (ce que dire à l'oral)
"""

    print(f"\n🚀 Génération du Pitch Deck\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(120):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            print(block.text)
                            content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")

    if content:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        path = OUTPUT_DIR / f"pitch_deck_{date_str}.md"
        path.write_text(
            f"# Pitch Deck KeywordMoneyMaker — {date_str}\n"
            f"Levée : {montant_recherche} | Cible : {type_investisseur}\n\n{content}",
            encoding="utf-8"
        )
        print(f"\n✅ Pitch deck sauvegardé : {path}")
        return str(path)
    return ""


if __name__ == "__main__":
    import sys
    montant = sys.argv[1] if len(sys.argv) > 1 else "150 000€"
    cible   = sys.argv[2] if len(sys.argv) > 2 else "business angel / seed fund"
    usage   = sys.argv[3] if len(sys.argv) > 3 else "développement produit, acquisition clients, recrutement"
    asyncio.run(generate_pitch(montant, cible, usage))
