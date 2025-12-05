"""
NoizyOS Ultra — NoizySync Store
===============================
In-memory key-value store for cross-device synchronization.
Stores UI state, mood, device stats, voice events, and more.

Production: Swap with Redis, Supabase, or any KV store.
"""

from datetime import datetime
from typing import Dict, Any, Optional, List

# Global sync state store
SYNC_STATE: Dict[str, Any] = {}

# User-specific state stores
USER_STATES: Dict[str, Dict[str, Any]] = {}

# Device presence tracking
DEVICE_PRESENCE: Dict[str, Dict[str, Any]] = {}


def sync_set(key: str, value: Any, ttl: Optional[int] = None) -> bool:
    """
    Set a global sync value.
    
    Args:
        key: State key
        value: State value
        ttl: Optional time-to-live in seconds (not enforced in memory mode)
    
    Returns:
        True if successful
    """
    SYNC_STATE[key] = {
        "value": value,
        "updated_at": datetime.now().isoformat(),
        "ttl": ttl
    }
    return True


def sync_get(key: str) -> Any:
    """
    Get a global sync value.
    
    Args:
        key: State key
    
    Returns:
        Value or None if not found
    """
    entry = SYNC_STATE.get(key)
    if entry:
        return entry.get("value")
    return None


def sync_delete(key: str) -> bool:
    """Delete a sync key."""
    if key in SYNC_STATE:
        del SYNC_STATE[key]
        return True
    return False


def sync_all() -> Dict[str, Any]:
    """Get all sync state (for debugging/admin)."""
    return {k: v.get("value") for k, v in SYNC_STATE.items()}


def sync_user_state(email: str, state: Dict[str, Any]) -> bool:
    """
    Sync state for a specific user.
    
    Args:
        email: User identifier
        state: State dict to merge
    
    Returns:
        True if successful
    """
    if email not in USER_STATES:
        USER_STATES[email] = {}
    
    USER_STATES[email].update(state)
    USER_STATES[email]["_updated_at"] = datetime.now().isoformat()
    
    return True


def get_user_state(email: str) -> Dict[str, Any]:
    """Get all synced state for a user."""
    return USER_STATES.get(email, {})


def set_device_presence(device_id: str, status: str, metadata: Optional[Dict] = None) -> bool:
    """
    Track device presence (online/offline/active).
    
    Args:
        device_id: Unique device identifier
        status: "online", "offline", "active", "idle"
        metadata: Optional device info
    """
    DEVICE_PRESENCE[device_id] = {
        "status": status,
        "last_seen": datetime.now().isoformat(),
        "metadata": metadata or {}
    }
    return True


def get_device_presence(device_id: str) -> Optional[Dict]:
    """Get presence status for a device."""
    return DEVICE_PRESENCE.get(device_id)


def get_online_devices() -> List[str]:
    """Get list of online device IDs."""
    return [
        device_id for device_id, info in DEVICE_PRESENCE.items()
        if info.get("status") in ["online", "active"]
    ]


def sync_flow_state(flow_state: str, source: str = "unknown") -> bool:
    """Sync the global flow state (calm/emergency/normal)."""
    return sync_set("global_flow_state", {
        "state": flow_state,
        "source": source,
        "timestamp": datetime.now().isoformat()
    })


def get_flow_state() -> str:
    """Get current global flow state."""
    state = sync_get("global_flow_state")
    if state:
        return state.get("state", "normal")
    return "normal"


def sync_omen_stats(stats: Dict[str, Any]) -> bool:
    """Sync HP Omen stats globally."""
    return sync_set("omen_stats", stats)


def get_omen_stats() -> Optional[Dict]:
    """Get latest synced Omen stats."""
    return sync_get("omen_stats")


def sync_emergency(active: bool, reason: str = "", source: str = "unknown") -> bool:
    """Sync emergency state across all devices."""
    return sync_set("emergency", {
        "active": active,
        "reason": reason,
        "source": source,
        "timestamp": datetime.now().isoformat()
    })


def is_emergency_active() -> bool:
    """Check if emergency mode is active."""
    state = sync_get("emergency")
    if state:
        return state.get("active", False)
    return False

