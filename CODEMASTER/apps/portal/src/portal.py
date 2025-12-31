#!/usr/bin/env python3
"""
🖥️ CODEMASTER PORTAL 🖥️
========================
TeamViewer-style web UI for:
- Vault search & browse
- Evidence pack viewer
- Fleet device dashboard
- MC96 network control
- AI assistant chat

All actions produce Evidence Packs!
"""

import os
import json
import httpx
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

PORTAL_ROOT = Path(__file__).parent.parent
STATIC_DIR = PORTAL_ROOT / "static"
TEMPLATES_DIR = PORTAL_ROOT / "templates"

# Service URLs (internal Docker network or localhost)
SERVICES = {
    "vault":    os.environ.get("VAULT_URL", "http://localhost:8000"),
    "catalog":  os.environ.get("CATALOG_URL", "http://localhost:8001"),
    "evidence": os.environ.get("EVIDENCE_URL", "http://localhost:8002"),
    "ai":       os.environ.get("AI_GATEWAY_URL", "http://localhost:8100"),
    "fleet":    os.environ.get("FLEET_URL", "http://localhost:8200"),
    "mc96":     os.environ.get("MC96_URL", "http://localhost:8300"),
}

# ═══════════════════════════════════════════════════════════════
# 🔧 HTTP CLIENT
# ═══════════════════════════════════════════════════════════════

http_client: Optional[httpx.AsyncClient] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage HTTP client lifecycle"""
    global http_client
    http_client = httpx.AsyncClient(timeout=30.0)
    yield
    await http_client.aclose()


async def service_call(service: str, method: str, path: str, 
                       data: Dict = None, params: Dict = None) -> Dict:
    """Make a call to a backend service"""
    if service not in SERVICES:
        raise HTTPException(status_code=400, detail=f"Unknown service: {service}")
    
    url = f"{SERVICES[service]}{path}"
    
    try:
        if method == "GET":
            response = await http_client.get(url, params=params)
        elif method == "POST":
            response = await http_client.post(url, json=data)
        elif method == "PUT":
            response = await http_client.put(url, json=data)
        elif method == "DELETE":
            response = await http_client.delete(url)
        else:
            raise HTTPException(status_code=400, detail=f"Unknown method: {method}")
        
        if response.status_code >= 400:
            return {"error": response.text, "status": response.status_code}
        
        return response.json()
    except httpx.ConnectError:
        return {"error": f"Service {service} unavailable", "status": 503}
    except Exception as e:
        return {"error": str(e), "status": 500}


# ═══════════════════════════════════════════════════════════════
# 🚀 FASTAPI APP
# ═══════════════════════════════════════════════════════════════

app = FastAPI(
    title="🖥️ CODEMASTER Portal",
    version="0.1.0",
    lifespan=lifespan,
)

# Static files and templates
STATIC_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# ═══════════════════════════════════════════════════════════════
# 📄 PAGE ROUTES
# ═══════════════════════════════════════════════════════════════

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Main dashboard"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "CODEMASTER Portal",
        "services": SERVICES,
    })


@app.get("/vault", response_class=HTMLResponse)
async def vault_page(request: Request):
    """Vault browser"""
    return templates.TemplateResponse("vault.html", {
        "request": request,
        "title": "Vault Browser",
    })


@app.get("/evidence", response_class=HTMLResponse)
async def evidence_page(request: Request):
    """Evidence pack viewer"""
    return templates.TemplateResponse("evidence.html", {
        "request": request,
        "title": "Evidence Packs",
    })


@app.get("/fleet", response_class=HTMLResponse)
async def fleet_page(request: Request):
    """Fleet device dashboard"""
    return templates.TemplateResponse("fleet.html", {
        "request": request,
        "title": "Fleet Dashboard",
    })


@app.get("/network", response_class=HTMLResponse)
async def network_page(request: Request):
    """MC96 network control"""
    return templates.TemplateResponse("network.html", {
        "request": request,
        "title": "Network Control",
    })


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    """AI assistant chat"""
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "title": "AI Assistant",
    })


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - Health & Status
# ═══════════════════════════════════════════════════════════════

@app.get("/health")
async def health():
    """Portal health check"""
    return {"status": "ok", "service": "portal"}


@app.get("/api/status")
async def status():
    """Get status of all services"""
    status_map = {}
    
    for name, url in SERVICES.items():
        try:
            response = await http_client.get(f"{url}/health", timeout=5.0)
            status_map[name] = {
                "status": "online" if response.status_code == 200 else "error",
                "url": url,
            }
        except:
            status_map[name] = {"status": "offline", "url": url}
    
    return {
        "portal": "online",
        "services": status_map,
        "timestamp": datetime.now().isoformat(),
    }


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - Vault
# ═══════════════════════════════════════════════════════════════

@app.get("/api/vault/search")
async def vault_search(q: str, limit: int = 20):
    """Search vault assets"""
    result = await service_call("catalog", "GET", "/assets/search", params={"q": q, "limit": limit})
    return result


@app.get("/api/vault/recent")
async def vault_recent(limit: int = 20):
    """Get recent vault assets"""
    result = await service_call("catalog", "GET", "/assets/recent", params={"limit": limit})
    return result


@app.get("/api/vault/stats")
async def vault_stats():
    """Get vault statistics"""
    result = await service_call("catalog", "GET", "/stats")
    return result


@app.get("/api/vault/asset/{asset_id}")
async def vault_asset(asset_id: str):
    """Get asset details"""
    result = await service_call("catalog", "GET", f"/assets/{asset_id}")
    return result


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - Evidence
# ═══════════════════════════════════════════════════════════════

@app.get("/api/evidence/packs")
async def evidence_list(limit: int = 50):
    """List evidence packs"""
    result = await service_call("evidence", "GET", "/packs", params={"limit": limit})
    return result


@app.get("/api/evidence/pack/{pack_id}")
async def evidence_get(pack_id: str):
    """Get evidence pack details"""
    result = await service_call("evidence", "GET", f"/packs/{pack_id}")
    return result


@app.post("/api/evidence/verify/{pack_id}")
async def evidence_verify(pack_id: str):
    """Verify an evidence pack"""
    result = await service_call("evidence", "POST", f"/packs/{pack_id}/verify")
    return result


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - Fleet
# ═══════════════════════════════════════════════════════════════

@app.get("/api/fleet/devices")
async def fleet_devices(state: str = None):
    """List fleet devices"""
    params = {"state": state} if state else {}
    result = await service_call("fleet", "GET", "/devices", params=params)
    return result


@app.get("/api/fleet/device/{device_id}")
async def fleet_device(device_id: str):
    """Get device details"""
    result = await service_call("fleet", "GET", f"/devices/{device_id}")
    return result


@app.get("/api/fleet/sessions")
async def fleet_sessions():
    """Get active sessions"""
    result = await service_call("fleet", "GET", "/sessions/active")
    return result


@app.post("/api/fleet/session/start/{device_id}")
async def fleet_session_start(device_id: str, user_id: str = None):
    """Start a remote session"""
    result = await service_call("fleet", "POST", f"/sessions/start/{device_id}", 
                               data={"user_id": user_id})
    return result


@app.post("/api/fleet/session/end/{session_id}")
async def fleet_session_end(session_id: str):
    """End a remote session"""
    result = await service_call("fleet", "POST", f"/sessions/{session_id}/end")
    return result


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - MC96 Network
# ═══════════════════════════════════════════════════════════════

@app.get("/api/network/devices")
async def network_devices(device_type: str = None):
    """List network devices"""
    params = {"device_type": device_type} if device_type else {}
    result = await service_call("mc96", "GET", "/devices", params=params)
    return result


@app.get("/api/network/device/{device_id}")
async def network_device(device_id: str):
    """Get network device details"""
    result = await service_call("mc96", "GET", f"/devices/{device_id}")
    return result


@app.get("/api/network/runbooks")
async def network_runbooks():
    """List available runbooks"""
    result = await service_call("mc96", "GET", "/runbooks")
    return result


@app.post("/api/network/runbook/{runbook_name}")
async def network_run_runbook(runbook_name: str, target_devices: List[str] = None, 
                              parameters: Dict = None):
    """Execute a network runbook"""
    result = await service_call("mc96", "POST", f"/runbooks/{runbook_name}/execute",
                               data={"target_devices": target_devices, "parameters": parameters})
    return result


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES - AI Chat
# ═══════════════════════════════════════════════════════════════

from pydantic import BaseModel

class ChatMessage(BaseModel):
    message: str
    system: Optional[str] = None

@app.post("/api/ai/chat")
async def ai_chat(body: ChatMessage):
    """Send message to AI"""
    result = await service_call("ai", "POST", "/reason", 
                               data={"prompt": body.message, "system": body.system})
    return result


@app.get("/api/ai/stats")
async def ai_stats():
    """Get AI gateway stats"""
    result = await service_call("ai", "GET", "/stats")
    return result


# ═══════════════════════════════════════════════════════════════
# 🔌 WEBSOCKET - Real-time updates
# ═══════════════════════════════════════════════════════════════

class ConnectionManager:
    """WebSocket connection manager"""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: Dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time updates"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            
            # Handle different message types
            if data.get("type") == "ping":
                await websocket.send_json({"type": "pong"})
            
            elif data.get("type") == "subscribe":
                # Subscribe to updates for a resource
                channel = data.get("channel")
                await websocket.send_json({"type": "subscribed", "channel": channel})
            
            elif data.get("type") == "chat":
                # AI chat message
                message = data.get("message", "")
                result = await service_call("ai", "POST", "/reason", 
                                           data={"prompt": message})
                await websocket.send_json({
                    "type": "chat_response",
                    "content": result.get("content", ""),
                    "error": result.get("error"),
                })
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# ═══════════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    import uvicorn
    import argparse
    
    parser = argparse.ArgumentParser(description='🖥️ CODEMASTER Portal')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--reload', action='store_true')
    
    args = parser.parse_args()
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  🖥️  CODEMASTER PORTAL                                        ║
║                                                               ║
║  Starting on http://{args.host}:{args.port}                          ║
║                                                               ║
║  Pages:                                                       ║
║    /         - Dashboard                                      ║
║    /vault    - Vault Browser                                  ║
║    /evidence - Evidence Packs                                 ║
║    /fleet    - Fleet Devices                                  ║
║    /network  - Network Control                                ║
║    /chat     - AI Assistant                                   ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "portal:app" if args.reload else app,
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
