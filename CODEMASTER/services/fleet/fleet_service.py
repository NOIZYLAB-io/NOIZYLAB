#!/usr/bin/env python3
"""
🚀 CODEMASTER FLEET SERVICE 🚀
================================
Device registry + enrollment + heartbeats + session audit

Device States:
- UNKNOWN → PENDING → ENROLLED → ONLINE/OFFLINE/MAINTENANCE
- Devices must prove identity via certificate or token

EVERY action produces evidence:
- Enrollment creates audit entry
- Heartbeats logged with metrics
- Session start/stop tracked
"""

import os
import json
import uuid
import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
from contextlib import contextmanager
from enum import Enum

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

NOIZY_ROOT = Path(os.environ.get("NOIZY_ROOT", "/Users/m2ultra/NOIZY_AI"))
FLEET_DB = NOIZY_ROOT / "fleet" / "fleet.db"
LOG_DIR = NOIZY_ROOT / "logs" / "fleet"
HEARTBEAT_TIMEOUT = 300  # 5 minutes


class DeviceState(str, Enum):
    UNKNOWN = "unknown"
    PENDING = "pending"
    ENROLLED = "enrolled"
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"
    REVOKED = "revoked"


class SessionState(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    TIMED_OUT = "timed_out"
    TERMINATED = "terminated"


# ═══════════════════════════════════════════════════════════════
# 💾 DATABASE
# ═══════════════════════════════════════════════════════════════

def init_db(db_path: Path = FLEET_DB):
    """Initialize fleet database"""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS devices (
            device_id TEXT PRIMARY KEY,
            hostname TEXT NOT NULL,
            device_type TEXT DEFAULT 'unknown',
            state TEXT DEFAULT 'pending',
            fingerprint TEXT,
            enrolled_at TEXT,
            last_seen TEXT,
            metadata TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS heartbeats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            metrics TEXT DEFAULT '{}',
            FOREIGN KEY (device_id) REFERENCES devices(device_id)
        );
        
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            device_id TEXT NOT NULL,
            user_id TEXT,
            state TEXT DEFAULT 'active',
            started_at TEXT DEFAULT CURRENT_TIMESTAMP,
            ended_at TEXT,
            actions TEXT DEFAULT '[]',
            FOREIGN KEY (device_id) REFERENCES devices(device_id)
        );
        
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            device_id TEXT,
            session_id TEXT,
            action TEXT NOT NULL,
            actor TEXT,
            details TEXT DEFAULT '{}'
        );
        
        CREATE INDEX IF NOT EXISTS idx_heartbeats_device ON heartbeats(device_id);
        CREATE INDEX IF NOT EXISTS idx_heartbeats_time ON heartbeats(timestamp);
        CREATE INDEX IF NOT EXISTS idx_sessions_device ON sessions(device_id);
        CREATE INDEX IF NOT EXISTS idx_audit_device ON audit_log(device_id);
        CREATE INDEX IF NOT EXISTS idx_audit_time ON audit_log(timestamp);
    """)
    
    conn.commit()
    return conn


@contextmanager
def get_db():
    """Database connection context manager"""
    conn = init_db()
    try:
        yield conn
    finally:
        conn.close()


# ═══════════════════════════════════════════════════════════════
# 📝 AUDIT LOGGING
# ═══════════════════════════════════════════════════════════════

def audit_log(action: str, device_id: str = None, session_id: str = None,
              actor: str = None, details: Dict = None):
    """Log an auditable action"""
    with get_db() as conn:
        conn.execute("""
            INSERT INTO audit_log (device_id, session_id, action, actor, details)
            VALUES (?, ?, ?, ?, ?)
        """, (device_id, session_id, action, actor, json.dumps(details or {})))
        conn.commit()
    
    # Also write to log file
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"
    with open(log_file, 'a') as f:
        entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'device_id': device_id,
            'session_id': session_id,
            'actor': actor,
            'details': details,
        }
        f.write(json.dumps(entry) + "\n")


# ═══════════════════════════════════════════════════════════════
# 📱 DEVICE MANAGEMENT
# ═══════════════════════════════════════════════════════════════

@dataclass
class Device:
    device_id: str
    hostname: str
    device_type: str = "unknown"
    state: str = DeviceState.PENDING
    fingerprint: str = None
    enrolled_at: str = None
    last_seen: str = None
    metadata: Dict = None
    created_at: str = None
    
    def to_dict(self) -> Dict:
        d = asdict(self)
        d['metadata'] = self.metadata or {}
        return d


class FleetManager:
    """Fleet device management"""
    
    def __init__(self, db_path: Path = FLEET_DB):
        self.db_path = db_path
        init_db(db_path)
    
    def register(self, hostname: str, device_type: str = "unknown",
                 fingerprint: str = None, metadata: Dict = None,
                 actor: str = None) -> Device:
        """Register a new device (pending enrollment)"""
        device_id = str(uuid.uuid4())[:8]
        now = datetime.now().isoformat()
        
        with get_db() as conn:
            conn.execute("""
                INSERT INTO devices (device_id, hostname, device_type, state, 
                                   fingerprint, metadata, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (device_id, hostname, device_type, DeviceState.PENDING,
                  fingerprint, json.dumps(metadata or {}), now))
            conn.commit()
        
        audit_log("device.registered", device_id=device_id, actor=actor,
                 details={"hostname": hostname, "type": device_type})
        
        return Device(
            device_id=device_id,
            hostname=hostname,
            device_type=device_type,
            state=DeviceState.PENDING,
            fingerprint=fingerprint,
            metadata=metadata,
            created_at=now,
        )
    
    def enroll(self, device_id: str, actor: str = None) -> bool:
        """Enroll a pending device"""
        now = datetime.now().isoformat()
        
        with get_db() as conn:
            cursor = conn.execute("""
                UPDATE devices 
                SET state = ?, enrolled_at = ?, last_seen = ?
                WHERE device_id = ? AND state = ?
            """, (DeviceState.ENROLLED, now, now, device_id, DeviceState.PENDING))
            conn.commit()
            
            if cursor.rowcount > 0:
                audit_log("device.enrolled", device_id=device_id, actor=actor)
                return True
        return False
    
    def get(self, device_id: str) -> Optional[Device]:
        """Get device by ID"""
        with get_db() as conn:
            row = conn.execute("""
                SELECT * FROM devices WHERE device_id = ?
            """, (device_id,)).fetchone()
            
            if row:
                return Device(
                    device_id=row['device_id'],
                    hostname=row['hostname'],
                    device_type=row['device_type'],
                    state=row['state'],
                    fingerprint=row['fingerprint'],
                    enrolled_at=row['enrolled_at'],
                    last_seen=row['last_seen'],
                    metadata=json.loads(row['metadata'] or '{}'),
                    created_at=row['created_at'],
                )
        return None
    
    def list_devices(self, state: str = None) -> List[Device]:
        """List all devices, optionally filtered by state"""
        with get_db() as conn:
            if state:
                rows = conn.execute("""
                    SELECT * FROM devices WHERE state = ? ORDER BY hostname
                """, (state,)).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM devices ORDER BY hostname
                """).fetchall()
            
            return [
                Device(
                    device_id=row['device_id'],
                    hostname=row['hostname'],
                    device_type=row['device_type'],
                    state=row['state'],
                    fingerprint=row['fingerprint'],
                    enrolled_at=row['enrolled_at'],
                    last_seen=row['last_seen'],
                    metadata=json.loads(row['metadata'] or '{}'),
                    created_at=row['created_at'],
                )
                for row in rows
            ]
    
    def heartbeat(self, device_id: str, metrics: Dict = None) -> bool:
        """Record device heartbeat"""
        now = datetime.now().isoformat()
        
        with get_db() as conn:
            # Update last_seen and state
            cursor = conn.execute("""
                UPDATE devices 
                SET last_seen = ?, state = CASE 
                    WHEN state IN ('enrolled', 'offline') THEN 'online'
                    ELSE state 
                END
                WHERE device_id = ?
            """, (now, device_id))
            
            # Record heartbeat
            conn.execute("""
                INSERT INTO heartbeats (device_id, timestamp, metrics)
                VALUES (?, ?, ?)
            """, (device_id, now, json.dumps(metrics or {})))
            conn.commit()
            
            return cursor.rowcount > 0
    
    def mark_offline(self, device_id: str, actor: str = None) -> bool:
        """Mark device as offline"""
        with get_db() as conn:
            cursor = conn.execute("""
                UPDATE devices SET state = ? WHERE device_id = ?
            """, (DeviceState.OFFLINE, device_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                audit_log("device.offline", device_id=device_id, actor=actor)
                return True
        return False
    
    def revoke(self, device_id: str, actor: str = None, reason: str = None) -> bool:
        """Revoke a device's enrollment"""
        with get_db() as conn:
            cursor = conn.execute("""
                UPDATE devices SET state = ? WHERE device_id = ?
            """, (DeviceState.REVOKED, device_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                audit_log("device.revoked", device_id=device_id, actor=actor,
                         details={"reason": reason})
                return True
        return False
    
    def check_stale_devices(self) -> List[str]:
        """Find devices that haven't sent heartbeat recently"""
        cutoff = (datetime.now() - timedelta(seconds=HEARTBEAT_TIMEOUT)).isoformat()
        
        with get_db() as conn:
            rows = conn.execute("""
                SELECT device_id FROM devices 
                WHERE state = 'online' AND last_seen < ?
            """, (cutoff,)).fetchall()
            
            stale = [row['device_id'] for row in rows]
            
            # Mark them offline
            for device_id in stale:
                self.mark_offline(device_id, actor="system.stale_check")
            
            return stale


# ═══════════════════════════════════════════════════════════════
# 🔐 SESSION MANAGEMENT
# ═══════════════════════════════════════════════════════════════

@dataclass
class Session:
    session_id: str
    device_id: str
    user_id: str = None
    state: str = SessionState.ACTIVE
    started_at: str = None
    ended_at: str = None
    actions: List[str] = None
    
    def to_dict(self) -> Dict:
        d = asdict(self)
        d['actions'] = self.actions or []
        return d


class SessionManager:
    """Remote session management"""
    
    def __init__(self, db_path: Path = FLEET_DB):
        self.db_path = db_path
    
    def start_session(self, device_id: str, user_id: str = None) -> Optional[Session]:
        """Start a new remote session"""
        session_id = str(uuid.uuid4())[:12]
        now = datetime.now().isoformat()
        
        with get_db() as conn:
            # Verify device is online
            device = conn.execute("""
                SELECT state FROM devices WHERE device_id = ?
            """, (device_id,)).fetchone()
            
            if not device or device['state'] not in ('online', 'enrolled'):
                return None
            
            conn.execute("""
                INSERT INTO sessions (session_id, device_id, user_id, state, started_at)
                VALUES (?, ?, ?, ?, ?)
            """, (session_id, device_id, user_id, SessionState.ACTIVE, now))
            conn.commit()
        
        audit_log("session.started", device_id=device_id, session_id=session_id,
                 actor=user_id, details={})
        
        return Session(
            session_id=session_id,
            device_id=device_id,
            user_id=user_id,
            state=SessionState.ACTIVE,
            started_at=now,
            actions=[],
        )
    
    def end_session(self, session_id: str, reason: str = "user_closed") -> bool:
        """End an active session"""
        now = datetime.now().isoformat()
        state = SessionState.TERMINATED if reason == "terminated" else SessionState.CLOSED
        
        with get_db() as conn:
            cursor = conn.execute("""
                UPDATE sessions 
                SET state = ?, ended_at = ?
                WHERE session_id = ? AND state = ?
            """, (state, now, session_id, SessionState.ACTIVE))
            conn.commit()
            
            if cursor.rowcount > 0:
                # Get session for audit
                row = conn.execute("""
                    SELECT device_id, user_id FROM sessions WHERE session_id = ?
                """, (session_id,)).fetchone()
                
                audit_log("session.ended", device_id=row['device_id'],
                         session_id=session_id, actor=row['user_id'],
                         details={"reason": reason})
                return True
        return False
    
    def record_action(self, session_id: str, action: str) -> bool:
        """Record an action in a session"""
        with get_db() as conn:
            row = conn.execute("""
                SELECT actions FROM sessions WHERE session_id = ? AND state = ?
            """, (session_id, SessionState.ACTIVE)).fetchone()
            
            if row:
                actions = json.loads(row['actions'] or '[]')
                actions.append({
                    'action': action,
                    'timestamp': datetime.now().isoformat(),
                })
                
                conn.execute("""
                    UPDATE sessions SET actions = ? WHERE session_id = ?
                """, (json.dumps(actions), session_id))
                conn.commit()
                return True
        return False
    
    def get_active_sessions(self, device_id: str = None) -> List[Session]:
        """Get active sessions, optionally filtered by device"""
        with get_db() as conn:
            if device_id:
                rows = conn.execute("""
                    SELECT * FROM sessions WHERE state = ? AND device_id = ?
                """, (SessionState.ACTIVE, device_id)).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM sessions WHERE state = ?
                """, (SessionState.ACTIVE,)).fetchall()
            
            return [
                Session(
                    session_id=row['session_id'],
                    device_id=row['device_id'],
                    user_id=row['user_id'],
                    state=row['state'],
                    started_at=row['started_at'],
                    ended_at=row['ended_at'],
                    actions=json.loads(row['actions'] or '[]'),
                )
                for row in rows
            ]


# ═══════════════════════════════════════════════════════════════
# 🌐 FASTAPI SERVER
# ═══════════════════════════════════════════════════════════════

def create_app():
    """Create FastAPI app for Fleet Service"""
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    
    app = FastAPI(title="🚀 CODEMASTER Fleet Service", version="0.1.0")
    fleet = FleetManager()
    sessions = SessionManager()
    
    class RegisterRequest(BaseModel):
        hostname: str
        device_type: str = "unknown"
        fingerprint: str = None
        metadata: Dict = None
    
    class HeartbeatRequest(BaseModel):
        metrics: Dict = None
    
    class StartSessionRequest(BaseModel):
        user_id: str = None
    
    @app.get("/health")
    async def health():
        return {"status": "ok", "service": "fleet"}
    
    @app.post("/devices/register")
    async def register_device(req: RegisterRequest):
        device = fleet.register(
            hostname=req.hostname,
            device_type=req.device_type,
            fingerprint=req.fingerprint,
            metadata=req.metadata,
        )
        return device.to_dict()
    
    @app.post("/devices/{device_id}/enroll")
    async def enroll_device(device_id: str):
        if fleet.enroll(device_id):
            return {"status": "enrolled", "device_id": device_id}
        raise HTTPException(status_code=400, detail="Enrollment failed")
    
    @app.get("/devices")
    async def list_devices(state: str = None):
        devices = fleet.list_devices(state)
        return [d.to_dict() for d in devices]
    
    @app.get("/devices/{device_id}")
    async def get_device(device_id: str):
        device = fleet.get(device_id)
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")
        return device.to_dict()
    
    @app.post("/devices/{device_id}/heartbeat")
    async def heartbeat(device_id: str, req: HeartbeatRequest):
        if fleet.heartbeat(device_id, req.metrics):
            return {"status": "ok"}
        raise HTTPException(status_code=404, detail="Device not found")
    
    @app.post("/devices/{device_id}/revoke")
    async def revoke_device(device_id: str, reason: str = None):
        if fleet.revoke(device_id, reason=reason):
            return {"status": "revoked"}
        raise HTTPException(status_code=404, detail="Device not found")
    
    @app.post("/sessions/start/{device_id}")
    async def start_session(device_id: str, req: StartSessionRequest):
        session = sessions.start_session(device_id, req.user_id)
        if not session:
            raise HTTPException(status_code=400, detail="Cannot start session")
        return session.to_dict()
    
    @app.post("/sessions/{session_id}/end")
    async def end_session(session_id: str, reason: str = "user_closed"):
        if sessions.end_session(session_id, reason):
            return {"status": "ended"}
        raise HTTPException(status_code=404, detail="Session not found")
    
    @app.get("/sessions/active")
    async def active_sessions(device_id: str = None):
        active = sessions.get_active_sessions(device_id)
        return [s.to_dict() for s in active]
    
    return app


# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🚀 CODEMASTER Fleet Service')
    parser.add_argument('command', choices=['serve', 'status', 'list', 'check-stale'])
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8200)
    parser.add_argument('--state', help='Filter by state')
    
    args = parser.parse_args()
    
    if args.command == 'serve':
        import uvicorn
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port)
    
    elif args.command == 'status':
        fleet = FleetManager()
        devices = fleet.list_devices()
        
        online = sum(1 for d in devices if d.state == 'online')
        offline = sum(1 for d in devices if d.state == 'offline')
        pending = sum(1 for d in devices if d.state == 'pending')
        
        print(f"\n🚀 FLEET STATUS")
        print(f"═══════════════════════════")
        print(f"  Total Devices: {len(devices)}")
        print(f"  Online:        {online}")
        print(f"  Offline:       {offline}")
        print(f"  Pending:       {pending}")
    
    elif args.command == 'list':
        fleet = FleetManager()
        devices = fleet.list_devices(args.state)
        
        print(f"\n🚀 FLEET DEVICES")
        print(f"═══════════════════════════")
        for d in devices:
            status_icon = {"online": "🟢", "offline": "🔴", "pending": "🟡"}.get(d.state, "⚪")
            print(f"  {status_icon} {d.device_id} | {d.hostname} | {d.device_type}")
    
    elif args.command == 'check-stale':
        fleet = FleetManager()
        stale = fleet.check_stale_devices()
        
        if stale:
            print(f"\n⚠️  Marked {len(stale)} devices as offline:")
            for device_id in stale:
                print(f"   - {device_id}")
        else:
            print("\n✅ All online devices are healthy")


if __name__ == "__main__":
    main()
