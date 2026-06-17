"""
Agent 4 — Documentation LinkedIn & CV
Analyse le travail accompli et génère du contenu professionnel :
- Posts LinkedIn percutants
- Sections CV détaillées
- Positionnement expert : Communication · Vente · Empathie
"""

import asyncio
import os
from datetime import datetime
from claude_agent_sdk import query, ClaudeAgentOptions


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "linkedin_cv")


async def generate_linkedin_post() -> str:
    prompt = """
Tu es un expert en personal branding et copywriting LinkedIn.

Génère 3 posts LinkedIn percutants pour une professionnelle qui a :
- Créé une plateforme SaaS SEO complète (KeywordMoneyMaker) capable de générer 50+ articles/mois
- Développé 3 agents IA autonomes (analyse de mots-clés, rapports, optimisation de contenu)
- Intégré des outils d'automatisation avancés (Claude Agent SDK, Composio, uv)
- Maîtrise la vente, la communication et l'empathie client

Son positionnement : experte en **communication persuasive**, **stratégie de vente digitale** et **empathie client** — elle comprend les besoins profonds des clients et construit des outils qui y répondent.

Pour chaque post LinkedIn :

### POST [numéro] — [Thème]

**Accroche** (1 ligne qui stoppe le scroll)

Corps du post (150-200 mots maximum) :
- Storytelling personnel et authentique
- Valeur concrète et chiffres
- Ton humain, chaleureux, empathique
- Pas de jargon technique pur — vulgarise intelligemment

**Hashtags** (5-7 pertinents)

**Appel à l'action** (engageant, pas commercial)

---

Les 3 angles :
1. **L'histoire du projet** — comment l'idée est née, le défi relevé
2. **L'expertise en vente/communication** — ce que l'IA ne remplacera jamais : l'humain
3. **Le conseil empathique** — une leçon apprise sur la compréhension des besoins clients
"""

    print("\n💼 Génération des posts LinkedIn...\n" + "="*60)
    content = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(allowed_tools=[]),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                    content += block.text
    return content


async def generate_cv_section() -> str:
    prompt = """
Tu es un expert en rédaction de CV haut de gamme et en personal branding.

Génère une section CV professionnelle et détaillée pour une experte qui a créé KeywordMoneyMaker.

Son profil : experte en **Communication · Vente · Empathie** qui utilise la technologie comme levier.

---

## PROFIL PROFESSIONNEL (Accroche CV)
3 phrases percutantes qui résument son identité professionnelle unique.
Met en avant : leadership, empathie, impact business, innovation.

---

## EXPÉRIENCE CLÉE

### Fondatrice & Architecte IA — KeywordMoneyMaker (2026)
Format : bullet points STAR (Situation → Tâche → Action → Résultat)

Inclure :
- Vision stratégique et conception du produit
- Développement de 3 agents IA autonomes (Python, Claude SDK, Composio)
- Architecture d'une plateforme SaaS multilingue (19 langues)
- Potentiel de revenus : 15 000€+/mois pour les utilisateurs
- Compétences en vente : modèle freemium 3 niveaux (0€ → 99€ → 199€/mois)
- Communication client : UX pensée avec empathie pour 3 personas distincts
- Automatisation complète du pipeline contenu SEO

---

## COMPÉTENCES CLÉES

### Communication & Vente
Liste détaillée des compétences soft et hard en communication persuasive, closing, empathie.

### Leadership & Stratégie
Vision produit, prise de décision, gestion de projet IA.

### Outils & Technologies
Stack technique de façon accessible (pas trop jargonneux).

---

## RÉALISATIONS CHIFFRÉES
5 bullet points avec métriques concrètes.

---

Ton : professionnel, confiant, humain. Évite le jargon creux. Chaque ligne doit montrer de la valeur réelle.
"""

    print("\n📄 Génération de la section CV...\n" + "="*60)
    content = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(allowed_tools=[]),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                    content += block.text
    return content


async def generate_about_section() -> str:
    prompt = """
Tu es un expert en personal branding LinkedIn.

Rédige une section "À propos" LinkedIn complète et percutante pour une professionnelle experte en :
- Communication persuasive et copywriting
- Vente digitale et stratégie commerciale
- Empathie client et compréhension des besoins profonds
- Innovation technologique (IA, SaaS, automatisation)

Elle a créé KeywordMoneyMaker : une plateforme qui aide les entreprises à générer du trafic organique et des revenus passifs grâce à l'IA.

Format de la section "À propos" LinkedIn (1 300 caractères max) :
- Ligne d'accroche inoubliable
- Ce qu'elle fait concrètement et pour qui
- Sa philosophie / valeurs (empathie, authenticité, impact)
- Résultats concrets qu'elle génère
- Appel à l'action pour la contacter

Ton : chaleureux, authentique, expert mais accessible. Pas de bullshit corporate.
"""

    print("\n🌟 Génération de la section À propos LinkedIn...\n" + "="*60)
    content = ""
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(allowed_tools=[]),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                    content += block.text
    return content


async def save_all(posts: str, cv: str, about: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(OUTPUT_DIR, f"linkedin_cv_{date_str}.md")

    full_content = f"""# LinkedIn & CV — KeywordMoneyMaker
Généré le {date_str}

---

# POSTS LINKEDIN

{posts}

---

# SECTION CV

{cv}

---

# SECTION À PROPOS LINKEDIN

{about}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"\n✅ Fichier sauvegardé : {output_path}")
    return output_path


async def main():
    print("🚀 Agent LinkedIn & CV — Démarrage\n")

    posts, cv, about = await asyncio.gather(
        generate_linkedin_post(),
        generate_cv_section(),
        generate_about_section(),
    )

    path = await save_all(posts, cv, about)
    print(f"\n🎯 Tout est prêt dans : {path}")
    print("   → Copiez le contenu directement sur LinkedIn et votre CV !")


if __name__ == "__main__":
    asyncio.run(main())
