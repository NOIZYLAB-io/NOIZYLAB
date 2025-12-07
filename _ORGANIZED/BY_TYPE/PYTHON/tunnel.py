"""
NoizyOS Ultra — Secure Tunnel
=============================
Secure session management for remote connections.
Zero-trust model with temporary access tokens.
"""

import secrets
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List

# Active sessions
SESSIONS: Dict[str, Dict[str, Any]] = {}

# Session configuration
SESSION_TTL = 3600  # 1 hour default
MAX_SESSIONS_PER_USER = 3


def create_session(
    email: str, 
    session_type: str = "remote",
    ttl: int = SESSION_TTL,
    metadata: Optional[Dict] = None
) -> Dict[str, Any]:
    """
    Create a new secure session.
    
    Args:
        email: User identifier
        session_type: Type of session (remote, technician, admin)
        ttl: Time-to-live in seconds
        metadata: Optional session metadata
    
    Returns:
        Session info including token
    """
    # Generate secure token
    token = secrets.token_hex(32)
    session_id = secrets.token_hex(8)
    
    now = datetime.now()
    expires = now + timedelta(seconds=ttl)
    
    session = {
        "id": session_id,
        "token": token,
        "email": email,
        "type": session_type,
        "created": now.isoformat(),
        "expires": expires.isoformat(),
        "ttl": ttl,
        "valid": True,
        "metadata": metadata or {},
        "last_activity": now.isoformat()
    }
    
    # Store by email (allow multiple sessions)
    if email not in SESSIONS:
        SESSIONS[email] = {}
    
    # Enforce max sessions per user
    if len(SESSIONS[email]) >= MAX_SESSIONS_PER_USER:
        # Remove oldest session
        oldest_id = min(
            SESSIONS[email].keys(),
            key=lambda k: SESSIONS[email][k]["created"]
        )
        del SESSIONS[email][oldest_id]
    
    SESSIONS[email][session_id] = session
    
    return {
        "session_id": session_id,
        "token": token,
        "expires": expires.isoformat(),
        "type": session_type
    }


def validate_session(email: str, token: str) -> Dict[str, Any]:
    """
    Validate a session token.
    
    Args:
        email: User identifier
        token: Session token
    
    Returns:
        Validation result with session info if valid
    """
    if email not in SESSIONS:
        return {"valid": False, "error": "No sessions for user"}
    
    now = datetime.now()
    
    for session_id, session in SESSIONS[email].items():
        if session["token"] != token:
            continue
        
        if not session["valid"]:
            return {"valid": False, "error": "Session revoked"}
        
        expires = datetime.fromisoformat(session["expires"])
        if now > expires:
            session["valid"] = False
            return {"valid": False, "error": "Session expired"}
        
        # Update last activity
        session["last_activity"] = now.isoformat()
        
        return {
            "valid": True,
            "session_id": session_id,
            "type": session["type"],
            "expires": session["expires"],
            "remaining_seconds": int((expires - now).total_seconds())
        }
    
    return {"valid": False, "error": "Invalid token"}


def revoke_session(email: str, session_id: Optional[str] = None) -> bool:
    """
    Revoke a session or all sessions for a user.
    
    Args:
        email: User identifier
        session_id: Specific session to revoke (None = revoke all)
    
    Returns:
        True if successful
    """
    if email not in SESSIONS:
        return False
    
    if session_id:
        if session_id in SESSIONS[email]:
            SESSIONS[email][session_id]["valid"] = False
            return True
        return False
    else:
        # Revoke all sessions
        for sid in SESSIONS[email]:
            SESSIONS[email][sid]["valid"] = False
        return True


def extend_session(email: str, session_id: str, additional_seconds: int = 1800) -> bool:
    """Extend a session's TTL."""
    if email not in SESSIONS or session_id not in SESSIONS[email]:
        return False
    
    session = SESSIONS[email][session_id]
    if not session["valid"]:
        return False
    
    current_expires = datetime.fromisoformat(session["expires"])
    new_expires = current_expires + timedelta(seconds=additional_seconds)
    session["expires"] = new_expires.isoformat()
    
    return True


def get_active_sessions(email: Optional[str] = None) -> List[Dict]:
    """
    Get active sessions.
    
    Args:
        email: Filter by user (None = all users)
    
    Returns:
        List of active session info (without tokens)
    """
    now = datetime.now()
    active = []
    
    users = [email] if email else SESSIONS.keys()
    
    for user in users:
        if user not in SESSIONS:
            continue
        
        for session_id, session in SESSIONS[user].items():
            if not session["valid"]:
                continue
            
            expires = datetime.fromisoformat(session["expires"])
            if now > expires:
                continue
            
            # Return session info without token
            active.append({
                "session_id": session_id,
                "email": session["email"],
                "type": session["type"],
                "created": session["created"],
                "expires": session["expires"],
                "last_activity": session["last_activity"]
            })
    
    return active


def cleanup_expired_sessions() -> int:
    """Remove expired sessions. Returns count of removed sessions."""
    now = datetime.now()
    removed = 0
    
    for email in list(SESSIONS.keys()):
        for session_id in list(SESSIONS[email].keys()):
            session = SESSIONS[email][session_id]
            expires = datetime.fromisoformat(session["expires"])
            
            if now > expires or not session["valid"]:
                del SESSIONS[email][session_id]
                removed += 1
        
        # Clean up empty user entries
        if not SESSIONS[email]:
            del SESSIONS[email]
    
    return removed


def get_session_stats() -> Dict[str, Any]:
    """Get session statistics."""
    total = sum(len(sessions) for sessions in SESSIONS.values())
    active = len(get_active_sessions())
    
    return {
        "total_sessions": total,
        "active_sessions": active,
        "unique_users": len(SESSIONS),
        "max_per_user": MAX_SESSIONS_PER_USER,
        "default_ttl": SESSION_TTL
    }

