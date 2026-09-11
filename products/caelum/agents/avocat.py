"""
Agent AVOCAT — Protection Juridique & Analyse de Risques Légaux
Analyse tout document, situation ou contrat sous l'angle juridique.
Droit belge, droit européen, droit du numérique, e-commerce, SaaS.
⚠️  Information juridique — ne remplace pas un avocat agréé.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "juridique"

DOMAINES = {
    "contrat":    "Analyse et risques d'un contrat client/prestataire",
    "cgv":        "Conditions Générales de Vente / d'Utilisation SaaS",
    "gdpr":       "Conformité RGPD et protection des données",
    "travail":    "Droit du travail belge — freelance vs salarié",
    "saas":       "Aspects juridiques d'un SaaS B2B en Belgique/UE",
    "propriete":  "Propriété intellectuelle, droits d'auteur, marques",
    "litige":     "Gestion d'un litige commercial ou client difficile",
}


async def analyser(situation: str, domaine: str = "saas", contexte: str = "") -> str:
    params = {"situation": situation[:200].lower(), "domaine": domaine}
    cached = cache.get("avocat", params)
    if cached:
        return cached

    contexte_block = f"\nContexte additionnel :\n{contexte}" if contexte else ""
    domaine_desc   = DOMAINES.get(domaine, domaine)

    prompt = f"""Tu es AVOCAT, expert en droit belge, droit européen et droit du numérique.
Tu conseilles Caelum Partners, agence digitale IA basée à Bruxelles (SaaS, freelance, B2B).

Situation soumise : "{situation}"{contexte_block}
Domaine juridique : {domaine_desc}

---

## ANALYSE JURIDIQUE AVOCAT

### 1. QUALIFICATION JURIDIQUE
Qualifie la situation en termes légaux précis (droit applicable, articles pertinents).

### 2. RISQUES IDENTIFIÉS
Pour chaque risque :
| Risque | Probabilité | Impact | Priorité |
|--------|-------------|--------|---------|
| ...    | Faible/Moyen/Élevé | € ou réputation | 🔴/🟠/🟡 |

### 3. CADRE LÉGAL APPLICABLE
- Lois belges concernées (avec articles)
- Règlements européens (RGPD, DSA, DMA si pertinent)
- Jurisprudence utile si connue

### 4. ACTIONS PROTECTRICES IMMÉDIATES
Liste ordonnée des actions à prendre maintenant :
1. ...
2. ...

### 5. CLAUSES À INCLURE / ÉVITER
Ce qu'il FAUT mettre par écrit et ce qu'il NE FAUT PAS dire ou écrire.

### 6. SEUIL D'ALERTE
À quel moment consulter un vrai avocat en urgence (signe avant-coureur).

### 7. COÛT DE L'INACTION
Estimation de ce que coûte de ne rien faire (amendes, préjudice, perte client).

---
⚠️  Cette analyse est fournie à titre informatif. Pour toute situation à fort enjeu,
consulter Maître [avocat agréé au barreau de Bruxelles]."""

    print(f"\n⚖️  AVOCAT — Analyse juridique : {domaine}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(60):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            print(block.text)
                            content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ {type(e).__name__}: {e}")

    if content:
        cache.set("avocat", params, content, ttl_hours=48)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        safe = situation[:35].replace(" ", "_")
        path = OUTPUT_DIR / f"avocat_{domaine}_{safe}_{date_str}.md"
        path.write_text(
            f"# AVOCAT — {domaine.upper()}\n**Situation :** {situation}\n**Date :** {date_str}\n\n{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Rapport : {path}")
        return str(path)
    return ""


async def audit_saas_complet() -> str:
    """Audit juridique complet pour un SaaS B2B en Belgique."""
    situations = [
        ("Un client refuse de payer la facture après livraison du site", "litige"),
        ("On collecte des emails via un formulaire sur le site", "gdpr"),
        ("On sous-traite à un freelance pour un projet client", "contrat"),
    ]
    print(f"\n🏛️  AVOCAT — Audit SaaS Complet ({len(situations)} analyses)\n{'='*60}")
    results = await asyncio.gather(
        *[analyser(s, d) for s, d in situations],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/{len(situations)} analyses complétées")
    return "\n".join(paths)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        domaine_arg = sys.argv[1] if sys.argv[1] in DOMAINES else "saas"
        situation_arg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else (
            "Un client nous demande les droits exclusifs sur tous les contenus IA générés pour lui"
        )
        asyncio.run(analyser(situation_arg, domaine_arg))
    else:
        asyncio.run(audit_saas_complet())
