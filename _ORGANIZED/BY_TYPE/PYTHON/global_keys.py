import secrets
import time
from typing import Dict, List

KEY_REGISTRY = {}


class GlobalKeyManager:
    """Manage global API keys and service credentials"""

    def __init__(self):
        self.keys = KEY_REGISTRY

    def generate_api_key(self, owner_id: str, permissions: List[str]) -> Dict:
        """Generate a new API key"""
        key = f"nz_{secrets.token_hex(24)}"
        self.keys[key] = {
            "owner_id": owner_id,
            "permissions": permissions,
            "created": time.time(),
            "last_used": None,
            "active": True
        }
        return {"api_key": key, "permissions": permissions}

    def validate_key(self, api_key: str) -> Dict:
        """Validate an API key"""
        if api_key not in self.keys:
            return {"valid": False, "error": "key_not_found"}

        key_data = self.keys[api_key]
        if not key_data["active"]:
            return {"valid": False, "error": "key_deactivated"}

        key_data["last_used"] = time.time()
        return {
            "valid": True,
            "owner_id": key_data["owner_id"],
            "permissions": key_data["permissions"]
        }

    def check_permission(self, api_key: str, required_permission: str) -> bool:
        """Check if key has specific permission"""
        if api_key not in self.keys:
            return False
        return required_permission in self.keys[api_key]["permissions"]

    def revoke_key(self, api_key: str) -> Dict:
        """Revoke an API key"""
        if api_key in self.keys:
            self.keys[api_key]["active"] = False
            return {"revoked": True}
        return {"revoked": False}

    def list_keys(self, owner_id: str) -> List[Dict]:
        """List all keys for an owner"""
        return [
            {"key": k[:12] + "...", **v}
            for k, v in self.keys.items()
            if v["owner_id"] == owner_id
        ]


keys = GlobalKeyManager()

