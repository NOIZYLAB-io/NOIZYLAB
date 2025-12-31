#!/usr/bin/env python3
"""
🚀 CODEMASTER CLI 🚀
====================
Master command center for all CODEMASTER services.

Commands:
  status    - Show all service statuses
  start     - Start all services (docker-compose up)
  stop      - Stop all services (docker-compose down)
  logs      - View service logs
  
  vault     - Vault operations (ingest, find, status)
  catalog   - Catalog operations (search, list, stats)
  evidence  - Evidence pack operations
  fleet     - Fleet device management
  mc96      - Network control operations
  ai        - AI gateway operations
  
  backup    - Run backup jobs
  health    - Health check all services

Run: python codemaster.py <command> [options]
"""

import os
import sys
import json
import argparse
import subprocess
import httpx
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

CODEMASTER_ROOT = Path(__file__).parent
COMPOSE_DIR = CODEMASTER_ROOT / "infra" / "compose"
NOIZY_ROOT = Path(os.environ.get("NOIZY_ROOT", "/Users/m2ultra/NOIZY_AI"))

SERVICES = {
    "vault":      {"port": 8000, "name": "Vault Service"},
    "catalog":    {"port": 8001, "name": "Catalog Service"},
    "evidence":   {"port": 8002, "name": "Evidence Service"},
    "ai-gateway": {"port": 8100, "name": "AI Gateway"},
    "fleet":      {"port": 8200, "name": "Fleet Service"},
    "mc96":       {"port": 8300, "name": "MC96 Network"},
    "portal":     {"port": 8080, "name": "Portal UI"},
}


# ═══════════════════════════════════════════════════════════════
# 🔧 HELPERS
# ═══════════════════════════════════════════════════════════════

def print_banner():
    """Print CODEMASTER banner"""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║    ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗        ║
║   ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗       ║
║   ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║       ║
║   ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║       ║
║   ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║       ║
║    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝       ║
║           S  T  E  R                                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)


def check_service(name: str, port: int) -> Dict:
    """Check if a service is healthy"""
    try:
        with httpx.Client(timeout=5.0) as client:
            response = client.get(f"http://localhost:{port}/health")
            if response.status_code == 200:
                return {"status": "online", "response": response.json()}
    except:
        pass
    return {"status": "offline", "response": None}


def run_docker_compose(cmd: str, *args):
    """Run docker-compose command"""
    compose_file = COMPOSE_DIR / "docker-compose.yml"
    full_cmd = ["docker-compose", "-f", str(compose_file), cmd] + list(args)
    return subprocess.run(full_cmd, cwd=str(COMPOSE_DIR))


# ═══════════════════════════════════════════════════════════════
# 📊 STATUS COMMAND
# ═══════════════════════════════════════════════════════════════

def cmd_status(args):
    """Show status of all services"""
    print_banner()
    print(f"📊 SERVICE STATUS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    online_count = 0
    offline_count = 0
    
    for service, info in SERVICES.items():
        status = check_service(service, info["port"])
        if status["status"] == "online":
            icon = "🟢"
            online_count += 1
        else:
            icon = "🔴"
            offline_count += 1
        
        print(f"  {icon} {info['name']:20s} | Port {info['port']:5d} | {status['status'].upper()}")
    
    print(f"\n  Summary: {online_count} online, {offline_count} offline")
    
    # Storage check
    print(f"\n📁 STORAGE: {NOIZY_ROOT}")
    if NOIZY_ROOT.exists():
        for subdir in ["vault", "catalog", "evidence_packs", "fleet", "mc96", "logs"]:
            path = NOIZY_ROOT / subdir
            if path.exists():
                # Count files
                try:
                    count = sum(1 for _ in path.rglob("*") if _.is_file())
                    print(f"  📂 {subdir:20s} | {count} files")
                except:
                    print(f"  📂 {subdir:20s} | exists")
            else:
                print(f"  ⚠️  {subdir:20s} | not created")
    else:
        print(f"  ⚠️  Root directory not found!")


# ═══════════════════════════════════════════════════════════════
# 🚀 START/STOP COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_start(args):
    """Start all services"""
    print_banner()
    print("🚀 Starting CODEMASTER services...\n")
    
    # Ensure storage directories exist
    for subdir in ["vault/raw", "vault/derived", "vault/index", "vault/staging",
                   "catalog", "evidence_packs", "fleet", "mc96/configs", 
                   "cache/ai", "logs"]:
        (NOIZY_ROOT / subdir).mkdir(parents=True, exist_ok=True)
    
    if args.dev:
        # Start services directly (development mode)
        print("  Starting in development mode...")
        print("  Run each service manually or use the individual service commands")
    else:
        # Docker compose
        run_docker_compose("up", "-d")
    
    print("\n✅ Services started!")
    print("   Portal: http://localhost:8080")


def cmd_stop(args):
    """Stop all services"""
    print_banner()
    print("🛑 Stopping CODEMASTER services...\n")
    run_docker_compose("down")
    print("\n✅ Services stopped!")


def cmd_logs(args):
    """View service logs"""
    if args.service:
        run_docker_compose("logs", "-f", args.service)
    else:
        run_docker_compose("logs", "-f")


# ═══════════════════════════════════════════════════════════════
# 📦 VAULT COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_vault(args):
    """Vault operations"""
    if args.action == "status":
        status = check_service("vault", 8000)
        print(f"\n📦 VAULT STATUS: {status['status'].upper()}")
        if status['response']:
            print(f"   {json.dumps(status['response'], indent=2)}")
    
    elif args.action == "ingest":
        if not args.path:
            print("❌ Error: --path required for ingest")
            return
        print(f"\n📥 Ingesting: {args.path}")
        # Call vault API
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    "http://localhost:8000/ingest",
                    json={"path": args.path, "source": args.source or "cli"}
                )
                print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "find":
        if not args.query:
            print("❌ Error: --query required for find")
            return
        print(f"\n🔍 Finding: {args.query}")
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(
                    "http://localhost:8000/find",
                    params={"q": args.query}
                )
                print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 📚 CATALOG COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_catalog(args):
    """Catalog operations"""
    if args.action == "status":
        status = check_service("catalog", 8001)
        print(f"\n📚 CATALOG STATUS: {status['status'].upper()}")
        if status['response']:
            print(f"   {json.dumps(status['response'], indent=2)}")
    
    elif args.action == "search":
        if not args.query:
            print("❌ Error: --query required for search")
            return
        print(f"\n🔍 Searching: {args.query}")
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(
                    "http://localhost:8001/assets/search",
                    params={"q": args.query}
                )
                results = response.json()
                for asset in results:
                    print(f"  📄 {asset.get('filename', 'unknown')} [{asset.get('asset_type', '?')}]")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "stats":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8001/stats")
                print("\n📊 CATALOG STATS")
                print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 📋 EVIDENCE COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_evidence(args):
    """Evidence pack operations"""
    if args.action == "status":
        status = check_service("evidence", 8002)
        print(f"\n📋 EVIDENCE STATUS: {status['status'].upper()}")
    
    elif args.action == "list":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8002/packs")
                packs = response.json()
                print(f"\n📋 EVIDENCE PACKS ({len(packs)} total)")
                for pack in packs[:20]:  # Show first 20
                    print(f"  {pack.get('pack_id', '?')} | {pack.get('status', '?')} | {pack.get('created_at', '?')[:10]}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "verify":
        if not args.pack_id:
            print("❌ Error: --pack-id required for verify")
            return
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(f"http://localhost:8002/packs/{args.pack_id}/verify")
                print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 🚀 FLEET COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_fleet(args):
    """Fleet operations"""
    if args.action == "status":
        status = check_service("fleet", 8200)
        print(f"\n🚀 FLEET STATUS: {status['status'].upper()}")
    
    elif args.action == "list":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8200/devices")
                devices = response.json()
                print(f"\n🚀 FLEET DEVICES ({len(devices)} total)")
                for device in devices:
                    status_icon = {"online": "🟢", "offline": "🔴", "pending": "🟡"}.get(device.get('state'), "⚪")
                    print(f"  {status_icon} {device.get('device_id', '?')} | {device.get('hostname', '?')} | {device.get('device_type', '?')}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "sessions":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8200/sessions/active")
                sessions = response.json()
                print(f"\n🔐 ACTIVE SESSIONS ({len(sessions)} total)")
                for session in sessions:
                    print(f"  {session.get('session_id', '?')} | {session.get('device_id', '?')} | {session.get('user_id', 'unknown')}")
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 🌐 MC96 COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_mc96(args):
    """MC96 network operations"""
    if args.action == "status":
        status = check_service("mc96", 8300)
        print(f"\n🌐 MC96 STATUS: {status['status'].upper()}")
    
    elif args.action == "devices":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8300/devices")
                devices = response.json()
                print(f"\n🌐 NETWORK DEVICES ({len(devices)} total)")
                for device in devices:
                    print(f"  {device.get('device_id', '?')} | {device.get('hostname', '?'):20s} | {device.get('ip_address', 'N/A'):15s} | {device.get('device_type', '?')}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "runbooks":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8300/runbooks")
                data = response.json()
                print(f"\n📋 AVAILABLE RUNBOOKS")
                for rb in data.get('runbooks', []):
                    print(f"  • {rb.get('name', '?')}")
                    print(f"    {rb.get('description', '')}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "backup":
        print("\n💾 Running config backup...")
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(
                    "http://localhost:8300/runbooks/backup_configs_nightly/execute",
                    json={"target_devices": args.targets}
                )
                result = response.json()
                print(f"  Status: {'✅ Success' if result.get('success') else '❌ Failed'}")
                print(f"  {result.get('summary', '')}")
                print(f"  Evidence Pack: {result.get('evidence_pack_id', 'N/A')}")
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 🧠 AI COMMANDS
# ═══════════════════════════════════════════════════════════════

def cmd_ai(args):
    """AI gateway operations"""
    if args.action == "status":
        status = check_service("ai-gateway", 8100)
        print(f"\n🧠 AI GATEWAY STATUS: {status['status'].upper()}")
        if status['response']:
            print(f"   Model: {status['response'].get('model', 'unknown')}")
    
    elif args.action == "stats":
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get("http://localhost:8100/stats")
                print("\n🧠 AI GATEWAY STATS")
                print(json.dumps(response.json(), indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")
    
    elif args.action == "test":
        prompt = args.prompt or "What is 2+2? Be brief."
        print(f"\n🧠 Testing AI: {prompt}")
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    "http://localhost:8100/reason",
                    json={"prompt": prompt}
                )
                result = response.json()
                print(f"\n✅ Response ({result.get('latency_ms', 0):.0f}ms):")
                print(f"   {result.get('content', 'No response')}")
        except Exception as e:
            print(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════
# 🏥 HEALTH CHECK
# ═══════════════════════════════════════════════════════════════

def cmd_health(args):
    """Health check all services"""
    print_banner()
    print("🏥 HEALTH CHECK\n")
    
    all_healthy = True
    for service, info in SERVICES.items():
        status = check_service(service, info["port"])
        if status["status"] == "online":
            print(f"  ✅ {info['name']}")
        else:
            print(f"  ❌ {info['name']} - OFFLINE")
            all_healthy = False
    
    if all_healthy:
        print("\n🎉 All services healthy!")
    else:
        print("\n⚠️  Some services are offline. Run 'codemaster start' to start them.")
        sys.exit(1)


# ═══════════════════════════════════════════════════════════════
# 🎯 MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='🚀 CODEMASTER CLI - Master Command Center',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    subparsers.add_parser('status', help='Show all service statuses')
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start all services')
    start_parser.add_argument('--dev', action='store_true', help='Development mode')
    
    # Stop command
    subparsers.add_parser('stop', help='Stop all services')
    
    # Logs command
    logs_parser = subparsers.add_parser('logs', help='View service logs')
    logs_parser.add_argument('service', nargs='?', help='Specific service')
    
    # Health command
    subparsers.add_parser('health', help='Health check all services')
    
    # Vault command
    vault_parser = subparsers.add_parser('vault', help='Vault operations')
    vault_parser.add_argument('action', choices=['status', 'ingest', 'find'])
    vault_parser.add_argument('--path', help='Path for ingest')
    vault_parser.add_argument('--source', help='Source identifier')
    vault_parser.add_argument('--query', '-q', help='Search query')
    
    # Catalog command
    catalog_parser = subparsers.add_parser('catalog', help='Catalog operations')
    catalog_parser.add_argument('action', choices=['status', 'search', 'stats'])
    catalog_parser.add_argument('--query', '-q', help='Search query')
    
    # Evidence command
    evidence_parser = subparsers.add_parser('evidence', help='Evidence pack operations')
    evidence_parser.add_argument('action', choices=['status', 'list', 'verify'])
    evidence_parser.add_argument('--pack-id', help='Pack ID for verify')
    
    # Fleet command
    fleet_parser = subparsers.add_parser('fleet', help='Fleet operations')
    fleet_parser.add_argument('action', choices=['status', 'list', 'sessions'])
    
    # MC96 command
    mc96_parser = subparsers.add_parser('mc96', help='MC96 network operations')
    mc96_parser.add_argument('action', choices=['status', 'devices', 'runbooks', 'backup'])
    mc96_parser.add_argument('--targets', nargs='*', help='Target device IDs')
    
    # AI command
    ai_parser = subparsers.add_parser('ai', help='AI gateway operations')
    ai_parser.add_argument('action', choices=['status', 'stats', 'test'])
    ai_parser.add_argument('--prompt', help='Test prompt')
    
    args = parser.parse_args()
    
    if not args.command:
        print_banner()
        parser.print_help()
        return
    
    # Route to command
    commands = {
        'status': cmd_status,
        'start': cmd_start,
        'stop': cmd_stop,
        'logs': cmd_logs,
        'health': cmd_health,
        'vault': cmd_vault,
        'catalog': cmd_catalog,
        'evidence': cmd_evidence,
        'fleet': cmd_fleet,
        'mc96': cmd_mc96,
        'ai': cmd_ai,
    }
    
    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
