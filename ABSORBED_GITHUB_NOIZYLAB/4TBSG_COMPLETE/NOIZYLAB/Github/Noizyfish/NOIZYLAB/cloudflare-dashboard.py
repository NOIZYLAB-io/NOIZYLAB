#!/usr/bin/env python3
"""
Cloudflare Dashboard - Streamlit Dashboard for Cloudflare Management
=====================================================================
"""

import streamlit as st
import requests
import json
import os
from datetime import datetime, timedelta
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Cloudflare HotRod Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration
API_TOKEN = st.sidebar.text_input("Cloudflare API Token", type="password", value=os.getenv("CLOUDFLARE_API_TOKEN", ""))
ACCOUNT_ID = st.sidebar.text_input("Account ID", value=os.getenv("CLOUDFLARE_ACCOUNT_ID", ""))
ZONE_ID = st.sidebar.text_input("Zone ID", value=os.getenv("CLOUDFLARE_ZONE_ID", ""))

BASE_URL = "https://api.cloudflare.com/client/v4"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

st.title("🚀 Cloudflare HotRod Dashboard")

if not API_TOKEN:
    st.warning("⚠️ Please enter your Cloudflare API Token in the sidebar")
    st.stop()

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Zones", "Workers", "D1 Databases", "Email Routing"])

with tab1:
    st.header("📊 Overview")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    # Get zones
    try:
        response = requests.get(f"{BASE_URL}/zones", headers=HEADERS, timeout=10)
        zones = response.json().get("result", []) if response.status_code == 200 else []
        
        with col1:
            st.metric("Zones", len(zones))
        
        # Get workers
        if ACCOUNT_ID:
            response = requests.get(
                f"{BASE_URL}/accounts/{ACCOUNT_ID}/workers/scripts",
                headers=HEADERS,
                timeout=10
            )
            workers = response.json().get("result", []) if response.status_code == 200 else []
            
            with col2:
                st.metric("Workers", len(workers))
            
            # Get D1 databases
            response = requests.get(
                f"{BASE_URL}/accounts/{ACCOUNT_ID}/d1/database",
                headers=HEADERS,
                timeout=10
            )
            d1_dbs = response.json().get("result", []) if response.status_code == 200 else []
            
            with col3:
                st.metric("D1 Databases", len(d1_dbs))
        else:
            with col2:
                st.metric("Workers", "N/A")
            with col3:
                st.metric("D1 Databases", "N/A")
        
        with col4:
            st.metric("Status", "✅ Connected" if zones else "⚠️ Check Config")
    
    except Exception as e:
        st.error(f"Error: {e}")

with tab2:
    st.header("🌐 Zones")
    
    if zones:
        # Zone table
        zone_data = []
        for zone in zones:
            zone_data.append({
                "Name": zone.get("name", ""),
                "Status": zone.get("status", ""),
                "Plan": zone.get("plan", {}).get("name", ""),
                "Created": zone.get("created_on", "")[:10] if zone.get("created_on") else ""
            })
        
        df = pd.DataFrame(zone_data)
        st.dataframe(df, use_container_width=True)
        
        # Zone selector
        if zones:
            selected_zone = st.selectbox("Select Zone", [z["name"] for z in zones])
            selected_zone_id = next(z["id"] for z in zones if z["name"] == selected_zone)
            
            if st.button("⚡ Optimize Zone"):
                st.info("Optimizing zone settings...")
                # Call optimization
    else:
        st.info("No zones found")

with tab3:
    st.header("⚙️ Workers")
    
    if ACCOUNT_ID:
        try:
            response = requests.get(
                f"{BASE_URL}/accounts/{ACCOUNT_ID}/workers/scripts",
                headers=HEADERS,
                timeout=10
            )
            
            if response.status_code == 200:
                workers = response.json().get("result", [])
                
                if workers:
                    worker_data = []
                    for worker in workers:
                        worker_data.append({
                            "Name": worker.get("id", ""),
                            "Created": worker.get("created_on", "")[:10] if worker.get("created_on") else "",
                            "Modified": worker.get("modified_on", "")[:10] if worker.get("modified_on") else ""
                        })
                    
                    df = pd.DataFrame(worker_data)
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No workers deployed")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Account ID required to view workers")

with tab4:
    st.header("💾 D1 Databases")
    
    if ACCOUNT_ID:
        try:
            response = requests.get(
                f"{BASE_URL}/accounts/{ACCOUNT_ID}/d1/database",
                headers=HEADERS,
                timeout=10
            )
            
            if response.status_code == 200:
                d1_dbs = response.json().get("result", [])
                
                if d1_dbs:
                    db_data = []
                    for db in d1_dbs:
                        db_data.append({
                            "Name": db.get("name", ""),
                            "UUID": db.get("uuid", ""),
                            "Created": db.get("created_at", "")[:10] if db.get("created_at") else ""
                        })
                    
                    df = pd.DataFrame(db_data)
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No D1 databases found")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Account ID required to view D1 databases")

with tab5:
    st.header("📧 Email Routing")
    
    if ZONE_ID:
        st.info("Email Routing configuration")
        
        if st.button("Enable Email Routing"):
            try:
                response = requests.post(
                    f"{BASE_URL}/zones/{ZONE_ID}/email/routing/enable",
                    headers=HEADERS,
                    timeout=10
                )
                if response.status_code == 200:
                    st.success("✅ Email Routing enabled!")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Zone ID required for Email Routing")

# Sidebar actions
st.sidebar.header("⚡ Quick Actions")
if st.sidebar.button("🔄 Refresh"):
    st.rerun()

if st.sidebar.button("⚡ Optimize All Zones"):
    st.sidebar.info("Optimizing all zones...")

