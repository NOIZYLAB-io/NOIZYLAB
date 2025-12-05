"""FrontDesk: Pre-Diagnostic Check"""
QUESTIONS = {
    "laptop": [{"id": "q1", "q": "Is it turning on?", "type": "yes_no"}, {"id": "q2", "q": "Any error messages?", "type": "text"}, {"id": "q3", "q": "When did it start?", "type": "text"}],
    "desktop": [{"id": "q1", "q": "Is it powering on?", "type": "yes_no"}, {"id": "q2", "q": "Any beeps or lights?", "type": "text"}],
    "network": [{"id": "q1", "q": "Is internet completely down or slow?", "type": "choice", "options": ["Down", "Slow", "Intermittent"]}, {"id": "q2", "q": "How many devices affected?", "type": "text"}],
    "general": [{"id": "q1", "q": "What device has the problem?", "type": "text"}, {"id": "q2", "q": "Describe the issue", "type": "text"}],
}

SESSIONS = {}

def get_questions(device_type):
    return QUESTIONS.get(device_type.lower(), QUESTIONS["general"])

def run_preflight(session_id, device_type):
    """Start pre-diagnostic session"""
    questions = get_questions(device_type)
    SESSIONS[session_id] = {"device": device_type, "questions": questions, "answers": {}, "current": 0}
    return {"session_id": session_id, "first_question": questions[0] if questions else None, "total": len(questions)}

def answer(session_id, answer_value):
    if session_id not in SESSIONS: return {"error": "Session not found"}
    s = SESSIONS[session_id]
    q = s["questions"][s["current"]]
    s["answers"][q["id"]] = answer_value
    s["current"] += 1
    if s["current"] >= len(s["questions"]):
        return {"complete": True, "diagnosis": _generate_diagnosis(s)}
    return {"next_question": s["questions"][s["current"]], "progress": f"{s['current']+1}/{len(s['questions'])}"}

def _generate_diagnosis(session):
    answers = session["answers"]
    issues = []
    severity = "medium"
    if answers.get("q1") == "no": issues.append("Device not powering on"); severity = "high"
    if "error" in str(answers).lower(): issues.append("Error messages present")
    return {"issues": issues or ["Further diagnosis needed"], "severity": severity, "recommended": "in_person" if severity == "high" else "remote"}

