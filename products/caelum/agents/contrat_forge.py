"""
Agent CONTRAT_FORGE — Générateur de Contrats & Documents Légaux
CGV, CGU, NDA, contrat client, mentions légales, politique de confidentialité.
Adapté au droit belge, RGPD, e-commerce UE, SaaS B2B.
⚠️  Documents à valider par un avocat avant signature officielle.
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
OUTPUT_DIR   = PROJECT_ROOT / "contrats"

TYPES_CONTRATS = {
    "nda":              "Accord de confidentialité (NDA) bilatéral",
    "contrat_client":   "Contrat de prestation de services digitaux",
    "cgv_saas":         "Conditions Générales de Vente — SaaS abonnement",
    "cgu":              "Conditions Générales d'Utilisation — plateforme web",
    "mentions_legales": "Mentions légales + politique de confidentialité RGPD",
    "sous_traitance":   "Contrat de sous-traitance freelance",
    "lettre_relance":   "Lettre de relance client impayé (3 niveaux)",
    "mise_en_demeure":  "Mise en demeure formelle avant procédure",
}


async def generer(
    type_contrat: str = "contrat_client",
    infos: dict | None = None,
) -> str:
    if infos is None:
        infos = {}

    prestataire = infos.get("prestataire", "Caelum Partners — Chaïma [NOM], Bruxelles, Belgique")
    client      = infos.get("client",      "[NOM DU CLIENT], [VILLE], [PAYS]")
    objet       = infos.get("objet",       "Prestation de services digitaux IA")
    montant     = infos.get("montant",     "[MONTANT]€ HT")
    duree       = infos.get("duree",       "1 mois / durée indéterminée")

    params = {"type": type_contrat, "objet": objet[:100].lower()}
    cached = cache.get("contrat_forge", params)
    if cached:
        return cached

    type_desc = TYPES_CONTRATS.get(type_contrat, type_contrat)

    prompt = f"""Tu es CONTRAT_FORGE, expert en rédaction de documents juridiques pour entrepreneurs du numérique.
Droit applicable : droit belge + règlements européens (RGPD, directive e-commerce).

Génère un {type_desc} complet et professionnel.

**Parties :**
- Prestataire : {prestataire}
- Client      : {client}
- Objet       : {objet}
- Montant     : {montant}
- Durée       : {duree}

---

# {type_desc.upper()}

Génère le document complet avec :
- Toutes les clauses essentielles pour ce type de contrat
- Langage clair, non ambigu, juridiquement solide
- Conformité droit belge + RGPD si données personnelles en jeu
- Variables à personnaliser entre [CROCHETS]
- Numérotation claire des articles

Inclure obligatoirement :
1. Identification des parties
2. Objet et périmètre exact de la prestation
3. Obligations de chaque partie
4. Conditions financières et modalités de paiement
5. Propriété intellectuelle (qui possède quoi après livraison)
6. Confidentialité
7. Responsabilité et limitations
8. Résiliation et conséquences
9. Loi applicable et juridiction compétente (Belgique)
10. Signatures et date

Pour les CGV/CGU SaaS, ajouter :
- Clause de modification unilatérale des conditions
- Politique de remboursement
- Clause de non-disponibilité (SLA)
- Traitement des données (DPA intégré si B2B EU)

Pour les lettres de relance/mise en demeure :
- 3 niveaux de ton (amiable → ferme → judiciaire)
- Délai légal de réponse
- Mention des intérêts de retard légaux (Belgique : taux BCE + 8%)

---
⚠️  Document à valider par un avocat agréé avant toute utilisation officielle.
Variables entre [CROCHETS] à compléter avant signature."""

    print(f"\n📄 CONTRAT_FORGE — {type_desc}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(90):
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
        cache.set("contrat_forge", params, content, ttl_hours=168)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        path = OUTPUT_DIR / f"{type_contrat}_{date_str}.md"
        path.write_text(
            f"# {type_desc}\n_Généré le {date_str} — À valider par un avocat_\n\n{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Document : {path}")
        return str(path)
    return ""


async def kit_juridique_complet() -> None:
    """Génère le kit juridique de démarrage complet en parallèle."""
    docs = [
        ("cgv_saas",         {}),
        ("mentions_legales", {}),
        ("nda",              {}),
        ("contrat_client",   {"montant": "1 500€ HT/mois"}),
    ]
    print(f"\n🏛️  CONTRAT_FORGE — Kit Juridique Complet ({len(docs)} documents)\n{'='*60}")
    results = await asyncio.gather(
        *[generer(t, i) for t, i in docs],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/{len(docs)} documents générés dans contrats/")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        type_arg = sys.argv[1] if sys.argv[1] in TYPES_CONTRATS else "contrat_client"
        asyncio.run(generer(type_arg))
    else:
        asyncio.run(kit_juridique_complet())
