"""FrontDesk: Call Router"""
from datetime import datetime

ACTIVE_CALLS = {}
CALL_LOG = []

def route_call(caller_id, intent=None):
    """Route call based on intent"""
    routes = {"booking": "schedule_bridge", "support": "diagnostics_precheck", "pricing": "intake_collector", "info": "voice_handler"}
    target = routes.get(intent, "voice_handler")
    ACTIVE_CALLS[caller_id] = {"intent": intent, "routed_to": target, "started": datetime.now().isoformat()}
    return {"caller_id": caller_id, "routed_to": target}

def end_call(caller_id, outcome="completed"):
    if caller_id in ACTIVE_CALLS:
        call = ACTIVE_CALLS.pop(caller_id)
        call["ended"] = datetime.now().isoformat()
        call["outcome"] = outcome
        CALL_LOG.append(call)
        return call
    return None

def get_active_calls():
    return list(ACTIVE_CALLS.values())

def get_call_stats():
    return {"total": len(CALL_LOG), "active": len(ACTIVE_CALLS)}

