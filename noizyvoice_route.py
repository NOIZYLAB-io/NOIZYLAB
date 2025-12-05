"""
NoizyVoice API Routes
=====================
REST API for voice processing, commands, and TTS.
"""

from fastapi import APIRouter, UploadFile, File, Query
from typing import Optional

router = APIRouter(prefix="/voice", tags=["NoizyVoice"])


@router.post("/process")
async def process_voice(
    device: str = Query("default", description="Device ID"),
    require_wakeword: bool = Query(True, description="Require wakeword"),
    verify_identity: bool = Query(False, description="Verify speaker identity"),
    generate_speech: bool = Query(True, description="Generate TTS response"),
    file: UploadFile = File(..., description="Audio data")
):
    """
    Process voice input through the complete pipeline.
    """
    from ..noizyvoice.pipeline import process_voice as pv
    
    audio_bytes = await file.read()
    result = pv(
        audio_bytes,
        device_id=device,
        require_wakeword=require_wakeword,
        verify_identity=verify_identity,
        generate_speech=generate_speech
    )
    
    return result.to_dict()


@router.post("/transcribe")
async def transcribe(
    device: str = Query("default"),
    file: UploadFile = File(...)
):
    """
    Transcribe audio to text (ASR only).
    """
    from ..noizyvoice.asr import transcribe_audio
    
    audio_bytes = await file.read()
    result = transcribe_audio(audio_bytes, device)
    
    return result.to_dict()


@router.post("/command")
async def text_command(payload: dict):
    """
    Process a text command (bypass ASR).
    """
    from ..noizyvoice.pipeline import process_text_command
    
    text = payload.get("text", "")
    device = payload.get("device", "default")
    
    result = process_text_command(text, device)
    return result.to_dict()


@router.post("/speak")
async def speak(payload: dict):
    """
    Generate speech from text (TTS).
    """
    from ..noizyvoice.tts import synthesize_speech
    
    text = payload.get("text", "")
    voice_id = payload.get("voice", "default")
    
    result = synthesize_speech(text, voice_id)
    return result.to_dict()


@router.post("/identify")
async def identify_speaker(file: UploadFile = File(...)):
    """
    Identify speaker from voice.
    """
    from ..noizyvoice.voiceprint import identify_speaker as identify
    
    audio_bytes = await file.read()
    result = identify(audio_bytes)
    
    return result


@router.post("/verify")
async def verify_speaker(
    identity_id: str = Query(..., description="Identity to verify"),
    file: UploadFile = File(...)
):
    """
    Verify speaker identity.
    """
    from ..noizyvoice.voiceprint import verify_voice
    
    audio_bytes = await file.read()
    result = verify_voice(audio_bytes, identity_id)
    
    return result


@router.post("/enroll")
async def enroll_voice(
    identity_id: str = Query(..., description="Identity ID"),
    file: UploadFile = File(...)
):
    """
    Enroll a voiceprint for an identity.
    """
    from ..noizyvoice.voiceprint import enroll_voice
    
    audio_bytes = await file.read()
    result = enroll_voice(audio_bytes, identity_id)
    
    return result


@router.post("/emotion")
async def detect_emotion(file: UploadFile = File(...)):
    """
    Detect emotion from voice.
    """
    from ..noizyvoice.emotion import detect_emotion as detect
    
    audio_bytes = await file.read()
    result = detect(audio_bytes)
    
    return result.to_dict()


@router.post("/wakeword")
async def check_wakeword(payload: dict):
    """
    Check text for wakeword.
    """
    from ..noizyvoice.wakeword import detect_wakeword
    
    text = payload.get("text", "")
    result = detect_wakeword(text)
    
    return result.to_dict()


@router.get("/wakewords")
async def list_wakewords():
    """
    List all registered wakewords.
    """
    from ..noizyvoice.wakeword import list_wakewords
    
    return list_wakewords()


@router.post("/wakeword/register")
async def register_wakeword(payload: dict):
    """
    Register a new wakeword.
    """
    from ..noizyvoice.wakeword import register_wakeword
    
    result = register_wakeword(
        payload["id"],
        payload["phrases"],
        payload["action"],
        payload.get("priority", 5)
    )
    
    return {"success": result}


@router.get("/voices")
async def list_voices():
    """
    List available TTS voices.
    """
    from ..noizyvoice.tts import list_voices
    
    return list_voices()


@router.get("/commands")
async def list_commands():
    """
    List available voice commands.
    """
    from ..noizyvoice.commands import list_available_commands
    
    return {"commands": list_available_commands()}


@router.get("/status")
async def voice_status():
    """
    Get voice system status.
    """
    from ..noizyvoice.asr import is_model_loaded
    from ..noizyvoice.wakeword import list_wakewords
    from ..noizyvoice.tts import list_voices
    
    return {
        "asr_model_loaded": is_model_loaded(),
        "wakewords_count": len(list_wakewords()),
        "voices_count": len(list_voices()),
        "status": "ready",
    }

