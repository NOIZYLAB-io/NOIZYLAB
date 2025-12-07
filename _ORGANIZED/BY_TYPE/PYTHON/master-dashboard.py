#!/usr/bin/env python3
"""
Master Dashboard - Unified Control Center for All NoizyLab Systems
==================================================================
"""

import streamlit as st
import requests
import sqlite3
import psutil
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

