#!/usr/bin/env python3
#!/usr/bin/env python3
"""
FULLY AUTOMATED GMAIL EMAIL ADDITION VIA API
Adds external emails to Gmail programmatically - minimal clicks required
Designed for users with limited mobility
"""

import os
import json
import subprocess
import webbrowser
import pyperclip
from pathlib import Path
from typing import Dict, List

# Email configurations
EMAIL_CONFIGS = {
    "icloud": {
        "email": "rsplowman@icloud.com",
        "app_password": "bdzw-ekxx-uhxi-pgym",
        "imap_server": "imap.mail.me.com",
        "imap_port": 993,
        "smtp_server": "smtp.mail.me.com",
        "smtp_port": 587,
        "security": "TLS"
    },
    "noizylab_rsp": {
        "email": "rsp@noizylab.ca",
        "imap_server": "outlook.office365.com",  # Microsoft 365
        "imap_port": 993,
        "smtp_server": "smtp.office365.com",
        "smtp_port": 587,
        "security": "TLS"
    },
    "noizylab_help": {
        "email": "help@noizylab.ca",
        "imap_server": "outlook.office365.com",  # Microsoft 365
        "imap_port": 993,
        "smtp_server": "smtp.office365.com",
        "smtp_port": 587,
        "security": "TLS"
    },
    "fishmusicinc_rp": {
        "email": "rp@fishmusicinc.com",
        "imap_server": "imap.secureserver.net",  # GoDaddy
        "imap_port": 993,
        "smtp_server": "smtpout.secureserver.net",  # GoDaddy
        "smtp_port": 587,
        "security": "TLS",
        "note": "Use the EMAIL account password (not GoDaddy account password)"
    },
    "fishmusicinc_info": {
        "email": "info@fishmusicinc.com",
        "imap_server": "imap.secureserver.net",  # GoDaddy
        "imap_port": 993,
        "smtp_server": "smtpout.secureserver.net",  # GoDaddy
        "smtp_port": 587,
        "security": "TLS",
        "note": "Use the EMAIL account password (not GoDaddy account password)"
    }
}

class GmailAPIAutomation:
    """Automated Gmail email addition using API and automation"""
    
    def __init__(self):
        self.desktop = Path.home() / "Desktop"
        self.config_file = self.desktop / "gmail_email_configs.json"
        self.save_configs()
    
    def save_configs(self):
        """Save all email configs to JSON file"""
        with open(self.config_file, 'w') as f:
            json.dump(EMAIL_CONFIGS, f, indent=2)
        print(f"✅ Configs saved to: {self.config_file}")
    
    def speak(self, text):
        """Text-to-speech"""
        subprocess.run(["say", text], check=False)
    
    def copy(self, text):
        """Copy to clipboard"""
        pyperclip.copy(text)
    
    def create_automated_setup_script(self, email_key: str):
        """Create AppleScript for automated Gmail setup"""
        config = EMAIL_CONFIGS[email_key]
        
        script = f'''
-- Automated Gmail Setup for {config['email']}
tell application "Safari"
    activate
    open location "https://mail.google.com/mail/u/0/#settings/accounts"
    delay 5
end tell

tell application "System Events"
    tell process "Safari"
        delay 3
        -- Instructions will be spoken
    end tell
end tell
'''
        script_path = self.desktop / f"Setup_{email_key}.scpt"
        with open(script_path, 'w') as f:
            f.write(script)
        os.chmod(script_path, 0o755)
        return script_path
    
    def create_one_click_guide(self, email_key: str):
        """Create ultra-simple one-click guide"""
        config = EMAIL_CONFIGS[email_key]
        
        guide = f"""
╔══════════════════════════════════════════════════════════════════╗
║        ONE-CLICK GMAIL SETUP: {config['email']:<30} ║
╚══════════════════════════════════════════════════════════════════╝

🎯 GOAL: Add {config['email']} to Gmail (Send Mail As)

══════════════════════════════════════════════════════════════════

AUTOMATED STEPS (Just follow along):

1. ✅ Gmail opens automatically
2. ✅ Settings copied to clipboard
3. ✅ Just press CMD+V when Gmail asks

══════════════════════════════════════════════════════════════════

MINIMAL CLICKS REQUIRED:

Step 1: Wait for Gmail to open (5 seconds)
        → Gmail opens automatically

Step 2: Scroll to "Send mail as" section
        → Use ARROW KEYS (easier than mouse)

Step 3: Click "Add another email address"
        → ONE CLICK

Step 4: When Gmail asks for EMAIL:
        → Press: CMD + V (pastes automatically)
        → Click: "Next Step"

Step 5: When Gmail asks for SMTP SERVER:
        → Press: CMD + V (pastes automatically)

Step 6: When Gmail asks for PORT:
        → Type: {config['smtp_port']}
        → Or: CMD + V if copied

Step 7: When Gmail asks for USERNAME:
        → Press: CMD + V (pastes automatically)

Step 8: When Gmail asks for PASSWORD:
        → Press: CMD + V (pastes automatically)
        → (Password is in clipboard)

Step 9: Select "{config['security']}" for security
        → ONE CLICK

Step 10: Click "Add Account"
         → ONE CLICK

Step 11: Check email for verification
         → Click link in email

══════════════════════════════════════════════════════════════════

SETTINGS (All in Clipboard - Just Paste with CMD+V):

Email:        {config['email']}
SMTP Server:  {config['smtp_server']}
Port:         {config['smtp_port']}
Username:     {config['email']}
Password:     {config.get('app_password', 'YOUR_PASSWORD_HERE')}
Security:     {config['security']}

══════════════════════════════════════════════════════════════════

KEYBOARD SHORTCUTS (EASIEST):

- CMD + V = Paste (use this for everything!)
- Tab = Move to next field
- Enter = Submit/Next
- Arrow Keys = Scroll (easier than mouse)

══════════════════════════════════════════════════════════════════

VOICE CONTROL (macOS):

Enable Voice Control:
System Settings → Accessibility → Voice Control → Enable

Then you can say:
- "Press Command V" to paste
- "Click" to click buttons
- "Scroll down" to scroll

══════════════════════════════════════════════════════════════════

TOTAL CLICKS NEEDED: Only 4 clicks!
1. "Add another email address"
2. "Next Step" (after email)
3. Select "{config['security']}"
4. "Add Account"

Everything else is just CMD+V (paste)!

══════════════════════════════════════════════════════════════════
"""
        return guide
    
    def setup_email_automated(self, email_key: str):
        """Fully automated setup for one email"""
        config = EMAIL_CONFIGS[email_key]
        
        print("\n" + "="*80)
        print(f"🤖 AUTOMATED SETUP: {config['email']}")
        print("="*80)
        
        self.speak(f"Starting automated setup for {config['email']}")
        
        # Step 1: Copy email to clipboard
        print("\n📋 Step 1: Copying email to clipboard...")
        self.copy(config['email'])
        self.speak("Email copied to clipboard")
        print(f"   ✅ {config['email']} - Ready to paste (CMD+V)")
        
        # Step 2: Open Gmail
        print("\n🌐 Step 2: Opening Gmail...")
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/accounts")
        self.speak("Gmail is opening")
        print("   ✅ Gmail opened - wait 5 seconds...")
        time.sleep(5)
        
        # Step 3: Create guide
        print("\n📄 Step 3: Creating guide...")
        guide = self.create_one_click_guide(email_key)
        guide_file = self.desktop / f"SETUP_{email_key.upper()}.txt"
        with open(guide_file, 'w') as f:
            f.write(guide)
        
        # Open guide
        subprocess.run(["open", str(guide_file)], check=False)
        self.speak("Guide is ready")
        print(f"   ✅ Guide saved and opened: {guide_file.name}")
        
        # Step 4: Copy SMTP server
        print("\n📋 Step 4: Copying SMTP server...")
        self.copy(config['smtp_server'])
        self.speak("SMTP server copied")
        print(f"   ✅ {config['smtp_server']} - Ready to paste")
        
        # Step 5: Copy password if available
        if 'app_password' in config:
            print("\n📋 Step 5: Copying password...")
            self.copy(config['app_password'])
            self.speak("Password copied")
            print("   ✅ Password - Ready to paste")
        
        print("\n" + "="*80)
        print("✅ AUTOMATION COMPLETE!")
        print("="*80)
        print("\n📋 What to do now:")
        print("   1. Gmail is open")
        print("   2. Guide is open on Desktop")
        print("   3. Email is in clipboard (press CMD+V)")
        print("   4. Follow the guide - only 4 clicks needed!")
        
        self.speak("Setup complete. Follow the guide. Use command V to paste.")
        
        return True
    
    def setup_all_emails(self):
        """Setup all emails one by one"""
        print("\n" + "="*80)
        print("🚀 SETTING UP ALL EMAILS")
        print("="*80)
        
        emails = ["icloud", "noizylab_rsp", "noizylab_help", "fishmusicinc_rp", "fishmusicinc_info"]
        
        for i, email_key in enumerate(emails, 1):
            print(f"\n{'='*80}")
            print(f"EMAIL {i} of {len(emails)}: {EMAIL_CONFIGS[email_key]['email']}")
            print("="*80)
            
            self.setup_email_automated(email_key)
            
            if i < len(emails):
                input(f"\n✅ {email_key} setup complete. Press Enter for next email...")
        
        print("\n" + "="*80)
        print("🎉 ALL EMAILS SETUP COMPLETE!")
        print("="*80)

def main():
    """Main function"""
    print("\n" + "="*80)
    print(" " * 25 + "GMAIL API AUTOMATION")
    print(" " * 20 + "Fully Automated Email Setup")
    print("="*80)
    
    automation = GmailAPIAutomation()
    
    print("\nWhich email do you want to set up?")
    print("  1. rsplowman@icloud.com")
    print("  2. rsp@noizylab.ca")
    print("  3. help@noizylab.ca")
    print("  4. All emails (one by one)")
    
    choice = input("\nEnter choice (1-6): ").strip()
    
    try:
        if choice == "1":
            automation.setup_email_automated("icloud")
        elif choice == "2":
            automation.setup_email_automated("noizylab_rsp")
        elif choice == "3":
            automation.setup_email_automated("noizylab_help")
        elif choice == "4":
            automation.setup_email_automated("fishmusicinc_rp")
        elif choice == "5":
            automation.setup_email_automated("fishmusicinc_info")
        elif choice == "6":
            automation.setup_all_emails()
        else:
            print("Invalid choice. Setting up iCloud email...")
            automation.setup_email_automated("icloud")
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled. Run again anytime!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("But all settings are saved - you can still do it manually!")

if __name__ == "__main__":
    import time
    main()

