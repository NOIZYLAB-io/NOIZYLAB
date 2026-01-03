#!/usr/bin/env python3
"""
Fleet Heartbeat Service - Enhanced with Agent Core Integration
Monitors and reports agent fleet status to mesh network
"""
import os
import socket
import time
import requests
import json
import sys
from pathlib import Path

# Add agents directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from agent_core import coordinator
    AGENT_CORE_AVAILABLE = True
except ImportError:
    AGENT_CORE_AVAILABLE = False
    print("⚠️  Agent core not available, running in basic mode")

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
        "services": get_running_services(),
        "agent_fleet": get_agent_fleet_status() if AGENT_CORE_AVAILABLE else None
    }
    
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
        
        # Enhanced logging
        agent_info = ""
        if AGENT_CORE_AVAILABLE and payload['agent_fleet']:
            agent_count = payload['agent_fleet'].get('total_agents', 0)
            tasks = payload['agent_fleet'].get('total_tasks', 0)
            agent_info = f" | Agents: {agent_count} | Tasks: {tasks}"
        
        print(f"[{time.strftime('%H:%M:%S')}] 💓 Heartbeat sent from {NODE}{agent_info}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ Heartbeat failed: {e}")

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
        if 'fleet_controller' in result.stdout:
            services.append('fleet_controller')
        if 'agent_dashboard' in result.stdout:
            services.append('agent_dashboard')
    except:
        pass
    return services

def get_agent_fleet_status():
    """Get agent fleet status if available"""
    if not AGENT_CORE_AVAILABLE:
        return None
    
    try:
        status = coordinator.get_fleet_status()
        return {
            'total_agents': status.get('total_agents', 0),
            'total_tasks': status['coordinator_metrics'].get('total_tasks', 0),
            'completed_tasks': status['coordinator_metrics'].get('completed_tasks', 0),
            'active_agents': sum(
                1 for agent in status['agents'].values() 
                if agent['status'] in ['active', 'busy']
            )
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    print(f"🌐 Mesh Fleet Heartbeat starting for node: {NODE}")
    while True:
        heartbeat()
        time.sleep(30)