#!/usr/bin/env python3
"""
Network Agent Service - Background service wrapper
==================================================
Runs DGS1210 agent as a background service with API interface
"""

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
import uvicorn
import time
from datetime import datetime
from pathlib import Path

from dgs1210_network_agent import DGS1210Agent

app = FastAPI(
    title="NoizyLab Network Agent API",
    description="API for DGS1210 network monitoring and device management",
    version="1.0.0"
)

# Global agent instance
agent: Optional[DGS1210Agent] = None


class AgentConfig(BaseModel):
    """Agent configuration"""
    switch_ip: str = "192.168.1.1"
    community: str = "public"
    interval: int = 5
    mc96_ports: List[int] = [1, 2, 3]


class HandshakeRequest(BaseModel):
    """Force handshake request"""
    port: int


@app.on_event("startup")
async def startup_event():
    """Initialize agent on startup"""
    global agent
    
    # Load configuration
    config = load_config()
    
    agent = DGS1210Agent(
        switch_ip=config.get("switch_ip", "192.168.1.1"),
        community=config.get("community", "public")
    )
    
    agent.mc96_ports = config.get("mc96_ports", [1, 2, 3])
    
    # Start monitoring
    agent.start_monitoring(interval=config.get("interval", 5))
    
    print("✅ Network Agent Service started")


@app.on_event("shutdown")
async def shutdown_event():
    """Stop agent on shutdown"""
    if agent:
        agent.stop_monitoring()
    print("✅ Network Agent Service stopped")


@app.get("/")
async def root():
    """Health check"""
    return {
        "service": "NoizyLab Network Agent",
        "status": "running",
        "monitoring": agent.monitoring if agent else False,
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    if not agent:
        return JSONResponse(
            status_code=503,
            content={"status": "unavailable", "error": "Agent not initialized"}
        )
    
    stats = agent.get_statistics()
    
    return {
        "status": "healthy",
        "monitoring": agent.monitoring,
        "switch_ip": agent.switch_ip,
        "statistics": stats,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/ports")
async def get_ports():
    """Get status of all ports"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    port_states = agent.get_port_status()
    
    # Convert to serializable format
    ports = {}
    for port, state in port_states.items():
        ports[port] = {
            "link_status": state["link_status"],
            "speed": state["speed"],
            "last_change": state["last_change"].isoformat(),
            "device": {
                "mac": state["device"].mac_address,
                "ip": state["device"].ip_address,
                "hostname": state["device"].hostname
            } if state["device"] else None
        }
    
    return {"ports": ports}


@app.get("/ports/{port}")
async def get_port(port: int):
    """Get status of specific port"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    if port < 1 or port > 10:
        return JSONResponse(status_code=400, content={"error": "Invalid port number"})
    
    state = agent.port_states.get(port)
    if not state:
        return JSONResponse(status_code=404, content={"error": "Port not found"})
    
    return {
        "port": port,
        "link_status": state["link_status"],
        "speed": state["speed"],
        "last_change": state["last_change"].isoformat(),
        "device": {
            "mac": state["device"].mac_address,
            "ip": state["device"].ip_address,
            "hostname": state["device"].hostname,
            "vendor": state["device"].vendor
        } if state["device"] else None
    }


@app.get("/devices")
async def get_devices():
    """Get all connected devices"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    devices = agent.get_connected_devices()
    
    return {
        "count": len(devices),
        "devices": [
            {
                "mac_address": d.mac_address,
                "ip_address": d.ip_address,
                "port": d.port,
                "hostname": d.hostname,
                "vendor": d.vendor,
                "device_type": d.device_type,
                "status": d.status,
                "first_seen": d.first_seen.isoformat(),
                "last_seen": d.last_seen.isoformat()
            }
            for d in devices
        ]
    }


@app.get("/mc96/devices")
async def get_mc96_devices():
    """Get MC96 devices"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    mc96_devices = agent.get_mc96_devices()
    
    return {
        "count": len(mc96_devices),
        "ports": agent.mc96_ports,
        "devices": {
            str(port): {
                "device": {
                    "mac": data["device"].mac_address,
                    "ip": data["device"].ip_address,
                    "hostname": data["device"].hostname
                },
                "handshake": {
                    "success": data["handshake"].success,
                    "type": data["handshake"].handshake_type,
                    "response_time": data["handshake"].response_time,
                    "details": data["handshake"].details
                },
                "registered": data["registered"].isoformat()
            }
            for port, data in mc96_devices.items()
        }
    }


@app.post("/handshake")
async def force_handshake(request: HandshakeRequest):
    """Force handshake on specific port"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    result = agent.force_handshake(request.port)
    
    if not result:
        return JSONResponse(
            status_code=404,
            content={"error": f"No device on port {request.port}"}
        )
    
    return {
        "success": result.success,
        "port": request.port,
        "device": {
            "mac": result.device.mac_address,
            "ip": result.device.ip_address,
            "hostname": result.device.hostname
        },
        "handshake_type": result.handshake_type,
        "response_time": result.response_time,
        "details": result.details,
        "timestamp": result.timestamp.isoformat()
    }


@app.get("/statistics")
async def get_statistics():
    """Get network statistics"""
    if not agent:
        return JSONResponse(status_code=503, content={"error": "Agent not initialized"})
    
    return agent.get_statistics()


@app.post("/config")
async def update_config(config: AgentConfig):
    """Update agent configuration"""
    global agent
    
    # Save configuration
    save_config(config.dict())
    
    # Restart agent with new config
    if agent:
        agent.stop_monitoring()
        time.sleep(1)
    
    agent = DGS1210Agent(
        switch_ip=config.switch_ip,
        community=config.community
    )
    agent.mc96_ports = config.mc96_ports
    agent.start_monitoring(interval=config.interval)
    
    return {"message": "Configuration updated", "config": config.dict()}


@app.get("/config")
async def get_config():
    """Get current configuration"""
    return load_config()


def load_config() -> Dict:
    """Load configuration from file"""
    config_file = Path(__file__).parent / "agent_config.json"
    
    if config_file.exists():
        import json
        with open(config_file) as f:
            return json.load(f)
    
    # Default configuration
    return {
        "switch_ip": "192.168.1.1",
        "community": "public",
        "interval": 5,
        "mc96_ports": [1, 2, 3]
    }


def save_config(config: Dict):
    """Save configuration to file"""
    config_file = Path(__file__).parent / "agent_config.json"
    
    import json
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    print("🚀 Starting Network Agent Service...")
    print("📡 API will be available at http://localhost:8005")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8005,
        log_level="info"
    )

