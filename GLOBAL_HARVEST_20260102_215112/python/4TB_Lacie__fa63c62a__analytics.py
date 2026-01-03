#!/usr/bin/env python3
"""
Email Analytics - Statistics and Reporting
==========================================
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

class EmailAnalytics:
    def __init__(self, log_path: str = "email_history.log"):
        """Initialize Email Analytics"""
        self.log_path = Path(log_path)
    
    def parse_log_entry(self, line: str) -> Dict:
        """Parse a log entry"""
        try:
            # Format: [timestamp] status | From: email | To: email | Subject: subject
            if "|" not in line:
                return None
            
            parts = line.split("|")
            if len(parts) < 4:
                return None
            
            timestamp_str = parts[0].strip().replace("[", "").replace("]", "")
            status = parts[0].split("]")[1].strip() if "]" in parts[0] else "unknown"
            
            from_email = parts[1].replace("From:", "").strip() if "From:" in parts[1] else ""
            to_email = parts[2].replace("To:", "").strip() if "To:" in parts[2] else ""
            subject = parts[3].replace("Subject:", "").strip() if "Subject:" in parts[3] else ""
            
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            except:
                timestamp = datetime.now()
            
            return {
                "timestamp": timestamp,
                "status": status.lower(),
                "from": from_email,
                "to": to_email,
                "subject": subject
            }
        except:
            return None
    
    def get_all_logs(self) -> List[Dict]:
        """Get all parsed log entries"""
        if not self.log_path.exists():
            return []
        
        logs = []
        try:
            with open(self.log_path, 'r') as f:
                for line in f:
                    entry = self.parse_log_entry(line.strip())
                    if entry:
                        logs.append(entry)
        except:
            pass
        
        return logs
    
    def get_statistics(self, days: int = 30) -> Dict:
        """Get comprehensive statistics"""
        logs = self.get_all_logs()
        
        # Filter by date range
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_logs = [log for log in logs if log['timestamp'] >= cutoff_date]
        
        stats = {
            "total_emails": len(recent_logs),
            "sent": len([l for l in recent_logs if "sent" in l['status']]),
            "failed": len([l for l in recent_logs if "failed" in l['status']]),
            "success_rate": 0,
            "by_day": {},
            "by_identity": {},
            "top_recipients": {},
            "recent_activity": recent_logs[-10:]
        }
        
        if stats["total_emails"] > 0:
            stats["success_rate"] = (stats["sent"] / stats["total_emails"]) * 100
        
        # Group by day
        for log in recent_logs:
            day = log['timestamp'].strftime("%Y-%m-%d")
            stats["by_day"][day] = stats["by_day"].get(day, 0) + 1
        
        # Group by identity (from email)
        for log in recent_logs:
            identity = log['from'].split("@")[0] if "@" in log['from'] else "unknown"
            stats["by_identity"][identity] = stats["by_identity"].get(identity, 0) + 1
        
        # Top recipients
        for log in recent_logs:
            if log['to']:
                stats["top_recipients"][log['to']] = stats["top_recipients"].get(log['to'], 0) + 1
        
        return stats
    
    def display_dashboard(self, days: int = 30):
        """Display analytics dashboard"""
        stats = self.get_statistics(days)
        
        # Header
        console.print(Panel.fit(
            f"[bold cyan]Email Analytics Dashboard[/bold cyan]\n"
            f"[dim]Last {days} days[/dim]",
            border_style="cyan"
        ))
        console.print()
        
        # Key Metrics
        metrics_table = Table.grid(padding=(0, 2))
        metrics_table.add_row(
            "[bold]Total Emails:[/bold]", f"[green]{stats['total_emails']}[/green]",
            "[bold]Sent:[/bold]", f"[green]{stats['sent']}[/green]",
            "[bold]Failed:[/bold]", f"[red]{stats['failed']}[/red]"
        )
        metrics_table.add_row(
            "[bold]Success Rate:[/bold]", 
            f"[{'green' if stats['success_rate'] > 90 else 'yellow' if stats['success_rate'] > 70 else 'red'}]{stats['success_rate']:.1f}%[/{'green' if stats['success_rate'] > 90 else 'yellow' if stats['success_rate'] > 70 else 'red'}]"
        )
        console.print(metrics_table)
        console.print()
        
        # Top Identities
        if stats['by_identity']:
            identity_table = Table(title="📊 Emails by Identity", show_header=True, header_style="bold magenta")
            identity_table.add_column("Identity", style="cyan")
            identity_table.add_column("Count", style="green", justify="right")
            
            sorted_identities = sorted(stats['by_identity'].items(), key=lambda x: x[1], reverse=True)
            for identity, count in sorted_identities[:10]:
                identity_table.add_row(identity, str(count))
            
            console.print(identity_table)
            console.print()
        
        # Top Recipients
        if stats['top_recipients']:
            recipient_table = Table(title="📧 Top Recipients", show_header=True, header_style="bold magenta")
            recipient_table.add_column("Email", style="yellow")
            recipient_table.add_column("Count", style="green", justify="right")
            
            sorted_recipients = sorted(stats['top_recipients'].items(), key=lambda x: x[1], reverse=True)
            for email, count in sorted_recipients[:10]:
                recipient_table.add_row(email, str(count))
            
            console.print(recipient_table)
            console.print()
        
        # Recent Activity
        if stats['recent_activity']:
            activity_table = Table(title="🕐 Recent Activity", show_header=True, header_style="bold magenta")
            activity_table.add_column("Time", style="dim", width=16)
            activity_table.add_column("Status", style="green")
            activity_table.add_column("To", style="yellow")
            activity_table.add_column("Subject", style="white")
            
            for log in stats['recent_activity'][-5:]:
                time_str = log['timestamp'].strftime("%Y-%m-%d %H:%M")
                status_style = "green" if "sent" in log['status'] else "red"
                activity_table.add_row(
                    time_str,
                    f"[{status_style}]{log['status']}[/{status_style}]",
                    log['to'][:30],
                    log['subject'][:40]
                )
            
            console.print(activity_table)

