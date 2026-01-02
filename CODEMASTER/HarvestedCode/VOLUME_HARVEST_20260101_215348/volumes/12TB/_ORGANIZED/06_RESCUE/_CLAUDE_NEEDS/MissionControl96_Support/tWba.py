#!/usr/bin/env python3
"""
Fleet API - Distributed node management
"""
from fastapi import FastAPI
import time
import json
from pathlib import Path
from uap_core import uap, UapEvent
import os
import platform

app = FastAPI(title="Mission Control Fleet API")

FLEET_DATA = Path("/Users/rsp_ms/Desktop/MissionControl96/state/fleet_nodes.json")

@app.get("/api/fleet/nodes")
async def get_fleet_nodes():
    """Get all known fleet nodes"""
    if FLEET_DATA.exists():
        try:
            with open(FLEET_DATA, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"nodes": []}

@app.post("/api/fleet/register")
async def register_node(node_data: dict):
    """Register a new fleet node"""
    nodes = {"nodes": []}
    if FLEET_DATA.exists():
        try:
            with open(FLEET_DATA, 'r') as f:
                nodes = json.load(f)
        except:
            pass
    
    # Update or add node
    node_found = False
    for i, node in enumerate(nodes["nodes"]):
        if node.get("hostname") == node_data.get("hostname"):
            nodes["nodes"][i] = {**node, **node_data, "last_seen": time.time()}
            node_found = True
            break
    
    if not node_found:
        nodes["nodes"].append({**node_data, "last_seen": time.time()})
    
    # Save updated fleet data
    FLEET_DATA.parent.mkdir(exist_ok=True)
    with open(FLEET_DATA, 'w') as f:
        json.dump(nodes, f, indent=2)
    
    return {"status": "registered", "node_count": len(nodes["nodes"])}

@app.get("/api/fleet/health")
async def get_fleet_health():
    """Get overall fleet health status"""
    nodes = []
    if FLEET_DATA.exists():
        try:
            with open(FLEET_DATA, 'r') as f:
                data = json.load(f)
                nodes = data.get("nodes", [])
        except:
            pass
    
    current_time = time.time()
    healthy_nodes = [n for n in nodes if current_time - n.get("last_seen", 0) < 120]
    
    return {
        "total_nodes": len(nodes),
        "healthy_nodes": len(healthy_nodes),
        "health_percentage": (len(healthy_nodes) / len(nodes) * 100) if nodes else 100
    }

# 1. Check and reset network
if not check_network():
    print("🌐 Network unreachable — resetting TCP/IP stack...")
    run_command("netsh winsock reset", "Reset Winsock")
    run_command("netsh int ip reset", "Reset IP stack")
    run_command("ipconfig /release", "Release IP")
    run_command("ipconfig /renew", "Renew IP")

# 2. Repair system files
run_command("sfc /scannow", "Run System File Checker")
run_command("DISM /Online /Cleanup-Image /RestoreHealth", "Run DISM Health Restore")

# 3. Clean temp files
temp_path = os.environ.get("TEMP", "C:\\Windows\\Temp")
run_command(f"del /q /s \"{temp_path}\\*.*\"", "Clean TEMP directory")

# 4. Check for updates
run_command("powershell Install-WindowsUpdate -AcceptAll -AutoReboot", "Install Windows Updates")

# 5. Reinstall Parallels Tools (if VM detected)
if "Parallels" in platform.platform():
    run_command("C:\\Program Files\\Parallels\\Parallels Tools\\Install.exe", "Reinstall Parallels Tools")

print("\n✅ Repair protocol complete. Check cockpit.yaml for logs.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)