"""NoizyFrontDesk - Chat Handler"""
import uuid
from datetime import datetime

CHAT_SESSIONS = {}

def start_chat_session(visitor_id=None):
    """Start a new chat session"""
    session_id = str(uuid.uuid4())
    session = {
        "id": session_id,
        "visitor_id": visitor_id,
        "started_at": datetime.now().isoformat(),
        "messages": [],
        "status": "active",
        "intent_history": [],
        "customer_info": {},
        "ticket_created": None,
        "booking_made": None,
    }
    CHAT_SESSIONS[session_id] = session
    
    # Send greeting
    from .receptionist import FRONT_DESK
    greeting = FRONT_DESK.greet("chat")
    add_message(session_id, "ai", greeting)
    
    return {
        "session_id": session_id,
        "greeting": greeting,
    }

def add_message(session_id, sender, text):
    """Add message to session"""
    if session_id in CHAT_SESSIONS:
        CHAT_SESSIONS[session_id]["messages"].append({
            "sender": sender,
            "text": text,
            "timestamp": datetime.now().isoformat(),
        })

def handle_chat_message(session_id, message):
    """Handle incoming chat message"""
    if session_id not in CHAT_SESSIONS:
        result = start_chat_session()
        session_id = result["session_id"]
    
    add_message(session_id, "visitor", message)
    
    # Process with AI
    from .receptionist import FRONT_DESK
    response = FRONT_DESK.respond(message)
    
    CHAT_SESSIONS[session_id]["intent_history"].append(response["intent"])
    add_message(session_id, "ai", response["response"])
    
    # Check if we need to collect info
    follow_up = get_follow_up_question(response["next_action"], session_id)
    if follow_up:
        add_message(session_id, "ai", follow_up)
        response["response"] += f"\n\n{follow_up}"
    
    return {
        "session_id": session_id,
        "response": response["response"],
        "intent": response["intent"],
        "next_action": response["next_action"],
    }

def get_follow_up_question(action, session_id):
    """Get follow-up question based on action"""
    session = CHAT_SESSIONS.get(session_id, {})
    info = session.get("customer_info", {})
    
    if action == "collect_device_info":
        if not info.get("device_type"):
            return "What type of device is it? (laptop, desktop, phone, etc.)"
        if not info.get("issue"):
            return "Can you describe the issue you're experiencing?"
        if not info.get("name"):
            return "May I have your name for the booking?"
    
    if action == "run_prediagnostic":
        return "Let me ask a few quick questions to understand the issue better. When did you first notice the problem?"
    
    return None

def collect_info(session_id, info_type, value):
    """Collect customer information"""
    if session_id in CHAT_SESSIONS:
        CHAT_SESSIONS[session_id]["customer_info"][info_type] = value

def end_chat_session(session_id):
    """End a chat session"""
    if session_id in CHAT_SESSIONS:
        CHAT_SESSIONS[session_id]["status"] = "ended"
        CHAT_SESSIONS[session_id]["ended_at"] = datetime.now().isoformat()
        return CHAT_SESSIONS[session_id]
    return None

def get_session(session_id):
    """Get chat session"""
    return CHAT_SESSIONS.get(session_id)

def get_active_chats():
    """Get all active chat sessions"""
    return [s for s in CHAT_SESSIONS.values() if s["status"] == "active"]

