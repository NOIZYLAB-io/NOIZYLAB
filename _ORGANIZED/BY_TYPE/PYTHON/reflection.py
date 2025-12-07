"""Decision Engine: Reflection - AI Self-Analysis"""
from datetime import datetime

REFLECTIONS = []

def reflect(action, outcome, context=None):
    """Reflect on an action and its outcome"""
    reflection = {
        "action": action,
        "outcome": outcome,
        "success": outcome.get("status") == "success",
        "timestamp": datetime.now().isoformat(),
        "learnings": [],
    }
    
    # Generate learnings
    if reflection["success"]:
        reflection["learnings"].append(f"Action '{action}' was successful - reinforce this approach")
    else:
        reflection["learnings"].append(f"Action '{action}' failed - consider alternatives")
        if outcome.get("error"):
            reflection["learnings"].append(f"Error: {outcome['error']} - add to known issues")
    
    # Analyze for improvements
    if context:
        if context.get("duration", 0) > 5:
            reflection["learnings"].append("Action took too long - optimize for speed")
        if context.get("resources_used", 0) > 0.8:
            reflection["learnings"].append("High resource usage - consider efficiency improvements")
    
    REFLECTIONS.append(reflection)
    return reflection

def get_reflections(limit=20):
    return REFLECTIONS[-limit:]

def get_success_rate():
    if not REFLECTIONS: return 1.0
    successes = len([r for r in REFLECTIONS if r["success"]])
    return round(successes / len(REFLECTIONS), 2)

def get_common_failures():
    failures = [r for r in REFLECTIONS if not r["success"]]
    return failures[-10:]

