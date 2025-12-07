"""NoizyBrain++ Multi-Agent Routing - 25 Geniuses"""
GENIUSES = ["Diagnostics", "Security", "Creative", "Technical", "Emotional", "Memory", "Vision", "Voice", "Home", "Compute", "Network", "Task", "Time", "Chat", "Flow", "Sync", "Drive", "ID", "Life", "Mind", "Synth", "Avatar", "Reality", "Grid", "Heart"]
ACTIVE = {}

def route_to_genius(query, context=None):
    q = query.lower()
    if "security" in q or "threat" in q: return "Security"
    if "emotion" in q or "stress" in q: return "Emotional"
    if "task" in q or "todo" in q: return "Task"
    if "schedule" in q or "time" in q: return "Time"
    if "home" in q or "room" in q: return "Home"
    if "compute" in q or "gpu" in q: return "Compute"
    if "memory" in q or "remember" in q: return "Memory"
    return "Technical"

def get_active_geniuses():
    return GENIUSES

def activate_genius(name):
    ACTIVE[name] = True

