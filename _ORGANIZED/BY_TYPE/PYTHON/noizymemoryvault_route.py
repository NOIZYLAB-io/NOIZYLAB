"""NoizyMemoryVault API Routes"""
from fastapi import APIRouter
from ..noizymemoryvault.vault import store_text, store_image, store_audio, link_memories
from ..noizymemoryvault.query import query_memory, get_recent_memories
from ..noizymemoryvault.store import count_memories, load_all
from ..noizymemoryvault.index import get_index_size
from ..noizymemoryvault.graph import get_graph_size

router = APIRouter(prefix="/vault", tags=["NoizyMemoryVault"])

@router.post("/store")
def store(payload: dict):
    return {"id": store_text(payload["text"], payload.get("meta", {}))}

@router.post("/query")
def query(payload: dict):
    return query_memory(payload["prompt"], payload.get("top", 5))

@router.get("/recent")
def recent(limit: int = 20):
    return get_recent_memories(limit)

@router.post("/link")
def link(payload: dict):
    link_memories(payload["a"], payload["b"], payload.get("relation", "related"))
    return {"linked": True}

@router.get("/stats")
def stats():
    return {"memories": count_memories(), "indexed": get_index_size(), "graph_nodes": get_graph_size()}

@router.get("/all")
def all_memories():
    return load_all()

