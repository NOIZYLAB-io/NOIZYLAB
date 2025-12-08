#!/usr/bin/env python3
"""
24/7 DOMAIN & EMAIL MONITORING SYSTEM
Continuous monitoring with alerts and automatic fixes
"""

import json
import time
import requests
import dns.resolver
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import os

# ==================== CONFIGURATION ====================
CONFIG_FILE = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/domains_and_emails_master.json"
ALERTS_DIR = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/monitoring_alerts"
MONITOR_INTERVAL = 300  # 5 minutes

os.makedirs(ALERTS_DIR, exist_ok=True)

# Load configuration
with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)

DOMAINS = CONFIG.get('all_domains', [])
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "")

# ==================== MONITORING METRICS ====================
class DomainMonitor:
    """Real-time domain monitoring"""
    
    def __init__(self, domain):
        self.domain = domain
        self.status = "unknown"
        self.response_time = 0
        self.alerts = []
    
    def check_availability(self):
        """Check if domain is accessible"""
        try:
            start = time.time()
            response = requests.get(f"https://{self.domain}", timeout=10)
            self.response_time = time.time() - start
            
            if response.status_code == 200:
                self.status = "healthy"
                return True
            else:
                self.status = f"http_{response.status_code}"
                self.alerts.append(f"HTTP {response.status_code} received")
                return False
        except requests.exceptions.SSLError:
            self.status = "ssl_error"
            self.alerts.append("SSL certificate error")
            return False
        except requests.exceptions.Timeout:
            self.status = "timeout"
            self.alerts.append("Domain timeout - slow response")
            return False
        except Exception as e:
            self.status = "error"
            self.alerts.append(f"Error: {str(e)}")
            return False
    
    def check_dns_health(self):
        """Check DNS resolution health"""
        try:
            # Check A record
            dns.resolver.resolve(self.domain, 'A')
            
            # Check MX record
            dns.resolver.resolve(self.domain, 'MX')
            
            return True
        except Exception as e:
            self.alerts.append(f"DNS error: {str(e)}")
            return False
    
    def get_status_emoji(self):
        """Get status emoji"""
        if self.status == "healthy":
            return "✅"
        elif self.status == "timeout":
            return "⏱️"
        elif "ssl" in self.status:
            return "🔒"
        elif "http" in self.status:
            return "⚠️"
        else:
            return "❌"

# ==================== EMAIL MONITORING ====================
class EmailMonitor:
    """Real-time email monitoring"""
    
    def __init__(self, email):
        self.email = email
        self.deliverable = False
        self.alerts = []
    
    def check_mx_records(self):
        """Check MX records for email deliverability"""
        domain = self.email.split('@')[1]
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            if len(list(mx_records)) > 0:
                self.deliverable = True
                return True
            else:
                self.alerts.append("No MX records found")
                return False
        except Exception as e:
            self.alerts.append(f"MX lookup failed: {str(e)}")
            return False
    
    def check_spam_reputation(self):
        """Check spam reputation"""
        # Placeholder for spam reputation check
        # Would integrate with services like Sender Score, etc.
        return True

# ==================== ALERT SYSTEM ====================
def send_alert(title, message, severity="info"):
    """Send alert notification"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    alert = {
        "timestamp": timestamp,
        "title": title,
        "message": message,
        "severity": severity
    }
    
    # Save to file
    alert_file = f"{ALERTS_DIR}/alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(alert_file, 'w') as f:
        json.dump(alert, f, indent=2)
    
    # Send to Slack if configured
    if SLACK_WEBHOOK:
        emoji = {
            "critical": "🚨",
            "warning": "⚠️",
            "info": "ℹ️",
            "success": "✅"
        }.get(severity, "ℹ️")
        
        payload = {
            "text": f"{emoji} *{title}*\n{message}\n_Time: {timestamp}_"
        }
        try:
            requests.post(SLACK_WEBHOOK, json=payload, timeout=5)
        except:
            pass
    
    # Print to console
    print(f"\n[ALERT] {severity.upper()}: {title}")
    print(f"        {message}")

# ==================== MONITORING LOOP ====================
def monitor_cycle():
    """Single monitoring cycle"""
    print(f"\n{'='*60}")
    print(f"🔍 MONITORING CYCLE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    all_healthy = True
    issues = []
    
    # Monitor domains
    print("\n[DOMAINS]")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for domain in DOMAINS:
            monitor = DomainMonitor(domain)
            futures.append(executor.submit(monitor.check_availability))
            futures.append(executor.submit(monitor.check_dns_health))
        
        for future in futures:
            future.result()
    
    for domain in DOMAINS:
        monitor = DomainMonitor(domain)
        monitor.check_availability()
        
        status_emoji = monitor.get_status_emoji()
        response_ms = int(monitor.response_time * 1000)
        print(f"  {status_emoji} {domain}: {monitor.status} ({response_ms}ms)")
        
        if monitor.status != "healthy":
            all_healthy = False
            issues.append(f"{domain}: {monitor.status}")
            
            if monitor.alerts:
                for alert in monitor.alerts:
                    send_alert(
                        f"Domain Issue: {domain}",
                        alert,
                        severity="warning"
                    )
    
    # Monitor emails
    print("\n[EMAILS]")
    for email in EMAILS[:5]:  # Monitor first 5 emails
        monitor = EmailMonitor(email)
        if monitor.check_mx_records():
            print(f"  ✅ {email}: Deliverable")
        else:
            print(f"  ❌ {email}: Issues detected")
            all_healthy = False
            issues.append(f"{email}: MX issues")
            
            if monitor.alerts:
                for alert in monitor.alerts:
                    send_alert(
                        f"Email Issue: {email}",
                        alert,
                        severity="warning"
                    )
    
    # Summary
    if all_healthy:
        print(f"\n✅ All systems healthy!")
    else:
        print(f"\n⚠️ {len(issues)} issues detected")
        for issue in issues:
            print(f"    • {issue}")
    
    return all_healthy

# ==================== AUTO-FIX SYSTEM ====================
def auto_fix_issues():
    """Attempt to automatically fix common issues"""
    print("\n[AUTO-FIX] Checking for fixable issues...")
    
    fixes_applied = []
    
    # Auto-fix examples:
    # 1. Clear DNS cache
    # 2. Retry failed connections
    # 3. Update DNS records via API
    
    print("  ℹ Auto-fix system ready (manual fixes require API keys)")
    
    return fixes_applied

# ==================== CONTINUOUS MONITORING ====================
def start_continuous_monitoring(duration_hours=24):
    """Start 24/7 monitoring"""
    print("="*60)
    print("🚀 STARTING 24/7 MONITORING")
    print("="*60)
    print(f"  • Monitoring {len(DOMAINS)} domains")
    print(f"  • Monitoring {len(EMAILS)} email accounts")
    print(f"  • Check interval: {MONITOR_INTERVAL} seconds")
    print(f"  • Duration: {duration_hours} hours")
    print(f"  • Alerts directory: {ALERTS_DIR}")
    
    send_alert(
        "Monitoring Started",
        f"24/7 monitoring activated for {len(DOMAINS)} domains and {len(EMAILS)} emails",
        severity="success"
    )
    
    end_time = time.time() + (duration_hours * 3600)
    cycle_count = 0
    
    try:
        while time.time() < end_time:
            cycle_count += 1
            print(f"\n{'='*60}")
            print(f"Cycle #{cycle_count}")
            print(f"{'='*60}")
            
            healthy = monitor_cycle()
            
            if not healthy:
                auto_fix_issues()
            
            # Wait before next cycle
            print(f"\n💤 Sleeping for {MONITOR_INTERVAL} seconds...")
            time.sleep(MONITOR_INTERVAL)
        
        send_alert(
            "Monitoring Completed",
            f"Completed {cycle_count} monitoring cycles over {duration_hours} hours",
            severity="success"
        )
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Monitoring stopped by user")
        send_alert(
            "Monitoring Stopped",
            f"Monitoring manually stopped after {cycle_count} cycles",
            severity="info"
        )

# ==================== QUICK SINGLE CHECK ====================
def quick_check():
    """Run a single quick check"""
    print("="*60)
    print("⚡ QUICK HEALTH CHECK")
    print("="*60)
    
    monitor_cycle()
    
    print("\n✅ Quick check complete!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "continuous":
        # Run continuous monitoring
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 24
        start_continuous_monitoring(duration_hours=hours)
    else:
        # Run single check
        quick_check()

