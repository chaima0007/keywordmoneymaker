"""
Agent FISCALISTE — Optimisation Fiscale & Conformité Belge/EU
Calcule, optimise et protège : TVA, ISOC, IPP, cotisations INASTI,
déductions SaaS, revenus passifs, revenus étrangers.
⚠️  Information fiscale — ne remplace pas un comptable agréé.
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
OUTPUT_DIR   = PROJECT_ROOT / "fiscal"

PROFILS = {
    "freelance_be":  "Indépendant·e complémentaire ou à titre principal en Belgique",
    "saas_be":       "SaaS B2B belge — abonnements, clients EU et hors-EU",
    "agence_be":     "Agence digitale — prestations de services, sous-traitance",
    "revenus_mixtes":"Revenus salariés + revenus indépendants + revenus passifs",
    "tva_eu":        "Régime TVA UE — ventes de services digitaux B2C à l'étranger",
}


async def optimiser(
    situation: str,
    profil: str = "freelance_be",
    revenus_annuels: str = "50 000€",
) -> str:
    params = {"situation": situation[:200].lower(), "profil": profil}
    cached = cache.get("fiscaliste", params)
    if cached:
        return cached

    profil_desc = PROFILS.get(profil, profil)

    prompt = f"""Tu es FISCALISTE, expert en fiscalité belge et européenne pour entrepreneurs du numérique.
Tu conseilles Caelum Partners (agence digitale IA, Bruxelles) et ses clients.

Situation : "{situation}"
Profil     : {profil_desc}
Revenus estimés : {revenus_annuels}/an

---

## ANALYSE FISCALE FISCALISTE

### 1. SITUATION FISCALE ACTUELLE
- Régime applicable (IPP / ISOC / assujetti TVA / franchise)
- Taux effectifs applicables aujourd'hui
- Obligations déclaratives en cours

### 2. OPTIMISATIONS LÉGALES DISPONIBLES
Pour chaque optimisation :
| Levier | Économie estimée/an | Complexité | Risque |
|--------|--------------------:|------------|--------|
| ...    | ...€                | Faible/Moy/Élevée | Faible |

### 3. DÉDUCTIONS SOUVENT OUBLIÉES
Liste des charges déductibles que 80% des indépendants du numérique manquent :
- Matériel informatique et logiciels (taux)
- Abonnements SaaS professionnels
- Formation et documentation
- Bureau à domicile (calcul belge)
- Voiture/déplacements professionnels
- Cotisations et assurances

### 4. TVA — POINTS DE VIGILANCE
- Assujettissement ou franchise (seuil 25 000€ Belgique)
- Clients B2B EU : autoliquidation — ce qu'il faut facturer
- Clients B2C EU : OSS (One Stop Shop) — quand s'inscrire
- Revenus SaaS passifs : traitement TVA

### 5. COTISATIONS INASTI (si indépendant BE)
- Calcul estimatif basé sur {revenus_annuels}
- Provisions trimestrielles recommandées
- Astuces légales pour lisser les cotisations

### 6. CALENDRIER FISCAL {datetime.now().year}
Dates-clés à ne pas manquer et pénalités en cas de retard.

### 7. STRUCTURE OPTIMALE
Rester en personne physique vs créer une SRL ? Analyse coût/bénéfice.

### 8. ÉCONOMIE TOTALE ESTIMÉE
Si toutes les optimisations sont appliquées : économie annuelle estimée en €.

---
⚠️  Information fiscale à titre éducatif. Valider avec un comptable IPCF/IRE agréé."""

    print(f"\n💼 FISCALISTE — Optimisation : {profil}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(70):
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
        cache.set("fiscaliste", params, content, ttl_hours=72)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
        path = OUTPUT_DIR / f"fiscal_{profil}_{date_str}.md"
        path.write_text(
            f"# FISCALISTE — {profil.upper()}\n"
            f"**Situation :** {situation}\n"
            f"**Revenus :** {revenus_annuels}\n"
            f"**Date :** {date_str}\n\n{content}",
            encoding="utf-8",
        )
        print(f"\n✅ Rapport : {path}")
        return str(path)
    return ""


async def bilan_annuel(revenus: str = "50 000€") -> str:
    """Lance les 3 analyses fiscales clés en parallèle."""
    situations = [
        ("Optimiser mes revenus de SaaS et prestations d'agence", "saas_be"),
        ("Gérer la TVA sur mes abonnements vendus à des clients EU", "tva_eu"),
        ("Revenus actifs agence + revenus passifs SEO en même temps", "revenus_mixtes"),
    ]
    print(f"\n📊 FISCALISTE — Bilan Annuel Complet\n{'='*60}")
    results = await asyncio.gather(
        *[optimiser(s, p, revenus) for s, p in situations],
        return_exceptions=True,
    )
    paths = [r for r in results if isinstance(r, str) and r]
    print(f"\n✅ {len(paths)}/{len(situations)} rapports générés")
    return "\n".join(paths)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        profil_arg  = sys.argv[1] if sys.argv[1] in PROFILS else "freelance_be"
        revenus_arg = sys.argv[2] if len(sys.argv) > 2 else "50 000€"
        situation_arg = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else (
            "Je génère des revenus via une agence digitale et un SaaS SEO, comment optimiser ma fiscalité ?"
        )
        asyncio.run(optimiser(situation_arg, profil_arg, revenus_arg))
    else:
        asyncio.run(bilan_annuel())
