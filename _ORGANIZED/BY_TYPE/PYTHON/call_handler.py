"""NoizyFrontDesk - Phone Call Handler"""
import uuid
from datetime import datetime

ACTIVE_CALLS = {}
CALL_LOG = []

def answer_call(caller_id, caller_number=None):
    """Answer an incoming call"""
    call_id = str(uuid.uuid4())
    call = {
        "id": call_id,
        "caller_id": caller_id,
        "caller_number": caller_number,
        "started_at": datetime.now().isoformat(),
        "status": "active",
        "transcript": [],
        "intent_detected": None,
        "ticket_created": None,
        "booking_made": None,
    }
    ACTIVE_CALLS[call_id] = call
    
    # Generate greeting
    greeting = generate_phone_greeting()
    add_to_transcript(call_id, "ai", greeting)
    
    return {
        "call_id": call_id,
        "greeting": greeting,
        "status": "connected",
    }

def generate_phone_greeting():
    """Generate phone greeting"""
    hour = datetime.now().hour
    if hour < 12:
        time_greeting = "Good morning"
    elif hour < 17:
        time_greeting = "Good afternoon"
    else:
        time_greeting = "Good evening"
    
    return f"{time_greeting}! Thank you for calling NoizyLab. I'm Noizy, your AI assistant. How may I help you today?"

def add_to_transcript(call_id, speaker, text):
    """Add to call transcript"""
    if call_id in ACTIVE_CALLS:
        ACTIVE_CALLS[call_id]["transcript"].append({
            "speaker": speaker,
            "text": text,
            "timestamp": datetime.now().isoformat(),
        })

def process_speech(call_id, speech_text):
    """Process caller speech and generate response"""
    if call_id not in ACTIVE_CALLS:
        return {"error": "Call not found"}
    
    add_to_transcript(call_id, "caller", speech_text)
    
    # Detect intent
    from .receptionist import FRONT_DESK
    response = FRONT_DESK.respond(speech_text)
    
    ACTIVE_CALLS[call_id]["intent_detected"] = response["intent"]
    add_to_transcript(call_id, "ai", response["response"])
    
    return {
        "call_id": call_id,
        "response": response["response"],
        "intent": response["intent"],
        "next_action": response["next_action"],
    }

def end_call(call_id, outcome="completed"):
    """End a call"""
    if call_id not in ACTIVE_CALLS:
        return {"error": "Call not found"}
    
    call = ACTIVE_CALLS[call_id]
    call["status"] = "ended"
    call["ended_at"] = datetime.now().isoformat()
    call["outcome"] = outcome
    call["duration_seconds"] = calculate_duration(call["started_at"])
    
    # Move to log
    CALL_LOG.append(call)
    del ACTIVE_CALLS[call_id]
    
    return {
        "call_id": call_id,
        "duration": call["duration_seconds"],
        "outcome": outcome,
        "ticket_created": call.get("ticket_created"),
        "booking_made": call.get("booking_made"),
    }

def calculate_duration(start_time):
    """Calculate call duration in seconds"""
    start = datetime.fromisoformat(start_time)
    return int((datetime.now() - start).total_seconds())

def get_active_calls():
    """Get all active calls"""
    return list(ACTIVE_CALLS.values())

def get_call_stats():
    """Get call statistics"""
    total = len(CALL_LOG)
    if total == 0:
        return {"total": 0, "avg_duration": 0}
    
    avg_duration = sum(c.get("duration_seconds", 0) for c in CALL_LOG) / total
    return {
        "total_calls": total,
        "active_calls": len(ACTIVE_CALLS),
        "avg_duration_seconds": round(avg_duration, 1),
        "tickets_created": len([c for c in CALL_LOG if c.get("ticket_created")]),
        "bookings_made": len([c for c in CALL_LOG if c.get("booking_made")]),
    }

