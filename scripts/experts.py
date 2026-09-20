#!/usr/bin/env python3
"""Engendre un agent EXPERT par domaine présent au registre des briques.

Demande de Chaima, 2026-09-20 : « des agents experts en chacun des domaines que
nous trouverons ». Le mot qui compte est TROUVERONS — au futur. Un expert écrit
à la main serait figé le jour de son écriture ; celui-ci naît quand son domaine
apparaît au registre et meurt quand le domaine disparaît.

Le SOCLE est extrait de `.claude/agents/contradicteur.md`, qui fait foi. Il n'est
jamais recopié dans ce fichier : une copie diverge, une extraction non.

Usage :
    python3 scripts/experts.py            # engendre
    python3 scripts/experts.py --verifier # contrôle bloquant
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "codex" / "briques" / "registre.json"
AGENTS = RACINE / ".claude" / "agents"
SOURCE_SOCLE = AGENTS / "contradicteur.md"
PREFIXE = "expert-"


def socle() -> str:
    lignes = SOURCE_SOCLE.read_text(encoding="utf-8").splitlines()
    debut = next(i for i, l in enumerate(lignes) if l.startswith("## SOCLE COMMUN"))
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## TA MISSION"))
    return "\n".join(lignes[debut:fin]).rstrip()


def grouper() -> dict[str, dict]:
    donnees = json.loads(REGISTRE.read_text(encoding="utf-8"))
    groupes: dict[str, dict] = defaultdict(lambda: {"briques": [], "description": ""})
    for brique in donnees["briques"]:
        dom = brique.get("domaine")
        if not dom or dom == "non-classe":
            continue
        groupes[dom]["briques"].append(brique)
        groupes[dom]["description"] = brique.get("domaine_description", "")
    return groupes


def rendre(domaine: str, groupe: dict) -> str:
    briques = sorted(groupe["briques"], key=lambda b: b["id"])
    titre = domaine.replace("-", " ")
    lignes = [
        "---",
        f"name: {PREFIXE}{domaine}",
        f"description: Expert du domaine « {titre} ». Engendré depuis le registre des briques — "
        "ne pas éditer à la main.",
        'tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]',
        "---",
        "",
        socle(),
        "",
        "## TA MISSION",
        "",
        f"Tu es l'expert du domaine **{titre}** : {groupe['description']}.",
        "",
        f"**Tu es ENGENDRÉ**, pas écrit. `scripts/experts.py` te recrée depuis",
        "`codex/briques/registre.json` à chaque fois que le registre bouge. Si ton domaine",
        "disparaît du registre, tu disparais. Si une brique arrive, elle apparaît ci-dessous",
        "sans que personne ne t'édite. C'est voulu : un expert écrit à la main est figé le jour",
        "de son écriture.",
        "",
        f"## Les briques de ton domaine au {date.today()}",
        "",
        "| Id | Brique | État | Licence | Ce qu'il faut savoir |",
        "|---|---|---|---|---|",
    ]
    for b in briques:
        attente = next(
            (v.replace("LECTURE HUMAINE REQUISE — ", "")
             for v in b.get("preuves", {}).values()
             if str(v).startswith("LECTURE HUMAINE")),
            "",
        )
        note = attente[:150] + "…" if len(attente) > 150 else (attente or "—")
        lignes.append(
            f"| {b['id']} | [{b['nom']}]({b['url']}) | **{b['etat']}** | "
            f"{b['licence_declaree']} | {note} |"
        )

    en_sas = [b["id"] for b in briques if b["etat"] == "SAS"]
    refusees = [b["id"] for b in briques if b["etat"] == "REFUSEE"]

    lignes += [
        "",
        "## Ce que tu fais",
        "",
        "1. **Tu connais l'état réel de tes briques**, pas leur réputation. Le tableau ci-dessus",
        "   est engendré du registre : il dit ce qui a été vérifié, et rien de plus.",
        "2. **Tu nommes ce que tes briques NE font PAS.** C'est plus utile que ce qu'elles font :",
        "   c'est là que se trouve la couche qu'on pourra protéger.",
        "3. **Tu cherches l'amont.** Une brique de ton domaine en cache souvent une autre, plus",
        "   ancienne et plus libre, dont elle dérive.",
        "4. **Tu ne proposes aucun assemblage** — c'est le travail de `chimiste`, et il ne",
        "   combine que des briques ADMISES.",
        "",
        "## Ce que tu ne fais jamais",
        "",
        "Tu ne déclares JAMAIS une brique utilisable. Seul `gardien-du-sas` instruit une",
        "admission, et il la PROPOSE — Chaima décide (§10).",
        "",
    ]
    if en_sas:
        lignes += [
            f"**À ce jour, {len(en_sas)} de tes briques sont encore en SAS** "
            f"({', '.join(en_sas)}) : tu peux les étudier, tu ne peux rien bâtir dessus.",
            "",
        ]
    if refusees:
        lignes += [
            f"**{len(refusees)} refusée(s)** ({', '.join(refusees)}) : tu dois savoir POURQUOI,",
            "parce qu'un motif de refus est une connaissance du domaine, pas un échec à oublier.",
            "",
        ]
    lignes += [
        "## À qui tu passes la main",
        "",
        "`gardien-du-sas` pour tout ce qui touche à l'admission · `chimiste` pour les réactions ·",
        "`veilleur-amont` si tu vois bouger une brique chez son éditeur · `contradicteur` quand",
        "ton domaine te paraît évident — c'est précisément là qu'on se trompe.",
    ]
    return "\n".join(lignes) + "\n"


def engendrer() -> list[str]:
    groupes = grouper()
    attendus = {f"{PREFIXE}{d}" for d in groupes}
    ecrits = []
    for domaine, groupe in sorted(groupes.items()):
        cible = AGENTS / f"{PREFIXE}{domaine}.md"
        contenu = rendre(domaine, groupe)
        if not cible.exists() or cible.read_text(encoding="utf-8") != contenu:
            cible.write_text(contenu, encoding="utf-8")
            ecrits.append(cible.name)
    # Un domaine disparu emporte son expert : on ne garde pas d'expert orphelin.
    for fichier in AGENTS.glob(f"{PREFIXE}*.md"):
        if fichier.stem not in attendus:
            fichier.unlink()
            ecrits.append(f"{fichier.name} (retiré — domaine disparu)")
    return ecrits


def verifier() -> int:
    """Le contrôle bloquant : un expert engendré ne doit jamais avoir dérivé."""
    groupes = grouper()
    fautes = []
    for domaine, groupe in groupes.items():
        cible = AGENTS / f"{PREFIXE}{domaine}.md"
        if not cible.exists():
            fautes.append(f"expert manquant pour le domaine « {domaine} »")
        elif cible.read_text(encoding="utf-8") != rendre(domaine, groupe):
            fautes.append(f"{cible.name} a dérivé du registre — relance scripts/experts.py")
    attendus = {f"{PREFIXE}{d}" for d in groupes}
    for fichier in AGENTS.glob(f"{PREFIXE}*.md"):
        if fichier.stem not in attendus:
            fautes.append(f"{fichier.name} est orphelin : son domaine n'est plus au registre")
    for faute in fautes:
        print(f"  🔴 {faute}")
    if not fautes:
        print(f"  ✅ EXPERTS — {len(groupes)} domaine(s), aucun écart au registre")
    return len(fautes)


if __name__ == "__main__":
    if "--verifier" in sys.argv:
        sys.exit(1 if verifier() else 0)
    for nom in engendrer():
        print(f"  🔨 {nom}")
    verifier()
