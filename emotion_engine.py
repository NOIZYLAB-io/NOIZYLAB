"""
NoizyOS Ultra — GEN-4 Emotional AI Engine
==========================================
Real-time sentiment analysis, stress detection, mood scoring.
Drives UX color changes, CalmMode automation, therapeutic responses.

This is the heart of emotional intelligence in NoizyOS.
"""

import re
from typing import Dict, List, Tuple

# ========================================
# EMOTION KEYWORD BANKS
# ========================================

POSITIVE = [
    "thank", "thanks", "great", "awesome", "better", "fixed", "ok", "cool",
    "perfect", "amazing", "excellent", "wonderful", "love", "happy", "good",
    "nice", "fantastic", "brilliant", "superb", "works", "working", "solved"
]

NEGATIVE = [
    "slow", "broken", "upset", "mad", "frustrated", "annoyed", "angry",
    "terrible", "awful", "horrible", "hate", "worst", "bad", "sucks",
    "useless", "garbage", "trash", "stupid", "dumb", "ridiculous"
]

STRESS = [
    "help", "urgent", "panic", "emergency", "can't", "stuck", "please",
    "asap", "now", "immediately", "desperate", "dying", "critical",
    "hurry", "fast", "quick", "important", "scared", "worried", "afraid"
]

CONFUSION = [
    "??", "?", "what", "how", "idk", "don't know", "confused", "lost",
    "huh", "wtf", "wth", "unclear", "understand", "explain", "meaning"
]

CALM_TRIGGERS = [
    "calm", "relax", "breathe", "okay", "alright", "fine", "settled",
    "better now", "feeling good", "all good", "no rush", "take time"
]


def analyze_emotion(text: str) -> Dict:
    """
    Analyze emotional content of text input.
    
    Args:
        text: User input text (from chat, voice transcription, etc.)
    
    Returns:
        Dict with mood, stress level, score, and recommendations.
    """
    if not text:
        return {
            "mood": "neutral",
            "stress": 0,
            "score": 0,
            "intensity": "low",
            "empathy_response": None
        }
    
    text_lower = text.lower()
    score = 0
    stress_value = 0
    confusion_value = 0

    # ========================================
    # POSITIVE SENTIMENT
    # ========================================
    for word in POSITIVE:
        if word in text_lower:
            score += 1
            # Double points for strong positives
            if word in ["amazing", "perfect", "love", "excellent"]:
                score += 1

    # ========================================
    # NEGATIVE SENTIMENT
    # ========================================
    for word in NEGATIVE:
        if word in text_lower:
            score -= 1
            # Double penalty for strong negatives
            if word in ["hate", "terrible", "awful", "worst"]:
                score -= 1

    # ========================================
    # STRESS INDICATORS
    # ========================================
    for word in STRESS:
        if word in text_lower:
            stress_value += 2
            # Extra stress for urgent words
            if word in ["emergency", "panic", "desperate", "dying"]:
                stress_value += 2

    # ========================================
    # CONFUSION INDICATORS
    # ========================================
    for word in CONFUSION:
        if word in text_lower:
            confusion_value += 1
            stress_value += 1  # Confusion adds mild stress

    # Count question marks (more = more confusion)
    question_marks = text.count("?")
    if question_marks > 2:
        confusion_value += question_marks - 1
        stress_value += 1

    # Check for ALL CAPS (indicates frustration/urgency)
    caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
    if caps_ratio > 0.5 and len(text) > 5:
        stress_value += 2
        score -= 1

    # Check for repeated punctuation (!!!, ???)
    if re.search(r'[!?]{3,}', text):
        stress_value += 2

    # ========================================
    # MOOD CATEGORIZATION
    # ========================================
    if stress_value >= 6:
        mood = "distress"
    elif stress_value >= 4:
        mood = "anxious"
    elif confusion_value >= 3:
        mood = "confused"
    elif score <= -3:
        mood = "frustrated"
    elif score < 0:
        mood = "unhappy"
    elif score >= 3:
        mood = "happy"
    elif score > 0:
        mood = "positive"
    else:
        mood = "neutral"

    # ========================================
    # INTENSITY LEVEL
    # ========================================
    total_signals = abs(score) + stress_value + confusion_value
    if total_signals >= 8:
        intensity = "high"
    elif total_signals >= 4:
        intensity = "medium"
    else:
        intensity = "low"

    # ========================================
    # EMPATHY RESPONSE GENERATION
    # ========================================
    empathy_response = generate_empathy_response(mood, stress_value)

    return {
        "mood": mood,
        "stress": stress_value,
        "confusion": confusion_value,
        "score": score,
        "intensity": intensity,
        "empathy_response": empathy_response
    }


def generate_empathy_response(mood: str, stress: int) -> str:
    """Generate an appropriate empathetic response based on mood."""
    
    responses = {
        "distress": [
            "I hear you. Let's slow down and solve this together.",
            "It's okay. I'm right here with you. We'll figure this out.",
            "Take a breath. I've got you. Let's tackle this step by step."
        ],
        "anxious": [
            "I understand this is stressful. Let me help.",
            "No rush — we'll work through this at your pace.",
            "I'm here to help. Let's take it one step at a time."
        ],
        "confused": [
            "No worries — let me explain that more clearly.",
            "Good question! Let me break that down for you.",
            "I get it — tech can be confusing. Here's what's happening..."
        ],
        "frustrated": [
            "I totally understand the frustration. Let's fix this.",
            "That's annoying — I get it. Here's what we can do.",
            "I hear you. Let me help make this right."
        ],
        "unhappy": [
            "I'm sorry you're dealing with this. Let me help.",
            "That's not great — let's see what we can do.",
            "I understand. Let's work on improving this."
        ],
        "happy": [
            "Awesome! Glad things are going well!",
            "That's great to hear!",
            "Excellent! Happy to help anytime."
        ],
        "positive": [
            "Great! Let me know if you need anything else.",
            "Perfect! I'm here if you have more questions.",
            "Sounds good! What else can I help with?"
        ],
        "neutral": [
            "How can I help you today?",
            "What would you like to work on?",
            "I'm here and ready to assist."
        ]
    }
    
    import random
    mood_responses = responses.get(mood, responses["neutral"])
    return random.choice(mood_responses)


def get_ui_mode(emotion_data: Dict) -> str:
    """Determine the UI mode based on emotional analysis."""
    mood = emotion_data.get("mood", "neutral")
    stress = emotion_data.get("stress", 0)
    
    if mood == "distress" or stress >= 6:
        return "calm"  # Blue, slow, soothing
    elif mood in ["anxious", "frustrated"] or stress >= 4:
        return "soft"  # Muted gold, gentle
    elif mood == "confused":
        return "guide"  # Helpful, clear, step-by-step
    elif mood in ["happy", "positive"]:
        return "bright"  # Vibrant, energetic
    else:
        return "normal"  # Standard gold/black


def get_ui_colors(ui_mode: str) -> Dict:
    """Get UI color scheme based on mode."""
    schemes = {
        "calm": {
            "bg": "#001F2F",
            "accent": "#00E5FF",
            "text": "#FFFFFF",
            "border": "#00A5B5"
        },
        "soft": {
            "bg": "#1A1A0A",
            "accent": "#D4A84B",
            "text": "#F0F0F0",
            "border": "#8B7355"
        },
        "guide": {
            "bg": "#0A0A1A",
            "accent": "#7B68EE",
            "text": "#FFFFFF",
            "border": "#5B4FCF"
        },
        "bright": {
            "bg": "#0A0A0A",
            "accent": "#00FF88",
            "text": "#FFFFFF",
            "border": "#00CC6A"
        },
        "normal": {
            "bg": "#000000",
            "accent": "#F5C542",
            "text": "#FFFFFF",
            "border": "#333333"
        }
    }
    return schemes.get(ui_mode, schemes["normal"])

