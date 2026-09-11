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

# ── Source UNIQUE du rattachement ─────────────────────────────────────────────
# La table vivait ici ET dans main.py : deux copies divergeraient (fiche E-01).
# Elle est désormais dans shared/attribution.py, lue par ce contrôle ET par main.py.
sys.path.insert(0, str(RACINE / "shared"))
from attribution import ATTRIBUTION, TRANSVERSES, incoherences, proprietaire  # noqa: E402

PRODUITS = {"caelum", "kmm", "competeiq"}
RACINE_AUTORISEE = {
    ".claude", ".github", "products", "shared", "scripts", "reports",
    # `codex/` : protocole CODEX installé sur main par une autre session (29c22b9, ab6d4dd).
    # Gouvernance de niveau dépôt, comme .claude/ — pas un produit, donc autorisé ici.
    # Contient codex/agents-correspondance.md, la réconciliation menée en parallèle, et
    # codex/expertise/ que le rôle METTEUR À JOUR alimente.
    "codex",
    # `linkedin_cv/` a été RETIRÉ du dépôt par main (54a61c1) et ajouté au .gitignore :
    # l'entrée de tolérance n'a plus d'objet.
}


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
    """Vrai quand products/ existe : la phase 3 est passée."""
    return (RACINE / "products").is_dir()


def _modules() -> list[tuple[Path, str, str]]:
    """(fichier, nom de module, propriétaire) — propriétaire ∈ produits ∪ {shared, inconnu}."""
    out: list[tuple[Path, str, str]] = []
    # Sous products/ ou shared/, le propriétaire vient du CHEMIN : c'est la disposition cible.
    for p in sorted((RACINE / "products").glob("*/agents/*.py")):
        out.append((p, p.stem, p.parents[1].name))
    for p in sorted((RACINE / "shared").glob("*.py")):
        out.append((p, p.stem, "shared"))
    # Dans agents/ à plat, le propriétaire vient de la table déclarée. Ce cas subsiste
    # avant la phase 3 et disparaît une fois la migration terminée.
    for p in sorted((RACINE / "agents").glob("*.py")):
        if p.stem == "__init__":
            continue        # marqueur de paquet, pas un module : les imports sont à plat
        out.append((p, p.stem, proprietaire(p.stem)))
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
        if p.name.startswith(".") or p.name == "__pycache__":
            continue        # état local et artefacts de build : non versionnés, hors sujet
        if p.is_dir() and p.name not in RACINE_AUTORISEE:
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
        # C4 ajouté le 2026-09-11 après test piégé : le contrôle de rattachement devenait
        # inopérant après migration, le chemin suffisant à attribuer un module. Or la table
        # déclarée servait encore au routage de la mémoire — deux sources pouvaient donc
        # diverger en silence. C4 compare explicitement le disque et la table.
        ("C4 TABLE_vs_DISQUE", incoherences()),
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
