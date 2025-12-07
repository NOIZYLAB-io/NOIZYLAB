from .stt_engine import transcribe
from .tts_engine import synthesize
from .wakeword import detect_wakeword
from ..brain_router import route
from ..noizyguardian import detect_distress, respond_to_distress


def process_audio(audio_bytes: bytes):
    text = transcribe(audio_bytes)

    if detect_wakeword(text):
        return {
            "wakeword": True,
            "reply": "Hey! I'm awake. What do you need?",
            "audio": synthesize("Hey! I'm awake. What do you need?")
        }

    if detect_distress(text):
        return {
            "wakeword": False,
            "distress": True,
            "reply": respond_to_distress(),
            "audio": synthesize(respond_to_distress())
        }

    response = route(text)
    tts = synthesize(response["reply"])

    return {
        "wakeword": False,
        "text_input": text,
        "ai_response": response,
        "audio": tts
    }

