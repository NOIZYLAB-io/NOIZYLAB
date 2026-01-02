#!/usr/bin/env python3
"""
NoizyLab Slack Management Dashboard
====================================
Streamlit dashboard for managing Slack integration
"""

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import os
import json
import plotly.express as px
import plotly.graph_objects as go

from slack_core import SlackClient, SlackBlockBuilder, SlackMessage


# Page config
st.set_page_config(
    page_title="NoizyLab Slack Integration",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #611f69, #e01e5a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .slack-card {
        background: linear-gradient(135deg, #611f69 0%, #e01e5a 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1rem;
    }
    .metric-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #611f69;
        margin-bottom: 1rem;
    }
    .success-msg {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .warning-msg {
        background: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .error-msg {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">💬 Slack Integration Dashboard</h1>', unsafe_allow_html=True)

# Initialize session state
if 'slack_client' not in st.session_state:
    try:
        st.session_state.slack_client = SlackClient()
        st.session_state.slack_connected = True
    except Exception as e:
        st.session_state.slack_connected = False
        st.session_state.error_message = str(e)

# Sidebar
st.sidebar.header("🔧 Slack Configuration")

# Check connection
if st.session_state.slack_connected:
    st.sidebar.success("✅ Connected to Slack")
else:
    st.sidebar.error("❌ Not Connected")
    if hasattr(st.session_state, 'error_message'):
        st.sidebar.error(st.session_state.error_message)
    
    st.sidebar.markdown("""
    ### Setup Instructions:
    1. Create a Slack App at [api.slack.com/apps](https://api.slack.com/apps)
    2. Add Bot Token Scopes:
       - `chat:write`
       - `channels:read`
       - `users:read`
       - `files:write`
       - `commands`
    3. Install app to workspace
    4. Set environment variables:
       ```bash
       export SLACK_BOT_TOKEN="xoxb-..."
       export SLACK_SIGNING_SECRET="..."
       ```
    """)

# Main tabs
if st.session_state.slack_connected:
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Overview",
        "📺 Channels",
        "👥 Users",
        "📨 Send Message",
        "📈 Analytics",
        "⚙️ Settings"
    ])
    
    client = st.session_state.slack_client
    db_path = client.db_path
    
    # Tab 1: Overview
    with tab1:
        st.header("📊 Slack Integration Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        # Get database stats
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM slack_channels")
        channel_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM slack_users WHERE is_bot = 0")
        user_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM slack_notifications WHERE sent_at > datetime('now', '-24 hours')")
        notifications_24h = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM slack_commands WHERE executed_at > datetime('now', '-24 hours')")
        commands_24h = cursor.fetchone()[0]
        
        conn.close()
        
        with col1:
            st.metric("📺 Channels", channel_count)
        with col2:
            st.metric("👥 Users", user_count)
        with col3:
            st.metric("📨 Messages (24h)", notifications_24h)
        with col4:
            st.metric("⚡ Commands (24h)", commands_24h)
        
        st.divider()
        
        # Recent activity
        st.subheader("📋 Recent Activity")
        
        conn = sqlite3.connect(str(db_path))
        
        # Recent notifications
        df_notifications = pd.read_sql_query("""
            SELECT notification_type, channel, message, status, sent_at
            FROM slack_notifications
            ORDER BY sent_at DESC
            LIMIT 10
        """, conn)
        
        if not df_notifications.empty:
            st.dataframe(df_notifications, use_container_width=True)
        else:
            st.info("No recent notifications")
        
        conn.close()
        
        # Quick actions
        st.divider()
        st.subheader("⚡ Quick Actions")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🔄 Sync Channels", use_container_width=True):
                with st.spinner("Syncing channels..."):
                    channels = client.list_channels(include_private=True)
                    st.success(f"✅ Synced {len(channels)} channels")
        
        with col2:
            if st.button("🔄 Sync Users", use_container_width=True):
                with st.spinner("Syncing users..."):
                    users = client.list_users()
                    st.success(f"✅ Synced {len(users)} users")
        
        with col3:
            if st.button("🧪 Test Connection", use_container_width=True):
                try:
                    channels = client.list_channels()
                    st.success("✅ Connection successful!")
                except Exception as e:
                    st.error(f"❌ Connection failed: {e}")
        
        with col4:
            if st.button("📊 Generate Report", use_container_width=True):
                st.info("Generating report...")
    
    # Tab 2: Channels
    with tab2:
        st.header("📺 Slack Channels")
        
        col1, col2 = st.columns([3, 1])
        
        with col2:
            if st.button("🔄 Refresh Channels", use_container_width=True):
                with st.spinner("Loading channels..."):
                    client.list_channels(include_private=True)
                    st.success("✅ Channels refreshed")
                    st.rerun()
        
        # Load channels from database
        conn = sqlite3.connect(str(db_path))
        df_channels = pd.read_sql_query("""
            SELECT name, is_private, is_archived, member_count, topic, purpose, updated_at
            FROM slack_channels
            ORDER BY member_count DESC
        """, conn)
        conn.close()
        
        if not df_channels.empty:
            # Filter options
            col1, col2, col3 = st.columns(3)
            
            with col1:
                show_archived = st.checkbox("Show Archived")
            with col2:
                show_private = st.checkbox("Show Private", value=True)
            with col3:
                search = st.text_input("🔍 Search channels")
            
            # Apply filters
            filtered_df = df_channels.copy()
            
            if not show_archived:
                filtered_df = filtered_df[filtered_df['is_archived'] == 0]
            
            if not show_private:
                filtered_df = filtered_df[filtered_df['is_private'] == 0]
            
            if search:
                filtered_df = filtered_df[filtered_df['name'].str.contains(search, case=False)]
            
            # Display channels
            st.dataframe(
                filtered_df,
                use_container_width=True,
                column_config={
                    "name": st.column_config.TextColumn("Channel Name", width="medium"),
                    "is_private": st.column_config.CheckboxColumn("Private"),
                    "is_archived": st.column_config.CheckboxColumn("Archived"),
                    "member_count": st.column_config.NumberColumn("Members"),
                    "topic": st.column_config.TextColumn("Topic", width="large"),
                    "updated_at": st.column_config.DatetimeColumn("Last Updated")
                }
            )
            
            # Channel stats
            st.divider()
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Channels", len(filtered_df))
            with col2:
                st.metric("Private Channels", len(filtered_df[filtered_df['is_private'] == 1]))
            with col3:
                st.metric("Archived Channels", len(df_channels[df_channels['is_archived'] == 1]))
        else:
            st.info("No channels found. Click 'Refresh Channels' to sync.")
    
    # Tab 3: Users
    with tab3:
        st.header("👥 Slack Users")
        
        col1, col2 = st.columns([3, 1])
        
        with col2:
            if st.button("🔄 Refresh Users", use_container_width=True):
                with st.spinner("Loading users..."):
                    client.list_users()
                    st.success("✅ Users refreshed")
                    st.rerun()
        
        # Load users from database
        conn = sqlite3.connect(str(db_path))
        df_users = pd.read_sql_query("""
            SELECT name, real_name, email, is_admin, is_bot, timezone, updated_at
            FROM slack_users
            ORDER BY name
        """, conn)
        conn.close()
        
        if not df_users.empty:
            # Filter options
            col1, col2, col3 = st.columns(3)
            
            with col1:
                show_bots = st.checkbox("Show Bots")
            with col2:
                admin_only = st.checkbox("Admins Only")
            with col3:
                user_search = st.text_input("🔍 Search users")
            
            # Apply filters
            filtered_users = df_users.copy()
            
            if not show_bots:
                filtered_users = filtered_users[filtered_users['is_bot'] == 0]
            
            if admin_only:
                filtered_users = filtered_users[filtered_users['is_admin'] == 1]
            
            if user_search:
                filtered_users = filtered_users[
                    filtered_users['name'].str.contains(user_search, case=False) |
                    filtered_users['real_name'].str.contains(user_search, case=False)
                ]
            
            # Display users
            st.dataframe(
                filtered_users,
                use_container_width=True,
                column_config={
                    "name": st.column_config.TextColumn("Username", width="medium"),
                    "real_name": st.column_config.TextColumn("Full Name", width="medium"),
                    "email": st.column_config.TextColumn("Email", width="medium"),
                    "is_admin": st.column_config.CheckboxColumn("Admin"),
                    "is_bot": st.column_config.CheckboxColumn("Bot"),
                    "timezone": st.column_config.TextColumn("Timezone"),
                    "updated_at": st.column_config.DatetimeColumn("Last Updated")
                }
            )
            
            # User stats
            st.divider()
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Users", len(filtered_users))
            with col2:
                st.metric("Admins", len(df_users[df_users['is_admin'] == 1]))
            with col3:
                st.metric("Bots", len(df_users[df_users['is_bot'] == 1]))
            with col4:
                st.metric("Regular Users", len(df_users[(df_users['is_bot'] == 0) & (df_users['is_admin'] == 0)]))
        else:
            st.info("No users found. Click 'Refresh Users' to sync.")
    
    # Tab 4: Send Message
    with tab4:
        st.header("📨 Send Slack Message")
        
        # Get channels for dropdown
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM slack_channels WHERE is_archived = 0 ORDER BY name")
        channels = cursor.fetchall()
        conn.close()
        
        if channels:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Message type selector
                message_type = st.radio(
                    "Message Type",
                    ["Simple Message", "Rich Notification", "Status Update"],
                    horizontal=True
                )
            
            with col2:
                # Channel selector
                channel_names = [f"#{name}" for _, name in channels]
                channel_ids = [id for id, _ in channels]
                
                selected_channel_idx = st.selectbox(
                    "Select Channel",
                    range(len(channel_names)),
                    format_func=lambda x: channel_names[x]
                )
                selected_channel = channel_ids[selected_channel_idx]
            
            st.divider()
            
            if message_type == "Simple Message":
                # Simple message form
                message_text = st.text_area("Message", height=150, placeholder="Enter your message here...")
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    username = st.text_input("Custom Username (optional)", placeholder="NoizyLab Bot")
                with col2:
                    emoji = st.text_input("Emoji (optional)", placeholder=":robot_face:")
                
                if st.button("📤 Send Message", type="primary", use_container_width=True):
                    if message_text:
                        try:
                            msg = SlackMessage(
                                channel=selected_channel,
                                text=message_text,
                                username=username if username else None,
                                icon_emoji=emoji if emoji else None
                            )
                            result = client.send_message(msg)
                            st.success("✅ Message sent successfully!")
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
                    else:
                        st.warning("Please enter a message")
            
            elif message_type == "Rich Notification":
                # Rich notification form
                title = st.text_input("Title", placeholder="Notification Title")
                message = st.text_area("Message", height=100, placeholder="Notification message...")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    color = st.selectbox("Color", ["good", "warning", "danger", "#36a64f"])
                
                with col2:
                    add_fields = st.checkbox("Add custom fields")
                
                fields = []
                if add_fields:
                    st.subheader("Custom Fields")
                    num_fields = st.number_input("Number of fields", min_value=1, max_value=10, value=2)
                    
                    for i in range(int(num_fields)):
                        col1, col2, col3 = st.columns([2, 2, 1])
                        with col1:
                            field_title = st.text_input(f"Field {i+1} Title", key=f"title_{i}")
                        with col2:
                            field_value = st.text_input(f"Field {i+1} Value", key=f"value_{i}")
                        with col3:
                            field_short = st.checkbox("Short", key=f"short_{i}", value=True)
                        
                        if field_title and field_value:
                            fields.append({
                                "title": field_title,
                                "value": field_value,
                                "short": field_short
                            })
                
                if st.button("📤 Send Notification", type="primary", use_container_width=True):
                    if title and message:
                        try:
                            result = client.send_notification(
                                channel=selected_channel,
                                title=title,
                                message=message,
                                color=color,
                                fields=fields if fields else None
                            )
                            st.success("✅ Notification sent successfully!")
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
                    else:
                        st.warning("Please enter title and message")
            
            elif message_type == "Status Update":
                # Status update form
                title = st.text_input("Status Title", placeholder="System Status Update")
                status_type = st.selectbox("Status Type", ["success", "info", "warning", "error"])
                
                st.subheader("Status Details")
                details = {}
                
                num_details = st.number_input("Number of status items", min_value=1, max_value=10, value=3)
                
                for i in range(int(num_details)):
                    col1, col2 = st.columns(2)
                    with col1:
                        key = st.text_input(f"Item {i+1} Name", key=f"status_key_{i}")
                    with col2:
                        value = st.text_input(f"Item {i+1} Value", key=f"status_value_{i}")
                    
                    if key and value:
                        details[key] = value
                
                if st.button("📤 Send Status", type="primary", use_container_width=True):
                    if title and details:
                        try:
                            blocks = SlackBlockBuilder.build_status_message(title, status_type, details)
                            result = client.send_rich_notification(selected_channel, blocks)
                            st.success("✅ Status update sent successfully!")
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
                    else:
                        st.warning("Please enter title and at least one status item")
        else:
            st.warning("No channels available. Please sync channels first.")
            if st.button("🔄 Sync Channels Now"):
                with st.spinner("Syncing..."):
                    client.list_channels(include_private=True)
                    st.success("✅ Channels synced!")
                    st.rerun()
    
    # Tab 5: Analytics
    with tab5:
        st.header("📈 Slack Analytics")
        
        # Date range selector
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", datetime.now() - timedelta(days=7))
        with col2:
            end_date = st.date_input("End Date", datetime.now())
        
        st.divider()
        
        # Load analytics data
        conn = sqlite3.connect(str(db_path))
        
        # Messages over time
        df_messages_time = pd.read_sql_query(f"""
            SELECT DATE(sent_at) as date, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY DATE(sent_at)
            ORDER BY date
        """, conn)
        
        if not df_messages_time.empty:
            fig = px.line(
                df_messages_time,
                x='date',
                y='count',
                title='Messages Sent Over Time',
                labels={'count': 'Number of Messages', 'date': 'Date'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Messages by channel
        df_by_channel = pd.read_sql_query(f"""
            SELECT channel, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY channel
            ORDER BY count DESC
            LIMIT 10
        """, conn)
        
        if not df_by_channel.empty:
            fig = px.bar(
                df_by_channel,
                x='channel',
                y='count',
                title='Top 10 Channels by Message Volume',
                labels={'count': 'Number of Messages', 'channel': 'Channel'}
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Commands usage
        df_commands = pd.read_sql_query(f"""
            SELECT command, COUNT(*) as count
            FROM slack_commands
            WHERE executed_at BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY command
            ORDER BY count DESC
        """, conn)
        
        if not df_commands.empty:
            fig = px.pie(
                df_commands,
                values='count',
                names='command',
                title='Slash Commands Usage'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Summary stats
        st.subheader("📊 Summary Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT COUNT(*) FROM slack_notifications
            WHERE sent_at BETWEEN '{start_date}' AND '{end_date}'
        """)
        total_messages = cursor.fetchone()[0]
        
        cursor.execute(f"""
            SELECT COUNT(DISTINCT channel) FROM slack_notifications
            WHERE sent_at BETWEEN '{start_date}' AND '{end_date}'
        """)
        active_channels = cursor.fetchone()[0]
        
        cursor.execute(f"""
            SELECT COUNT(*) FROM slack_commands
            WHERE executed_at BETWEEN '{start_date}' AND '{end_date}'
        """)
        total_commands = cursor.fetchone()[0]
        
        cursor.execute(f"""
            SELECT COUNT(*) FROM slack_notifications
            WHERE status = 'sent' AND sent_at BETWEEN '{start_date}' AND '{end_date}'
        """)
        successful_sends = cursor.fetchone()[0]
        
        conn.close()
        
        with col1:
            st.metric("Total Messages", total_messages)
        with col2:
            st.metric("Active Channels", active_channels)
        with col3:
            st.metric("Commands Executed", total_commands)
        with col4:
            success_rate = (successful_sends / total_messages * 100) if total_messages > 0 else 0
            st.metric("Success Rate", f"{success_rate:.1f}%")
    
    # Tab 6: Settings
    with tab6:
        st.header("⚙️ Slack Integration Settings")
        
        st.subheader("🔑 API Configuration")
        
        # Environment variables
        slack_token = os.getenv("SLACK_BOT_TOKEN", "")
        signing_secret = os.getenv("SLACK_SIGNING_SECRET", "")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input(
                "Bot Token",
                value=f"{slack_token[:15]}..." if slack_token else "Not set",
                disabled=True
            )
        
        with col2:
            st.text_input(
                "Signing Secret",
                value=f"{signing_secret[:10]}..." if signing_secret else "Not set",
                disabled=True
            )
        
        st.divider()
        
        st.subheader("📺 Default Channels")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.text_input("Alerts Channel", value=os.getenv("SLACK_ALERTS_CHANNEL", "#noizylab-alerts"))
        
        with col2:
            st.text_input("Monitoring Channel", value=os.getenv("SLACK_MONITORING_CHANNEL", "#noizylab-monitor"))
        
        with col3:
            st.text_input("Email Channel", value=os.getenv("SLACK_EMAIL_CHANNEL", "#noizylab-email"))
        
        st.divider()
        
        st.subheader("🗄️ Database")
        
        st.code(f"Database Path: {db_path}", language="text")
        
        if st.button("📊 View Database Stats"):
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            st.write("**Database Tables:**")
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
                count = cursor.fetchone()[0]
                st.write(f"- {table[0]}: {count} records")
            
            conn.close()
        
        if st.button("🗑️ Clear Old Data (>30 days)", type="secondary"):
            if st.checkbox("I understand this will delete old data"):
                conn = sqlite3.connect(str(db_path))
                cursor = conn.cursor()
                
                cursor.execute("""
                    DELETE FROM slack_notifications 
                    WHERE sent_at < datetime('now', '-30 days')
                """)
                
                cursor.execute("""
                    DELETE FROM slack_commands 
                    WHERE executed_at < datetime('now', '-30 days')
                """)
                
                conn.commit()
                conn.close()
                
                st.success("✅ Old data cleared")
        
        st.divider()
        
        st.subheader("📚 Documentation")
        
        st.markdown("""
        ### Available Slash Commands:
        - `/noizylab-status` - View system status
        - `/noizylab-services` - Manage services
        - `/noizylab-notify <message>` - Send notification
        - `/noizylab-logs [service]` - View logs
        - `/noizylab-deploy [component]` - Deploy components
        
        ### API Endpoints:
        - `POST /webhooks/slack/events` - Event webhook
        - `POST /webhooks/slack/interactions` - Interactive components
        - `POST /notify/system-alert` - System alerts
        - `POST /notify/email-event` - Email events
        
        ### Environment Variables:
        ```bash
        export SLACK_BOT_TOKEN="xoxb-your-token"
        export SLACK_SIGNING_SECRET="your-secret"
        export SLACK_ALERTS_CHANNEL="#alerts"
        export SLACK_MONITORING_CHANNEL="#monitoring"
        export SLACK_EMAIL_CHANNEL="#email"
        ```
        """)

else:
    st.warning("⚠️ Please configure Slack integration to continue.")
    
    # Setup wizard
    with st.expander("🚀 Setup Wizard", expanded=True):
        st.markdown("""
        ## Getting Started with Slack Integration
        
        ### Step 1: Create a Slack App
        1. Go to [api.slack.com/apps](https://api.slack.com/apps)
        2. Click "Create New App"
        3. Choose "From scratch"
        4. Name it "NoizyLab Portal" and select your workspace
        
        ### Step 2: Configure Permissions
        Under "OAuth & Permissions", add these Bot Token Scopes:
        - `chat:write` - Send messages
        - `chat:write.public` - Send to public channels
        - `channels:read` - View channels
        - `groups:read` - View private channels
        - `users:read` - View users
        - `users:read.email` - View user emails
        - `files:write` - Upload files
        - `commands` - Use slash commands
        
        ### Step 3: Install to Workspace
        1. Click "Install to Workspace"
        2. Authorize the app
        3. Copy the "Bot User OAuth Token" (starts with `xoxb-`)
        
        ### Step 4: Get Signing Secret
        Under "Basic Information", copy the "Signing Secret"
        
        ### Step 5: Set Environment Variables
        ```bash
        export SLACK_BOT_TOKEN="xoxb-your-token-here"
        export SLACK_SIGNING_SECRET="your-signing-secret-here"
        ```
        
        ### Step 6: Configure Event Subscriptions (Optional)
        1. Enable Event Subscriptions
        2. Set Request URL to: `https://your-domain.com/webhooks/slack/events`
        3. Subscribe to bot events:
           - `message.channels`
           - `app_mention`
           - `reaction_added`
        
        ### Step 7: Create Slash Commands (Optional)
        Add these slash commands:
        - Command: `/noizylab-status`
          - Request URL: `https://your-domain.com/commands/status`
          - Short Description: "View NoizyLab system status"
        
        ### Step 8: Restart Dashboard
        After setting environment variables, restart this dashboard.
        """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>💬 NoizyLab Slack Integration Dashboard | Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)

