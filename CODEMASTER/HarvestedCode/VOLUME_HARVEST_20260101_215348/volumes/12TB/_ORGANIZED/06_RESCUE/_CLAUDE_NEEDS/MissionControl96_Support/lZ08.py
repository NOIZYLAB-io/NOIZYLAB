#!/usr/bin/env python3
"""
Robust Fleet Handshake Orchestration Script
Checks connectivity, retries, and logs results for OMEN, Inspiron, MacStudio, MacPro
"""
import subprocess
import time
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(__file__))
from move_noizywin_assets import inject_assets

NODES = [
    {"name": "OMEN", "ip": "192.168.1.101"},
    {"name": "Inspiron", "ip": "192.168.1.102"},
    {"name": "MacStudio", "ip": "192.168.1.103"},
    {"name": "MacPro", "ip": "10.0.0.199"}
]

HANDSHAKE_COMMAND = "echo 'Fleet Handshake Triggered'"
RETRY_LIMIT = 3
PING_TIMEOUT = 2
LOG_PATH = "."

# === UTILS ===
def log(message):
    os.makedirs(LOG_PATH, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(os.path.join(LOG_PATH, "ritual.log"), "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"🧾 {message}")

def ping_node(ip):
    try:
        result = subprocess.run([
            "ping", "-c", "1", "-W", str(PING_TIMEOUT), ip
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        log(f"Ping error for {ip}: {e}")
        return False

def trigger_handshake(node):
    log(f"Triggering handshake on {node['name']} ({node['ip']})...")
    # Replace with actual remote execution logic (e.g., SSH, WinRM)
    try:
        if "Mac" in node["name"]:
            subprocess.run([
                "ssh", f"user@{node['ip']}", HANDSHAKE_COMMAND
            ], check=True)
        elif node["name"] in ["OMEN", "Inspiron"]:
            log(f"[Simulated] Would run handshake on Windows node: {node['name']}")
        else:
            log(f"Unknown node type: {node['name']}")
    except Exception as e:
        log(f"Error triggering handshake on {node['name']}: {e}")

def main():
    log("Starting Fleet Handshake...")
    if len(sys.argv) > 1 and sys.argv[1] == "ping":
        log("Pinging all fleet nodes...")
        for node in NODES:
            log(f"Pinging {node['name']} ({node['ip']})...")
            if ping_node(node["ip"]):
                log(f"{node['name']} is reachable.")
            else:
                log(f"{node['name']} is unreachable.")
        log("Ping check complete.")
        return

    for node in NODES:
        reachable = False
        for attempt in range(1, RETRY_LIMIT + 1):
            log(f"Checking connectivity to {node['name']} ({node['ip']}) [Attempt {attempt}]...")
            if ping_node(node["ip"]):
                log(f"{node['name']} is reachable.")
                reachable = True
                break
            else:
                log(f"{node['name']} is unreachable. Retrying...")
                time.sleep(2)
        if not reachable:
            log(f"Forcing handshake on unreachable node: {node['name']} ({node['ip']})")
        else:
            log(f"Proceeding with handshake for {node['name']} ({node['ip']})")
        trigger_handshake(node)
    log("Fleet Handshake complete.")

    # Added ipconfig command execution
    try:
        log("Executing ipconfig on all nodes...")
        for node in NODES:
            log(f"Running ipconfig on {node['name']} ({node['ip']})...")
            if "Mac" in node["name"]:
                subprocess.run([
                    "ssh", f"user@{node['ip']}", "ipconfig"
                ], check=True)
            elif node["name"] in ["OMEN", "Inspiron"]:
                log(f"[Simulated] Would run ipconfig on Windows node: {node['name']}")
            else:
                log(f"Unknown node type for ipconfig: {node['name']}")
    except Exception as e:
        log(f"Error executing ipconfig: {e}")

    # Execute fleet_status.sh script
    try:
        log("Executing fleet_status.sh on all nodes...")
        for node in NODES:
            log(f"Running fleet_status.sh on {node['name']} ({node['ip']})...")
            if "Mac" in node["name"]:
                subprocess.run([
                    "ssh", f"user@{node['ip']}", "/Users/rsp_ms/noizy_vista_demo/tools/fleet_status.sh"
                ], check=True)
            elif node["name"] in ["OMEN", "Inspiron"]:
                log(f"[Simulated] Would run fleet_status.sh on Windows node: {node['name']}")
            else:
                log(f"Unknown node type for fleet_status.sh: {node['name']}")
    except Exception as e:
        log(f"Error executing fleet_status.sh: {e}")

    # Restart NOIZYWIN VM
    try:
        log("Restarting NOIZYWIN VM...")
        subprocess.run(["prlctl", "stop", "NOIZYWIN", "--kill"], check=True)
        subprocess.run(["prlctl", "start", "NOIZYWIN"], check=True)
        log("NOIZYWIN VM restarted successfully.")
    except Exception as e:
        log(f"Error restarting NOIZYWIN VM: {e}")

    # Inject assets
    try:
        log("Injecting assets to NOIZYWIN VM...")
        inject_assets()
        log("Assets injected successfully.")
    except Exception as e:
        log(f"Error injecting assets: {e}")

if __name__ == "__main__":
    main()
