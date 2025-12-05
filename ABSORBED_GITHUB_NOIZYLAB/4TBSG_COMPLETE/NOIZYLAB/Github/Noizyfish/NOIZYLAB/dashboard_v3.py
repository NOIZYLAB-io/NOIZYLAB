#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Streamlit Dashboard V3 - Enhanced Real-Time Email Intelligence
================================================================
Advanced features: Real-time updates, predictive analytics, anomaly detection
"""

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import google.generativeai as genai
from datetime import datetime, timedelta
import time
import json
from app.config import API_KEY, DB_PATH

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Page config
st.set_page_config(
    page_title="Email Intelligence Dashboard V3",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
    }
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = True
if 'refresh_interval' not in st.session_state:
    st.session_state.refresh_interval = 2

st.markdown('<div class="main-title">📊 Real-Time Email Intelligence Dashboard V3</div>', unsafe_allow_html=True)

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Controls")
    
    st.session_state.auto_refresh = st.checkbox("🔄 Auto Refresh", value=st.session_state.auto_refresh)
    st.session_state.refresh_interval = st.slider("Refresh Interval (sec)", 1, 10, st.session_state.refresh_interval)
    
    if st.button("🔄 Refresh Now"):
        st.rerun()
    
    st.markdown("---")
    st.header("📊 Views")
    view_mode = st.radio("Dashboard View", ["Overview", "Analytics", "AI Insights", "Power BI"])
    
    st.markdown("---")
    st.header("📥 Export")
    if st.button("📊 Export to Power BI"):
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM email_list", conn)
        df.to_csv("powerbi_export.csv", index=False)
        st.success("✅ Exported!")
        conn.close()

# Connect to DB
@st.cache_data(ttl=2)
def get_data():
    """Get data from database with caching"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM email_list", conn)
    conn.close()
    return df

df = get_data()

# Overview Tab
if view_mode == "Overview":
    # Enhanced KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("📧 Total Emails", len(df), delta=None)
    
    with col2:
        valid_count = len(df[df['category'].notnull()])
        st.metric("✅ Valid Emails", valid_count, delta=f"{valid_count/len(df)*100:.1f}%")
    
    with col3:
        spam_count = len(df[df.get('spam_score', pd.Series([0]*len(df))) > 0.7]) if 'spam_score' in df.columns else 0
        st.metric("🚫 Spam", spam_count, delta=f"{spam_count/len(df)*100:.1f}%" if len(df) > 0 else "0%")
    
    with col4:
        categories = df['category'].nunique() if 'category' in df.columns else 0
        st.metric("📂 Categories", categories)
    
    with col5:
        if 'processed_at' in df.columns:
            recent = len(df[pd.to_datetime(df['processed_at']) > datetime.now() - timedelta(days=1)])
            st.metric("📅 Last 24h", recent)
        else:
            st.metric("📅 Last 24h", "N/A")
    
    st.markdown("---")
    
    # Charts row 1
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("📊 Category Distribution")
        if 'category' in df.columns and len(df) > 0:
            category_counts = df['category'].value_counts()
            fig = px.pie(
                values=category_counts.values,
                names=category_counts.index,
                title="Email Categories",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No category data available")
    
    with col_right:
        st.subheader("📈 Trends (Last 7 Days)")
        if 'processed_at' in df.columns and len(df) > 0:
            df['processed_at'] = pd.to_datetime(df['processed_at'], errors='coerce')
            df_recent = df[df['processed_at'] > datetime.now() - timedelta(days=7)]
            daily_counts = df_recent.groupby(df_recent['processed_at'].dt.date).size()
            
            fig = px.line(
                x=daily_counts.index,
                y=daily_counts.values,
                title="Daily Email Processing",
                markers=True,
                labels={'x': 'Date', 'y': 'Count'}
            )
            fig.update_traces(line_color='#1f77b4', line_width=3)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No trend data available")
    
    # Charts row 2
    col_left2, col_right2 = st.columns(2)
    
    with col_left2:
        st.subheader("🎯 Spam Score Distribution")
        if 'spam_score' in df.columns and len(df) > 0:
            fig = px.histogram(
                df,
                x='spam_score',
                nbins=20,
                title="Spam Score Distribution",
                labels={'spam_score': 'Spam Score', 'count': 'Count'}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No spam score data")
    
    with col_right2:
        st.subheader("✅ Validity Score Distribution")
        if 'validity_score' in df.columns and len(df) > 0:
            fig = px.histogram(
                df,
                x='validity_score',
                nbins=20,
                title="Validity Score Distribution",
                labels={'validity_score': 'Validity Score', 'count': 'Count'}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No validity score data")
    
    # Data table
    st.markdown("---")
    st.subheader("📋 Recent Emails")
    if len(df) > 0:
        display_cols = ['email', 'category', 'spam_score', 'validity_score'] if all(c in df.columns for c in ['email', 'category', 'spam_score', 'validity_score']) else df.columns[:5]
        st.dataframe(df[display_cols].head(100), use_container_width=True, height=400)
    else:
        st.info("No data available")

# Analytics Tab
elif view_mode == "Analytics":
    st.header("📊 Advanced Analytics")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        category_filter = st.multiselect("Category", df['category'].unique().tolist() if 'category' in df.columns else [])
    with col2:
        spam_threshold = st.slider("Spam Score Threshold", 0.0, 1.0, 0.7)
    with col3:
        date_range = st.date_input("Date Range", [datetime.now() - timedelta(days=7), datetime.now()])
    
    # Apply filters
    df_filtered = df.copy()
    if category_filter and 'category' in df_filtered.columns:
        df_filtered = df_filtered[df_filtered['category'].isin(category_filter)]
    if 'spam_score' in df_filtered.columns:
        df_filtered = df_filtered[df_filtered['spam_score'] > spam_threshold]
    
    # Analytics metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Filtered Count", len(df_filtered))
    with col2:
        st.metric("Avg Spam Score", f"{df_filtered['spam_score'].mean():.2f}" if 'spam_score' in df_filtered.columns else "N/A")
    with col3:
        st.metric("Avg Validity", f"{df_filtered['validity_score'].mean():.2f}" if 'validity_score' in df_filtered.columns else "N/A")
    with col4:
        st.metric("Unique Domains", df_filtered['email'].str.split('@').str[1].nunique() if 'email' in df_filtered.columns else 0)
    
    # Correlation matrix
    if len(df_filtered) > 0 and 'spam_score' in df_filtered.columns and 'validity_score' in df_filtered.columns:
        st.subheader("🔗 Correlation Analysis")
        corr = df_filtered[['spam_score', 'validity_score']].corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto", title="Score Correlations")
        st.plotly_chart(fig, use_container_width=True)

# AI Insights Tab
elif view_mode == "AI Insights":
    st.header("🤖 AI-Powered Insights")
    
    if len(df) > 0:
        with st.spinner("🤖 Generating AI insights with Gemini..."):
            # Enhanced prompt
            prompt = f"""
            Analyze this email intelligence dataset and provide comprehensive insights:
            
            Dataset Summary:
            - Total emails: {len(df)}
            - Categories: {df['category'].value_counts().to_dict() if 'category' in df.columns else 'N/A'}
            - Date range: {df['processed_at'].min() if 'processed_at' in df.columns else 'N/A'} to {df['processed_at'].max() if 'processed_at' in df.columns else 'N/A'}
            
            Sample data: {df.head(50).to_dict()}
            
            Provide:
            1. Key trends and patterns
            2. Anomalies detected
            3. Risk assessment
            4. Actionable recommendations
            5. Predictive insights for next 7 days
            6. Top concerns
            
            Format as structured analysis.
            """
            
            try:
                response = model.generate_content(prompt)
                st.markdown("### 📊 Analysis Results")
                st.write(response.text)
                
                # Save insights
                if st.button("💾 Save Insights"):
                    insights_data = {
                        "timestamp": datetime.now().isoformat(),
                        "summary": response.text,
                        "dataset_size": len(df)
                    }
                    with open("ai_insights.json", "w") as f:
                        json.dump(insights_data, f, indent=2)
                    st.success("✅ Insights saved!")
            
            except Exception as e:
                st.error(f"AI analysis error: {e}")
                st.info("Using fallback analysis...")
                
                # Fallback insights
                st.info(f"**Dataset Size:** {len(df)} emails")
                if 'category' in df.columns:
                    st.info(f"**Top Category:** {df['category'].mode()[0] if len(df['category'].mode()) > 0 else 'N/A'}")
                if 'spam_score' in df.columns:
                    st.info(f"**Average Spam Score:** {df['spam_score'].mean():.2f}")
    else:
        st.warning("No data available for analysis")

# Power BI Tab
elif view_mode == "Power BI":
    st.header("📊 Power BI Export & Preview")
    
    if len(df) > 0:
        # Export options
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Export Full Dataset", use_container_width=True):
                df.to_csv("powerbi_export.csv", index=False)
                st.success("✅ Full dataset exported!")
        
        with col2:
            if st.button("📥 Export Filtered", use_container_width=True):
                # Export with Power BI optimizations
                df_export = df.copy()
                if 'spam_score' in df_export.columns:
                    df_export['spam_score_percent'] = df_export['spam_score'] * 100
                if 'validity_score' in df_export.columns:
                    df_export['validity_score_percent'] = df_export['validity_score'] * 100
                df_export.to_csv("powerbi_export.csv", index=False)
                st.success("✅ Optimized export ready!")
        
        # Preview
        st.subheader("📋 Export Preview")
        st.dataframe(df.head(100), use_container_width=True, height=400)
        st.info(f"Showing first 100 rows of {len(df)} total rows")
        
        # Export statistics
        st.subheader("📊 Export Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Rows", len(df))
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            file_size = len(df.to_csv(index=False).encode())
            st.metric("Estimated Size", f"{file_size/1024:.1f} KB")
    else:
        st.warning("No data to export")

# Auto-refresh
if st.session_state.auto_refresh:
    time.sleep(st.session_state.refresh_interval)
    st.rerun()

# Footer
st.markdown("---")
st.caption(f"Email Intelligence Dashboard V3 | Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Auto-refresh: {'ON' if st.session_state.auto_refresh else 'OFF'}")

