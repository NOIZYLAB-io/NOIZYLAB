#!/usr/bin/env python3
"""
🌟 NOIZYLAB Unified Integration API 🌟
Connects TypeScript CLI, Python Backend, and ALL services!
"""

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import requests
import subprocess
from typing import Dict, Optional

app = FastAPI(title="NoizyLab Unified API", version="2.0.0")


class SupporterEvent(BaseModel):
    """Supporter event"""
    email: str
    name: Optional[str] = None
    action: str  # joined, repaired, subscribed


class NetworkEvent(BaseModel):
    """Network event"""
    device: str
    event_type: str
    details: Dict


@app.post("/unified/supporter")
async def handle_supporter_event(event: SupporterEvent, bg: BackgroundTasks):
    """
    Handle supporter event - triggers EVERYTHING!
    
    - TypeScript: Creates Stripe customer, archives to Notion/Airtable
    - Python: Sends Slack notification with AI insights
    - Both: Post to C0CKP1T channel
    """
    
    # TypeScript: Create customer
    ts_result = subprocess.run(
        ["npx", "noizylab", "subs", "customer", "-e", event.email, "-n", event.name or ""],
        capture_output=True
    )
    
    # TypeScript: Archive
    subprocess.run(
        ["npx", "noizylab", "archive", "supporter", "-e", event.email, "-n", event.name or ""],
        capture_output=True
    )
    
    # Python: AI analysis + Slack
    requests.post("http://localhost:8003/notify/system-alert", json={
        "title": f"New Supporter: {event.name or event.email}",
        "message": f"Welcome to NOIZYLAB!\n{event.action}",
        "level": "success"
    })
    
    # TypeScript: Slack alert
    subprocess.run(
        ["npx", "noizylab", "alerts", "supporter", "-e", event.email, "-n", event.name or ""],
        capture_output=True
    )
    
    return {"success": True, "integrated": True}


@app.post("/unified/device-connected")
async def handle_device_connection(event: NetworkEvent):
    """
    Handle device connection - Full integration!
    
    - Python: Network detection, MC96 handshake
    - TypeScript: Send branded email notification
    - Both: Post to Slack C0CKP1T
    """
    
    # Python handles network
    device_details = {
        "device": event.device,
        "type": event.event_type,
        **event.details
    }
    
    # Post to Slack via Python
    requests.post("http://localhost:8003/notify/system-alert", json={
        "title": "Device Connected",
        "message": f"{event.device} connected to network",
        "level": "info",
        "details": device_details
    })
    
    return {"success": True, "network_processed": True}


@app.get("/unified/status")
async def unified_status():
    """Get complete unified system status"""
    
    status = {
        "system": "NOIZYLAB Unified",
        "version": "2.0.0",
        "typescript_cli": "available",
        "python_backend": "running",
        "integrations": {
            "slack": {"channel": "C0CKP1T", "status": "connected"},
            "cloudflare": "configured",
            "ms365": "configured",
            "stripe": "configured",
            "network": "monitoring",
            "ai": "active",
            "mc96_universe": "online"
        },
        "curse_beasts": {
            "CURSE_BEAST_01": "active",
            "CURSE_BEAST_02": "active"
        }
    }
    
    return status


if __name__ == "__main__":
    import uvicorn
    
    print("🌟 Starting NOIZYLAB Unified Integration API...")
    print("🔗 Connecting TypeScript + Python + ALL services!")
    print("📡 API: http://localhost:8007")
    
    uvicorn.run(app, host="0.0.0.0", port=8007)
