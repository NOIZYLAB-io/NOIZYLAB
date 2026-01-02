#!/usr/bin/env python3
"""
NoizyLab Slack Integration - Core Library
==========================================
Enterprise-grade Slack integration with full feature support
"""

import os
import json
import time
import hmac
import hashlib
import requests
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import sqlite3
from pathlib import Path


@dataclass
class SlackMessage:
    """Represents a Slack message"""
    channel: str
    text: str
    blocks: Optional[List[Dict]] = None
    attachments: Optional[List[Dict]] = None
    thread_ts: Optional[str] = None
    username: Optional[str] = None
    icon_emoji: Optional[str] = None


@dataclass
class SlackUser:
    """Represents a Slack user"""
    id: str
    name: str
    real_name: str
    email: Optional[str] = None
    is_admin: bool = False
    is_bot: bool = False


class SlackClient:
    """Main Slack API client for NoizyLab"""
    
    def __init__(self, token: Optional[str] = None, signing_secret: Optional[str] = None):
        """
        Initialize Slack client
        
        Args:
            token: Slack Bot Token (xoxb-...)
            signing_secret: Slack Signing Secret for webhook verification
        """
        self.token = token or os.getenv("SLACK_BOT_TOKEN")
        self.signing_secret = signing_secret or os.getenv("SLACK_SIGNING_SECRET")
        self.base_url = "https://slack.com/api"
        
        if not self.token:
            raise ValueError("Slack token not provided. Set SLACK_BOT_TOKEN environment variable.")
        
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        # Initialize database
        self.db_path = Path(__file__).parent / "slack_data.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for Slack data"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Messages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slack_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                channel_id TEXT NOT NULL,
                channel_name TEXT,
                user_id TEXT,
                user_name TEXT,
                text TEXT,
                timestamp TEXT,
                thread_ts TEXT,
                message_type TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Channels table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slack_channels (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                is_private BOOLEAN,
                is_archived BOOLEAN,
                topic TEXT,
                purpose TEXT,
                member_count INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slack_users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                real_name TEXT,
                email TEXT,
                is_admin BOOLEAN,
                is_bot BOOLEAN,
                timezone TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Notifications table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slack_notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                notification_type TEXT NOT NULL,
                channel TEXT NOT NULL,
                message TEXT NOT NULL,
                status TEXT,
                response TEXT,
                sent_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Commands table (for slash commands)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slack_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL,
                user_id TEXT,
                user_name TEXT,
                channel_id TEXT,
                text TEXT,
                response TEXT,
                executed_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def verify_webhook(self, request_body: str, timestamp: str, signature: str) -> bool:
        """
        Verify Slack webhook signature
        
        Args:
            request_body: Raw request body
            timestamp: X-Slack-Request-Timestamp header
            signature: X-Slack-Signature header
        
        Returns:
            True if signature is valid
        """
        if not self.signing_secret:
            return False
        
        # Check if timestamp is recent (within 5 minutes)
        if abs(time.time() - int(timestamp)) > 60 * 5:
            return False
        
        # Create signature
        sig_basestring = f"v0:{timestamp}:{request_body}"
        my_signature = 'v0=' + hmac.new(
            self.signing_secret.encode(),
            sig_basestring.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(my_signature, signature)
    
    def _api_call(self, endpoint: str, method: str = "POST", data: Optional[Dict] = None) -> Dict:
        """
        Make API call to Slack
        
        Args:
            endpoint: API endpoint (without base URL)
            method: HTTP method
            data: Request data
        
        Returns:
            API response as dictionary
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            if method == "POST":
                response = requests.post(url, headers=self.headers, json=data)
            else:
                response = requests.get(url, headers=self.headers, params=data)
            
            response.raise_for_status()
            result = response.json()
            
            if not result.get("ok"):
                raise Exception(f"Slack API error: {result.get('error')}")
            
            return result
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Slack API request failed: {str(e)}")
    
    def send_message(self, message: SlackMessage) -> Dict:
        """
        Send a message to Slack
        
        Args:
            message: SlackMessage object
        
        Returns:
            API response
        """
        data = {
            "channel": message.channel,
            "text": message.text
        }
        
        if message.blocks:
            data["blocks"] = message.blocks
        if message.attachments:
            data["attachments"] = message.attachments
        if message.thread_ts:
            data["thread_ts"] = message.thread_ts
        if message.username:
            data["username"] = message.username
        if message.icon_emoji:
            data["icon_emoji"] = message.icon_emoji
        
        result = self._api_call("chat.postMessage", data=data)
        
        # Log to database
        self._log_notification("message", message.channel, message.text, "sent", json.dumps(result))
        
        return result
    
    def send_notification(self, channel: str, title: str, message: str, 
                         color: str = "good", fields: Optional[List[Dict]] = None) -> Dict:
        """
        Send a formatted notification with attachments
        
        Args:
            channel: Channel ID or name
            title: Notification title
            message: Notification message
            color: Color (good, warning, danger, or hex)
            fields: Additional fields
        
        Returns:
            API response
        """
        attachment = {
            "color": color,
            "title": title,
            "text": message,
            "footer": "NoizyLab Portal",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": int(time.time())
        }
        
        if fields:
            attachment["fields"] = fields
        
        slack_message = SlackMessage(
            channel=channel,
            text=title,
            attachments=[attachment]
        )
        
        return self.send_message(slack_message)
    
    def send_rich_notification(self, channel: str, blocks: List[Dict]) -> Dict:
        """
        Send a rich notification using Block Kit
        
        Args:
            channel: Channel ID or name
            blocks: Block Kit blocks
        
        Returns:
            API response
        """
        slack_message = SlackMessage(
            channel=channel,
            text="Notification from NoizyLab",
            blocks=blocks
        )
        
        return self.send_message(slack_message)
    
    def list_channels(self, include_private: bool = False) -> List[Dict]:
        """
        List all channels
        
        Args:
            include_private: Include private channels
        
        Returns:
            List of channels
        """
        data = {
            "exclude_archived": True,
            "types": "public_channel,private_channel" if include_private else "public_channel"
        }
        
        result = self._api_call("conversations.list", method="GET", data=data)
        channels = result.get("channels", [])
        
        # Update database
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        for channel in channels:
            cursor.execute("""
                INSERT OR REPLACE INTO slack_channels 
                (id, name, is_private, is_archived, topic, purpose, member_count, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                channel["id"],
                channel["name"],
                channel.get("is_private", False),
                channel.get("is_archived", False),
                channel.get("topic", {}).get("value", ""),
                channel.get("purpose", {}).get("value", ""),
                channel.get("num_members", 0),
                datetime.now()
            ))
        
        conn.commit()
        conn.close()
        
        return channels
    
    def get_user_info(self, user_id: str) -> Dict:
        """
        Get user information
        
        Args:
            user_id: Slack user ID
        
        Returns:
            User information
        """
        result = self._api_call("users.info", method="GET", data={"user": user_id})
        return result.get("user", {})
    
    def list_users(self) -> List[SlackUser]:
        """
        List all users in workspace
        
        Returns:
            List of SlackUser objects
        """
        result = self._api_call("users.list", method="GET")
        members = result.get("members", [])
        
        users = []
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        for member in members:
            if member.get("deleted"):
                continue
            
            user = SlackUser(
                id=member["id"],
                name=member["name"],
                real_name=member.get("real_name", ""),
                email=member.get("profile", {}).get("email"),
                is_admin=member.get("is_admin", False),
                is_bot=member.get("is_bot", False)
            )
            users.append(user)
            
            # Update database
            cursor.execute("""
                INSERT OR REPLACE INTO slack_users
                (id, name, real_name, email, is_admin, is_bot, timezone, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user.id,
                user.name,
                user.real_name,
                user.email,
                user.is_admin,
                user.is_bot,
                member.get("tz", ""),
                datetime.now()
            ))
        
        conn.commit()
        conn.close()
        
        return users
    
    def upload_file(self, channels: str, file_path: str, 
                   title: Optional[str] = None, comment: Optional[str] = None) -> Dict:
        """
        Upload a file to Slack
        
        Args:
            channels: Comma-separated channel IDs
            file_path: Path to file
            title: File title
            comment: File comment
        
        Returns:
            API response
        """
        url = f"{self.base_url}/files.upload"
        
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {'channels': channels}
            
            if title:
                data['title'] = title
            if comment:
                data['initial_comment'] = comment
            
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.post(url, headers=headers, data=data, files=files)
            
        response.raise_for_status()
        return response.json()
    
    def _log_notification(self, notification_type: str, channel: str, 
                         message: str, status: str, response: str):
        """Log notification to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO slack_notifications 
            (notification_type, channel, message, status, response)
            VALUES (?, ?, ?, ?, ?)
        """, (notification_type, channel, message, status, response))
        
        conn.commit()
        conn.close()
    
    def get_notification_history(self, limit: int = 100) -> List[Dict]:
        """Get notification history from database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM slack_notifications 
            ORDER BY sent_at DESC 
            LIMIT ?
        """, (limit,))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results


class SlackBlockBuilder:
    """Helper class to build Slack Block Kit messages"""
    
    @staticmethod
    def section(text: str, markdown: bool = True) -> Dict:
        """Create a section block"""
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn" if markdown else "plain_text",
                "text": text
            }
        }
    
    @staticmethod
    def divider() -> Dict:
        """Create a divider block"""
        return {"type": "divider"}
    
    @staticmethod
    def header(text: str) -> Dict:
        """Create a header block"""
        return {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": text
            }
        }
    
    @staticmethod
    def button(text: str, action_id: str, value: str, style: Optional[str] = None) -> Dict:
        """Create a button"""
        button = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": text
            },
            "action_id": action_id,
            "value": value
        }
        
        if style:
            button["style"] = style  # primary or danger
        
        return button
    
    @staticmethod
    def actions(elements: List[Dict]) -> Dict:
        """Create an actions block"""
        return {
            "type": "actions",
            "elements": elements
        }
    
    @staticmethod
    def context(elements: List[str]) -> Dict:
        """Create a context block"""
        return {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": elem} for elem in elements
            ]
        }
    
    @staticmethod
    def build_status_message(title: str, status: str, details: Dict) -> List[Dict]:
        """Build a status message with blocks"""
        emoji_map = {
            "success": "✅",
            "warning": "⚠️",
            "error": "❌",
            "info": "ℹ️"
        }
        
        blocks = [
            SlackBlockBuilder.header(f"{emoji_map.get(status, '📊')} {title}"),
            SlackBlockBuilder.divider()
        ]
        
        for key, value in details.items():
            blocks.append(SlackBlockBuilder.section(f"*{key}:* {value}"))
        
        blocks.append(SlackBlockBuilder.context([
            f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ]))
        
        return blocks


# Convenience functions
def send_alert(channel: str, message: str, level: str = "info"):
    """Quick alert function"""
    client = SlackClient()
    color_map = {
        "info": "good",
        "warning": "warning",
        "error": "danger",
        "success": "good"
    }
    
    return client.send_notification(
        channel=channel,
        title=f"{level.upper()} Alert",
        message=message,
        color=color_map.get(level, "good")
    )


def send_system_status(channel: str, services: Dict[str, str]):
    """Send system status to Slack"""
    client = SlackClient()
    blocks = SlackBlockBuilder.build_status_message(
        "System Status Update",
        "info",
        services
    )
    
    return client.send_rich_notification(channel, blocks)


if __name__ == "__main__":
    # Test the client
    try:
        client = SlackClient()
        print("✅ Slack client initialized successfully")
        
        # Test listing channels
        channels = client.list_channels()
        print(f"📺 Found {len(channels)} channels")
        
    except Exception as e:
        print(f"❌ Error: {e}")

