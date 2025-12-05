"""
NoizyOS Ultra — NoizySync API
=============================
REST endpoints for cross-device synchronization.
"""

from fastapi import APIRouter
from ..sync.noizysync_store import (
    sync_set, sync_get, sync_delete, sync_all,
    sync_user_state, get_user_state,
    set_device_presence, get_device_presence, get_online_devices,
    sync_flow_state, get_flow_state,
    sync_omen_stats, get_omen_stats,
    sync_emergency, is_emergency_active
)

router = APIRouter()


@router.post("/set")
def set_state(payload: dict):
    """Set a global sync key-value pair."""
    key = payload.get("key")
    value = payload.get("value")
    ttl = payload.get("ttl")
    
    if not key:
        return {"ok": False, "error": "Key required"}
    
    sync_set(key, value, ttl)
    return {"ok": True, "key": key}


@router.get("/get/{key}")
def get_state(key: str):
    """Get a global sync value."""
    value = sync_get(key)
    return {"key": key, "value": value}


@router.delete("/delete/{key}")
def delete_state(key: str):
    """Delete a sync key."""
    sync_delete(key)
    return {"ok": True}


@router.get("/all")
def get_all_state():
    """Get all sync state (admin/debug)."""
    return {"state": sync_all()}


@router.post("/user")
def sync_user(payload: dict):
    """Sync state for a specific user."""
    email = payload.get("email")
    state = payload.get("state", {})
    
    if not email:
        return {"ok": False, "error": "Email required"}
    
    sync_user_state(email, state)
    return {"ok": True}


@router.get("/user/{email}")
def get_user(email: str):
    """Get synced state for a user."""
    return {"email": email, "state": get_user_state(email)}


@router.post("/presence")
def update_presence(payload: dict):
    """Update device presence status."""
    device_id = payload.get("device_id")
    status = payload.get("status", "online")
    metadata = payload.get("metadata", {})
    
    if not device_id:
        return {"ok": False, "error": "Device ID required"}
    
    set_device_presence(device_id, status, metadata)
    return {"ok": True}


@router.get("/presence/{device_id}")
def get_presence(device_id: str):
    """Get presence status for a device."""
    return {"device_id": device_id, "presence": get_device_presence(device_id)}


@router.get("/devices/online")
def list_online_devices():
    """Get list of online devices."""
    return {"devices": get_online_devices()}


@router.post("/flow")
def set_flow(payload: dict):
    """Sync global flow state."""
    flow_state = payload.get("flow_state", "normal")
    source = payload.get("source", "unknown")
    
    sync_flow_state(flow_state, source)
    return {"ok": True, "flow_state": flow_state}


@router.get("/flow")
def get_flow():
    """Get current global flow state."""
    return {"flow_state": get_flow_state()}


@router.post("/omen")
def sync_omen(payload: dict):
    """Sync Omen stats globally."""
    stats = payload.get("stats", {})
    sync_omen_stats(stats)
    return {"ok": True}


@router.get("/omen")
def get_omen():
    """Get latest synced Omen stats."""
    return {"stats": get_omen_stats()}


@router.post("/emergency")
def set_emergency(payload: dict):
    """Activate/deactivate emergency mode globally."""
    active = payload.get("active", False)
    reason = payload.get("reason", "")
    source = payload.get("source", "unknown")
    
    sync_emergency(active, reason, source)
    return {"ok": True, "emergency": active}


@router.get("/emergency")
def check_emergency():
    """Check if emergency mode is active."""
    return {"active": is_emergency_active()}

