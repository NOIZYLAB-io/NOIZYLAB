#!/usr/bin/env python3
"""
NoizyLab Slack Notifier - Integration Module
============================================
Easy integration for existing NoizyLab services
"""

import os
from typing import Dict, List, Optional, Any
from datetime import datetime
from slack_core import SlackClient, SlackBlockBuilder


class NoizyLabSlackNotifier:
    """Convenient wrapper for sending notifications from NoizyLab services"""
    
    def __init__(self):
        try:
            self.client = SlackClient()
            self.enabled = True
        except:
            self.enabled = False
            print("⚠️ Slack notifications disabled (token not configured)")
        
        # Default channels
        self.alerts_channel = os.getenv("SLACK_ALERTS_CHANNEL", "#noizylab-alerts")
        self.monitoring_channel = os.getenv("SLACK_MONITORING_CHANNEL", "#noizylab-monitor")
        self.email_channel = os.getenv("SLACK_EMAIL_CHANNEL", "#noizylab-email")
        self.network_channel = os.getenv("SLACK_NETWORK_CHANNEL", "#noizylab-network")
    
    def send_alert(self, message: str, level: str = "info", channel: Optional[str] = None):
        """Send a simple alert"""
        if not self.enabled:
            return
        
        emoji_map = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "❌",
            "critical": "🚨"
        }
        
        color_map = {
            "info": "good",
            "success": "good",
            "warning": "warning",
            "error": "danger",
            "critical": "danger"
        }
        
        emoji = emoji_map.get(level, "📢")
        title = f"{emoji} {level.upper()} Alert"
        
        self.client.send_notification(
            channel=channel or self.alerts_channel,
            title=title,
            message=message,
            color=color_map.get(level, "good")
        )
    
    def send_system_status(self, services: Dict[str, str], channel: Optional[str] = None):
        """Send system status update"""
        if not self.enabled:
            return
        
        blocks = SlackBlockBuilder.build_status_message(
            "System Status Update",
            "info",
            services
        )
        
        self.client.send_rich_notification(
            channel=channel or self.monitoring_channel,
            blocks=blocks
        )
    
    def send_email_notification(self, event_type: str, details: Dict[str, Any]):
        """Send email system notification"""
        if not self.enabled:
            return
        
        emoji_map = {
            "received": "📨",
            "sent": "📤",
            "bounced": "⚠️",
            "spam": "🚫",
            "validated": "✅",
            "failed": "❌"
        }
        
        emoji = emoji_map.get(event_type, "📧")
        
        blocks = [
            SlackBlockBuilder.header(f"{emoji} Email Event: {event_type.title()}"),
            SlackBlockBuilder.divider()
        ]
        
        for key, value in details.items():
            blocks.append(SlackBlockBuilder.section(f"*{key.title()}:* {value}"))
        
        blocks.append(SlackBlockBuilder.context([
            f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ]))
        
        self.client.send_rich_notification(self.email_channel, blocks)
    
    def send_network_event(self, event_type: str, device: str, details: Dict[str, Any]):
        """Send network event notification"""
        if not self.enabled:
            return
        
        emoji_map = {
            "connected": "🔌",
            "disconnected": "🔴",
            "link_up": "🟢",
            "link_down": "🔴",
            "handshake": "🤝",
            "error": "❌",
            "warning": "⚠️"
        }
        
        emoji = emoji_map.get(event_type, "🌐")
        
        blocks = [
            SlackBlockBuilder.header(f"{emoji} Network Event: {event_type.title()}"),
            SlackBlockBuilder.section(f"*Device:* {device}"),
            SlackBlockBuilder.divider()
        ]
        
        for key, value in details.items():
            blocks.append(SlackBlockBuilder.section(f"*{key}:* {value}"))
        
        blocks.append(SlackBlockBuilder.context([
            f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ]))
        
        self.client.send_rich_notification(self.network_channel, blocks)
    
    def send_deployment_notification(self, component: str, status: str, details: Optional[Dict] = None):
        """Send deployment notification"""
        if not self.enabled:
            return
        
        emoji_map = {
            "started": "🚀",
            "completed": "✅",
            "failed": "❌",
            "in_progress": "⏳"
        }
        
        color_map = {
            "started": "warning",
            "completed": "good",
            "failed": "danger",
            "in_progress": "warning"
        }
        
        emoji = emoji_map.get(status, "📦")
        title = f"{emoji} Deployment {status.title()}: {component}"
        message = f"Component: {component}\nStatus: {status}"
        
        fields = []
        if details:
            fields = [
                {"title": key, "value": str(value), "short": True}
                for key, value in details.items()
            ]
        
        self.client.send_notification(
            channel=self.monitoring_channel,
            title=title,
            message=message,
            color=color_map.get(status, "good"),
            fields=fields
        )


# Global notifier instance
notifier = NoizyLabSlackNotifier()


# Convenience functions
def alert(message: str, level: str = "info", channel: Optional[str] = None):
    """Quick alert function"""
    notifier.send_alert(message, level, channel)


def system_status(services: Dict[str, str], channel: Optional[str] = None):
    """Quick system status function"""
    notifier.send_system_status(services, channel)


def email_event(event_type: str, details: Dict[str, Any]):
    """Quick email event function"""
    notifier.send_email_notification(event_type, details)


def network_event(event_type: str, device: str, details: Dict[str, Any]):
    """Quick network event function"""
    notifier.send_network_event(event_type, device, details)


def deployment(component: str, status: str, details: Optional[Dict] = None):
    """Quick deployment function"""
    notifier.send_deployment_notification(component, status, details)

