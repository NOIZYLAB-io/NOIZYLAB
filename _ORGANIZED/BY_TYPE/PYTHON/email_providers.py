#!/usr/bin/env python3
"""
Email Provider Configuration - Multi-Provider Setup
==================================================
Supports: iCloud, Microsoft Exchange, Google, Yahoo, AOL, Custom SMTP
"""

from typing import Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

class EmailProviderSetup:
    """Email provider configuration manager"""
    
    PROVIDERS = {
        "icloud": {
            "name": "iCloud",
            "smtp_server": "smtp.mail.me.com",
            "smtp_port": 587,
            "imap_server": "imap.mail.me.com",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "Apple iCloud Mail"
        },
        "exchange": {
            "name": "Microsoft Exchange",
            "smtp_server": "smtp.office365.com",
            "smtp_port": 587,
            "imap_server": "outlook.office365.com",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "Microsoft 365 / Outlook"
        },
        "google": {
            "name": "Google",
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "imap_server": "imap.gmail.com",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "Gmail / Google Workspace",
            "note": "Requires App Password for Gmail"
        },
        "yahoo": {
            "name": "Yahoo",
            "smtp_server": "smtp.mail.yahoo.com",
            "smtp_port": 587,
            "imap_server": "imap.mail.yahoo.com",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "Yahoo Mail"
        },
        "aol": {
            "name": "AOL",
            "smtp_server": "smtp.aol.com",
            "smtp_port": 587,
            "imap_server": "imap.aol.com",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "AOL Mail"
        },
        "custom": {
            "name": "Other Mail Account",
            "smtp_server": "",
            "smtp_port": 587,
            "imap_server": "",
            "imap_port": 993,
            "use_tls": True,
            "use_ssl": True,
            "description": "Custom SMTP/IMAP"
        }
    }
    
    @staticmethod
    def display_providers():
        """Display available email providers"""
        table = Table(title="📧 Email Account Providers", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="cyan", width=3)
        table.add_column("Provider", style="green")
        table.add_column("Description", style="white")
        
        providers = list(EmailProviderSetup.PROVIDERS.items())
        for i, (key, provider) in enumerate(providers, 1):
            table.add_row(str(i), provider['name'], provider['description'])
        
        console.print(table)
        return providers
    
    @staticmethod
    def setup_provider(provider_key: str) -> Optional[Dict]:
        """Setup a specific email provider"""
        if provider_key not in EmailProviderSetup.PROVIDERS:
            console.print(f"[red]❌ Unknown provider: {provider_key}[/red]")
            return None
        
        provider = EmailProviderSetup.PROVIDERS[provider_key]
        
        console.print()
        console.print(Panel.fit(
            f"[bold]Setting up {provider['name']}[/bold]\n{provider['description']}",
            border_style="cyan"
        ))
        console.print()
        
        # Get account details
        email = Prompt.ask("[bold]Email Address[/bold]")
        password = Prompt.ask("[bold]Password[/bold]", password=True)
        name = Prompt.ask("[bold]Display Name[/bold]", default=email.split('@')[0].title())
        
        # Custom provider needs server details
        if provider_key == "custom":
            console.print()
            console.print("[bold yellow]Custom SMTP Configuration:[/bold yellow]")
            smtp_server = Prompt.ask("[bold]SMTP Server[/bold]")
            smtp_port = int(Prompt.ask("[bold]SMTP Port[/bold]", default="587"))
            use_tls = Confirm.ask("[bold]Use TLS?[/bold]", default=True)
            
            provider['smtp_server'] = smtp_server
            provider['smtp_port'] = smtp_port
            provider['use_tls'] = use_tls
        
        # Special notes
        if provider_key == "google":
            console.print()
            console.print("[bold yellow]⚠️  Gmail Setup Note:[/bold yellow]")
            console.print("[dim]Gmail requires an App Password (not your regular password).[/dim]")
            console.print("[dim]Get one from: https://myaccount.google.com/apppasswords[/dim]")
            console.print()
            use_app_password = Confirm.ask("[bold]Using App Password?[/bold]", default=True)
            if not use_app_password:
                console.print("[yellow]⚠️  Regular password may not work with Gmail[/yellow]")
        
        # Create configuration
        config = {
            "provider": provider_key,
            "provider_name": provider['name'],
            "email": email,
            "password": password,
            "name": name,
            "smtp": {
                "server": provider['smtp_server'],
                "port": provider['smtp_port'],
                "username": email,
                "password": password,
                "use_tls": provider.get('use_tls', True)
            },
            "imap": {
                "server": provider.get('imap_server', ''),
                "port": provider.get('imap_port', 993),
                "username": email,
                "password": password,
                "use_ssl": provider.get('use_ssl', True)
            }
        }
        
        return config
    
    @staticmethod
    def test_connection(config: Dict) -> bool:
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
            return True
        except Exception as e:
            console.print(f"[red]❌ Connection failed: {e}[/red]")
            console.print("[yellow]⚠️  Check your credentials and try again[/yellow]")
            return False
    
    @staticmethod
    def save_to_identities(config: Dict, identity_key: Optional[str] = None):
        """Save provider config as email identity"""
        import json
        from pathlib import Path
        
        config_path = Path("config/email_config.json")
        
        # Load existing config
        if config_path.exists():
            with open(config_path, 'r') as f:
                email_config = json.load(f)
        else:
            email_config = {
                "smtp": config['smtp'],
                "identities": {}
            }
        
        # Generate identity key if not provided
        if not identity_key:
            identity_key = config['provider'] + "_" + config['email'].split('@')[0]
        
        # Add identity
        email_config['identities'][identity_key] = {
            "name": config['name'],
            "email": config['email'],
            "signature": f"\n\n--\n{config['name']}",
            "provider": config['provider'],
            "provider_name": config['provider_name']
        }
        
        # Update SMTP if this is the first identity
        if not email_config.get('smtp'):
            email_config['smtp'] = config['smtp']
        
        # Save
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(email_config, f, indent=2)
        
        console.print(f"[green]✅ Account saved as identity: {identity_key}[/green]")
        return identity_key

