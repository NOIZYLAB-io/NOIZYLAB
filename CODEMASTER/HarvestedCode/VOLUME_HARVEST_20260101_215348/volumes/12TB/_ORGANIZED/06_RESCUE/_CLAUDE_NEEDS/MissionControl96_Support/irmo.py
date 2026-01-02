#!/usr/bin/env python3
import os, socket, time, requests
from uap_core import UapEvent, uap
import json

# Configuration
SIG = os.getenv("MESH_SHARED_SECRET", "changeme")
BASE = f"http://{os.getenv('NOIZY_BIND','127.0.0.1')}:{os.getenv('UAP_WS_PORT','8123')}"
NODE = socket.gethostname()

def heartbeat():
    """Send heartbeat to the mesh network"""
    payload = {
        "node": NODE, 
        "ts": time.time(),
        "status": "active",
        "load": get_system_load(),
        "services": get_running_services()
    }
    
    # Publish locally first
    uap.publish(UapEvent(
        topic="fleet_heartbeat",
        payload=payload,
        source=f"mesh_node_{NODE}"
    ))
    
    # Send to mesh network
    try:
        body = json.dumps({
            'topic': 'fleet_heartbeat',
            'payload': payload,
            'timestamp': time.time(),
            'source': NODE
        })
        
        requests.post(
            BASE + "/uap/publish",
            data=body,
            headers={"Content-Type": "application/json"},
            timeout=1.2
        )
        print(f"[{time.strftime('%H:%M:%S')}] Heartbeat sent from {NODE}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Heartbeat failed: {e}")

def get_system_load():
    """Get basic system load info"""
    try:
        import psutil
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
    except ImportError:
        return {"cpu": 0, "memory": 0, "disk": 0}

def get_running_services():
    """Get list of running Mission Control services"""
    services = []
    try:
        import subprocess
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'vs_activity_monitor' in result.stdout:
            services.append('vs_activity_monitor')
        if 'tab_guard' in result.stdout:
            services.append('tab_guard')
        if 'uap_core' in result.stdout:
            services.append('uap_core')
    except:
        pass
    return services

if __name__ == "__main__":
    print(f"🌐 Mesh Fleet Heartbeat starting for node: {NODE}")
    while True:
        heartbeat()
        time.sleep(30)