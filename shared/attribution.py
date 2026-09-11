"""
attribution — à quel produit appartient chaque module ? SOURCE UNIQUE DE VÉRITÉ.

Lu par `scripts/audit_cloisonnement.py` (contrôle CI) ET par `main.py` (routage de la mémoire).
Il n'y a volontairement qu'une seule copie de cette table : deux copies divergeraient, et personne
ne remarquerait laquelle est obsolète (fiche E-01 de `.claude/BASE-ERREURS.md`).

Un module non déclaré ici n'est PAS transverse par défaut : il est « inconnu », et le contrôle CI
le signale pour qu'une décision soit prise. Le silence n'est pas une décision.
"""

from __future__ import annotations

from pathlib import Path

PRODUITS = ("caelum", "kmm", "competeiq")

# ── Modules rattachés à UN produit ─────────────────────────────────────────────
ATTRIBUTION: dict[str, str] = {
    # Caelum Partners — conformité, juridique, fiscal
    "avocat": "caelum",
    "fiscaliste": "caelum",
    "contrat_forge": "caelum",
    "contrat_client_expert": "caelum",
    "gdpr_garde": "caelum",
    # KeywordMoneyMaker — SEO et contenu
    "keyword_analyzer": "kmm",
    "fast_analyzer": "kmm",
    "report_generator": "kmm",
    "content_optimizer": "kmm",
    "trend_radar": "kmm",
    "monetization_detector": "kmm",
    # KeywordMoneyMaker — orchestrateurs du pipeline SEO.
    # Rattachés le 2026-09-11 sur PREUVE D'IMPORTS : ils importent keyword_analyzer,
    # trend_radar, report_generator, fast_analyzer, content_optimizer. Les catégories de
    # main.py les présentaient comme transverses — l'interprétation était fausse, le code
    # a tranché.
    "commandant": "kmm",
    "parallel_runner": "kmm",
    "run_all": "kmm",
    # PROVISOIRE — DÉCISION REQUISE DE CHAIMA.
    # `superviseur` s'annonce « scan santé de la flotte », donc transverse par intention,
    # mais n'inspecte en pratique que des modules KMM. Rattaché à kmm pour refléter le code
    # tel qu'il est. Le rendre réellement transverse est un refactor (couper ses imports
    # KMM directs), pas un déplacement.
    "superviseur": "kmm",
    # Récupérés le 2026-09-11 du travail du 2026-07-17 resté non fusionné.
    # Rattachés à kmm sur PREUVE D'IMPORTS : leur unique consommateur est
    # commandant.py (« import drive_audit », « from protocole import with_protocole »),
    # lui-même rattaché à kmm. Ils vivent dans products/kmm/agents/ à côté de lui.
    "drive_audit": "kmm",
    "protocole": "kmm",
    # CompeteIQ — intelligence concurrentielle
    "competitor_tracker": "competeiq",
    "battle_card_generator": "competeiq",
    "signal_detector": "competeiq",
    "competeiq_orchestrator": "competeiq",
}

# ── Modules transverses : sécurité, pilotage, outillage. Domicile : shared/ ────
TRANSVERSES: frozenset[str] = frozenset({
    "attribution", "base_erreurs",
    "security_audit", "secrets_scanner", "security_hardener", "dependency_checker",
    "resolveur", "innovateur", "decision_simulator", "source_validator", "cache_manager",
    "emotion_analyzer", "pitch_deck_agent", "cold_outreach_agent", "linkedin_cv_agent",
})


_RACINE = Path(__file__).resolve().parent.parent


def _carte_disque() -> dict[str, str]:
    """Propriétaire de chaque module tel qu'il est RANGÉ SUR LE DISQUE.

    Le disque primait déjà pour le contrôle CI après migration, alors que cette table
    servait encore au routage de la mémoire : deux sources de vérité pour la même
    question, donc la divergence qu'E-01 décrit — dans le module même censé l'empêcher.
    Trouvé par test piégé le 2026-09-11. Le disque fait désormais foi, la table ne sert
    plus que de repli et de garde-fou de cohérence (contrôle C4).
    """
    carte: dict[str, str] = {}
    for f in (_RACINE / "products").glob("*/agents/*.py"):
        if f.stem == "__init__":
            continue        # marqueur de paquet, pas un module : les imports sont à plat
        carte[f.stem] = f.parents[1].name
    for f in (_RACINE / "shared").glob("*.py"):
        if f.stem == "__init__":
            continue
        carte[f.stem] = "shared"
    return carte


def proprietaire(module: str) -> str:
    """« caelum » · « kmm » · « competeiq » · « shared » · « inconnu ».

    Le rangement sur le disque fait foi. La table déclarée sert de repli — utile avant
    migration, et pour un module importé sans fichier repérable.
    """
    depuis_disque = _carte_disque().get(module)
    if depuis_disque:
        return depuis_disque
    if module in ATTRIBUTION:
        return ATTRIBUTION[module]
    if module in TRANSVERSES:
        return "shared"
    return "inconnu"


def incoherences() -> list[str]:
    """Modules dont le rangement sur le disque contredit la table déclarée."""
    ecarts = []
    for module, sur_disque in sorted(_carte_disque().items()):
        declare = ATTRIBUTION.get(module) or ("shared" if module in TRANSVERSES else None)
        if declare is None:
            ecarts.append(f"{module} : rangé dans « {sur_disque} » mais absent de la table déclarée")
        elif declare != sur_disque:
            ecarts.append(f"{module} : rangé dans « {sur_disque} » mais déclaré « {declare} »")
    return ecarts
