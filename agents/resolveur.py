"""
Agent RÉSOLVEUR — Diagnostic & Résolution Premium
Reçoit n'importe quel problème (technique, SEO, business, code, performance),
diagnostique la cause racine, génère un plan correctif priorisé
et peut auto-corriger les problèmes détectés dans le code.
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

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR = PROJECT_ROOT / "resolutions"

PROBLEM_CATEGORIES = {
    "seo":         "Trafic organique, classements, mots-clés, Core Web Vitals, E-E-A-T",
    "securite":    "Vulnérabilités OWASP, secrets exposés, CVE, XSS, injection",
    "performance": "Latence agents, temps de réponse API, cache, parallélisme",
    "business":    "Acquisition clients, conversion, pricing, personas, objections",
    "code":        "Bugs Python, imports, asyncio, erreurs runtime, refactoring",
    "contenu":     "Qualité articles, monétisation, affiliation, copywriting",
}


async def _diagnose(problem: str, context: str = "") -> dict:
    """Diagnostic approfondi par catégorie de problème."""
    params = {"problem": problem.strip().lower()[:200]}
    cached = cache.get("resolveur_diag", params)
    if cached:
        try:
            return json.loads(cached)
        except json.JSONDecodeError:
            pass

    categories_str = "\n".join(f"- {k}: {v}" for k, v in PROBLEM_CATEGORIES.items())
    context_block = f"\nContexte additionnel :\n{context}" if context else ""

    prompt = f"""Tu es RÉSOLVEUR, expert en diagnostic et résolution de problèmes pour une plateforme SaaS SEO (KeywordMoneyMaker).

Problème déclaré : "{problem}"{context_block}

Catégories disponibles :
{categories_str}

Génère un diagnostic JSON avec cette structure exacte :
{{
  "categorie": "seo|securite|performance|business|code|contenu",
  "severite": "critique|haute|moyenne|faible",
  "cause_racine": "explication précise de la vraie cause en 2-3 phrases",
  "symptomes": ["symptôme visible 1", "symptôme visible 2"],
  "impacts": {{
    "revenu": "impact estimé sur les revenus (ex: -30% trafic = -500€/mois)",
    "technique": "impact technique",
    "utilisateur": "impact sur l'expérience utilisateur"
  }},
  "solutions": [
    {{
      "priorite": 1,
      "action": "Action concrète et précise",
      "effort": "30min|2h|1jour|1semaine",
      "impact_attendu": "résultat mesurable attendu",
      "auto_corrigeable": true
    }}
  ],
  "solution_rapide": "1 action à faire maintenant en moins de 15 minutes",
  "prevention": "Comment éviter que ce problème se reproduise",
  "score_urgence": 8
}}

Réponds UNIQUEMENT avec le JSON valide, sans markdown ni explication."""

    content = ""
    try:
        async with asyncio.timeout(35):
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
        diag = json.loads(content)
        cache.set("resolveur_diag", params, json.dumps(diag), ttl_hours=2)
        return diag
    except json.JSONDecodeError:
        return {
            "categorie": "code",
            "severite": "moyenne",
            "cause_racine": problem,
            "symptomes": [problem],
            "impacts": {"revenu": "inconnu", "technique": "inconnu", "utilisateur": "inconnu"},
            "solutions": [{"priorite": 1, "action": "Analyser manuellement", "effort": "2h",
                           "impact_attendu": "Résolution du problème", "auto_corrigeable": False}],
            "solution_rapide": "Identifier la source du problème",
            "prevention": "Mettre en place des tests automatisés",
            "score_urgence": 5,
        }


async def _auto_fix_performance() -> str:
    """Correction automatique des problèmes de performance connus."""
    fixes = []

    expired = cache.purge_expired()
    if expired:
        fixes.append(f"✅ Cache purgé : {expired} entrée(s) expirée(s) supprimée(s)")

    run_all_path = PROJECT_ROOT / "agents" / "run_all.py"
    if run_all_path.exists():
        content = run_all_path.read_text(encoding="utf-8")
        if "parallel_runner" in content:
            fixes.append("✅ run_all.py : mode parallèle déjà activé")
        else:
            fixes.append("⚠️  run_all.py : mode parallèle non activé — exécuter agents/parallel_runner.py")

    stats = cache.stats()
    fixes.append(f"📦 Cache actuel : {stats['valid']} entrée(s) valide(s) sur {stats['total']}")

    return "\n".join(fixes) if fixes else "Aucune correction automatique disponible"


async def _auto_fix_security() -> str:
    """Lance un scan de sécurité rapide et retourne le rapport."""
    fixes = []
    try:
        from secrets_scanner import scan_project
        found, _ = await asyncio.get_event_loop().run_in_executor(None, scan_project)
        if found == 0:
            fixes.append("✅ Aucun secret exposé détecté")
        else:
            fixes.append(f"🚨 {found} secret(s) potentiel(s) trouvé(s) — vérifier manuellement")
    except Exception as e:
        fixes.append(f"⚠️  Scanner indisponible : {e}")

    gitignore = PROJECT_ROOT / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        if ".env" in content:
            fixes.append("✅ .gitignore : .env protégé")
        else:
            fixes.append("🚨 .gitignore : .env non protégé — ajouter manuellement")
    else:
        fixes.append("🚨 .gitignore manquant — créer avec agents/security_hardener.py")

    return "\n".join(fixes)


async def _generate_action_plan(problem: str, diag: dict) -> str:
    """Génère le plan d'action détaillé en langage naturel."""
    solutions_str = "\n".join(
        f"{s['priorite']}. {s['action']} ({s['effort']}) → {s['impact_attendu']}"
        for s in diag.get("solutions", [])
    )
    prompt = f"""Tu es RÉSOLVEUR. Rédige un plan d'action clair et actionnable en français.

Problème : {problem}
Catégorie : {diag.get('categorie', '?')}
Sévérité  : {diag.get('severite', '?')}
Cause racine : {diag.get('cause_racine', '?')}

Solutions identifiées :
{solutions_str}

Solution rapide : {diag.get('solution_rapide', '?')}
Prévention : {diag.get('prevention', '?')}

Rédige un plan d'action en 300-400 mots avec :
## PLAN D'ACTION RÉSOLVEUR
### Diagnostic
### Actions immédiates (aujourd'hui)
### Actions court terme (cette semaine)
### Comment mesurer la résolution
### Prévention future"""

    content = ""
    try:
        async with asyncio.timeout(40):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except (asyncio.TimeoutError, Exception):
        content = f"Plan manuel requis. Cause racine : {diag.get('cause_racine', problem)}"
    return content


async def resolve(problem: str, context: str = "", auto_fix: bool = True) -> str:
    print(f"\n{'='*60}")
    print(f"  RÉSOLVEUR — Problème reçu")
    print(f"  {problem[:70]}{'...' if len(problem) > 70 else ''}")
    print(f"{'='*60}")

    wall_start = time.perf_counter()

    print("\n🔍 Diagnostic en cours...")
    diag = await _diagnose(problem, context)

    severity_icon = {"critique": "🔴", "haute": "🟠", "moyenne": "🟡", "faible": "🟢"}.get(
        diag.get("severite", ""), "⚪"
    )
    print(f"  Catégorie  : {diag.get('categorie', '?')}")
    print(f"  Sévérité   : {severity_icon} {diag.get('severite', '?').upper()}")
    print(f"  Cause      : {diag.get('cause_racine', '?')[:80]}")
    print(f"  Urgence    : {diag.get('score_urgence', '?')}/10")
    print(f"  Solution rapide : {diag.get('solution_rapide', '?')}")

    auto_fix_results = ""
    if auto_fix:
        cat = diag.get("categorie", "")
        print("\n🔧 Corrections automatiques...")
        if cat == "performance":
            auto_fix_results = await _auto_fix_performance()
        elif cat == "securite":
            auto_fix_results = await _auto_fix_security()
        if auto_fix_results:
            print(auto_fix_results)

    print("\n📋 Génération du plan d'action...")
    plan = await _generate_action_plan(problem, diag)
    print(plan)

    wall = round(time.perf_counter() - wall_start, 1)
    print(f"\n{'='*60}")
    print(f"  Résolution terminée en {wall}s")
    print(f"{'='*60}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    safe = problem[:40].replace(" ", "_").replace("/", "-")
    path = OUTPUT_DIR / f"resolution_{safe}_{date_str}.md"
    full_content = (
        f"# RÉSOLVEUR — {problem[:60]}\n"
        f"**Date :** {date_str} | **Durée :** {wall}s\n\n"
        f"## Diagnostic\n"
        f"- **Catégorie :** {diag.get('categorie', '?')}\n"
        f"- **Sévérité :** {severity_icon} {diag.get('severite', '?')}\n"
        f"- **Score urgence :** {diag.get('score_urgence', '?')}/10\n"
        f"- **Cause racine :** {diag.get('cause_racine', '?')}\n\n"
    )
    if diag.get("impacts"):
        imp = diag["impacts"]
        full_content += (
            f"## Impacts\n"
            f"- Revenu : {imp.get('revenu', '?')}\n"
            f"- Technique : {imp.get('technique', '?')}\n"
            f"- Utilisateur : {imp.get('utilisateur', '?')}\n\n"
        )
    if auto_fix_results:
        full_content += f"## Corrections automatiques\n{auto_fix_results}\n\n"
    full_content += f"{plan}\n\n"
    full_content += (
        f"## Données brutes\n"
        f"```json\n{json.dumps(diag, ensure_ascii=False, indent=2)}\n```\n"
    )
    path.write_text(full_content, encoding="utf-8")
    print(f"  Rapport : {path}")
    return str(path)


async def resolve_batch(problems: list[str]) -> list[str]:
    """Résout plusieurs problèmes en parallèle."""
    print(f"\n⚡ RÉSOLVEUR BATCH — {len(problems)} problème(s) en parallèle")
    results = await asyncio.gather(
        *[resolve(p, auto_fix=False) for p in problems],
        return_exceptions=True,
    )
    return [r if isinstance(r, str) else f"ERREUR: {r}" for r in results]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem_input = " ".join(sys.argv[1:])
        asyncio.run(resolve(problem_input))
    else:
        asyncio.run(resolve(
            "Les agents mettent 60 à 90 secondes à répondre, "
            "ce qui rend la plateforme inutilisable en production"
        ))
