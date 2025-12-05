import secrets
import time
from typing import Dict

TOKEN_STORE = {}


class TokenExchange:
    """Cross-system token exchange"""

    def __init__(self):
        self.tokens = TOKEN_STORE

    def issue_token(self, identity_id: str, scope: str, ttl: int = 3600) -> Dict:
        """Issue a scoped access token"""
        token = secrets.token_hex(32)
        self.tokens[token] = {
            "identity_id": identity_id,
            "scope": scope,
            "issued": time.time(),
            "expires": time.time() + ttl
        }
        return {"token": token, "expires_in": ttl}

    def validate_token(self, token: str, required_scope: str = None) -> Dict:
        """Validate token and optionally check scope"""
        if token not in self.tokens:
            return {"valid": False, "error": "token_not_found"}

        token_data = self.tokens[token]
        if time.time() > token_data["expires"]:
            del self.tokens[token]
            return {"valid": False, "error": "token_expired"}

        if required_scope and token_data["scope"] != required_scope:
            return {"valid": False, "error": "scope_mismatch"}

        return {
            "valid": True,
            "identity_id": token_data["identity_id"],
            "scope": token_data["scope"]
        }

    def refresh_token(self, token: str, ttl: int = 3600) -> Dict:
        """Refresh token expiry"""
        if token not in self.tokens:
            return {"refreshed": False, "error": "token_not_found"}

        self.tokens[token]["expires"] = time.time() + ttl
        return {"refreshed": True, "expires_in": ttl}

    def revoke_token(self, token: str) -> Dict:
        if token in self.tokens:
            del self.tokens[token]
            return {"revoked": True}
        return {"revoked": False}


exchange = TokenExchange()

