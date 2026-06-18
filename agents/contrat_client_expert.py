"""
Agent CONTRAT_CLIENT_EXPERT — Contrats de Signature Client Premium
Génère des contrats professionnels sur mesure pour chaque offre Caelum Partners.
Protège sur chaque clause critique : paiement, PI, révisions, résiliation, scope creep.
Droit belge · RGPD · Directive services UE · Signature électronique valide.
⚠️  À valider par un avocat agréé avant utilisation officielle.
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
OUTPUT_DIR   = PROJECT_ROOT / "contrats_clients"

OFFRES = {
    "presence_web": {
        "nom":       "Contrat Présence Web — 500€",
        "montant":   "500€ HT",
        "duree":     "Prestation one-shot, livraison en 7 jours calendaires",
        "livrable":  "Site web 1 page responsive, hébergé sur Cloudflare Pages",
        "paiement":  "50% à la signature (250€), 50% à la livraison (250€)",
        "revisions": "1 révision incluse dans les 7 jours suivant la livraison",
        "risques":   "Scope creep, demandes illimitées de modifications, retard de validation client",
    },
    "croissance_auto": {
        "nom":       "Contrat Croissance Automatisée — 1 500€/mois",
        "montant":   "1 500€ HT/mois",
        "duree":     "Engagement minimum 3 mois, puis mensuel avec préavis 30 jours",
        "livrable":  "20 articles SEO, rapport mensuel, séquences outreach, monitoring",
        "paiement":  "Prélèvement ou virement le 1er de chaque mois, pénalité 1.5%/mois de retard",
        "revisions": "Contenu livré selon brief validé — modifications majeures facturées 75€/h",
        "risques":   "Non-paiement récurrent, résiliation anticipée sans préavis, brief incomplet",
    },
    "partenariat_strategique": {
        "nom":       "Contrat Partenariat Stratégique — 3 000€/mois",
        "montant":   "3 000€ HT/mois",
        "duree":     "Engagement minimum 6 mois, renouvellement tacite, préavis 60 jours",
        "livrable":  "Suite complète : 50 articles, pitch deck, stratégie LinkedIn, RÉSOLVEUR dédié",
        "paiement":  "Virement le 1er du mois, clause d'indexation annuelle IPCH Belgique",
        "revisions": "Réunion bi-mensuelle incluse, modifications stratégiques sous 48h",
        "risques":   "Confidentialité, exclusivité sectorielle, accès données sensibles client",
    },
}

CLAUSES_CRITIQUES = """
CLAUSES À NE JAMAIS OMETTRE :
1. Propriété intellectuelle — qui possède quoi AVANT et APRÈS livraison
2. Confidentialité réciproque — données client ET méthodes Caelum
3. Limitation de responsabilité — plafond = montant du contrat
4. Résiliation pour faute — délai 15 jours pour remédier avant résiliation
5. Résiliation sans faute — préavis + indemnité équivalente à 1 mensualité
6. Scope creep — toute demande hors périmètre = devis séparé
7. Validation client — silence de 5 jours = validation tacite
8. Force majeure — suspension sans pénalité (panne API, incident technique)
9. Clause anti-débauchage — interdiction de recruter nos collaborateurs 12 mois
10. Juridiction — Tribunaux de Bruxelles, droit belge applicable
"""


async def generer_contrat(
    offre: str = "presence_web",
    client_nom: str = "[NOM DU CLIENT]",
    client_adresse: str = "[ADRESSE DU CLIENT]",
    client_email: str = "[EMAIL DU CLIENT]",
    client_tva: str = "[NUMÉRO TVA OU 'Particulier']",
    date_debut: str = "",
    specificites: str = "",
) -> str:
    if offre not in OFFRES:
        print(f"❌ Offre inconnue. Choisir : {', '.join(OFFRES.keys())}")
        return ""

    o = OFFRES[offre]
    if not date_debut:
        date_debut = datetime.now().strftime("%d/%m/%Y")

    params = {"offre": offre, "client": client_nom[:50].lower()}
    cached = cache.get("contrat_client_expert", params)
    if cached and "[NOM DU CLIENT]" not in client_nom:
        pass  # Ne pas utiliser le cache si client réel

    specificites_block = f"\nSpécificités demandées : {specificites}" if specificites else ""

    prompt = f"""Tu es CONTRAT_CLIENT_EXPERT, avocat spécialisé en droit des services numériques belge.
Tu rédiges des contrats de prestation pour Caelum Partners — agence digitale IA, Bruxelles.

**OFFRE :** {o['nom']}
**MONTANT :** {o['montant']}
**DURÉE :** {o['duree']}
**LIVRABLES :** {o['livrable']}
**PAIEMENT :** {o['paiement']}
**RÉVISIONS :** {o['revisions']}
**RISQUES SPÉCIFIQUES :** {o['risques']}{specificites_block}

**PARTIES :**
- Prestataire : Caelum Partners, représenté par Chaïma [NOM], [ADRESSE BRUXELLES], TVA BE [NUMÉRO]
- Client      : {client_nom}, {client_adresse}, Email : {client_email}, TVA/Réf : {client_tva}
- Date de début : {date_debut}

{CLAUSES_CRITIQUES}

---

Génère le contrat COMPLET avec ces sections, en français juridique clair et sans ambiguïté :

# CONTRAT DE PRESTATION DE SERVICES NUMÉRIQUES
## {o['nom']}

**Entre les soussignés :**
[Identification complète des deux parties]

---

## ARTICLE 1 — OBJET DU CONTRAT
[Description précise de la mission, sans vague]

## ARTICLE 2 — LIVRABLES ET PÉRIMÈTRE
[Liste exhaustive de ce qui EST inclus + ce qui N'EST PAS inclus]
[Clause scope creep : toute demande hors périmètre = avenant écrit]

## ARTICLE 3 — PLANNING ET DÉLAIS
[Dates, jalons, conditions de livraison]
[Clause de validation tacite : 5 jours ouvrés sans retour = validation]

## ARTICLE 4 — CONDITIONS FINANCIÈRES
[Montant HT/TTC, échéancier précis]
[Conditions de paiement : mode, délai, pénalités de retard]
[Clause d'indexation si contrat long terme]
[Que se passe-t-il si le client arrête en cours de mission]

## ARTICLE 5 — PROPRIÉTÉ INTELLECTUELLE
[Ce que le client possède après paiement complet]
[Ce que Caelum Partners conserve (méthodes, outils, agents IA)]
[Droits sur les contenus IA générés]
[Licence d'utilisation si PI non transférée]

## ARTICLE 6 — CONFIDENTIALITÉ
[Obligations réciproques — durée 3 ans après fin de contrat]
[Données sensibles identifiées par le client]
[Interdiction de divulguer les méthodes propriétaires Caelum]

## ARTICLE 7 — TRAITEMENT DES DONNÉES (RGPD)
[Rôle de chaque partie : responsable de traitement vs sous-traitant]
[Base légale du traitement]
[Durée de conservation, suppression]
[Droits des personnes concernées]

## ARTICLE 8 — OBLIGATIONS DU CLIENT
[Fournir les accès, briefs, validations dans les délais]
[Conséquences du retard client sur le planning]
[Respect de la loi dans l'utilisation des livrables]

## ARTICLE 9 — RESPONSABILITÉ ET GARANTIES
[Plafond de responsabilité = montant total du contrat]
[Exclusions : force majeure, faute du client, tiers]
[Garantie de conformité sur 30 jours après livraison]

## ARTICLE 10 — RÉSILIATION
[Résiliation pour faute : préavis 15 jours pour remédier]
[Résiliation sans faute : préavis + indemnité]
[Résiliation immédiate : cas de non-paiement > 30 jours]
[Sort des livrables en cours à la résiliation]

## ARTICLE 11 — CLAUSE ANTI-DÉBAUCHAGE
[12 mois après fin de contrat]

## ARTICLE 12 — FORCE MAJEURE
[Définition adaptée au numérique : pannes API, cyberattaques, etc.]

## ARTICLE 13 — DISPOSITIONS GÉNÉRALES
[Modifications : avenant signé des deux parties]
[Nullité partielle : reste du contrat maintenu]
[Loi applicable : droit belge]
[Juridiction : Tribunaux de l'arrondissement de Bruxelles]
[Langue : version française fait foi]

---

## SIGNATURES

**Fait à Bruxelles, le {date_debut}**
**En deux exemplaires originaux**

| Caelum Partners | {client_nom} |
|----------------|--------------|
| Chaïma [NOM]   | [Nom du signataire] |
| Date : _______ | Date : _______ |
| Signature :    | Signature : |
| Lu et approuvé | Lu et approuvé |

---

## ANNEXE A — DESCRIPTION DÉTAILLÉE DES LIVRABLES
[Spécifications techniques précises de chaque livrable]

## ANNEXE B — GRILLE TARIFAIRE PRESTATIONS SUPPLÉMENTAIRES
[Prix horaire : 75€/h HT]
[Urgence <48h : majoration 50%]
[Traductions : 0,12€/mot]

---
⚠️  Document généré par CONTRAT_CLIENT_EXPERT (Caelum Partners).
À valider par Maître [Avocat] au barreau de Bruxelles avant première utilisation."""

    print(f"\n📋 CONTRAT_CLIENT_EXPERT — {o['nom']}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(120):
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
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        safe_client = client_nom[:30].replace(" ", "_").replace("[", "").replace("]", "")
        path = OUTPUT_DIR / f"contrat_{offre}_{safe_client}_{date_str}.md"
        path.write_text(
            f"<!-- CONTRAT CAELUM PARTNERS — {o['nom']} -->\n"
            f"<!-- Client : {client_nom} | Date : {date_str} -->\n"
            f"<!-- ⚠️  À VALIDER PAR UN AVOCAT AVANT SIGNATURE -->\n\n"
            f"{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Contrat prêt : {path}")
        return str(path)
    return ""


async def generer_tous_modeles() -> None:
    """Génère les 3 modèles de contrats en parallèle."""
    print(f"\n⚖️  CONTRAT_CLIENT_EXPERT — Génération des 3 modèles\n{'='*60}")
    results = await asyncio.gather(
        generer_contrat("presence_web"),
        generer_contrat("croissance_auto"),
        generer_contrat("partenariat_strategique"),
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/3 modèles générés dans contrats_clients/")
    for p in paths:
        print(f"   → {p}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        offre_arg  = sys.argv[1] if sys.argv[1] in OFFRES else "presence_web"
        client_arg = sys.argv[2] if len(sys.argv) > 2 else "[NOM DU CLIENT]"
        asyncio.run(generer_contrat(offre_arg, client_arg))
    else:
        asyncio.run(generer_tous_modeles())
