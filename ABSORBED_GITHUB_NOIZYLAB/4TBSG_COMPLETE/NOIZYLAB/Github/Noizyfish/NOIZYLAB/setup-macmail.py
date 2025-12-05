#!/usr/bin/env python3
"""
MacMail Setup - Configure All Emails in macOS Mail App
=======================================================
Automates email setup for macOS Mail application
"""

import subprocess
import json
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class MacMailSetup:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
        self.config_path = self.base / "google_accounts.json"
    
    def load_emails(self):
        """Load email configuration"""
        if not self.config_path.exists():
            console.print("[red]❌ google_accounts.json not found[/red]")
            return None
        
        with open(self.config_path) as f:
            return json.load(f)
    
    def create_mail_account_script(self, email: str, domain: str = None):
        """Create AppleScript to add email account to Mail"""
        if domain == "gmail.com" or not domain:
            # Gmail account
            script = f'''
tell application "Mail"
    set newAccount to make new account with properties {{name:"{email}", account type:imap account}}
    set fullName of newAccount to "{email}"
    set emailAddresses of newAccount to {{"{email}"}}
    set userName of newAccount to "{email}"
    set password of newAccount to "USE_APP_PASSWORD"
    set serverName of newAccount to "imap.gmail.com"
    set port of newAccount to 993
    set usesSSL of newAccount to true
    set usesTLS of newAccount to false
    
    -- SMTP settings
    set smtpServer of newAccount to "smtp.gmail.com"
    set smtpPort of newAccount to 587
    set smtpUsesSSL of newAccount to false
    set smtpUsesTLS of newAccount to true
end tell
'''
        else:
            # Custom domain (assuming Google Workspace)
            script = f'''
tell application "Mail"
    set newAccount to make new account with properties {{name:"{email}", account type:imap account}}
    set fullName of newAccount to "{email}"
    set emailAddresses of newAccount to {{"{email}"}}
    set userName of newAccount to "{email}"
    set password of newAccount to "USE_APP_PASSWORD"
    set serverName of newAccount to "imap.gmail.com"
    set port of newAccount to 993
    set usesSSL of newAccount to true
    set usesTLS of newAccount to false
    
    -- SMTP settings
    set smtpServer of newAccount to "smtp.gmail.com"
    set smtpPort of newAccount to 587
    set smtpUsesSSL of newAccount to false
    set smtpUsesTLS of newAccount to true
end tell
'''
        return script
    
    def generate_setup_scripts(self):
        """Generate setup scripts for all emails"""
        emails_data = self.load_emails()
        if not emails_data:
            return
        
        console.print(Panel.fit(
            "[bold blue]Generating MacMail Setup Scripts[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        scripts_dir = self.base / "macmail-scripts"
        scripts_dir.mkdir(exist_ok=True)
        
        scripts = []
        
        # Primary Gmail
        primary = emails_data.get("google_account", {}).get("primary", "")
        if primary:
            script = self.create_mail_account_script(primary, "gmail.com")
            script_path = scripts_dir / "setup-gmail-primary.applescript"
            script_path.write_text(script)
            scripts.append(("Gmail Primary", script_path))
            console.print(f"[green]✅ Gmail script: {primary}[/green]")
        
        # NoizyLab emails
        for email in emails_data.get("noizylab_emails", []):
            script = self.create_mail_account_script(email, "noizylab.ca")
            name = email.split('@')[0]
            script_path = scripts_dir / f"setup-noizylab-{name}.applescript"
            script_path.write_text(script)
            scripts.append((f"NoizyLab {name}", script_path))
            console.print(f"[green]✅ NoizyLab script: {email}[/green]")
        
        # Fish Music emails
        for email in emails_data.get("fishmusic_emails", []):
            script = self.create_mail_account_script(email, "fishmusicinc.com")
            name = email.split('@')[0]
            script_path = scripts_dir / f"setup-fishmusic-{name}.applescript"
            script_path.write_text(script)
            scripts.append((f"Fish Music {name}", script_path))
            console.print(f"[green]✅ Fish Music script: {email}[/green]")
        
        # Create master script
        master_script = "#!/bin/bash\n# Setup All MacMail Accounts\n\n"
        for name, script_path in scripts:
            master_script += f'echo "Setting up {name}..."\n'
            master_script += f'osascript "{script_path}"\n'
            master_script += 'sleep 2\n\n'
        
        master_path = scripts_dir / "setup-all-accounts.sh"
        master_path.write_text(master_script)
        master_path.chmod(0o755)
        
        console.print()
        console.print(f"[green]✅ Generated {len(scripts)} MacMail scripts[/green]")
        console.print(f"[green]✅ Master script: {master_path}[/green]")
        
        return scripts
    
    def create_manual_setup_guide(self):
        """Create manual setup guide"""
        guide = """
# MacMail Setup Guide - All Emails

## Quick Setup (Recommended: Use Scripts)

### Automated Setup:
```bash
cd ~/NOIZYLAB/email-intelligence/macmail-scripts
./setup-all-accounts.sh
```

### Manual Setup:

#### 1. Open Mail App
- Applications → Mail

#### 2. Add Gmail Account (rspplowman@gmail.com)
- Mail → Add Account
- Select "Google"
- Enter email and password
- Use App Password (not regular password)
- Enable Mail, Contacts, Calendars

#### 3. Add NoizyLab Emails
For each email (rsp@, help@, hello@noizylab.ca):
- Mail → Add Account
- Select "Other Mail Account"
- Enter:
  - Name: Your Name
  - Email: your@noizylab.ca
  - Password: App Password
- Click "Sign In"
- If prompted, enter manually:
  - Incoming: imap.gmail.com, Port 993, SSL
  - Outgoing: smtp.gmail.com, Port 587, TLS

#### 4. Add Fish Music Emails
Same as NoizyLab, but use fishmusicinc.com addresses

## Gmail App Passwords

1. Go to: https://myaccount.google.com/apppasswords
2. Generate App Password for "Mail"
3. Use this password (not your regular password)

## Troubleshooting

- If connection fails, check App Password
- Ensure 2-Step Verification is enabled
- Try removing and re-adding account
- Check firewall settings
"""
        
        guide_path = self.base / "macmail-scripts" / "MANUAL_SETUP.md"
        guide_path.write_text(guide)
        console.print(f"[green]✅ Manual guide saved[/green]")

if __name__ == "__main__":
    setup = MacMailSetup()
    setup.generate_setup_scripts()
    setup.create_manual_setup_guide()

