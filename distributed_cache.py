import time
from typing import Any, Optional, Dict

CACHE_STORE = {}
CACHE_TTL = 3600  # 1 hour default


class DistributedCache:
    def __init__(self, namespace: str = "global"):
        self.namespace = namespace

    def _key(self, key: str) -> str:
        return f"{self.namespace}:{key}"

    def set(self, key: str, value: Any, ttl: int = CACHE_TTL) -> bool:
        full_key = self._key(key)
        CACHE_STORE[full_key] = {
            "value": value,
            "expires": time.time() + ttl,
            "created": time.time()
        }
        return True

    def get(self, key: str) -> Optional[Any]:
        full_key = self._key(key)
        if full_key not in CACHE_STORE:
            return None
        
        entry = CACHE_STORE[full_key]
        if time.time() > entry["expires"]:
            del CACHE_STORE[full_key]
            return None
        
        return entry["value"]

    def delete(self, key: str) -> bool:
        full_key = self._key(key)
        if full_key in CACHE_STORE:
            del CACHE_STORE[full_key]
            return True
        return False

    def flush_namespace(self) -> int:
        prefix = f"{self.namespace}:"
        keys_to_delete = [k for k in CACHE_STORE if k.startswith(prefix)]
        for k in keys_to_delete:
            del CACHE_STORE[k]
        return len(keys_to_delete)

    def stats(self) -> Dict:
        prefix = f"{self.namespace}:"
        ns_keys = [k for k in CACHE_STORE if k.startswith(prefix)]
        return {
            "namespace": self.namespace,
            "keys": len(ns_keys),
            "global_keys": len(CACHE_STORE)
        }


def get_cache(namespace: str = "global") -> DistributedCache:
    return DistributedCache(namespace)

