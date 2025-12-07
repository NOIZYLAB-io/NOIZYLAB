"""Decision Engine: Action Core - Execute Actions"""
from datetime import datetime
from .mode_manager import can_auto_execute, get_mode

ACTION_QUEUE = []
ACTION_LOG = []

def execute(action, context=None):
    """Execute an action (with mode-based permission check)"""
    context = context or {}
    
    # Check if action can be auto-executed
    permission = can_auto_execute(action.get("type", "general"))
    
    if not permission["allowed"]:
        # Queue for approval
        return queue_action(action, permission["reason"])
    
    # Execute the action
    result = _do_execute(action, context)
    
    # Log the action
    log_entry = {"action": action, "result": result, "mode": get_mode()["current"], 
                 "timestamp": datetime.now().isoformat()}
    ACTION_LOG.append(log_entry)
    
    return result

def _do_execute(action, context):
    """Actually execute the action"""
    action_type = action.get("type", "unknown")
    
    # Route to appropriate handler
    handlers = {
        "intake": lambda a, c: {"status": "success", "message": "Client intake processed"},
        "schedule": lambda a, c: {"status": "success", "message": "Appointment scheduled"},
        "invoice": lambda a, c: {"status": "success", "message": "Invoice generated"},
        "repair": lambda a, c: {"status": "success", "message": "Repair executed"},
        "diagnostic": lambda a, c: {"status": "success", "message": "Diagnostic complete"},
        "notification": lambda a, c: {"status": "success", "message": "Notification sent"},
    }
    
    handler = handlers.get(action_type, lambda a, c: {"status": "success", "message": f"Action {action_type} executed"})
    return handler(action, context)

def queue_action(action, reason):
    """Queue action for approval"""
    queued = {"action": action, "reason": reason, "queued_at": datetime.now().isoformat(), "status": "pending_approval"}
    ACTION_QUEUE.append(queued)
    return {"status": "queued", "reason": reason, "queue_position": len(ACTION_QUEUE)}

def approve_action(index):
    """Approve a queued action"""
    if 0 <= index < len(ACTION_QUEUE):
        action = ACTION_QUEUE.pop(index)
        action["status"] = "approved"
        return execute(action["action"])
    return {"error": "Invalid queue index"}

def reject_action(index, reason=None):
    """Reject a queued action"""
    if 0 <= index < len(ACTION_QUEUE):
        action = ACTION_QUEUE.pop(index)
        action["status"] = "rejected"
        action["reject_reason"] = reason
        ACTION_LOG.append(action)
        return {"status": "rejected", "action": action}
    return {"error": "Invalid queue index"}

def get_queue():
    return ACTION_QUEUE

def get_action_log(limit=50):
    return ACTION_LOG[-limit:]

