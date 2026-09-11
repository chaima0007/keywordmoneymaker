"""
attribution — à quel produit appartient chaque module ? SOURCE UNIQUE DE VÉRITÉ.

Lu par `scripts/audit_cloisonnement.py` (contrôle CI) ET par `main.py` (routage de la mémoire).
Il n'y a volontairement qu'une seule copie de cette table : deux copies divergeraient, et personne
ne remarquerait laquelle est obsolète (fiche E-01 de `.claude/BASE-ERREURS.md`).

Un module non déclaré ici n'est PAS transverse par défaut : il est « inconnu », et le contrôle CI
le signale pour qu'une décision soit prise. Le silence n'est pas une décision.
"""

from __future__ import annotations

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


def proprietaire(module: str) -> str:
    """« caelum » · « kmm » · « competeiq » · « shared » · « inconnu »."""
    if module in ATTRIBUTION:
        return ATTRIBUTION[module]
    if module in TRANSVERSES:
        return "shared"
    return "inconnu"
