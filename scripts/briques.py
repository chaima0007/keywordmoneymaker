#!/usr/bin/env python3
"""Registre des briques libres — sas, vérification, admission.

Principe, et il n'est pas négociable : TOUTE brique entre en SAS.
Aucune n'entre directement en ADMISE, quel que soit son prestige.
Deux des sept briques du premier relevé viennent d'NVIDIA et d'OpenAI ;
elles passent le même sas qu'un dépôt inconnu hébergé sur Gitee.

Usage :
    python3 scripts/briques.py --entrer <nom> <url> <licence> <origine>
    python3 scripts/briques.py --controler <id> <controle> <oui|non> "<preuve>"
    python3 scripts/briques.py --admettre <id>
    python3 scripts/briques.py --reaction <id_a> <id_b> "<ce que la combinaison donne>"
    python3 scripts/briques.py            # régénère la vue Markdown
    python3 scripts/briques.py --verifier # contrôle bloquant (CI)
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "codex" / "briques" / "registre.json"
VUE = RACINE / "codex" / "briques" / "REGISTRE.md"

CONTROLES = (
    "licence_permissive",
    "provenance",
    "entite_non_sanctionnee",
    "empreinte",
    "execution_isolee",
    "fonctionne_reellement",
)

PERMISSIVES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "Unlicense"}
COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "SSPL-1.0"}


def charger() -> dict:
    return json.loads(REGISTRE.read_text(encoding="utf-8"))


def ecrire(donnees: dict) -> None:
    REGISTRE.write_text(
        json.dumps(donnees, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _horodatage() -> str:
    return datetime.now().strftime("%Y-%m-%d %Hh%M")


def entrer(nom: str, url: str, licence: str, origine: str) -> None:
    """Fait entrer une brique EN SAS. Jamais ailleurs."""
    donnees = charger()
    if any(b["url"] == url for b in donnees["briques"]):
        print(f"  ⏭  déjà au registre : {url}")
        return
    identifiant = f"B-{len(donnees['briques']) + 1:02d}"
    donnees["briques"].append(
        {
            "id": identifiant,
            "nom": nom,
            "url": url,
            "origine": origine,
            "licence_declaree": licence,
            "commit_epingle": None,
            "etat": "SAS",
            "releve_le": str(date.today()),
            "controles": {c: None for c in CONTROLES},
            "preuves": {},
            "ce_que_ca_donne": "",
            "ce_que_ca_ne_fait_pas": "",
            "journal": [{"date": _horodatage(), "evenement": "entrée en SAS"}],
        }
    )
    ecrire(donnees)
    print(f"  🔒 {identifiant} — {nom} entre en SAS. Isolée jusqu'à preuve du contraire.")


def controler(identifiant: str, controle: str, verdict: str, preuve: str) -> None:
    if controle not in CONTROLES:
        sys.exit(f"contrôle inconnu : {controle} (attendus : {', '.join(CONTROLES)})")
    donnees = charger()
    for brique in donnees["briques"]:
        if brique["id"] != identifiant:
            continue
        passe = verdict.lower() in ("oui", "o", "true", "1")
        brique["controles"][controle] = passe
        brique["preuves"][controle] = preuve
        brique["journal"].append(
            {
                "date": _horodatage(),
                "evenement": f"contrôle {controle} : {'VERT' if passe else 'ROUGE'} — {preuve}",
            }
        )
        if not passe:
            brique["etat"] = "REFUSEE"
            brique["journal"].append(
                {"date": _horodatage(), "evenement": f"REFUSÉE sur {controle}"}
            )
        elif all(brique["controles"][c] is True for c in CONTROLES):
            brique["etat"] = "VERIFIEE"
            brique["journal"].append(
                {"date": _horodatage(), "evenement": "six contrôles au vert — VÉRIFIÉE, pas encore admise"}
            )
        ecrire(donnees)
        print(f"  {'✅' if passe else '🔴'} {identifiant} · {controle} · état → {brique['etat']}")
        return
    sys.exit(f"brique inconnue : {identifiant}")


def attente(identifiant: str, controle: str, motif: str) -> None:
    """Un contrôle qui NE PEUT PAS conclure. Ce n'est ni vert ni rouge.

    Confondre « je ne peux pas conclure » avec « refusé » est une faute de
    modélisation : la première se lève par une lecture humaine, la seconde non.
    Le contrôle reste à None — donc l'admission reste impossible — et le motif
    est consigné pour que l'humain sache exactement quoi lire.
    """
    if controle not in CONTROLES:
        sys.exit(f"contrôle inconnu : {controle}")
    donnees = charger()
    for brique in donnees["briques"]:
        if brique["id"] != identifiant:
            continue
        brique["controles"][controle] = None
        brique["preuves"][controle] = f"LECTURE HUMAINE REQUISE — {motif}"
        brique["journal"].append(
            {"date": _horodatage(), "evenement": f"contrôle {controle} : NE CONCLUT PAS — {motif}"}
        )
        ecrire(donnees)
        print(f"  ⏸  {identifiant} · {controle} · lecture humaine requise")
        return
    sys.exit(f"brique inconnue : {identifiant}")


def epingler(identifiant: str, sha: str) -> None:
    donnees = charger()
    for brique in donnees["briques"]:
        if brique["id"] != identifiant:
            continue
        brique["commit_epingle"] = sha
        brique["controles"]["empreinte"] = True
        brique["preuves"]["empreinte"] = f"commit {sha} relevé au clone du {date.today()}"
        brique["journal"].append({"date": _horodatage(), "evenement": f"commit épinglé : {sha}"})
        ecrire(donnees)
        print(f"  📌 {identifiant} épinglée sur {sha[:12]}")
        return
    sys.exit(f"brique inconnue : {identifiant}")


def admettre(identifiant: str) -> None:
    donnees = charger()
    for brique in donnees["briques"]:
        if brique["id"] != identifiant:
            continue
        manquants = [c for c in CONTROLES if brique["controles"][c] is not True]
        if manquants:
            sys.exit(
                f"REFUS d'admission — contrôles non passés : {', '.join(manquants)}.\n"
                "Un sas qu'on contourne n'est pas un sas."
            )
        brique["etat"] = "ADMISE"
        brique["journal"].append({"date": _horodatage(), "evenement": "ADMISE"})
        ecrire(donnees)
        print(f"  🟢 {identifiant} admise.")
        return
    sys.exit(f"brique inconnue : {identifiant}")


def reaction(id_a: str, id_b: str, effet: str) -> None:
    """Une réaction entre deux briques ADMISES. La chimie, pas le catalogue."""
    donnees = charger()
    index = {b["id"]: b for b in donnees["briques"]}
    for identifiant in (id_a, id_b):
        if identifiant not in index:
            sys.exit(f"brique inconnue : {identifiant}")
        if index[identifiant]["etat"] != "ADMISE":
            sys.exit(
                f"REFUS — {identifiant} est en état {index[identifiant]['etat']}.\n"
                "On ne combine que des briques admises : une réaction avec un réactif non vérifié\n"
                "ne se distingue pas d'un accident."
            )
    donnees["reactions"].append(
        {
            "briques": [id_a, id_b],
            "effet": effet,
            "date": _horodatage(),
            "anteriorite_cherchee": False,
        }
    )
    ecrire(donnees)
    print(f"  ⚗️  réaction {id_a} × {id_b} consignée. Antériorité NON cherchée.")


def engendrer_vue() -> None:
    donnees = charger()
    briques = donnees["briques"]
    par_etat: dict[str, list] = {}
    for brique in briques:
        par_etat.setdefault(brique["etat"], []).append(brique)

    lignes = [
        "# Registre des briques — vue engendrée",
        "",
        "**Ne pas modifier à la main.** Engendré par `scripts/briques.py` depuis",
        "`codex/briques/registre.json`, qui est la source.",
        "",
        f"Relevé du {date.today()} · {len(briques)} brique(s) · {len(donnees['reactions'])} réaction(s)",
        "",
        "## Règle d'entrée",
        "",
        "Toute brique entre en **SAS**. Aucune n'entre directement en ADMISE, quel que soit",
        "son prestige : un dépôt d'NVIDIA passe le même sas qu'un dépôt inconnu sur Gitee.",
        "Le contrôle de sécurité est **neutre en origine** ; le contrôle de sanctions porte sur",
        "l'entité, jamais sur le pays.",
        "",
    ]

    for etat in ("ADMISE", "VERIFIEE", "SAS", "REFUSEE", "RETIREE"):
        lot = par_etat.get(etat, [])
        if not lot:
            continue
        lignes += [f"## {etat} — {len(lot)}", ""]
        lignes += ["| Id | Nom | Origine | Licence | Contrôles au vert |", "|---|---|---|---|---|"]
        for brique in lot:
            verts = sum(1 for c in CONTROLES if brique["controles"][c] is True)
            attentes = sum(1 for c in CONTROLES
                           if str(brique["preuves"].get(c, "")).startswith("LECTURE HUMAINE"))
            lignes.append(
                f"| {brique['id']} | [{brique['nom']}]({brique['url']}) | {brique['origine']} "
                f"| {brique['licence_declaree']} | {verts}/{len(CONTROLES)}"
                + (f" · ⏸ {attentes}" if attentes else "") + " |"
            )
        lignes.append("")

    if donnees["reactions"]:
        lignes += ["## Réactions consignées", ""]
        for r in donnees["reactions"]:
            marque = "antériorité cherchée" if r["anteriorite_cherchee"] else "**antériorité NON cherchée**"
            lignes.append(f"- `{' × '.join(r['briques'])}` — {r['effet']} ({marque})")
        lignes.append("")

    lignes += [
        "---",
        "",
        "*Rappel honnête : ce registre prouve que les contrôles ont été consignés.*",
        "*Il ne prouve pas qu'ils ont été bien faits. Un contrôle est une trace, pas une garantie.*",
    ]
    VUE.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"  🔨 {VUE.relative_to(RACINE)} engendré — {len(briques)} brique(s)")


def _journal_precedent() -> dict[str, int]:
    """Longueur du journal de chaque brique dans la version commitée."""
    resultat = subprocess.run(
        ["git", "-C", str(RACINE), "show", f"HEAD:{REGISTRE.relative_to(RACINE)}"],
        capture_output=True, text=True,
    )
    if resultat.returncode != 0:
        return {}
    try:
        avant = json.loads(resultat.stdout)
    except json.JSONDecodeError:
        return {}
    return {b["id"]: len(b["journal"]) for b in avant.get("briques", [])}


def verifier() -> int:
    """Contrôle bloquant. Renvoie le nombre de violations."""
    donnees = charger()
    fautes: list[str] = []
    avant = _journal_precedent()

    for brique in donnees["briques"]:
        ident = brique["id"]

        # V1 — une brique ADMISE doit avoir ses six contrôles au vert
        if brique["etat"] == "ADMISE":
            manquants = [c for c in CONTROLES if brique["controles"][c] is not True]
            if manquants:
                fautes.append(f"V1 {ident} ADMISE sans : {', '.join(manquants)}")

        # V2 — licence copyleft admise sans dérogation écrite
        if brique["licence_declaree"] in COPYLEFT and brique["etat"] in ("ADMISE", "VERIFIEE"):
            if "derogation" not in brique.get("preuves", {}):
                fautes.append(
                    f"V2 {ident} licence copyleft {brique['licence_declaree']} en état "
                    f"{brique['etat']} sans dérogation écrite de Chaima"
                )

        # V3 — licence ni permissive ni copyleft connue : à qualifier, jamais à supposer
        if brique["licence_declaree"] not in PERMISSIVES | COPYLEFT:
            if brique["controles"]["licence_permissive"] is True:
                fautes.append(
                    f"V3 {ident} licence « {brique['licence_declaree'] or 'vide'} » inconnue du "
                    "référentiel, mais le contrôle de licence est au vert"
                )

        # V4 — une brique admise sans commit épinglé n'est pas reproductible
        if brique["etat"] == "ADMISE" and not brique["commit_epingle"]:
            fautes.append(f"V4 {ident} ADMISE sans commit épinglé")

        # V5 — journal en ajout seul
        if ident in avant and len(brique["journal"]) < avant[ident]:
            fautes.append(
                f"V5 {ident} journal raccourci ({avant[ident]} → {len(brique['journal'])}) : "
                "le registre est en ajout seul"
            )

    for r in donnees["reactions"]:
        index = {b["id"]: b for b in donnees["briques"]}
        for ident in r["briques"]:
            if index.get(ident, {}).get("etat") != "ADMISE":
                fautes.append(f"V6 réaction {' × '.join(r['briques'])} avec {ident} non admise")

    for faute in fautes:
        print(f"  🔴 {faute}")
    if not fautes:
        print(f"  ✅ REGISTRE — {len(donnees['briques'])} brique(s), aucune violation")
        print("  Rappel honnête : ceci prouve que les contrôles sont consignés,")
        print("  pas qu'ils ont été bien faits.")
    return len(fautes)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        engendrer_vue()
    elif args[0] == "--entrer":
        entrer(args[1], args[2], args[3], args[4])
        engendrer_vue()
    elif args[0] == "--controler":
        controler(args[1], args[2], args[3], args[4])
        engendrer_vue()
    elif args[0] == "--attente":
        attente(args[1], args[2], args[3])
        engendrer_vue()
    elif args[0] == "--epingler":
        epingler(args[1], args[2])
        engendrer_vue()
    elif args[0] == "--admettre":
        admettre(args[1])
        engendrer_vue()
    elif args[0] == "--reaction":
        reaction(args[1], args[2], args[3])
        engendrer_vue()
    elif args[0] == "--verifier":
        sys.exit(1 if verifier() else 0)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
