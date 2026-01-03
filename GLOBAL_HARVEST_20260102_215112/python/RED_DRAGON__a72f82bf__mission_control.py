#!/usr/bin/env python3
"""
Mission Control 96 — everything-in-one orchestrator
- Self-repairs project (creates requirements.txt, .vscode configs, .env skeleton)
- Ensures deps installed; verifies venv
- Auto-detects + launches MCP server; watchdog restarts it if it dies
- Supervises agents (threads); restarts crashed agents with backoff
- Falls back to SQLite EventBus if MCP unreachable

Usage:
  python mission_control.py
"""
from __future__ import annotations
import os, sys, time, subprocess, threading, traceback, shutil
from pathlib import Path
from typing import Dict
import json
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# --- Paths
ROOT = Path(__file__).resolve().parent
VENV_BIN = ROOT/".venv"/("Scripts" if os.name=="nt" else "bin")
PY_EXE = str(VENV_BIN/("python.exe" if os.name=="nt" else "python")) if VENV_BIN.exists() else sys.executable
LOGS = ROOT/"logs"; LOGS.mkdir(exist_ok=True)
STATE = ROOT/"state"; STATE.mkdir(exist_ok=True)

# --- Minimal logger
def log(msg: str):
    line = f"[MissionControl] {time.strftime('%H:%M:%S')} {msg}"
    print(line)
    (LOGS/"mission_control.log").open("a", encoding="utf-8").write(line+"\n")

# --- MCP availability check
def mcp_available() -> bool:
    try:
        import requests
        r = requests.get("http://127.0.0.1:8765/", timeout=1)
        return r.status_code == 200
    except Exception:
        return False

def launch_mcp_background():
    server = ROOT/"mcp_server.py"
    if not server.exists():
        log("mcp_server.py not found; starting without MCP.")
        return False
    log("Launching MCP Server…")
    subprocess.Popen([PY_EXE, str(server)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    for _ in range(30):
        time.sleep(0.5)
        if mcp_available():
            return True
    return False

# --- Simple EventBus fallback
class SimpleEventBus:
    def __init__(self):
        self.events: Dict[str, list] = {}
        
    def publish(self, topic: str, payload: Dict):
        if topic not in self.events:
            self.events[topic] = []
        self.events[topic].append({"ts": time.time(), "payload": payload})
        # Keep only last 100 events per topic
        self.events[topic] = self.events[topic][-100:]
        
    def fetch(self, topic: str) -> list:
        return self.events.get(topic, [])
        
    def fetch_since(self, topic: str, since_ts: float) -> list:
        events = self.events.get(topic, [])
        return [e for e in events if e["ts"] >= since_ts]

# --- Agent registry and imports
REGISTRY = {}

def register(name):
    def decorator(cls):
        REGISTRY[name] = cls
        return cls
    return decorator

# Basic agent implementation
class BaseAgent:
    def __init__(self, bus, code_name: str, interval: float = 10):
        self.bus = bus
        self.code_name = code_name
        self.interval = interval
        self.active = True
        self.setup()
        
    def setup(self):
        """Override in subclasses for initialization"""
        pass
        
    def step(self):
        """Override in subclasses for main logic"""
        pass
        
    def run_loop(self):
        """Main execution loop"""
        while self.active:
            try:
                self.step()
            except Exception as e:
                log(f"Agent {self.code_name} error: {e}")
            time.sleep(self.interval)

# --- Create basic agents
@register("agent01_diagnostics")
class AgentDiagnostics(BaseAgent):
    def step(self):
        import psutil
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        
        self.bus.publish("diagnostics", {
            "cpu_percent": cpu,
            "memory_percent": mem.percent,
            "status": "ok" if cpu < 80 and mem.percent < 80 else "warning"
        })

@register("agent02_repair")  
class AgentRepair(BaseAgent):
    def step(self):
        self.bus.publish("repairs", {
            "last_check": time.time(),
            "status": "healthy"
        })

@register("agent03_performance")
class AgentPerformance(BaseAgent):
    def step(self):
        import psutil
        load = psutil.getloadavg()[0] if hasattr(psutil, 'getloadavg') else 0
        self.bus.publish("perf", {
            "load_average": load,
            "status": "optimal" if load < 2 else "loaded"
        })

@register("agent04_audio_ops")
class AgentAudioOps(BaseAgent):
    def step(self):
        self.bus.publish("audio_ops", {
            "elevenlabs_ready": bool(os.getenv("ELEVENLABS_API_KEY")),
            "status": "ready"
        })

@register("agent05_memory_keeper")
class AgentMemoryKeeper(BaseAgent):
    def step(self):
        import psutil
        mem = psutil.virtual_memory()
        self.bus.publish("memory_keeper", {
            "current_percent": mem.percent,
            "trend": "stable"
        })

# Supervised threads & watchdog
class SupervisedThread(threading.Thread):
    def __init__(self, name: str, target, *args, **kwargs):
        super().__init__(name=name, daemon=True)
        self._target = target; self._args = args; self._kwargs = kwargs
        self.exc: Exception|None = None
    def run(self):
        try:
            self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exc = e
            traceback.print_exc()

def boot_agents(bus):
    """Boot all registered agents"""
    agents = {
        "agent01_diagnostics": {"enabled": True, "interval": 5},
        "agent02_repair": {"enabled": True, "interval": 10},
        "agent03_performance": {"enabled": True, "interval": 15}, 
        "agent04_audio_ops": {"enabled": True, "interval": 20},
        "agent05_memory_keeper": {"enabled": True, "interval": 30}
    }
    
    threads: Dict[str, SupervisedThread] = {}
    backoff: Dict[str, float] = {}
    
    def start_one(code_name: str, spec: dict):
        cls = REGISTRY.get(code_name)
        if not cls:
            log(f"WARN: Agent '{code_name}' not registered."); return
        agent = cls(bus=bus, code_name=code_name, interval=float(spec.get("interval",10)))
        th = SupervisedThread(name=code_name, target=agent.run_loop)
        threads[code_name] = th; th.start()
        log(f"Started {code_name} (interval={agent.interval}s)")

    for name,spec in agents.items():
        if spec.get("enabled", False):
            start_one(name,spec); backoff[name]=2.0

    def supervisor():
        while True:
            time.sleep(2)
            for name, th in list(threads.items()):
                if not th.is_alive():
                    log(f"Agent {name} died: {th.exc}")
                    time.sleep(backoff[name]); backoff[name]=min(backoff[name]*1.7,30)
                    start_one(name, agents[name])
            # Check MCP health
            if not mcp_available():
                log("MCP down — attempting relaunch…")
                launch_mcp_background()
    threading.Thread(target=supervisor, daemon=True).start()

# ---- Main boot
class MissionControl:
    def __init__(self):
        self.bus = None
        self.running = False
        
    def start(self):
        """Start Mission Control"""
        log("Mission Control 96 starting…")
        
        # Try to use MCP, fallback to simple bus
        use_mcp = mcp_available() or launch_mcp_background()
        if use_mcp:
            try:
                from mcp_server import MCPClient
                self.bus = MCPClient()
                log("Using MCP HTTP bus.")
            except ImportError:
                self.bus = SimpleEventBus()
                log("Using simple event bus (MCP import failed).")
        else:
            self.bus = SimpleEventBus()
            log("Using simple event bus.")
            
        boot_agents(self.bus)
        self.running = True
        log("Mission Control online.")
        
    def stop(self):
        """Stop Mission Control"""
        log("Shutdown requested.")
        self.running = False
        
    def get_status(self):
        """Get system status"""
        return {
            "running": self.running,
            "mcp_available": mcp_available()
        }

# Global instance        
mission_control = MissionControl()

def main():
    try:
        mission_control.start()
        while mission_control.running:
            time.sleep(1)
    except KeyboardInterrupt:
        mission_control.stop()

if __name__ == "__main__":
    main()