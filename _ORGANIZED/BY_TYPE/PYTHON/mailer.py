#!/usr/bin/env python3
"""
NoizyMailer - Advanced Email Sending with Identity Management
============================================================
Enhanced with attachments, better error handling, and async support
"""

import json
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List, Optional, Dict
from rich.console import Console

# Performance decorators (optional - graceful fallback)
try:
    from src.performance import performance_monitor, cached
except ImportError:
    # Fallback if performance module not available
    def performance_monitor(func):
        return func
    def cached(ttl=300):
        def decorator(func):
            return func
        return decorator

console = Console()

class NoizyMailer:
    def __init__(self, config_path: str = "config/email_config.json"):
        """Initialize NoizyMailer with configuration"""
        self.config_path = Path(config_path)
        self.config = self.load_config()
        self.log_path = Path("email_history.log")
        self.drafts_path = Path("config/drafts.json")
        self.drafts_path.parent.mkdir(parents=True, exist_ok=True)
        
    @cached(ttl=60)
    def load_config(self) -> dict:
        """Load email configuration"""
        if not self.config_path.exists():
            # Create default config
            default_config = {
                "smtp": {
                    "server": os.getenv("SMTP_SERVER", "smtp.office365.com"),
                    "port": int(os.getenv("SMTP_PORT", "587")),
                    "username": os.getenv("SMTP_USERNAME", ""),
                    "password": os.getenv("SMTP_PASSWORD", ""),
                    "use_tls": True,
                    "timeout": 30
                },
                "identities": {
                    "personal": {
                        "name": "Your Name",
                        "email": os.getenv("FROM_EMAIL", ""),
                        "signature": "\n\n--\nYour Name"
                    }
                },
                "settings": {
                    "auto_save_drafts": True,
                    "log_level": "detailed",
                    "retry_attempts": 3
                }
            }
            
            # Ensure config directory exists
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save default config
            with open(self.config_path, 'w') as f:
                json.dump(default_config, f, indent=2)
            
            return default_config
        
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def save_draft(self, identity_key: str, to: str, subject: str, body: str, draft_id: Optional[str] = None):
        """Save email as draft"""
        drafts = self.load_drafts()
        
        if not draft_id:
            draft_id = f"draft_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        drafts[draft_id] = {
            "identity": identity_key,
            "to": to,
            "subject": subject,
            "body": body,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        with open(self.drafts_path, 'w') as f:
            json.dump(drafts, f, indent=2)
        
        return draft_id
    
    def load_drafts(self) -> Dict:
        """Load saved drafts"""
        if not self.drafts_path.exists():
            return {}
        
        try:
            with open(self.drafts_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def delete_draft(self, draft_id: str) -> bool:
        """Delete a draft"""
        drafts = self.load_drafts()
        if draft_id in drafts:
            del drafts[draft_id]
            with open(self.drafts_path, 'w') as f:
                json.dump(drafts, f, indent=2)
            return True
        return False
    
    @performance_monitor
    def send_email(self, identity_key: str, to: str, subject: str, body: str, 
                   attachments: Optional[List[str]] = None, draft_id: Optional[str] = None) -> bool:
        """Send email using specified identity with enhanced features"""
        try:
            # Get identity
            if identity_key not in self.config['identities']:
                console.print(f"[red]❌ Identity '{identity_key}' not found.[/red]")
                return False
            
            identity = self.config['identities'][identity_key]
            smtp_config = self.config['smtp']
            settings = self.config.get('settings', {})
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = f"{identity['name']} <{identity['email']}>"
            msg['To'] = to
            msg['Subject'] = subject
            
            # Add body with signature
            full_body = body + identity.get('signature', '')
            msg.attach(MIMEText(full_body, 'plain'))
            
            # Add attachments
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        try:
                            with open(file_path, 'rb') as f:
                                part = MIMEBase('application', 'octet-stream')
                                part.set_payload(f.read())
                                encoders.encode_base64(part)
                                part.add_header(
                                    'Content-Disposition',
                                    f'attachment; filename= {os.path.basename(file_path)}'
                                )
                                msg.attach(part)
                        except Exception as e:
                            console.print(f"[yellow]⚠️  Could not attach {file_path}: {e}[/yellow]")
            
            # Connect and send with retry logic
            retry_attempts = settings.get('retry_attempts', 3)
            timeout = smtp_config.get('timeout', 30)
            
            for attempt in range(retry_attempts):
                try:
                    server = smtplib.SMTP(smtp_config['server'], smtp_config['port'], timeout=timeout)
                    if smtp_config.get('use_tls', True):
                        server.starttls()
                    
                    server.login(smtp_config['username'], smtp_config['password'])
                    server.send_message(msg)
                    server.quit()
                    
                    # Log success
                    self.log_email(identity['email'], to, subject, "sent", attachments)
                    
                    # Delete draft if sent
                    if draft_id:
                        self.delete_draft(draft_id)
                    
                    console.print(f"[green]✅ Email sent from {identity['email']} to {to}[/green]")
                    return True
                    
                except smtplib.SMTPException as e:
                    if attempt < retry_attempts - 1:
                        console.print(f"[yellow]⚠️  Attempt {attempt + 1} failed, retrying...[/yellow]")
                        continue
                    else:
                        raise
                except Exception as e:
                    raise
            
        except Exception as e:
            error_msg = str(e)
            console.print(f"[red]❌ Error sending email: {error_msg}[/red]")
            
            # Log error with details
            try:
                identity = self.config['identities'].get(identity_key, {})
                self.log_email(
                    identity.get('email', 'unknown'), 
                    to, 
                    subject, 
                    f"FAILED: {error_msg}",
                    attachments
                )
            except:
                pass
            
            return False
    
    def log_email(self, from_email: str, to_email: str, subject: str, status: str, 
                  attachments: Optional[List[str]] = None):
        """Enhanced logging with attachment info"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attach_info = f" [{len(attachments)} attachments]" if attachments else ""
        log_entry = f"[{timestamp}] {status} | From: {from_email} | To: {to_email} | Subject: {subject}{attach_info}\n"
        
        with open(self.log_path, 'a') as f:
            f.write(log_entry)
    
    def get_statistics(self) -> Dict:
        """Get email statistics"""
        stats = {
            "total_sent": 0,
            "total_failed": 0,
            "by_identity": {},
            "recent_activity": []
        }
        
        if not self.log_path.exists():
            return stats
        
        try:
            with open(self.log_path, 'r') as f:
                lines = f.readlines()
                
            for line in lines:
                if "sent" in line.lower():
                    stats["total_sent"] += 1
                elif "failed" in line.lower():
                    stats["total_failed"] += 1
                
                # Extract identity
                if "From:" in line:
                    parts = line.split("From:")
                    if len(parts) > 1:
                        email = parts[1].split("|")[0].strip()
                        identity = email.split("@")[0] if "@" in email else "unknown"
                        stats["by_identity"][identity] = stats["by_identity"].get(identity, 0) + 1
            
            # Recent activity (last 10 lines)
            stats["recent_activity"] = [line.strip() for line in lines[-10:]]
            
        except Exception as e:
            console.print(f"[yellow]⚠️  Error reading statistics: {e}[/yellow]")
        
        return stats
