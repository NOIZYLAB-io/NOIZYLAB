"""NoizyBrain++ Thinkers - Agents that act on intentions"""

def execute_intention(intent):
    """Convert intention to executable action"""
    plan = intent.get("plan", "")
    reflection = intent.get("reflection", "")
    
    # Client workflows
    if "client" in plan:
        return {"action": "flow/start_client_pipeline", "module": "noizyflow", "priority": "high"}
    
    # Compute optimization
    if "optimize_compute_distribution" in plan:
        if "urgent" in reflection:
            return {"action": "compute/emergency_rebalance", "module": "noizygrid", "priority": "critical"}
        return {"action": "compute/rebalance", "module": "noizygrid", "priority": "medium"}
    
    # Calm/stress management
    if "prepare_calm_flow" in plan:
        if "immediate" in reflection:
            return {"action": "home/emergency_calm", "module": "noizyhome", "priority": "critical"}
        return {"action": "home/set_calm_mode", "module": "noizyhome", "priority": "high"}
    
    # Threat response
    if "emergency_threat" in plan:
        return {"action": "shield/lockdown", "module": "noizyshield", "priority": "critical"}
    
    # Session support
    if "support_active_session" in plan:
        return {"action": "session/monitor", "module": "noizysync", "priority": "high"}
    
    # Default scan
    return {"action": "core/scan", "module": "noizycore", "priority": "low"}

def get_action_endpoint(action):
    """Convert action to API endpoint"""
    parts = action["action"].split("/")
    if len(parts) == 2:
        return f"http://localhost:8080/{parts[0]}/{parts[1]}"
    return f"http://localhost:8080/{action['action']}"

def validate_action(action):
    """Validate action before execution"""
    required = ["action", "module"]
    return all(k in action for k in required)

