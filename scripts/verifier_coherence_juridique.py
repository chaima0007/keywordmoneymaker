#!/usr/bin/env python3
"""Contrôle de cohérence juridique entre la brochure et l'outil.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 2026-09-14, une correction juridique a été apportée à `index.html` et PAS à
`assets/simulateur.js`, qui rendait un verdict vert « a priori non concerné » à une
entité que la loi oblige sans seuil. Aucun contrôle ne l'a vu : les contrôles
existants lisent le code, les secrets, les dépendances et les rapports — aucun ne
lit le contenu juridique du site. Fiche E-01 : une règle sans mécanisme n'est pas
une règle.

POURQUOI IL A ÉTÉ RÉÉCRIT LE JOUR MÊME
--------------------------------------
Sa première version ne cherchait que des sous-chaînes affirmatives. Le contradicteur
a montré, et le test l'a confirmé, qu'elle passait au VERT sur les deux fautes
qu'elle prétendait empêcher :
  · « 1 000 salariés OU 450 millions » — la conjonction n'était pas testée, alors
    que le OU à la place du ET EST la faute d'origine (commit 94fd510) ;
  · « cette directive EST DÉSORMAIS transposée en droit belge » — l'empreinte
    cherchée survivait à l'inversion exacte du sens.
Un contrôle qui rassure à tort est pire que pas de contrôle. D'où deux ajouts :
des motifs INTERDITS en plus des motifs exigés, et un périmètre élargi à toutes
les pages du site, version néerlandaise comprise.

CE QU'IL SAIT FAIRE
-------------------
Pour chaque affirmation juridique sensible : exiger des motifs présents ET refuser
des motifs interdits, dans chacun des fichiers déclarés. Il détecte donc la
suppression d'une correction, son inversion de sens, et la substitution du OU au ET.

CE QU'IL NE SAIT PAS FAIRE — à dire, pas à taire
------------------------------------------------
Il ne lit pas le droit : il compare des chaînes. Une formulation juridiquement
fausse mais contenant les bons mots passera. Seul un recoupement à la source
primaire établit qu'une affirmation est exacte — ce contrôle établit seulement
qu'elle n'a pas été supprimée, inversée, ni appliquée à un seul support.

Il ne couvre pas non plus le contenu juridique EN NÉERLANDAIS. Tous ses motifs
sont français. `nl/index.html` est lu, donc une contradiction rédigée en français
y serait vue — mais une contradiction rédigée en néerlandais passerait. Ce n'est
pas un trou aujourd'hui : cette page ne porte aucune affirmation juridique, elle
annonce que la version néerlandaise n'est pas prête. Le jour où elle en portera,
il faudra ajouter les motifs néerlandais ICI, sans quoi les deux langues du site
pourront diverger en silence — et en Belgique les deux versions font également foi.

Usage :  python3 scripts/verifier_coherence_juridique.py
Sortie :  0 si tout tient, 1 dès la première divergence (bloquant en CI).
"""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SITE = RACINE / "products" / "caelum" / "site"

PAGE = "index.html"
OUTIL = "assets/simulateur.js"

# Fichiers susceptibles de porter une affirmation juridique. Le contrôle ne les
# exige pas tous — il refuse seulement qu'ils CONTREDISENT (motifs interdits).
TOUTES_LES_PAGES = [
    "index.html", "simulateur.html", "offres.html", "mentions-legales.html",
    "404.html", "nl/index.html", "assets/simulateur.js",
]

# (libellé, {fichier: [motifs exigés]}, [motifs interdits partout])
EXIGENCES = [
    (
        "Lanceurs d'alerte — l'obligation sans seuil d'effectif est énoncée",
        {PAGE: ["quel que soit leur effectif"], OUTIL: ["SANS SEUIL"]},
        [],
    ),
    (
        "Lanceurs d'alerte — la branche anti-blanchiment est nommée",
        {PAGE: ["blanchiment"], OUTIL: ["anti-blanchiment"]},
        [],
    ),
    (
        "Lanceurs d'alerte — le verdict du simulateur n'est pas « non concerné »",
        {OUTIL: ['n: "Canal lanceurs d\'alerte", s: "verifier"']},
        ['n: "Canal lanceurs d\'alerte", s: "non"'],
    ),
    (
        "CSRD — les deux seuils sont CUMULATIFS, pas alternatifs",
        {PAGE: ["à la fois", "1&nbsp;000 salariés", "450 millions"],
         OUTIL: ["À LA FOIS", "1 000 salariés ET 450 M€"]},
        ["1&nbsp;000 salariés OU", "1 000 salariés OU", "salariés ou 450"],
    ),
    (
        "CSRD — le verdict du simulateur n'est pas « non concerné »",
        {OUTIL: ['n: "CSRD et DORA — le point honnête", s: "verifier"']},
        ['n: "CSRD et DORA — le point honnête", s: "non"'],
    ),
    (
        "NIS2 — l'échéance du 18/04/2026 est présentée comme PASSÉE, pas à venir",
        {PAGE: ["Échéance passée"], OUTIL: ["est passée"]},
        ["Échéance clé&nbsp;: 18/04/2026"],
    ),
    (
        "RGPD et NIS2 — le plafond est le montant le PLUS ÉLEVÉ, pas l'un ou l'autre",
        # Deux occurrences attendues : une par carte. Le compte est contrôlé plus bas.
        {PAGE: ["le montant le plus élevé étant retenu"]},
        [],
    ),
    (
        "CSRD — la directive n'est PAS encore transposée en droit belge",
        {PAGE: ["doit encore être transposée en droit belge"],
         OUTIL: ["n'est pas encore transposée en droit belge"]},
        # Motifs volontairement amputés de leur verbe : un interdit qui dépend d'une
        # forme verbale (« est » / « a été » / « is ») se contourne sans le vouloir.
        # Éprouvé : le piège inséré avec « is désormais » passait au vert.
        ["désormais transposée en droit belge",
         "déjà transposée en droit belge",
         "a été transposée en droit belge"],
    ),
]


def main() -> int:
    contenus: dict[str, str] = {}
    for rel in TOUTES_LES_PAGES:
        f = SITE / rel
        if not f.exists():
            print(f"::error::Fichier déclaré mais introuvable : {f.relative_to(RACINE)}")
            return 1
        contenus[rel] = f.read_text(encoding="utf-8")

    manques: list[str] = []

    # Contrôle de COMPTE, et pas seulement de présence : les deux cartes à sanction
    # (RGPD et NIS2) doivent chacune porter la règle du montant le plus élevé. Une
    # seule occurrence signifierait qu'une des deux l'a perdue — ce qu'un simple
    # test de présence ne verrait pas.
    n = contenus[PAGE].count("le montant le plus élevé étant retenu")
    if n < 2:
        manques.append(
            "RGPD et NIS2 — règle du montant le plus élevé\n"
            f"       ATTENDUE 2 fois dans {PAGE} (une par carte à sanction), trouvée {n} fois"
        )

    for libelle, exiges, interdits in EXIGENCES:
        for rel, motifs in exiges.items():
            for motif in motifs:
                if motif not in contenus[rel]:
                    manques.append(f"{libelle}\n       EXIGÉ et ABSENT de {rel} : « {motif} »")
        for motif in interdits:
            for rel, texte in contenus.items():
                if motif in texte:
                    manques.append(f"{libelle}\n       INTERDIT et PRÉSENT dans {rel} : « {motif} »")

    print()
    print("  COHÉRENCE JURIDIQUE — la brochure et l'outil disent-ils la même chose ?")
    print(f"  {len(EXIGENCES)} affirmations · {len(TOUTES_LES_PAGES)} fichiers lus, version néerlandaise comprise")
    print()

    if manques:
        print(f"  ❌ {len(manques)} divergence(s)")
        for m in manques:
            print(f"     – {m}")
        print()
        print("  " + "─" * 72)
        print("  VERDICT : ❌ un support contredit l'autre, ou une correction a disparu.")
        print("  Corriger LES DEUX, jamais un seul : un visiteur fait davantage confiance au")
        print("  simulateur qu'à une carte, parce qu'il lui répond personnellement.")
        print("  " + "─" * 72)
        return 1

    for libelle, _, _ in EXIGENCES:
        print(f"  ✅ {libelle}")
    print()
    print("  " + "─" * 72)
    # Le compte est LU, jamais écrit en dur : la version précédente annonçait « 5 »
    # alors qu'il y en avait 7. Un chiffre faux SUR NOUS est ce que le §13 désigne
    # comme le plus dangereux, parce que personne ne pense à le vérifier.
    print(f"  VERDICT : ✅ aucune des {len(EXIGENCES)} affirmations n'a été supprimée,")
    print("  inversée, ni appliquée à un seul support.")
    print("  Rappel honnête : ce contrôle COMPARE DES CHAÎNES, il ne lit pas le droit.")
    print("  Une formulation juridiquement fausse contenant les bons mots passerait.")
    print("  Seul un recoupement à la source primaire établit qu'une affirmation est exacte.")
    print("  " + "─" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
