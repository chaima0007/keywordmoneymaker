"""
Agent 4 — Documentation LinkedIn & CV
Génère des posts LinkedIn percutants, une section CV détaillée et un "À propos".
Positionnement : Communication · Vente · Empathie
Intègre les recommandations de l'audit expert Business/LinkedIn.
"""

import asyncio
import os
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "linkedin_cv")


async def generate_linkedin_post() -> str:
    prompt = """
Tu es un expert en personal branding et copywriting LinkedIn.

Génère 3 posts LinkedIn percutants pour une professionnelle qui a :
- Créé une plateforme SaaS SEO complète (KeywordMoneyMaker) : 50+ articles/mois, ce qui remplace 200+ heures de travail manuel
- Développé 4 agents IA autonomes (analyse mots-clés, rapports, optimisation, LinkedIn/CV)
- Intégré des outils avancés (Claude Agent SDK, Composio, uv)
- Expertise : vente consultative, communication persuasive, empathie client

Son positionnement : experte en **communication persuasive**, **stratégie de vente digitale** et **empathie client**.

Règles impératives :
- Maximum 5 hashtags par post (pas plus)
- Chaque chiffre doit avoir un contexte (ex. "50 articles = 200+ heures remplacées")
- CTA personnalisé et engageant (pas générique)
- Ton authentique, humain, jamais corporate

---

### POST 1 — L'histoire du projet

**Accroche** (1 ligne qui stoppe le scroll, révèle une vulnérabilité ou une contradiction)

Corps (150-200 mots) :
- Comment l'idée est née d'une frustration personnelle
- Le défi relevé avec des chiffres contextualisés
- Leçon apprise : la meilleure tech vient d'un problème humain réel

**CTA** : invite les lecteurs à partager leur frustration et promet une réponse personnelle

---

### POST 2 — L'humain que l'IA ne remplacera jamais

**Accroche** (joue sur la contradiction IA vs humain)

Corps (150-200 mots) :
- Automatise la production mais pas la relation
- Proof point concret : les utilisateurs Premium restent parce que l'UX est pensée avec empathie
- Les 3 compétences que l'IA ne code pas (écouter, reformuler, savoir quand reculer)

**CTA** : invite à taguer un bon vendeur en commentaire

---

### POST 3 — La leçon d'empathie qui a tout changé

**Accroche** (admet un vrai échec)

Corps (150-200 mots) :
- Version du produit techniquement parfaite mais qui ne marchait pas
- Les 3 questions à poser avant chaque fonctionnalité
- Conclusion : l'empathie est un avantage concurrentiel, pas une qualité douce

**CTA** : demande une histoire similaire dans les commentaires

---

Pour chaque post, ajoute exactement 5 hashtags pertinents.
"""

    print("\n💼 Génération des posts LinkedIn...\n" + "="*60)
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
        print("❌ Timeout génération posts LinkedIn")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")
    return content


async def generate_cv_section() -> str:
    prompt = """
Tu es un expert en rédaction de CV haut de gamme et personal branding.

Génère une section CV professionnelle pour une experte qui a créé KeywordMoneyMaker.
Profil : Communication · Vente · Empathie — la tech est un levier, pas le cœur.

---

## PROFIL PROFESSIONNEL
3 phrases percutantes. Inclure un chiffre clé (ex. "50+ articles en 3 minutes vs. 8 heures").
Mettre en avant : empathie d'abord, tech ensuite.

---

## EXPÉRIENCE CLÉE

### Fondatrice & Architecte Produit IA — KeywordMoneyMaker (2026)

Format bullets STAR. Organiser en 4 blocs :

**Vision & Stratégie Produit**
- Identifier le besoin marché non adressé, concevoir l'architecture SaaS 19 langues, définir 3 personas

**Développement Technique & IA**
- 4 agents IA autonomes Python (Claude SDK + Composio)
- Pipeline automatisé : de l'intention de recherche à la publication — 8h → 3 min par article
- Sécurité : score 2/9 → 9/9 grâce à CSP, hreflang, meta-tags de sécurité

**Vente, Modèle Économique & Acquisition**
- Freemium 3 niveaux (0€ / 99€ / 199€/mois) optimisé pour la conversion
- Copywriting complet : pages de vente, onboarding, emails — bénéfice avant fonctionnalité
- Utilisateurs Premium actifs : potentiel de 15 000€+/mois en contenu SEO monétisé

**Communication Client & Empathie**
- Cartographie 3 personas, UX pensée pour rassurer autant qu'informer
- Chaque message (erreur, notif, email) rédigé avec une logique d'empathie structurée
- Voix de marque cohérente entre produit, communication externe et support

---

## COMPÉTENCES CLÉES (hiérarchie Tier 1/2/3)

### Tier 1 — Communication & Vente (compétences maîtresses)
Copywriting, storytelling, vente consultative, écoute active, empathie structurée, reformulation,
communication multicanal, freemium & upsell

### Tier 2 — Leadership & Stratégie
Vision produit, décision autonome, pensée systémique, gestion de projet IA, résilience

### Tier 3 — Outils & Technologies
Tableau : IA / Dev / SEO / Produit / Business

---

## RÉALISATIONS CHIFFRÉES (6 bullets avec emojis)
Inclure : lancement solo, 19 langues, 95% réduction temps, 15 000€+/mois, 4 agents IA, rétention empathique

---

Ton : confiant, humain, sans jargon creux. Corriger la faute : "Architécturé" → "Architecturé".
"""

    print("\n📄 Génération de la section CV...\n" + "="*60)
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
        print("❌ Timeout génération CV")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")
    return content


async def generate_about_section() -> str:
    prompt = """
Tu es un expert en personal branding LinkedIn.

Rédige la section "À propos" LinkedIn pour une experte en Communication · Vente · Empathie.
Elle a créé KeywordMoneyMaker : 50+ articles SEO/mois, 8h → 3 minutes par article, 19 langues, 4 agents IA.

Limite réelle LinkedIn : 2 600 caractères. Vise 1 600-1 800 pour avoir de l'impact sans remplissage.

Structure :
1. **Accroche 3 temps** mémorable (couvre Communication / Tech / Empathie)
2. **Ce qu'elle fait** concrètement et pour qui (entrepreneurs, startups, équipes commerciales)
3. **Philosophie** : tech sans empathie = bruit / mots sans stratégie = gaspillage
4. **Chiffre clé** : "8 heures → 3 minutes" (crédibilité immédiate)
5. **Ce que le lecteur obtient** : 3 bullets scannables, orientés résultats
6. **Mention LinkedIn** : elle partage aussi du contenu sur l'IA + relation client (ancre sa crédibilité de communicant)
7. **CTA à deux volets** : deux raisons claires d'envoyer un DM (contenu SEO OU IA sans perdre la relation client)

Ton : chaleureux, direct ("tu"), authentique, jamais corporate.
Pas de bullet "Mes valeurs sont..." — montrer, pas annoncer.
"""

    print("\n🌟 Génération de la section À propos LinkedIn...\n" + "="*60)
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
        print("❌ Timeout génération À propos")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")
    return content


async def save_all(posts: str, cv: str, about: str) -> str:
    try:
        Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    except (OSError, PermissionError) as e:
        print(f"❌ Impossible de créer {OUTPUT_DIR}: {e}")
        return ""

    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = Path(OUTPUT_DIR) / f"linkedin_cv_{date_str}.md"

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
    try:
        output_path.write_text(full_content, encoding="utf-8")
        print(f"\n✅ Fichier sauvegardé : {output_path}")
        return str(output_path)
    except (OSError, IOError) as e:
        print(f"❌ Échec sauvegarde : {e}")
        return ""


async def main():
    print("🚀 Agent LinkedIn & CV — Démarrage\n")
    try:
        posts, cv, about = await asyncio.wait_for(
            asyncio.gather(
                generate_linkedin_post(),
                generate_cv_section(),
                generate_about_section(),
                return_exceptions=True,
            ),
            timeout=300,
        )

        for name, result in [("Posts LinkedIn", posts), ("CV", cv), ("À propos", about)]:
            if isinstance(result, Exception):
                print(f"❌ {name} : {type(result).__name__}")

        path = await save_all(
            posts if isinstance(posts, str) else "",
            cv if isinstance(cv, str) else "",
            about if isinstance(about, str) else "",
        )
        if path:
            print(f"\n🎯 Tout est prêt dans : {path}")
            print("   → Copiez le contenu directement sur LinkedIn et votre CV !")

    except asyncio.TimeoutError:
        print("❌ Timeout global (>5 min)")
    except Exception as e:
        print(f"❌ Erreur critique : {type(e).__name__}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
