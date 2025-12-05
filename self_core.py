"""NoizySelf++ Core - Internal State Tracking"""
import time
from threading import Lock

SELF_STATE = {
    "stress": 0.1,
    "energy": 0.9,
    "focus": 0.6,
    "overload": False,
    "latency": 0.02,
    "errors": 0,
    "heal_mode": False,
    "optimizing": False,
    "safe_mode": False,
    "last_heal": None,
    "last_optimize": None,
    "uptime_start": time.time(),
    "heartbeat_count": 0,
    "module_health": {},
    "emotional_state": "neutral",
    "user_stress_detected": 0.0,
}

_lock = Lock()

def get_self_state():
    """Get current self state"""
    with _lock:
        return SELF_STATE.copy()

def update_self_state(key, value):
    """Update a self state value"""
    with _lock:
        SELF_STATE[key] = value
        return SELF_STATE.copy()

def batch_update_self_state(updates: dict):
    """Batch update multiple state values"""
    with _lock:
        SELF_STATE.update(updates)
        return SELF_STATE.copy()

def increment_heartbeat():
    """Increment heartbeat counter"""
    with _lock:
        SELF_STATE["heartbeat_count"] += 1
        return SELF_STATE["heartbeat_count"]

def get_uptime():
    """Get system uptime in seconds"""
    return time.time() - SELF_STATE["uptime_start"]

def is_healthy():
    """Quick health check"""
    return (
        SELF_STATE["stress"] < 0.8 and
        SELF_STATE["energy"] > 0.2 and
        not SELF_STATE["overload"] and
        SELF_STATE["errors"] < 10
    )

def enter_safe_mode():
    """Enter safe mode"""
    with _lock:
        SELF_STATE["safe_mode"] = True
        SELF_STATE["overload"] = True
        return True

def exit_safe_mode():
    """Exit safe mode"""
    with _lock:
        SELF_STATE["safe_mode"] = False
        SELF_STATE["overload"] = False
        return True

def record_error():
    """Record an error occurrence"""
    with _lock:
        SELF_STATE["errors"] += 1
        return SELF_STATE["errors"]

def clear_errors():
    """Clear error count"""
    with _lock:
        SELF_STATE["errors"] = 0

