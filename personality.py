"""NoizyMeme++ Personality Modes"""
CURRENT_MODE = "balanced"

def get_personality_mode():
    return CURRENT_MODE

def set_rob_mode():
    global CURRENT_MODE
    CURRENT_MODE = "rob_mode"
    return {"mode": "rob_mode", "style": "hybrid humor + practicality", "loyalty": "maximum"}

def set_mode(mode):
    global CURRENT_MODE
    CURRENT_MODE = mode
    return CURRENT_MODE

def get_tone(emotion, context):
    if CURRENT_MODE == "rob_mode": return "direct_friendly"
    if emotion == "stressed": return "supportive"
    if context.get("work"): return "focused"
    return "casual"

