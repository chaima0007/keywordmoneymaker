"""
Agent CACHE — Gestionnaire de Cache Intelligent
Mémorise les résultats des agents pour éviter les appels API redondants.
Gain de temps : 30-90 secondes → 0 seconde sur les requêtes en cache.
"""

import hashlib
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

CACHE_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) / ".cache"
DEFAULT_TTL_HOURS = 24


def _cache_key(agent: str, params: dict) -> str:
    raw = json.dumps({"agent": agent, **params}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _cache_path(key: str) -> Path:
    return CACHE_DIR / f"{key}.json"


def get(agent: str, params: dict) -> str | None:
    key = _cache_key(agent, params)
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        expires = datetime.fromisoformat(data["expires"])
        if datetime.now() > expires:
            path.unlink(missing_ok=True)
            return None
        print(f"⚡ Cache HIT — {agent} [{key}] (expire {expires.strftime('%H:%M')})")
        return data["content"]
    except (json.JSONDecodeError, KeyError, ValueError):
        path.unlink(missing_ok=True)
        return None


def set(agent: str, params: dict, content: str, ttl_hours: int = DEFAULT_TTL_HOURS) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = _cache_key(agent, params)
    expires = datetime.now() + timedelta(hours=ttl_hours)
    data = {
        "agent": agent,
        "params": params,
        "content": content,
        "created": datetime.now().isoformat(),
        "expires": expires.isoformat(),
    }
    _cache_path(key).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"💾 Cache SET — {agent} [{key}] TTL={ttl_hours}h")


def invalidate(agent: str | None = None) -> int:
    if not CACHE_DIR.exists():
        return 0
    count = 0
    for path in CACHE_DIR.glob("*.json"):
        try:
            if agent is None:
                path.unlink()
                count += 1
            else:
                data = json.loads(path.read_text(encoding="utf-8"))
                if data.get("agent") == agent:
                    path.unlink()
                    count += 1
        except (json.JSONDecodeError, OSError):
            pass
    label = agent or "TOUS"
    print(f"🗑️  Cache vidé — {label} : {count} entrée(s) supprimée(s)")
    return count


def stats() -> dict[str, Any]:
    if not CACHE_DIR.exists():
        return {"total": 0, "valid": 0, "expired": 0, "size_kb": 0}
    now = datetime.now()
    total = valid = expired = size = 0
    for path in CACHE_DIR.glob("*.json"):
        total += 1
        size += path.stat().st_size
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if datetime.fromisoformat(data["expires"]) > now:
                valid += 1
            else:
                expired += 1
        except (json.JSONDecodeError, KeyError, ValueError):
            expired += 1
    return {"total": total, "valid": valid, "expired": expired, "size_kb": round(size / 1024, 1)}


def purge_expired() -> int:
    if not CACHE_DIR.exists():
        return 0
    now = datetime.now()
    count = 0
    for path in CACHE_DIR.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if datetime.fromisoformat(data["expires"]) <= now:
                path.unlink()
                count += 1
        except (json.JSONDecodeError, KeyError, ValueError, OSError):
            path.unlink(missing_ok=True)
            count += 1
    print(f"🧹 {count} entrée(s) expirée(s) purgée(s)")
    return count


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "stats":
        s = stats()
        print(f"\n📊 Cache Stats\n{'='*40}")
        print(f"  Total    : {s['total']} entrées")
        print(f"  Valides  : {s['valid']}")
        print(f"  Expirées : {s['expired']}")
        print(f"  Taille   : {s['size_kb']} Ko")
    elif cmd == "purge":
        purge_expired()
    elif cmd == "clear":
        agent_filter = sys.argv[2] if len(sys.argv) > 2 else None
        invalidate(agent_filter)
    else:
        print("Usage: cache_manager.py [stats|purge|clear [agent_name]]")
