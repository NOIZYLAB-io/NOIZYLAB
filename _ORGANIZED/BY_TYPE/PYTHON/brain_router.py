from .intent_classifier import classify_intent
from .persona_core import persona
from .skills_repair import handle_repair
from .skills_diag import handle_diag
from .skills_calmmode import handle_calm
from .skills_hype import handle_hype
from .skills_story import handle_story


def route(input_text: str):
    intent = classify_intent(input_text)
    tone = persona.pick_tone(intent)

    if intent == "repair":
        return handle_repair(input_text, tone)

    if intent == "diagnostic":
        return handle_diag(input_text, tone)

    if intent == "comfort":
        return handle_calm(input_text, tone)

    if intent == "hype":
        return handle_hype(input_text, tone)

    if intent == "story":
        return handle_story(input_text, tone)

    return {
        "intent": intent,
        "tone": tone,
        "reply": f"{persona.base_intro()} What's on your mind?"
    }

