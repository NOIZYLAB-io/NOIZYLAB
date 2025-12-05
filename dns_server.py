"""
NoizyNet AI DNS Server
======================
Local resolver with smart caching, overrides, and mesh integration.
Replaces router DNS with intelligent local resolution.
"""

from typing import Dict, Optional, List
from datetime import datetime, timedelta
import socket


# DNS Overrides (local hostname → IP mapping)
DNS_OVERRIDES: Dict[str, str] = {
    # Core devices
    "noizy.local": "192.168.1.100",      # GABRIEL / M2 Ultra
    "gabriel.local": "192.168.1.100",
    "omen.local": "192.168.1.101",       # HP Omen
    "mc96.local": "192.168.1.1",         # Switch
    
    # Services
    "api.noizy.local": "192.168.1.100",
    "portal.noizy.local": "192.168.1.100",
    "verse.noizy.local": "192.168.1.100",
    
    # NoizyLab domains
    "noizylab.local": "192.168.1.100",
}

# DNS Cache
DNS_CACHE: Dict[str, Dict] = {}

# Blocked domains (malicious/unwanted)
BLOCKED_DOMAINS: List[str] = [
    "malware.com",
    "tracking.example.com",
    "ads.doubleclick.net",
]

# Cache TTL in seconds
DEFAULT_TTL = 300


def resolve(name: str, context: Dict = None) -> Optional[str]:
    """
    Resolve a domain name to IP address.
    Uses overrides → cache → upstream.
    """
    name_lower = name.lower().rstrip(".")
    
    # Check if blocked
    if is_blocked(name_lower):
        return "0.0.0.0"  # Sinkhole
    
    # Check overrides first
    if name_lower in DNS_OVERRIDES:
        return DNS_OVERRIDES[name_lower]
    
    # Check cache
    cached = get_cached(name_lower)
    if cached:
        return cached
    
    # Upstream resolution
    ip = upstream_resolve(name_lower)
    if ip:
        cache_result(name_lower, ip)
    
    return ip


def upstream_resolve(name: str) -> Optional[str]:
    """
    Resolve using upstream DNS servers.
    """
    try:
        result = socket.gethostbyname(name)
        return result
    except socket.gaierror:
        return None


def get_cached(name: str) -> Optional[str]:
    """
    Get cached DNS result if still valid.
    """
    if name in DNS_CACHE:
        entry = DNS_CACHE[name]
        if datetime.now() < entry["expires"]:
            entry["hits"] += 1
            return entry["ip"]
        else:
            del DNS_CACHE[name]
    return None


def cache_result(name: str, ip: str, ttl: int = DEFAULT_TTL) -> None:
    """
    Cache a DNS result.
    """
    DNS_CACHE[name] = {
        "ip": ip,
        "expires": datetime.now() + timedelta(seconds=ttl),
        "cached_at": datetime.now().isoformat(),
        "hits": 0,
    }


def add_override(name: str, ip: str) -> None:
    """
    Add a DNS override.
    """
    DNS_OVERRIDES[name.lower()] = ip


def remove_override(name: str) -> bool:
    """
    Remove a DNS override.
    """
    name_lower = name.lower()
    if name_lower in DNS_OVERRIDES:
        del DNS_OVERRIDES[name_lower]
        return True
    return False


def is_blocked(name: str) -> bool:
    """
    Check if domain is blocked.
    """
    for blocked in BLOCKED_DOMAINS:
        if blocked in name or name.endswith(blocked):
            return True
    return False


def block_domain(name: str) -> None:
    """
    Add domain to blocklist.
    """
    if name not in BLOCKED_DOMAINS:
        BLOCKED_DOMAINS.append(name.lower())


def unblock_domain(name: str) -> bool:
    """
    Remove domain from blocklist.
    """
    try:
        BLOCKED_DOMAINS.remove(name.lower())
        return True
    except ValueError:
        return False


def get_cache_stats() -> Dict:
    """
    Get DNS cache statistics.
    """
    now = datetime.now()
    valid = sum(1 for e in DNS_CACHE.values() if now < e["expires"])
    total_hits = sum(e["hits"] for e in DNS_CACHE.values())
    
    return {
        "total_entries": len(DNS_CACHE),
        "valid_entries": valid,
        "expired_entries": len(DNS_CACHE) - valid,
        "total_hits": total_hits,
        "overrides_count": len(DNS_OVERRIDES),
        "blocked_count": len(BLOCKED_DOMAINS),
    }


def clear_cache() -> int:
    """
    Clear DNS cache.
    """
    count = len(DNS_CACHE)
    DNS_CACHE.clear()
    return count


def get_all_overrides() -> Dict[str, str]:
    """
    Get all DNS overrides.
    """
    return DNS_OVERRIDES.copy()


def resolve_mesh_device(role: str) -> Optional[str]:
    """
    Resolve device by mesh role.
    """
    role_map = {
        "primary": "gabriel.local",
        "work": "omen.local",
        "network": "mc96.local",
    }
    
    hostname = role_map.get(role)
    if hostname:
        return resolve(hostname)
    return None

