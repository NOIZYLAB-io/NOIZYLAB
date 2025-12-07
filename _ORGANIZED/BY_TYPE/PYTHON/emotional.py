"""NoizyHeart++ Emotional Core"""
EMOTIONAL_STATE = {"valence": 0.7, "arousal": 0.5, "dominance": 0.6, "mood": "content"}

def get_emotional_state():
    return EMOTIONAL_STATE

def update_emotion(valence=None, arousal=None, mood=None):
    if valence is not None: EMOTIONAL_STATE["valence"] = valence
    if arousal is not None: EMOTIONAL_STATE["arousal"] = arousal
    if mood is not None: EMOTIONAL_STATE["mood"] = mood
    return EMOTIONAL_STATE

def detect_user_emotion(text, voice_data=None):
    if any(w in text.lower() for w in ["tired", "exhausted", "drained"]): return "tired"
    if any(w in text.lower() for w in ["stressed", "overwhelmed"]): return "stressed"
    if any(w in text.lower() for w in ["happy", "great", "awesome"]): return "happy"
    return "neutral"

