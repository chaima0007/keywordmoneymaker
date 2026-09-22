#!/usr/bin/env python3
"""Garde PreToolUse — interdit d'écrire du contenu de fichier À TRAVERS le shell.

Motif : fiches E-27 (2026-09-16), E-29, E-34 (2026-09-20). Trois fois en quatre
jours, du contenu destiné à un fichier est passé par le shell et en est ressorti
abîmé : accents graves EXÉCUTÉS comme des commandes, sections entières
disparues, apostrophes mangées par l'interpolation.

E-34 a établi la vraie leçon : « une contre-mesure qui repose sur la discipline
sera contournée le jour où elle gêne ». La contre-mesure d'E-27 disait « utilise
un heredoc entre quotes » — et j'ai quand même factorisé dans une fonction shell
parce que c'était plus élégant. Cette garde-ci ne demande rien : elle REFUSE.

Ce qu'elle refuse, et rien d'autre :
  G1  heredoc à délimiteur NON quoté qui écrit dans un fichier
  G2  echo / printf contenant un accent grave, redirigé vers un fichier
  G3  echo / printf multi-lignes redirigé vers un fichier de texte

Ce qu'elle laisse passer, volontairement :
  · les heredocs entre quotes (<<'FIN'), qui sont la forme sûre
  · les redirections vers /dev/null, les journaux, les fichiers temporaires
  · tout ce qui ne construit pas de contenu de fichier

Une garde qui refuserait trop serait désactivée dans la semaine. Elle vise
étroitement le geste qui a abîmé quatre fichiers.
"""
from __future__ import annotations

import json
import re
import sys

# Un heredoc SÛR : le délimiteur est entre quotes ou échappé (<<'FIN', <<"FIN", <<\FIN).
# Un heredoc DANGEREUX : délimiteur nu, donc le shell interpole $, ` et \ dedans.
HEREDOC_NU = re.compile(r"<<-?\s*([A-Za-z_][A-Za-z0-9_]*)\b")
HEREDOC_QUOTE = re.compile(r"<<-?\s*(['\"]|\\)")

# Une redirection vers un vrai fichier (pas /dev/null, pas un flux).
REDIRECTION = re.compile(r">>?\s*(?!/dev/)([\w./~$-]+\.\w+|\"[^\"]+\"|'[^']+')")

# Extensions dont le contenu est du TEXTE qu'on relira — celles qui ont souffert.
TEXTE = (".md", ".txt", ".json", ".yml", ".yaml", ".py", ".toml", ".html", ".css")

ECHO_VERS_FICHIER = re.compile(r"\b(echo|printf)\b[^|;&\n]*>>?\s*[^|;&\n]+")


def juger(commande: str) -> str | None:
    """Renvoie le motif de refus, ou None si la commande passe."""

    # G1 — heredoc à délimiteur nu ET écriture dans un fichier.
    if HEREDOC_NU.search(commande) and not HEREDOC_QUOTE.search(commande):
        if REDIRECTION.search(commande):
            delimiteur = HEREDOC_NU.search(commande).group(1)
            return (
                f"HEREDOC NON QUOTÉ « <<{delimiteur} » écrivant dans un fichier.\n"
                f"Le shell va interpoler $, ` et \\ dans le contenu : les accents graves "
                f"seront EXÉCUTÉS comme des commandes et les apostrophes mangées.\n"
                f"C'est exactement ce qui a mutilé gardien-du-sas.md — 49 lignes au lieu "
                f"de 83, toute sa section des six contrôles disparue (fiche E-34).\n"
                f"Écris <<'{delimiteur}' avec des quotes, ou mieux : utilise l'outil Write."
            )

    for appel in ECHO_VERS_FICHIER.finditer(commande):
        fragment = appel.group(0)
        cible = fragment.split(">")[-1].strip().strip("\"'")

        # G2 — accent grave dans un echo redirigé : substitution de commande.
        if "`" in fragment.split(">")[0]:
            return (
                "ACCENT GRAVE dans un echo/printf redirigé vers un fichier.\n"
                "Le shell exécutera ce qui est entre accents graves au lieu de l'écrire.\n"
                "Utilise l'outil Write."
            )

        # G3 — contenu multi-lignes vers un fichier de texte.
        if cible.endswith(TEXTE) and ("\\n" in fragment or "\n" in fragment):
            return (
                f"CONTENU MULTI-LIGNES écrit dans « {cible} » par le shell.\n"
                "Le contenu d'un fichier ne transite jamais par le shell (fiche E-34).\n"
                "Utilise l'outil Write, ou pathlib.write_text dans un script Python."
            )

    return None


def main() -> None:
    try:
        entree = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)  # Rien à juger : on ne bloque pas sur une entrée illisible.

    commande = (entree.get("tool_input") or {}).get("command", "")
    if not isinstance(commande, str) or not commande:
        sys.exit(0)

    motif = juger(commande)
    if motif is None:
        sys.exit(0)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": motif,
        },
        "systemMessage": "Garde d'écriture : le contenu d'un fichier ne passe pas par le shell.",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
