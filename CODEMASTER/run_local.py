#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🚀 CODEMASTER LOCAL LAUNCHER                                                  ║
║  Run all services locally without Docker                                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Usage:
    python3 run_local.py           # Start all services
    python3 run_local.py --stop    # Stop all services
    python3 run_local.py --status  # Check status
"""

import asyncio
import subprocess
import signal
import sys
import os
from pathlib import Path
from typing import Dict, List, Optional
import time

# Service definitions
SERVICES = {
    "vault": {
        "port": 8000,
        "path": "services/vault/vault_service.py",
        "module": "vault_service:app"
    },
    "catalog": {
        "port": 8001,
        "path": "services/catalog/catalog_service.py",
        "module": "catalog_service:app"
    },
    "evidence": {
        "port": 8002,
        "path": "services/evidence/evidence_service.py",
        "module": "evidence_service:app"
    },
    "ai_gateway": {
        "port": 8100,
        "path": "services/ai_gateway/ai_gateway.py",
        "module": "ai_gateway:app"
    },
    "fleet": {
        "port": 8200,
        "path": "services/fleet/fleet_service.py",
        "module": "fleet_service:app"
    },
    "mc96": {
        "port": 8300,
        "path": "services/mc96/mc96_service.py",
        "module": "mc96_service:app"
    },
    "mesh": {
        "port": 8400,
        "path": "services/mesh/mesh_service.py",
        "module": "mesh_service:app"
    },
    "god_brain": {
        "port": 8500,
        "path": "services/god_brain/god_brain.py",
        "module": "god_brain:app"
    },
    "observability": {
        "port": 9090,
        "path": "services/observability/observability.py",
        "module": "observability:app"
    },
    "portal": {
        "port": 8080,
        "path": "apps/portal/src/portal.py",
        "module": "portal:app"
    }
}

CODEMASTER_ROOT = Path(__file__).parent
PROCESSES: Dict[str, subprocess.Popen] = {}


def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║  🚀 CODEMASTER LOCAL LAUNCHER                                 ║
╚═══════════════════════════════════════════════════════════════╝
""")


def start_service(name: str, config: dict) -> Optional[subprocess.Popen]:
    """Start a single service."""
    service_dir = CODEMASTER_ROOT / Path(config["path"]).parent
    module = config["module"]
    port = config["port"]
    
    if not service_dir.exists():
        print(f"  ⚠️  {name}: Directory not found ({service_dir})")
        return None
    
    try:
        # Build uvicorn command
        cmd = [
            sys.executable, "-m", "uvicorn",
            module,
            "--host", "0.0.0.0",
            "--port", str(port),
            "--reload"
        ]
        
        # Start process
        proc = subprocess.Popen(
            cmd,
            cwd=str(service_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env={**os.environ, "PYTHONUNBUFFERED": "1"}
        )
        
        print(f"  ✅ {name} started on port {port}")
        return proc
    except Exception as e:
        print(f"  ❌ {name}: Failed to start - {e}")
        return None


def stop_services():
    """Stop all running services."""
    print("\n🛑 Stopping services...")
    for name, proc in PROCESSES.items():
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
                print(f"  ✓ {name} stopped")
            except subprocess.TimeoutExpired:
                proc.kill()
                print(f"  ✓ {name} killed")
    PROCESSES.clear()


def check_status():
    """Check status of services."""
    import socket
    
    print("\n📊 Service Status:")
    print("-" * 50)
    
    for name, config in SERVICES.items():
        port = config["port"]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("localhost", port))
        sock.close()
        
        if result == 0:
            print(f"  🟢 {name:15} port {port} - RUNNING")
        else:
            print(f"  🔴 {name:15} port {port} - STOPPED")
    
    print("-" * 50)


def main():
    print_banner()
    
    if "--stop" in sys.argv:
        # Kill any running uvicorn processes on our ports
        for name, config in SERVICES.items():
            port = config["port"]
            subprocess.run(
                f"lsof -ti tcp:{port} | xargs kill -9 2>/dev/null",
                shell=True
            )
        print("✅ All services stopped")
        return
    
    if "--status" in sys.argv:
        check_status()
        return
    
    # Create data directories
    data_root = Path("/Users/m2ultra/NOIZY_AI")
    for subdir in ["vault", "catalog", "evidence_packs", "fleet", "mc96/configs", "cache/ai", "logs"]:
        (data_root / subdir).mkdir(parents=True, exist_ok=True)
    
    # Set environment variables
    os.environ["NOIZY_ROOT"] = str(data_root)
    os.environ["VAULT_URL"] = "http://localhost:8000"
    os.environ["CATALOG_URL"] = "http://localhost:8001"
    os.environ["EVIDENCE_URL"] = "http://localhost:8002"
    os.environ["AI_GATEWAY_URL"] = "http://localhost:8100"
    os.environ["FLEET_URL"] = "http://localhost:8200"
    os.environ["MC96_URL"] = "http://localhost:8300"
    os.environ["MESH_URL"] = "http://localhost:8400"
    os.environ["GOD_HOST"] = "http://localhost:11434"  # Ollama
    
    # Signal handler
    def signal_handler(sig, frame):
        stop_services()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Start services
    print("🚀 Starting services...\n")
    
    for name, config in SERVICES.items():
        proc = start_service(name, config)
        if proc:
            PROCESSES[name] = proc
    
    print("\n" + "=" * 55)
    print("✅ CODEMASTER RUNNING!")
    print("=" * 55)
    print("\n📍 Service URLs:")
    print("   Portal:       http://localhost:8080")
    print("   Vault:        http://localhost:8000/docs")
    print("   Catalog:      http://localhost:8001/docs")
    print("   Evidence:     http://localhost:8002/docs")
    print("   AI Gateway:   http://localhost:8100/docs")
    print("   Fleet:        http://localhost:8200/docs")
    print("   MC96:         http://localhost:8300/docs")
    print("   Mesh:         http://localhost:8400/docs")
    print("   GOD Brain:    http://localhost:8500/docs")
    print("   Observability:http://localhost:9090/docs")
    print("\n💡 Press Ctrl+C to stop all services\n")
    
    # Wait and monitor
    try:
        while True:
            time.sleep(1)
            # Check if any process died
            for name, proc in list(PROCESSES.items()):
                if proc and proc.poll() is not None:
                    print(f"⚠️  {name} stopped unexpectedly!")
    except KeyboardInterrupt:
        stop_services()


if __name__ == "__main__":
    main()
