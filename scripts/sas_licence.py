#!/usr/bin/env python3
"""Contrôle de licence du sas — lit les FICHIERS, jamais l'étiquette.

Motif, et il est daté du 2026-09-20 : la fiche du dépôt CodeGeeX4 affiche
Apache-2.0. Apache-2.0 ne couvre que LE CODE ; les poids du modèle sont sous
une licence distincte interdisant l'usage commercial sans formulaire. Une
brique dont le code et les poids n'ont pas la même licence n'est pas une
brique : ce sont deux.

Ce contrôle clone le dépôt en profondeur 1 dans un répertoire isolé, épingle le
commit exact, et cherche TOUS les fichiers de licence — pas seulement LICENSE.
Il signale toute licence secondaire, toute mention restrictive dans le README,
et refuse de conclure quand il en trouve plusieurs.

Usage :
    python3 scripts/sas_licence.py <url> [<url> ...]
    python3 scripts/sas_licence.py --toutes-en-sas
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "codex" / "briques" / "registre.json"

# Un TEXTE de licence, c'est un fichier dont le nom EST « licence » — pas un fichier
# qui parle de licences. Distinction apprise en production le 2026-09-20 (fiche E-33) :
# la première version prenait les sidecars REUSE « *.license » et les scripts
# « resolve_licenses.py » pour des licences distinctes, et déclarait NVIDIA/OpenShell
# multi-licencié alors qu'il ne l'est pas.
#
# Le durcissement ne consiste PAS à ignorer les sidecars — ce serait desserrer. Il
# consiste à les LIRE correctement : un sidecar REUSE porte un identifiant SPDX, qui
# est une déclaration de licence. On la compare au texte principal. Un sidecar qui
# déclare autre chose que la licence du dépôt est exactement ce qu'on cherche.
NOMS_DE_TEXTE = {"license", "licence", "licenses", "licences", "copying"}

# NOTICE n'est PAS un texte de licence : sous Apache-2.0 c'est un fichier
# d'ATTRIBUTION, et le confondre avec une licence faisait refuser à tort quatre
# briques sur dix. Mais on ne l'ignore pas — c'est là que se cachent les
# incohérences. Constaté le 2026-09-20 sur winsenlabs/platos, dont la fiche de
# dépôt annonce Apache-2.0 tandis que son NOTICE renvoie aux « full MIT license
# terms » du projet amont trigger.dev. Un NOTICE qui nomme une licence autre que
# celle du fichier LICENSE est exactement ce qu'on cherche.
NOMS_ATTRIBUTION = {"notice", "authors", "credits", "third_party_notices", "third-party-notices"}
LICENCES_NOMMEES = re.compile(
    r"\b(MIT|Apache[- ]?2(\.0)?|BSD[- ]?[23]?[- ]?Clause|GPL[- ]?[23]?(\.0)?|AGPL[- ]?3?(\.0)?|LGPL|ISC|MPL[- ]?2(\.0)?|SSPL)\b",
    re.IGNORECASE)

# Une licence retypée à la main — guillemets typographiques, deux-points pleine
# largeur — n'est plus le texte canonique. Elle peut différer sur le fond. On la
# reconnaît quand même, et ON LE DIT. Cas JoyAgent-JDGenie, 2026-09-20.
GUILLEMETS = str.maketrans({"\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",
                            "\uff1a": ":", "\u00a0": " "})
EXTENSIONS_DE_TEXTE = {"", ".txt", ".md", ".rst"}
SPDX = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.\-+ ()]+)")

# Un identifiant SPDX se termine par une lettre ou un chiffre. Tout ce qui suit est
# la fin du commentaire qui le portait : « --> » en HTML, « */ » en C, « #» en shell.
# Faux positif constaté le 2026-09-20 sur NVIDIA/OpenShell, qui était déclaré
# discordant avec lui-même : « Apache-2.0 » contre « Apache-2.0 -- ».
FIN_DE_COMMENTAIRE = re.compile(r"[^A-Za-z0-9)]+$")


def _normaliser_spdx(brut: str) -> str:
    return FIN_DE_COMMENTAIRE.sub("", brut.strip())


def _est_un_texte_de_licence(chemin: Path, racine: Path) -> bool:
    """Le nom EST « licence », ou le fichier vit dans un dossier LICENSES/."""
    if chemin.suffix.lower() not in EXTENSIONS_DE_TEXTE:
        return False
    if chemin.stem.lower().split(".")[0] in NOMS_DE_TEXTE:
        return True
    return any(p.lower() in ("licenses", "licences") for p in chemin.relative_to(racine).parts[:-1])


EMPREINTES = {
    "Apache-2.0": ("Apache License", "Version 2.0"),
    "MIT": ("MIT License", "Permission is hereby granted, free of charge"),
    "BSD-3-Clause": ("Redistribution and use in source and binary forms", "Neither the name of"),
    "BSD-2-Clause": ("Redistribution and use in source and binary forms",),
    "GPL-3.0": ("GNU GENERAL PUBLIC LICENSE", "Version 3"),
    "GPL-2.0": ("GNU GENERAL PUBLIC LICENSE", "Version 2"),
    "AGPL-3.0": ("GNU AFFERO GENERAL PUBLIC LICENSE",),
    "LGPL": ("GNU LESSER GENERAL PUBLIC LICENSE",),
    "ISC": ("ISC License",),
}

# Formules qui trahissent une restriction, même sous une licence permissive.
DRAPEAUX_ROUGES = (
    ("usage commercial sous condition", re.compile(
        r"commercial (use|purposes?)[^.]{0,120}(registration|register|license|licence|permission|form|contact)",
        re.IGNORECASE)),
    ("réservé à la recherche", re.compile(
        r"(academic|research)[- ]only|for (academic|research) (use|purposes?) only", re.IGNORECASE)),
    ("licence de modèle distincte", re.compile(
        r"model (weights?|license|licence)[^.]{0,120}(license|licence|agreement)", re.IGNORECASE)),
    ("clause de non-concurrence", re.compile(
        r"may not (be used to )?compete|non[- ]compete", re.IGNORECASE)),
)


def _reconnaitre(texte: str) -> tuple[str | None, bool]:
    """Renvoie (licence, texte_canonique). Un texte retypé est signalé."""
    brut = texte[:4000]
    entete = brut.translate(GUILLEMETS)
    retype = entete != brut
    for nom, marqueurs in EMPREINTES.items():
        if all(m in entete for m in marqueurs):
            return nom, not retype
    return None, not retype


def examiner(url: str) -> dict:
    """Clone en profondeur 1, épingle le commit, lit toutes les licences."""
    dossier = Path(tempfile.mkdtemp(prefix="sas-"))
    rapport: dict = {"url": url, "commit": None, "licences": {}, "declarations": {},
                     "attributions": {}, "retypees": [], "drapeaux": [], "erreur": None}
    try:
        clone = subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", url, str(dossier / "d")],
            capture_output=True, text=True, timeout=180,
        )
        if clone.returncode != 0:
            rapport["erreur"] = clone.stderr.strip()[:200] or "clone refusé"
            return rapport
        depot = dossier / "d"

        sha = subprocess.run(
            ["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True
        )
        rapport["commit"] = sha.stdout.strip()

        racine_depot = depot
        for fichier in depot.rglob("*"):
            if not fichier.is_file() or ".git/" in str(fichier):
                continue
            try:
                if fichier.stat().st_size > 400_000:
                    continue
            except OSError:
                continue
            relatif = str(fichier.relative_to(racine_depot))

            nom_simple = fichier.stem.lower().split(".")[0]

            if nom_simple in NOMS_ATTRIBUTION and fichier.suffix.lower() in EXTENSIONS_DE_TEXTE:
                texte = fichier.read_text(encoding="utf-8", errors="replace")
                nommees = {m.group(1).upper().replace(" ", "-") for m in LICENCES_NOMMEES.finditer(texte)}
                if nommees:
                    rapport["attributions"][relatif] = sorted(nommees)
                continue

            if _est_un_texte_de_licence(fichier, racine_depot):
                texte = fichier.read_text(encoding="utf-8", errors="replace")
                licence, canonique = _reconnaitre(texte)
                rapport["licences"][relatif] = licence or "NON RECONNUE"
                if licence and not canonique:
                    rapport["retypees"].append(relatif)
                continue

            # Déclaration SPDX : sidecar REUSE, ou en-tête dans un fichier source.
            if fichier.suffix.lower() in (".license", ".txt", ".md", ".py", ".js", ".ts", ".go", ".toml"):
                try:
                    entete = fichier.read_text(encoding="utf-8", errors="replace")[:2000]
                except OSError:
                    continue
                for trouve in SPDX.finditer(entete):
                    identifiant = _normaliser_spdx(trouve.group(1))
                    if identifiant:
                        rapport["declarations"].setdefault(identifiant, []).append(relatif)

        for readme in list(depot.glob("README*")) + list(depot.glob("readme*")):
            if not readme.is_file():
                continue
            texte = readme.read_text(encoding="utf-8", errors="replace")
            for etiquette, motif in DRAPEAUX_ROUGES:
                trouve = motif.search(texte)
                if trouve:
                    extrait = " ".join(trouve.group(0).split())[:160]
                    rapport["drapeaux"].append(f"{readme.name} — {etiquette} : « {extrait} »")
    finally:
        shutil.rmtree(dossier, ignore_errors=True)
    return rapport


def verdict(rapport: dict) -> tuple[bool, str]:
    """Renvoie (licence unique et permissive ?, motif)."""
    if rapport["erreur"]:
        return False, f"clone impossible : {rapport['erreur']}"
    if not rapport["licences"]:
        return False, "AUCUN fichier de licence trouvé — un dépôt sans licence n'est pas libre"

    textes = {v for v in rapport["licences"].values()}
    declarees = set(rapport.get("declarations", {}))
    permissives = {"MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "ISC"}

    if rapport["drapeaux"]:
        return False, "restriction signalée dans le README : " + " | ".join(rapport["drapeaux"][:2])

    non_reconnus = [f for f, v in rapport["licences"].items() if v == "NON RECONNUE"]
    if non_reconnus:
        return False, ("texte de licence NON RECONNU, lecture humaine requise : "
                       + ", ".join(non_reconnus[:3]))
    if len(textes) > 1:
        detail = ", ".join(f"{k} → {v}" for k, v in rapport["licences"].items())
        return False, f"TEXTES DE LICENCE MULTIPLES ({len(textes)}) : {detail}"

    licence = textes.pop()

    # Une déclaration SPDX qui contredit le texte principal est le signal recherché.
    discordantes = {d for d in declarees if d not in (licence, "CC0-1.0", "CC-BY-4.0")}
    if discordantes:
        detail = "; ".join(
            f"{d} dans {', '.join(rapport['declarations'][d][:2])}" for d in sorted(discordantes)[:3])
        return False, f"DÉCLARATIONS SPDX DISCORDANTES avec {licence} : {detail}"

    def _famille(nom: str) -> str:
        n = nom.upper().replace(".", "").replace("-", "").replace(" ", "")
        return {"APACHE20": "APACHE2", "APACHE2": "APACHE2"}.get(n, n)

    attendue = _famille(licence)
    for fichier, nommees in rapport.get("attributions", {}).items():
        discordance = [n for n in nommees if _famille(n) != attendue]
        if discordance:
            return False, (f"ATTRIBUTION DISCORDANTE — {fichier} nomme {', '.join(discordance)} "
                           f"alors que LICENSE est {licence}. Le projet incorpore du code amont "
                           "sous d'autres termes : lecture humaine requise avant tout usage.")

    if licence in permissives:
        fichiers = ", ".join(rapport["licences"])
        n = sum(len(v) for v in rapport.get("declarations", {}).values())
        marque = " · TEXTE RETYPÉ, non canonique" if rapport.get("retypees") else ""
        return True, (f"{licence} lue dans {fichiers} · {n} déclaration(s) SPDX concordante(s)"
                      f"{marque} · commit {rapport['commit'][:12]}")
    return False, f"licence {licence} non permissive"


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == "--toutes-en-sas":
        donnees = json.loads(REGISTRE.read_text(encoding="utf-8"))
        urls = [b["url"] for b in donnees["briques"] if b["etat"] == "SAS"]
    else:
        urls = args
    if not urls:
        sys.exit(__doc__)

    for url in urls:
        print(f"\n─── {url}")
        rapport = examiner(url)
        passe, motif = verdict(rapport)
        print(f"  {'✅' if passe else '🔴'} {motif}")
        if rapport["commit"]:
            print(f"     commit : {rapport['commit']}")
        for f, l in rapport["licences"].items():
            print(f"     · {f} → {l}")
        for d in rapport["drapeaux"]:
            print(f"     ⚠ {d}")


if __name__ == "__main__":
    main()
