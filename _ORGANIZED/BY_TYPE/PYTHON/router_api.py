from fastapi import APIRouter
from .brain_router import route

router = APIRouter()


@router.post("/")
def ai_entry(payload: dict):
    inp = payload.get("input", "")
    return route(inp)

