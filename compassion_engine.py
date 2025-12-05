from typing import Dict, Optional
import time

CONVERSATION_MEMORY = {}


class CompassionEngine:
    """GEN3 Compassion Engine v3 - Deep human understanding"""

    def __init__(self):
        self.warmth_phrases = [
            "I'm right here with you.",
            "You're not alone in this.",
            "Let's figure this out together.",
            "I've got you.",
            "Take your time — no rush.",
        ]

        self.distress_responses = {
            "panic": "Breathe with me. In... out... You're safe. I'm here.",
            "frustration": "I completely understand why this is frustrating. Let's fix it.",
            "confusion": "That's okay — this stuff can be confusing. Let me break it down.",
            "fear": "Nothing bad is happening. We'll go step by step, nice and slow.",
            "overwhelm": "Let's pause and focus on just one thing at a time."
        }

    def detect_distress_level(self, text: str) -> Dict:
        """Detect specific type and level of distress"""
        text_lower = text.lower()

        if any(w in text_lower for w in ["panic", "can't breathe", "freaking out"]):
            return {"type": "panic", "level": 3}
        if any(w in text_lower for w in ["angry", "pissed", "frustrated", "stupid"]):
            return {"type": "frustration", "level": 2}
        if any(w in text_lower for w in ["confused", "don't understand", "lost"]):
            return {"type": "confusion", "level": 1}
        if any(w in text_lower for w in ["scared", "afraid", "worried"]):
            return {"type": "fear", "level": 2}
        if any(w in text_lower for w in ["overwhelmed", "too much", "can't handle"]):
            return {"type": "overwhelm", "level": 2}

        return {"type": "neutral", "level": 0}

    def get_compassionate_response(self, distress: Dict) -> str:
        """Get appropriate compassionate response"""
        dtype = distress.get("type", "neutral")
        if dtype in self.distress_responses:
            return self.distress_responses[dtype]
        return self.warmth_phrases[0]

    def mirror_tone(self, text: str) -> str:
        """Mirror the user's communication style"""
        if text.isupper():
            return "loud"  # User is emphatic
        if "?" in text and len(text) < 30:
            return "questioning"
        if "..." in text:
            return "hesitant"
        if "!" in text:
            return "energetic"
        return "calm"

    def remember_conversation(self, user_id: str, message: str, response: str):
        """Store conversation for context memory"""
        if user_id not in CONVERSATION_MEMORY:
            CONVERSATION_MEMORY[user_id] = []

        CONVERSATION_MEMORY[user_id].append({
            "timestamp": time.time(),
            "user": message,
            "ai": response
        })

        # Keep last 50 exchanges
        CONVERSATION_MEMORY[user_id] = CONVERSATION_MEMORY[user_id][-50:]

    def get_conversation_context(self, user_id: str, last_n: int = 5) -> list:
        """Get recent conversation context"""
        if user_id not in CONVERSATION_MEMORY:
            return []
        return CONVERSATION_MEMORY[user_id][-last_n:]


compassion = CompassionEngine()

