"""
NoizySync+ Follow-Me Mode
=========================
Your session follows you across all devices.
Walk from iPad to Mac - exact UI appears instantly.
"""

from typing import Dict, Optional, List
from .device_state import DEVICE_STATES, update_state
from .snapshots import SNAPSHOTS, save_snapshot
import time


# Follow mode settings
FOLLOW_MODE: Dict[str, Dict] = {}

# Active follows
ACTIVE_FOLLOWS: List[Dict] = []


def follow_me(source_device: str, target_device: str) -> Optional[Dict]:
    """
    Transfer session from source to target device.
    
    Transfers:
    - UI state
    - Scroll position
    - Active panels
    - Form data
    - Selection state
    - Everything
    """
    from_state = DEVICE_STATES.get(source_device)
    if not from_state:
        return None
    
    # Deep copy state to target
    transferred_state = {
        **from_state,
        "device_id": target_device,
        "transferred_from": source_device,
        "transfer_time": time.time(),
    }
    
    DEVICE_STATES[target_device] = transferred_state
    
    # Log the follow
    ACTIVE_FOLLOWS.append({
        "from": source_device,
        "to": target_device,
        "timestamp": time.time(),
        "state_keys": list(from_state.keys()),
    })
    
    return transferred_state


def enable_auto_follow(user_id: str, devices: List[str]) -> Dict:
    """
    Enable automatic follow mode for a user across devices.
    When user becomes active on one device, state syncs from last active.
    """
    FOLLOW_MODE[user_id] = {
        "enabled": True,
        "devices": devices,
        "last_active": None,
        "created": time.time(),
    }
    return FOLLOW_MODE[user_id]


def disable_auto_follow(user_id: str) -> bool:
    """
    Disable auto-follow for a user.
    """
    if user_id in FOLLOW_MODE:
        FOLLOW_MODE[user_id]["enabled"] = False
        return True
    return False


def process_device_activity(user_id: str, device_id: str) -> Optional[Dict]:
    """
    Process device becoming active - auto-follow if enabled.
    """
    follow_config = FOLLOW_MODE.get(user_id)
    if not follow_config or not follow_config.get("enabled"):
        return None
    
    if device_id not in follow_config.get("devices", []):
        return None
    
    last_active = follow_config.get("last_active")
    
    if last_active and last_active != device_id:
        # Transfer state from last active device
        result = follow_me(last_active, device_id)
        follow_config["last_active"] = device_id
        return result
    
    follow_config["last_active"] = device_id
    return None


def get_follow_history(limit: int = 20) -> List[Dict]:
    """
    Get recent follow transfers.
    """
    return ACTIVE_FOLLOWS[-limit:]


def teleport_state(state: Dict, target_device: str) -> Dict:
    """
    Teleport a specific state to a device.
    Used for VR → Desktop → Mobile transitions.
    """
    teleported = {
        **state,
        "device_id": target_device,
        "teleported": True,
        "teleport_time": time.time(),
    }
    
    DEVICE_STATES[target_device] = teleported
    save_snapshot(target_device, teleported)
    
    return teleported


def sync_all_devices(source_device: str, target_devices: List[str]) -> Dict:
    """
    Sync state from source to multiple targets simultaneously.
    """
    source_state = DEVICE_STATES.get(source_device)
    if not source_state:
        return {"success": False, "error": "Source device not found"}
    
    results = {}
    for target in target_devices:
        if target != source_device:
            results[target] = follow_me(source_device, target) is not None
    
    return {"success": True, "synced": results}

