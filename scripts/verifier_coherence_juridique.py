#!/usr/bin/env python3
"""Contrôle de cohérence juridique entre la brochure et l'outil.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 2026-09-14, une correction juridique a été apportée à `index.html` — l'exception
qui oblige les entités financières et anti-blanchiment à disposer d'un canal de
signalement sans seuil d'effectif — et la session qui l'a écrite a annoncé que
« le site était corrigé ».

C'était faux. `assets/simulateur.js` portait encore les DEUX formulations fautives,
et rendait un verdict VERT « a priori non concerné » à une entité financière de
moins de 50 travailleurs. Le contradicteur l'a trouvé ; aucun contrôle ne l'avait vu.

La raison est structurelle : les contrôles existants lisent le code Python, les
secrets, les dépendances et les rapports. AUCUN ne lit le contenu juridique du site.
Une correction pouvait donc être appliquée à la page et pas à l'outil, ou effacée
par une refonte de mise en page, sans qu'une seule intégration continue s'en aperçoive.

C'est la leçon de la fiche E-01 : une règle sans mécanisme d'application n'est pas
une règle. Ce script est le mécanisme.

CE QU'IL SAIT FAIRE
-------------------
Pour chaque affirmation juridique sensible, il vérifie qu'une empreinte est présente
à la fois dans la page ET dans l'outil. Il ne juge pas la formulation : il constate
qu'aucun des deux supports n'a été corrigé sans l'autre.

CE QU'IL NE SAIT PAS FAIRE — à dire, pas à taire
------------------------------------------------
Il ne vérifie pas que le droit est correctement énoncé : seul un humain, ou un
recoupement à la source primaire, le peut. Il rend impossible une catégorie d'erreur
— la divergence silencieuse entre la brochure et l'outil — pas toutes.

Usage :  python3 scripts/verifier_coherence_juridique.py
Sortie :  0 si tout tient, 1 à la première divergence (contrôle bloquant en CI).
"""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SITE = RACINE / "products" / "caelum" / "site"
PAGE = SITE / "index.html"
OUTIL = SITE / "assets" / "simulateur.js"

# Chaque entrée : (libellé, empreinte attendue dans la PAGE, empreinte attendue dans l'OUTIL)
# Les empreintes sont volontairement courtes et stables : on veut détecter la DISPARITION
# d'une correction, pas imposer une formulation au mot près.
EXIGENCES = [
    (
        "Lanceurs d'alerte — exception sans seuil d'effectif",
        "quel que soit leur effectif",
        "SANS SEUIL",
    ),
    (
        "Lanceurs d'alerte — la branche anti-blanchiment est nommée",
        "blanchiment",
        "anti-blanchiment",
    ),
    (
        "CSRD — les deux seuils sont cumulatifs",
        "450 millions",
        "450 M€",
    ),
    (
        "CSRD — la directive n'est pas encore transposée en droit belge",
        "transposée en droit belge",
        "transposée en droit belge",
    ),
]


def main() -> int:
    for fichier in (PAGE, OUTIL):
        if not fichier.exists():
            print(f"::error::Fichier introuvable : {fichier.relative_to(RACINE)}")
            return 1

    page = PAGE.read_text(encoding="utf-8")
    outil = OUTIL.read_text(encoding="utf-8")

    manques: list[str] = []
    for libelle, att_page, att_outil in EXIGENCES:
        if att_page not in page:
            manques.append(f"{libelle} — absent de {PAGE.relative_to(RACINE)} (cherché : « {att_page} »)")
        if att_outil not in outil:
            manques.append(f"{libelle} — absent de {OUTIL.relative_to(RACINE)} (cherché : « {att_outil} »)")

    print()
    print("  CONTRÔLE DE COHÉRENCE JURIDIQUE — la page et l'outil disent-ils la même chose ?")
    print(f"  Affirmations contrôlées : {len(EXIGENCES)} · supports : la page d'accueil et le simulateur")
    print()

    if manques:
        print(f"  ❌ COHÉRENCE_JURIDIQUE — {len(manques)} divergence(s)")
        for m in manques:
            print(f"     – {m}")
        print()
        print("  " + "─" * 70)
        print("  VERDICT : ❌ la brochure et l'outil ne disent pas la même chose.")
        print("  Corriger LES DEUX, jamais un seul. Un visiteur qui utilise le simulateur")
        print("  lui fait davantage confiance qu'à une carte : il lui répond personnellement.")
        print("  " + "─" * 70)
        return 1

    for libelle, _, _ in EXIGENCES:
        print(f"  ✅ {libelle}")
    print()
    print("  " + "─" * 70)
    print("  VERDICT : ✅ la page et l'outil portent les mêmes corrections.")
    print("  Rappel honnête : ceci prouve que les deux supports ont été corrigés ensemble.")
    print("  Cela ne prouve pas que le droit y est correctement énoncé — seule une")
    print("  relecture à la source primaire le peut.")
    print("  " + "─" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
