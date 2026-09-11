"""
Agent GDPR_GARDE — Gardien RGPD & Protection des Données
Audit de conformité RGPD, registre des traitements, politique de confidentialité,
gestion des droits utilisateurs, breach notification, DPA B2B.
⚠️  Analyse informative — l'autorité de contrôle belge est l'APD (autoriteprotectiondonnees.be).
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
OUTPUT_DIR   = PROJECT_ROOT / "gdpr"

TYPES_AUDIT = {
    "site_web":        "Site web avec formulaire de contact et analytics",
    "saas_b2b":        "SaaS B2B — traitement données clients professionnels",
    "saas_b2c":        "SaaS B2C — traitement données utilisateurs particuliers",
    "email_marketing": "Collecte emails et campagnes marketing",
    "ia_contenu":      "Utilisation de l'IA pour générer du contenu sur données utilisateurs",
    "sous_traitant":   "Position de sous-traitant RGPD (DPA requis)",
}


async def audit_rgpd(contexte: str = "site_web", description: str = "") -> str:
    params = {"contexte": contexte, "desc": description[:150].lower()}
    cached = cache.get("gdpr_garde", params)
    if cached:
        return cached

    type_desc = TYPES_AUDIT.get(contexte, contexte)
    desc_block = f"\nDescription du système : {description}" if description else ""

    prompt = f"""Tu es GDPR_GARDE, expert en conformité RGPD et protection des données personnelles.
Tu interviens pour Caelum Partners (agence digitale IA, Bruxelles — soumise au droit belge et au RGPD UE).

Contexte à auditer : {type_desc}{desc_block}

---

## AUDIT RGPD — GDPR_GARDE

### 1. CARTOGRAPHIE DES DONNÉES COLLECTÉES
Pour chaque donnée identifiée :
| Donnée | Base légale | Durée conservation | Risque RGPD |
|--------|------------|-------------------|-------------|

Bases légales possibles : consentement / contrat / intérêt légitime / obligation légale

### 2. REGISTRE DES TRAITEMENTS (Article 30)
Entrée de registre prête à copier-coller :
- Nom du traitement
- Finalité
- Catégories de personnes concernées
- Catégories de données
- Destinataires
- Transferts hors UE (et garanties)
- Durée de conservation

### 3. SCORE DE CONFORMITÉ RGPD
Note /10 avec détail par critère :
- [ ] Politique de confidentialité visible et complète
- [ ] Bandeau cookies conforme (pas de dark pattern)
- [ ] Formulaires avec case à cocher non pré-cochée
- [ ] Registre des traitements tenu à jour
- [ ] DPA signé avec sous-traitants
- [ ] Procédure de réponse aux demandes (droits RGPD 72h)
- [ ] Procédure de notification de violation (72h à l'APD)
- [ ] Données minimisées (pas de collecte excessive)
- [ ] Chiffrement des données au repos et en transit
- [ ] Politique de retention et suppression

### 4. VIOLATIONS IDENTIFIÉES
Chaque violation classée par sévérité :
🔴 CRITIQUE (amende jusqu'à 4% CA mondial ou 20M€)
🟠 ÉLEVÉE (amende jusqu'à 2% CA)
🟡 MODÉRÉE (mise en demeure probable)

### 5. PLAN DE MISE EN CONFORMITÉ
Actions classées par priorité et effort :
| Action | Délai | Effort | Amende évitée |
|--------|-------|--------|---------------|

### 6. MODÈLE DE RÉPONSE AUX DROITS RGPD
Textes prêts à l'emploi pour :
- Droit d'accès (Article 15)
- Droit à l'effacement (Article 17)
- Droit d'opposition (Article 21)

### 7. CLAUSE DPA PRÊTE À INSÉRER
Si vous êtes sous-traitant, clause DPA Article 28 à insérer dans vos contrats.

---
⚠️  Pour toute violation suspectée ou amende reçue, contacter l'APD Belgique :
autoriteprotectiondonnees.be | +32 2 274 48 00"""

    print(f"\n🔒 GDPR_GARDE — Audit RGPD : {type_desc}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(75):
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
        cache.set("gdpr_garde", params, content, ttl_hours=48)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        path = OUTPUT_DIR / f"rgpd_{contexte}_{date_str}.md"
        path.write_text(
            f"# GDPR_GARDE — Audit RGPD : {type_desc}\n"
            f"**Date :** {date_str}\n\n{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Rapport : {path}")
        return str(path)
    return ""


async def audit_complet_caelum() -> None:
    """Audit RGPD complet pour Caelum Partners (site + SaaS + emails)."""
    audits = [
        ("site_web",        "Site caelumpartners.agency avec formulaire contact"),
        ("saas_b2b",        "KeywordMoneyMaker — génération articles SEO pour clients professionnels"),
        ("email_marketing", "Collecte emails via formulaire et newsletter mensuelle"),
        ("ia_contenu",      "Utilisation Claude AI pour générer contenu basé sur données clients"),
    ]
    print(f"\n🛡️  GDPR_GARDE — Audit Complet Caelum Partners\n{'='*60}")
    results = await asyncio.gather(
        *[audit_rgpd(ctx, desc) for ctx, desc in audits],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/{len(audits)} audits complétés dans gdpr/")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        contexte_arg = sys.argv[1] if sys.argv[1] in TYPES_AUDIT else "site_web"
        desc_arg     = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        asyncio.run(audit_rgpd(contexte_arg, desc_arg))
    else:
        asyncio.run(audit_complet_caelum())
