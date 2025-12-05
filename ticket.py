"""NoizyFrontDesk - Ticket System"""
import uuid
from datetime import datetime

TICKET_DB = {}

def create_ticket(data):
    """Create a support ticket"""
    ticket_id = f"TKT-{uuid.uuid4().hex[:8].upper()}"
    
    ticket = {
        "id": ticket_id,
        "customer_name": data.get("customer_name"),
        "customer_email": data.get("customer_email"),
        "customer_phone": data.get("customer_phone"),
        "device_type": data.get("device_type"),
        "issue": data.get("issue"),
        "prediagnostic": data.get("prediagnostic"),
        "booking_id": data.get("booking_id"),
        "status": "open",
        "priority": determine_priority(data),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "assigned_to": None,
        "notes": [],
        "timeline": [{"action": "created", "timestamp": datetime.now().isoformat()}],
    }
    TICKET_DB[ticket_id] = ticket
    return ticket

def determine_priority(data):
    """Determine ticket priority"""
    issue = str(data.get("issue", "")).lower()
    prediag = data.get("prediagnostic", {})
    
    if prediag.get("severity") == "high":
        return "high"
    if "urgent" in issue or "emergency" in issue or "not working" in issue:
        return "high"
    if "slow" in issue:
        return "low"
    return "medium"

def get_ticket(ticket_id):
    """Get ticket by ID"""
    return TICKET_DB.get(ticket_id)

def update_ticket(ticket_id, updates):
    """Update a ticket"""
    if ticket_id not in TICKET_DB:
        return None
    TICKET_DB[ticket_id].update(updates)
    TICKET_DB[ticket_id]["updated_at"] = datetime.now().isoformat()
    TICKET_DB[ticket_id]["timeline"].append({
        "action": "updated",
        "changes": list(updates.keys()),
        "timestamp": datetime.now().isoformat(),
    })
    return TICKET_DB[ticket_id]

def add_note(ticket_id, note, author="system"):
    """Add note to ticket"""
    if ticket_id not in TICKET_DB:
        return None
    TICKET_DB[ticket_id]["notes"].append({
        "text": note,
        "author": author,
        "timestamp": datetime.now().isoformat(),
    })
    return TICKET_DB[ticket_id]

def close_ticket(ticket_id, resolution):
    """Close a ticket"""
    if ticket_id not in TICKET_DB:
        return None
    TICKET_DB[ticket_id]["status"] = "closed"
    TICKET_DB[ticket_id]["resolution"] = resolution
    TICKET_DB[ticket_id]["closed_at"] = datetime.now().isoformat()
    TICKET_DB[ticket_id]["timeline"].append({
        "action": "closed",
        "resolution": resolution,
        "timestamp": datetime.now().isoformat(),
    })
    return TICKET_DB[ticket_id]

def get_open_tickets():
    """Get all open tickets"""
    return [t for t in TICKET_DB.values() if t["status"] == "open"]

def get_tickets_by_priority(priority):
    """Get tickets by priority"""
    return [t for t in TICKET_DB.values() if t["priority"] == priority and t["status"] == "open"]

def search_tickets(query):
    """Search tickets"""
    query = query.lower()
    return [t for t in TICKET_DB.values() 
            if query in t.get("customer_name", "").lower()
            or query in t.get("issue", "").lower()
            or query in t["id"].lower()]

