#!/usr/bin/env python3
"""Contrôle mécanique des rapports déposés — la surveillance de celui qui surveille.

POURQUOI CE FICHIER EXISTE
--------------------------
Le protocole impose depuis le 11/09/2026 qu'aucun rapport ne commence sans une phrase
de contrôle honnête (CLAUDE.md §2 ter, point 2). Mais cette phrase est écrite par
l'agent qui se contrôle lui-même : elle ne prouve rien. Un rapport peut être sincère,
bien formé, et citer un commit qui n'existe pas, un fichier qui n'a jamais été créé,
un run d'intégration continue imaginaire. C'est exactement le motif des fiches E-11
(une date lue dans un dépôt superficiel, prise pour une date de divulgation) et E-13
(une recherche web prise pour un registre officiel) : l'erreur n'était pas un mensonge,
c'était une trace jamais recoupée.

Ce script ne juge pas la sincérité. Il recoupe les TRACES.

CE QU'IL SAIT FAIRE
-------------------
Falsifier mécaniquement ce qu'un rapport affirme sur le dépôt lui-même :
  R1  le nom du fichier respecte la convention horodatée de Chaima ;
  R2  la phrase de contrôle honnête est présente ;
  R3  tout commit cité existe réellement dans le dépôt ;
  R4  tout chemin de fichier cité existe, sauf s'il est explicitement dit absent ;
  R5  tout run d'intégration continue cité est une URL vérifiable, pas un numéro nu ;
  R6  aucune confiance exprimée en pourcentage (CODEX §13 l'interdit) ;
  R7  toute ligne qui affirme « VÉRIFIÉ » porte une trace (commande ou URL).

CE QU'IL NE SAIT PAS FAIRE — à dire, pas à taire
------------------------------------------------
Il ne vérifie pas que le monde est conforme au rapport. Un commit peut exister et ne
rien contenir d'utile ; une URL peut être valide et pointer sur un échec. Ce contrôle
rend impossible une catégorie d'erreur (la trace inventée ou périmée), pas toutes.
La lecture humaine et la méta-surveillance du soir restent nécessaires.

Il est écrit par la partie surveillée. C'est son défaut structurel, et il est assumé
ici plutôt que masqué : sa seule défense est d'être mécanique, court, et relisible.

Usage :  python3 scripts/verifier_rapports.py [--dossier codex/rapports]
Sortie :  0 si tout tient, 1 à la première violation (contrôle bloquant en CI).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_DEFAUT = RACINE / "codex" / "rapports"

# Convention imposée par Chaima : AAAA-MM-JJ-HHhMM — [Projet] — [Catégorie] — [Sujet précis]
CONVENTION = re.compile(
    r"^\d{4}-\d{2}-\d{2}-\d{2}h\d{2} — .+ — .+ — .+\.md$"
)

MARQUEURS_CONTROLE = (
    "phrase de contrôle",
    "contrôle honnête",
)

# Un jeton entre accents graves qui ressemble à un commit : hexadécimal, 7 à 40
# caractères, et contenant au moins une lettre — sinon « 20260914 » serait testé.
JETON_ENCADRE = re.compile(r"`([^`\n]{1,200})`")
RESSEMBLE_A_UN_COMMIT = re.compile(r"^[0-9a-f]{7,40}$")
CONTIENT_UNE_LETTRE = re.compile(r"[a-f]")

# Un chemin : au moins un « / » et une extension connue, ou un fichier racine connu.
EXTENSIONS = (
    ".md", ".py", ".yml", ".yaml", ".css", ".js", ".html", ".json", ".txt",
    ".woff2", ".svg", ".png", ".toml", ".lock",
)
FICHIERS_RACINE = {"CLAUDE.md", "AGENTS.md", "LICENSE", "README.md", "main.py"}

# Formules qui disent explicitement qu'une chose n'existe pas : le contrôle R4 doit
# alors se taire, sinon on interdirait d'écrire « le site LLAM n'existe pas ».
AVEUX_D_ABSENCE = (
    "absent", "n'existe pas", "nexiste pas", "inexistant", "aucun fichier",
    "à créer", "a creer", "supprimé", "supprime", "jamais créé", "n'a jamais",
    "introuvable", "sera créé", "manquant",
)

CONFIANCE_EN_POURCENT = re.compile(
    r"(confiance|certitude|fiabilité|probabilité)[^.\n]{0,40}\d{1,3}\s?%", re.IGNORECASE
)

# « VÉRIFIÉ » seul, pas « NON VÉRIFIÉ » (qui est précisément l'aveu honnête attendu).
VERIFIE_SANS_NEGATION = re.compile(r"(?<!NON )(?<!non )VÉRIFIÉ")
PORTE_UNE_TRACE = re.compile(r"`[^`\n]+`|https?://")

RUN_CI_NU = re.compile(r"\brun\s+(?:CI\s+)?(?:n[°o]\s*)?(\d{8,})\b", re.IGNORECASE)


class Violation(Exception):
    pass


def _commit_existe(sha: str) -> bool:
    resultat = subprocess.run(
        ["git", "-C", str(RACINE), "cat-file", "-e", f"{sha}^{{commit}}"],
        capture_output=True,
    )
    return resultat.returncode == 0


def _est_un_chemin(jeton: str) -> bool:
    if jeton in FICHIERS_RACINE:
        return True
    if " " in jeton and not jeton.endswith(EXTENSIONS):
        return False
    return "/" in jeton and jeton.endswith(EXTENSIONS)


def controler(chemin: Path) -> list[str]:
    """Renvoie la liste des violations trouvées dans un rapport. Vide = conforme."""
    fautes: list[str] = []
    texte = chemin.read_text(encoding="utf-8")
    lignes = texte.splitlines()

    # R1 — convention de nommage
    if not CONVENTION.match(chemin.name):
        fautes.append(
            f"R1 nom hors convention : « {chemin.name} » ; attendu "
            "« AAAA-MM-JJ-HHhMM — Projet — Catégorie — Sujet.md »"
        )

    # R2 — phrase de contrôle honnête (§2 ter, point 2)
    debut = "\n".join(lignes[:15]).lower()
    if not any(marqueur in debut for marqueur in MARQUEURS_CONTROLE):
        fautes.append(
            "R2 aucune phrase de contrôle honnête dans les 15 premières lignes "
            "(CLAUDE.md §2 ter, point 2)"
        )

    for numero, ligne in enumerate(lignes, start=1):
        minuscule = ligne.lower()
        # L'aveu d'absence se cherche HORS des accents graves : sinon un fichier nommé
        # « inexistant.html » s'auto-absoudrait par son seul nom. Piège réellement
        # rencontré au banc d'essai du 2026-09-14.
        hors_code = JETON_ENCADRE.sub(" ", ligne).lower()
        absence_avouee = any(aveu in hors_code for aveu in AVEUX_D_ABSENCE)
        parle_de_digest = "sha256" in minuscule or "digest" in minuscule

        for jeton in JETON_ENCADRE.findall(ligne):
            # R3 — commit cité
            if (
                RESSEMBLE_A_UN_COMMIT.match(jeton)
                and CONTIENT_UNE_LETTRE.search(jeton)
                and not parle_de_digest
            ):
                if not _commit_existe(jeton):
                    fautes.append(
                        f"R3 ligne {numero} : le commit `{jeton}` n'existe pas dans ce dépôt"
                    )
                continue

            # R4 — chemin cité
            if _est_un_chemin(jeton) and not absence_avouee:
                if not (RACINE / jeton).exists():
                    fautes.append(
                        f"R4 ligne {numero} : le chemin `{jeton}` n'existe pas "
                        "(s'il est absent exprès, écris-le en toutes lettres sur la ligne)"
                    )

        # R5 — run d'intégration continue cité sans URL
        if RUN_CI_NU.search(ligne) and "http" not in minuscule:
            fautes.append(
                f"R5 ligne {numero} : run cité par numéro nu, sans URL vérifiable"
            )

        # R6 — confiance en pourcentage (CODEX §13 : FAIBLE / MODÉRÉE / ÉLEVÉE)
        if CONFIANCE_EN_POURCENT.search(ligne):
            fautes.append(
                f"R6 ligne {numero} : confiance exprimée en pourcentage — "
                "CODEX §13 impose FAIBLE / MODÉRÉE / ÉLEVÉE"
            )

        # R7 — « VÉRIFIÉ » sans trace
        if VERIFIE_SANS_NEGATION.search(ligne) and not PORTE_UNE_TRACE.search(ligne):
            fautes.append(
                f"R7 ligne {numero} : « VÉRIFIÉ » affirmé sans trace "
                "(commande entre accents graves, ou URL)"
            )

    return fautes


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument("--dossier", default=str(DOSSIER_DEFAUT))
    arguments = analyseur.parse_args()

    dossier = Path(arguments.dossier)
    if not dossier.is_dir():
        print(f"::warning::Aucun dossier de rapports à « {dossier} » — contrôle NON EXÉCUTÉ.")
        return 0

    rapports = sorted(p for p in dossier.glob("*.md") if p.name != "README.md")
    if not rapports:
        print(f"Aucun rapport déposé dans « {dossier} ». Rien à recouper.")
        return 0

    total = 0
    for rapport in rapports:
        fautes = controler(rapport)
        total += len(fautes)
        if fautes:
            print(f"\n✗ {rapport.name}")
            for faute in fautes:
                print(f"   {faute}")
        else:
            print(f"✓ {rapport.name}")

    print(f"\n{len(rapports)} rapport(s) recoupé(s), {total} violation(s).")
    if total:
        print(
            "::error::Un rapport cite une trace qui ne tient pas. "
            "Corrige le rapport, pas le contrôle."
        )
        return 1
    print(
        "Rappel honnête : ce contrôle prouve que les traces citées existent. "
        "Il ne prouve pas que les conclusions sont justes."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
