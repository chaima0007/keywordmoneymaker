"""
Agent 6 — Analyse Émotionnelle des Prospects
Prend des feedbacks clients (emails, commentaires, avis) et détecte :
- Les vraies frustrations cachées derrière les mots
- Les désirs non exprimés
- Les objections récurrentes avant achat
- Ce qui convertit vs. ce qui fait fuir
Alimente directement la stratégie produit, le copywriting et la vente.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

OUTPUT_DIR = Path(os.path.dirname(__file__)).parent / "reports"

# Exemple de feedbacks par défaut si aucun n'est fourni
DEFAULT_FEEDBACKS = """
1. "C'est bien mais je ne sais pas si ça va vraiment marcher pour moi, j'ai déjà essayé des trucs comme ça"
2. "Le prix est élevé pour commencer, j'aimerais voir des résultats avant de payer"
3. "Mon problème c'est que j'ai pas le temps de tout gérer, pas le budget pour quelqu'un"
4. "Je comprends pas trop comment ça fonctionne, vous pouvez m'expliquer simplement ?"
5. "J'ai peur que le contenu IA soit détecté par Google et que ça me pénalise"
6. "Super outil mais j'aurais besoin que ça soit encore plus automatique"
7. "Je galère à trouver des sujets qui rapportent vraiment de l'argent"
8. "J'ai essayé et les articles sont corrects mais pas extraordinaires"
9. "Est-ce que c'est vraiment adapté aux petits blogs qui démarrent ?"
10. "J'ai l'impression que tout le monde fait la même chose maintenant avec l'IA"
"""


async def analyze_emotions(feedbacks: str = DEFAULT_FEEDBACKS, contexte: str = "plateforme SaaS SEO") -> str:
    prompt = f"""
Tu es un expert en psychologie du consommateur, copywriting et stratégie produit.

Analyse ces feedbacks/commentaires de prospects pour la solution suivante : {contexte}

FEEDBACKS À ANALYSER :
{feedbacks}

---

## 1. CARTE DES ÉMOTIONS

Pour chaque feedback, identifie :
- **Émotion dominante** (peur, frustration, espoir, scepticisme, désir, méfiance...)
- **Besoin profond** (sécurité, gain de temps, revenu, reconnaissance, simplicité...)
- **Objection implicite** (ce qui n'est pas dit mais bloque l'achat)
- **Déclencheur de conversion** (qu'est-ce qui les ferait dire oui ?)

---

## 2. PATTERNS RÉCURRENTS

Regroupe les feedbacks par thèmes émotionnels :
- Peurs les plus fréquentes (avec %)
- Désirs les plus fréquents (avec %)
- Objections les plus bloquantes
- Signaux de haute intention d'achat

---

## 3. CE QUE LE COPYWRITING DOIT DIRE

Basé sur les émotions détectées, rédige :

**Phrase d'accroche pour chaque peur principale** :
→ Peur de Google : "..."
→ Peur du prix : "..."
→ Peur de ne pas avoir le temps : "..."

**Arguments de vente émotionnels** (pas rationnels) :
→ ...

**Ce qu'il ne faut JAMAIS dire** (déclenche une résistance) :
→ ...

---

## 4. RECOMMANDATIONS PRODUIT

Fonctionnalités ou changements UX à prioriser basés sur les émotions :
1. ...
2. ...
3. ...

---

## 5. SCRIPT DE VENTE EMPATHIQUE

Rédige un mini-script pour répondre à l'objection la plus fréquente, qui :
- Valide l'émotion du prospect (ne la contredit pas)
- Reformule son besoin profond
- Répond avec une preuve, pas une promesse
- Se termine par une question ouverte
"""

    print(f"\n🧠 Analyse Émotionnelle des Prospects\n{'='*60}")
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
        path = OUTPUT_DIR / f"emotions_prospects_{date_str}.md"
        path.write_text(f"# Analyse Émotionnelle — {date_str}\n\n{content}", encoding="utf-8")
        print(f"\n✅ Sauvegardé : {path}")
        return str(path)
    return ""


if __name__ == "__main__":
    # Usage : uv run python agents/emotion_analyzer.py "feedback1|feedback2|..."
    feedbacks = sys.argv[1].replace("|", "\n") if len(sys.argv) > 1 else DEFAULT_FEEDBACKS
    asyncio.run(analyze_emotions(feedbacks))
