"""
NoizyOS Ultra — NoizyMemory Unified Endpoint
============================================
Single API for all memory operations.
Combines client, device, issue, and emotional memory.
"""

from fastapi import APIRouter
from ..memory.client_memory import remember_client, recall_client, update_client
from ..memory.device_memory import remember_device, recall_device, get_recurring_device_problems
from ..memory.issue_memory import log_issue, recall_issues, repeated_issues, get_issue_patterns
from ..memory.emotion_memory import log_emotion, average_mood, emotion_trend, get_mood_recommendation

router = APIRouter()


@router.post("/remember")
def remember(payload: dict):
    """
    Store information about a client.
    Accepts any combination of: client, device, issue, mood data.
    """
    email = payload.get("email")
    
    if not email:
        return {"ok": False, "error": "Email required"}
    
    # Client data
    if "client" in payload:
        for key, value in payload["client"].items():
            remember_client(email, key, value)
    
    # Device data
    if "device" in payload:
        remember_device(email, payload["device"])
    
    # Issue data
    if "issue" in payload:
        issue_details = payload.get("issue_details", {})
        log_issue(email, payload["issue"], issue_details)
    
    # Mood data
    if "mood" in payload:
        context = payload.get("mood_context")
        log_emotion(email, payload["mood"], context)
    
    return {"ok": True, "email": email}


@router.get("/recall/{email}")
def recall(email: str):
    """
    Retrieve all stored information about a client.
    Returns unified memory profile.
    """
    client_data = recall_client(email)
    device_data = recall_device(email)
    issues = recall_issues(email)
    patterns = repeated_issues(email)
    issue_analysis = get_issue_patterns(email)
    avg_mood = average_mood(email)
    mood_trend = emotion_trend(email)
    mood_rec = get_mood_recommendation(email)
    device_problems = get_recurring_device_problems(email)
    
    return {
        "email": email,
        "client": client_data,
        "device": device_data,
        "issues": issues,
        "patterns": patterns,
        "issue_analysis": issue_analysis,
        "avg_mood": avg_mood,
        "mood_trend": mood_trend,
        "mood_recommendation": mood_rec,
        "device_problems": device_problems,
        "is_returning": client_data.get("session_count", 0) > 1
    }


@router.post("/update-client")
def update_client_data(payload: dict):
    """Update client profile data."""
    email = payload.get("email")
    data = payload.get("data", {})
    
    if not email:
        return {"ok": False, "error": "Email required"}
    
    update_client(email, data)
    return {"ok": True}


@router.post("/log-issue")
def log_issue_endpoint(payload: dict):
    """Log a new issue for a client."""
    email = payload.get("email")
    issue = payload.get("issue")
    details = payload.get("details", {})
    
    if not email or not issue:
        return {"ok": False, "error": "Email and issue required"}
    
    log_issue(email, issue, details)
    return {"ok": True}


@router.post("/log-mood")
def log_mood_endpoint(payload: dict):
    """Log a mood for a client."""
    email = payload.get("email")
    mood = payload.get("mood")
    context = payload.get("context")
    
    if not email or not mood:
        return {"ok": False, "error": "Email and mood required"}
    
    log_emotion(email, mood, context)
    return {"ok": True}


@router.get("/patterns/{email}")
def get_patterns(email: str):
    """Get issue patterns for a client."""
    return {
        "issue_patterns": get_issue_patterns(email),
        "device_problems": get_recurring_device_problems(email),
        "mood_trend": emotion_trend(email)
    }


@router.get("/summary/{email}")
def get_summary(email: str):
    """Get a brief summary for AI context."""
    client = recall_client(email)
    issues = recall_issues(email, limit=5)
    patterns = repeated_issues(email)
    mood = average_mood(email)
    
    return {
        "name": client.get("name", "Client"),
        "session_count": client.get("session_count", 0),
        "recent_issues": [i.get("issue") for i in issues],
        "recurring_problems": [k for k, v in patterns.items() if v > 1],
        "mood": mood,
        "recommendation": get_mood_recommendation(email)
    }

