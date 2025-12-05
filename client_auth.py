from fastapi import APIRouter

router = APIRouter()

# Shared client store
clients = {}


@router.post("/register")
def register(payload: dict):
    email = payload["email"]
    clients[email] = {
        "email": email,
        "pass": payload["pass"],
        "sessions": [],
        "history": []
    }
    return {"ok": True, "client": {"email": email}}


@router.post("/login")
def login(payload: dict):
    email = payload["email"]
    if email in clients and clients[email]["pass"] == payload["pass"]:
        return {"ok": True, "client": {"email": email}}
    return {"ok": False, "error": "Invalid credentials"}


@router.get("/profile/{email}")
def get_profile(email: str):
    if email in clients:
        return {"ok": True, "client": clients[email]}
    return {"ok": False, "error": "Not found"}

