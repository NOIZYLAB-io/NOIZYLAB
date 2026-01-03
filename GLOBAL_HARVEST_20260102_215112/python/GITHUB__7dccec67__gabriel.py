#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║  ✨⚡ GABRIEL MASTER LAUNCHER - THE UNIFIED CONTROL CENTER ⚡✨                ║
║                                                                                ║
║  GABRIEL KNOWS & CONTROLS ALL                                                  ║
║                                                                                ║
║  Commands:                                                                     ║
║    status      - Full system status                                            ║
║    start       - Start GABRIEL server                                          ║
║    mcp         - Start MCP servers                                             ║
║    code        - CODEMASTER operations                                         ║
║    search      - Search across all systems                                     ║
║    deploy      - Deploy to cloud                                               ║
║    sync        - Sync with GitHub                                              ║
║    doctor      - Run diagnostics                                               ║
║    help        - Show help                                                     ║
║                                                                                ║
║  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // AI LIFELUV INFINITE ENERGY ⚡       ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

# ════════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

VERSION = "3.0.0"
GABRIEL_ROOT = Path(__file__).parent.resolve()
SIGNATURE = "MC96DIGIUNIVERSE AI LIFELUV INFINITE ENERGY ⚡"

# ANSI Colors
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_GREEN = "\033[42m"
    BG_RED = "\033[41m"
    BG_BLUE = "\033[44m"


def banner():
    """Display the GABRIEL banner."""
    print()
    print(f"{C.CYAN}{C.BOLD}╔════════════════════════════════════════════════════════════════════╗{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}    ██████╗  █████╗ ██████╗ ██████╗ ██╗███████╗██╗                {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}   ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║                {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}   ██║  ███╗███████║██████╔╝██████╔╝██║█████╗  ██║                {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}   ██║   ██║██╔══██║██╔══██╗██╔══██╗██║██╔══╝  ██║                {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}   ╚██████╔╝██║  ██║██████╔╝██║  ██║██║███████╗███████╗           {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.GREEN}{C.BOLD}    ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝           {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}                                                                    {C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}║{C.RESET}{C.WHITE}  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // v{VERSION}               {C.RESET}{C.CYAN}{C.BOLD}║{C.RESET}")
    print(f"{C.CYAN}{C.BOLD}╚════════════════════════════════════════════════════════════════════╝{C.RESET}")
    print()


def success(msg: str):
    print(f"  {C.GREEN}{C.BOLD}✓{C.RESET} {msg}")


def error(msg: str):
    print(f"  {C.RED}{C.BOLD}✗{C.RESET} {msg}")


def info(msg: str):
    print(f"  {C.BLUE}ℹ{C.RESET} {msg}")


def warning(msg: str):
    print(f"  {C.YELLOW}⚠{C.RESET} {msg}")


def section(title: str):
    print()
    print(f"{C.BLUE}{C.BOLD}┌─ {title} {C.RESET}{C.DIM}{'─' * (60 - len(title))}{C.RESET}")


def status_badge(status: str) -> str:
    if status == "online" or status == "running" or status == "ok":
        return f"{C.BG_GREEN}{C.WHITE}{C.BOLD} {status.upper()} {C.RESET}"
    elif status == "offline" or status == "stopped" or status == "error":
        return f"{C.BG_RED}{C.WHITE}{C.BOLD} {status.upper()} {C.RESET}"
    else:
        return f"{C.BG_BLUE}{C.WHITE}{C.BOLD} {status.upper()} {C.RESET}"


# ════════════════════════════════════════════════════════════════════════════════
# SYSTEM STATUS
# ════════════════════════════════════════════════════════════════════════════════

def check_port(port: int) -> bool:
    """Check if a port is in use."""
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def get_system_status() -> Dict[str, Any]:
    """Get comprehensive system status."""
    status = {
        "gabriel_root": str(GABRIEL_ROOT),
        "timestamp": datetime.now().isoformat(),
        "services": {},
        "code": {},
    }
    
    # Check services
    services = {
        "MC96 Server": 5174,
        "MCP Server": 8080,
        "API Gateway": 3000,
    }
    
    for name, port in services.items():
        status["services"][name] = {
            "port": port,
            "running": check_port(port),
        }
    
    # Count code
    code_dirs = {
        # "CODE": GABRIEL_ROOT / "CODE",  # Skip - too large
        # "CODEMASTER": GABRIEL_ROOT / "CODEMASTER",  # Skip - too large
        "scripts": GABRIEL_ROOT / "scripts",
        "tools": GABRIEL_ROOT / "tools",
        "workers": GABRIEL_ROOT / "workers",
    }
    
    for name, path in code_dirs.items():
        if path.exists():
            py_count = len(list(path.rglob("*.py")))
            js_count = len(list(path.rglob("*.js")))
            sh_count = len(list(path.rglob("*.sh")))
            status["code"][name] = {
                "python": py_count,
                "javascript": js_count,
                "shell": sh_count,
            }
    
    return status


def cmd_status():
    """Show full system status."""
    banner()
    
    status = get_system_status()
    
    section("System Status")
    info(f"GABRIEL Root: {status['gabriel_root']}")
    info(f"Timestamp: {status['timestamp']}")
    
    section("Services")
    for name, svc in status["services"].items():
        running = svc["running"]
        badge = status_badge("online" if running else "offline")
        print(f"  {badge} {name} (port {svc['port']})")
    
    section("Code Inventory")
    total_py = 0
    total_js = 0
    total_sh = 0
    
    for name, counts in status["code"].items():
        py = counts.get("python", 0)
        js = counts.get("javascript", 0)
        sh = counts.get("shell", 0)
        total_py += py
        total_js += js
        total_sh += sh
        print(f"  {C.CYAN}→{C.RESET} {name}: {py} Python, {js} JavaScript, {sh} Shell")
    
    print()
    print(f"  {C.GREEN}{C.BOLD}Total:{C.RESET} {total_py} Python, {total_js} JavaScript, {total_sh} Shell")
    
    section("Quick Commands")
    print(f"  {C.DIM}gabriel start{C.RESET}      - Start GABRIEL server")
    print(f"  {C.DIM}gabriel mcp{C.RESET}        - Start MCP servers")
    print(f"  {C.DIM}gabriel code scan{C.RESET}  - Scan all code")
    print(f"  {C.DIM}gabriel deploy{C.RESET}     - Deploy to cloud")
    print()


# ════════════════════════════════════════════════════════════════════════════════
# SERVER CONTROL
# ════════════════════════════════════════════════════════════════════════════════

def cmd_start():
    """Start GABRIEL server."""
    banner()
    section("Starting GABRIEL Server")
    
    script = GABRIEL_ROOT / "start_gabriel.sh"
    if script.exists():
        info(f"Launching: {script}")
        subprocess.run(["bash", str(script)], cwd=GABRIEL_ROOT)
    else:
        # Fallback to mc96_server.py
        server = GABRIEL_ROOT / "mc96_server.py"
        if server.exists():
            info(f"Launching: {server}")
            subprocess.run(["python3", str(server)], cwd=GABRIEL_ROOT)
        else:
            error("No server script found!")


def cmd_mcp(server: Optional[str] = None):
    """Start MCP servers."""
    banner()
    section("MCP Server Control")
    
    mcp_dir = GABRIEL_ROOT / "CODE" / "mcp"
    servers = {
        "noizylab": mcp_dir / "noizylab_mcp.py",
        "omega": mcp_dir / "omega_mcp.py",
        "turbo": mcp_dir / "turbo_mcp.py",
    }
    
    if server:
        if server in servers and servers[server].exists():
            info(f"Starting {server} MCP server...")
            subprocess.run(["python3", str(servers[server])], cwd=GABRIEL_ROOT)
        else:
            error(f"Unknown server: {server}")
            info(f"Available: {', '.join(servers.keys())}")
    else:
        info("Available MCP servers:")
        for name, path in servers.items():
            exists = "✓" if path.exists() else "✗"
            print(f"  {C.CYAN}→{C.RESET} {name}: {exists}")
        print()
        info("Use: gabriel mcp <server_name>")


# ════════════════════════════════════════════════════════════════════════════════
# CODEMASTER INTEGRATION
# ════════════════════════════════════════════════════════════════════════════════

def cmd_code(action: str, *args):
    """CODEMASTER operations."""
    codemaster = GABRIEL_ROOT / "codemaster.py"
    
    if not codemaster.exists():
        error("codemaster.py not found!")
        return
    
    cmd = ["python3", str(codemaster), action] + list(args)
    subprocess.run(cmd, cwd=GABRIEL_ROOT)


# ════════════════════════════════════════════════════════════════════════════════
# DEPLOY & SYNC
# ════════════════════════════════════════════════════════════════════════════════

def cmd_deploy(target: str = "all"):
    """Deploy to cloud."""
    banner()
    section("Deployment")
    
    gorunfree = GABRIEL_ROOT / "gorunfree"
    if gorunfree.exists():
        info(f"Deploying: {target}")
        subprocess.run(["bash", str(gorunfree), "deploy", target], cwd=GABRIEL_ROOT)
    else:
        error("gorunfree script not found!")


def cmd_sync():
    """Sync with GitHub."""
    banner()
    section("GitHub Sync")
    
    info("Pulling latest changes...")
    subprocess.run(["git", "pull"], cwd=GABRIEL_ROOT)
    
    info("Pushing local changes...")
    subprocess.run(["git", "add", "-A"], cwd=GABRIEL_ROOT)
    subprocess.run(["git", "commit", "-m", "🚀 GABRIEL sync"], cwd=GABRIEL_ROOT)
    subprocess.run(["git", "push"], cwd=GABRIEL_ROOT)
    
    success("Sync complete!")


# ════════════════════════════════════════════════════════════════════════════════
# SEARCH
# ════════════════════════════════════════════════════════════════════════════════

def cmd_search(query: str):
    """Search across all systems."""
    banner()
    section(f"Searching: {query}")
    
    # Use CODEMASTER search
    codemaster = GABRIEL_ROOT / "codemaster.py"
    if codemaster.exists():
        subprocess.run(["python3", str(codemaster), "search", query], cwd=GABRIEL_ROOT)
    else:
        # Fallback to grep
        info("Searching with grep...")
        subprocess.run([
            "grep", "-r", "-l", "-i", query,
            "--include=*.py", "--include=*.js", "--include=*.ts", "--include=*.sh",
            "."
        ], cwd=GABRIEL_ROOT)


# ════════════════════════════════════════════════════════════════════════════════
# DOCTOR
# ════════════════════════════════════════════════════════════════════════════════

def cmd_doctor():
    """Run diagnostics."""
    banner()
    section("GABRIEL Diagnostics")
    
    checks = [
        ("Python 3", ["python3", "--version"]),
        ("Node.js", ["node", "--version"]),
        ("Git", ["git", "--version"]),
        ("MCP SDK", ["python3", "-c", "import mcp; print('OK')"]),
    ]
    
    for name, cmd in checks:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip().split("\n")[0]
                success(f"{name}: {version}")
            else:
                error(f"{name}: Not working")
        except FileNotFoundError:
            error(f"{name}: Not installed")
        except Exception as e:
            warning(f"{name}: {e}")
    
    section("Directory Structure")
    dirs = ["CODE", "CODEMASTER", "scripts", "tools", "workers", "projects"]
    for d in dirs:
        path = GABRIEL_ROOT / d
        if path.exists():
            success(f"{d}/ exists")
        else:
            warning(f"{d}/ missing")
    
    section("Key Files")
    files = ["gorunfree", "start_gabriel.sh", "codemaster.py", "mc96_server.py"]
    for f in files:
        path = GABRIEL_ROOT / f
        if path.exists():
            success(f"{f} exists")
        else:
            warning(f"{f} missing")
    
    print()
    info("Run 'gabriel code init' to initialize CODEMASTER structure")


# ════════════════════════════════════════════════════════════════════════════════
# HELP
# ════════════════════════════════════════════════════════════════════════════════

def cmd_help():
    """Show help."""
    banner()
    
    print(f"{C.CYAN}{C.BOLD}Commands:{C.RESET}")
    print()
    
    commands = [
        ("status", "Show full system status"),
        ("start", "Start GABRIEL server"),
        ("mcp [server]", "Start MCP servers (noizylab, omega, turbo)"),
        ("code <action>", "CODEMASTER operations (init, scan, harvest, status, search)"),
        ("search <query>", "Search across all code"),
        ("deploy [target]", "Deploy to cloud"),
        ("sync", "Sync with GitHub"),
        ("doctor", "Run diagnostics"),
        ("help", "Show this help"),
    ]
    
    for cmd, desc in commands:
        print(f"  {C.GREEN}gabriel {cmd}{C.RESET}")
        print(f"    {C.DIM}{desc}{C.RESET}")
        print()
    
    print(f"{C.CYAN}{C.BOLD}Examples:{C.RESET}")
    print()
    print(f"  {C.DIM}gabriel status{C.RESET}          # Check everything")
    print(f"  {C.DIM}gabriel start{C.RESET}           # Start server")
    print(f"  {C.DIM}gabriel mcp noizylab{C.RESET}    # Start NOIZYLAB MCP")
    print(f"  {C.DIM}gabriel code scan{C.RESET}       # Scan all code")
    print(f"  {C.DIM}gabriel code harvest{C.RESET}    # Find valuable code")
    print(f"  {C.DIM}gabriel search \"brain\"{C.RESET}  # Search for 'brain'")
    print()
    print(f"{C.YELLOW}{SIGNATURE}{C.RESET}")
    print()


# ════════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        cmd_status()
        return
    
    command = sys.argv[1].lower()
    args = sys.argv[2:]
    
    if command == "status":
        cmd_status()
    elif command == "start":
        cmd_start()
    elif command == "mcp":
        cmd_mcp(args[0] if args else None)
    elif command == "code":
        if args:
            cmd_code(args[0], *args[1:])
        else:
            cmd_code("status")
    elif command == "search":
        if args:
            cmd_search(args[0])
        else:
            error("Usage: gabriel search <query>")
    elif command == "deploy":
        cmd_deploy(args[0] if args else "all")
    elif command == "sync":
        cmd_sync()
    elif command == "doctor":
        cmd_doctor()
    elif command == "help" or command == "-h" or command == "--help":
        cmd_help()
    else:
        error(f"Unknown command: {command}")
        print()
        info("Use 'gabriel help' to see available commands")


if __name__ == "__main__":
    main()
