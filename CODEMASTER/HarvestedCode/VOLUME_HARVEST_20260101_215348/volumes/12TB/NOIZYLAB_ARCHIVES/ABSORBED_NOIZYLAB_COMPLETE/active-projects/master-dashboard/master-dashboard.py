#!/usr/bin/env python3
"""
Master Dashboard - Unified Control Center for All NoizyLab Systems
==================================================================
"""

import streamlit as st
import requests
import sqlite3
import psutil
import os
from datetime import datetime
import plotly.express as px
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="NoizyLab Master Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🎛️ NoizyLab Master Dashboard</h1>', unsafe_allow_html=True)

# System Status
st.header("📊 System Status")

col1, col2, col3, col4, col5 = st.columns(5)

# Check services
services_status = {}
try:
    response = requests.get("http://localhost:8000/", timeout=2)
    services_status["V4 API"] = "🟢 Running" if response.status_code == 200 else "🟡 Warning"
except:
    services_status["V4 API"] = "🔴 Down"

try:
    response = requests.get("http://localhost:8002/mobile/health", timeout=2)
    services_status["Mobile API"] = "🟢 Running" if response.status_code == 200 else "🟡 Warning"
except:
    services_status["Mobile API"] = "🔴 Down"

try:
    response = requests.get("http://localhost:8001/docs", timeout=2)
    services_status["Webhook Hub"] = "🟢 Running" if response.status_code == 200 else "🟡 Warning"
except:
    services_status["Webhook Hub"] = "🔴 Down"

try:
    response = requests.get("http://localhost:8003/health", timeout=2)
    services_status["Slack Integration"] = "🟢 Running" if response.status_code == 200 else "🟡 Warning"
except:
    services_status["Slack Integration"] = "🔴 Down"

try:
    response = requests.get("http://localhost:8005/health", timeout=2)
    services_status["Network Agent"] = "🟢 Running" if response.status_code == 200 else "🟡 Warning"
except:
    services_status["Network Agent"] = "🔴 Down"

# System metrics
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

with col1:
    st.metric("CPU", f"{cpu:.1f}%")
with col2:
    st.metric("Memory", f"{memory:.1f}%")
with col3:
    st.metric("Disk", f"{disk:.1f}%")
with col4:
    st.metric("Services", f"{len([s for s in services_status.values() if '🟢' in s])}/{len(services_status)}")
with col5:
    st.metric("Time", datetime.now().strftime("%H:%M:%S"))

# Services Status
st.header("🔧 Services")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Service Status")
    for service, status in services_status.items():
        st.write(f"{status} {service}")

with col2:
    st.subheader("Quick Actions")
    if st.button("🔄 Restart All Services"):
        st.info("Restarting services...")
    if st.button("🌍 Run HealTheWorld"):
        st.info("Running healing process...")
    if st.button("⚡ Optimize All"):
        st.info("Optimizing systems...")

# Email System
st.header("📧 Email System")

col1, col2, col3 = st.columns(3)

# Email stats
base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
db_path = base / "email_intelligence.db"

if db_path.exists():
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Email stats
    cursor.execute("SELECT COUNT(*) FROM email_list")
    total_emails = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM email_list WHERE valid = 1")
    valid_emails = cursor.fetchone()[0]
    
    # History stats
    try:
        cursor.execute("SELECT COUNT(*) FROM email_history")
        sent_emails = cursor.fetchone()[0]
    except:
        sent_emails = 0
    
    # Contacts
    try:
        cursor.execute("SELECT COUNT(*) FROM email_contacts")
        contacts = cursor.fetchone()[0]
    except:
        contacts = 0
    
    conn.close()
    
    with col1:
        st.metric("Total Emails", total_emails)
    with col2:
        st.metric("Valid Emails", valid_emails)
    with col3:
        st.metric("Sent Emails", sent_emails)
    
    st.metric("Contacts", contacts)
else:
    st.info("Email database not found")

# Email Actions
st.subheader("Email Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📧 Send Test Email"):
        st.info("Email sending interface...")
with col2:
    if st.button("📋 View History"):
        st.info("Opening email history...")
with col3:
    if st.button("👥 Manage Contacts"):
        st.info("Opening contacts...")

# Slack Integration
st.header("💬 Slack Integration")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Slack Status")
    slack_token = os.getenv("SLACK_BOT_TOKEN", "")
    if slack_token:
        st.success("✅ Slack Bot Token configured")
        
        # Get Slack stats
        try:
            response = requests.get("http://localhost:8003/health", timeout=2)
            if response.status_code == 200:
                st.success("✅ Slack API Server running")
        except:
            st.warning("⚠️ Slack API Server not running")
    else:
        st.warning("⚠️ Slack Bot Token not configured")
    
    # Slack database stats
    slack_db = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
    if slack_db.exists():
        try:
            conn = sqlite3.connect(str(slack_db))
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM slack_notifications WHERE sent_at > datetime('now', '-24 hours')")
            notifications_24h = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM slack_channels")
            channels_count = cursor.fetchone()[0]
            
            conn.close()
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Messages (24h)", notifications_24h)
            with col_b:
                st.metric("Channels", channels_count)
        except:
            pass

with col2:
    st.subheader("Quick Actions")
    if st.button("💬 Open Slack Dashboard"):
        st.info("Run: streamlit run integrations/slack/slack_dashboard.py --server.port 8506")
    if st.button("📨 Send Test Alert"):
        try:
            response = requests.post("http://localhost:8003/notify/system-alert", json={
                "title": "Test Alert",
                "message": "This is a test alert from NoizyLab Master Dashboard",
                "level": "info"
            }, timeout=2)
            if response.status_code == 200:
                st.success("✅ Test alert sent!")
            else:
                st.error("❌ Failed to send alert")
        except:
            st.error("❌ Slack service not available")
    if st.button("🔄 View Slack Logs"):
        st.info("Opening Slack logs...")

# Network Monitoring
st.header("🌐 Network Monitoring (DGS1210)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Network Agent Status")
    try:
        response = requests.get("http://localhost:8005/health", timeout=2)
        if response.status_code == 200:
            data = response.json()
            st.success("✅ Network Agent running")
            
            stats = data.get("statistics", {})
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Active Devices", stats.get("active_devices", 0))
            with col_b:
                st.metric("Total Handshakes", stats.get("total_handshakes", 0))
            with col_c:
                success_rate = stats.get("success_rate", 0)
                st.metric("Success Rate", f"{success_rate:.1f}%")
    except:
        st.error("❌ Network Agent not running")
        if st.button("🚀 Start Network Agent"):
            st.info("Run: python3 network/network_agent_service.py")

with col2:
    st.subheader("MC96 Devices")
    try:
        response = requests.get("http://localhost:8005/mc96/devices", timeout=2)
        if response.status_code == 200:
            data = response.json()
            mc96_count = data.get("count", 0)
            
            st.metric("Connected MC96 Devices", mc96_count)
            
            if mc96_count > 0:
                st.success(f"✅ {mc96_count} MC96 device(s) online")
                
                devices = data.get("devices", {})
                for port, device_data in devices.items():
                    device = device_data.get("device", {})
                    handshake = device_data.get("handshake", {})
                    
                    with st.expander(f"Port {port}: {device.get('hostname', 'Unknown')}"):
                        st.write(f"**MAC:** {device.get('mac', 'Unknown')}")
                        st.write(f"**IP:** {device.get('ip', 'Unknown')}")
                        st.write(f"**Handshake:** {'✅ Success' if handshake.get('success') else '❌ Failed'}")
                        st.write(f"**Response Time:** {handshake.get('response_time', 0):.2f}s")
            else:
                st.info("No MC96 devices connected")
    except:
        st.info("Network agent not available")

# Port Status
st.subheader("Switch Port Status")
try:
    response = requests.get("http://localhost:8005/ports", timeout=2)
    if response.status_code == 200:
        data = response.json()
        ports = data.get("ports", {})
        
        port_cols = st.columns(10)
        for i, (port_num, port_data) in enumerate(sorted(ports.items(), key=lambda x: int(x[0]))):
            with port_cols[i]:
                status = port_data.get("link_status", "down")
                emoji = "🟢" if status == "up" else "⚪"
                device = port_data.get("device")
                
                st.markdown(f"**{emoji} P{port_num}**")
                if device:
                    st.caption(device.get("hostname", "Device")[:8])
except:
    st.info("Port status not available")

# Jumbo Frames Status
st.subheader("🔥 Jumbo Frames (Hot Rod Mode)")
try:
    import subprocess
    result = subprocess.run(['ifconfig'], capture_output=True, text=True, timeout=2)
    
    # Find primary interface MTU
    mtu_found = False
    for line in result.stdout.split('\n'):
        if 'en0' in line or ('mtu 9000' in line and mtu_found):
            if 'mtu' in line.lower():
                parts = line.split()
                for i, part in enumerate(parts):
                    if part.lower() == 'mtu' and i + 1 < len(parts):
                        mtu = int(parts[i + 1])
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Current MTU", mtu)
                        with col2:
                            if mtu >= 9000:
                                st.metric("Status", "🔥 HOT ROD!")
                            else:
                                st.metric("Status", "Standard")
                        with col3:
                            if mtu >= 9000:
                                st.metric("Performance", "+15%")
                            else:
                                if st.button("🔥 Enable Hot Rod"):
                                    st.info("Run: sudo python3 network/jumbo_frame_manager.py hotrod")
                        
                        mtu_found = True
                        break
        
        if mtu_found:
            break
    
    if not mtu_found:
        if st.button("🔥 Configure Jumbo Frames"):
            st.info("Run: ./🔥_HOT_ROD_MC96.sh")
except:
    st.info("MTU detection not available")

# Cloudflare Integration
st.header("☁️ Cloudflare Integration")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Cloudflare Status")
    cf_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
    if cf_token:
        st.success("✅ Cloudflare API Token configured")
    else:
        st.warning("⚠️ Cloudflare API Token not set")
    
    if st.button("🚀 Open Cloudflare Dashboard"):
        st.info("Opening Cloudflare Dashboard...")
        # Will open in new tab

with col2:
    st.subheader("Quick Actions")
    if st.button("☁️ Deploy Workers"):
        st.info("Deploying Cloudflare Workers...")
    if st.button("💾 Sync D1 Database"):
        st.info("Syncing with D1 database...")

# System Health
st.header("🏥 System Health")

# Database health
databases = [
    ("Email DB", "email-intelligence/email_intelligence.db"),
    ("Auth DB", "security/auth.db"),
    ("Webhook DB", "integrations/webhooks.db")
]

db_status = []
for name, path in databases:
    full_path = base.parent / path
    if full_path.exists():
        try:
            conn = sqlite3.connect(str(full_path))
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM sqlite_master")
            db_status.append((name, "🟢 Healthy"))
            conn.close()
        except:
            db_status.append((name, "🔴 Error"))
    else:
        db_status.append((name, "⚠️ Missing"))

for name, status in db_status:
    st.write(f"{status} {name}")

# Quick Links
st.sidebar.header("🔗 Quick Links")
st.sidebar.markdown("""
- [Email Dashboard](http://localhost:8501)
- [V4 API](http://localhost:8000)
- [Mobile API](http://localhost:8002)
- [Webhook Hub](http://localhost:8001)
- [Slack Integration](http://localhost:8506)
- [Slack API](http://localhost:8003)
- [Network Agent](http://localhost:8005)
- [Cloudflare Dashboard](http://localhost:8504)
""")

st.sidebar.header("🛠️ Tools")
st.sidebar.markdown("""
- HealTheWorld
- Code Fixer
- Performance Optimizer
- Health Monitor
""")

# Auto-refresh
if st.sidebar.checkbox("Auto-refresh (30s)"):
    import time
    time.sleep(30)
    st.rerun()

