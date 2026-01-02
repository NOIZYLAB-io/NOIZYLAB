#!/usr/bin/env python3
"""
Email Sender - Core Email Sending Functionality
===============================================
"""

import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from typing import List, Dict, Optional
import sqlite3
from pathlib import Path
from rich.console import Console

console = Console()

class EmailSender:
    def __init__(self, config_path: str = None):
        # Get parent directory for relative paths
        _parent_dir = Path(__file__).parent.parent
        if config_path is None:
            config_path = str(_parent_dir / "config" / "email" / "email_config.json")
        self.config_path = Path(config_path)
        self.config = self.load_config()
        self.db_path = str(_parent_dir / "data" / "email_intelligence.db")
        self.init_database()
    
    def load_config(self) -> Dict:
        """Load email configuration"""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {
            "smtp_server": os.getenv("SMTP_SERVER", "smtp.office365.com"),
            "smtp_port": int(os.getenv("SMTP_PORT", "587")),
            "username": os.getenv("EMAIL_USERNAME", ""),
            "password": os.getenv("EMAIL_PASSWORD", ""),
            "use_tls": True,
            "from_email": os.getenv("FROM_EMAIL", ""),
            "from_name": os.getenv("FROM_NAME", "NoizyLab")
        }
    
    def save_config(self):
        """Save email configuration"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def configure(self, smtp_server: str, smtp_port: int, username: str, 
                  password: str, from_email: str, from_name: str = "NoizyLab"):
        """Configure email settings"""
        self.config.update({
            "smtp_server": smtp_server,
            "smtp_port": smtp_port,
            "username": username,
            "password": password,
            "from_email": from_email,
            "from_name": from_name
        })
        self.save_config()
        console.print("[green]✅ Email configuration saved[/green]")
    
    def init_database(self):
        """Initialize email history database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_email TEXT,
                to_email TEXT,
                subject TEXT,
                body TEXT,
                status TEXT,
                error_message TEXT,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                attachments TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                name TEXT,
                company TEXT,
                tags TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_contacted TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def send_email(self, to_email: str, subject: str, body: str, 
                   html_body: Optional[str] = None, attachments: List[str] = None) -> Dict:
        """Send email"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.config['from_name']} <{self.config['from_email']}>"
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add body
            if html_body:
                part1 = MIMEText(body, 'plain')
                part2 = MIMEText(html_body, 'html')
                msg.attach(part1)
                msg.attach(part2)
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            # Add attachments
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as f:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(f.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename= {os.path.basename(file_path)}'
                            )
                            msg.attach(part)
            
            # Connect and send
            server = smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port'])
            if self.config.get('use_tls', True):
                server.starttls()
            
            server.login(self.config['username'], self.config['password'])
            server.send_message(msg)
            server.quit()
            
            # Log to database
            self.log_email(self.config['from_email'], to_email, subject, body, "sent", None, attachments)
            
            return {"status": "success", "message": "Email sent successfully"}
        
        except Exception as e:
            error_msg = str(e)
            self.log_email(self.config['from_email'], to_email, subject, body, "failed", error_msg, attachments)
            return {"status": "error", "message": error_msg}
    
    def log_email(self, from_email: str, to_email: str, subject: str, body: str,
                  status: str, error_message: Optional[str] = None, attachments: List[str] = None):
        """Log email to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        attachments_json = json.dumps(attachments) if attachments else None
        
        cursor.execute("""
            INSERT INTO email_history 
            (from_email, to_email, subject, body, status, error_message, attachments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (from_email, to_email, subject, body, status, error_message, attachments_json))
        
        conn.commit()
        conn.close()
    
    def get_email_history(self, limit: int = 50) -> List[Dict]:
        """Get email history"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, from_email, to_email, subject, status, sent_at, error_message
            FROM email_history
            ORDER BY sent_at DESC
            LIMIT ?
        """, (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": row[0],
                "from": row[1],
                "to": row[2],
                "subject": row[3],
                "status": row[4],
                "sent_at": row[5],
                "error": row[6]
            }
            for row in rows
        ]
    
    def add_contact(self, email: str, name: str = "", company: str = "", 
                    tags: List[str] = None, notes: str = ""):
        """Add email contact"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        tags_json = json.dumps(tags) if tags else None
        
        try:
            cursor.execute("""
                INSERT INTO email_contacts (email, name, company, tags, notes)
                VALUES (?, ?, ?, ?, ?)
            """, (email, name, company, tags_json, notes))
            conn.commit()
            console.print(f"[green]✅ Contact added: {email}[/green]")
        except sqlite3.IntegrityError:
            console.print(f"[yellow]⚠️  Contact already exists: {email}[/yellow]")
        
        conn.close()
    
    def get_contacts(self) -> List[Dict]:
        """Get all contacts"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, email, name, company, tags, notes FROM email_contacts")
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": row[0],
                "email": row[1],
                "name": row[2],
                "company": row[3],
                "tags": json.loads(row[4]) if row[4] else [],
                "notes": row[5]
            }
            for row in rows
        ]

if __name__ == "__main__":
    sender = EmailSender()
    console.print("[bold blue]Email Sender - Core Functionality[/bold blue]")
    console.print("\nConfigure with:")
    console.print("  sender.configure(smtp_server, port, username, password, from_email)")

