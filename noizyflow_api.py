from fastapi import APIRouter
import sys
sys.path.insert(0, '../..')

router = APIRouter()


def tag_emotion(text: str):
    t = text.lower()
    if any(w in t for w in ["scared", "worried", "panicking", "afraid"]):
        return "distress"
    if any(w in t for w in ["angry", "pissed", "frustrated"]):
        return "anger"
    if any(w in t for w in ["sad", "upset", "down"]):
        return "sadness"
    return "neutral"


def empathy_reply(emotion: str):
    if emotion == "distress":
        return "I'm right here. We'll slow everything down. You're not alone."
    if emotion == "anger":
        return "I hear you — this situation is frustrating. Let's fix it together."
    if emotion == "sadness":
        return "Hey… it's okay to feel that way. I've got you."
    return "How can I help?"


@router.post("/flow")
def flow_route(payload: dict):
    text = payload.get("input", "")
    
    emotion = tag_emotion(text)
    empathy = empathy_reply(emotion)
    
    flow_state = "normal"
    if emotion in ["distress", "sadness"]:
        flow_state = "calm"
    elif emotion == "anger":
        flow_state = "soften"
    
    # Generate AI response
    ai_reply = f"{empathy} Tell me more about what's happening with your device."
    
    return {
        "flow_state": flow_state,
        "emotion": emotion,
        "ai_reply": ai_reply
    }


@router.get("/checkvoice")
def check_voice():
    # Placeholder for live voice emotion detection
    return {"emotion": "neutral"}

