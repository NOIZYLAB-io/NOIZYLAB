"""Orchestra: State Router - Global State Management"""
from datetime import datetime

GLOBAL_STATE = {
    "stress": 0.1,
    "energy": 0.9,
    "mood": "neutral",
    "threat": 0.0,
    "compute_load": 0.2,
    "network_quality": "excellent",
    "active_session": None,
    "pending_tasks": 0,
    "pending_clients": 0,
    "system_health": "optimal",
}

STATE_HISTORY = []

def route_state(key, value):
    """Route a state update"""
    old_value = GLOBAL_STATE.get(key)
    GLOBAL_STATE[key] = value
    
    change = {"key": key, "old": old_value, "new": value, "timestamp": datetime.now().isoformat()}
    STATE_HISTORY.append(change)
    
    # Trigger reactions based on state changes
    _react_to_change(key, value, old_value)
    
    return {"updated": key, "value": value}

def _react_to_change(key, new_value, old_value):
    """React to state changes"""
    if key == "stress" and new_value > 0.7 and (old_value or 0) <= 0.7:
        # Stress just crossed threshold
        pass  # Trigger calm mode
    
    if key == "threat" and new_value > 0.5:
        # Threat detected
        pass  # Alert shield

def get_global_state():
    return GLOBAL_STATE.copy()

def get_state(key):
    return GLOBAL_STATE.get(key)

def batch_update(updates):
    """Batch update multiple state values"""
    for key, value in updates.items():
        route_state(key, value)
    return GLOBAL_STATE.copy()

def get_state_history(limit=50):
    return STATE_HISTORY[-limit:]

