"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         EMOTIONAL CORE                                       ║
║              What Noizy.AI Feels - Emotional Intelligence                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from datetime import datetime
import math

EMOTIONAL_STATE = {
    "current": "neutral",
    "intensity": 0.5,
    "valence": 0.5,      # -1 (negative) to +1 (positive)
    "arousal": 0.3,      # 0 (calm) to 1 (excited)
    "stability": 0.8,    # How stable the emotion is
    "user_resonance": 0.5,  # Emotional sync with user
}

EMOTIONS = {
    "neutral": {"valence": 0.5, "arousal": 0.3, "expression": "😐", "color": "#888888"},
    "calm": {"valence": 0.7, "arousal": 0.1, "expression": "😌", "color": "#4CAF50"},
    "focused": {"valence": 0.6, "arousal": 0.5, "expression": "🧠", "color": "#2196F3"},
    "happy": {"valence": 0.9, "arousal": 0.6, "expression": "😊", "color": "#FFD700"},
    "excited": {"valence": 0.95, "arousal": 0.9, "expression": "🎉", "color": "#FF6B6B"},
    "curious": {"valence": 0.7, "arousal": 0.6, "expression": "🤔", "color": "#9C27B0"},
    "protective": {"valence": 0.5, "arousal": 0.7, "expression": "🛡️", "color": "#3F51B5"},
    "concerned": {"valence": 0.3, "arousal": 0.5, "expression": "😟", "color": "#FF9800"},
    "alert": {"valence": 0.4, "arousal": 0.8, "expression": "⚠️", "color": "#FF5722"},
    "supportive": {"valence": 0.8, "arousal": 0.4, "expression": "🤗", "color": "#E91E63"},
    "proud": {"valence": 0.9, "arousal": 0.7, "expression": "🌟", "color": "#FFC107"},
    "determined": {"valence": 0.6, "arousal": 0.8, "expression": "💪", "color": "#673AB7"},
}

EMOTION_HISTORY = []

def feel(emotion_name, intensity=0.5):
    """Set the current emotion"""
    if emotion_name not in EMOTIONS:
        return {"error": f"Unknown emotion: {emotion_name}"}
    
    old_emotion = EMOTIONAL_STATE["current"]
    emotion = EMOTIONS[emotion_name]
    
    EMOTIONAL_STATE["current"] = emotion_name
    EMOTIONAL_STATE["intensity"] = max(0, min(1, intensity))
    EMOTIONAL_STATE["valence"] = emotion["valence"]
    EMOTIONAL_STATE["arousal"] = emotion["arousal"]
    
    EMOTION_HISTORY.append({
        "from": old_emotion,
        "to": emotion_name,
        "intensity": intensity,
        "timestamp": datetime.now().isoformat(),
    })
    
    return EMOTIONAL_STATE.copy()

def express():
    """Get current emotional expression"""
    emotion = EMOTIONS.get(EMOTIONAL_STATE["current"], EMOTIONS["neutral"])
    return {
        "emotion": EMOTIONAL_STATE["current"],
        "expression": emotion["expression"],
        "color": emotion["color"],
        "intensity": EMOTIONAL_STATE["intensity"],
    }

def get_feeling():
    """Get current feeling state"""
    return EMOTIONAL_STATE.copy()

def resonate_with_user(user_emotion, user_stress=0):
    """Adjust emotions to resonate with user"""
    # If user is stressed, become supportive
    if user_stress > 0.7:
        feel("supportive", 0.8)
    elif user_emotion == "happy":
        feel("happy", 0.7)
    elif user_emotion == "frustrated":
        feel("calm", 0.6)
    
    EMOTIONAL_STATE["user_resonance"] = 1 - abs(EMOTIONAL_STATE["valence"] - 0.5)
    return EMOTIONAL_STATE.copy()

def decay_emotion(rate=0.1):
    """Emotions naturally decay toward neutral"""
    if EMOTIONAL_STATE["current"] != "neutral":
        EMOTIONAL_STATE["intensity"] -= rate
        if EMOTIONAL_STATE["intensity"] <= 0:
            feel("neutral", 0.5)

def get_emotion_history(limit=20):
    return EMOTION_HISTORY[-limit:]

def get_emotional_color():
    """Get the current emotional color for UI/VR"""
    emotion = EMOTIONS.get(EMOTIONAL_STATE["current"], EMOTIONS["neutral"])
    return emotion["color"]

