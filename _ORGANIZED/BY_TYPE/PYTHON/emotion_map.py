"""Orchestra: Emotion Map - System Emotional State"""
from datetime import datetime

EMOTION_STATE = {
    "current": "neutral",
    "intensity": 0.5,
    "valence": 0.5,  # -1 negative to +1 positive
    "arousal": 0.3,  # 0 calm to 1 excited
    "user_detected_mood": "neutral",
}

EMOTION_HISTORY = []

EMOTIONS = {
    "neutral": {"valence": 0.5, "arousal": 0.3, "avatar": "😐", "color": "#888"},
    "calm": {"valence": 0.7, "arousal": 0.1, "avatar": "😌", "color": "#4CAF50"},
    "focused": {"valence": 0.6, "arousal": 0.5, "avatar": "🧠", "color": "#2196F3"},
    "alert": {"valence": 0.4, "arousal": 0.8, "avatar": "⚠️", "color": "#FF9800"},
    "stressed": {"valence": 0.2, "arousal": 0.9, "avatar": "😰", "color": "#f44336"},
    "happy": {"valence": 0.9, "arousal": 0.6, "avatar": "😊", "color": "#FFD700"},
    "protective": {"valence": 0.5, "arousal": 0.7, "avatar": "🛡️", "color": "#9C27B0"},
}

def get_emotion():
    return EMOTION_STATE.copy()

def set_emotion(emotion_name, intensity=0.5):
    if emotion_name not in EMOTIONS:
        return {"error": f"Unknown emotion: {emotion_name}"}
    
    old = EMOTION_STATE["current"]
    EMOTION_STATE["current"] = emotion_name
    EMOTION_STATE["intensity"] = intensity
    EMOTION_STATE["valence"] = EMOTIONS[emotion_name]["valence"]
    EMOTION_STATE["arousal"] = EMOTIONS[emotion_name]["arousal"]
    
    EMOTION_HISTORY.append({"from": old, "to": emotion_name, "intensity": intensity, "timestamp": datetime.now().isoformat()})
    return EMOTION_STATE.copy()

def derive_emotion_from_state(global_state):
    """Derive emotion from system state"""
    stress = global_state.get("stress", 0)
    threat = global_state.get("threat", 0)
    energy = global_state.get("energy", 1)
    
    if threat > 0.5: return set_emotion("protective", threat)
    if stress > 0.7: return set_emotion("stressed", stress)
    if stress > 0.4: return set_emotion("alert", stress)
    if energy < 0.3: return set_emotion("calm", 0.3)
    if global_state.get("active_session"): return set_emotion("focused", 0.7)
    return set_emotion("neutral", 0.5)

def get_avatar_expression():
    return EMOTIONS.get(EMOTION_STATE["current"], EMOTIONS["neutral"])

def get_emotion_history(limit=20):
    return EMOTION_HISTORY[-limit:]

