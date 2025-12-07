"""
NOIZY.AI AVATAR BACKEND ROUTES
WebSocket and REST endpoints for avatar state management
SAFE: Data relay only, no autonomous behavior
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import asyncio
import json
from typing import Dict, Set

router = APIRouter(prefix="/api/avatar", tags=["avatar"])

# Connected WebSocket clients
connected_clients: Set[WebSocket] = set()

# Current avatar state
avatar_state = {
    "current_mode": "Safe Autopilot",
    "cpu_load": 0,
    "gpu_load": 0,
    "network_load": 0,
    "is_speaking": False,
    "has_error": False,
    "intent_in_progress": False,
    "diagnostics_running": False,
    "task_completed": False,
    "look_target": None,
    "gesture": None
}


async def broadcast_state():
    """Broadcast current state to all connected clients"""
    if not connected_clients:
        return
    
    message = json.dumps(avatar_state)
    disconnected = set()
    
    for client in connected_clients:
        try:
            await client.send_text(message)
        except:
            disconnected.add(client)
    
    # Clean up disconnected clients
    for client in disconnected:
        connected_clients.discard(client)


@router.websocket("/ws")
async def avatar_websocket(websocket: WebSocket):
    """WebSocket endpoint for real-time avatar state updates"""
    await websocket.accept()
    connected_clients.add(websocket)
    
    try:
        # Send initial state
        await websocket.send_text(json.dumps(avatar_state))
        
        while True:
            # Receive commands from frontend
            data = await websocket.receive_text()
            command = json.loads(data)
            
            # Handle commands
            if command.get("type") == "set_mode":
                avatar_state["current_mode"] = command.get("mode", "Safe Autopilot")
                await broadcast_state()
            
            elif command.get("type") == "interaction":
                # Log VR interaction
                print(f"[AVATAR] VR Interaction: {command}")
                
    except WebSocketDisconnect:
        connected_clients.discard(websocket)
    except Exception as e:
        print(f"[AVATAR] WebSocket error: {e}")
        connected_clients.discard(websocket)


@router.get("/state")
async def get_avatar_state():
    """Get current avatar state"""
    return JSONResponse(content=avatar_state)


@router.post("/command")
async def avatar_command(payload: dict):
    """Handle avatar commands from frontend"""
    command = payload.get("command")
    params = payload.get("params", {})
    
    result = {"success": True, "command": command}
    
    if command == "set_mode":
        mode = params.get("mode", "Safe Autopilot")
        avatar_state["current_mode"] = mode
        await broadcast_state()
        result["new_mode"] = mode
        
    elif command == "voice_command":
        transcript = params.get("transcript", "")
        # Process voice command
        result["transcript"] = transcript
        result["processed"] = True
        
    elif command == "vr_interaction":
        interaction_type = params.get("type")
        result["interaction"] = interaction_type
        
    elif command == "quick_action":
        action = params.get("action")
        # Trigger appropriate flow
        if action == "scan":
            avatar_state["diagnostics_running"] = True
            await broadcast_state()
            # Simulate scan
            await asyncio.sleep(2)
            avatar_state["diagnostics_running"] = False
            avatar_state["task_completed"] = True
            await broadcast_state()
            avatar_state["task_completed"] = False
            
        elif action == "repair":
            avatar_state["intent_in_progress"] = True
            await broadcast_state()
            
        result["action"] = action
        
    else:
        result["success"] = False
        result["error"] = f"Unknown command: {command}"
    
    return JSONResponse(content=result)


@router.post("/update")
async def update_avatar_state(payload: dict):
    """Update avatar state from backend systems"""
    for key, value in payload.items():
        if key in avatar_state:
            avatar_state[key] = value
    
    await broadcast_state()
    return JSONResponse(content={"success": True, "state": avatar_state})


@router.post("/speak")
async def trigger_speech(payload: dict):
    """Signal avatar to speak"""
    avatar_state["is_speaking"] = True
    await broadcast_state()
    
    # Duration from payload or default
    duration = payload.get("duration", 2)
    await asyncio.sleep(duration)
    
    avatar_state["is_speaking"] = False
    await broadcast_state()
    
    return JSONResponse(content={"success": True})


@router.post("/error")
async def trigger_error(payload: dict):
    """Signal error state"""
    avatar_state["has_error"] = True
    await broadcast_state()
    
    # Auto-clear after duration
    duration = payload.get("duration", 3)
    await asyncio.sleep(duration)
    
    avatar_state["has_error"] = False
    await broadcast_state()
    
    return JSONResponse(content={"success": True})


@router.post("/success")
async def trigger_success():
    """Signal success state"""
    avatar_state["task_completed"] = True
    await broadcast_state()
    
    await asyncio.sleep(1.5)
    
    avatar_state["task_completed"] = False
    await broadcast_state()
    
    return JSONResponse(content={"success": True})


# Integration with Mode Manager
def sync_with_mode_manager(mode_manager):
    """Sync avatar state with Mode Manager"""
    avatar_state["current_mode"] = mode_manager.get_mode()


# Integration with Orchestra Engine
def sync_with_orchestra(orchestra_state: dict):
    """Sync avatar state with Orchestra Engine metrics"""
    if "cpu_load" in orchestra_state:
        avatar_state["cpu_load"] = orchestra_state["cpu_load"]
    if "gpu_load" in orchestra_state:
        avatar_state["gpu_load"] = orchestra_state["gpu_load"]
    if "network_load" in orchestra_state:
        avatar_state["network_load"] = orchestra_state["network_load"]

