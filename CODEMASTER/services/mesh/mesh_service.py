#!/usr/bin/env python3
"""
🖥️ CODEMASTER MESH SERVICE 🖥️
==============================
MeshCentral integration for remote control.

Features:
- MeshCentral API client
- Device group management
- Remote desktop sessions
- File transfer
- Terminal access
- Power actions
- Evidence pack integration

Every action creates Evidence!
"""

import os
import json
import httpx
import hashlib
import asyncio
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

MESH_URL = os.environ.get("MESH_URL", "https://localhost")
MESH_USER = os.environ.get("MESH_USER", "admin")
MESH_PASSWORD = os.environ.get("MESH_PASSWORD", "")
MESH_LOGIN_KEY = os.environ.get("MESH_LOGIN_KEY", "")  # Alternative to password

EVIDENCE_SERVICE = os.environ.get("EVIDENCE_URL", "http://localhost:8002")

# ═══════════════════════════════════════════════════════════════
# 📊 MODELS
# ═══════════════════════════════════════════════════════════════

class MeshDevice(BaseModel):
    """MeshCentral device"""
    id: str
    name: str
    host: Optional[str] = None
    os: Optional[str] = None
    agent_version: Optional[str] = None
    connected: bool = False
    last_connect: Optional[str] = None
    group_id: Optional[str] = None
    group_name: Optional[str] = None


class MeshGroup(BaseModel):
    """MeshCentral device group"""
    id: str
    name: str
    desc: Optional[str] = None
    device_count: int = 0


class SessionRequest(BaseModel):
    """Remote session request"""
    device_id: str
    session_type: str = Field(default="desktop", 
                              description="desktop, terminal, or files")
    user_id: Optional[str] = None


class FileTransferRequest(BaseModel):
    """File transfer request"""
    device_id: str
    action: str = Field(description="download or upload")
    remote_path: str
    local_path: Optional[str] = None


class PowerAction(BaseModel):
    """Power action request"""
    device_id: str
    action: str = Field(description="restart, shutdown, sleep, or wake")


# ═══════════════════════════════════════════════════════════════
# 🔌 MESHCENTRAL CLIENT
# ═══════════════════════════════════════════════════════════════

class MeshCentralClient:
    """Client for MeshCentral API"""
    
    def __init__(self, url: str, user: str, password: str = None, login_key: str = None):
        self.url = url.rstrip('/')
        self.user = user
        self.password = password
        self.login_key = login_key
        self.client = httpx.AsyncClient(verify=False, timeout=30.0)  # Self-signed certs
        self.token = None
        self.session_id = None
    
    async def close(self):
        await self.client.aclose()
    
    async def authenticate(self) -> bool:
        """Authenticate with MeshCentral"""
        try:
            if self.login_key:
                # Use login key (preferred)
                response = await self.client.post(
                    f"{self.url}/api/login",
                    json={"loginkey": self.login_key}
                )
            else:
                # Use username/password
                response = await self.client.post(
                    f"{self.url}/api/login",
                    json={"user": self.user, "pass": self.password}
                )
            
            if response.status_code == 200:
                data = response.json()
                self.token = data.get("token")
                self.session_id = response.cookies.get("meshcentral")
                return True
            return False
            
        except Exception as e:
            print(f"❌ Auth error: {e}")
            return False
    
    def _headers(self) -> Dict[str, str]:
        """Get headers with auth token"""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["x-meshcentral-token"] = self.token
        return headers
    
    async def api_call(self, action: str, data: Dict = None) -> Dict:
        """Make an API call to MeshCentral"""
        try:
            payload = {"action": action}
            if data:
                payload.update(data)
            
            response = await self.client.post(
                f"{self.url}/api/",
                headers=self._headers(),
                json=payload
            )
            
            if response.status_code == 200:
                return response.json()
            return {"error": response.text, "status": response.status_code}
            
        except Exception as e:
            return {"error": str(e)}
    
    # ─────────────────────────────────────────────────────────
    # Device Operations
    # ─────────────────────────────────────────────────────────
    
    async def get_devices(self) -> List[Dict]:
        """Get all devices"""
        result = await self.api_call("meshes")
        
        devices = []
        meshes = result.get("meshes", {})
        
        for mesh_id, mesh in meshes.items():
            nodes = await self.api_call("nodes", {"meshid": mesh_id})
            
            for node_id, node in nodes.get("nodes", {}).items():
                devices.append({
                    "id": node_id,
                    "name": node.get("name", "Unknown"),
                    "host": node.get("host"),
                    "os": node.get("osdesc"),
                    "agent_version": node.get("agent"),
                    "connected": node.get("conn", 0) > 0,
                    "last_connect": node.get("lastconnect"),
                    "group_id": mesh_id,
                    "group_name": mesh.get("name"),
                })
        
        return devices
    
    async def get_device(self, device_id: str) -> Optional[Dict]:
        """Get single device details"""
        result = await self.api_call("nodes", {"nodeid": device_id})
        node = result.get("nodes", {}).get(device_id)
        
        if node:
            return {
                "id": device_id,
                "name": node.get("name"),
                "host": node.get("host"),
                "os": node.get("osdesc"),
                "agent_version": node.get("agent"),
                "connected": node.get("conn", 0) > 0,
                "hardware": node.get("hardware"),
                "ip_addresses": node.get("ip"),
            }
        return None
    
    async def get_groups(self) -> List[Dict]:
        """Get device groups (meshes)"""
        result = await self.api_call("meshes")
        
        groups = []
        for mesh_id, mesh in result.get("meshes", {}).items():
            groups.append({
                "id": mesh_id,
                "name": mesh.get("name"),
                "desc": mesh.get("desc"),
                "type": mesh.get("mtype"),
            })
        
        return groups
    
    # ─────────────────────────────────────────────────────────
    # Remote Sessions
    # ─────────────────────────────────────────────────────────
    
    async def create_desktop_session(self, device_id: str) -> Dict:
        """Create a remote desktop session URL"""
        # Generate one-time link
        result = await self.api_call("createuserlogintoken", {
            "expire": 3600,  # 1 hour
            "tokentype": "desktop",
            "nodeid": device_id,
        })
        
        if "token" in result:
            return {
                "session_type": "desktop",
                "device_id": device_id,
                "url": f"{self.url}/?login={result['token']}&node={device_id}&viewmode=1",
                "expires_in": 3600,
            }
        return {"error": result.get("error", "Failed to create session")}
    
    async def create_terminal_session(self, device_id: str) -> Dict:
        """Create a remote terminal session URL"""
        result = await self.api_call("createuserlogintoken", {
            "expire": 3600,
            "tokentype": "terminal",
            "nodeid": device_id,
        })
        
        if "token" in result:
            return {
                "session_type": "terminal",
                "device_id": device_id,
                "url": f"{self.url}/?login={result['token']}&node={device_id}&viewmode=3",
                "expires_in": 3600,
            }
        return {"error": result.get("error", "Failed to create session")}
    
    async def create_files_session(self, device_id: str) -> Dict:
        """Create a file manager session URL"""
        result = await self.api_call("createuserlogintoken", {
            "expire": 3600,
            "tokentype": "files",
            "nodeid": device_id,
        })
        
        if "token" in result:
            return {
                "session_type": "files",
                "device_id": device_id,
                "url": f"{self.url}/?login={result['token']}&node={device_id}&viewmode=5",
                "expires_in": 3600,
            }
        return {"error": result.get("error", "Failed to create session")}
    
    # ─────────────────────────────────────────────────────────
    # Device Actions
    # ─────────────────────────────────────────────────────────
    
    async def power_action(self, device_id: str, action: str) -> Dict:
        """Perform power action on device"""
        action_map = {
            "restart": 2,
            "shutdown": 1,
            "sleep": 4,
            "wake": 5,
        }
        
        if action not in action_map:
            return {"error": f"Unknown action: {action}"}
        
        result = await self.api_call("poweraction", {
            "nodeids": [device_id],
            "actiontype": action_map[action],
        })
        
        return {
            "action": action,
            "device_id": device_id,
            "success": "error" not in result,
            "result": result,
        }
    
    async def run_command(self, device_id: str, command: str, 
                         shell_type: str = "auto") -> Dict:
        """Run a command on a remote device"""
        # Determine shell type
        if shell_type == "auto":
            device = await self.get_device(device_id)
            if device and "Windows" in (device.get("os") or ""):
                shell_type = "powershell"
            else:
                shell_type = "bash"
        
        result = await self.api_call("runcommand", {
            "nodeids": [device_id],
            "command": command,
            "type": 1 if shell_type == "bash" else 2,  # 1=bash, 2=powershell
        })
        
        return {
            "device_id": device_id,
            "command": command,
            "shell": shell_type,
            "success": "error" not in result,
            "result": result,
        }
    
    async def send_message(self, device_id: str, title: str, message: str) -> Dict:
        """Send a message to device (displays popup)"""
        result = await self.api_call("sendmessage", {
            "nodeids": [device_id],
            "msg": message,
            "title": title,
        })
        
        return {
            "device_id": device_id,
            "title": title,
            "message": message,
            "success": "error" not in result,
        }


# ═══════════════════════════════════════════════════════════════
# 📋 EVIDENCE INTEGRATION
# ═══════════════════════════════════════════════════════════════

async def create_evidence(action: str, data: Dict) -> Optional[str]:
    """Create evidence pack for action"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{EVIDENCE_SERVICE}/packs/create",
                json={
                    "type": f"mesh_{action}",
                    "actor": "mesh_service",
                    "target": data.get("device_id", "system"),
                    "data": data,
                }
            )
            
            if response.status_code == 200:
                return response.json().get("pack_id")
    except:
        pass
    return None


# ═══════════════════════════════════════════════════════════════
# 🚀 FASTAPI APP
# ═══════════════════════════════════════════════════════════════

from contextlib import asynccontextmanager

mesh_client: Optional[MeshCentralClient] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage MeshCentral client lifecycle"""
    global mesh_client
    mesh_client = MeshCentralClient(MESH_URL, MESH_USER, MESH_PASSWORD, MESH_LOGIN_KEY)
    
    # Authenticate on startup
    if MESH_PASSWORD or MESH_LOGIN_KEY:
        await mesh_client.authenticate()
    
    yield
    await mesh_client.close()


app = FastAPI(
    title="🖥️ CODEMASTER Mesh Service",
    version="0.1.0",
    lifespan=lifespan,
)


# ═══════════════════════════════════════════════════════════════
# 🔌 API ROUTES
# ═══════════════════════════════════════════════════════════════

@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "ok",
        "service": "mesh",
        "mesh_url": MESH_URL,
        "authenticated": mesh_client.token is not None if mesh_client else False,
    }


# ─────────────────────────────────────────────────────────
# Devices
# ─────────────────────────────────────────────────────────

@app.get("/devices")
async def list_devices():
    """List all devices from MeshCentral"""
    devices = await mesh_client.get_devices()
    return {"devices": devices, "count": len(devices)}


@app.get("/devices/{device_id}")
async def get_device(device_id: str):
    """Get device details"""
    device = await mesh_client.get_device(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@app.get("/groups")
async def list_groups():
    """List device groups"""
    groups = await mesh_client.get_groups()
    return {"groups": groups}


# ─────────────────────────────────────────────────────────
# Sessions
# ─────────────────────────────────────────────────────────

@app.post("/sessions/desktop")
async def create_desktop_session(req: SessionRequest, bg: BackgroundTasks):
    """Create remote desktop session"""
    result = await mesh_client.create_desktop_session(req.device_id)
    
    # Create evidence
    bg.add_task(create_evidence, "desktop_session", {
        "device_id": req.device_id,
        "user_id": req.user_id,
        "session_type": "desktop",
    })
    
    return result


@app.post("/sessions/terminal")
async def create_terminal_session(req: SessionRequest, bg: BackgroundTasks):
    """Create remote terminal session"""
    result = await mesh_client.create_terminal_session(req.device_id)
    
    bg.add_task(create_evidence, "terminal_session", {
        "device_id": req.device_id,
        "user_id": req.user_id,
        "session_type": "terminal",
    })
    
    return result


@app.post("/sessions/files")
async def create_files_session(req: SessionRequest, bg: BackgroundTasks):
    """Create file manager session"""
    result = await mesh_client.create_files_session(req.device_id)
    
    bg.add_task(create_evidence, "files_session", {
        "device_id": req.device_id,
        "user_id": req.user_id,
        "session_type": "files",
    })
    
    return result


# ─────────────────────────────────────────────────────────
# Device Actions
# ─────────────────────────────────────────────────────────

@app.post("/devices/{device_id}/power")
async def device_power_action(device_id: str, action: PowerAction, bg: BackgroundTasks):
    """Perform power action on device"""
    result = await mesh_client.power_action(device_id, action.action)
    
    bg.add_task(create_evidence, "power_action", {
        "device_id": device_id,
        "action": action.action,
        "success": result.get("success"),
    })
    
    return result


class CommandRequest(BaseModel):
    command: str
    shell: str = "auto"


@app.post("/devices/{device_id}/command")
async def run_device_command(device_id: str, req: CommandRequest, bg: BackgroundTasks):
    """Run command on remote device"""
    result = await mesh_client.run_command(device_id, req.command, req.shell)
    
    bg.add_task(create_evidence, "remote_command", {
        "device_id": device_id,
        "command": req.command,
        "shell": req.shell,
        "success": result.get("success"),
    })
    
    return result


class MessageRequest(BaseModel):
    title: str
    message: str


@app.post("/devices/{device_id}/message")
async def send_device_message(device_id: str, req: MessageRequest):
    """Send message to device"""
    return await mesh_client.send_message(device_id, req.title, req.message)


# ═══════════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    import uvicorn
    import argparse
    
    parser = argparse.ArgumentParser(description='🖥️ CODEMASTER Mesh Service')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8400)
    parser.add_argument('--mesh-url', default=MESH_URL)
    parser.add_argument('--reload', action='store_true')
    
    args = parser.parse_args()
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  🖥️  CODEMASTER MESH SERVICE                                  ║
║                                                               ║
║  MeshCentral: {args.mesh_url:<42} ║
║  Port: {args.port:<51} ║
║                                                               ║
║  Endpoints:                                                   ║
║    /devices           - List all devices                      ║
║    /devices/{{id}}      - Get device details                    ║
║    /groups            - List device groups                    ║
║    /sessions/desktop  - Create desktop session                ║
║    /sessions/terminal - Create terminal session               ║
║    /sessions/files    - Create file manager session           ║
║    /devices/{{id}}/power   - Power actions                      ║
║    /devices/{{id}}/command - Run remote command                 ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "mesh_service:app" if args.reload else app,
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
