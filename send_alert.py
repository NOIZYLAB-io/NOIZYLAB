#!/usr/bin/env python3
"""
🚨 ALERTS - NOTIFICATION SYSTEM
Fish Music Inc - CB_01
🔥 GORUNFREE! 🎸🔥
"""

import sys
import subprocess
from datetime import datetime

class AlertManager:
    """Send alerts via macOS notifications, email, or SMS"""
    
    def __init__(self):
        self.log_file = "/tmp/omega_alerts.log"
        
    def send_notification(self, title: str, message: str, sound: bool = True):
        """Send macOS notification"""
        cmd = [
            "osascript",
            "-e",
            f'display notification "{message}" with title "{title}"'
        ]
        
        if sound:
            cmd += ["-e", 'beep']
        
        subprocess.run(cmd)
        self.log_alert(title, message, "notification")
        
    def send_email(self, recipient: str, subject: str, body: str):
        """Send email alert (requires mail setup)"""
        print(f"📧 Email alert: {subject}")
        print(f"   To: {recipient}")
        print(f"   (Email not configured - would send here)")
        self.log_alert(subject, body, "email")
        
    def send_sms(self, phone: str, message: str):
        """Send SMS alert (requires Twilio or similar)"""
        print(f"📱 SMS alert: {message}")
        print(f"   To: {phone}")
        print(f"   (SMS not configured - would send here)")
        self.log_alert("SMS", message, "sms")
        
    def log_alert(self, title: str, message: str, alert_type: str):
        """Log alert to file"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {alert_type.upper()}: {title} - {message}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
    
    def check_system_health(self):
        """Check system health and send alerts if needed"""
        import psutil
        
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        # Send alerts if thresholds exceeded
        if cpu > 90:
            self.send_notification("⚠️ OMEGA ALERT", f"High CPU usage: {cpu}%")
        
        if ram > 90:
            self.send_notification("⚠️ OMEGA ALERT", f"High RAM usage: {ram}%")
        
        if disk > 95:
            self.send_notification("🚨 OMEGA CRITICAL", f"Disk almost full: {disk}%", sound=True)

if __name__ == "__main__":
    alert = AlertManager()
    
    if len(sys.argv) > 1:
        # Send custom alert
        title = sys.argv[1]
        message = sys.argv[2] if len(sys.argv) > 2 else "OMEGA alert triggered"
        alert.send_notification(title, message)
    else:
        # Check system health
        print("🚨 OMEGA ALERT SYSTEM")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("")
        print("Checking system health...")
        alert.check_system_health()
        print("")
        print("✅ Alert check complete")
        print("")
        print("Usage:")
        print("  ./send_alert.py 'Title' 'Message'")
        print("")
        print("🔥 GORUNFREE! 🎸🔥")
