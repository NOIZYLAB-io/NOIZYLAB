import hashlib
import time
import secrets
from typing import Dict, Optional

IDENTITY_STORE = {}
SESSION_STORE = {}


class AuthCore:
    """Core authentication system"""

    def __init__(self):
        self.identities = IDENTITY_STORE
        self.sessions = SESSION_STORE

    def register(self, identity_type: str, identity_id: str, credentials: Dict) -> Dict:
        """Register a new identity"""
        # identity_type: citizen, enterprise, government, ai
        hashed_secret = self._hash(credentials.get("secret", ""))

        self.identities[identity_id] = {
            "type": identity_type,
            "created": time.time(),
            "secret_hash": hashed_secret,
            "metadata": credentials.get("metadata", {}),
            "active": True
        }

        return {"registered": True, "identity_id": identity_id}

    def authenticate(self, identity_id: str, secret: str) -> Dict:
        """Authenticate and create session"""
        if identity_id not in self.identities:
            return {"authenticated": False, "error": "identity_not_found"}

        identity = self.identities[identity_id]
        if self._hash(secret) != identity["secret_hash"]:
            return {"authenticated": False, "error": "invalid_credentials"}

        # Create session
        session_token = secrets.token_hex(32)
        self.sessions[session_token] = {
            "identity_id": identity_id,
            "identity_type": identity["type"],
            "created": time.time(),
            "expires": time.time() + 86400  # 24 hours
        }

        return {
            "authenticated": True,
            "session_token": session_token,
            "expires_in": 86400
        }

    def validate_session(self, session_token: str) -> Dict:
        """Validate a session token"""
        if session_token not in self.sessions:
            return {"valid": False, "error": "session_not_found"}

        session = self.sessions[session_token]
        if time.time() > session["expires"]:
            del self.sessions[session_token]
            return {"valid": False, "error": "session_expired"}

        return {
            "valid": True,
            "identity_id": session["identity_id"],
            "identity_type": session["identity_type"]
        }

    def revoke_session(self, session_token: str) -> Dict:
        """Revoke a session"""
        if session_token in self.sessions:
            del self.sessions[session_token]
            return {"revoked": True}
        return {"revoked": False}

    def _hash(self, value: str) -> str:
        return hashlib.sha256(value.encode()).hexdigest()


auth = AuthCore()

