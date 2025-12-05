#!/usr/bin/env python3
"""
Configuration Wizard - First-Time Setup
========================================
"""

import json
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import box

console = Console()

class ConfigWizard:
    def __init__(self, config_path: str = "config/email_config.json"):
        """Initialize Configuration Wizard"""
        self.config_path = Path(config_path)
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
    
    def run(self):
        """Run the configuration wizard"""
        console.print(Panel.fit(
            "[bold cyan]NoizyLab Email Intelligence[/bold cyan]\n"
            "[dim]Configuration Wizard[/dim]",
            border_style="cyan"
        ))
        console.print()
        
        console.print("[bold]Let's set up your email system![/bold]")
        console.print()
        
        # SMTP Configuration
        console.print(Panel.fit(
            "[bold]Step 1: SMTP Server Configuration[/bold]",
            border_style="yellow"
        ))
        
        smtp_server = Prompt.ask(
            "[bold]SMTP Server[/bold]",
            default="smtp.office365.com",
            choices=["smtp.office365.com", "smtp.gmail.com", "smtp.mail.yahoo.com", "custom"]
        )
        
        if smtp_server == "custom":
            smtp_server = Prompt.ask("[bold]Enter custom SMTP server[/bold]")
        
        smtp_port = int(Prompt.ask("[bold]SMTP Port[/bold]", default="587"))
        smtp_username = Prompt.ask("[bold]Email Username[/bold]")
        smtp_password = Prompt.ask("[bold]Email Password[/bold]", password=True)
        
        console.print()
        
        # Identity Configuration
        console.print(Panel.fit(
            "[bold]Step 2: Email Identity[/bold]",
            border_style="yellow"
        ))
        
        identity_name = Prompt.ask("[bold]Your Name[/bold]")
        identity_email = Prompt.ask("[bold]Your Email Address[/bold]")
        
        # Create config
        config = {
            "smtp": {
                "server": smtp_server,
                "port": smtp_port,
                "username": smtp_username,
                "password": smtp_password,
                "use_tls": True,
                "timeout": 30
            },
            "identities": {
                "personal": {
                    "name": identity_name,
                    "email": identity_email,
                    "signature": f"\n\n--\n{identity_name}"
                }
            },
            "settings": {
                "auto_save_drafts": True,
                "log_level": "detailed",
                "retry_attempts": 3
            }
        }
        
        # Save config
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ Configuration saved successfully![/bold green]",
            border_style="green"
        ))
        console.print()
        
        # Test connection
        test = Confirm.ask("[bold]Would you like to test the connection?[/bold]", default=True)
        if test:
            self.test_connection(config)
    
    def test_connection(self, config: dict):
        """Test SMTP connection"""
        import smtplib
        
        console.print()
        console.print("[dim]Testing connection...[/dim]")
        
        try:
            server = smtplib.SMTP(config['smtp']['server'], config['smtp']['port'], timeout=10)
            if config['smtp'].get('use_tls', True):
                server.starttls()
            server.login(config['smtp']['username'], config['smtp']['password'])
            server.quit()
            
            console.print("[green]✅ Connection successful![/green]")
        except Exception as e:
            console.print(f"[red]❌ Connection failed: {e}[/red]")
            console.print("[yellow]⚠️  Please check your credentials and try again.[/yellow]")

