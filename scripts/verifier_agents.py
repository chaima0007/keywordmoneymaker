#!/usr/bin/env python3
"""Contrôle bloquant des fiches d'agent — détecte les mutilations d'écriture.

Motif : fiches E-27 (2026-09-16), E-29 (2026-09-16), E-34 (2026-09-20). Trois
fois en quatre jours, du contenu de fichier est passé par le shell et en est
ressorti abîmé : accents graves EXÉCUTÉS comme des commandes, sections entières
disparues, apostrophes mangées par l'interpolation.

E-34 a établi que la contre-mesure « utilise un heredoc entre quotes » ne tient
pas : elle repose sur la discipline, et la discipline cède dès qu'elle gêne.
Ce contrôle est l'autre moitié de la réponse — le hook `garde-ecriture.py`
empêche, celui-ci constate. On garde les deux : un garde peut être contourné,
un contrôle bloquant en CI ne l'est pas sans que ça se voie.

Cinq contrôles :
  A1  socle commun identique à la référence (contradicteur.md)
  A2  en-tête YAML complet : name, description, tools
  A3  le nom déclaré correspond au nom du fichier
  A4  section « TA MISSION » présente et non vide
  A5  aucune élision mutilée (« qu on », « l air », « ce qu elles »)

Usage :
    python3 scripts/verifier_agents.py            # rapport
    python3 scripts/verifier_agents.py --verifier # bloquant (CI)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
AGENTS = RACINE / ".claude" / "agents"
REFERENCE = AGENTS / "contradicteur.md"

DEBUT_SOCLE = "## SOCLE COMMUN"
DEBUT_MISSION = "## TA MISSION"

# DEUX FAMILLES cohabitent, et les confondre fait accuser 29 fiches saines.
# Constaté le 2026-09-22, première exécution de ce contrôle : il exigeait le
# socle CODEX de TOUTES les fiches et en accusait 29 d'être mutilées. Elles ne
# l'étaient pas — elles suivent une charte antérieure. C'est la fiche E-25 sous
# une autre forme : un contrôle qui ne comprend pas ce qu'il lit accuse ce qu'il
# lit plutôt que lui-même.
FAMILLE_CODEX = ("## SOCLE COMMUN", "## TA MISSION")
FAMILLE_CHARTE = ("## CHARTE COMMUNE", "## MISSION")

# Projets explicitement SORTIS du périmètre, avec la date de sortie. Une fiche
# qui s'instruit de travailler dessus envoie l'agent sur le mauvais projet.
HORS_PERIMETRE = {
    "Caelum Partners": "sorti le 2026-09-19",
    "La Loi Avec Moi": "sorti le 2026-09-20",
}

# Une élision française mutilée : lettre d'élision, espace, puis un mot qui ne
# peut PAS suivre cette lettre sans apostrophe. Volontairement étroit : un faux
# positif ferait échouer la CI sur du français correct.
ELISION_MUTILEE = re.compile(
    r"\b(qu|n|l|d|s|c|j|m|t)\s+"
    r"(on|air|elle|elles|il|ils|est|une|un|autre|ordre|assemblage|antériorité|"
    r"art|accord|éditeur|état|ancien|humain|enthousiasme|agent|adresse|entrée|"
    r"existence|endroit|erreur|évidence|exécution|étiquette|amont|admission)\b"
)

# Un en-tête YAML minimal. On ne parse pas du YAML : on vérifie une forme.
CHAMPS_REQUIS = ("name:", "description:", "tools:")


def socle_reference() -> str:
    lignes = REFERENCE.read_text(encoding="utf-8").splitlines()
    debut = next(i for i, l in enumerate(lignes) if l.startswith(DEBUT_SOCLE))
    fin = next(i for i, l in enumerate(lignes) if l.startswith(DEBUT_MISSION))
    return "\n".join(lignes[debut:fin]).rstrip()


def extraire_socle(texte: str) -> str | None:
    lignes = texte.splitlines()
    try:
        debut = next(i for i, l in enumerate(lignes) if l.startswith(DEBUT_SOCLE))
    except StopIteration:
        return None
    try:
        fin = next(i for i, l in enumerate(lignes) if l.startswith(DEBUT_MISSION))
    except StopIteration:
        fin = len(lignes)
    return "\n".join(lignes[debut:fin]).rstrip()


def controler(chemin: Path, reference: str) -> list[str]:
    texte = chemin.read_text(encoding="utf-8")
    lignes = texte.splitlines()
    fautes: list[str] = []

    # A2 — en-tête YAML
    if not lignes or lignes[0].strip() != "---":
        fautes.append("A2 pas d'en-tête YAML ouvrant")
        entete = ""
    else:
        try:
            ferme = next(i for i, l in enumerate(lignes[1:], 1) if l.strip() == "---")
            entete = "\n".join(lignes[1:ferme])
        except StopIteration:
            fautes.append("A2 en-tête YAML non refermé")
            entete = ""
    for champ in CHAMPS_REQUIS:
        if champ not in entete:
            fautes.append(f"A2 champ « {champ} » absent de l'en-tête")

    # A3 — nom déclaré == nom de fichier
    declare = re.search(r"^name:\s*(\S+)", entete, re.M)
    if declare and declare.group(1) != chemin.stem:
        fautes.append(f"A3 name « {declare.group(1)} » ≠ fichier « {chemin.stem} »")

    # Quelle famille ? On ne juge une fiche qu'avec sa propre règle.
    est_codex = all(marqueur in texte for marqueur in FAMILLE_CODEX)
    est_charte = all(marqueur in texte for marqueur in FAMILLE_CHARTE)

    if not est_codex and not est_charte:
        fautes.append(
            "A1 fiche d'aucune famille connue : ni socle CODEX + « TA MISSION », "
            "ni charte + « MISSION »"
        )

    # A1 — socle identique, pour la famille CODEX seulement
    if est_codex:
        socle = extraire_socle(texte)
        if socle != reference:
            manquantes = len(reference.splitlines()) - len(socle.splitlines())
            detail = f", {manquantes} ligne(s) manquante(s)" if manquantes > 0 else ""
            fautes.append(f"A1 socle différent de la référence{detail}")

    # A4 — mission présente et substantielle, quelle que soit la famille
    entete_mission = DEBUT_MISSION if est_codex else "## MISSION"
    if entete_mission in texte:
        apres = texte.split(entete_mission, 1)[1].strip()
        if len(apres.splitlines()) < 3:
            fautes.append(
                f"A4 mission quasi vide ({len(apres.splitlines())} ligne(s)) — "
                "signature d'une troncature par le shell (E-34)"
            )

    # A6 — périmètre obsolète. La faute la plus silencieuse : la fiche est
    # parfaitement formée et envoie l'agent sur un projet hors périmètre.
    for projet, sortie in HORS_PERIMETRE.items():
        if re.search(rf"PÉRIMÈTRE\s*:[^\n]*{re.escape(projet)}", texte, re.IGNORECASE):
            fautes.append(
                f"A6 PÉRIMÈTRE OBSOLÈTE — la fiche s'instruit de travailler sur "
                f"« {projet} », {sortie}. Rien n'est supprimé sans l'accord de Chaima : "
                "à trancher, pas à effacer."
            )

    # A5 — élisions mutilées
    mutilees = [m.group(0) for m in ELISION_MUTILEE.finditer(texte)]
    if mutilees:
        fautes.append(
            f"A5 {len(mutilees)} élision(s) mutilée(s) par interpolation shell : "
            + ", ".join(f"« {m} »" for m in mutilees[:4])
        )

    return fautes


def main() -> None:
    reference = socle_reference()
    fiches = sorted(AGENTS.glob("*.md"))

    # DEUX CATÉGORIES, et les confondre serait la même faute que confondre
    # « je ne peux pas conclure » avec « refusé » dans le sas.
    #
    # A1–A5 sont des DÉFAUTS : un fichier abîmé, à réparer. Bloquant.
    # A6 est une DÉCISION EN ATTENTE DE CHAIMA : la fiche est parfaitement
    # formée, c'est son périmètre qui a changé sous elle, et §10 dit que rien
    # n'est supprimé ni réécrit sans son accord. Bloquer la CI là-dessus
    # reviendrait à exiger d'un agent qu'il tranche à sa place.
    #
    # Ce n'est PAS un desserrage : A6 est compté, nommé et réaffiché à chaque
    # exécution. Une dette visible et chiffrée vaut mieux qu'une dette
    # invisible — mais elle ne doit pas bloquer le reste du travail.
    defauts = 0
    attentes: list[tuple[str, str]] = []

    for fiche in fiches:
        for faute in controler(fiche, reference):
            if faute.startswith("A6"):
                attentes.append((fiche.name, faute))
            else:
                defauts += 1
                print(f"  🔴 {fiche.name}\n       {faute}")

    if defauts:
        print(f"\n  🔴 {defauts} MUTILATION(S) sur {len(fiches)} fiche(s) — à réparer.")
    else:
        print(f"  ✅ AGENTS — {len(fiches)} fiche(s), socle identique, aucune mutilation")

    if attentes:
        projets = sorted({p for p in HORS_PERIMETRE if any(p in f for _, f in attentes)})
        print(f"\n  ⏸  {len(attentes)} fiche(s) EN ATTENTE DE CHAIMA — périmètre obsolète")
        print(f"      Projet(s) concerné(s) : {', '.join(projets)}")
        print("      Trois options, et le choix lui revient (§10) : retirer, réécrire au")
        print("      périmètre actuel, ou archiver pour le jour où le projet reprendra.")
        print("      Rien n'est supprimé sans son accord. Voir fiche E-35.")
        for nom, _ in attentes[:5]:
            print(f"        · {nom}")
        if len(attentes) > 5:
            print(f"        · … et {len(attentes) - 5} autre(s)")

    print("\n  Rappel honnête : ceci détecte les dégâts d'écriture connus et les")
    print("  périmètres obsolètes. Il ne dit rien de la JUSTESSE des missions écrites.")

    if "--verifier" in sys.argv:
        sys.exit(1 if defauts else 0)


if __name__ == "__main__":
    main()
