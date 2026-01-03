"""
MC96 ECOUNIVERSE - System Network Controller
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GORUNFREE • Unified System Intelligence • Zero Latency

The MC96ECOUNIVERSE is a network of intelligent systems:
  - GOD:      Mac Studio M2 Ultra (Temporal OS)
  - GABRIEL:  HP Omen (System Bridge & Messenger)
  - DaFixer:  MacBook Pro (Mobile Operations)

Philosophy: One command = everything done.
"""

import asyncio
import json
import os
import socket
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
import hashlib

# Try hypervelocity imports
try:
    import orjson
    def dumps(obj): return orjson.dumps(obj)
    def loads(s): return orjson.loads(s)
except ImportError:
    def dumps(obj): return json.dumps(obj).encode()
    def loads(s): return json.loads(s) if isinstance(s, str) else json.loads(s.decode())


# ============================================================================
# CONFIGURATION
# ============================================================================

VERSION = "1.0.0"
MC96_PORT = 9696  # MC96 communication port
DISCOVERY_PORT = 9697  # UDP broadcast for discovery
HEARTBEAT_INTERVAL = 30  # seconds
BUFFER_SIZE = 8192  # Socket buffer size
CONNECTION_TIMEOUT = 5.0  # seconds


class SystemRole(Enum):
    """System roles in the MC96ECOUNIVERSE"""
    GOD = "god"           # Primary compute (M2 Ultra)
    BRIDGE = "bridge"     # Communication hub
    MOBILE = "mobile"     # Mobile operations
    WORKER = "worker"     # Task execution
    AGENT = "agent"       # AI agent


class SystemStatus(Enum):
    """System operational status"""
    ONLINE = "online"
    OFFLINE = "offline"
    BUSY = "busy"
    MAINTENANCE = "maintenance"
    UNKNOWN = "unknown"


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class MC96System:
    """Represents a system in the MC96ECOUNIVERSE"""
    id: str
    name: str
    role: SystemRole
    hostname: str
    ip_address: Optional[str] = None
    port: int = MC96_PORT
    status: SystemStatus = SystemStatus.UNKNOWN
    capabilities: List[str] = field(default_factory=list)
    last_seen: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role.value,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "port": self.port,
            "status": self.status.value,
            "capabilities": self.capabilities,
            "last_seen": self.last_seen,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MC96System":
        return cls(
            id=data["id"],
            name=data["name"],
            role=SystemRole(data["role"]),
            hostname=data["hostname"],
            ip_address=data.get("ip_address"),
            port=data.get("port", MC96_PORT),
            status=SystemStatus(data.get("status", "unknown")),
            capabilities=data.get("capabilities", []),
            last_seen=data.get("last_seen", time.time()),
            metadata=data.get("metadata", {})
        )
    
    def is_alive(self, timeout: int = 120) -> bool:
        """Check if system was seen recently"""
        return (time.time() - self.last_seen) < timeout


@dataclass
class MC96Message:
    """Inter-system message format"""
    id: str
    source: str
    target: str  # "*" for broadcast
    action: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source": self.source,
            "target": self.target,
            "action": self.action,
            "payload": self.payload,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MC96Message":
        return cls(
            id=data["id"],
            source=data["source"],
            target=data["target"],
            action=data["action"],
            payload=data.get("payload", {}),
            timestamp=data.get("timestamp", time.time())
        )
    
    def serialize(self) -> bytes:
        return dumps(self.to_dict())
    
    @classmethod
    def deserialize(cls, data: bytes) -> "MC96Message":
        return cls.from_dict(loads(data))


# ============================================================================
# SYSTEM REGISTRY (Known Systems)
# ============================================================================

KNOWN_SYSTEMS = {
    "GOD": MC96System(
        id="mc96-god-001",
        name="GOD",
        role=SystemRole.GOD,
        hostname="m2ultra.local",
        capabilities=[
            "llm-70b", "llm-8b", "music-gen", "metal-fft",
            "temporal-graph", "neural-engine", "video-gen"
        ],
        metadata={
            "hardware": "Mac Studio M2 Ultra",
            "ram": "192GB",
            "gpu_cores": 76,
            "neural_cores": 32
        }
    ),
    "GABRIEL": MC96System(
        id="mc96-gabriel-001",
        name="GABRIEL",
        role=SystemRole.BRIDGE,
        hostname="gabriel.local",
        capabilities=[
            "system-bridge", "messenger", "web-gateway",
            "cloudflare-worker", "gemini-api", "openai-api"
        ],
        metadata={
            "hardware": "HP Omen",
            "type": "Communication Hub"
        }
    ),
    "DaFixer": MC96System(
        id="mc96-dafixer-001",
        name="DaFixer",
        role=SystemRole.MOBILE,
        hostname="dafixer.local",
        capabilities=[
            "mobile-ops", "remote-access", "diagnostics",
            "repair-intake", "customer-portal"
        ],
        metadata={
            "hardware": "MacBook Pro",
            "type": "Mobile Operations"
        }
    )
}


# ============================================================================
# MC96 NETWORK CONTROLLER
# ============================================================================

class MC96Network:
    """
    MC96ECOUNIVERSE Network Controller
    Manages system discovery, health monitoring, and inter-system communication
    """
    
    def __init__(self, local_system: MC96System = None):
        self.systems: Dict[str, MC96System] = {}
        self.local_system = local_system or self._detect_local_system()
        self.message_handlers: Dict[str, Callable] = {}
        self._running = False
        self._heartbeat_task = None
        self._discovery_task = None
        self._listener_task = None
        
        # Register known systems
        for name, system in KNOWN_SYSTEMS.items():
            self.register_system(system)
        
        # Default message handlers
        self._register_default_handlers()
    
    def _detect_local_system(self) -> MC96System:
        """Auto-detect the local system based on hostname"""
        hostname = socket.gethostname().lower()
        
        # Try to match known systems
        for name, system in KNOWN_SYSTEMS.items():
            if system.hostname.replace(".local", "") in hostname:
                return MC96System(
                    id=system.id,
                    name=system.name,
                    role=system.role,
                    hostname=hostname,
                    ip_address=self._get_local_ip(),
                    capabilities=system.capabilities,
                    metadata=system.metadata
                )
        
        # Default to a worker node
        return MC96System(
            id=f"mc96-worker-{hashlib.md5(hostname.encode()).hexdigest()[:8]}",
            name=f"WORKER-{hostname[:8].upper()}",
            role=SystemRole.WORKER,
            hostname=hostname,
            ip_address=self._get_local_ip(),
            capabilities=["worker"]
        )
    
    def _get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"
    
    def _register_default_handlers(self):
        """Register default message handlers"""
        self.message_handlers["ping"] = self._handle_ping
        self.message_handlers["status"] = self._handle_status
        self.message_handlers["discovery"] = self._handle_discovery
        self.message_handlers["execute"] = self._handle_execute
    
    # --- System Management ---
    
    def register_system(self, system: MC96System):
        """Register a system in the network"""
        self.systems[system.name] = system
    
    def get_system(self, name: str) -> Optional[MC96System]:
        """Get a system by name"""
        return self.systems.get(name)
    
    def get_online_systems(self) -> List[MC96System]:
        """Get all online systems"""
        return [s for s in self.systems.values() if s.is_alive()]
    
    def get_systems_by_capability(self, capability: str) -> List[MC96System]:
        """Find systems with a specific capability"""
        return [
            s for s in self.systems.values()
            if capability in s.capabilities and s.is_alive()
        ]
    
    # --- Message Handling ---
    
    def register_handler(self, action: str, handler: Callable):
        """Register a message handler"""
        self.message_handlers[action] = handler
    
    async def _handle_ping(self, msg: MC96Message) -> dict:
        """Handle ping messages"""
        return {
            "status": "pong",
            "system": self.local_system.name,
            "timestamp": time.time()
        }
    
    async def _handle_status(self, msg: MC96Message) -> dict:
        """Handle status request"""
        return {
            "system": self.local_system.to_dict(),
            "uptime": time.time() - self.local_system.last_seen,
            "network": {
                "online_systems": len(self.get_online_systems()),
                "total_systems": len(self.systems)
            }
        }
    
    async def _handle_discovery(self, msg: MC96Message) -> dict:
        """Handle discovery messages"""
        self.local_system.last_seen = time.time()
        return self.local_system.to_dict()
    
    async def _handle_execute(self, msg: MC96Message) -> dict:
        """Handle execute command (placeholder for task execution)"""
        command = msg.payload.get("command", "")
        return {
            "status": "received",
            "command": command,
            "system": self.local_system.name
        }
    
    # --- Network Operations ---
    
    def create_message(self, target: str, action: str, payload: dict = None) -> MC96Message:
        """Create a new message"""
        return MC96Message(
            id=hashlib.md5(f"{time.time()}{action}".encode()).hexdigest()[:12],
            source=self.local_system.name,
            target=target,
            action=action,
            payload=payload or {}
        )
    
    async def send_message(self, target: str, action: str, payload: dict = None) -> Optional[dict]:
        """Send a message to a target system"""
        system = self.get_system(target)
        if not system or not system.ip_address:
            return None
        
        msg = self.create_message(target, action, payload)
        
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(system.ip_address, system.port),
                timeout=CONNECTION_TIMEOUT
            )
            
            writer.write(msg.serialize())
            await writer.drain()
            
            response_data = await asyncio.wait_for(reader.read(BUFFER_SIZE), timeout=CONNECTION_TIMEOUT)
            writer.close()
            await writer.wait_closed()
            
            return loads(response_data)
        except Exception as e:
            return {"error": str(e)}
    
    async def broadcast(self, action: str, payload: dict = None) -> Dict[str, dict]:
        """Broadcast a message to all systems concurrently"""
        async def send_to_system(name: str):
            try:
                return name, await self.send_message(name, action, payload)
            except Exception as e:
                return name, {"error": str(e)}
        
        # Create tasks for all systems except local
        tasks = [
            send_to_system(name)
            for name in self.systems
            if name != self.local_system.name
        ]
        
        # Execute all tasks concurrently
        results_list = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Build results dict
        results = {}
        for item in results_list:
            if isinstance(item, Exception):
                continue
            name, result = item
            results[name] = result
        
        return results
    
    # --- Status & Monitoring ---
    
    def get_network_status(self) -> dict:
        """Get comprehensive network status"""
        online = self.get_online_systems()
        
        return {
            "mc96_version": VERSION,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "local_system": self.local_system.to_dict(),
            "network": {
                "total_systems": len(self.systems),
                "online_systems": len(online),
                "offline_systems": len(self.systems) - len(online)
            },
            "systems": {
                name: {
                    "status": s.status.value,
                    "role": s.role.value,
                    "alive": s.is_alive(),
                    "last_seen": datetime.fromtimestamp(s.last_seen).isoformat()
                }
                for name, s in self.systems.items()
            },
            "capabilities": self._aggregate_capabilities()
        }
    
    def _aggregate_capabilities(self) -> Dict[str, List[str]]:
        """Aggregate capabilities across all systems"""
        caps = {}
        for system in self.get_online_systems():
            for cap in system.capabilities:
                if cap not in caps:
                    caps[cap] = []
                caps[cap].append(system.name)
        return caps
    
    # --- Server Mode ---
    
    async def start(self):
        """Start the MC96 network controller"""
        self._running = True
        self.local_system.status = SystemStatus.ONLINE
        self.local_system.last_seen = time.time()
        
        # Start background tasks
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    MC96 ECOUNIVERSE                          ║
║               Network Controller v{VERSION}                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Local System: {self.local_system.name:43}  ║
║  Role:         {self.local_system.role.value:43}  ║
║  IP:           {self.local_system.ip_address or 'detecting...':43}  ║
║  Port:         {self.local_system.port:<43}  ║
║                                                              ║
║  Network Status:                                             ║
║    Known Systems: {len(self.systems):<40}  ║
║    Online:        {len(self.get_online_systems()):<40}  ║
║                                                              ║
║                     GORUNFREE                                ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    async def stop(self):
        """Stop the MC96 network controller"""
        self._running = False
        self.local_system.status = SystemStatus.OFFLINE
        
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
    
    async def _heartbeat_loop(self):
        """Send periodic heartbeats"""
        while self._running:
            self.local_system.last_seen = time.time()
            await asyncio.sleep(HEARTBEAT_INTERVAL)


# ============================================================================
# CLI INTERFACE
# ============================================================================

async def main():
    """Main entry point for MC96 CLI"""
    network = MC96Network()
    await network.start()
    
    print("\nMC96 ECOUNIVERSE READY.")
    print("Commands: status, systems, ping <name>, exit")
    print("")
    
    loop = asyncio.get_running_loop()
    
    while network._running:
        try:
            cmd = await loop.run_in_executor(None, input, "MC96 >> ")
            cmd = cmd.strip().lower()
            
            if cmd == "exit":
                break
            
            elif cmd == "status":
                status = network.get_network_status()
                print(json.dumps(status, indent=2, default=str))
            
            elif cmd == "systems":
                print("\n--- MC96 SYSTEMS ---")
                for name, system in network.systems.items():
                    alive = "🟢" if system.is_alive() else "🔴"
                    print(f"  {alive} {name:12} | {system.role.value:8} | {system.hostname}")
                print("")
            
            elif cmd.startswith("ping "):
                target = cmd.split(" ", 1)[1].upper()
                result = await network.send_message(target, "ping")
                print(f"Response: {result}")
            
            elif cmd == "caps" or cmd == "capabilities":
                caps = network._aggregate_capabilities()
                print("\n--- CAPABILITIES ---")
                for cap, systems in caps.items():
                    print(f"  {cap}: {', '.join(systems)}")
                print("")
            
            else:
                print("Unknown command. Try: status, systems, ping <name>, caps, exit")
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
    
    await network.stop()
    print("MC96 SHUTDOWN.")


if __name__ == "__main__":
    asyncio.run(main())
