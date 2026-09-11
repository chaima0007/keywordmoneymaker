#!/usr/bin/env python3
"""
audit_cloisonnement — le cloisonnement des produits est-il tenu ?

POURQUOI CE CONTRÔLE EXISTE
Ce dépôt héberge trois produits (Caelum Partners, KeywordMoneyMaker, CompeteIQ). La base d'erreurs
documente deux fois le même échec : une règle sans mécanisme d'application n'est pas une règle
(fiches E-01 et E-07). Un cloisonnement tenu par la discipline seule finit par céder. Ce script le
rend vérifiable par la machine.

TROIS CONTRÔLES
  C1 — aucun module d'un produit n'importe un module d'un autre produit.
  C2 — la racine du dépôt reste propre : aucun répertoire de premier niveau hors liste autorisée.
  C3 — `shared/` ne dépend d'aucun produit (sinon le cloisonnement fuit par le bas).

DEUX MODES
  --avertir   (défaut) : rapporte et sort en 0. Mode de la phase 1 : on mesure l'état réel avant
              de déplacer quoi que ce soit, plutôt que de le supposer.
  --bloquant  : sort en 1 si un contrôle échoue. Mode de la phase 5, branché sur la CI.

DEUX DISPOSITIONS RECONNUES
  Avant migration : tous les modules dans `agents/` à plat. Le rattachement vient de ATTRIBUTION
  ci-dessous. C'est cette disposition qui permet de mesurer les dépendances croisées AVANT de bouger.
  Après migration : `products/<produit>/agents/` et `shared/`. Le rattachement vient du chemin.

L'analyse est faite par AST (`ast.parse`), pas par `grep` : un grep rate les imports écrits
autrement et se trompe sur les commentaires et les chaînes de caractères.
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# ── Rattachement déclaré des modules (disposition « avant migration ») ─────────
# Source : la liste AGENTS et le dictionnaire CATEGORIES de main.py, lus le 2026-09-11.
# Un module ne figure ici que s'il sert UN produit. Tout le reste est transverse, donc `shared`.
ATTRIBUTION: dict[str, str] = {
    # ── Caelum Partners — conformité, juridique, fiscal (CATEGORIES « JURIDIQUE & FISC. »)
    "avocat": "caelum",
    "fiscaliste": "caelum",
    "contrat_forge": "caelum",
    "contrat_client_expert": "caelum",
    "gdpr_garde": "caelum",
    # ── KeywordMoneyMaker — SEO et contenu (CATEGORIES « SEO & CONTENU »)
    "keyword_analyzer": "kmm",
    "fast_analyzer": "kmm",
    "report_generator": "kmm",
    "content_optimizer": "kmm",
    "trend_radar": "kmm",
    "monetization_detector": "kmm",
    # Reclassés le 2026-09-11 sur PREUVE D'IMPORTS, pas sur interprétation : la phase 1 a montré
    # que ces modules importent keyword_analyzer / trend_radar / report_generator / fast_analyzer /
    # content_optimizer, tous KMM. Ce sont des orchestrateurs du pipeline SEO, pas du transverse.
    # L'interprétation initiale (les catégories de main.py) les disait transverses : elle avait tort.
    "commandant": "kmm",
    "parallel_runner": "kmm",
    "run_all": "kmm",
    # PROVISOIRE — DÉCISION REQUISE DE CHAIMA.
    # `superviseur` s'annonce « scan santé de la flotte », donc transverse par intention, mais il
    # n'inspecte en pratique que des modules KMM. Rattaché à kmm pour refléter le code tel qu'il est.
    # Si l'intention est bien de superviser les trois produits, il doit repasser en transverse ET
    # perdre ses imports KMM directs — ce qui est un vrai refactor, pas un déplacement.
    "superviseur": "kmm",
    # ── CompeteIQ — intelligence concurrentielle (CATEGORIES « COMPETEIQ »)
    "competitor_tracker": "competeiq",
    "battle_card_generator": "competeiq",
    "signal_detector": "competeiq",
    "competeiq_orchestrator": "competeiq",
}

# Transverse par nature : sécurité, pilotage, orchestration, cache, outillage.
# Ces modules iront dans `shared/`. Les lister explicitement évite qu'un module nouveau
# devienne transverse par défaut, sans décision.
TRANSVERSES = {
    "__init__", "base_erreurs",
    "security_audit", "secrets_scanner", "security_hardener", "dependency_checker",
    "resolveur", "innovateur",
    "decision_simulator", "source_validator", "cache_manager",
    "emotion_analyzer", "pitch_deck_agent", "cold_outreach_agent", "linkedin_cv_agent",
}

PRODUITS = {"caelum", "kmm", "competeiq"}
RACINE_AUTORISEE = {".claude", ".github", "products", "shared", "scripts", "reports", "assets"}


def _imports(fichier: Path) -> set[str]:
    """Les noms de modules importés par ce fichier, par analyse AST."""
    try:
        arbre = ast.parse(fichier.read_text(encoding="utf-8"), filename=str(fichier))
    except (OSError, SyntaxError) as e:
        print(f"     – {fichier.relative_to(RACINE)} : NON ANALYSÉ ({e.__class__.__name__})")
        return set()
    noms: set[str] = set()
    for n in ast.walk(arbre):
        if isinstance(n, ast.Import):
            noms.update(a.name.split(".")[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom) and n.module:
            noms.add(n.module.split(".")[0])
    return noms


def _apres_migration() -> bool:
    return (RACINE / "products").is_dir()


def _modules() -> list[tuple[Path, str, str]]:
    """(fichier, nom de module, propriétaire) — propriétaire ∈ produits ∪ {shared, inconnu}."""
    out: list[tuple[Path, str, str]] = []
    if _apres_migration():
        for p in sorted((RACINE / "products").glob("*/agents/*.py")):
            out.append((p, p.stem, p.parents[1].name))
        for p in sorted((RACINE / "shared").glob("*.py")):
            out.append((p, p.stem, "shared"))
    else:
        for p in sorted((RACINE / "agents").glob("*.py")):
            nom = p.stem
            if nom in ATTRIBUTION:
                prop = ATTRIBUTION[nom]
            elif nom in TRANSVERSES:
                prop = "shared"
            else:
                prop = "inconnu"
            out.append((p, nom, prop))
    return out


def c1_imports_croises(mods) -> list[str]:
    """Un produit n'importe jamais un module d'un autre produit."""
    proprio = {nom: prop for _, nom, prop in mods}
    faux = []
    for fichier, nom, prop in mods:
        if prop not in PRODUITS:
            continue
        for imp in _imports(fichier):
            autre = proprio.get(imp)
            if autre in PRODUITS and autre != prop:
                faux.append(
                    f"{fichier.relative_to(RACINE)} (produit {prop}) importe « {imp} » "
                    f"qui appartient à {autre}"
                )
    return faux


def c2_racine_propre() -> list[str]:
    if not _apres_migration():
        return []
    faux = []
    for p in sorted(RACINE.iterdir()):
        if p.is_dir() and not p.name.startswith(".git") and p.name not in RACINE_AUTORISEE:
            if p.name.startswith("."):
                continue
            faux.append(f"répertoire de premier niveau non autorisé : {p.name}/")
    return faux


def c3_shared_independant(mods) -> list[str]:
    proprio = {nom: prop for _, nom, prop in mods}
    faux = []
    for fichier, nom, prop in mods:
        if prop != "shared":
            continue
        for imp in _imports(fichier):
            if proprio.get(imp) in PRODUITS:
                faux.append(
                    f"{fichier.relative_to(RACINE)} (shared) importe « {imp} » "
                    f"qui appartient à {proprio[imp]} — shared ne doit dépendre d'aucun produit"
                )
    return faux


def main() -> int:
    ap = argparse.ArgumentParser(description="Contrôle du cloisonnement des produits.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--avertir", action="store_true", help="rapporte sans échouer (défaut)")
    g.add_argument("--bloquant", action="store_true", help="sort en 1 si un contrôle échoue")
    args = ap.parse_args()
    bloquant = args.bloquant

    mods = _modules()
    disposition = "APRÈS migration (products/ + shared/)" if _apres_migration() else "AVANT migration (agents/ à plat)"
    print(f"\n  Disposition détectée : {disposition}")
    print(f"  Modules analysés : {len(mods)}")

    repartition: dict[str, int] = {}
    for _, _, prop in mods:
        repartition[prop] = repartition.get(prop, 0) + 1
    print("  Répartition : " + " · ".join(f"{k} {v}" for k, v in sorted(repartition.items())))

    inconnus = [n for _, n, p in mods if p == "inconnu"]
    echecs = 0

    print()
    for titre, faux in (
        ("C1 IMPORTS_CROISES", c1_imports_croises(mods)),
        ("C2 RACINE_PROPRE", c2_racine_propre()),
        ("C3 SHARED_INDEPENDANT", c3_shared_independant(mods)),
    ):
        if faux:
            echecs += 1
            print(f"  {'❌' if bloquant else '⚠️ '} {titre} — {len(faux)} problème(s)")
            for f in faux:
                print(f"     – {f}")
        else:
            print(f"  ✅ {titre} — aucun problème")

    if inconnus:
        echecs += 1
        print(f"  {'❌' if bloquant else '⚠️ '} RATTACHEMENT — {len(inconnus)} module(s) non rattaché(s)")
        for n in inconnus:
            print(f"     – {n} : ni dans ATTRIBUTION, ni dans TRANSVERSES → décision requise")
        print("     Un module non rattaché ne devient JAMAIS transverse par défaut.")
    else:
        print("  ✅ RATTACHEMENT — tous les modules sont rattachés explicitement")

    print("\n" + "─" * 72)
    if echecs == 0:
        print("  VERDICT : ✅ cloisonnement tenu.")
    elif bloquant:
        print(f"  VERDICT : ❌ {echecs} contrôle(s) en échec — mode bloquant, on ne pousse pas.")
    else:
        print(f"  VERDICT : ⚠️  {echecs} contrôle(s) en échec — mode avertissement, sortie 0.")
    print("  Rappel honnête : ceci contrôle les imports statiques et l'arborescence.")
    print("  Un import dynamique (importlib, __import__) échappe à l'analyse AST.")
    print("─" * 72 + "\n")

    return 1 if (bloquant and echecs) else 0


if __name__ == "__main__":
    sys.exit(main())
