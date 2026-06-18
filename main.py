"""
Caelum Partners — Lanceur Central
Menu interactif pour accéder à tous les agents IA.
Lancement : uv run python main.py
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# ── Couleurs terminal ──────────────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
VIOLET = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
BG_DARK= "\033[40m"

ROOT = Path(__file__).parent
AGENTS_DIR = ROOT / "agents"
MEMORY_FILE = ROOT / ".caelum_memory.json"

sys.path.insert(0, str(AGENTS_DIR))


# ── Mémoire de session ─────────────────────────────────────────────────────────
def load_memory() -> dict:
    if MEMORY_FILE.exists():
        try:
            return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"sessions": 0, "agents_lances": {}, "derniere_session": None}


def save_memory(mem: dict) -> None:
    MEMORY_FILE.write_text(json.dumps(mem, ensure_ascii=False, indent=2), encoding="utf-8")


def record_launch(mem: dict, agent_name: str) -> None:
    mem["agents_lances"][agent_name] = mem["agents_lances"].get(agent_name, 0) + 1
    save_memory(mem)


# ── Affichage ──────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header(mem: dict):
    now = datetime.now().strftime("%d/%m/%Y  %H:%M")
    total_lancements = sum(mem["agents_lances"].values())
    agents_uniques   = len(mem["agents_lances"])
    sessions         = mem.get("sessions", 0)

    print(f"{VIOLET}{BOLD}")
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║          CAELUM PARTNERS — Centre de Commandement IA                ║")
    print("║              Chaima Mhadbi · Bruxelles · 2026                       ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(RESET)
    print(f"  {DIM}{now}{RESET}   "
          f"{GREEN}Sessions : {sessions}{RESET}   "
          f"{CYAN}Agents lancés : {total_lancements}{RESET}   "
          f"{YELLOW}Agents actifs : {agents_uniques}{RESET}")
    print()


AGENTS = [
    # num  label                    description                          module              fonction
    ( "1", "Orchestrateur",         "Tout déléguer — mission en texte", "commandant",       "execute_mission"),
    ( "2", "Résolveur Stratégique", "Diagnose + plan correctif complet","resolveur",        "resolve"),
    ( "3", "Mots-Clés SEO",         "Analyse SEO approfondie",          "keyword_analyzer", "analyze_keyword"),
    ( "4", "Analyse Rapide SEO",    "Résultat en <30s avec cache",      "fast_analyzer",    "fast_keyword"),
    ( "5", "Rapport Performance",   "Rapport hebdomadaire automatisé",  "report_generator", "generate_report"),
    ( "6", "Optimiseur Contenu",    "Optimise un fichier HTML",         "content_optimizer","optimize_all"),
    ( "7", "LinkedIn & CV",         "Posts, CV, À propos LinkedIn",     "linkedin_cv_agent","main"),
    ( "8", "Radar Tendances",       "Mots-clés émergents avant tous",   "trend_radar",      "detect_trends"),
    ( "9", "Analyse Émotions",      "Peurs, désirs, objections clients","emotion_analyzer", "analyze_emotions"),
    ("10", "Détecteur Monétisat.",  "Opportunités affiliation manquées","monetization_detector","scan_all_content"),
    ("11", "Pitch Deck",            "12 slides pour investisseurs",     "pitch_deck_agent", "generate_pitch"),
    ("12", "Cold Outreach",         "Séquences prospection 4 messages", "cold_outreach_agent","generate_all"),
    ("13", "Audit Sécurité",        "Audit OWASP du projet",            "security_audit",   "run_audit"),
    ("14", "Scanner Secrets",       "Détecte credentials exposés",      "secrets_scanner",  "scan_project"),
    ("15", "Durcissement Sécu.",    "Ajoute meta-tags + .gitignore",    "security_hardener","run_hardening"),
    ("16", "Vérif. Dépendances",    "CVE et packages obsolètes",        "dependency_checker","check_dependencies"),
    ("17", "AVOCAT",                "Analyse juridique & risques",      "avocat",           "audit_saas_complet"),
    ("18", "FISCALISTE",            "Optimisation fiscale Belgique",    "fiscaliste",       "bilan_annuel"),
    ("19", "CONTRAT_FORGE",         "Génère contrats et documents",     "contrat_forge",    "kit_juridique_complet"),
    ("20", "CONTRAT CLIENT",        "Contrats de signature premium",    "contrat_client_expert","generer_tous_modeles"),
    ("21", "GDPR_GARDE",            "Audit RGPD & conformité données",  "gdpr_garde",       "audit_complet_caelum"),
    ("22", "SUPERVISEUR",           "Scan santé de la flotte",          "superviseur",      "superviser"),
    ("23", "INNOVATEUR",            "Veille techno — 18 mois d'avance","innovateur",       "radar_complet"),
    ("24", "DECISION SIMULATOR",    "50 simulations avant de décider",  "decision_simulator","simulate"),
    ("25", "SOURCE VALIDATOR",      "Vérifie la fiabilité des sources", "source_validator", "valider_source"),
    # ── CompeteIQ ────────────────────────────────────────────────────────────
    ("26", "Tracker Concurrents",   "Fiches JSON par concurrent",       "competitor_tracker","track_all"),
    ("27", "Battle Cards",          "Armes commerciales anti-concurr.", "battle_card_generator","generate_from_tracker_output"),
    ("28", "Signal Detector",       "Signaux faibles concurrentiels",   "signal_detector",  "scan_all_competitors"),
    ("29", "Intel Orchestrator",    "Pipeline complet CompeteIQ",       "competeiq_orchestrator","run"),
    # ── Parallèle & Cache ────────────────────────────────────────────────────
    ("30", "Runner Parallèle",      "Lance N agents simultanément",     "parallel_runner",  "run_full_suite"),
    ("31", "Cache Manager",         "Stats + purge du cache",           "cache_manager",    "stats"),
]

CATEGORIES = {
    "SEO & CONTENU":     ["3","4","5","6","8","10"],
    "VENTE & GROWTH":    ["1","9","11","12"],
    "JURIDIQUE & FISC.": ["17","18","19","20","21"],
    "SÉCURITÉ":          ["13","14","15","16"],
    "COMPETEIQ":         ["26","27","28","29"],
    "PILOTAGE":          ["2","7","22","23","24","25","30","31"],
}

CAT_COLORS = {
    "SEO & CONTENU":     CYAN,
    "VENTE & GROWTH":    GREEN,
    "JURIDIQUE & FISC.": YELLOW,
    "SÉCURITÉ":          RED,
    "COMPETEIQ":         VIOLET,
    "PILOTAGE":          BLUE,
}


def menu(mem: dict):
    agents_index = {a[0]: a for a in AGENTS}

    for cat, nums in CATEGORIES.items():
        color = CAT_COLORS.get(cat, WHITE)
        print(f"  {color}{BOLD}── {cat} {'─'*(42-len(cat))}{RESET}")
        for num in nums:
            a = agents_index.get(num)
            if not a:
                continue
            n, label, desc = a[0], a[1], a[2]
            launches = mem["agents_lances"].get(label, 0)
            badge = f"{DIM}×{launches}{RESET}" if launches else ""
            print(f"  {color}[{n:>2}]{RESET}  {BOLD}{label:<26}{RESET}{DIM}{desc}{RESET}  {badge}")
        print()

    print(f"  {DIM}──────────────────────────────────────────────────────{RESET}")
    print(f"  {WHITE}[s]{RESET}  {DIM}Stats & mémoire{RESET}   "
          f"{WHITE}[r]{RESET}  {DIM}Tous les agents en parallèle{RESET}   "
          f"{WHITE}[0]{RESET}  {DIM}Quitter{RESET}")
    print()


def ask_param(label: str, default: str = "") -> str:
    prompt = f"  {CYAN}{label}{RESET}"
    if default:
        prompt += f" {DIM}[{default}]{RESET}"
    prompt += f" {BOLD}→{RESET} "
    val = input(prompt).strip()
    return val if val else default


async def launch_agent(num: str, mem: dict) -> None:
    agents_index = {a[0]: a for a in AGENTS}
    if num not in agents_index:
        print(f"  {RED}Choix invalide.{RESET}")
        return

    _, label, desc, module_name, func_name = agents_index[num]
    record_launch(mem, label)

    print(f"\n  {VIOLET}{BOLD}▶  {label}{RESET}  {DIM}{desc}{RESET}")
    print(f"  {'─'*60}")

    try:
        mod = __import__(module_name)
        func = getattr(mod, func_name)
    except ImportError as e:
        print(f"  {RED}Module introuvable : {module_name} — {e}{RESET}")
        return
    except AttributeError:
        print(f"  {RED}Fonction introuvable : {func_name} dans {module_name}{RESET}")
        return

    # Agents qui demandent un paramètre
    param_agents = {
        "3":  ("Mot-clé à analyser", "générateur articles seo ia"),
        "4":  ("Mot-clé (analyse rapide)", "outil seo ia"),
        "8":  ("Niche à surveiller", "SEO et monétisation de contenu"),
        "17": None,  # pas de param
        "24": ("Décision à simuler (50 scénarios)", "Lancer une offre CompeteIQ à 149€/mois"),
        "25": ("Information à valider", ""),
        "26": ("Concurrents séparés par espace", ""),
        "27": None,
        "28": None,
    }

    t0 = time.perf_counter()
    try:
        if num in param_agents and param_agents[num] is not None:
            hint, default = param_agents[num]
            val = ask_param(hint, default)
            if asyncio.iscoroutinefunction(func):
                if num == "26":
                    concurrents = [v.strip() for v in val.split() if v.strip()] or None
                    await func(concurrents)
                else:
                    await func(val)
            else:
                func(val)
        else:
            if asyncio.iscoroutinefunction(func):
                await func()
            else:
                result = func()
                if result:
                    print(result)
    except KeyboardInterrupt:
        print(f"\n  {YELLOW}Interrompu.{RESET}")
    except Exception as e:
        print(f"\n  {RED}Erreur : {type(e).__name__}: {e}{RESET}")

    elapsed = round(time.perf_counter() - t0, 1)
    print(f"\n  {DIM}{'─'*60}{RESET}")
    print(f"  {GREEN}✓ Terminé en {elapsed}s{RESET}")


def show_stats(mem: dict):
    print(f"\n  {BOLD}{VIOLET}MÉMOIRE DE SESSION{RESET}")
    print(f"  {'─'*50}")
    print(f"  Sessions totales    : {mem.get('sessions', 0)}")
    print(f"  Agents utilisés     : {len(mem['agents_lances'])}")
    print(f"  Lancements totaux   : {sum(mem['agents_lances'].values())}")
    print(f"  Dernière session    : {mem.get('derniere_session', 'Première fois')}")
    if mem["agents_lances"]:
        print(f"\n  {BOLD}Top agents :{RESET}")
        top = sorted(mem["agents_lances"].items(), key=lambda x: x[1], reverse=True)[:5]
        for name, count in top:
            bar = "█" * min(count, 20)
            print(f"  {CYAN}{name:<26}{RESET} {GREEN}{bar}{RESET} {count}×")

    # Stats cache
    try:
        import cache_manager as cm
        cs = cm.stats()
        print(f"\n  {BOLD}Cache :{RESET}")
        print(f"  Entrées valides : {cs['valid']} / {cs['total']}  ({cs['size_kb']} Ko)")
    except ImportError:
        pass


async def run_all_parallel(mem: dict):
    print(f"\n  {VIOLET}{BOLD}⚡ LANCEMENT PARALLÈLE — Suite complète{RESET}")
    print(f"  {DIM}Agents indépendants lancés simultanément…{RESET}\n")
    try:
        from parallel_runner import run_full_suite
        await run_full_suite()
    except Exception as e:
        print(f"  {RED}Erreur : {e}{RESET}")


async def main_loop():
    mem = load_memory()
    mem["sessions"] = mem.get("sessions", 0) + 1
    mem["derniere_session"] = datetime.now().isoformat()
    save_memory(mem)

    while True:
        clear()
        header(mem)
        menu(mem)

        try:
            choix = input(f"  {BOLD}Ton choix{RESET} {VIOLET}→{RESET} ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break

        if choix == "0":
            break
        elif choix == "s":
            show_stats(mem)
            input(f"\n  {DIM}Appuie sur Entrée…{RESET}")
        elif choix == "r":
            await run_all_parallel(mem)
            input(f"\n  {DIM}Appuie sur Entrée…{RESET}")
        elif choix in {a[0] for a in AGENTS}:
            await launch_agent(choix, mem)
            input(f"\n  {DIM}Appuie sur Entrée pour revenir au menu…{RESET}")
        else:
            print(f"  {RED}Choix invalide. Tape un numéro entre 1 et {len(AGENTS)}.{RESET}")
            time.sleep(1)

    clear()
    print(f"\n  {VIOLET}{BOLD}Caelum Partners — À bientôt.{RESET}")
    print(f"  {DIM}Session terminée · {datetime.now().strftime('%H:%M')}{RESET}\n")


if __name__ == "__main__":
    asyncio.run(main_loop())
