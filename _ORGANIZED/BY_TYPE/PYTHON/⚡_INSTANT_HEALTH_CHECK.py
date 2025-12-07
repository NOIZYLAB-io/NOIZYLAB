#!/usr/bin/env python3
"""
⚡ Instant Health Check ⚡
========================
Ultra-fast comprehensive health check
"""

import psutil
import requests
from pathlib import Path
import sys


def instant_health():
    """Lightning-fast health check"""
    
    print("\n⚡⚡⚡ INSTANT HEALTH CHECK ⚡⚡⚡")
    print("="*50)
    
    score = 100
    issues = []
    
    # System metrics (0.5s)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    print(f"\n📊 SYSTEM METRICS:")
    print(f"  CPU:    {cpu:.1f}% {'🟢' if cpu < 70 else '🟡' if cpu < 90 else '🔴'}")
    print(f"  Memory: {mem:.1f}% {'🟢' if mem < 75 else '🟡' if mem < 90 else '🔴'}")
    print(f"  Disk:   {disk:.1f}% {'🟢' if disk < 80 else '🟡' if disk < 95 else '🔴'}")
    
    if cpu > 90:
        score -= 20
        issues.append("Critical CPU")
    elif cpu > 70:
        score -= 10
        issues.append("High CPU")
    
    if mem > 90:
        score -= 20
        issues.append("Critical Memory")
    elif mem > 75:
        score -= 10
        issues.append("High Memory")
    
    if disk > 95:
        score -= 20
        issues.append("Critical Disk")
    elif disk > 80:
        score -= 10
        issues.append("High Disk")
    
    # Services (0.5s)
    print(f"\n🔧 SERVICES:")
    
    services = {
        "Slack API": 8003,
        "Network Agent": 8005,
        "Master Dashboard": 8501
    }
    
    services_up = 0
    for name, port in services.items():
        try:
            import socket
            sock = socket.socket()
            sock.settimeout(0.3)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            
            if result == 0:
                print(f"  {name}: 🟢 Running")
                services_up += 1
            else:
                print(f"  {name}: 🔴 Down")
                score -= 15
                issues.append(f"{name} down")
        except:
            print(f"  {name}: ⚪ Unknown")
            score -= 5
    
    # Files (0.1s)
    print(f"\n📁 STRUCTURE:")
    
    required = ["integrations/slack", "network", "ai", "monitoring", "automation"]
    for dir_name in required:
        dir_path = Path(f"/Users/m2ultra/NOIZYLAB/{dir_name}")
        exists = dir_path.exists()
        print(f"  {dir_name}: {'✅' if exists else '❌'}")
        if not exists:
            score -= 5
            issues.append(f"Missing {dir_name}")
    
    # Databases (0.1s)
    print(f"\n💾 DATABASES:")
    
    dbs = [
        "integrations/slack/slack_data.db",
        "network/network_devices.db"
    ]
    
    for db in dbs:
        db_path = Path(f"/Users/m2ultra/NOIZYLAB/{db}")
        exists = db_path.exists()
        print(f"  {db.split('/')[-1]}: {'✅' if exists else '⚪'}")
    
    # Final score
    score = max(0, score)
    
    print(f"\n{'='*50}")
    print(f"🏥 HEALTH SCORE: {score}/100")
    
    if score >= 90:
        status = "EXCELLENT"
        emoji = "🟢"
    elif score >= 70:
        status = "GOOD"
        emoji = "🟡"
    elif score >= 50:
        status = "FAIR"
        emoji = "🟠"
    else:
        status = "POOR"
        emoji = "🔴"
    
    print(f"{emoji} STATUS: {status}")
    
    if issues:
        print(f"\n⚠️  Issues ({len(issues)}):")
        for issue in issues[:5]:
            print(f"  - {issue}")
    else:
        print(f"\n✅ No issues detected!")
    
    print(f"{'='*50}\n")
    
    return score


if __name__ == "__main__":
    score = instant_health()
    sys.exit(0 if score >= 70 else 1)

