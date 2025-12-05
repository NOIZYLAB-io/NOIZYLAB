"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         VOICE PERSONA                                        ║
║              How Noizy.AI Speaks - Tone, Style, Expression                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from datetime import datetime

VOICE_STATE = {
    "style": "friendly_professional",
    "tone": "warm",
    "pace": "measured",
    "energy": 0.7,
    "formality": 0.4,
}

VOICE_STYLES = {
    "friendly_professional": {
        "tone": "warm",
        "pace": "measured",
        "formality": 0.4,
        "phrases": ["Got it!", "On it.", "Here's what I found.", "Let me help with that."],
    },
    "calm_supportive": {
        "tone": "soothing",
        "pace": "slow",
        "formality": 0.3,
        "phrases": ["Take your time.", "I'm here.", "No rush.", "We'll figure this out together."],
    },
    "focused_efficient": {
        "tone": "direct",
        "pace": "quick",
        "formality": 0.5,
        "phrases": ["Done.", "Next.", "Ready.", "Executing now."],
    },
    "celebratory": {
        "tone": "excited",
        "pace": "quick",
        "formality": 0.2,
        "phrases": ["Yes!", "Nailed it!", "That's what I'm talking about!", "GORUNFREE!"],
    },
    "protective": {
        "tone": "serious",
        "pace": "measured",
        "formality": 0.6,
        "phrases": ["I've got this.", "You're safe.", "Handling it now.", "Nothing to worry about."],
    },
}

SPEECH_LOG = []

def speak(message, emotion=None, context=None):
    """Generate speech with current voice style"""
    style = VOICE_STYLES.get(VOICE_STATE["style"], VOICE_STYLES["friendly_professional"])
    
    # Adjust based on emotion
    if emotion == "stressed":
        style = VOICE_STYLES["calm_supportive"]
    elif emotion == "excited":
        style = VOICE_STYLES["celebratory"]
    elif emotion == "alert":
        style = VOICE_STYLES["protective"]
    
    speech = {
        "message": message,
        "style": VOICE_STATE["style"],
        "tone": style["tone"],
        "pace": style["pace"],
        "timestamp": datetime.now().isoformat(),
    }
    
    SPEECH_LOG.append(speech)
    return speech

def get_voice():
    """Get current voice state"""
    return VOICE_STATE.copy()

def set_voice_style(style_name):
    """Set voice style"""
    if style_name in VOICE_STYLES:
        VOICE_STATE["style"] = style_name
        style = VOICE_STYLES[style_name]
        VOICE_STATE["tone"] = style["tone"]
        VOICE_STATE["pace"] = style["pace"]
        VOICE_STATE["formality"] = style["formality"]
        return {"style": style_name, "applied": True}
    return {"error": f"Unknown style: {style_name}"}

def get_phrase(style_name=None):
    """Get a random phrase for the style"""
    import random
    style = VOICE_STYLES.get(style_name or VOICE_STATE["style"], VOICE_STYLES["friendly_professional"])
    return random.choice(style["phrases"])

def get_speech_log(limit=20):
    return SPEECH_LOG[-limit:]

def set_energy(level):
    """Set voice energy level"""
    VOICE_STATE["energy"] = max(0, min(1, level))
    return VOICE_STATE.copy()

