from fastapi import APIRouter

router = APIRouter()

# Import shared clients
clients = {}


@router.post("/newsession")
def newsession(payload: dict):
    email = payload["email"]
    issue = payload["issue"]
    
    if email not in clients:
        clients[email] = {"email": email, "sessions": [], "history": []}
    
    clients[email]["sessions"].append({"issue": issue, "status": "active"})
    return {"ok": True}


@router.get("/sessions/{email}")
def get_sessions(email: str):
    if email in clients:
        return {"sessions": clients[email].get("sessions", [])}
    return {"sessions": []}


@router.post("/close/{email}")
def close_session(email: str, payload: dict):
    if email in clients:
        sessions = clients[email].get("sessions", [])
        # Move to history
        for s in sessions:
            if s["issue"] == payload.get("issue"):
                s["status"] = "closed"
                clients[email]["history"].append({
                    "date": "now",
                    "summary": s["issue"]
                })
        return {"ok": True}
    return {"ok": False}

