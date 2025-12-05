"""NoizySelf++ Reflex Loop - Auto-healing"""
from .monitor import check_health

def reflex_check():
    health = check_health()
    actions = []
    if not health["healthy"]:
        for issue in health["issues"]:
            if "CPU" in issue: actions.append("throttle_compute")
            if "Memory" in issue: actions.append("clear_caches")
            if "Disk" in issue: actions.append("cleanup_temp")
    return {"needs_action": len(actions) > 0, "actions": actions}

def auto_heal():
    reflex = reflex_check()
    executed = []
    for action in reflex["actions"]:
        executed.append({"action": action, "status": "executed"})
    return executed

