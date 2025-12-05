"""NoizyBrain++ API Routes"""
from fastapi import APIRouter
from ..noizybrain.brain import think, get_brain, BRAIN
from ..noizybrain.cognitive_graph import get_graph, add_concept, related
from ..noizybrain.router import get_all_geniuses

router = APIRouter(prefix="/brain", tags=["NoizyBrain"])

@router.post("/think")
def think_endpoint(payload: dict):
    return think(payload.get("state", {}), payload.get("memory", []), payload.get("events", []))

@router.get("/history")
def get_history(limit: int = 20):
    return get_brain().get_thought_history(limit)

@router.get("/intentions")
def get_intentions():
    return get_brain().get_pending_intentions()

@router.get("/geniuses")
def get_geniuses():
    return get_all_geniuses()

@router.get("/graph")
def get_cognitive_graph():
    return get_graph()

@router.post("/graph/add")
def add_to_graph(payload: dict):
    add_concept(payload["a"], payload["b"], payload.get("weight", 1.0), payload.get("relation", "related"))
    return {"added": True}

@router.get("/graph/related/{concept}")
def get_related(concept: str):
    return related(concept)

@router.get("/status")
def brain_status():
    brain = get_brain()
    return {"thoughts": len(brain.thought_history), "pending_intentions": len(brain.intention_queue), "status": "thinking"}

