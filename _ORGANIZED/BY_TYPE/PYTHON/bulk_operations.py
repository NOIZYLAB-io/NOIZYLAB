#!/usr/bin/env python3
"""
Bulk Operations - Send emails to multiple recipients
====================================================
"""

from typing import List, Dict
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table

console = Console()

class BulkEmailSender:
    """Send emails to multiple recipients"""
    
    def __init__(self, mailer):
        """Initialize Bulk Email Sender"""
        self.mailer = mailer
    
    def send_bulk(self, identity_key: str, recipients: List[str], subject: str,
                  body: str, personalize: bool = False, delay: float = 1.0) -> Dict:
        """Send email to multiple recipients"""
        import time
        
        results = {
            "total": len(recipients),
            "sent": 0,
            "failed": 0,
            "errors": []
        }
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Sending bulk emails...", total=len(recipients))
            
            for i, recipient in enumerate(recipients):
                # Personalize if requested
                personalized_body = body
                if personalize:
                    personalized_body = body.replace("{name}", recipient.split('@')[0].title())
                    personalized_body = body.replace("{email}", recipient)
                
                # Send email
                try:
                    success = self.mailer.send_email(identity_key, recipient, subject, personalized_body)
                    if success:
                        results["sent"] += 1
                    else:
                        results["failed"] += 1
                        results["errors"].append(f"{recipient}: Send failed")
                except Exception as e:
                    results["failed"] += 1
                    results["errors"].append(f"{recipient}: {str(e)}")
                
                # Update progress
                progress.update(task, advance=1)
                
                # Delay between sends
                if i < len(recipients) - 1:
                    time.sleep(delay)
        
        return results
    
    def display_results(self, results: Dict):
        """Display bulk send results"""
        table = Table(title="📊 Bulk Send Results", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan")
        table.add_column("Count", style="green", justify="right")
        
        table.add_row("Total Recipients", str(results["total"]))
        table.add_row("Sent Successfully", f"[green]{results['sent']}[/green]")
        table.add_row("Failed", f"[red]{results['failed']}[/red]")
        table.add_row("Success Rate", f"{((results['sent']/results['total'])*100):.1f}%")
        
        console.print(table)
        
        if results["errors"]:
            console.print("\n[bold red]Errors:[/bold red]")
            for error in results["errors"][:10]:  # Show first 10 errors
                console.print(f"  • {error}")
            if len(results["errors"]) > 10:
                console.print(f"  ... and {len(results['errors']) - 10} more")

