"""
Agent 5 — Radar de Tendances Émergentes
Détecte les mots-clés qui COMMENCENT à monter avant que la concurrence s'y mette.
L'avantage du premier arrivé : ranker quand le KD est encore bas.
"""

import asyncio
import os
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

OUTPUT_DIR = Path(os.path.dirname(__file__)).parent / "reports"


async def detect_trends(niche: str = "SEO et monétisation de contenu", langue: str = "fr") -> str:
    prompt = f"""
Tu es un analyste en tendances digitales et veille stratégique.

Identifie les **10 opportunités de mots-clés émergents** dans la niche : "{niche}" (langue : {langue})
Ces mots-clés doivent être en PHASE DE MONTÉE — pas encore saturés, pas encore détectés par la masse.

Pour chaque opportunité :

### [Numéro]. [Mot-clé émergent]

| Indicateur | Valeur |
|---|---|
| Volume actuel | X req/mois (en hausse) |
| Tendance | % de croissance sur 6 mois |
| KD actuel | /100 (opportunité car < 40) |
| Fenêtre d'action | Combien de mois avant saturation |
| Signal détecté via | Reddit / Twitter / Google Trends / forums niche |

**Pourquoi ça monte** : explication du macro-trend sous-jacent (IA, régulation, changement comportemental...)

**Type de contenu à créer maintenant** :
- Format idéal (guide, liste, comparatif, étude de cas...)
- Angle différenciant pour arriver 1er
- Monétisation anticipée

**Score d'urgence** : 🔴 Agir dans 30 jours / 🟠 60 jours / 🟡 90 jours

---

Catégories à couvrir :
1. Tendances IA génératives (nouveaux usages, nouvelles craintes)
2. Changements d'algorithme Google (ce que les gens cherchent maintenant)
3. Nouvelles niches de monétisation (affiliation, SaaS B2B, formations)
4. Mots-clés liés aux crises (économie, emploi, reconversion)
5. Tendances saisonnières imminentes (dans les 60 prochains jours)

Termine par un **tableau récapitulatif priorisé** avec score d'urgence et potentiel de revenus.
"""

    print(f"\n📡 Radar Tendances Émergentes — {niche}\n{'='*60}")
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
        path = OUTPUT_DIR / f"tendances_{date_str}.md"
        path.write_text(f"# Radar Tendances Émergentes — {date_str}\n\n{content}", encoding="utf-8")
        print(f"\n✅ Sauvegardé : {path}")
        return str(path)
    return ""


if __name__ == "__main__":
    import sys
    niche = sys.argv[1] if len(sys.argv) > 1 else "SEO et monétisation de contenu"
    langue = sys.argv[2] if len(sys.argv) > 2 else "fr"
    asyncio.run(detect_trends(niche, langue))
