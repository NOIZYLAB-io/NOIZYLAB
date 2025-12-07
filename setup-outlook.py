#!/usr/bin/env python3
"""
Outlook Setup - Configure All Emails in Microsoft Outlook
=========================================================
Creates Outlook configuration for all emails
"""

import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

class OutlookSetup:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
        self.config_path = self.base / "google_accounts.json"
    
    def load_emails(self):
        """Load email configuration"""
        if not self.config_path.exists():
            return None
        with open(self.config_path) as f:
            return json.load(f)
    
    def create_outlook_config(self, email: str, domain: str = None):
        """Create Outlook configuration"""
        if domain == "outlook.com" or not domain:
            config = {
                "account_type": "IMAP",
                "email": email,
                "incoming_server": "outlook.office365.com",
                "incoming_port": 993,
                "incoming_ssl": True,
                "outgoing_server": "smtp.office365.com",
                "outgoing_port": 587,
                "outgoing_tls": True,
                "username": email,
                "password": "USE_M365_PASSWORD"
            }
        else:
            # Custom domain (Google Workspace or other)
            config = {
                "account_type": "IMAP",
                "email": email,
                "incoming_server": "imap.gmail.com",
                "incoming_port": 993,
                "incoming_ssl": True,
                "outgoing_server": "smtp.gmail.com",
                "outgoing_port": 587,
                "outgoing_tls": True,
                "username": email,
                "password": "USE_APP_PASSWORD"
            }
        return config
    
    def generate_outlook_configs(self):
        """Generate Outlook configurations"""
        emails_data = self.load_emails()
        if not emails_data:
            return
        
        console.print(Panel.fit(
            "[bold blue]Generating Outlook Configurations[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        configs_dir = self.base / "outlook-configs"
        configs_dir.mkdir(exist_ok=True)
        
        configs = []
        
        # Primary Microsoft 365
        primary = "rsplowman@outlook.com"
        config = self.create_outlook_config(primary, "outlook.com")
        config_path = configs_dir / "m365-primary.json"
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        configs.append(("Microsoft 365 Primary", config_path))
        console.print(f"[green]✅ Microsoft 365 config: {primary}[/green]")
        
        # NoizyLab
        for email in emails_data.get("noizylab_emails", []):
            config = self.create_outlook_config(email, "noizylab.ca")
            name = email.split('@')[0]
            config_path = configs_dir / f"noizylab-{name}.json"
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            configs.append((f"NoizyLab {name}", config_path))
            console.print(f"[green]✅ NoizyLab config: {email}[/green]")
        
        # Fish Music
        for email in emails_data.get("fishmusic_emails", []):
            config = self.create_outlook_config(email, "fishmusicinc.com")
            name = email.split('@')[0]
            config_path = configs_dir / f"fishmusic-{name}.json"
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            configs.append((f"Fish Music {name}", config_path))
            console.print(f"[green]✅ Fish Music config: {email}[/green]")
        
        # Create setup guide
        guide = """
# Outlook Setup Guide

## Add Email Account

### For Microsoft 365:
1. Outlook → Preferences → Accounts
2. Click "+" → New Account
3. Enter email address: rsplowman@outlook.com
4. Select "IMAP"
5. Enter:
   - Incoming: outlook.office365.com:993 (SSL)
   - Outgoing: smtp.office365.com:587 (TLS)
   - Username: rsplowman@outlook.com
   - Password: M365 Password or App Password

### For Custom Domains (NoizyLab/Fish Music):
Check if using Google Workspace or other provider

## App Passwords
- Microsoft 365: https://account.microsoft.com/security
- Google Workspace: https://myaccount.google.com/apppasswords
"""
        
        guide_path = configs_dir / "SETUP_GUIDE.md"
        guide_path.write_text(guide)
        
        console.print()
        console.print(f"[green]✅ Generated {len(configs)} Outlook configs[/green]")

if __name__ == "__main__":
    setup = OutlookSetup()
    setup.generate_outlook_configs()

