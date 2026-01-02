#!/usr/bin/env python3
"""
NoizyLab Slack API Server
==========================
FastAPI server for handling Slack webhooks, slash commands, and interactive components
"""

from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Optional, List, Any
import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path
import psutil
import requests

from slack_core import SlackClient, SlackBlockBuilder, SlackMessage

app = FastAPI(
    title="NoizyLab Slack Integration API",
    description="Webhook and command handler for Slack integration",
    version="1.0.0"
)

# Initialize Slack client
slack_client = SlackClient()


class CommandResponse(BaseModel):
    """Slack command response"""
    response_type: str = "in_channel"  # or "ephemeral"
    text: str
    blocks: Optional[List[Dict]] = None


class SlashCommandRequest(BaseModel):
    """Slash command request from Slack"""
    token: str
    team_id: str
    team_domain: str
    channel_id: str
    channel_name: str
    user_id: str
    user_name: str
    command: str
    text: str
    response_url: str
    trigger_id: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "NoizyLab Slack Integration",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "slack_connected": bool(slack_client.token),
        "database": str(slack_client.db_path.exists()),
        "timestamp": datetime.now().isoformat()
    }


@app.post("/webhooks/slack/events")
async def slack_events(request: Request):
    """
    Handle Slack Events API
    Receives events like messages, reactions, etc.
    """
    # Verify Slack signature
    body = await request.body()
    timestamp = request.headers.get("X-Slack-Request-Timestamp", "")
    signature = request.headers.get("X-Slack-Signature", "")
    
    if not slack_client.verify_webhook(body.decode(), timestamp, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    data = await request.json()
    
    # Handle URL verification challenge
    if data.get("type") == "url_verification":
        return {"challenge": data.get("challenge")}
    
    # Handle events
    if data.get("type") == "event_callback":
        event = data.get("event", {})
        event_type = event.get("type")
        
        # Log event to database
        _log_event(event_type, event)
        
        # Handle different event types
        if event_type == "message":
            await handle_message_event(event)
        elif event_type == "app_mention":
            await handle_mention_event(event)
        elif event_type == "reaction_added":
            await handle_reaction_event(event)
    
    return {"ok": True}


@app.post("/webhooks/slack/interactions")
async def slack_interactions(request: Request):
    """
    Handle Slack interactive components
    (buttons, select menus, etc.)
    """
    form_data = await request.form()
    payload = json.loads(form_data.get("payload", "{}"))
    
    action_type = payload.get("type")
    
    if action_type == "block_actions":
        actions = payload.get("actions", [])
        for action in actions:
            action_id = action.get("action_id")
            value = action.get("value")
            
            # Handle different actions
            if action_id == "restart_service":
                await handle_restart_service(value, payload)
            elif action_id == "view_logs":
                await handle_view_logs(value, payload)
            elif action_id == "run_health_check":
                await handle_health_check(payload)
    
    return {"ok": True}


@app.post("/commands/status")
async def command_status(request: Request):
    """
    Slash command: /noizylab-status
    Shows system status
    """
    form_data = await request.form()
    
    # Log command
    _log_command("/status", dict(form_data))
    
    # Get system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # Check services
    services = _check_services()
    
    # Build response
    blocks = [
        SlackBlockBuilder.header("🎛️ NoizyLab System Status"),
        SlackBlockBuilder.divider(),
        SlackBlockBuilder.section(f"*CPU Usage:* {cpu:.1f}%"),
        SlackBlockBuilder.section(f"*Memory:* {memory.percent:.1f}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)"),
        SlackBlockBuilder.section(f"*Disk:* {disk.percent:.1f}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)"),
        SlackBlockBuilder.divider(),
        SlackBlockBuilder.section("*Services:*")
    ]
    
    for service, status in services.items():
        emoji = "🟢" if status == "running" else "🔴"
        blocks.append(SlackBlockBuilder.section(f"{emoji} {service}: {status}"))
    
    blocks.append(SlackBlockBuilder.context([
        f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ]))
    
    # Add action buttons
    blocks.append(SlackBlockBuilder.actions([
        SlackBlockBuilder.button("🔄 Refresh", "refresh_status", "refresh", "primary"),
        SlackBlockBuilder.button("🏥 Health Check", "run_health_check", "health_check")
    ]))
    
    return {
        "response_type": "in_channel",
        "blocks": blocks
    }


@app.post("/commands/services")
async def command_services(request: Request):
    """
    Slash command: /noizylab-services
    Manage services
    """
    form_data = await request.form()
    text = form_data.get("text", "")
    
    _log_command("/services", dict(form_data))
    
    services = _check_services()
    
    blocks = [
        SlackBlockBuilder.header("🔧 NoizyLab Services"),
        SlackBlockBuilder.divider()
    ]
    
    for service, status in services.items():
        emoji = "🟢" if status == "running" else "🔴"
        service_id = service.lower().replace(" ", "_")
        
        blocks.append(SlackBlockBuilder.section(f"{emoji} *{service}*\nStatus: {status}"))
        
        if status != "running":
            blocks.append(SlackBlockBuilder.actions([
                SlackBlockBuilder.button("▶️ Start", "restart_service", service_id, "primary")
            ]))
    
    return {
        "response_type": "in_channel",
        "blocks": blocks
    }


@app.post("/commands/notify")
async def command_notify(request: Request):
    """
    Slash command: /noizylab-notify <message>
    Send a notification to monitoring channel
    """
    form_data = await request.form()
    text = form_data.get("text", "")
    user_name = form_data.get("user_name", "")
    
    _log_command("/notify", dict(form_data))
    
    if not text:
        return {
            "response_type": "ephemeral",
            "text": "Please provide a message: /noizylab-notify <message>"
        }
    
    # Send notification to monitoring channel
    monitoring_channel = os.getenv("SLACK_MONITORING_CHANNEL", "#noizylab-alerts")
    
    slack_client.send_notification(
        channel=monitoring_channel,
        title=f"Manual Alert from {user_name}",
        message=text,
        color="warning"
    )
    
    return {
        "response_type": "ephemeral",
        "text": f"✅ Notification sent to {monitoring_channel}"
    }


@app.post("/commands/logs")
async def command_logs(request: Request):
    """
    Slash command: /noizylab-logs [service]
    View recent logs
    """
    form_data = await request.form()
    service = form_data.get("text", "").strip()
    
    _log_command("/logs", dict(form_data))
    
    # Get recent logs
    logs = _get_recent_logs(service, limit=10)
    
    blocks = [
        SlackBlockBuilder.header(f"📋 Recent Logs{f' - {service}' if service else ''}"),
        SlackBlockBuilder.divider()
    ]
    
    if logs:
        for log in logs:
            blocks.append(SlackBlockBuilder.section(f"`{log}`"))
    else:
        blocks.append(SlackBlockBuilder.section("No recent logs found"))
    
    return {
        "response_type": "ephemeral",
        "blocks": blocks
    }


@app.post("/commands/deploy")
async def command_deploy(request: Request, background_tasks: BackgroundTasks):
    """
    Slash command: /noizylab-deploy [component]
    Deploy components
    """
    form_data = await request.form()
    component = form_data.get("text", "").strip() or "all"
    user_name = form_data.get("user_name", "")
    channel_id = form_data.get("channel_id", "")
    
    _log_command("/deploy", dict(form_data))
    
    # Start deployment in background
    background_tasks.add_task(
        run_deployment,
        component=component,
        user=user_name,
        channel=channel_id
    )
    
    return {
        "response_type": "in_channel",
        "text": f"🚀 Starting deployment of {component}...\nYou'll be notified when complete."
    }


@app.post("/notify/system-alert")
async def notify_system_alert(alert: Dict[str, Any]):
    """
    Endpoint to send system alerts to Slack
    Called by other NoizyLab services
    """
    channel = alert.get("channel", os.getenv("SLACK_ALERTS_CHANNEL", "#noizylab-alerts"))
    title = alert.get("title", "System Alert")
    message = alert.get("message", "")
    level = alert.get("level", "info")
    details = alert.get("details", {})
    
    color_map = {
        "info": "good",
        "warning": "warning",
        "error": "danger",
        "critical": "danger"
    }
    
    fields = [
        {"title": key, "value": str(value), "short": True}
        for key, value in details.items()
    ]
    
    result = slack_client.send_notification(
        channel=channel,
        title=title,
        message=message,
        color=color_map.get(level, "good"),
        fields=fields
    )
    
    return {"success": True, "ts": result.get("ts")}


@app.post("/notify/email-event")
async def notify_email_event(event: Dict[str, Any]):
    """
    Notify about email events
    Integrates with email-intelligence system
    """
    channel = os.getenv("SLACK_EMAIL_CHANNEL", "#noizylab-email")
    event_type = event.get("type", "unknown")
    
    emoji_map = {
        "received": "📨",
        "sent": "📤",
        "bounced": "⚠️",
        "spam": "🚫",
        "validated": "✅"
    }
    
    emoji = emoji_map.get(event_type, "📧")
    
    blocks = [
        SlackBlockBuilder.header(f"{emoji} Email Event: {event_type.title()}"),
        SlackBlockBuilder.divider()
    ]
    
    for key, value in event.items():
        if key != "type":
            blocks.append(SlackBlockBuilder.section(f"*{key.title()}:* {value}"))
    
    result = slack_client.send_rich_notification(channel, blocks)
    
    return {"success": True, "ts": result.get("ts")}


# Helper functions

def _check_services() -> Dict[str, str]:
    """Check status of all services"""
    services = {}
    
    # Check various service endpoints
    service_checks = [
        ("Email Intelligence", "http://localhost:8000/"),
        ("Mobile API", "http://localhost:8002/mobile/health"),
        ("Webhook Hub", "http://localhost:8001/docs"),
        ("Master Dashboard", "http://localhost:8501/")
    ]
    
    for name, url in service_checks:
        try:
            response = requests.get(url, timeout=2)
            services[name] = "running" if response.status_code == 200 else "error"
        except:
            services[name] = "stopped"
    
    return services


def _log_event(event_type: str, event: Dict):
    """Log Slack event to database"""
    conn = sqlite3.connect(str(slack_client.db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO slack_messages 
        (channel_id, channel_name, user_id, text, timestamp, message_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        event.get("channel"),
        event.get("channel_name", ""),
        event.get("user"),
        event.get("text", ""),
        event.get("ts"),
        event_type
    ))
    
    conn.commit()
    conn.close()


def _log_command(command: str, data: Dict):
    """Log slash command to database"""
    conn = sqlite3.connect(str(slack_client.db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO slack_commands 
        (command, user_id, user_name, channel_id, text)
        VALUES (?, ?, ?, ?, ?)
    """, (
        command,
        data.get("user_id"),
        data.get("user_name"),
        data.get("channel_id"),
        data.get("text", "")
    ))
    
    conn.commit()
    conn.close()


def _get_recent_logs(service: Optional[str] = None, limit: int = 10) -> List[str]:
    """Get recent logs from NoizyLab systems"""
    logs = []
    
    log_dir = Path("/Users/m2ultra/NOIZYLAB/logs")
    if log_dir.exists():
        log_files = sorted(log_dir.glob("*.log"), key=lambda x: x.stat().st_mtime, reverse=True)
        
        for log_file in log_files[:3]:
            if service and service not in log_file.name:
                continue
            
            try:
                with open(log_file) as f:
                    lines = f.readlines()
                    logs.extend(lines[-limit:])
            except:
                pass
    
    return logs[:limit]


async def handle_message_event(event: Dict):
    """Handle message events"""
    # Implement custom message handling logic
    pass


async def handle_mention_event(event: Dict):
    """Handle bot mentions"""
    channel = event.get("channel")
    text = event.get("text", "")
    
    # Simple bot response
    response = "👋 Hey! I'm the NoizyLab bot. Use slash commands to interact with me!"
    
    slack_client.send_message(SlackMessage(
        channel=channel,
        text=response,
        thread_ts=event.get("ts")
    ))


async def handle_reaction_event(event: Dict):
    """Handle reaction events"""
    # Implement reaction handling logic
    pass


async def handle_restart_service(service: str, payload: Dict):
    """Handle service restart button click"""
    # Implement service restart logic
    response_url = payload.get("response_url")
    
    if response_url:
        requests.post(response_url, json={
            "text": f"🔄 Restarting {service}..."
        })


async def handle_view_logs(service: str, payload: Dict):
    """Handle view logs button click"""
    logs = _get_recent_logs(service, limit=5)
    
    response_url = payload.get("response_url")
    if response_url:
        requests.post(response_url, json={
            "text": f"📋 Recent logs for {service}:\n```\n" + "\n".join(logs) + "\n```"
        })


async def handle_health_check(payload: Dict):
    """Handle health check button click"""
    services = _check_services()
    
    all_healthy = all(status == "running" for status in services.values())
    
    message = "✅ All services healthy!" if all_healthy else "⚠️ Some services need attention"
    
    response_url = payload.get("response_url")
    if response_url:
        requests.post(response_url, json={
            "text": message
        })


async def run_deployment(component: str, user: str, channel: str):
    """Run deployment in background"""
    import asyncio
    
    # Simulate deployment
    slack_client.send_notification(
        channel=channel,
        title=f"Deployment Started by {user}",
        message=f"Deploying {component}...",
        color="warning"
    )
    
    await asyncio.sleep(5)  # Simulate deployment time
    
    slack_client.send_notification(
        channel=channel,
        title="Deployment Complete",
        message=f"Successfully deployed {component}",
        color="good"
    )


if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Starting NoizyLab Slack API Server...")
    print("📡 Listening on http://localhost:8003")
    
    uvicorn.run(app, host="0.0.0.0", port=8003)

