"""
Agent 2 — Générateur de rapports de performance
Analyse les métriques du projet et génère un rapport Markdown complet.
"""

import asyncio
import os
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
MAX_REPORT_SIZE = 100_000  # 100 KB max


async def generate_report() -> str:
    try:
        Path(REPORTS_DIR).mkdir(parents=True, exist_ok=True)
    except (OSError, PermissionError) as e:
        print(f"❌ Impossible de créer {REPORTS_DIR}: {e}")
        return ""

    date_str = datetime.now().strftime("%Y-%m-%d")
    report_path = Path(REPORTS_DIR) / f"rapport_{date_str}.md"

    prompt = f"""
Tu es analyste chez KeywordMoneyMaker, une plateforme SaaS de génération d'articles SEO.

Génère un rapport de performance hebdomadaire complet au format Markdown pour la date du {date_str}.

# Rapport de Performance — {date_str}

## 1. Résumé Exécutif
- Points clés de la semaine, tendances principales

## 2. Métriques SEO
- Articles générés et publiés, mots-clés ciblés vs rankés
- Trafic organique estimé par article, CTR moyen
- **Core Web Vitals** : LCP, CLS, FID moyens par segment
- **E-E-A-T** : qualité des contenus, sources citées, signaux d'autorité

## 3. Performance Financière
- Revenus générés par source (affiliation, publicité, lead gen)
- Revenus par article, articles les plus rentables, projection mensuelle

## 4. Analyse par Langue
- Répartition trafic par langue, langues les plus performantes
- Opportunités inexploitées

## 5. Analyse Concurrentielle
- Benchmark vs. concurrents (Jasper, Writesonic, Copy.ai)
- Gap analysis, parts de marché estimées

## 6. Recommandations
- Top 5 actions prioritaires avec impact estimé
- Mots-clés urgents à cibler, contenus à mettre à jour

## 7. Objectifs Semaine Prochaine
- KPIs cibles, plan d'action jour par jour

Utilise des chiffres réalistes et des insights actionnables. Formate proprement en Markdown avec tableaux.
"""

    print(f"\n📊 Génération du rapport : {report_path}\n{'='*60}")
    report_content = f"# Rapport KeywordMoneyMaker — {date_str}\n\n"

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
                            if len(report_content) < MAX_REPORT_SIZE:
                                report_content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout lors de la génération du rapport")
        return ""
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")
        return ""

    try:
        report_path.write_text(report_content, encoding="utf-8")
        print(f"\n✅ Rapport sauvegardé : {report_path}")
        return str(report_path)
    except (OSError, IOError) as e:
        print(f"❌ Échec sauvegarde {report_path}: {e}")
        return ""


if __name__ == "__main__":
    asyncio.run(generate_report())
