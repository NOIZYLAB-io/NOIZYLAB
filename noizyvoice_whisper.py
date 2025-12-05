"""
NoizyOS Ultra — NoizyVoice GEN-2
================================
Real-time voice transcription with Whisper + Emotional AI.
Provides voice → text → emotion → UI mode pipeline.

For production: pip install openai-whisper
For development: Uses mock transcription if Whisper not available.
"""

from fastapi import APIRouter, UploadFile, File
import os
import tempfile

router = APIRouter()

# Try to load Whisper model
try:
    import whisper
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
    WHISPER_AVAILABLE = True
    print("✓ Whisper model loaded successfully")
except ImportError:
    WHISPER_AVAILABLE = False
    model = None
    print("⚠ Whisper not installed - using mock transcription")

# Import emotion engine
try:
    from ..ai.emotion_engine import analyze_emotion, get_ui_mode
except:
    # Fallback if import fails
    def analyze_emotion(text):
        return {"mood": "neutral", "stress": 0, "score": 0, "intensity": "low", "empathy_response": None}
    def get_ui_mode(emo):
        return "normal"


@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    """
    Transcribe audio file and analyze emotion.
    Returns text, mood, stress level, and recommended UI mode.
    """
    audio_bytes = await file.read()
    
    if WHISPER_AVAILABLE and model:
        # Write to temp file for Whisper
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
        
        try:
            result = model.transcribe(tmp_path)
            text = result["text"].strip()
        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    else:
        # Mock transcription for development
        text = "[Voice input received - Whisper not installed]"
    
    # Analyze emotion
    emo = analyze_emotion(text)
    ui_mode = get_ui_mode(emo)
    
    return {
        "text": text,
        "mood": emo["mood"],
        "stress": emo["stress"],
        "intensity": emo.get("intensity", "low"),
        "ui_mode": ui_mode,
        "empathy_response": emo.get("empathy_response"),
        "whisper_available": WHISPER_AVAILABLE
    }


@router.post("/analyze-text")
async def analyze_voice_text(payload: dict):
    """
    Analyze text that was transcribed elsewhere.
    Useful for external speech-to-text services.
    """
    text = payload.get("text", "")
    emo = analyze_emotion(text)
    ui_mode = get_ui_mode(emo)
    
    return {
        "text": text,
        "mood": emo["mood"],
        "stress": emo["stress"],
        "ui_mode": ui_mode,
        "empathy_response": emo.get("empathy_response")
    }


@router.get("/status")
def voice_status():
    """Check if voice transcription is available."""
    return {
        "whisper_available": WHISPER_AVAILABLE,
        "model": "base" if WHISPER_AVAILABLE else None,
        "status": "ready" if WHISPER_AVAILABLE else "mock_mode"
    }


@router.post("/quick-emotion")
async def quick_emotion(payload: dict):
    """
    Quick emotion check for voice without full transcription.
    Used for real-time UI updates during recording.
    """
    text = payload.get("text", "")
    if not text:
        return {"ui_mode": "normal", "mood": "neutral"}
    
    emo = analyze_emotion(text)
    return {
        "ui_mode": get_ui_mode(emo),
        "mood": emo["mood"],
        "stress": emo["stress"]
    }

