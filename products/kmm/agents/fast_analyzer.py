"""
Agent FAST — Analyse Rapide avec Cache Intégré
Version allégée du keyword_analyzer : prompt court, cache 24h, réponse en <15s.
Pour les analyses à la volée sans attendre 60 secondes.
"""

import asyncio
import os
import sys
import time
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions

sys.path.insert(0, str(Path(__file__).parent))
import cache_manager as cache

OUTPUT_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) / "reports"


async def fast_keyword(keyword: str, langue: str = "fr") -> str:
    params = {"keyword": keyword.strip().lower(), "langue": langue}
    cached = cache.get("fast_keyword", params)
    if cached:
        return cached

    prompt = f"""Analyse SEO rapide pour "{keyword}" ({langue}). Réponds en moins de 200 mots avec :
- Volume estimé (req/mois) et tendance (↑↓→)
- Difficulté /100
- Intention (informationnelle / commerciale / transactionnelle)
- Top 3 sous-mots-clés longue traîne
- 1 angle d'article différenciant
- Score d'opportunité /10"""

    print(f"\n⚡ FAST Keyword — {keyword}")
    t0 = time.perf_counter()
    content = ""
    try:
        async with asyncio.timeout(30):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout (30s)")
        return ""
    except Exception as e:
        print(f"❌ {type(e).__name__}: {e}")
        return ""

    elapsed = round(time.perf_counter() - t0, 1)
    print(f"✅ Terminé en {elapsed}s")
    print(content)

    if content:
        cache.set("fast_keyword", params, content, ttl_hours=24)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUTPUT_DIR / f"fast_{keyword[:30].replace(' ', '_')}.md"
        out.write_text(f"# Analyse Rapide — {keyword}\n\n{content}", encoding="utf-8")

    return content


async def fast_idea(niche: str, langue: str = "fr") -> str:
    params = {"niche": niche.strip().lower(), "langue": langue}
    cached = cache.get("fast_idea", params)
    if cached:
        return cached

    prompt = f"""Génère 5 idées d'articles SEO à fort potentiel pour la niche "{niche}" ({langue}).
Pour chaque idée : titre, mot-clé principal, volume estimé, difficulté /100, angle unique.
Format compact, 30 mots max par idée."""

    print(f"\n⚡ FAST Ideas — {niche}")
    t0 = time.perf_counter()
    content = ""
    try:
        async with asyncio.timeout(25):
            async for message in query(
                prompt=prompt,
                options=ClaudeAgentOptions(allowed_tools=[]),
            ):
                if hasattr(message, "content") and message.content:
                    for block in message.content:
                        if hasattr(block, "text"):
                            content += block.text
    except asyncio.TimeoutError:
        print("❌ Timeout (25s)")
        return ""
    except Exception as e:
        print(f"❌ {type(e).__name__}: {e}")
        return ""

    elapsed = round(time.perf_counter() - t0, 1)
    print(f"✅ {elapsed}s")
    print(content)

    if content:
        cache.set("fast_idea", params, content, ttl_hours=12)

    return content


async def fast_batch(keywords: list[str], langue: str = "fr") -> list[str]:
    """Analyse plusieurs mots-clés en parallèle avec cache."""
    results = await asyncio.gather(
        *[fast_keyword(kw, langue) for kw in keywords],
        return_exceptions=True,
    )
    return [r if isinstance(r, str) else "" for r in results]


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "keyword"
    if mode == "keyword":
        kw = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "générateur articles seo ia"
        asyncio.run(fast_keyword(kw))
    elif mode == "ideas":
        niche = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "SEO et monétisation"
        asyncio.run(fast_idea(niche))
    elif mode == "batch":
        kws = sys.argv[2:] if len(sys.argv) > 2 else [
            "outil seo ia gratuit",
            "contenu ia penalisation google",
            "affiliation seo 2025",
        ]
        asyncio.run(fast_batch(kws))
