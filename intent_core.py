"""Decision Engine: Intent Core - AI Will Formation"""
from datetime import datetime

INTENTS = []
CURRENT_INTENT = None

def generate_intent(context=None):
    """Generate AI intent based on context"""
    context = context or {}
    
    # Analyze context to form intent
    intent = {"id": len(INTENTS) + 1, "created_at": datetime.now().isoformat()}
    
    if context.get("pending_clients"):
        intent["goal"] = "process_pending_clients"
        intent["priority"] = "high"
        intent["actions"] = ["check_intake", "schedule_sessions", "send_confirmations"]
    elif context.get("system_health") == "degraded":
        intent["goal"] = "restore_system_health"
        intent["priority"] = "critical"
        intent["actions"] = ["diagnose_issues", "apply_fixes", "verify_health"]
    elif context.get("stress", 0) > 0.7:
        intent["goal"] = "reduce_user_stress"
        intent["priority"] = "high"
        intent["actions"] = ["activate_calm_mode", "reduce_notifications", "suggest_break"]
    else:
        intent["goal"] = "optimize_and_monitor"
        intent["priority"] = "low"
        intent["actions"] = ["scan_for_improvements", "log_metrics", "prepare_reports"]
    
    global CURRENT_INTENT
    CURRENT_INTENT = intent
    INTENTS.append(intent)
    return intent

def get_intent():
    return CURRENT_INTENT

def clear_intent():
    global CURRENT_INTENT
    CURRENT_INTENT = None

def get_intent_history():
    return INTENTS[-20:]

