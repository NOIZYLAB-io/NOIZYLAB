"""NoizyEconomy - Automated Client Intake"""
import uuid
from datetime import datetime

INTAKE_DB = {}

def auto_intake_client(data):
    """Automatically intake a new client"""
    client_id = str(uuid.uuid4())
    intake = {
        "id": client_id,
        "name": data.get("name", "Unknown"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "device_type": data.get("device_type"),
        "issue_description": data.get("issue_description"),
        "urgency": data.get("urgency", "normal"),
        "source": data.get("source", "website"),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "auto_responses_sent": [],
        "estimated_value": estimate_job_value(data),
    }
    INTAKE_DB[client_id] = intake
    
    # Auto-send confirmation
    send_intake_confirmation(intake)
    
    return intake

def estimate_job_value(data):
    """Estimate job value based on device and issue"""
    base_values = {
        "laptop": 150,
        "desktop": 175,
        "server": 300,
        "network": 200,
        "phone": 100,
        "tablet": 100,
    }
    device = data.get("device_type", "laptop").lower()
    base = base_values.get(device, 150)
    
    # Urgency multiplier
    if data.get("urgency") == "critical":
        base *= 1.5
    elif data.get("urgency") == "high":
        base *= 1.25
    
    return base

def send_intake_confirmation(intake):
    """Send automatic confirmation to client"""
    intake["auto_responses_sent"].append({
        "type": "intake_confirmation",
        "sent_at": datetime.now().isoformat(),
        "channel": "email" if intake.get("email") else "sms",
    })

def get_pending_intakes():
    """Get all pending intakes"""
    return [i for i in INTAKE_DB.values() if i["status"] == "pending"]

def approve_intake(client_id):
    """Approve an intake and move to scheduling"""
    if client_id in INTAKE_DB:
        INTAKE_DB[client_id]["status"] = "approved"
        return INTAKE_DB[client_id]
    return None

def get_intake(client_id):
    """Get intake by ID"""
    return INTAKE_DB.get(client_id)

