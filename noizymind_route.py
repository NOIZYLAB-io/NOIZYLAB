"""
NoizyMind API Routes
====================
Exposes memory search, planning, agent synthesis, and thought inspection.
"""

from fastapi import APIRouter, Query
from typing import Optional
from ..noizymind.encoder import (
    store_memory, 
    search_memory, 
    get_recent_memories,
    get_memory_stats,
)
from ..noizymind.planner import (
    generate_plan,
    generate_daily_plan,
    generate_weekly_goals,
)
from ..noizymind.multi_agent import (
    agent_synth,
    run_all_agents,
    get_all_recommendations,
)
from ..noizymind.synth import (
    synthesize,
    full_synthesis,
    debate_and_decide,
)
from ..noizymind.thinker import get_thinker


router = APIRouter()


# === MEMORY ENDPOINTS ===

@router.get("/mind/search")
def search(q: str, top: int = 5, type: Optional[str] = None):
    """
    Semantic search through NoizyMind memory.
    """
    return search_memory(q, top=top, type_filter=type)


@router.post("/mind/store")
def remember(payload: dict):
    """
    Store a new memory.
    """
    text = payload.get("text", "")
    meta = payload.get("meta", {})
    memory = store_memory(text, meta)
    return {"ok": True, "id": memory["id"]}


@router.get("/mind/recent")
def recent(n: int = 10, type: Optional[str] = None):
    """
    Get recent memories.
    """
    return get_recent_memories(n, type_filter=type)


@router.get("/mind/stats")
def stats():
    """
    Get memory database statistics.
    """
    return get_memory_stats()


# === PLANNING ENDPOINTS ===

@router.post("/mind/plan")
def plan(payload: dict):
    """
    Generate a task plan based on context.
    """
    return {"tasks": generate_plan(payload)}


@router.get("/mind/daily")
def daily_plan():
    """
    Get daily maintenance plan.
    """
    return generate_daily_plan({})


@router.get("/mind/weekly")
def weekly_goals():
    """
    Get weekly improvement goals.
    """
    return {"goals": generate_weekly_goals({})}


# === MULTI-AGENT ENDPOINTS ===

@router.post("/mind/agents")
def agents(payload: dict):
    """
    Run all agents and get their analyses.
    """
    outputs = agent_synth(payload)
    decision = synthesize(outputs)
    return {
        "agents": outputs,
        "decision": decision,
    }


@router.post("/mind/agents/full")
def agents_full(payload: dict):
    """
    Get full agent analysis with detailed results.
    """
    return run_all_agents(payload)


@router.post("/mind/agents/recommendations")
def agent_recommendations(payload: dict):
    """
    Get all recommendations from all agents.
    """
    return {"recommendations": get_all_recommendations(payload)}


# === SYNTHESIS ENDPOINTS ===

@router.post("/mind/synthesize")
def synth(payload: dict):
    """
    Full synthesis with decision making.
    """
    return full_synthesis(payload)


@router.post("/mind/debate")
def debate(payload: dict):
    """
    Simulate agent debate and consensus.
    """
    return debate_and_decide(payload)


# === THINKER ENDPOINTS ===

@router.get("/mind/thinker/status")
def thinker_status():
    """
    Get continuous thinker status.
    """
    thinker = get_thinker()
    if thinker:
        return thinker.get_status()
    return {"running": False, "message": "Thinker not started"}


@router.get("/mind/thoughts")
def get_thoughts(n: int = 10):
    """
    Get recent thoughts from the thinker.
    """
    return get_recent_memories(n, type_filter="thought")


@router.get("/mind/insights")
def get_insights(n: int = 10):
    """
    Get recent insights from pattern detection.
    """
    return get_recent_memories(n, type_filter="insight")

