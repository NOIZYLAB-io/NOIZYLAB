#!/usr/bin/env python3
"""
Auto-Monitor - Automated System Monitoring & Healing
====================================================
Continuously monitors and heals the system
"""

import time
import requests
import subprocess
import sqlite3
from datetime import datetime
from pathlib import Path
import json

class AutoMonitor:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB")
        self.check_interval = 300  # 5 minutes
        self.services = {
            "V4 API": "http://localhost:8000",
            "Mobile API": "http://localhost:8002",
            "Webhook Hub": "http://localhost:8001"
        }
    
    def check_service(self, name, url):
        """Check if service is running"""
        try:
            response = requests.get(url, timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def restart_service(self, service_name):
        """Restart a service"""
        if "API" in service_name:
            subprocess.Popen(
                ["python3", str(self.base / "email-intelligence/api_server_v4.py")],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
    
    def check_databases(self):
        """Check database health"""
        databases = [
            "email-intelligence/email_intelligence.db",
            "security/auth.db",
            "integrations/webhooks.db"
        ]
        
        for db_path in databases:
            full_path = self.base / db_path
            if full_path.exists():
                try:
                    conn = sqlite3.connect(str(full_path))
                    cursor = conn.cursor()
                    cursor.execute("PRAGMA integrity_check")
                    result = cursor.fetchone()
                    if result[0] != "ok":
                        # Run healer
                        subprocess.run(
                            ["python3", str(self.base / "health/healtheworld.py")],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                    conn.close()
                except:
                    pass
    
    def monitor_loop(self):
        """Main monitoring loop"""
        print("🔍 Auto-Monitor started")
        print(f"   Checking every {self.check_interval} seconds")
        
        while True:
            # Check services
            for service, url in self.services.items():
                if not self.check_service(service, url):
                    print(f"⚠️  {service} is down - attempting restart...")
                    self.restart_service(service)
                    time.sleep(5)
            
            # Check databases
            self.check_databases()
            
            # Wait before next check
            time.sleep(self.check_interval)

if __name__ == "__main__":
    monitor = AutoMonitor()
    try:
        monitor.monitor_loop()
    except KeyboardInterrupt:
        print("\n🛑 Auto-Monitor stopped")

