"""
NoizySync+ Device State Manager
===============================
Extended heartbeat with full context for sync.
Tracks everything needed for seamless device switching.
"""

import time
from typing import Dict, List, Optional
from datetime import datetime


# Device states storage
DEVICE_STATES: Dict[str, Dict] = {}

# State change history
STATE_CHANGES: List[Dict] = []


def update_state(device_id: str, state: Dict) -> Dict:
    """
    Update device state with full context.
    
    State includes:
    - active_app: current application
    - active_window: current window/panel
    - scroll_position: {x, y} scroll offsets
    - timeline_position: media/timeline position
    - focus_context: what's being worked on
    - action_history: recent actions list
    - cursor_position: {x, y} cursor
    - selected_items: currently selected items
    - form_data: any form inputs
    - modal_state: open modals/dialogs
    """
    # Merge with existing state
    existing = DEVICE_STATES.get(device_id, {})
    
    updated = {
        **existing,
        **state,
        "device_id": device_id,
        "last_update": time.time(),
        "last_update_iso": datetime.now().isoformat(),
    }
    
    DEVICE_STATES[device_id] = updated
    
    # Log state change
    STATE_CHANGES.append({
        "device_id": device_id,
        "timestamp": time.time(),
        "changes": list(state.keys()),
    })
    
    # Trim history
    if len(STATE_CHANGES) > 1000:
        STATE_CHANGES[:] = STATE_CHANGES[-500:]
    
    return updated


def get_state(device_id: str) -> Dict:
    """
    Get current state for a device.
    """
    return DEVICE_STATES.get(device_id, {})


def get_all_states() -> Dict[str, Dict]:
    """
    Get states for all devices.
    """
    return DEVICE_STATES


def is_device_active(device_id: str, timeout: int = 30) -> bool:
    """
    Check if device is actively syncing.
    """
    state = DEVICE_STATES.get(device_id)
    if not state:
        return False
    return time.time() - state.get("last_update", 0) < timeout


def get_active_devices() -> List[Dict]:
    """
    Get all active devices with their states.
    """
    now = time.time()
    active = []
    for device_id, state in DEVICE_STATES.items():
        if now - state.get("last_update", 0) < 30:
            active.append({
                "device_id": device_id,
                "active_app": state.get("active_app"),
                "active_window": state.get("active_window"),
                "last_update": state.get("last_update"),
            })
    return active


def get_device_focus(device_id: str) -> Optional[str]:
    """
    Get what the device is currently focused on.
    """
    state = DEVICE_STATES.get(device_id, {})
    return state.get("focus_context")


def sync_form_data(from_device: str, to_device: str) -> bool:
    """
    Sync form data between devices.
    """
    from_state = DEVICE_STATES.get(from_device, {})
    form_data = from_state.get("form_data", {})
    
    if to_device not in DEVICE_STATES:
        DEVICE_STATES[to_device] = {}
    
    DEVICE_STATES[to_device]["form_data"] = form_data
    return True


def get_recent_changes(device_id: str, limit: int = 20) -> List[Dict]:
    """
    Get recent state changes for a device.
    """
    return [
        c for c in STATE_CHANGES[-limit * 2:]
        if c["device_id"] == device_id
    ][-limit:]

