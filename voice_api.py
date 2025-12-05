from fastapi import APIRouter, UploadFile
from .voice.voice_router import process_audio

router = APIRouter()


@router.post("/voice")
async def voice_entry(file: UploadFile):
    audio_bytes = await file.read()
    return process_audio(audio_bytes)

