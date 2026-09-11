"""
Protocole d'audit partagé de la flotte — Journal Drive.

Règle de la maison : chaque agent qui termine un travail dépose un AUDIT propre
— titre clair + synopsis complet — pour que Chaima ET les agents collègues
sachent qui a fait quoi, quand, et avec quel résultat.

Le COMMANDANT (orchestrateur) :
  1. AVANT d'agir  → lit le journal (read_journal) pour ne pas refaire un travail
     déjà fait par un autre agent / un autre service.
  2. APRÈS chaque mission → écrit un audit (record_audit).

Les entrées sont écrites dans PROJECT_ROOT/audit_drive/ :
  - manifest.jsonl        : une ligne JSON par audit (lecture machine, ordre chrono)
  - <titre_propre>.md     : un fichier lisible par audit (déposé sur le Drive)

RÈGLE DE SÉCURITÉ : aucune donnée sensible (mot de passe, clé API, secret,
token) ne doit jamais être écrite dans un audit. Le protocole s'applique à tous.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
AUDIT_DIR = PROJECT_ROOT / "audit_drive"
MANIFEST = AUDIT_DIR / "manifest.jsonl"

# Motifs interdits : on refuse d'écrire un audit qui ressemble à un secret.
_SECRET_HINTS = re.compile(
    r"(?i)(password|passwd|mot de passe|api[_\- ]?key|secret|token|"
    r"authorization:\s*bearer|-----BEGIN)"
)

STATUTS = {"ok": "✅", "attention": "⚠️", "echec": "❌", "en_cours": "⏳"}


def _slug(text: str, maxlen: int = 60) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip()
    text = re.sub(r"\s+", "_", text)
    return text[:maxlen].strip("_") or "sans_titre"


def titre_propre(agent: str, sujet: str, horodatage: datetime | None = None) -> str:
    """Titre normalisé : '2026-07-13 16h46 — [AGENT] — sujet'."""
    h = horodatage or datetime.now()
    return f"{h.strftime('%Y-%m-%d %Hh%M')} — [{agent.upper()}] — {sujet.strip()}"


def _contient_secret(*parts: str) -> bool:
    return any(_SECRET_HINTS.search(p or "") for p in parts)


def record_audit(
    agent: str,
    sujet: str,
    synopsis: str,
    statut: str = "ok",
    details: str = "",
    service: str = "",
) -> str:
    """
    Dépose un audit propre du travail d'un agent.

    agent    : nom de l'agent qui a fait le travail (ex: 'commandant', 'avocat').
    sujet    : sujet court et clair (sert au titre).
    synopsis : résumé COMPLET et lisible (2-6 phrases) — le cœur de l'audit,
               pour que tout le monde comprenne sans ouvrir autre chose.
    statut   : 'ok' | 'attention' | 'echec' | 'en_cours'.
    details  : compléments optionnels (chiffres, chemins, décisions).
    service  : service concerné (ex: 'SEO', 'Juridique', 'Web/Déploiement').

    Retourne le chemin du fichier .md créé.
    """
    if statut not in STATUTS:
        statut = "ok"

    if _contient_secret(synopsis, details):
        raise ValueError(
            "AUDIT REFUSÉ : le contenu ressemble à un secret. "
            "Le protocole interdit d'écrire mots de passe / clés / tokens."
        )

    now = datetime.now()
    titre = titre_propre(agent, sujet, now)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)

    entry = {
        "horodatage": now.strftime("%Y-%m-%d %H:%M:%S"),
        "agent": agent,
        "service": service,
        "sujet": sujet,
        "statut": statut,
        "synopsis": synopsis.strip(),
        "details": details.strip(),
        "titre": titre,
    }

    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    md = (
        f"# {titre}\n\n"
        f"**Agent :** {agent}\n"
        f"**Service :** {service or '—'}\n"
        f"**Statut :** {STATUTS[statut]} {statut}\n"
        f"**Horodatage :** {entry['horodatage']} (Europe/Bruxelles)\n\n"
        f"## Synopsis\n{synopsis.strip()}\n"
    )
    if details.strip():
        md += f"\n## Détails\n{details.strip()}\n"
    md += "\n---\n*Audit déposé automatiquement selon le protocole de la flotte. Aucune donnée sensible.*\n"

    path = AUDIT_DIR / f"{now.strftime('%Y-%m-%d_%H%M')}_{agent}_{_slug(sujet)}.md"
    path.write_text(md, encoding="utf-8")
    return str(path)


def read_journal(limit: int = 20) -> list[dict]:
    """
    Lit les derniers audits (les plus récents en premier).
    Le COMMANDANT l'appelle AVANT d'agir pour savoir ce que les autres
    agents / services ont déjà fait et agir en conséquence.
    """
    if not MANIFEST.exists():
        return []
    entries: list[dict] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return list(reversed(entries))[:limit]


def resume_journal(limit: int = 20) -> str:
    """Résumé texte du journal, injectable dans un prompt d'orchestrateur."""
    entries = read_journal(limit)
    if not entries:
        return "Journal vide : aucun travail antérieur enregistré."
    lignes = [
        f"- {e['horodatage']} · [{e['agent']}] {STATUTS.get(e['statut'], '')} "
        f"{e['sujet']} — {e['synopsis'][:120]}"
        for e in entries
    ]
    return "TRAVAUX DÉJÀ EFFECTUÉS (journal de la flotte) :\n" + "\n".join(lignes)


if __name__ == "__main__":
    # Démonstration / test rapide du protocole.
    p = record_audit(
        agent="drive_audit",
        sujet="Initialisation du protocole d'audit partagé",
        synopsis=(
            "Mise en place du module d'audit commun à toute la flotte. "
            "Chaque agent dépose désormais un audit propre (titre + synopsis) "
            "après son travail ; le COMMANDANT lit le journal avant d'agir."
        ),
        statut="ok",
        service="Gouvernance/Flotte",
        details="Fichiers : audit_drive/manifest.jsonl + un .md par audit.",
    )
    print("Audit de test écrit :", p)
    print("\n" + resume_journal())
