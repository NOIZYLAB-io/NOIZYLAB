from .persona_core import persona


def handle_story(text, tone):
    return {
        "intent": "story",
        "tone": tone,
        "reply": (
            f"{persona.base_intro()} Let me paint you a scene — "
            "a device at the edge of failure, the hum of a fan like a heartbeat, "
            "and a technician with fire in their eyes. "
            "Now tell me your part of the story."
        )
    }

