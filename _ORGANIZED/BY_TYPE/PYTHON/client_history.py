from fastapi import APIRouter

router = APIRouter()

# Import shared clients
clients = {}


@router.get("/history/{email}")
def get_history(email: str):
    if email in clients:
        return {"history": clients[email].get("history", [])}
    return {"history": []}


@router.post("/add/{email}")
def add_history(email: str, payload: dict):
    if email not in clients:
        clients[email] = {"email": email, "sessions": [], "history": []}
    
    clients[email]["history"].append({
        "date": payload.get("date", "now"),
        "summary": payload.get("summary", "Repair completed"),
        "job_id": payload.get("job_id", "N/A")
    })
    return {"ok": True}

