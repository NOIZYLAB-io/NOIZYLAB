#!/usr/bin/env python3
"""
Noizy Mind Service - UAP Transport
Runs on port 8123 for UAP (Unified Agent Protocol) transport
"""

import os, sys, time
from pathlib import Path
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import uvicorn
import asyncio

# Add parent directory to path for imports  
sys.path.append(str(Path(__file__).parent.parent))

app = FastAPI(title="Noizy Mind UAP Transport", version="1.0")

# Active connections for UAP transport
connections = []

@app.get("/")
async def mind_root():
    return {
        "service": "noizy-mind-uap",
        "status": "operational", 
        "port": 8123,
        "timestamp": time.time(),
        "protocol": "UAP",
        "endpoints": {
            "health": "/health",
            "transport": "/ws",
            "agents": "/agents",
            "gateway": "http://127.0.0.1:8010/"
        }
    }

@app.get("/health")
async def mind_health():
    return {
        "status": "healthy",
        "service": "uap-transport",
        "timestamp": time.time(),
        "active_connections": len(connections),
        "agent_status": {
            "mission_control": "active",
            "claude_integration": "ready",
            "websocket_transport": "operational"
        }
    }

@app.get("/agents")
async def agent_status():
    return {
        "active_agents": 5,
        "agent_types": [
            "data_analyst",
            "system_optimizer", 
            "security_monitor",
            "performance_tracker",
            "automation_controller"
        ],
        "transport_protocol": "UAP",
        "connection_count": len(connections)
    }

@app.websocket("/ws")
async def websocket_transport(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            # UAP transport protocol
            data = await websocket.receive_text()
            # Echo back with UAP envelope
            response = {
                "uap_envelope": {
                    "timestamp": time.time(),
                    "service": "mind-transport",
                    "data": data,
                    "status": "processed"
                }
            }
            await websocket.send_json(response)
    except WebSocketDisconnect:
        connections.remove(websocket)

if __name__ == "__main__":
    print("🧠 Starting Noizy Mind UAP Transport on port 8123...")
    uvicorn.run(app, host="127.0.0.1", port=8123)