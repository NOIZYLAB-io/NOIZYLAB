"""FrontDesk: Intake Collector"""
SESSIONS = {}

def collect_info(session_id, field, value):
    """Collect client information"""
    if session_id not in SESSIONS: SESSIONS[session_id] = {}
    SESSIONS[session_id][field] = value
    return get_next_question(session_id)

def get_next_question(session_id):
    info = SESSIONS.get(session_id, {})
    if not info.get("name"): return {"field": "name", "question": "May I have your name?"}
    if not info.get("device"): return {"field": "device", "question": "What type of device needs service?"}
    if not info.get("issue"): return {"field": "issue", "question": "Can you describe the issue?"}
    if not info.get("contact"): return {"field": "contact", "question": "What's the best way to reach you?"}
    return {"complete": True, "data": info}

def get_collected(session_id):
    return SESSIONS.get(session_id, {})

def clear_session(session_id):
    if session_id in SESSIONS: del SESSIONS[session_id]

