import json
import os
import subprocess
import requests

def ping_node(ip):
    try:
        result = subprocess.run(["ping", "-n", "2", ip], capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False

def update_status(node, online):
    node["status"] = "online" if online else "offline"
    return node

def main():
    manifest_path = r"u:\MissionControl96\Config\FleetManifest.json"
    with open(manifest_path, "r") as f:
        data = json.load(f)
    nodes = data["nodes"]
    offline_nodes = []
    for node in nodes:
        online = ping_node(node["ip"])
        update_status(node, online)
        if not online:
            offline_nodes.append(node["name"])
    with open(manifest_path, "w") as f:
        json.dump(data, f, indent=2)
    if offline_nodes:
        print(f"ALERT: Offline nodes detected: {', '.join(offline_nodes)}")
    else:
        print("All nodes online.")

if __name__ == "__main__":
    main()
