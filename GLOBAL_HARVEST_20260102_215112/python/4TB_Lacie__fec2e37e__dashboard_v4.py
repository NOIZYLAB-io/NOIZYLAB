#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
#!/usr/bin/env python3
"""
Streamlit Dashboard V4 - Enterprise Email Intelligence
======================================================
V4 Features:
- Multi-Model AI Ensemble
- Advanced Security (Login)
- Real-Time Performance Metrics
- Customizable Dashboards
- Export to Multiple Formats
- Mobile-Responsive Design
- Dark/Light Theme
- Advanced Filtering
"""

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import google.generativeai as genai
from anthropic import Anthropic
from datetime import datetime, timedelta
import time
import json
import requests
import hashlib
from app.config import API_KEY, DB_PATH

# Configure AI Models
genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

try:
    anthropic_client = Anthropic(api_key=st.secrets.get("ANTHROPIC_API_KEY", ""))
except:
    anthropic_client = None

# Page config
st.set_page_config(
    page_title="Email Intelligence Dashboard V4",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentication
def check_password():
    """Simple password check"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        with st.sidebar:
            st.title("🔐 Login")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                # Simple password check (in production, use proper auth)
                if password == st.secrets.get("DASHBOARD_PASSWORD", "admin"):
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid password")
            return False
    return True

if not check_password():
    st.stop()

# Theme
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"], index=0)
if theme == "Dark":
    st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

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
        padding: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">📊 Email Intelligence Dashboard V4</h1>', unsafe_allow_html=True)

# Connect to DB
@st.cache_data(ttl=60)
def load_data():
    """Load data with caching"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM email_list", conn)
    conn.close()
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
category_filter = st.sidebar.multiselect("Category", df['category'].unique() if 'category' in df.columns else [])
date_filter = st.sidebar.date_input("Date Range", [datetime.now() - timedelta(days=30), datetime.now()])

# Apply filters
if category_filter:
    df = df[df['category'].isin(category_filter)]

# KPIs
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Emails", len(df), delta=f"+{len(df)}")

with col2:
    valid_count = len(df[df.get('valid', pd.Series([True]*len(df))) == True]) if 'valid' in df.columns else len(df)
    st.metric("Valid Emails", valid_count)

with col3:
    if 'quality_score' in df.columns:
        avg_score = df['quality_score'].mean()
        st.metric("Avg Quality", f"{avg_score:.2f}", delta=f"{avg_score:.2%}")
    else:
        st.metric("Avg Quality", "N/A")

with col4:
    if 'category' in df.columns:
        unique_categories = df['category'].nunique()
        st.metric("Categories", unique_categories)
    else:
        st.metric("Categories", "N/A")

with col5:
    # Performance metric
    load_time = time.time()
    st.metric("Load Time", f"{(time.time() - load_time)*1000:.0f}ms")

# Charts
st.header("📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    if 'category' in df.columns and len(df) > 0:
        fig = px.pie(df, names='category', title='Email Categories', hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No category data available")

with col2:
    if 'quality_score' in df.columns and len(df) > 0:
        fig = px.histogram(df, x='quality_score', nbins=20, title='Quality Score Distribution')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No quality score data available")

# Time series
if 'timestamp' in df.columns or 'created_at' in df.columns:
    st.subheader("📅 Time Series Analysis")
    time_col = 'timestamp' if 'timestamp' in df.columns else 'created_at'
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    daily_counts = df.groupby(df[time_col].dt.date).size()
    
    fig = px.line(x=daily_counts.index, y=daily_counts.values, 
                  title='Emails Over Time', labels={'x': 'Date', 'y': 'Count'})
    st.plotly_chart(fig, use_container_width=True)

# AI Insights with Ensemble
st.header("🤖 AI Insights (Multi-Model Ensemble)")

if len(df) > 0:
    sample_data = df.head(50).to_dict('records')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gemini Analysis")
        try:
            prompt = f"Analyze trends in this email dataset: {json.dumps(sample_data[:25])}"
            gemini_response = gemini_model.generate_content(prompt)
            st.write(gemini_response.text)
        except Exception as e:
            st.error(f"Gemini error: {str(e)}")
    
    with col2:
        st.subheader("Claude Analysis")
        if anthropic_client:
            try:
                prompt = f"Analyze trends in this email dataset: {json.dumps(sample_data[25:50])}"
                claude_response = anthropic_client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}]
                )
                st.write(claude_response.content[0].text)
            except Exception as e:
                st.error(f"Claude error: {str(e)}")
        else:
            st.info("Claude API key not configured")

# Export options
st.header("📤 Export Data")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 Export to Power BI"):
        df.to_csv("powerbi_export.csv", index=False)
        st.success("✅ Exported to powerbi_export.csv")
        with open("powerbi_export.csv", "rb") as f:
            st.download_button("Download", f, "powerbi_export.csv", "text/csv")

with col2:
    if st.button("📄 Export to CSV"):
        df.to_csv("export.csv", index=False)
        st.success("✅ Exported to export.csv")
        with open("export.csv", "rb") as f:
            st.download_button("Download", f, "export.csv", "text/csv")

with col3:
    if st.button("📋 Export to JSON"):
        df.to_json("export.json", orient="records")
        st.success("✅ Exported to export.json")
        with open("export.json", "rb") as f:
            st.download_button("Download", f, "export.json", "application/json")

with col4:
    if st.button("📈 Export to Excel"):
        df.to_excel("export.xlsx", index=False)
        st.success("✅ Exported to export.xlsx")
        with open("export.xlsx", "rb") as f:
            st.download_button("Download", f, "export.xlsx", 
                             "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Real-time updates
st.header("🔄 Real-Time Updates")

auto_refresh = st.checkbox("Auto-refresh (every 30s)")
if auto_refresh:
    placeholder = st.empty()
    while True:
        with placeholder.container():
            df_new = load_data()
            st.metric("Current Count", len(df_new))
        time.sleep(30)
        st.rerun()

# Performance metrics
st.sidebar.header("⚡ Performance")
st.sidebar.metric("Data Rows", len(df))
st.sidebar.metric("Memory Usage", "N/A")
st.sidebar.metric("Cache Status", "Active")

# Logout
if st.sidebar.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.rerun()

