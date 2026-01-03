#!/usr/bin/env python3
"""
MC96 Local API Server
=====================
Local API endpoint for device handshakes (runs on port 8096)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from datetime import datetime
import sqlite3
import json
from pathlib import Path
import uuid

app = FastAPI(
    title="MC96 Local API",
    description="Local API for device management and handshakes",
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database
DB_PATH = Path(__file__).parent / "mc96_devices.db"


class DeviceInfo(BaseModel):
    """Device information model"""
    mac_address: str
    ip_address: str
    port: int
    hostname: Optional[str] = None
    vendor: Optional[str] = None
    timestamp: str


class SwitchInfo(BaseModel):
    """Switch information model"""
    ip: str
    model: str


class HandshakeRequest(BaseModel):
    """Handshake request model"""
    action: str
    device: DeviceInfo
    switch: SwitchInfo


class HandshakeResponse(BaseModel):
    """Handshake response model"""
    success: bool
    device_id: str
    message: str
    services: List[str]
    configuration: Dict[str, Any]
    timestamp: str


class HeartbeatRequest(BaseModel):
    """Heartbeat request model"""
    device_id: str
    status: Dict[str, Any]


def init_database():
    """Initialize MC96 database"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mc96_devices (
            device_id TEXT PRIMARY KEY,
            mac_address TEXT UNIQUE NOT NULL,
            ip_address TEXT,
            port INTEGER,
            hostname TEXT,
            vendor TEXT,
            services TEXT,
            configuration TEXT,
            status TEXT DEFAULT 'active',
            registered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_heartbeat DATETIME
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mc96_heartbeats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mc96_commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            command TEXT,
            parameters TEXT,
            status TEXT DEFAULT 'pending',
            result TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            executed_at DATETIME
        )
    """)
    
    conn.commit()
    conn.close()


# Initialize database on startup
init_database()


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "MC96 Local API",
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM mc96_devices WHERE status = 'active'")
    active_devices = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mc96_devices")
    total_devices = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "status": "healthy",
        "database": "connected",
        "active_devices": active_devices,
        "total_devices": total_devices,
        "timestamp": datetime.now().isoformat()
    }


@app.post("/api/handshake", response_model=HandshakeResponse)
async def device_handshake(request: HandshakeRequest):
    """
    Handle device handshake
    Called when a new device connects to the network
    """
    device = request.device
    switch = request.switch
    
    print(f"🤝 Handshake request from {device.mac_address} ({device.ip_address})")
    
    # Generate device ID
    device_id = f"MC96-{device.mac_address.replace(':', '')}-{uuid.uuid4().hex[:8]}"
    
    # Determine services based on device
    services = determine_services(device)
    
    # Generate configuration
    configuration = generate_configuration(device, switch)
    
    # Store device in database
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO mc96_devices 
            (device_id, mac_address, ip_address, port, hostname, vendor, services, configuration)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            device_id,
            device.mac_address,
            device.ip_address,
            device.port,
            device.hostname,
            device.vendor,
            json.dumps(services),
            json.dumps(configuration)
        ))
        
        conn.commit()
        print(f"✅ Device registered: {device_id}")
    
    except Exception as e:
        conn.rollback()
        print(f"❌ Failed to register device: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        conn.close()
    
    # Import and send Slack notification
    try:
        import sys
        sys.path.append(str(Path(__file__).parent.parent / "integrations" / "slack"))
        from slack_notifier import network_event
        
        network_event(
            "handshake",
            device.hostname or device.mac_address,
            {
                "Device ID": device_id,
                "IP Address": device.ip_address,
                "MAC Address": device.mac_address,
                "Port": f"Port {device.port}",
                "Vendor": device.vendor or "Unknown",
                "Services": ", ".join(services),
                "Status": "✅ Registered with MC96"
            }
        )
    except:
        pass
    
    return HandshakeResponse(
        success=True,
        device_id=device_id,
        message=f"Device {device.mac_address} successfully registered with MC96",
        services=services,
        configuration=configuration,
        timestamp=datetime.now().isoformat()
    )


@app.post("/api/heartbeat")
async def device_heartbeat(request: HeartbeatRequest):
    """
    Handle device heartbeat
    Devices should send regular heartbeats to indicate they're alive
    """
    device_id = request.device_id
    status = request.status
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Update last heartbeat
    cursor.execute("""
        UPDATE mc96_devices 
        SET last_heartbeat = CURRENT_TIMESTAMP
        WHERE device_id = ?
    """, (device_id,))
    
    # Log heartbeat
    cursor.execute("""
        INSERT INTO mc96_heartbeats (device_id, status)
        VALUES (?, ?)
    """, (device_id, json.dumps(status)))
    
    conn.commit()
    conn.close()
    
    return {
        "acknowledged": True,
        "timestamp": datetime.now().isoformat(),
        "instructions": []
    }


@app.post("/api/status")
async def device_status(device_id: str, status: Dict[str, Any]):
    """Handle device status update"""
    print(f"📊 Status update from {device_id}")
    
    return {
        "acknowledged": True,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/devices")
async def list_devices():
    """List all registered devices"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT device_id, mac_address, ip_address, hostname, vendor, 
               status, registered_at, last_heartbeat
        FROM mc96_devices
        ORDER BY registered_at DESC
    """)
    
    columns = [desc[0] for desc in cursor.description]
    devices = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    conn.close()
    
    return {
        "devices": devices,
        "count": len(devices),
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/devices/{device_id}")
async def get_device(device_id: str):
    """Get specific device information"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT device_id, mac_address, ip_address, port, hostname, vendor,
               services, configuration, status, registered_at, last_heartbeat
        FROM mc96_devices
        WHERE device_id = ?
    """, (device_id,))
    
    row = cursor.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="Device not found")
    
    columns = [desc[0] for desc in cursor.description]
    device = dict(zip(columns, row))
    
    # Parse JSON fields
    if device['services']:
        device['services'] = json.loads(device['services'])
    if device['configuration']:
        device['configuration'] = json.loads(device['configuration'])
    
    conn.close()
    
    return device


@app.delete("/api/devices/{device_id}")
async def remove_device(device_id: str):
    """Remove a device"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM mc96_devices WHERE device_id = ?", (device_id,))
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Device not found")
    
    conn.commit()
    conn.close()
    
    return {"message": f"Device {device_id} removed", "timestamp": datetime.now().isoformat()}


@app.get("/api/stats")
async def get_stats():
    """Get MC96 statistics"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM mc96_devices WHERE status = 'active'")
    active_devices = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mc96_devices")
    total_devices = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT COUNT(*) FROM mc96_heartbeats 
        WHERE timestamp > datetime('now', '-5 minutes')
    """)
    recent_heartbeats = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mc96_commands WHERE status = 'pending'")
    pending_commands = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "active_devices": active_devices,
        "total_devices": total_devices,
        "recent_heartbeats": recent_heartbeats,
        "pending_commands": pending_commands,
        "timestamp": datetime.now().isoformat()
    }


def determine_services(device: DeviceInfo) -> List[str]:
    """Determine which services to enable for the device"""
    services = ['monitoring', 'heartbeat']
    
    # Add services based on vendor
    if device.vendor:
        if 'Raspberry Pi' in device.vendor:
            services.extend(['ssh', 'docker', 'deployment'])
        elif 'Apple' in device.vendor:
            services.extend(['bonjour', 'airplay'])
        elif 'ESP' in device.vendor or 'Espressif' in device.vendor:
            services.extend(['mqtt', 'ota_updates', 'telemetry'])
    
    # Add services based on hostname
    if device.hostname:
        if 'server' in device.hostname.lower():
            services.extend(['api', 'database'])
        if 'printer' in device.hostname.lower():
            services.append('printing')
    
    return list(set(services))  # Remove duplicates


def generate_configuration(device: DeviceInfo, switch: SwitchInfo) -> Dict[str, Any]:
    """Generate device-specific configuration"""
    return {
        "network": {
            "ip": device.ip_address,
            "gateway": switch.ip,
            "dns": ["1.1.1.1", "8.8.8.8"],
            "switch_port": device.port
        },
        "monitoring": {
            "enabled": True,
            "interval": 60,
            "metrics": ["cpu", "memory", "network", "disk"],
            "endpoint": "http://localhost:8096/api/status"
        },
        "heartbeat": {
            "enabled": True,
            "interval": 30,
            "endpoint": "http://localhost:8096/api/heartbeat"
        },
        "security": {
            "firewall": True,
            "auto_update": True,
            "scan_frequency": 3600
        },
        "mc96": {
            "enabled": True,
            "features": ["auto_discovery", "remote_management", "telemetry"]
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting MC96 Local API Server...")
    print("📡 Listening on http://localhost:8096")
    print("📚 API Documentation: http://localhost:8096/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8096)

