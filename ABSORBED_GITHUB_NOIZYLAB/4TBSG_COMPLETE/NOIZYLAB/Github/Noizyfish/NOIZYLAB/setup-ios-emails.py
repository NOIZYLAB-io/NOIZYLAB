#!/usr/bin/env python3
"""
iOS Email Setup - Configure All Emails on iOS Devices
======================================================
Creates configuration profiles and setup instructions for iOS
"""

import json
import plistlib
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class iOSEmailSetup:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
        self.config_path = self.base / "google_accounts.json"
        self.output_dir = self.base / "ios-configs"
        self.output_dir.mkdir(exist_ok=True)
    
    def load_emails(self):
        """Load email configuration"""
        if not self.config_path.exists():
            console.print("[red]❌ google_accounts.json not found. Run google-account-manager.py first.[/red]")
            return None
        
        with open(self.config_path) as f:
            return json.load(f)
    
    def create_gmail_config(self, email: str, password: str = None):
        """Create Gmail configuration for iOS"""
        # Gmail uses IMAP/SMTP with app-specific password
        config = {
            "account_description": f"Gmail - {email}",
            "email_address": email,
            "incoming_mail_server": {
                "hostname": "imap.gmail.com",
                "username": email,
                "password": password or "USE_APP_PASSWORD",
                "port": 993,
                "use_ssl": True
            },
            "outgoing_mail_server": {
                "hostname": "smtp.gmail.com",
                "username": email,
                "password": password or "USE_APP_PASSWORD",
                "port": 587,
                "use_tls": True
            }
        }
        return config
    
    def create_icloud_config(self, email: str, password: str = None):
        """Create iCloud configuration for iOS"""
        config = {
            "account_description": f"iCloud - {email}",
            "email_address": email,
            "incoming_mail_server": {
                "hostname": "imap.mail.me.com",
                "username": email,
                "password": password or "USE_ICLOUD_PASSWORD",
                "port": 993,
                "use_ssl": True
            },
            "outgoing_mail_server": {
                "hostname": "smtp.mail.me.com",
                "username": email,
                "password": password or "USE_ICLOUD_PASSWORD",
                "port": 587,
                "use_tls": True
            }
        }
        return config
    
    def create_custom_domain_config(self, email: str, domain: str, password: str = None):
        """Create custom domain email configuration"""
        # For noizylab.ca and fishmusicinc.com
        # Using Gmail/Google Workspace settings (most common)
        config = {
            "account_description": f"{domain} - {email}",
            "email_address": email,
            "incoming_mail_server": {
                "hostname": "imap.gmail.com",  # If using Google Workspace
                "username": email,
                "password": password or "USE_APP_PASSWORD",
                "port": 993,
                "use_ssl": True
            },
            "outgoing_mail_server": {
                "hostname": "smtp.gmail.com",
                "username": email,
                "password": password or "USE_APP_PASSWORD",
                "port": 587,
                "use_tls": True
            }
        }
        return config
    
    def generate_ios_config_profiles(self):
        """Generate iOS configuration profiles"""
        emails_data = self.load_emails()
        if not emails_data:
            return
        
        console.print(Panel.fit(
            "[bold blue]Generating iOS Email Configurations[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        configs = []
        
        # Primary Gmail
        primary = emails_data.get("google_account", {}).get("primary", "")
        if primary:
            config = self.create_gmail_config(primary)
            configs.append(("gmail-primary", config))
            console.print(f"[green]✅ Gmail config: {primary}[/green]")
        
        # NoizyLab emails
        for email in emails_data.get("noizylab_emails", []):
            config = self.create_custom_domain_config(email, "noizylab.ca")
            configs.append((f"noizylab-{email.split('@')[0]}", config))
            console.print(f"[green]✅ NoizyLab config: {email}[/green]")
        
        # Fish Music emails
        for email in emails_data.get("fishmusic_emails", []):
            config = self.create_custom_domain_config(email, "fishmusicinc.com")
            configs.append((f"fishmusic-{email.split('@')[0]}", config))
            console.print(f"[green]✅ Fish Music config: {email}[/green]")
        
        # iCloud email
        recovery = emails_data.get("google_account", {}).get("recovery", "")
        if recovery and "icloud" in recovery:
            config = self.create_icloud_config(recovery)
            configs.append(("icloud-recovery", config))
            console.print(f"[green]✅ iCloud config: {recovery}[/green]")
        
        # Save configurations
        for name, config in configs:
            config_file = self.output_dir / f"{name}.json"
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
        
        console.print()
        console.print(f"[green]✅ Generated {len(configs)} iOS configurations[/green]")
        
        return configs
    
    def generate_setup_instructions(self):
        """Generate step-by-step iOS setup instructions"""
        instructions = """
# iOS Email Setup Instructions

## Quick Setup (Recommended: Gmail App)

### Option 1: Gmail App (Easiest)
1. Download Gmail app from App Store
2. Sign in with: rspplowman@gmail.com
3. Add accounts:
   - Go to Settings → Add Account
   - Add each email address
   - Use Gmail for all (if using Google Workspace)

### Option 2: iOS Mail App (Native)

#### For Gmail (rspplowman@gmail.com):
1. Settings → Mail → Accounts → Add Account
2. Select "Google"
3. Enter email and password
4. Enable Mail, Contacts, Calendars
5. Use App Password (not regular password)

#### For NoizyLab emails:
1. Settings → Mail → Accounts → Add Account
2. Select "Other"
3. Enter:
   - Email: your@noizylab.ca
   - Password: App Password
   - IMAP Server: imap.gmail.com
   - SMTP Server: smtp.gmail.com
   - Port: 993 (IMAP), 587 (SMTP)
   - SSL: Enabled

#### For Fish Music emails:
Same as NoizyLab, but use fishmusicinc.com addresses

## App Passwords Setup

### Gmail App Passwords:
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password
4. Use this password in iOS Mail settings

## Xcode Setup (For Development)

### 1. Install Xcode
```bash
xcode-select --install
```

### 2. Configure Signing
- Open Xcode
- Preferences → Accounts
- Add Apple ID
- Select team for signing

### 3. Device Setup
- Connect iOS device
- Trust computer on device
- Enable Developer Mode in Settings

## Automated Setup Script

Run the setup script:
```bash
cd ~/NOIZYLAB/email-intelligence
python3 setup-ios-emails.py
```

This generates configuration files you can use.
"""
        
        instructions_path = self.output_dir / "SETUP_INSTRUCTIONS.md"
        instructions_path.write_text(instructions)
        
        console.print(f"[green]✅ Instructions saved to {instructions_path}[/green]")

if __name__ == "__main__":
    setup = iOSEmailSetup()
    setup.generate_ios_config_profiles()
    setup.generate_setup_instructions()

