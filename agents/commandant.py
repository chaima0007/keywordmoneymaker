"""
Agent COMMANDANT — Orchestrateur Stratégique Premium
Reçoit une mission en langage naturel, la décompose en sous-tâches,
délègue aux bons agents, agrège les résultats en rapport exécutif.
C'est le CEO de la flotte d'agents.
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache
import drive_audit

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR = PROJECT_ROOT / "commandant"

AGENT_REGISTRY = {
    "keyword_analyzer":     "Analyse SEO d'un mot-clé (volume, KD, opportunités)",
    "fast_analyzer":        "Analyse rapide mot-clé + idées (<30s, cache)",
    "report_generator":     "Rapport de performance hebdomadaire",
    "content_optimizer":    "Optimisation SEO d'un fichier HTML",
    "trend_radar":          "Détection mots-clés émergents avant la concurrence",
    "emotion_analyzer":     "Analyse émotionnelle des prospects (peurs, désirs, objections)",
    "monetization_detector":"Détection opportunités d'affiliation manquées dans un article",
    "pitch_deck_agent":     "Génération pitch deck investisseur (12 slides)",
    "cold_outreach_agent":  "Séquences de prospection froide par persona",
    "security_audit":       "Audit OWASP sécurité du projet",
    "secrets_scanner":      "Scan des secrets/credentials exposés dans le code",
    "parallel_runner":      "Lance plusieurs agents en parallèle simultanément",
}


async def _plan_mission(mission: str, journal: str = "") -> dict:
    """Demande à Claude de décomposer la mission en plan d'action.

    `journal` : résumé des travaux déjà effectués par la flotte (lu sur le Drive
    via drive_audit). Le COMMANDANT en tient compte pour ne pas refaire un travail
    déjà fait par un autre agent / service — c'est le protocole « regarder le
    Drive et agir en conséquence ».
    """
    params = {"mission": mission.strip().lower(), "journal": journal[:500]}
    cached = cache.get("commandant_plan", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    agents_list = "\n".join(f"- {k}: {v}" for k, v in AGENT_REGISTRY.items())
    contexte_journal = (
        f"\n{journal}\nTiens compte de ces travaux déjà faits : ne les refais pas, "
        f"complète-les ou enchaîne dessus.\n" if journal else ""
    )
    prompt = f"""Tu es COMMANDANT, l'orchestrateur stratégique d'une flotte d'agents IA pour KeywordMoneyMaker (plateforme SaaS SEO).

Mission reçue : "{mission}"
{contexte_journal}
Agents disponibles :
{agents_list}

Analyse la mission et génère un plan d'action JSON avec cette structure exacte :
{{
  "objectif": "résumé de la mission en 1 phrase",
  "priorite": "critique|haute|normale",
  "etapes": [
    {{
      "ordre": 1,
      "agent": "nom_agent",
      "params": {{"param1": "valeur1"}},
      "parallele_avec": [],
      "raison": "pourquoi cet agent pour cette étape"
    }}
  ],
  "kpis": ["KPI 1 à mesurer", "KPI 2"],
  "risques": ["Risque identifié 1"],
  "estimation_minutes": 5
}}

Réponds UNIQUEMENT avec le JSON valide, sans markdown ni explication."""

    content = ""
    try:
        async with asyncio.timeout(30):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception):
        pass

    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        plan = json.loads(content)
        cache.set("commandant_plan", params, json.dumps(plan), ttl_hours=6)
        return plan
    except json.JSONDecodeError:
        return {
            "objectif": mission,
            "priorite": "normale",
            "etapes": [],
            "kpis": [],
            "risques": ["Planification automatique échouée — exécution manuelle requise"],
            "estimation_minutes": 0,
        }


async def _execute_step(step: dict) -> dict:
    agent_name = step.get("agent", "")
    params = step.get("params", {})
    raison = step.get("raison", "")

    print(f"\n  → [{step.get('ordre', '?')}] {agent_name}")
    print(f"     {raison}")

    t0 = time.perf_counter()
    result = ""

    try:
        async with asyncio.timeout(120):
            if agent_name == "keyword_analyzer":
                from keyword_analyzer import analyze_keyword
                result = await analyze_keyword(
                    params.get("keyword", "seo ia"),
                    params.get("langue", "fr"),
                ) or ""
            elif agent_name == "fast_analyzer":
                from fast_analyzer import fast_keyword
                result = await fast_keyword(
                    params.get("keyword", "seo ia"),
                    params.get("langue", "fr"),
                ) or ""
            elif agent_name == "report_generator":
                from report_generator import generate_report
                result = await generate_report() or ""
            elif agent_name == "trend_radar":
                from trend_radar import detect_trends
                result = await detect_trends(
                    params.get("niche", "SEO et monétisation de contenu"),
                    params.get("langue", "fr"),
                ) or ""
            elif agent_name == "emotion_analyzer":
                from emotion_analyzer import analyze_emotions
                result = await analyze_emotions(
                    params.get("feedbacks", ""),
                ) or ""
            elif agent_name == "pitch_deck_agent":
                from pitch_deck_agent import generate_pitch
                result = await generate_pitch(
                    params.get("montant", "150 000€"),
                    params.get("investisseur", "business angel / seed fund"),
                ) or ""
            elif agent_name == "cold_outreach_agent":
                from cold_outreach_agent import generate_sequence
                result = await generate_sequence(
                    params.get("persona", "entrepreneur_solo"),
                    params.get("langue", "fr"),
                ) or ""
            elif agent_name == "security_audit":
                from security_audit import run_audit
                result = await run_audit() or ""
            elif agent_name == "secrets_scanner":
                from secrets_scanner import scan_project
                found, _ = await asyncio.get_event_loop().run_in_executor(None, scan_project)
                result = f"{found} secret(s) détecté(s)"
            else:
                result = f"Agent '{agent_name}' non disponible pour exécution directe"
    except asyncio.TimeoutError:
        result = "TIMEOUT (>120s)"
    except Exception as e:
        result = f"ERREUR : {type(e).__name__}: {e}"

    elapsed = round(time.perf_counter() - t0, 1)
    status = "ok" if not result.startswith(("TIMEOUT", "ERREUR")) else "error"
    print(f"     {'✅' if status == 'ok' else '❌'} {elapsed}s")
    return {"agent": agent_name, "status": status, "elapsed": elapsed, "result": result}


async def _generate_report(mission: str, plan: dict, executions: list[dict]) -> str:
    """Génère le rapport exécutif final."""
    results_summary = "\n".join(
        f"- {e['agent']} : {e['status']} ({e['elapsed']}s)"
        for e in executions
    )
    prompt = f"""Tu es COMMANDANT. Voici le bilan d'une mission exécutée par ta flotte d'agents.

Mission : {mission}
Objectif : {plan.get('objectif', '')}
KPIs suivis : {', '.join(plan.get('kpis', []))}

Résultats des agents :
{results_summary}

Rédige un rapport exécutif en français (400-600 mots) avec :
## RAPPORT COMMANDANT — {datetime.now().strftime('%d/%m/%Y %H:%M')}
### Bilan de Mission
### Ce qui a fonctionné
### Points d'attention
### Prochaines actions prioritaires (top 3)
### Score de mission /10"""

    content = ""
    try:
        async with asyncio.timeout(45):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception):
        content = "Rapport automatique indisponible. Voir les résultats ci-dessus."
    return content


async def execute_mission(mission: str) -> str:
    print(f"\n{'='*60}")
    print(f"  COMMANDANT — Mission reçue")
    print(f"  {mission}")
    print(f"{'='*60}")

    wall_start = time.perf_counter()

    # PROTOCOLE — Étape 0 : lire le journal d'audit (le Drive de la flotte)
    # pour agir en conséquence et ne pas doublonner le travail d'un autre agent.
    print("\n📚 Consultation du journal d'audit de la flotte...")
    journal = drive_audit.resume_journal(limit=15)
    print("  " + journal.splitlines()[0])

    print("\n🗂️  Planification en cours...")
    plan = await _plan_mission(mission, journal)
    print(f"  Objectif  : {plan.get('objectif', '?')}")
    print(f"  Priorité  : {plan.get('priorite', '?')}")
    print(f"  Étapes    : {len(plan.get('etapes', []))}")
    print(f"  Estimation: ~{plan.get('estimation_minutes', '?')} min")
    if plan.get("risques"):
        print(f"  Risques   : {plan['risques'][0]}")

    etapes = plan.get("etapes", [])
    executions: list[dict] = []

    if not etapes:
        print("\n⚠️  Aucune étape planifiée. Mission enregistrée pour exécution manuelle.")
    else:
        print(f"\n⚡ Exécution ({len(etapes)} étape(s))...")

        parallel_groups: dict[int, list[dict]] = {}
        for step in etapes:
            groupe = step.get("ordre", 999)
            parallel_groups.setdefault(groupe, []).append(step)

        for ordre in sorted(parallel_groups.keys()):
            groupe = parallel_groups[ordre]
            if len(groupe) == 1:
                executions.append(await _execute_step(groupe[0]))
            else:
                results = await asyncio.gather(*[_execute_step(s) for s in groupe])
                executions.extend(results)

    print("\n📝 Génération du rapport exécutif...")
    rapport = await _generate_report(mission, plan, executions)
    print(rapport)

    wall = round(time.perf_counter() - wall_start, 1)
    ok = sum(1 for e in executions if e["status"] == "ok")
    print(f"\n{'='*60}")
    print(f"  Mission terminée en {wall}s | {ok}/{len(executions)} étapes réussies")
    print(f"{'='*60}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    safe = mission[:40].replace(" ", "_").replace("/", "-")
    path = OUTPUT_DIR / f"mission_{safe}_{date_str}.md"
    full_content = (
        f"# COMMANDANT — Mission\n"
        f"**Mission :** {mission}\n"
        f"**Date :** {date_str}\n"
        f"**Durée :** {wall}s\n\n"
        f"## Plan\n```json\n{json.dumps(plan, ensure_ascii=False, indent=2)}\n```\n\n"
        f"## Rapport Exécutif\n{rapport}"
    )
    path.write_text(full_content, encoding="utf-8")
    print(f"  Rapport : {path}")

    # PROTOCOLE — Étape finale : déposer un audit propre (titre + synopsis)
    # dans le journal de la flotte, pour Chaima et les agents collègues.
    try:
        synopsis = (
            f"Mission « {plan.get('objectif', mission)[:120]} » exécutée par la flotte : "
            f"{ok}/{len(executions)} étape(s) réussie(s) en {wall}s. "
            f"Agents mobilisés : {', '.join(e['agent'] for e in executions) or 'aucun'}."
        )
        audit_path = drive_audit.record_audit(
            agent="commandant",
            sujet=f"Mission — {mission[:60]}",
            synopsis=synopsis,
            statut="ok" if ok == len(executions) and executions else "attention",
            service="Orchestration",
            details=f"Rapport complet : {path}",
        )
        print(f"  Audit  : {audit_path}")
    except Exception as e:
        print(f"  ⚠️  Audit non déposé : {type(e).__name__}: {e}")

    return str(path)


if __name__ == "__main__":
    mission = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else (
        "Analyser les meilleures opportunités SEO pour KeywordMoneyMaker "
        "et générer une séquence de prospection pour les agences digitales"
    )
    asyncio.run(execute_mission(mission))
