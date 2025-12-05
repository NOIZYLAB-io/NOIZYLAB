"""
NoizyOS Ultra — GEN-5 Personality Route
=======================================
API for generating and retrieving AI personas.
"""

from fastapi import APIRouter
from ..memory.client_memory import recall_client
from ..memory.device_memory import recall_device
from ..memory.issue_memory import recall_issues, repeated_issues
from ..memory.emotion_memory import average_mood, emotion_trend
from ..ai.personality_engine import generate_persona, get_greeting, build_ai_prompt

router = APIRouter()


def get_full_memory(email: str) -> dict:
    """Assemble complete memory profile for persona generation."""
    return {
        "client": recall_client(email),
        "device": recall_device(email),
        "issues": recall_issues(email),
        "patterns": repeated_issues(email),
        "avg_mood": average_mood(email),
        "mood_trend": emotion_trend(email),
        "is_returning": recall_client(email).get("session_count", 0) > 1
    }


@router.get("/persona/{email}")
def get_persona(email: str):
    """
    Generate a persona for a specific client.
    Returns personality configuration based on memory.
    """
    memory = get_full_memory(email)
    persona = generate_persona(memory)
    
    # Add greeting
    client_name = memory.get("client", {}).get("name")
    persona["greeting"] = get_greeting(persona, client_name)
    
    return persona


@router.post("/persona/generate")
def generate_persona_endpoint(payload: dict):
    """
    Generate a persona from provided memory data.
    Useful for testing or custom scenarios.
    """
    memory = payload.get("memory", {})
    persona = generate_persona(memory)
    return persona


@router.get("/greeting/{email}")
def get_client_greeting(email: str):
    """Get a personalized greeting for a client."""
    memory = get_full_memory(email)
    persona = generate_persona(memory)
    client_name = memory.get("client", {}).get("name")
    
    return {
        "greeting": get_greeting(persona, client_name),
        "relationship": persona.get("relationship"),
        "tone": persona.get("tone")
    }


@router.post("/prompt")
def build_prompt(payload: dict):
    """
    Build a complete AI prompt with personality and context.
    
    Expects:
        email: Client email
        input: User's message
    """
    email = payload.get("email")
    user_input = payload.get("input", "")
    
    if not email:
        return {"error": "Email required"}
    
    memory = get_full_memory(email)
    persona = generate_persona(memory)
    prompt = build_ai_prompt(persona, memory, user_input)
    
    return {
        "prompt": prompt,
        "persona": persona,
        "memory_summary": {
            "session_count": memory.get("client", {}).get("session_count", 0),
            "avg_mood": memory.get("avg_mood"),
            "issue_count": len(memory.get("issues", []))
        }
    }


@router.get("/modes")
def list_personality_modes():
    """List all available personality modes and configurations."""
    return {
        "tones": ["calm", "warm", "clinical", "upbeat", "empathetic", "professional"],
        "humor_levels": ["light", "techy", "dry", "none", "playful"],
        "relationships": ["new_client", "returning_client", "established_client", "trusted_partner"],
        "diagnostic_modes": ["proactive", "standard", "reactive"],
        "language_levels": ["simple", "gentle", "standard"],
        "priorities": ["emotional_support", "maintain_momentum", "problem_solving"]
    }

