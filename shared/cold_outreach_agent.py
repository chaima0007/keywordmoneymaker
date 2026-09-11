"""
Agent 9 — Séquences de Prospection Froide (Cold Outreach)
Génère des séquences d'emails et messages LinkedIn personnalisés
par persona cible — empathiques, non-spammeux, orientés valeur.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

OUTPUT_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) / "outreach"

PERSONAS = {
    "entrepreneur_solo": {
        "description": "Entrepreneur solo, 1-3 ans d'activité, blog ou site e-commerce, veut plus de trafic organique sans y passer des heures",
        "douleur_principale": "Pas le temps de produire du contenu régulièrement",
        "objection_principale": "J'ai peur que le contenu IA soit mauvais ou pénalisé par Google",
        "canal": "Email froid",
    },
    "agence_digitale": {
        "description": "Agence SEO ou content marketing, 5-20 clients, cherche à scaler sans embaucher",
        "douleur_principale": "Coût de production du contenu trop élevé, marges qui s'érodent",
        "objection_principale": "Mes clients veulent du contenu 100% humain",
        "canal": "LinkedIn DM",
    },
    "createur_contenu": {
        "description": "YouTuber, blogger, influenceur, monétise via affiliation/pub, veut augmenter son trafic SEO",
        "douleur_principale": "Saturé de créer du contenu vidéo ET des articles de blog",
        "objection_principale": "Mon audience me connait, elle va détecter que c'est de l'IA",
        "canal": "Email froid",
    },
}


async def generate_sequence(persona_key: str = "entrepreneur_solo", langue: str = "fr") -> str:
    if persona_key not in PERSONAS:
        print(f"❌ Persona inconnu. Choisir parmi : {', '.join(PERSONAS.keys())}")
        return ""

    p = PERSONAS[persona_key]
    prompt = f"""
Tu es un expert en cold outreach, copywriting et vente B2B empathique.

Génère une séquence de prospection complète pour le persona suivant :

**Persona :** {p['description']}
**Douleur principale :** {p['douleur_principale']}
**Objection principale :** {p['objection_principale']}
**Canal :** {p['canal']}
**Langue :** {langue}
**Produit proposé :** KeywordMoneyMaker — plateforme SaaS qui génère 50+ articles SEO/mois en 3 minutes, 19 langues, 15 000€+/mois potentiel pour les utilisateurs actifs.

---

## SÉQUENCE EN 4 MESSAGES

### MESSAGE 1 — Premier contact (J+0)
Objectif : créer la connexion, PAS vendre.
- Objet email / 1ère ligne LinkedIn : ultra-personnalisé, montre que tu as fait tes recherches
- Corps : 3-5 lignes MAX, 1 question ouverte sur leur situation
- Aucune mention du produit
- Ton : humain, curieux, pas commercial

### MESSAGE 2 — Valeur sans demande (J+3)
Objectif : donner avant de prendre.
- Partager une insight, un outil gratuit ou un conseil actionnable lié à leur douleur
- Mention légère du produit seulement si naturelle
- Finir par une question ouverte

### MESSAGE 3 — L'offre (J+7)
Objectif : présenter la solution en répondant à leur objection principale avant qu'ils la posent.
- Commencer par valider leur réalité (empathie)
- Répondre à l'objection "{p['objection_principale']}" avec une preuve concrète
- Faire l'offre claire : "Je peux te montrer comment..."
- CTA simple : "Tu as 15 min cette semaine ?"

### MESSAGE 4 — Breakup (J+14)
Objectif : clore proprement ou rouvrir la conversation.
- Ton légèrement humour / sincère
- Pas de pression, respect de leur choix
- Laisser la porte ouverte avec une question personnelle

---

## VARIANTES PAR TRIGGER

Génère aussi 2 variantes du Message 1 pour ces déclencheurs :
- **Trigger "ils ont publié un article"** : commenter leur contenu récent
- **Trigger "ils cherchent un freelance"** : répondre à une offre d'emploi/prestation

---

## TEMPLATE DE PERSONNALISATION

Crée un tableau de variables à remplacer pour personnaliser chaque message :
| Variable | Exemple | Où trouver |
|---|---|---|
| {{prénom}} | Marie | LinkedIn / email |
| {{blog_url}} | monblog.fr | Profil LinkedIn |
| {{article_récent}} | "Comment gagner..." | Leur blog |
| {{douleur_spécifique}} | ... | Post LinkedIn récent |

---

Règles absolues :
- Jamais de "Je me permets de vous contacter" (interdit)
- Jamais de liste de fonctionnalités en message 1
- Maximum 120 mots par message
- Chaque message doit pouvoir être lu en 20 secondes
"""

    print(f"\n📨 Séquence Cold Outreach — Persona : {persona_key}\n{'='*60}")
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
                            print(block.text)
                            content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")

    if content:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        path = OUTPUT_DIR / f"outreach_{persona_key}_{date_str}.md"
        path.write_text(
            f"# Séquence Cold Outreach — {persona_key.replace('_', ' ').title()}\n{date_str}\n\n{content}",
            encoding="utf-8"
        )
        print(f"\n✅ Séquence sauvegardée : {path}")
        return str(path)
    return ""


async def generate_all() -> None:
    for persona in PERSONAS:
        await generate_sequence(persona)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(generate_sequence(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "fr"))
    else:
        asyncio.run(generate_all())
