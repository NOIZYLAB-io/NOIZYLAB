# ──────────────────────────────────────────────────────────────────────────────
# FILE: mcp_server.py (Self-Locating, Auto-Launcher, VS-Ready)
# ──────────────────────────────────────────────────────────────────────────────
"""
MCP Server — FastAPI Bridge for Mission Control 96 (Universal Launcher)

Features:
- Works from any directory; automatically locates itself.
- POST /publish — agents post events.
- GET /fetch/{topic} — agents retrieve events.
- Optional WebSocket /stream endpoint (for future live streaming).
- Drop-in MCPClient class replaces EventBus in Mission Control.
- Built-in launcher; just run `python mcp_server.py` from anywhere.

Run:
  pip install fastapi uvicorn pydantic requests
  python mcp_server.py

This will automatically start Uvicorn on port 8765.
"""

# --- Self-locating bootstrap -----------------------------------------------
import os, sys, json, time, threading
from typing import Any, Dict, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)
os.chdir(CURRENT_DIR)

# ----------------------------------------------------------------------------
# Event schema
# ----------------------------------------------------------------------------
class Event(BaseModel):
    topic: str
    payload: Dict[str, Any]

class BatchEvent(BaseModel):
    events: List[Dict[str, Any]]

# ----------------------------------------------------------------------------
# In-memory event store (thread-safe ring buffer)
# ----------------------------------------------------------------------------
class MemoryStore:
    def __init__(self, limit: int = 4000):
        self.lock = threading.Lock()
        self.events: List[Dict[str, Any]] = []
        self.limit = limit

    def add(self, topic: str, payload: Dict[str, Any]):
        with self.lock:
            event = {"ts": time.time(), "topic": topic, "payload": payload}
            self.events.append(event)
            if len(self.events) > self.limit:
                self.events.pop(0)

    def add_batch(self, events: List[Dict[str, Any]]):
        with self.lock:
            for event_data in events:
                event = {
                    "ts": time.time(), 
                    "topic": event_data["topic"], 
                    "payload": event_data["payload"]
                }
                self.events.append(event)
            while len(self.events) > self.limit:
                self.events.pop(0)

    def fetch(self, topic: str) -> List[Dict[str, Any]]:
        with self.lock:
            return [e for e in self.events if e["topic"] == topic]

    def fetch_since(self, topic: str, since_ts: float) -> List[Dict[str, Any]]:
        with self.lock:
            return [e for e in self.events if e["topic"] == topic and e["ts"] >= since_ts]

store = MemoryStore(limit=4000)

# ----------------------------------------------------------------------------
# FastAPI app setup
# ----------------------------------------------------------------------------
app = FastAPI(title="Mission Control MCP Server", version="1.1")


class EventMessage(BaseModel):
    topic: str
    payload: Dict[str, Any]


class StatusResponse(BaseModel):
    status: str
    data: Optional[Dict[str, Any]] = None


@app.on_event("startup")
async def startup_event():
    """Initialize Mission Control on startup"""
    logger.info("Starting MCP Server...")
    mission_control.start()


@app.on_event("shutdown") 
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down MCP Server...")
    mission_control.stop()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Mission Control 96 MCP Server", "status": "operational"}


@app.get("/status")
async def get_status():
    """Get system status"""
    try:
        status = mission_control.get_status()
        return StatusResponse(status="success", data=status)
    except Exception as e:
        logger.error(f"Status error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/publish")
async def publish_event(event: EventMessage):
    """Publish an event to the system"""
    try:
        mission_control.bus.publish(event.topic, event.payload)
        return StatusResponse(status="published")
    except Exception as e:
        logger.error(f"Publish error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/events/{topic}")
async def get_events(topic: str):
    """Get events from a topic"""
    try:
        events = mission_control.bus.fetch(topic)
        return StatusResponse(status="success", data={"events": events})
    except Exception as e:
        logger.error(f"Events error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/agents/{agent_name}/activate")
async def activate_agent(agent_name: str):
    """Activate an agent"""
    try:
        if agent_name not in mission_control.agents:
            raise HTTPException(status_code=404, detail=f"Agent {agent_name} not found")
        
        mission_control.agents[agent_name].activate()
        return StatusResponse(status="activated")
    except Exception as e:
        logger.error(f"Activate error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/agents/{agent_name}/deactivate")
async def deactivate_agent(agent_name: str):
    """Deactivate an agent"""
    try:
        if agent_name not in mission_control.agents:
            raise HTTPException(status_code=404, detail=f"Agent {agent_name} not found")
        
        mission_control.agents[agent_name].deactivate()
        return StatusResponse(status="deactivated")
    except Exception as e:
        logger.error(f"Deactivate error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8765)