"""NoizyBrain++ Reflection Engine - AI thinks about its own thoughts"""

def reflect(context, last_plan):
    """Self-reflection on current plan and context"""
    state = context.get("state", {})
    
    # Plan-specific reflections
    if last_plan == "prepare_client_workflow":
        return "ensure_client_tools_ready"
    
    if last_plan == "optimize_compute_distribution":
        if state.get("compute", 0) > 0.9:
            return "urgent_rebalance_required"
        return "reroute_tasks_if_required"
    
    if last_plan == "prepare_calm_flow":
        if state.get("stress", 0) > 0.9:
            return "immediate_intervention_needed"
        return "gradual_stress_reduction"
    
    if last_plan == "emergency_threat_response":
        return "verify_threat_contained"
    
    if last_plan == "support_active_session":
        return "monitor_session_health"
    
    if last_plan == "idle_scan_for_opportunities":
        return "evaluate_system_health"
    
    return "continue_monitoring"

def evaluate_reflection(reflection, context):
    """Evaluate if reflection leads to action"""
    urgent = ["urgent_rebalance_required", "immediate_intervention_needed", "verify_threat_contained"]
    if reflection in urgent:
        return {"urgent": True, "action_required": True}
    return {"urgent": False, "action_required": reflection != "continue_monitoring"}

def meta_reflect(plan, reflection, outcome):
    """Meta-reflection: learn from outcomes"""
    return {
        "plan": plan,
        "reflection": reflection,
        "outcome": outcome,
        "learning": f"Plan '{plan}' with reflection '{reflection}' resulted in '{outcome}'"
    }

