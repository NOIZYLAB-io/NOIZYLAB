"""
NoizyOS Ultra — NoizySync WebSocket
===================================
Real-time bidirectional sync via WebSocket.
Broadcasts state changes to all connected devices instantly.
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict, Any
from datetime import datetime
import json
import asyncio

router = APIRouter()

# Active WebSocket connections
connections: List[WebSocket] = []

# Connection metadata
connection_info: Dict[WebSocket, Dict[str, Any]] = {}


class ConnectionManager:
    """Manages WebSocket connections for sync broadcasting."""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_metadata: Dict[str, Dict] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str = None):
        """Accept and register a new connection."""
        await websocket.accept()
        self.active_connections.append(websocket)
        
        if client_id:
            self.connection_metadata[client_id] = {
                "connected_at": datetime.now().isoformat(),
                "websocket": websocket
            }
        
        # Notify others of new connection
        await self.broadcast({
            "type": "presence",
            "event": "connected",
            "client_id": client_id,
            "timestamp": datetime.now().isoformat()
        }, exclude=websocket)
    
    def disconnect(self, websocket: WebSocket, client_id: str = None):
        """Remove a connection."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        
        if client_id and client_id in self.connection_metadata:
            del self.connection_metadata[client_id]
    
    async def broadcast(self, message: dict, exclude: WebSocket = None):
        """Broadcast message to all connections except excluded."""
        disconnected = []
        
        for connection in self.active_connections:
            if connection != exclude:
                try:
                    await connection.send_json(message)
                except:
                    disconnected.append(connection)
        
        # Clean up disconnected
        for conn in disconnected:
            if conn in self.active_connections:
                self.active_connections.remove(conn)
    
    async def send_to(self, client_id: str, message: dict):
        """Send message to a specific client."""
        if client_id in self.connection_metadata:
            ws = self.connection_metadata[client_id].get("websocket")
            if ws:
                try:
                    await ws.send_json(message)
                except:
                    pass
    
    def get_connection_count(self) -> int:
        """Get number of active connections."""
        return len(self.active_connections)


manager = ConnectionManager()


@router.websocket("/ws/sync")
async def sync_stream(websocket: WebSocket):
    """
    Main sync WebSocket endpoint.
    Receives and broadcasts sync events.
    """
    client_id = None
    
    try:
        # Get client ID from query params if provided
        client_id = websocket.query_params.get("client_id", f"client_{id(websocket)}")
        
        await manager.connect(websocket, client_id)
        
        # Send initial state
        await websocket.send_json({
            "type": "connected",
            "client_id": client_id,
            "connections": manager.get_connection_count(),
            "timestamp": datetime.now().isoformat()
        })
        
        while True:
            # Receive message
            data = await websocket.receive_json()
            
            # Add metadata
            data["_from"] = client_id
            data["_timestamp"] = datetime.now().isoformat()
            
            # Handle different message types
            msg_type = data.get("type", "sync")
            
            if msg_type == "ping":
                # Respond to ping
                await websocket.send_json({"type": "pong"})
            
            elif msg_type == "flowState":
                # Flow state change - broadcast to all
                await manager.broadcast({
                    "type": "flowState",
                    "flowState": data.get("flowState"),
                    "source": client_id
                }, exclude=websocket)
            
            elif msg_type == "emergency":
                # Emergency - broadcast immediately to ALL (no exclusion)
                await manager.broadcast({
                    "type": "emergency",
                    "active": data.get("active", True),
                    "reason": data.get("reason", ""),
                    "source": client_id
                })
            
            elif msg_type == "omenStats":
                # Omen stats update
                await manager.broadcast({
                    "type": "omenStats",
                    "stats": data.get("stats"),
                    "source": client_id
                }, exclude=websocket)
            
            elif msg_type == "voiceEvent":
                # Voice event
                await manager.broadcast({
                    "type": "voiceEvent",
                    "mood": data.get("mood"),
                    "text": data.get("text"),
                    "source": client_id
                }, exclude=websocket)
            
            elif msg_type == "chat":
                # Chat message sync
                await manager.broadcast({
                    "type": "chat",
                    "message": data.get("message"),
                    "source": client_id
                }, exclude=websocket)
            
            else:
                # Generic sync - broadcast to others
                await manager.broadcast(data, exclude=websocket)
    
    except WebSocketDisconnect:
        manager.disconnect(websocket, client_id)
        
        # Notify others of disconnect
        await manager.broadcast({
            "type": "presence",
            "event": "disconnected",
            "client_id": client_id,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        manager.disconnect(websocket, client_id)


@router.get("/ws/status")
def ws_status():
    """Get WebSocket connection status."""
    return {
        "active_connections": manager.get_connection_count(),
        "clients": list(manager.connection_metadata.keys())
    }

