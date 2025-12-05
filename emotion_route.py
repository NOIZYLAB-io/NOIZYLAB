"""
NoizyOS Ultra — GEN-4 Emotional AI Route
=========================================
Analyzes user input for emotional content.
Returns mood, stress level, and UI mode recommendations.
Drives real-time UX adaptation.
"""

from fastapi import APIRouter
from ..ai.emotion_engine import (
    analyze_emotion,
    get_ui_mode,
    get_ui_colors,
    generate_empathy_response
)

router = APIRouter()


@router.post("/emotion")
def emotion(payload: dict):
    """
    Analyze emotional content of user input.
    Returns mood, stress, score, and recommended UI mode.
    """
    text = payload.get("text", "")
    emo = analyze_emotion(text)
    
    # Get UI recommendations
    ui_mode = get_ui_mode(emo)
    ui_colors = get_ui_colors(ui_mode)

    return {
        "mood": emo["mood"],
        "stress": emo["stress"],
        "confusion": emo.get("confusion", 0),
        "score": emo["score"],
        "intensity": emo["intensity"],
        "ui_mode": ui_mode,
        "ui_colors": ui_colors,
        "empathy_response": emo["empathy_response"]
    }


@router.post("/empathy")
def get_empathy(payload: dict):
    """Get an empathetic response for a given mood."""
    mood = payload.get("mood", "neutral")
    stress = payload.get("stress", 0)
    response = generate_empathy_response(mood, stress)
    return {"response": response}


@router.post("/ui-mode")
def get_recommended_ui(payload: dict):
    """Get recommended UI mode and colors based on text."""
    text = payload.get("text", "")
    emo = analyze_emotion(text)
    ui_mode = get_ui_mode(emo)
    ui_colors = get_ui_colors(ui_mode)
    
    return {
        "mode": ui_mode,
        "colors": ui_colors
    }


@router.get("/modes")
def list_ui_modes():
    """List all available UI modes and their color schemes."""
    modes = ["calm", "soft", "guide", "bright", "normal"]
    return {
        mode: get_ui_colors(mode) for mode in modes
    }

