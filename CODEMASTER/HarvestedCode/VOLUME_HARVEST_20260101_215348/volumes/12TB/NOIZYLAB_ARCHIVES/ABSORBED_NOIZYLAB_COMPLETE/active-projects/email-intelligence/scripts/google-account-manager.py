#!/usr/bin/env python3
"""
Google Account Email Manager - Manage All Google Account Emails
================================================================
Integrates your Google Account emails with NoizyLab
"""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime

console = Console()

class GoogleAccountManager:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
        self.db_path = self.base / "data" / "email_intelligence.db"
        self.config_path = self.base / "config" / "security" / "google_accounts.json"
        self.init_database()
    
    def init_database(self):
        """Initialize database for Google account emails"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS google_account_emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                account_type TEXT,
                purpose TEXT,
                sharing_status TEXT,
                is_primary INTEGER DEFAULT 0,
                is_recovery INTEGER DEFAULT 0,
                is_contact INTEGER DEFAULT 0,
                is_alternate INTEGER DEFAULT 0,
                is_about_me INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def import_from_screenshot(self):
        """Import emails from the screenshot data"""
        emails = {
            "google_account": {
                "email": "rspplowman@gmail.com",
                "purpose": "Primary Google Account email - cannot be changed",
                "is_primary": True
            },
            "recovery": {
                "email": "rsplowman@icloud.com",
                "purpose": "Recovery email for account security",
                "is_recovery": True
            },
            "contact": {
                "email": "rsplowman@icloud.com",
                "purpose": "Contact email for Google products",
                "is_contact": True
            },
            "alternate": {
                "email": "rsplowman@icloud.com",
                "purpose": "Alternate email for sign-in",
                "is_alternate": True
            },
            "about_me": [
                {"email": "rsp@noizylab.ca", "sharing": "shared", "purpose": "Shared with everyone"},
                {"email": "rp@fishmusicinc.com", "sharing": "private", "purpose": "Not shared"},
                {"email": "help@noizylab.ca", "sharing": "private", "purpose": "Not shared"},
                {"email": "hello@noizylab.ca", "sharing": "private", "purpose": "Not shared"},
                {"email": "info@fishmusicinc.com", "sharing": "private", "purpose": "Not shared"},
                {"email": "rsplowman@icloud.com", "sharing": "private", "purpose": "Not shared"}
            ]
        }
        
        return emails
    
    def add_email(self, email: str, account_type: str, purpose: str = "", 
                  sharing_status: str = "private", **flags):
        """Add email to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO google_account_emails 
                (email, account_type, purpose, sharing_status, is_primary, is_recovery, 
                 is_contact, is_alternate, is_about_me)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                email,
                account_type,
                purpose,
                sharing_status,
                flags.get("is_primary", 0),
                flags.get("is_recovery", 0),
                flags.get("is_contact", 0),
                flags.get("is_alternate", 0),
                flags.get("is_about_me", 0)
            ))
            conn.commit()
            console.print(f"[green]✅ Added: {email}[/green]")
        except sqlite3.IntegrityError:
            # Update existing
            cursor.execute("""
                UPDATE google_account_emails
                SET account_type = ?, purpose = ?, sharing_status = ?,
                    is_primary = ?, is_recovery = ?, is_contact = ?,
                    is_alternate = ?, is_about_me = ?
                WHERE email = ?
            """, (
                account_type, purpose, sharing_status,
                flags.get("is_primary", 0), flags.get("is_recovery", 0),
                flags.get("is_contact", 0), flags.get("is_alternate", 0),
                flags.get("is_about_me", 0), email
            ))
            conn.commit()
            console.print(f"[yellow]⚠️  Updated: {email}[/yellow]")
        
        conn.close()
    
    def import_all_emails(self):
        """Import all emails from screenshot"""
        console.print(Panel.fit(
            "[bold blue]Importing Google Account Emails[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        emails_data = self.import_from_screenshot()
        
        # Primary account
        self.add_email(
            emails_data["google_account"]["email"],
            "google_account",
            emails_data["google_account"]["purpose"],
            is_primary=True
        )
        
        # Recovery
        self.add_email(
            emails_data["recovery"]["email"],
            "recovery",
            emails_data["recovery"]["purpose"],
            is_recovery=True
        )
        
        # Contact
        self.add_email(
            emails_data["contact"]["email"],
            "contact",
            emails_data["contact"]["purpose"],
            is_contact=True
        )
        
        # Alternate
        self.add_email(
            emails_data["alternate"]["email"],
            "alternate",
            emails_data["alternate"]["purpose"],
            is_alternate=True
        )
        
        # About Me emails
        for email_data in emails_data["about_me"]:
            self.add_email(
                email_data["email"],
                "about_me",
                email_data["purpose"],
                sharing_status=email_data["sharing"],
                is_about_me=True
            )
        
        console.print()
        console.print("[bold green]✅ All emails imported![/bold green]")
    
    def get_all_emails(self) -> List[Dict]:
        """Get all Google account emails"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT email, account_type, purpose, sharing_status, is_primary,
                   is_recovery, is_contact, is_alternate, is_about_me
            FROM google_account_emails
            ORDER BY is_primary DESC, email
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                "email": row[0],
                "type": row[1],
                "purpose": row[2],
                "sharing": row[3],
                "is_primary": bool(row[4]),
                "is_recovery": bool(row[5]),
                "is_contact": bool(row[6]),
                "is_alternate": bool(row[7]),
                "is_about_me": bool(row[8])
            }
            for row in rows
        ]
    
    def display_emails(self):
        """Display all emails in a table"""
        emails = self.get_all_emails()
        
        if not emails:
            console.print("[yellow]No emails found. Run import_all_emails() first.[/yellow]")
            return
        
        table = Table(title="Google Account Emails", box=box.ROUNDED)
        table.add_column("Email", style="cyan")
        table.add_column("Type", style="green")
        table.add_column("Purpose", style="yellow")
        table.add_column("Sharing", style="magenta")
        table.add_column("Flags", style="blue")
        
        for email in emails:
            flags = []
            if email["is_primary"]:
                flags.append("Primary")
            if email["is_recovery"]:
                flags.append("Recovery")
            if email["is_contact"]:
                flags.append("Contact")
            if email["is_alternate"]:
                flags.append("Alternate")
            if email["is_about_me"]:
                flags.append("About Me")
            
            table.add_row(
                email["email"],
                email["type"],
                email["purpose"][:40] + "..." if len(email["purpose"]) > 40 else email["purpose"],
                email["sharing"],
                ", ".join(flags) if flags else "-"
            )
        
        console.print(table)
    
    def sync_with_email_intelligence(self):
        """Sync Google account emails with email intelligence system"""
        console.print("[cyan]🔄 Syncing with Email Intelligence...[/cyan]")
        
        emails = self.get_all_emails()
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        for email_data in emails:
            # Add to email_list if not exists
            cursor.execute("""
                INSERT OR IGNORE INTO email_list (email, valid, category, enriched_info)
                VALUES (?, 1, ?, ?)
            """, (
                email_data["email"],
                email_data["type"],
                json.dumps({
                    "source": "google_account",
                    "purpose": email_data["purpose"],
                    "sharing": email_data["sharing"],
                    "flags": {
                        "primary": email_data["is_primary"],
                        "recovery": email_data["is_recovery"],
                        "contact": email_data["is_contact"]
                    }
                })
            ))
        
        conn.commit()
        conn.close()
        
        console.print(f"[green]✅ Synced {len(emails)} emails[/green]")
    
    def generate_config(self):
        """Generate email configuration for NoizyLab"""
        emails = self.get_all_emails()
        
        config = {
            "google_account": {
                "primary": next((e["email"] for e in emails if e["is_primary"]), ""),
                "recovery": next((e["email"] for e in emails if e["is_recovery"]), ""),
                "contact": next((e["email"] for e in emails if e["is_contact"]), "")
            },
            "noizylab_emails": [
                e["email"] for e in emails 
                if "noizylab" in e["email"].lower()
            ],
            "fishmusic_emails": [
                e["email"] for e in emails 
                if "fishmusic" in e["email"].lower()
            ],
            "about_me_shared": [
                e["email"] for e in emails 
                if e["is_about_me"] and e["sharing"] == "shared"
            ],
            "about_me_private": [
                e["email"] for e in emails 
                if e["is_about_me"] and e["sharing"] == "private"
            ]
        }
        
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print(f"[green]✅ Configuration saved to {self.config_path}[/green]")
        return config

if __name__ == "__main__":
    manager = GoogleAccountManager()
    
    console.print(Panel.fit(
        "[bold blue]Google Account Email Manager[/bold blue]",
        border_style="blue"
    ))
    console.print()
    
    # Import emails
    manager.import_all_emails()
    console.print()
    
    # Display
    manager.display_emails()
    console.print()
    
    # Sync
    manager.sync_with_email_intelligence()
    console.print()
    
    # Generate config
    manager.generate_config()

