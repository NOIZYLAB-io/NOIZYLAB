"""NoizyHeart++ Warmth Engine"""
from .relationship import get_relationship
from .emotional import detect_user_emotion

def get_warmth_level(user_id="rob"):
    rel = get_relationship(user_id)
    return rel["trust"] * rel["familiarity"]

def comfort_response(user_emotion, user_id="rob"):
    warmth = get_warmth_level(user_id)
    if user_emotion == "stressed":
        return "Hey, I can tell things are heavy right now. Let's take it one step at a time. I'm here." if warmth > 0.7 else "I'm here to help. What do you need?"
    if user_emotion == "tired":
        return "You've been pushing hard. Maybe it's time for a break? I'll handle what I can." if warmth > 0.7 else "Consider taking a break."
    return "I'm here for you."

def get_presence_mode(energy, stress):
    if stress > 0.7: return "supportive"
    if energy < 0.3: return "gentle"
    if energy > 0.8: return "energetic"
    return "balanced"

