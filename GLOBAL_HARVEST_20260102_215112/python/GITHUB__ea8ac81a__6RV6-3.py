#!/usr/bin/env python3
"""
Mission Control 96 - Status Dashboard
Real-time system status and management
"""

import requests
import json
import time
import os
from datetime import datetime

class MissionControlStatus:
    def __init__(self):
        self.mcp_url = "http://127.0.0.1:8765"
        self.rock_mode_url = "http://127.0.0.1:9090"
        
    def check_mcp_server(self):
        """Check MCP Server status"""
        try:
            response = requests.get(f"{self.mcp_url}/", timeout=3)
            if response.status_code == 200:
                data = response.json()
                return {
                    "status": "✅ ONLINE", 
                    "events_stored": data.get("events_stored", 0),
                    "url": f"{self.mcp_url}/dashboard"
                }
        except Exception as e:
            return {"status": "❌ OFFLINE", "error": str(e)}
            
    def check_rock_mode(self):
        """Check Rock Mode XL status"""
        try:
            response = requests.get(f"{self.rock_mode_url}/", timeout=3)
            if response.status_code == 200:
                return {
                    "status": "✅ ONLINE",
                    "url": self.rock_mode_url
                }
        except Exception as e:
            return {"status": "❌ OFFLINE", "error": str(e)}
            
    def get_agent_status(self):
        """Get agent telemetry from MCP"""
        agents = {}
        topics = ["diagnostics", "repairs", "perf", "audio_ops", "memory_keeper"]
        
        for topic in topics:
            try:
                response = requests.get(f"{self.mcp_url}/fetch/{topic}", timeout=3)
                if response.status_code == 200:
                    events = response.json()
                    if events:
                        latest = events[-1]["payload"]
                        agents[topic] = {
                            "status": latest.get("status", "unknown"),
                            "last_update": datetime.fromtimestamp(events[-1]["ts"]).strftime("%H:%M:%S"),
                            "data": latest
                        }
                    else:
                        agents[topic] = {"status": "no data", "last_update": "never"}
            except Exception as e:
                agents[topic] = {"status": "error", "error": str(e)}
                
        return agents
        
    def display_status(self):
        """Display comprehensive status"""
        print("🚀 Mission Control 96 - System Status")
        print("=" * 50)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # MCP Server
        mcp_status = self.check_mcp_server()
        print(f"📡 MCP Server: {mcp_status['status']}")
        if "events_stored" in mcp_status:
            print(f"   Events Stored: {mcp_status['events_stored']}")
            print(f"   Dashboard: {mcp_status['url']}")
        print()
        
        # Rock Mode XL
        rock_status = self.check_rock_mode()
        print(f"🎸 Rock Mode XL: {rock_status['status']}")
        if "url" in rock_status:
            print(f"   Portal: {rock_status['url']}")
        print()
        
        # Agents
        print("🤖 Agent Status:")
        agents = self.get_agent_status()
        for agent_name, agent_data in agents.items():
            status_icon = "✅" if agent_data["status"] in ["ok", "optimal", "healthy", "ready", "stable"] else "⚠️" if agent_data["status"] in ["warning", "loaded", "degraded"] else "❌"
            print(f"   {status_icon} {agent_name}: {agent_data['status']} (last: {agent_data['last_update']})")
        print()
        
        # Quick stats
        if agents.get("diagnostics", {}).get("data"):
            diag = agents["diagnostics"]["data"]
            print("📊 System Stats:")
            print(f"   CPU: {diag.get('cpu_percent', 0):.1f}%")
            print(f"   Memory: {diag.get('memory_percent', 0):.1f}%")
            if "platform" in diag:
                print(f"   Platform: {diag['platform']}")
        print()
        
    def run_live(self, interval=5):
        """Run live status updates"""
        try:
            while True:
                os.system('clear' if os.name == 'posix' else 'cls')
                self.display_status()
                print(f"🔄 Refreshing in {interval}s... (Ctrl+C to exit)")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n👋 Status monitoring stopped.")

def main():
    import sys
    
    status = MissionControlStatus()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--live":
        status.run_live()
    else:
        status.display_status()

if __name__ == "__main__":
    main()