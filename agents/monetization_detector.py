"""
Agent 7 — Détecteur d'Opportunités de Monétisation Manquées
Lit un article (HTML ou Markdown) et détecte toutes les opportunités
d'affiliation, de lead gen et de monétisation que l'auteur n'a pas exploitées.
Calcule le manque à gagner et génère les liens/CTAs manquants.
"""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

PROJECT_ROOT = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
OUTPUT_DIR   = PROJECT_ROOT / "reports"

# Programmes d'affiliation à fort potentiel par niche
AFFILIATION_PROGRAMS = """
SEO & Contenu : Ahrefs (20% récurrent), Semrush (40%/$200/ref), Surfer SEO (25%), Rank Math (30%)
IA & Automation : Jasper (30%), Copy.ai (45%), Writesonic (30%), Notion AI (15%)
Hébergement : Kinsta ($50-500/ref), WP Engine ($200/ref), Cloudways ($30/ref)
Email Marketing : Mailchimp (30% rec.), ConvertKit (30% rec.), ActiveCampaign ($35+)
Formation : Udemy (15-25%), Teachable (30%), Kajabi ($69-$250/ref)
Finance : eToro ($100-200/ref), Trade Republic (€30/ref), Scaleway (20%)
Outils SaaS : HubSpot ($250-1000/ref), Monday.com (10-20%), ClickUp (20%)
"""


async def detect_monetization(file_path: str) -> str:
    path = Path(file_path).resolve()
    if not str(path).startswith(str(PROJECT_ROOT)):
        print(f"❌ Chemin hors projet : {file_path}")
        return ""
    if not path.exists():
        print(f"❌ Fichier introuvable : {file_path}")
        return ""

    prompt = f"""
Tu es un expert en monétisation de contenu et marketing d'affiliation.

Analyse le fichier suivant pour détecter toutes les opportunités de monétisation manquées :
Fichier : {path}

Programmes d'affiliation disponibles :
{AFFILIATION_PROGRAMS}

**Étapes :**

1. **Lis le fichier** avec Read

2. **Détecte chaque opportunité manquée** :
   Pour chaque sujet/outil/service mentionné sans lien d'affiliation :
   - Nom du produit/service mentionné
   - Programme d'affiliation correspondant
   - Commission estimée par conversion
   - Où insérer le lien dans le texte (citation exacte)
   - CTA suggéré (texte du lien d'ancrage)

3. **Calcule le manque à gagner** :
   Si cet article génère 1 000 visiteurs/mois avec un taux de conversion de 2% :
   | Opportunité | Commission | Conv./mois | Revenu/mois |
   |---|---|---|---|

4. **Génère les CTAs manquants** à insérer :
   Pour les 3 meilleures opportunités, rédige le bloc HTML/Markdown du CTA
   (bouton, texte d'ancrage, phrase d'accroche)

5. **Détecte les lead gen manqués** :
   - Y a-t-il un formulaire de capture email ? Sinon, propose-en un.
   - Y a-t-il un lead magnet (guide gratuit, checklist) ? Propose le sujet idéal.
   - Y a-t-il un quiz ou calculateur ? (fort taux de conversion)

6. **Score de monétisation** /10 avec potentiel non exploité en €/mois
"""

    filename = path.name
    print(f"\n💰 Détection opportunités — {filename}\n{'='*60}")
    content = ""
    try:
        async with asyncio.timeout(120):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=["Read"]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            print(block.text)
                            content += block.text
    except asyncio.TimeoutError:
        print(f"❌ Timeout : {filename}")
    except Exception as e:
        print(f"❌ Erreur : {type(e).__name__}: {e}")

    if content:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_name = path.stem.replace(" ", "_")[:30]
        out_path = OUTPUT_DIR / f"monetisation_{safe_name}_{date_str}.md"
        out_path.write_text(f"# Opportunités Monétisation — {filename}\n{date_str}\n\n{content}", encoding="utf-8")
        print(f"\n✅ Rapport sauvegardé : {out_path}")
        return str(out_path)
    return ""


async def scan_all_content() -> None:
    """Scanne tous les fichiers HTML et Markdown du projet."""
    files = [
        f for f in PROJECT_ROOT.rglob("*")
        if f.suffix.lower() in {".html", ".htm", ".md"}
        and not any(p in str(f) for p in [".git", ".venv", "agents", "reports", "security_reports", "linkedin_cv"])
    ]
    if not files:
        print("❌ Aucun fichier de contenu trouvé.")
        return
    print(f"🔎 {len(files)} fichier(s) de contenu détecté(s)")
    for f in files:
        await detect_monetization(str(f))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(detect_monetization(sys.argv[1]))
    else:
        asyncio.run(scan_all_content())
