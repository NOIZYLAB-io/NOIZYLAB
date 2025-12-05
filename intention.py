"""NoizyBrain++ Intention Engine - AI decides helpful actions autonomously"""
INTENTION_QUEUE = []

def detect_intention(state, context):
    intentions = []
    if state.get("stress", 0) > 0.7:
        intentions.append({"action": "activate_calm_mode", "reason": "High stress detected"})
    if state.get("pending_tasks", 0) > 5:
        intentions.append({"action": "prioritize_tasks", "reason": "Task overload"})
    if state.get("energy", 1) < 0.3:
        intentions.append({"action": "suggest_break", "reason": "Low energy"})
    INTENTION_QUEUE.extend(intentions)
    return intentions

def execute_intention(intention):
    return {"executed": intention["action"], "result": "success"}

def get_pending_intentions():
    return INTENTION_QUEUE[-20:]

