import json
import time
import hashlib
from typing import Dict, Any, Optional

SYNC_REGISTRY = {}


class SyncHub:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.last_sync = None
        self.sync_version = 0

    def push(self, data: Dict[str, Any]) -> Dict:
        """Push local state to cloud"""
        self.sync_version += 1
        payload = {
            "node_id": self.node_id,
            "version": self.sync_version,
            "timestamp": time.time(),
            "checksum": self._checksum(data),
            "data": data
        }
        SYNC_REGISTRY[self.node_id] = payload
        return {"status": "synced", "version": self.sync_version}

    def pull(self, target_node: Optional[str] = None) -> Dict:
        """Pull state from cloud"""
        if target_node:
            return SYNC_REGISTRY.get(target_node, {})
        return SYNC_REGISTRY

    def merge(self, remote_data: Dict) -> Dict:
        """Merge remote state with local"""
        local = SYNC_REGISTRY.get(self.node_id, {})
        merged = {**local.get("data", {}), **remote_data}
        return self.push(merged)

    def _checksum(self, data: Dict) -> str:
        return hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()


def create_hub(node_id: str) -> SyncHub:
    return SyncHub(node_id)

