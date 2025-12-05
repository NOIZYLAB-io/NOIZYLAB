"""Orchestra: Avatar Sync - Synchronize Avatar State"""
from datetime import datetime

AVATAR_STATE = {
    "emotion": "neutral",
    "expression": "default",
    "speaking": False,
    "gesture": None,
    "gaze_target": None,
    "position": {"x": 0, "y": 0, "z": -1},
    "visible": True,
    "personality": "friendly",
}

AVATAR_LOG = []

def sync_avatar(updates=None):
    """Sync avatar state"""
    if updates:
        AVATAR_STATE.update(updates)
    
    # Sync emotion from orchestra
    from .emotion_map import get_emotion
    emotion = get_emotion()
    AVATAR_STATE["emotion"] = emotion["current"]
    
    AVATAR_LOG.append({"state": AVATAR_STATE.copy(), "timestamp": datetime.now().isoformat()})
    return AVATAR_STATE.copy()

def get_avatar_state():
    return AVATAR_STATE.copy()

def set_speaking(is_speaking):
    AVATAR_STATE["speaking"] = is_speaking
    return sync_avatar()

def set_gesture(gesture_name):
    AVATAR_STATE["gesture"] = gesture_name
    return sync_avatar()

def set_gaze(target):
    AVATAR_STATE["gaze_target"] = target
    return sync_avatar()

def set_expression(expression):
    AVATAR_STATE["expression"] = expression
    return sync_avatar()

def set_personality(personality):
    AVATAR_STATE["personality"] = personality
    return sync_avatar()

def hide_avatar():
    AVATAR_STATE["visible"] = False
    return sync_avatar()

def show_avatar():
    AVATAR_STATE["visible"] = True
    return sync_avatar()

def get_avatar_log(limit=20):
    return AVATAR_LOG[-limit:]

