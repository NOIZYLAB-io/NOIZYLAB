#!/usr/bin/env python3
"""
MCP Server for Mission Control 96
Provides HTTP API endpoints for system interaction
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from typing import Dict, Any, Optional
import logging

# Import mission control
from mission_control import mission_control

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Mission Control 96 MCP Server",
    description="Model Context Protocol server for Mission Control",
    version="1.0.0"
)


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