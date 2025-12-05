"""
NoizyID Passkey Authentication
==============================
WebAuthn-compatible passkey system for all platforms.
"""

import secrets
import hashlib
import hmac
from typing import Optional, Dict, Tuple
from datetime import datetime, timedelta


# Passkey storage
PASSKEY_CHALLENGES: Dict[str, Dict] = {}

# Challenge expiry
CHALLENGE_EXPIRY_SECONDS = 300


def generate_passkey() -> str:
    """
    Generate a secure passkey.
    """
    return secrets.token_hex(32)


def hash_passkey(passkey: str, salt: str = None) -> Tuple[str, str]:
    """
    Hash a passkey with salt.
    Returns (hash, salt).
    """
    if salt is None:
        salt = secrets.token_hex(16)
    
    # Use PBKDF2 for secure hashing
    key = hashlib.pbkdf2_hmac(
        'sha256',
        passkey.encode(),
        salt.encode(),
        100000  # iterations
    )
    
    return key.hex(), salt


def verify_passkey(stored_hash: str, stored_salt: str, provided: str) -> bool:
    """
    Verify a passkey against stored hash.
    """
    computed_hash, _ = hash_passkey(provided, stored_salt)
    return hmac.compare_digest(stored_hash, computed_hash)


def verify_passkey_simple(stored: str, provided: str) -> bool:
    """
    Simple passkey verification (for development).
    """
    return hmac.compare_digest(stored, provided)


def generate_challenge(identity_id: str) -> str:
    """
    Generate a WebAuthn-style challenge.
    """
    challenge = secrets.token_urlsafe(32)
    
    PASSKEY_CHALLENGES[identity_id] = {
        "challenge": challenge,
        "created": datetime.now().isoformat(),
        "expires": (datetime.now() + timedelta(seconds=CHALLENGE_EXPIRY_SECONDS)).isoformat(),
    }
    
    return challenge


def verify_challenge(identity_id: str, response: str) -> bool:
    """
    Verify a challenge response.
    """
    stored = PASSKEY_CHALLENGES.get(identity_id)
    if not stored:
        return False
    
    # Check expiry
    expires = datetime.fromisoformat(stored["expires"])
    if datetime.now() > expires:
        del PASSKEY_CHALLENGES[identity_id]
        return False
    
    # Verify (simplified - real WebAuthn would verify signature)
    valid = stored["challenge"] == response
    
    if valid:
        del PASSKEY_CHALLENGES[identity_id]
    
    return valid


def generate_recovery_codes(count: int = 10) -> list:
    """
    Generate recovery codes for account recovery.
    """
    return [secrets.token_hex(4).upper() for _ in range(count)]


def generate_api_key(identity_id: str, name: str = "default") -> Dict:
    """
    Generate an API key for programmatic access.
    """
    key = secrets.token_urlsafe(32)
    key_id = secrets.token_hex(8)
    
    return {
        "key_id": key_id,
        "key": key,
        "identity_id": identity_id,
        "name": name,
        "created": datetime.now().isoformat(),
        "prefix": key[:8],  # For identification
    }


def validate_passkey_strength(passkey: str) -> Dict:
    """
    Validate passkey strength.
    """
    issues = []
    score = 0
    
    if len(passkey) >= 32:
        score += 30
    elif len(passkey) >= 16:
        score += 20
    else:
        issues.append("Passkey too short")
    
    if any(c.isupper() for c in passkey):
        score += 15
    if any(c.islower() for c in passkey):
        score += 15
    if any(c.isdigit() for c in passkey):
        score += 20
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in passkey):
        score += 20
    
    return {
        "score": min(100, score),
        "strong": score >= 70,
        "issues": issues,
    }

