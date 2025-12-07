from fastapi import APIRouter
import sys
sys.path.insert(0, '..')
from accessibility_engine.simple_mode import simple_text
from accessibility_engine.autism_calm_protocol import autism_calm_response
from accessibility_engine.motor_limit_support import motor_predict
from accessibility_engine.emergency_flag import emergency_protocol
from accessibility_engine.voice_simplify import clean_voice_input
from accessibility_engine.visual_aid import visual_contrast
from accessibility_engine.touch_assist import touch_buttons

router = APIRouter()


@router.post("/simple")
def simplify(payload: dict):
    return {"text": simple_text(payload["text"])}


@router.get("/calm")
def calm():
    return {"text": autism_calm_response()}


@router.post("/motor")
def motor(payload: dict):
    return {"action": motor_predict(payload["intent"])}


@router.get("/emergency")
def emergency():
    return emergency_protocol()


@router.post("/cleanvoice")
def clean(payload: dict):
    return {"clean": clean_voice_input(payload["text"])}


@router.get("/visual")
def contrast():
    return visual_contrast("Accessibility Mode Enabled")


@router.get("/touch")
def touch():
    return touch_buttons()

