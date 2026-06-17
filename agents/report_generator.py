"""
Agent 2 — Générateur de rapports de performance
Analyse les métriques du projet et génère un rapport Markdown complet.
"""

import asyncio
import os
from datetime import datetime
from claude_agent_sdk import query, ClaudeAgentOptions


REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")


async def generate_report() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_path = os.path.join(REPORTS_DIR, f"rapport_{date_str}.md")

    prompt = f"""
Tu es analyste chez KeywordMoneyMaker, une plateforme SaaS de génération d'articles SEO.

Génère un rapport de performance hebdomadaire complet au format Markdown pour la date du {date_str}.

Le rapport doit inclure :

# Rapport de Performance — {date_str}

## 1. Résumé Exécutif
- Points clés de la semaine
- Tendances principales

## 2. Métriques SEO
- Articles générés et publiés
- Mots-clés ciblés vs rankés
- Trafic organique estimé par article
- Taux de clic moyen (CTR)

## 3. Performance Financière
- Revenus générés (affiliation, publicité)
- Revenus par article
- Articles les plus rentables
- Projection mensuelle

## 4. Analyse par Langue
- Répartition du trafic par langue
- Langues les plus performantes
- Opportunités inexploitées

## 5. Recommandations
- Top 5 actions prioritaires pour la semaine suivante
- Mots-clés à cibler en urgence
- Contenus à mettre à jour

## 6. Objectifs Semaine Prochaine
- KPIs cibles
- Plan d'action détaillé

Utilise des chiffres réalistes et des insights actionnables. Formate proprement en Markdown.
"""

    print(f"\n📊 Génération du rapport : {report_path}\n{'='*60}")
    report_content = f"# Rapport KeywordMoneyMaker — {date_str}\n\n"

    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            allowed_tools=["Write"],
        ),
    ):
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                    report_content += block.text

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n✅ Rapport sauvegardé : {report_path}")
    return report_path


if __name__ == "__main__":
    asyncio.run(generate_report())
