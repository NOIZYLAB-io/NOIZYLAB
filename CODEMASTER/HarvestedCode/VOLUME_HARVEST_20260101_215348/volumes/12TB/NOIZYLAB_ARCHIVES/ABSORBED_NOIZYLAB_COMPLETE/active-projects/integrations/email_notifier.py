#!/usr/bin/env python3
"""
Email Notification System
==========================
Send email notifications in addition to Slack
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path
import sqlite3


class EmailNotifier:
    """Email notification system"""
    
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL", self.smtp_user)
        
        self.enabled = bool(self.smtp_user and self.smtp_password)
        
        if not self.enabled:
            print("⚠️ Email notifications disabled (SMTP not configured)")
        
        self.db_path = Path(__file__).parent / "email_notifications.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize email notification database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                to_emails TEXT,
                subject TEXT,
                body TEXT,
                success BOOLEAN,
                error TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def send_email(self, to_emails: List[str], subject: str, body: str, 
                   html: bool = False) -> Dict:
        """
        Send email notification
        
        Args:
            to_emails: List of recipient emails
            subject: Email subject
            body: Email body
            html: Send as HTML
        
        Returns:
            Result dictionary
        """
        if not self.enabled:
            return {"success": False, "error": "Email not configured"}
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.from_email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject
            
            # Add body
            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
            
            # Log success
            self._log_email(to_emails, subject, body, True, None)
            
            return {"success": True}
        
        except Exception as e:
            # Log failure
            self._log_email(to_emails, subject, body, False, str(e))
            
            return {"success": False, "error": str(e)}
    
    def send_alert(self, to_emails: List[str], alert_type: str, 
                   message: str, details: Dict = None):
        """Send formatted alert email"""
        subject = f"NoizyLab Alert: {alert_type}"
        
        body = f"""NoizyLab System Alert

Type: {alert_type}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Message:
{message}

"""
        
        if details:
            body += "\nDetails:\n"
            for key, value in details.items():
                body += f"  {key}: {value}\n"
        
        body += "\n---\nNoizyLab Portal\n"
        
        return self.send_email(to_emails, subject, body)
    
    def send_daily_digest(self, to_emails: List[str], stats: Dict):
        """Send daily digest email"""
        subject = f"NoizyLab Daily Digest - {datetime.now().strftime('%Y-%m-%d')}"
        
        html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; }}
        h1 {{ color: #667eea; }}
        .metric {{ background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .metric-name {{ font-weight: bold; color: #333; }}
        .metric-value {{ font-size: 24px; color: #667eea; }}
        .status-good {{ color: #28a745; }}
        .status-warning {{ color: #ffc107; }}
        .status-critical {{ color: #dc3545; }}
    </style>
</head>
<body>
    <h1>🎛️ NoizyLab Daily Digest</h1>
    <p>{datetime.now().strftime('%A, %B %d, %Y')}</p>
    
    <div class="metric">
        <div class="metric-name">System Health Score</div>
        <div class="metric-value">{stats.get('health_score', 0):.0f}/100</div>
    </div>
    
    <div class="metric">
        <div class="metric-name">Alerts (24h)</div>
        <div class="metric-value">{stats.get('alerts_24h', 0)}</div>
    </div>
    
    <div class="metric">
        <div class="metric-name">Devices Connected</div>
        <div class="metric-value">{stats.get('devices_connected', 0)}</div>
    </div>
    
    <div class="metric">
        <div class="metric-name">Slack Messages Sent</div>
        <div class="metric-value">{stats.get('slack_messages', 0)}</div>
    </div>
    
    <h2>Service Status</h2>
    <ul>
"""
        
        for service, status in stats.get('services', {}).items():
            status_class = "status-good" if status == "running" else "status-critical"
            html_body += f'        <li class="{status_class}">{service}: {status}</li>\n'
        
        html_body += """
    </ul>
    
    <p style="color: #666; margin-top: 30px;">
        Generated by NoizyLab Portal<br>
        <a href="http://localhost:8501">View Dashboard</a>
    </p>
</body>
</html>
"""
        
        return self.send_email(to_emails, subject, html_body, html=True)
    
    def _log_email(self, to_emails: List[str], subject: str, body: str,
                   success: bool, error: Optional[str]):
        """Log email to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO email_notifications (to_emails, subject, body, success, error)
            VALUES (?, ?, ?, ?, ?)
        """, (
            ', '.join(to_emails),
            subject,
            body[:1000],  # Truncate body
            success,
            error
        ))
        
        conn.commit()
        conn.close()


# Global instance
email_notifier = EmailNotifier()


# Convenience functions
def send_alert_email(to_emails: List[str], alert_type: str, message: str, details: Dict = None):
    """Quick alert email"""
    return email_notifier.send_alert(to_emails, alert_type, message, details)


def send_digest_email(to_emails: List[str], stats: Dict):
    """Quick digest email"""
    return email_notifier.send_daily_digest(to_emails, stats)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Email Notifier")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--message", required=True, help="Email message")
    
    args = parser.parse_args()
    
    notifier = EmailNotifier()
    result = notifier.send_email([args.to], args.subject, args.message)
    
    if result["success"]:
        print("✅ Email sent!")
    else:
        print(f"❌ Failed: {result.get('error')}")

