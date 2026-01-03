#!/usr/bin/env python3
"""
NoizyLab System Monitor - Real-time monitoring for all tools
============================================================
"""

import psutil
import sqlite3
import requests
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
import time

console = Console()

class SystemMonitor:
    def __init__(self):
        self.services = {
            "email_intelligence": {
                "api": "http://localhost:8000",
                "dashboard": "http://localhost:8501",
                "status": "unknown"
            },
            "universal_blocker": {
                "status": "unknown"
            },
            "imessage_filter": {
                "status": "unknown"
            }
        }
    
    def check_service(self, name, url=None):
        """Check if service is running"""
        if url:
            try:
                response = requests.get(url, timeout=2)
                return response.status_code == 200
            except:
                return False
        else:
            # Check process
            for proc in psutil.process_iter(['name']):
                if name.lower() in proc.info['name'].lower():
                    return True
            return False
    
    def get_system_stats(self):
        """Get system statistics"""
        return {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "network": {
                "sent": psutil.net_io_counters().bytes_sent,
                "recv": psutil.net_io_counters().bytes_recv
            }
        }
    
    def monitor_loop(self):
        """Main monitoring loop"""
        with Live(self.generate_table(), refresh_per_second=2) as live:
            while True:
                live.update(self.generate_table())
                time.sleep(2)
    
    def generate_table(self):
        """Generate monitoring table"""
        table = Table(title="NoizyLab System Monitor")
        table.add_column("Service", style="cyan")
        table.add_column("Status", style="magenta")
        table.add_column("CPU", style="green")
        table.add_column("Memory", style="yellow")
        table.add_column("Uptime", style="blue")
        
        stats = self.get_system_stats()
        
        for service, config in self.services.items():
            status = "🟢 Running" if self.check_service(service, config.get("api")) else "🔴 Stopped"
            table.add_row(
                service,
                status,
                f"{stats['cpu']:.1f}%",
                f"{stats['memory']:.1f}%",
                "N/A"
            )
        
        return table

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.monitor_loop()

