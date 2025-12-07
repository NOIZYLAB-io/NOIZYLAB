from .persona_core import persona


def handle_hype(text, tone):
    return {
        "intent": "hype",
        "tone": tone,
        "reply": (
            f"{persona.base_intro()} BRO — LET ME COOK FOR A SECOND 🔥🔥🔥 "
            "You're sitting on an M2 Ultra, jumbo frames, Cursor, CB_01… "
            "you're basically piloting a spaceship. What's the mission today?"
        )
    }

