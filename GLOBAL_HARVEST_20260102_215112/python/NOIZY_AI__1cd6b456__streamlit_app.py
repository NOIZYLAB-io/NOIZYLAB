#!/usr/bin/env python3
"""
GABRIEL Dashboard - Streamlit UI
Interactive web interface for file management
"""

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration
API_URL = "http://localhost:8080"
st.set_page_config(
    page_title="GABRIEL File Suite",
    page_icon="🗂️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .stat-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🗂️ GABRIEL File Suite</div>', unsafe_allow_html=True)
st.markdown("**Intelligent File Management for Network Drives**")

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=GABRIEL", width=150)
    st.markdown("### Navigation")
    page = st.radio("", ["📊 Dashboard", "🔍 Search", "📁 Categories", "🔄 Duplicates", "⚙️ Actions"])
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    
    try:
        response = requests.get(f"{API_URL}/api/health")
        if response.ok:
            st.success("✅ API Connected")
        else:
            st.error("❌ API Offline")
    except:
        st.error("❌ API Offline")

# Helper function to fetch data
def fetch_stats():
    try:
        response = requests.get(f"{API_URL}/api/stats")
        if response.ok:
            return response.json()
        return None
    except:
        return None

# Page: Dashboard
if page == "📊 Dashboard":
    st.markdown("## 📊 Overview")
    
    stats = fetch_stats()
    
    if stats:
        # Top metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Files", f"{stats['total_files']:,}")
        with col2:
            st.metric("Total Size", f"{stats['total_size_gb']} GB")
        with col3:
            st.metric("Categories", len(stats['categories']))
        with col4:
            st.metric("File Types", len(stats['top_extensions']))
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📁 Files by Category")
            if stats['categories']:
                df_cat = pd.DataFrame(stats['categories'])
                fig = px.pie(df_cat, names='category', values='count', 
                            title="File Distribution")
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 💾 Storage by Category")
            if stats['categories']:
                df_cat = pd.DataFrame(stats['categories'])
                fig = px.bar(df_cat, x='category', y='size_gb',
                            title="Storage Usage (GB)")
                st.plotly_chart(fig, use_container_width=True)
        
        # Top extensions
        st.markdown("### 📄 Top File Extensions")
        if stats['top_extensions']:
            df_ext = pd.DataFrame(stats['top_extensions'])
            st.dataframe(df_ext, use_container_width=True)
    
    else:
        st.error("Failed to load statistics. Is the API running?")

# Page: Search
elif page == "🔍 Search":
    st.markdown("## 🔍 File Search")
    
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        query = st.text_input("Search files", placeholder="Enter filename...")
    with col2:
        category = st.selectbox("Category", ["All", "Audio", "Design", "Code", "Documents", "Video"])
    with col3:
        limit = st.number_input("Limit", min_value=10, max_value=1000, value=100)
    
    if st.button("Search", type="primary"):
        with st.spinner("Searching..."):
            try:
                params = {"query": query, "limit": limit}
                if category != "All":
                    params["category"] = category
                
                response = requests.get(f"{API_URL}/api/search", params=params)
                
                if response.ok:
                    data = response.json()
                    st.success(f"Found {data['count']} files")
                    
                    if data['results']:
                        df = pd.DataFrame(data['results'])
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.info("No files found")
                else:
                    st.error("Search failed")
            except Exception as e:
                st.error(f"Error: {e}")

# Page: Categories
elif page == "📁 Categories":
    st.markdown("## 📁 File Categories")
    
    try:
        response = requests.get(f"{API_URL}/api/categories")
        if response.ok:
            data = response.json()
            categories = data['categories']
            
            if categories:
                df = pd.DataFrame(categories)
                
                # Summary cards
                cols = st.columns(len(categories) if len(categories) <= 4 else 4)
                for i, cat in enumerate(categories[:4]):
                    with cols[i]:
                        st.metric(
                            cat['category'],
                            f"{cat['count']} files",
                            f"{cat['size_gb']} GB"
                        )
                
                # Detailed table
                st.markdown("### 📊 Category Details")
                st.dataframe(df, use_container_width=True)
                
                # Visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    fig = px.treemap(df, path=['category'], values='count',
                                    title="File Count by Category")
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    fig = px.scatter(df, x='count', y='size_gb', size='count',
                                    text='category', title="Files vs Storage")
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to load categories")
    except Exception as e:
        st.error(f"Error: {e}")

# Page: Duplicates
elif page == "🔄 Duplicates":
    st.markdown("## 🔄 Duplicate Files")
    
    try:
        response = requests.get(f"{API_URL}/api/duplicates")
        if response.ok:
            data = response.json()
            
            st.metric("Total Wasted Space", f"{data['total_wasted_gb']} GB", delta="-cleanup potential")
            st.metric("Duplicate Groups", data['duplicate_groups'])
            
            if data['duplicates']:
                st.markdown("### 📋 Duplicate Groups")
                
                for dup in data['duplicates'][:20]:  # Show top 20
                    with st.expander(f"🔄 {dup['count']} copies - Wasting {dup['wasted_space_mb']} MB"):
                        df = pd.DataFrame(dup['files'])
                        st.dataframe(df, use_container_width=True)
            else:
                st.success("✅ No duplicates found!")
        else:
            st.error("Failed to load duplicates")
    except Exception as e:
        st.error(f"Error: {e}")

# Page: Actions
elif page == "⚙️ Actions":
    st.markdown("## ⚙️ File Actions")
    
    tab1, tab2, tab3 = st.tabs(["🔍 Scan", "🧠 Classify", "📁 Organize"])
    
    with tab1:
        st.markdown("### 🔍 Scan Volume")
        volume_path = st.text_input("Volume Path", "/Volumes/GABRIEL")
        workers = st.slider("Worker Threads", 1, 16, 8)
        
        if st.button("Start Scan", type="primary"):
            st.info("🚧 Scan functionality requires CLI. Use: `gabriel.py scan <volume> --database gabriel.db`")
    
    with tab2:
        st.markdown("### 🧠 Classify Files")
        batch_size = st.number_input("Batch Size", 10, 1000, 100)
        use_ai = st.checkbox("Use AI Classification", value=False)
        
        if st.button("Start Classification", type="primary"):
            st.info("🚧 Classification requires CLI. Use: `gabriel.py classify gabriel.db --batch 100`")
    
    with tab3:
        st.markdown("### 📁 Organize Files")
        output_path = st.text_input("Output Path", "/Volumes/GABRIEL/Organized")
        mode = st.selectbox("Mode", ["symlink", "copy", "move", "hardlink"])
        dry_run = st.checkbox("Dry Run", value=True)
        
        if st.button("Start Organization", type="primary"):
            st.info(f"🚧 Organization requires CLI. Use: `gabriel.py organize gabriel.db {output_path} --mode {mode}`")

# Footer
st.markdown("---")
st.markdown("**GABRIEL File Suite** | Production-ready file intelligence for network drives")
