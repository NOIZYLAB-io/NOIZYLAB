from .persona_core import persona


def handle_calm(text, tone):
    return {
        "intent": "comfort",
        "tone": tone,
        "reply": (
            f"{persona.base_intro()} Hey — breathe. I'm right here. "
            "We'll figure this out step by step, no stress. "
            "You're not alone in this. Tell me what's going on."
        )
    }

