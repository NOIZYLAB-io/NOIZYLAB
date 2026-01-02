#!/usr/bin/env python3
"""
Noizy Core Service - v5 Gateway
Runs on port 8010 as the main service gateway
"""

import os, sys, time
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

app = FastAPI(title="Noizy Core v5 Gateway", version="5.0")

@app.get("/")
async def gateway_root():
    return {
        "service": "noizy-core-v5",
        "status": "operational",
        "port": 8010,
        "timestamp": time.time(),
        "version": "5.0",
        "endpoints": {
            "health": "/health",
            "status": "/status",
            "gateway": "/",
            "transport": "http://127.0.0.1:8123/health"
        }
    }

@app.get("/health")
async def gateway_health():
    return {
        "status": "healthy",
        "service": "core-gateway",
        "timestamp": time.time(),
        "dependencies": {
            "uap_transport": "http://127.0.0.1:8123/health",
            "mission_control": "http://127.0.0.1:8765/",
            "admin_panel": "http://127.0.0.1:8000/admin"
        }
    }

@app.get("/status")
async def gateway_status():
    return {
        "core_services": {
            "gateway": "running",
            "transport": "check_8123",
            "mission_control": "check_8765",
            "admin": "check_8000"
        },
        "system": {
            "hp_omen": "connected",
            "dell_inspiron_7779": "connected", 
            "planar_2495": "connected"
        }
    }

if __name__ == "__main__":
    print("🚀 Starting Noizy Core v5 Gateway on port 8010...")
    uvicorn.run(app, host="127.0.0.1", port=8010)