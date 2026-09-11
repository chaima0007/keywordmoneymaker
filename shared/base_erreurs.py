"""
base_erreurs — passerelle de la flotte Python vers la base d'erreurs de la chaîne.

POURQUOI CE MODULE EXISTE
Le dépôt contient deux substrats d'exécution qui s'ignoraient totalement (voir
`.claude/FRONTIERE-SUBSTRATS.md`) : les agents Markdown de `.claude/agents/`, lus par Claude Code,
et cette flotte Python, lancée par `main.py`. La règle « consulter la base d'erreurs avant d'agir »
est inscrite au `CLAUDE.md` §2 ter — que la flotte Python ne lit jamais. Ce module comble ce trou.

PRINCIPE DE CONCEPTION — il ne duplique rien.
Il **lit** `.claude/BASE-ERREURS.md` et `CLAUDE.md` comme sources uniques de vérité. Aucune fiche,
aucune question de contrôle n'est recopiée ici. C'est la leçon de la fiche E-01 : une règle qui vit
à plusieurs endroits finit par diverger, et personne ne remarque quelle copie est obsolète.
Corollaire : si le contenu de la base change, ce module suit sans être modifié.

USAGE
    import base_erreurs
    print(base_erreurs.rappel_demarrage())          # au lancement d'une session
    for f in base_erreurs.pour_action("créer un document au Drive"):
        print(f["id"], f["erreur"])                 # avant une action précise
    print(base_erreurs.regle_controle())            # avant de remettre un rapport
"""

from __future__ import annotations

import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CHEMIN_BASE = RACINE / ".claude" / "BASE-ERREURS.md"
CHEMIN_CLAUDE_MD = RACINE / "CLAUDE.md"
CHEMIN_FRONTIERE = RACINE / ".claude" / "FRONTIERE-SUBSTRATS.md"


class BaseIntrouvable(RuntimeError):
    """La base d'erreurs est absente ou illisible.

    On lève au lieu de retourner vide : une base silencieusement absente ferait croire
    « aucune erreur connue » alors que la vraie réponse est « je n'ai pas pu vérifier ».
    C'est exactement la confusion que documente la fiche E-16.
    """


def _lire(chemin: Path) -> str:
    try:
        return chemin.read_text(encoding="utf-8")
    except OSError as e:
        raise BaseIntrouvable(
            f"{chemin} illisible ({e}). NE PAS conclure « aucune erreur connue » : "
            f"la base n'a pas pu être consultée. Signale-le et corrige avant d'agir."
        ) from e


def index() -> list[dict[str, str]]:
    """Les lignes de l'INDEX de la base : id · erreur · signal de détection · rôle responsable."""
    texte = _lire(CHEMIN_BASE)
    lignes: list[dict[str, str]] = []
    for ligne in texte.splitlines():
        if not ligne.startswith("| E-"):
            continue
        cells = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cells) >= 4:
            lignes.append(
                {"id": cells[0], "erreur": cells[1], "signal": cells[2], "role": cells[3]}
            )
    if not lignes:
        raise BaseIntrouvable(
            f"{CHEMIN_BASE} lue mais aucune ligne d'index reconnue — format modifié ? "
            f"Ne pas conclure « aucune erreur connue »."
        )
    return lignes


def fiche(identifiant: str) -> str:
    """Le texte intégral d'une fiche (ex. « E-02 »), tel qu'il est écrit dans la base."""
    texte = _lire(CHEMIN_BASE)
    m = re.search(
        rf"^## {re.escape(identifiant)} —.*?(?=^## |\Z)", texte, re.MULTILINE | re.DOTALL
    )
    if not m:
        raise BaseIntrouvable(f"Fiche {identifiant} absente de {CHEMIN_BASE}.")
    return m.group(0).rstrip()


def pour_action(description: str) -> list[dict[str, str]]:
    """Les fiches dont le *signal de détection* recoupe l'action décrite.

    Volontairement grossier : on préfère proposer une fiche de trop que d'en rater une.
    Le filtre final reste le jugement de l'agent, pas cette fonction.
    """
    mots = {m for m in re.findall(r"\w{4,}", description.lower())}
    trouvees = []
    for ligne in index():
        cible = f"{ligne['signal']} {ligne['erreur']}".lower()
        if any(m in cible for m in mots):
            trouvees.append(ligne)
    return trouvees


def regle_controle() -> str:
    """Le §2 ter du CLAUDE.md — texte normatif du contrôle avant rapport, lu à la source."""
    texte = _lire(CHEMIN_CLAUDE_MD)
    m = re.search(r"^## 2 ter\..*?(?=^## \d|\Z)", texte, re.MULTILINE | re.DOTALL)
    if not m:
        raise BaseIntrouvable(
            f"§2 ter introuvable dans {CHEMIN_CLAUDE_MD}. La règle de contrôle avant rapport "
            f"n'a pas pu être lue — le dire, ne pas la contourner."
        )
    return m.group(0).rstrip()


def rappel_demarrage() -> str:
    """Rappel court à afficher au lancement d'une session de la flotte Python."""
    try:
        lignes = index()
    except BaseIntrouvable as e:
        return f"  /!\\ BASE D'ERREURS NON CONSULTABLE — {e}"
    return (
        f"  Base d'erreurs : {len(lignes)} fiches connues ({CHEMIN_BASE.relative_to(RACINE)}).\n"
        f"  AVANT D'AGIR   : lis les fiches dont le signal de détection ressemble a ton action.\n"
        f"  AVANT RAPPORT  : controle honnete (repetitions ? condition d'arret ?) — CLAUDE.md §2 ter.\n"
        f"  Erreur nouvelle : tu AJOUTES une fiche, tu ne modifies jamais les existantes.\n"
        f"  Deux substrats  : {CHEMIN_FRONTIERE.relative_to(RACINE)}"
    )


if __name__ == "__main__":
    print(rappel_demarrage())
    print()
    for l in index():
        print(f"  {l['id']}  {l['erreur']}")
