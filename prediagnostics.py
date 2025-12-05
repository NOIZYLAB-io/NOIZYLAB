"""NoizyFrontDesk - Pre-Diagnostic Questions"""
import uuid
from datetime import datetime

DIAGNOSTIC_FLOWS = {
    "laptop": [
        {"id": "q1", "question": "Is your laptop turning on at all?", "type": "yes_no"},
        {"id": "q2", "question": "Do you see any error messages? If yes, what do they say?", "type": "text"},
        {"id": "q3", "question": "When did the problem start?", "type": "choice", "options": ["Today", "This week", "Longer than a week"]},
        {"id": "q4", "question": "Has anything changed recently? (new software, updates, physical damage)", "type": "text"},
        {"id": "q5", "question": "What's the make and model of your laptop?", "type": "text"},
    ],
    "desktop": [
        {"id": "q1", "question": "Is your computer turning on?", "type": "yes_no"},
        {"id": "q2", "question": "Do you hear any beeps or see any lights?", "type": "text"},
        {"id": "q3", "question": "When did the problem start?", "type": "choice", "options": ["Today", "This week", "Longer than a week"]},
        {"id": "q4", "question": "What's the make and model?", "type": "text"},
    ],
    "phone": [
        {"id": "q1", "question": "What type of phone do you have? (iPhone, Samsung, etc.)", "type": "text"},
        {"id": "q2", "question": "Is the screen cracked or damaged?", "type": "yes_no"},
        {"id": "q3", "question": "What issue are you experiencing?", "type": "text"},
    ],
    "network": [
        {"id": "q1", "question": "Is your internet completely down or just slow?", "type": "choice", "options": ["Completely down", "Slow", "Intermittent"]},
        {"id": "q2", "question": "How many devices are affected?", "type": "choice", "options": ["One device", "Some devices", "All devices"]},
        {"id": "q3", "question": "Have you tried restarting your router?", "type": "yes_no"},
    ],
    "general": [
        {"id": "q1", "question": "What device is having the problem?", "type": "text"},
        {"id": "q2", "question": "Can you describe the issue?", "type": "text"},
        {"id": "q3", "question": "When did it start?", "type": "text"},
    ],
}

DIAGNOSTIC_SESSIONS = {}

def get_diagnostic_questions(device_type):
    """Get diagnostic questions for a device type"""
    return DIAGNOSTIC_FLOWS.get(device_type.lower(), DIAGNOSTIC_FLOWS["general"])

def run_prediagnostic(session_id, device_type):
    """Start a pre-diagnostic session"""
    diag_id = str(uuid.uuid4())
    questions = get_diagnostic_questions(device_type)
    
    session = {
        "id": diag_id,
        "session_id": session_id,
        "device_type": device_type,
        "questions": questions,
        "answers": {},
        "current_question": 0,
        "started_at": datetime.now().isoformat(),
        "completed": False,
        "preliminary_diagnosis": None,
    }
    DIAGNOSTIC_SESSIONS[diag_id] = session
    
    return {
        "diagnostic_id": diag_id,
        "first_question": questions[0] if questions else None,
        "total_questions": len(questions),
    }

def answer_question(diag_id, answer):
    """Answer a diagnostic question"""
    if diag_id not in DIAGNOSTIC_SESSIONS:
        return {"error": "Diagnostic session not found"}
    
    session = DIAGNOSTIC_SESSIONS[diag_id]
    current = session["current_question"]
    questions = session["questions"]
    
    if current >= len(questions):
        return {"error": "All questions answered"}
    
    session["answers"][questions[current]["id"]] = answer
    session["current_question"] += 1
    
    if session["current_question"] >= len(questions):
        session["completed"] = True
        session["completed_at"] = datetime.now().isoformat()
        session["preliminary_diagnosis"] = generate_preliminary_diagnosis(session)
        return {
            "completed": True,
            "diagnosis": session["preliminary_diagnosis"],
        }
    
    return {
        "completed": False,
        "next_question": questions[session["current_question"]],
        "progress": f"{session['current_question'] + 1}/{len(questions)}",
    }

def generate_preliminary_diagnosis(session):
    """Generate preliminary diagnosis from answers"""
    answers = session["answers"]
    device = session["device_type"]
    
    issues = []
    severity = "medium"
    
    # Analyze answers
    if answers.get("q1") == "no":
        issues.append("Device not powering on - possible power supply or hardware issue")
        severity = "high"
    
    if "error" in str(answers).lower():
        issues.append("Error messages present - software or driver issue likely")
    
    if "slow" in str(answers).lower():
        issues.append("Performance issues - may need optimization or hardware upgrade")
        severity = "low"
    
    if "crack" in str(answers).lower() or "broken" in str(answers).lower():
        issues.append("Physical damage detected - hardware repair needed")
        severity = "high"
    
    if not issues:
        issues.append("Further in-person diagnosis recommended")
    
    return {
        "device_type": device,
        "issues_detected": issues,
        "severity": severity,
        "recommended_service": get_recommended_service(issues, severity),
        "estimated_time": estimate_repair_time(severity),
    }

def get_recommended_service(issues, severity):
    """Get recommended service type"""
    if severity == "high":
        return "in_person_priority"
    if "software" in str(issues).lower():
        return "remote_support"
    return "standard_diagnostic"

def estimate_repair_time(severity):
    """Estimate repair time"""
    times = {"low": "30-60 minutes", "medium": "1-2 hours", "high": "2-4 hours or more"}
    return times.get(severity, "1-2 hours")

def get_diagnostic_session(diag_id):
    """Get diagnostic session"""
    return DIAGNOSTIC_SESSIONS.get(diag_id)

