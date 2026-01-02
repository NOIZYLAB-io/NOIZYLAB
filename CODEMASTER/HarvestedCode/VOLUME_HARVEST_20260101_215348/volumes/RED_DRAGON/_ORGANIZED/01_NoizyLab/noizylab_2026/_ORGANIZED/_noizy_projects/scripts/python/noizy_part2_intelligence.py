#!/usr/bin/env python3
"""
Noizy.ai — Part 2: Intelligence Layer
- Boots MCP server if needed
- Starts Mission Control (96 agents) with auto-recovery
- Bridges MCP → Chat stream (if present) and vice versa
- Resilient, restart-on-crash, health pings
"""

from __future__ import annotations
import os, sys, time, subprocess, signal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY   = sys.executable

BIND_HOST = os.getenv("NOIZY_BIND", "127.0.0.1")
MCP_PORT  = int(os.getenv("MCP_PORT", "8765"))

procs: dict[str, subprocess.Popen] = {}

def log(msg:str):
    print(f"[MIND {time.strftime('%H:%M:%S')}] {msg}", flush=True)

def ensure_dep(mod: str, pip_name: str|None=None):
    try:
        __import__(mod)
    except Exception:
        subprocess.run([PY, "-m", "pip", "install", pip_name or mod])

def start(name: str, argv: list[str]):
    # Start detached so restarts are clean
    p = subprocess.Popen(argv)
    procs[name] = p
    log(f"Started {name} (pid {p.pid})")

def is_up(url: str, timeout=1.2) -> bool:
    try:
        import requests
        r = requests.get(url, timeout=timeout)
        return r.status_code == 200
    except Exception:
        return False

def boot_mcp():
    # Prefer user-provided mcp_server.py; else fall back to fastapi import if bundled
    server = ROOT / "mcp_server.py"
    if server.exists():
        start("mcp", [PY, str(server)])
    else:
        # Try to run embedded module if available
        start("mcp", [PY, "-m", "uvicorn", "mcp_server:app", "--host", BIND_HOST, "--port", str(MCP_PORT), "--reload"])
    # wait a bit
    for _ in range(20):
        time.sleep(0.5)
        if is_up(f"http://{BIND_HOST}:{MCP_PORT}/"):
            log("MCP healthy ✔"); return True
    log("MCP healthcheck failed (continuing anyway).")
    return False

def boot_mission_control():
    mc = ROOT / "mission_control.py"
    if not mc.exists():
        log("mission_control.py not found — skipping.")
        return
    start("mission", [PY, str(mc)])

def boot_chat_bridge():
    bridge = ROOT / "noizy_chat_bridge.py"
    stream = ROOT / "noizy_stream_server.py"
    if stream.exists():
        start("stream", [PY, str(stream)])
    if bridge.exists():
        start("bridge", [PY, str(bridge)])

def watchdog():
    while True:
        time.sleep(3)
        for name, p in list(procs.items()):
            if p.poll() is not None:
                log(f"{name} exited (code {p.returncode}) — restarting…")
                argv = p.args if isinstance(p.args, list) else None
                if not argv:
                    continue
                start(name, argv)

def shutdown(signum=None, frame=None):
    log("Shutting down services…")
    for name, p in procs.items():
        try:
            if p.poll() is None:
                p.terminate()
        except Exception:
            pass
    time.sleep(2)
    for name, p in procs.items():
        try:
            if p.poll() is None:
                p.kill()
        except Exception:
            pass
    sys.exit(0)

def main():
    ensure_dep("requests")
    # Boot sequence
    boot_mcp()
    boot_mission_control()
    boot_chat_bridge()

    log("Intelligence online. Press Ctrl+C to stop.")
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        watchdog()
    except KeyboardInterrupt:
        shutdown()

if __name__ == "__main__":
    main()