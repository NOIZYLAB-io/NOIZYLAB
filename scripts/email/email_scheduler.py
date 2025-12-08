#!/usr/bin/env python3
"""
Email Scheduler - Schedule emails for later sending
==================================================
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class EmailScheduler:
    """Schedule emails for future sending"""
    
    def __init__(self, schedule_path: str = "config/scheduled_emails.json"):
        """Initialize Email Scheduler"""
        self.schedule_path = Path(schedule_path)
        self.schedule_path.parent.mkdir(parents=True, exist_ok=True)
        self.scheduled = self.load_schedule()
    
    def load_schedule(self) -> List[Dict]:
        """Load scheduled emails"""
        if not self.schedule_path.exists():
            return []
        
        try:
            with open(self.schedule_path, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def save_schedule(self):
        """Save scheduled emails"""
        with open(self.schedule_path, 'w') as f:
            json.dump(self.scheduled, f, indent=2)
    
    def schedule_email(self, identity_key: str, to: str, subject: str, body: str,
                      send_at: datetime, attachments: Optional[List[str]] = None) -> str:
        """Schedule an email for future sending"""
        schedule_id = f"scheduled_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        scheduled_email = {
            "id": schedule_id,
            "identity": identity_key,
            "to": to,
            "subject": subject,
            "body": body,
            "send_at": send_at.isoformat(),
            "created_at": datetime.now().isoformat(),
            "status": "scheduled",
            "attachments": attachments or []
        }
        
        self.scheduled.append(scheduled_email)
        self.save_schedule()
        
        console.print(f"[green]✅ Email scheduled for {send_at.strftime('%Y-%m-%d %H:%M')}[/green]")
        return schedule_id
    
    def get_due_emails(self) -> List[Dict]:
        """Get emails that are due to be sent"""
        now = datetime.now()
        due = []
        
        for email in self.scheduled:
            if email['status'] == 'scheduled':
                send_at = datetime.fromisoformat(email['send_at'])
                if send_at <= now:
                    due.append(email)
        
        return due
    
    def cancel_scheduled(self, schedule_id: str) -> bool:
        """Cancel a scheduled email"""
        for email in self.scheduled:
            if email['id'] == schedule_id and email['status'] == 'scheduled':
                email['status'] = 'cancelled'
                self.save_schedule()
                console.print(f"[green]✅ Scheduled email cancelled[/green]")
                return True
        return False
    
    def list_scheduled(self) -> List[Dict]:
        """List all scheduled emails"""
        return [e for e in self.scheduled if e['status'] == 'scheduled']
    
    def display_scheduled(self):
        """Display scheduled emails in a table"""
        scheduled = self.list_scheduled()
        
        if not scheduled:
            console.print("[yellow]No scheduled emails[/yellow]")
            return
        
        table = Table(title="📅 Scheduled Emails", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="cyan", width=20)
        table.add_column("To", style="yellow")
        table.add_column("Subject", style="white")
        table.add_column("Send At", style="green")
        
        for email in scheduled:
            send_at = datetime.fromisoformat(email['send_at'])
            table.add_row(
                email['id'],
                email['to'],
                email['subject'][:40],
                send_at.strftime('%Y-%m-%d %H:%M')
            )
        
        console.print(table)

