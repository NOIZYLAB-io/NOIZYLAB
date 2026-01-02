#!/usr/bin/env python3
"""
Robust Fleet Handshake Orchestration Script
Checks connectivity, retries, and logs results for OMEN, Inspiron, MacStudio, MacPro
"""
import subprocess
import time
import sys

NODES = [
    {"name": "OMEN", "ip": "192.168.1.101"},
    {"name": "Inspiron", "ip": "192.168.1.102"},
    {"name": "MacStudio", "ip": "192.168.1.103"},
    {"name": "MacPro", "ip": "10.0.0.199"}
]

HANDSHAKE_COMMAND = "echo 'Fleet Handshake Triggered'"
RETRY_LIMIT = 3
PING_TIMEOUT = 2

def ping_node(ip):
    try:
        result = subprocess.run([
            "ping", "-c", "1", "-W", str(PING_TIMEOUT), ip
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Ping error for {ip}: {e}")
        return False

def trigger_handshake(node):
    print(f"Triggering handshake on {node['name']} ({node['ip']})...")
    # Replace with actual remote execution logic (e.g., SSH, WinRM)
    try:
        if "Mac" in node["name"]:
            subprocess.run([
                "ssh", f"user@{node['ip']}", HANDSHAKE_COMMAND
            ], check=True)
        elif node["name"] in ["OMEN", "Inspiron"]:
            print(f"[Simulated] Would run handshake on Windows node: {node['name']}")
        else:
            print(f"Unknown node type: {node['name']}")
    except Exception as e:
        print(f"Error triggering handshake on {node['name']}: {e}")

def main():
    print("Starting Fleet Handshake...")
    if len(sys.argv) > 1 and sys.argv[1] == "ping":
        print("Pinging all fleet nodes...")
        for node in NODES:
            print(f"Pinging {node['name']} ({node['ip']})...")
            if ping_node(node["ip"]):
                print(f"{node['name']} is reachable.")
            else:
                print(f"{node['name']} is unreachable.")
        print("Ping check complete.")
        return

    for node in NODES:
        reachable = False
        for attempt in range(1, RETRY_LIMIT + 1):
            print(f"Checking connectivity to {node['name']} ({node['ip']}) [Attempt {attempt}]...")
            if ping_node(node["ip"]):
                print(f"{node['name']} is reachable.")
                reachable = True
                break
            else:
                print(f"{node['name']} is unreachable. Retrying...")
                time.sleep(2)
        if not reachable:
            print(f"Forcing handshake on unreachable node: {node['name']} ({node['ip']})")
        else:
            print(f"Proceeding with handshake for {node['name']} ({node['ip']})")
        trigger_handshake(node)
    print("Fleet Handshake complete.")

    # Added ipconfig command execution
    try:
        print("Executing ipconfig on all nodes...")
        for node in NODES:
            print(f"Running ipconfig on {node['name']} ({node['ip']})...")
            if "Mac" in node["name"]:
                subprocess.run([
                    "ssh", f"user@{node['ip']}", "ipconfig"
                ], check=True)
            elif node["name"] in ["OMEN", "Inspiron"]:
                print(f"[Simulated] Would run ipconfig on Windows node: {node['name']}")
            else:
                print(f"Unknown node type for ipconfig: {node['name']}")
    except Exception as e:
        print(f"Error executing ipconfig: {e}")

if __name__ == "__main__":
    main()
