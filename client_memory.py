"""
NoizyMemory GEN-1 — Layer 1: Client Memory
==========================================
Stores client profile data: name, email, preferences, accessibility settings.
Enables personalized AI interactions.
"""

from datetime import datetime
from typing import Dict, Any, Optional

# In-memory store (replace with database in production)
CLIENT_MEMORY: Dict[str, Dict[str, Any]] = {}


def remember_client(email: str, key: str, value: Any) -> bool:
    """
    Store a specific piece of information about a client.
    
    Args:
        email: Client identifier
        key: Data key (e.g., "name", "preferred_mode", "accessibility")
        value: Data value
    
    Returns:
        True if successful
    """
    if email not in CLIENT_MEMORY:
        CLIENT_MEMORY[email] = {
            "created_at": datetime.now().isoformat(),
            "last_seen": datetime.now().isoformat(),
            "session_count": 0
        }
    
    CLIENT_MEMORY[email][key] = value
    CLIENT_MEMORY[email]["last_updated"] = datetime.now().isoformat()
    
    return True


def recall_client(email: str) -> Dict[str, Any]:
    """
    Retrieve all stored information about a client.
    
    Args:
        email: Client identifier
    
    Returns:
        Dict of all client data, or empty dict if not found
    """
    if email in CLIENT_MEMORY:
        # Update last seen
        CLIENT_MEMORY[email]["last_seen"] = datetime.now().isoformat()
        CLIENT_MEMORY[email]["session_count"] = CLIENT_MEMORY[email].get("session_count", 0) + 1
    
    return CLIENT_MEMORY.get(email, {})


def update_client(email: str, data: Dict[str, Any]) -> bool:
    """
    Update multiple client fields at once.
    
    Args:
        email: Client identifier
        data: Dict of key-value pairs to update
    
    Returns:
        True if successful
    """
    for key, value in data.items():
        remember_client(email, key, value)
    return True


def get_client_preference(email: str, key: str, default: Any = None) -> Any:
    """Get a specific client preference."""
    client = recall_client(email)
    return client.get(key, default)


def set_accessibility_mode(email: str, mode: str) -> bool:
    """Set client's preferred accessibility mode."""
    return remember_client(email, "accessibility_mode", mode)


def get_accessibility_mode(email: str) -> Optional[str]:
    """Get client's accessibility mode preference."""
    return get_client_preference(email, "accessibility_mode")


def is_returning_client(email: str) -> bool:
    """Check if this is a returning client."""
    client = CLIENT_MEMORY.get(email, {})
    return client.get("session_count", 0) > 1


def get_client_tenure(email: str) -> Optional[str]:
    """Get how long client has been with NoizyLab."""
    client = CLIENT_MEMORY.get(email, {})
    created = client.get("created_at")
    if created:
        return created
    return None

