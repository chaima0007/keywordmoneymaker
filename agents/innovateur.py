"""
Agent INNOVATEUR — Veille Technologique & Recommandations de Pointe
Analyse les dernières avancées IA/tech, identifie ce que Caelum Partners
doit adopter maintenant pour rester 18 mois en avance sur la concurrence.
Agent surqualifié : synthèse multi-sources, recommandations actionnables.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "innovation"

DOMAINES_VEILLE = {
    "ia_agents":     "Nouveaux frameworks d'agents IA (LangGraph, CrewAI, AutoGen, A2A protocol)",
    "seo_2025":      "SEO à l'ère de l'IA : AIO, SGE, recherche vocale, featured snippets",
    "monetisation":  "Nouveaux modèles de monétisation SaaS : usage-based, AI credits, agents-as-a-service",
    "securite_ia":   "Sécurité des systèmes IA : prompt injection, jailbreak, poisoning, détection",
    "tech_stack":    "Stack technique optimal pour SaaS IA 2025 : infra, observabilité, déploiement",
    "ux_ia":         "UX des produits IA : attentes utilisateurs, patterns de confiance, explainability",
}


async def veille(domaine: str = "ia_agents", profondeur: str = "expert") -> str:
    params = {"domaine": domaine, "profondeur": profondeur}
    cached = cache.get("innovateur", params)
    if cached:
        return cached

    domaine_desc = DOMAINES_VEILLE.get(domaine, domaine)

    prompt = f"""Tu es INNOVATEUR, l'agent de veille technologique surqualifié de Caelum Partners.
Tu surveilles les tendances tech avec 18 mois d'avance sur le marché.
Niveau de profondeur : {profondeur}

Domaine d'analyse : {domaine_desc}

---

## RAPPORT INNOVATEUR — {domaine.upper()}
*{datetime.now().strftime('%B %Y')}*

### 1. ÉTAT DE L'ART (Ce qui est vrai aujourd'hui)
Les 5 avancées les plus significatives des 90 derniers jours dans ce domaine.
Pour chaque avancée : impact réel vs hype, qui l'utilise déjà, niveau de maturité (TRL 1-9).

### 2. CE QUI ARRIVE DANS 6 MOIS
Signaux faibles actuels qui deviendront des standards dans 6 mois.
- Signal faible + preuve (où l'a-t-on vu ?)
- Implication pour Caelum Partners

### 3. CE QUE LA CONCURRENCE NE FAIT PAS ENCORE
Opportunité de premier entrant : technologies ou approches disponibles mais non exploitées
par les agences digitales et plateformes SaaS de taille similaire.

### 4. RECOMMANDATIONS POUR CAELUM PARTNERS
Technologies/approches à adopter maintenant (ROI > 3 mois) :

| Recommandation | Effort | Impact | Délai ROI | Priorité |
|----------------|--------|--------|-----------|---------|
| ...            | S/M/L  | €      | semaines  | 🔴/🟠/🟡 |

### 5. CE QU'IL NE FAUT PAS FAIRE
Technologies surévaluées à éviter en 2025 (hype sans substance) + pourquoi.

### 6. RESSOURCES POUR ALLER PLUS LOIN
- 3 papers/articles de référence (titres et auteurs, sans URLs inventées)
- 2 communautés/forums où suivre ce domaine
- 1 outil open-source à tester immédiatement

### 7. SCORE D'OPPORTUNITÉ POUR CAELUM
Note /10 + justification : dans quelle mesure ce domaine est actionnable maintenant ?"""

    print(f"\n🔬 INNOVATEUR — Veille {domaine}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(80):
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
        print(f"❌ {type(e).__name__}: {e}")

    if content:
        cache.set("innovateur", params, content, ttl_hours=72)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        path = OUTPUT_DIR / f"innovation_{domaine}_{date_str}.md"
        path.write_text(
            f"# INNOVATEUR — {domaine_desc}\n*{date_str}*\n\n{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Rapport : {path}")
        return str(path)
    return ""


async def radar_complet() -> None:
    """Lance la veille sur tous les domaines critiques en parallèle."""
    domaines_prioritaires = ["ia_agents", "seo_2025", "monetisation", "tech_stack"]
    print(f"\n🚀 INNOVATEUR — Radar Technologique Complet ({len(domaines_prioritaires)} domaines)\n{'='*60}")
    results = await asyncio.gather(
        *[veille(d) for d in domaines_prioritaires],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/{len(domaines_prioritaires)} rapports dans innovation/")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        domaine_arg = sys.argv[1] if sys.argv[1] in DOMAINES_VEILLE else "ia_agents"
        asyncio.run(veille(domaine_arg))
    else:
        asyncio.run(radar_complet())
