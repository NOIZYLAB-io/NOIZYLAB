"""NoizySynth API Routes"""
from fastapi import APIRouter
from ..noizysynth.pipeline import synthesize

router = APIRouter(prefix="/synth", tags=["NoizySynth"])

@router.post("/generate")
def generate(payload: dict):
    return synthesize(payload["mode"], payload["prompt"], payload.get("context", {}))

@router.post("/code")
def gen_code(payload: dict):
    return synthesize("code", payload["prompt"], payload.get("context", {}))

@router.post("/audio")
def gen_audio(payload: dict):
    return synthesize("audio", payload["prompt"], {})

@router.post("/image")
def gen_image(payload: dict):
    return synthesize("image", payload["prompt"], {})

@router.post("/ui")
def gen_ui(payload: dict):
    return synthesize("ui", payload["prompt"], {})

@router.post("/text")
def gen_text(payload: dict):
    return synthesize("text", payload["prompt"], payload.get("context", {}))

