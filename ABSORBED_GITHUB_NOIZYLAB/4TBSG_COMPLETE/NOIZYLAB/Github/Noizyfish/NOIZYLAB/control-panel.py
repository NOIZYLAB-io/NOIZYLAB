#!/usr/bin/env python3
#!/usr/bin/env python3
"""
NoizyLab Control Panel - Unified management interface
======================================================
"""

import streamlit as st
import subprocess
import requests
import json
from pathlib import Path

st.set_page_config(page_title="NoizyLab Control Panel", layout="wide")

st.title("🎛️ NoizyLab Control Panel")
st.markdown("Unified management for all NoizyLab tools")

# Tool status
st.header("📊 Tool Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Email Intelligence
    try:
        response = requests.get("http://localhost:8000", timeout=2)
        st.success("✅ Email Intelligence API")
    except:
        st.error("❌ Email Intelligence API")
    
    try:
        response = requests.get("http://localhost:8501", timeout=2)
        st.success("✅ Email Dashboard")
    except:
        st.error("❌ Email Dashboard")

with col2:
    # Universal Blocker
    if Path("/etc/hosts").exists():
        with open("/etc/hosts") as f:
            if "Universal Blocker" in f.read():
                st.success("✅ Universal Blocker")
            else:
                st.warning("⚠️ Universal Blocker (not active)")
    else:
        st.info("ℹ️ Universal Blocker (check hosts file)")

with col3:
    # iMessage Filter
    launch_agent = Path.home() / "Library/LaunchAgents/com.noizylab.imessage-spam-filter.plist"
    if launch_agent.exists():
        st.success("✅ iMessage Filter")
    else:
        st.info("ℹ️ iMessage Filter (not auto-enabled)")

with col4:
    # System
    import psutil
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    st.metric("CPU", f"{cpu:.1f}%")
    st.metric("Memory", f"{mem:.1f}%")

# Quick actions
st.header("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Start All Services", use_container_width=True):
        st.info("Starting all services...")
        # Start services

with col2:
    if st.button("🛑 Stop All Services", use_container_width=True):
        st.info("Stopping all services...")

with col3:
    if st.button("🔄 Restart All", use_container_width=True):
        st.info("Restarting...")

# Service management
st.header("🔧 Service Management")

services = {
    "Email Intelligence": {
        "start": "cd ~/NOIZYLAB/email-intelligence && python3 api_server_v3.py &",
        "stop": "pkill -f api_server_v3.py",
        "status": "http://localhost:8000"
    },
    "Universal Blocker": {
        "start": "cd ~/NOIZYLAB/universal-blocker && sudo ./setup-blocker-v3.sh",
        "status": "check_hosts"
    }
}

for service, config in services.items():
    with st.expander(service):
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"▶️ Start {service}"):
                subprocess.Popen(config["start"], shell=True)
                st.success(f"Started {service}")
        with col2:
            if "stop" in config:
                if st.button(f"⏹️ Stop {service}"):
                    subprocess.run(config["stop"], shell=True)
                    st.success(f"Stopped {service}")

