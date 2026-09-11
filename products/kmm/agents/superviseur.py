"""
Agent SUPERVISEUR — Intelligence Collective & Coordination de Flotte
Détecte les agents en échec, bloqués ou sous-performants.
Les redirige, les reconfigue, les relance avec les bons paramètres.
Agent surqualifié : vision globale, décisions en temps réel.
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
OUTPUT_DIR   = PROJECT_ROOT / "supervision"

AGENT_FLEET = {
    "keyword_analyzer":     {"timeout": 60,  "categorie": "seo",      "critique": True},
    "report_generator":     {"timeout": 90,  "categorie": "analyse",  "critique": False},
    "content_optimizer":    {"timeout": 120, "categorie": "contenu",  "critique": False},
    "linkedin_cv_agent":    {"timeout": 300, "categorie": "vente",    "critique": False},
    "security_audit":       {"timeout": 120, "categorie": "securite", "critique": True},
    "secrets_scanner":      {"timeout": 60,  "categorie": "securite", "critique": True},
    "trend_radar":          {"timeout": 90,  "categorie": "seo",      "critique": False},
    "emotion_analyzer":     {"timeout": 90,  "categorie": "vente",    "critique": False},
    "monetization_detector":{"timeout": 120, "categorie": "revenu",   "critique": False},
    "pitch_deck_agent":     {"timeout": 120, "categorie": "business", "critique": False},
    "cold_outreach_agent":  {"timeout": 90,  "categorie": "vente",    "critique": False},
    "avocat":               {"timeout": 60,  "categorie": "juridique","critique": True},
    "fiscaliste":           {"timeout": 70,  "categorie": "fiscal",   "critique": True},
    "contrat_forge":        {"timeout": 90,  "categorie": "juridique","critique": False},
    "gdpr_garde":           {"timeout": 75,  "categorie": "securite", "critique": True},
    "commandant":           {"timeout": 300, "categorie": "strategie","critique": True},
    "resolveur":            {"timeout": 120, "categorie": "debug",    "critique": True},
}


def _scan_fleet_health() -> dict:
    """Vérifie l'état de santé de chaque agent (fichier existe, syntaxe ok)."""
    agents_dir = Path(__file__).parent
    statuses = {}
    for name in AGENT_FLEET:
        path = agents_dir / f"{name}.py"
        if not path.exists():
            statuses[name] = {"status": "MANQUANT", "taille": 0}
            continue
        size = path.stat().st_size
        if size < 200:
            statuses[name] = {"status": "VIDE", "taille": size}
            continue
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
            statuses[name] = {"status": "OK", "taille": size}
        except SyntaxError as e:
            statuses[name] = {"status": f"SYNTAXE_ERROR:{e.lineno}", "taille": size}
    return statuses


async def _diagnostic_avance(problemes: list[dict]) -> str:
    """Demande à Claude un diagnostic et un plan de relance pour les agents en échec."""
    if not problemes:
        return "Tous les agents sont opérationnels."

    problemes_str = "\n".join(
        f"- {p['agent']} : {p['status']} (critique={p.get('critique', False)})"
        for p in problemes
    )

    prompt = f"""Tu es SUPERVISEUR, l'agent surqualifié de la flotte Caelum Partners.
Tu détectes les agents défaillants et prescris des actions correctives précises.

Agents avec problèmes détectés :
{problemes_str}

Pour chaque agent défaillant, génère :
1. **Cause probable** de la défaillance
2. **Action corrective** (commande exacte ou étape précise)
3. **Alternative** si l'agent ne peut pas être relancé
4. **Priorité** : CRITIQUE (stoppe la production) ou NORMALE

Réponds en JSON :
{{
  "agents_critiques": ["nom1", "nom2"],
  "corrections": [
    {{
      "agent": "nom",
      "cause": "...",
      "correction": "commande ou action",
      "alternative": "...",
      "priorite": "CRITIQUE|NORMALE"
    }}
  ],
  "action_immediate": "1 phrase — ce qu'il faut faire maintenant"
}}"""

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

    try:
        data = json.loads(content.strip())
        return json.dumps(data, ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        return content


async def superviser(verbose: bool = True) -> dict:
    """Scan complet de la flotte + diagnostic IA des défaillances."""
    print(f"\n{'='*60}")
    print("  SUPERVISEUR — Scan de flotte en cours")
    print(f"{'='*60}")

    t0 = time.perf_counter()
    statuses = _scan_fleet_health()

    ok = [n for n, s in statuses.items() if s["status"] == "OK"]
    ko = [n for n, s in statuses.items() if s["status"] != "OK"]
    problemes = [
        {"agent": n, "status": statuses[n]["status"], "critique": AGENT_FLEET.get(n, {}).get("critique", False)}
        for n in ko
    ]

    print(f"\n📊 Flotte : {len(ok)} OK | {len(ko)} en anomalie\n")

    for name, info in statuses.items():
        icon = "✅" if info["status"] == "OK" else ("🔴" if AGENT_FLEET.get(name, {}).get("critique") else "🟠")
        size_kb = round(info["taille"] / 1024, 1)
        if verbose or info["status"] != "OK":
            print(f"  {icon} {name:<30} {info['status']:<25} {size_kb}Ko")

    cache_stats = cache.stats()
    print(f"\n📦 Cache : {cache_stats['valid']} entrées valides | {cache_stats['size_kb']}Ko")

    diagnostic = ""
    if problemes:
        print(f"\n🔧 Diagnostic IA des {len(problemes)} anomalie(s)...")
        diagnostic = await _diagnostic_avance(problemes)
        print(diagnostic)
    else:
        print("\n🎯 Flotte en parfait état. Aucune intervention requise.")

    elapsed = round(time.perf_counter() - t0, 1)
    rapport = {
        "date": datetime.now().isoformat(),
        "elapsed_s": elapsed,
        "total_agents": len(statuses),
        "ok": len(ok),
        "ko": len(ko),
        "agents_ok": ok,
        "agents_ko": ko,
        "diagnostic": diagnostic,
        "cache": cache_stats,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = OUTPUT_DIR / f"supervision_{date_str}.json"
    path.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"  Scan terminé en {elapsed}s | Rapport : {path}")
    print(f"{'='*60}")
    return rapport


async def relancer_agent(agent_name: str) -> bool:
    """Tente de relancer un agent spécifique avec son cas par défaut."""
    if agent_name not in AGENT_FLEET:
        print(f"❌ Agent inconnu : {agent_name}")
        return False

    print(f"\n🔄 SUPERVISEUR — Relance de {agent_name}...")
    try:
        if agent_name == "keyword_analyzer":
            from keyword_analyzer import analyze_keyword
            await asyncio.wait_for(analyze_keyword("seo ia test"), timeout=60)
        elif agent_name == "trend_radar":
            from trend_radar import detect_trends
            await asyncio.wait_for(detect_trends("SEO"), timeout=90)
        elif agent_name == "security_audit":
            from security_audit import run_audit
            await asyncio.wait_for(run_audit(), timeout=120)
        else:
            print(f"  ℹ️  Relance automatique non disponible pour {agent_name}")
            print(f"     Commande manuelle : uv run python agents/{agent_name}.py")
            return False
        print(f"  ✅ {agent_name} relancé avec succès")
        return True
    except Exception as e:
        print(f"  ❌ Échec relance : {e}")
        return False


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "scan"
    if mode == "relancer" and len(sys.argv) > 2:
        asyncio.run(relancer_agent(sys.argv[2]))
    else:
        asyncio.run(superviser(verbose="--verbose" in sys.argv or "--v" in sys.argv))
