"""Decision Engine: Planner"""
from datetime import datetime

PLANS = []
DAILY_PLAN = None

def plan_day(context=None):
    """Plan the day's activities"""
    context = context or {}
    plan = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "priorities": [],
        "tasks": [],
        "created_at": datetime.now().isoformat(),
    }
    
    # Add priorities based on context
    if context.get("pending_clients"): plan["priorities"].append({"type": "clients", "count": context["pending_clients"]})
    if context.get("pending_repairs"): plan["priorities"].append({"type": "repairs", "count": context["pending_repairs"]})
    if context.get("system_issues"): plan["priorities"].append({"type": "system", "issues": context["system_issues"]})
    
    # Generate tasks
    plan["tasks"] = [
        {"task": "check_intake_queue", "priority": "high"},
        {"task": "process_pending_invoices", "priority": "medium"},
        {"task": "run_system_health_check", "priority": "low"},
        {"task": "backup_mirrormind", "priority": "low"},
    ]
    
    global DAILY_PLAN
    DAILY_PLAN = plan
    PLANS.append(plan)
    return plan

def plan_action(action_type, context=None):
    """Plan a specific action"""
    context = context or {}
    plan = {"action": action_type, "steps": [], "risks": [], "created_at": datetime.now().isoformat()}
    
    if action_type == "repair":
        plan["steps"] = ["diagnose", "backup_state", "execute_repair", "verify", "log"]
        plan["risks"] = ["data_loss", "system_instability"]
        plan["rollback"] = "restore_from_backup"
    
    PLANS.append(plan)
    return plan

def get_plan():
    return DAILY_PLAN

def get_plan_history():
    return PLANS[-20:]

