#!/usr/bin/env python3
"""
generer_registre_erreurs — le registre `🔴 ERREURS.md` est DÉRIVÉ, jamais recopié.

POURQUOI CE SCRIPT EXISTE
Le CODEX §12 impose `/🔴 ERREURS.md` à la racine. Une chaîne parallèle avait par ailleurs créé
`.claude/BASE-ERREURS.md` avec des fiches détaillées. Résultat au 2026-09-11 : **deux registres
d'erreurs**, formats différents, contenus qui se recoupent, et rien pour les comparer. C'est la fiche
E-18 — deux sources de vérité pour la même question — commise dans le dispositif écrit pour l'empêcher.

LA CORRECTION N'EST PAS « CHOISIR UN CAMP »
`.claude/BASE-ERREURS.md` **fait foi** : c'est là que vivent les fiches (cause racine, signal de
détection, contre-mesure). `🔴 ERREURS.md` en est l'**index généré**, au format attendu par le §12.
Un index dérivé ne peut pas dériver : il est reconstruit, et la CI échoue s'il ne correspond plus.

C'est la contre-mesure d'E-18 appliquée à la lettre : une source qui fait foi, une autre subordonnée,
et un contrôle qui vérifie qu'elles s'accordent.

USAGE
    python3 scripts/generer_registre_erreurs.py              # régénère le registre
    python3 scripts/generer_registre_erreurs.py --verifier   # sort en 1 s'il n'est plus à jour (CI)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BASE = RACINE / ".claude" / "BASE-ERREURS.md"
REGISTRE = RACINE / "🔴 ERREURS.md"

EN_TETE = """# 🔴 ERREURS.md — registre des erreurs (réelles, datées, avec correction)

> Une erreur = une ligne datée. On ne supprime pas une erreur corrigée : on la marque CORRIGÉE (traçabilité).
> Vérité totale : une erreur cachée est une erreur qui reviendra. Le plus récent en haut.
>
> ⚠️ **CE FICHIER EST GÉNÉRÉ — ne pas l'éditer à la main.**
> Source unique : `.claude/BASE-ERREURS.md`, où chaque erreur a une fiche complète (cause racine,
> signal de détection, contre-mesure, rôle responsable). Ce registre en est l'index, au format §12.
> Régénérer : `python3 scripts/generer_registre_erreurs.py`
> La CI vérifie qu'il est à jour ; une modification manuelle sera écrasée à la prochaine génération.

| Date | Erreur | Statut | Fiche complète |
|---|---|---|---|
"""


def fiches() -> list[tuple[str, str, str, str]]:
    """(id, titre, date, statut) — lu depuis la base, qui fait foi."""
    texte = BASE.read_text(encoding="utf-8")
    out = []
    # Le bloc de métadonnées va du titre jusqu'à la première ligne vide ou au récit.
    # Il peut tenir sur PLUSIEURS lignes : ne lire que la première fait manquer un « État »
    # reporté à la ligne suivante — défaut réel constaté sur E-17 le 2026-09-11, dont le
    # statut ressortait « DOCUMENTÉE » alors que sa fiche disait « corrigé ».
    for m in re.finditer(
        r"^## (E-\d+) — (.+?)\n(.*?)(?=\n\s*\n|\n\*\*Ce qui s'est passé)", texte, re.MULTILINE | re.DOTALL
    ):
        ident, titre, meta = m.group(1), m.group(2).strip(), m.group(3)
        date = dm.group(1) if (dm := re.search(r"Constaté le\*{0,2}\s*(\d{4}-\d{2}-\d{2})", meta)) else "date inconnue"
        # Statut déduit du seul vocabulaire présent dans la fiche — jamais inventé.
        bas = meta.lower()
        if "non corrigé" in bas or "non résolu" in bas:
            statut = "⚠️ NON CORRIGÉE"
        elif "corrigé" in bas:
            statut = "✅ CORRIGÉE"
        else:
            statut = "▫️ DOCUMENTÉE"      # leçon consignée, aucune correction revendiquée
        out.append((ident, titre, date, statut))
    return out


def rendu() -> str:
    lignes = fiches()
    if not lignes:
        raise SystemExit(f"Aucune fiche trouvée dans {BASE} — format modifié ? Rien n'a été écrit.")
    # Le plus récent en haut (exigence de l'en-tête §12) : les ID croissent avec le temps.
    lignes.sort(key=lambda t: int(t[0].split("-")[1]), reverse=True)
    corps = "".join(
        f"| {date} | {titre} | {statut} | [`{ident}`](.claude/BASE-ERREURS.md) |\n"
        for ident, titre, date, statut in lignes
    )
    return EN_TETE + corps + f"\n*{len(lignes)} fiches. Généré depuis `.claude/BASE-ERREURS.md`.*\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Génère ou vérifie le registre d'erreurs.")
    ap.add_argument("--verifier", action="store_true", help="sort en 1 si le registre n'est plus à jour")
    args = ap.parse_args()

    attendu = rendu()
    actuel = REGISTRE.read_text(encoding="utf-8") if REGISTRE.exists() else ""

    if args.verifier:
        if actuel == attendu:
            print(f"  ✅ REGISTRE_ERREURS — à jour ({len(fiches())} fiches)")
            return 0
        print("  ❌ REGISTRE_ERREURS — « 🔴 ERREURS.md » ne correspond plus à .claude/BASE-ERREURS.md")
        print("     Une erreur a été ajoutée à la base sans régénérer le registre, ou le registre a été")
        print("     édité à la main. Les deux feraient revivre la divergence de la fiche E-18.")
        print("     Corriger : python3 scripts/generer_registre_erreurs.py")
        return 1

    REGISTRE.write_text(attendu, encoding="utf-8")
    print(f"  🔴 ERREURS.md régénéré depuis la base — {len(fiches())} fiches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
