from .persona_core import persona


def handle_diag(text, tone):
    return {
        "intent": "diagnostic",
        "tone": tone,
        "reply": f"{persona.base_intro()} Running mental diagnostics… tell me the issue and I'll snap together a diagnostic chain faster than your CPU hits turbo mode."
    }

