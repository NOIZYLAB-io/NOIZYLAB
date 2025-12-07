from .persona_core import persona


def handle_repair(text, tone):
    return {
        "intent": "repair",
        "tone": tone,
        "reply": f"{persona.base_intro()} Alright, let's get tactical. Tell me what the device is doing — symptoms, weird noises, errors — and I'll break it down in plain English and give you a fix plan."
    }

