#!/usr/bin/env python3
"""
Health Monitor - Real-time System Health Monitoring
===================================================
"""

import time
import psutil
import requests
import sqlite3
from datetime import datetime
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

console = Console()

class HealthMonitor:
    def __init__(self):
        self.services = {
            "V4 API": "http://localhost:8000",
            "Dashboard": "http://localhost:8501",
            "Mobile API": "http://localhost:8002",
            "Webhook Hub": "http://localhost:8001"
        }
        self.base = "/Users/m2ultra/NOIZYLAB"
    
    def check_service(self, name, url):
        """Check service health"""
        try:
            response = requests.get(url, timeout=2)
            return "🟢 Running" if response.status_code == 200 else "🟡 Warning"
        except:
            return "🔴 Down"
    
    def check_database(self, db_path):
        """Check database health"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM sqlite_master")
            conn.close()
            return "🟢 Healthy"
        except:
            return "🔴 Error"
    
    def get_system_stats(self):
        """Get system statistics"""
        return {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
    
    def generate_table(self):
        """Generate health monitoring table"""
        table = Table(title="NoizyLab Health Monitor", show_header=True)
        table.add_column("Service", style="cyan")
        table.add_column("Status", style="magenta")
        table.add_column("CPU", style="green")
        table.add_column("Memory", style="yellow")
        
        stats = self.get_system_stats()
        
        for service, url in self.services.items():
            status = self.check_service(service, url)
            table.add_row(
                service,
                status,
                f"{stats['cpu']:.1f}%",
                f"{stats['memory']:.1f}%"
            )
        
        # Database health
        table.add_row("Email DB", self.check_database(f"{self.base}/email-intelligence/email_intelligence.db"), "-", "-")
        table.add_row("Auth DB", self.check_database(f"{self.base}/security/auth.db"), "-", "-")
        
        return table
    
    def monitor(self):
        """Start monitoring"""
        with Live(self.generate_table(), refresh_per_second=2) as live:
            while True:
                live.update(self.generate_table())
                time.sleep(2)

if __name__ == "__main__":
    monitor = HealthMonitor()
    monitor.monitor()

