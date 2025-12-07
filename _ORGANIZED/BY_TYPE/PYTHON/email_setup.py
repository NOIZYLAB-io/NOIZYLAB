#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Email Setup Module for IT Genius
Handles Gmail, iCloud, and custom domain email configurations
"""

import json
from typing import Dict, Optional

class EmailSetup:
    """Email account configuration wizard"""
    
    # Email provider configurations
    PROVIDERS = {
        "gmail": {
            "imap_server": "imap.gmail.com",
            "imap_port": 993,
            "imap_security": "SSL/TLS",
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "smtp_security": "STARTTLS",
            "note": "Requires app-specific password if 2FA is enabled"
        },
        "icloud": {
            "imap_server": "imap.mail.me.com",
            "imap_port": 993,
            "imap_security": "SSL/TLS",
            "smtp_server": "smtp.mail.me.com",
            "smtp_port": 587,
            "smtp_security": "STARTTLS",
            "note": "Requires app-specific password from appleid.apple.com"
        },
        "outlook": {
            "imap_server": "outlook.office365.com",
            "imap_port": 993,
            "imap_security": "SSL/TLS",
            "smtp_server": "smtp.office365.com",
            "smtp_port": 587,
            "smtp_security": "STARTTLS",
            "note": "Use your Microsoft 365 credentials"
        },
        "yahoo": {
            "imap_server": "imap.mail.yahoo.com",
            "imap_port": 993,
            "imap_security": "SSL/TLS",
            "smtp_server": "smtp.mail.yahoo.com",
            "smtp_port": 587,
            "smtp_security": "STARTTLS",
            "note": "Requires app-specific password"
        },
        "custom": {
            "imap_server": "",
            "imap_port": 993,
            "imap_security": "SSL/TLS",
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_security": "STARTTLS",
            "note": "Custom configuration"
        }
    }
    
    def __init__(self, config: Dict):
        self.config = config
        if "saved_emails" not in self.config:
            self.config["saved_emails"] = {}
    
    def display_menu(self):
        """Display email setup menu"""
        print("\n" + "="*70)
        print("EMAIL ACCOUNT SETUP")
        print("="*70)
        print("1. Setup Gmail Account")
        print("2. Setup iCloud Account")
        print("3. Setup Outlook/Office 365 Account")
        print("4. Setup Yahoo Account")
        print("5. Setup Custom Domain Email")
        print("6. View Saved Email Configurations")
        print("7. Generate Configuration for Gmail Integration")
        print("8. Gmail in Mac Mail - Step-by-Step Guide")
        print("9. Add Alternate Email to Gmail Account")
        print("0. Back to Main Menu")
        print("="*70)
    
    def detect_provider(self, email: str) -> Optional[str]:
        """Detect email provider from email address"""
        email_lower = email.lower()
        if "@gmail.com" in email_lower:
            return "gmail"
        elif "@icloud.com" in email_lower or "@me.com" in email_lower or "@mac.com" in email_lower:
            return "icloud"
        elif "@outlook.com" in email_lower or "@hotmail.com" in email_lower or "@live.com" in email_lower:
            return "outlook"
        elif "@yahoo.com" in email_lower or "@ymail.com" in email_lower:
            return "yahoo"
        else:
            return "custom"
    
    def setup_email(self, provider: str, email: str = None):
        """Setup email account"""
        if not email:
            email = input(f"\nEnter your {provider} email address: ").strip()
        
        if not email or "@" not in email:
            print("❌ Invalid email address")
            return
        
        # Auto-detect provider if not specified
        if provider == "auto":
            provider = self.detect_provider(email)
            print(f"Detected provider: {provider}")
        
        if provider not in self.PROVIDERS:
            print(f"❌ Unknown provider: {provider}")
            return
        
        provider_config = self.PROVIDERS[provider].copy()
        
        # For custom domains, ask for server details
        if provider == "custom":
            print("\nEnter custom email server settings:")
            provider_config["imap_server"] = input("IMAP Server (e.g., mail.yourdomain.com): ").strip()
            provider_config["smtp_server"] = input("SMTP Server (e.g., mail.yourdomain.com): ").strip()
            
            imap_port = input("IMAP Port (default 993): ").strip()
            if imap_port:
                provider_config["imap_port"] = int(imap_port)
            
            smtp_port = input("SMTP Port (default 587): ").strip()
            if smtp_port:
                provider_config["smtp_port"] = int(smtp_port)
        
        # Display configuration
        print("\n" + "="*70)
        print(f"EMAIL CONFIGURATION FOR: {email}")
        print("="*70)
        print("\n📥 INCOMING MAIL (IMAP) SETTINGS:")
        print(f"  Server:     {provider_config['imap_server']}")
        print(f"  Port:       {provider_config['imap_port']}")
        print(f"  Security:   {provider_config['imap_security']}")
        print(f"  Username:   {email}")
        print(f"  Password:   [Your email password or app-specific password]")
        
        print("\n📤 OUTGOING MAIL (SMTP) SETTINGS:")
        print(f"  Server:     {provider_config['smtp_server']}")
        print(f"  Port:       {provider_config['smtp_port']}")
        print(f"  Security:   {provider_config['smtp_security']}")
        print(f"  Username:   {email}")
        print(f"  Password:   [Your email password or app-specific password]")
        
        if provider_config.get("note"):
            print(f"\n⚠️  Note: {provider_config['note']}")
        
        print("\n" + "="*70)
        
        # Save configuration
        save = input("\nSave this configuration? (y/n): ").strip().lower()
        if save == 'y':
            self.config["saved_emails"][email] = {
                "provider": provider,
                **provider_config
            }
            print(f"✅ Configuration saved for {email}")
        
        # Show Gmail integration steps
        if provider != "gmail":
            show_gmail = input("\nShow Gmail integration steps? (y/n): ").strip().lower()
            if show_gmail == 'y':
                self.show_gmail_integration(email, provider_config)
    
    def show_gmail_integration(self, email: str, config: Dict):
        """Show steps to integrate email with Gmail"""
        print("\n" + "="*70)
        print("GMAIL INTEGRATION STEPS")
        print("="*70)
        print("\n1. Open Gmail → Settings (gear icon) → See all settings")
        print("2. Go to 'Accounts and Import' tab")
        print("\n3. To RECEIVE emails:")
        print("   → Under 'Check mail from other accounts', click 'Add a mail account'")
        print(f"   → Enter: {email}")
        print("   → Choose 'Link accounts with Gmailify (IMAP)'")
        print(f"   → IMAP Server: {config['imap_server']}")
        print(f"   → Port: {config['imap_port']}")
        print(f"   → Security: {config['imap_security']}")
        print(f"   → Username: {email}")
        print("   → Password: [Your email password]")
        
        print("\n4. To SEND emails:")
        print("   → Under 'Send mail as', click 'Add another email address'")
        print(f"   → Enter: {email}")
        print(f"   → SMTP Server: {config['smtp_server']}")
        print(f"   → Port: {config['smtp_port']}")
        print(f"   → Security: {config['smtp_security']}")
        print(f"   → Username: {email}")
        print("   → Password: [Your email password]")
        print("   → Verify the email when Gmail sends confirmation")
        
        print("\n" + "="*70)
    
    def view_saved_emails(self):
        """View all saved email configurations"""
        print("\n" + "="*70)
        print("SAVED EMAIL CONFIGURATIONS")
        print("="*70)
        
        if not self.config["saved_emails"]:
            print("\nNo saved email configurations.")
        else:
            for email, settings in self.config["saved_emails"].items():
                print(f"\n📧 {email}")
                print(f"   Provider: {settings.get('provider', 'Unknown')}")
                print(f"   IMAP: {settings.get('imap_server')}:{settings.get('imap_port')}")
                print(f"   SMTP: {settings.get('smtp_server')}:{settings.get('smtp_port')}")
        
        print("\n" + "="*70)
        input("\nPress Enter to continue...")
    
    def gmail_integration_wizard(self):
        """Special wizard for setting up custom email in Gmail"""
        print("\n" + "="*70)
        print("GMAIL INTEGRATION WIZARD")
        print("="*70)
        print("\nThis wizard helps you add an external email account to Gmail.")
        
        email = input("\nEnter the email address to add to Gmail: ").strip()
        if not email or "@" not in email:
            print("❌ Invalid email address")
            return
        
        provider = self.detect_provider(email)
        if provider == "custom":
            print("\nCustom domain detected. Please provide server details:")
            self.setup_email("custom", email)
        else:
            print(f"\nDetected provider: {provider}")
            self.setup_email(provider, email)
    
    def macmail_gmail_setup(self):
        """Step-by-step guide for adding Gmail to Mac Mail"""
        print("\n" + "="*70)
        print("GMAIL IN MAC MAIL - STEP-BY-STEP GUIDE")
        print("="*70)
        
        print("\n📋 Prerequisites:")
        print("   1. Gmail account with IMAP enabled")
        print("   2. App-specific password (if 2FA is enabled)")
        
        print("\n" + "="*70)
        print("STEP 1: Enable IMAP in Gmail")
        print("="*70)
        print("\n1. Go to: https://mail.google.com/mail/u/0/#settings/general")
        print("2. Click 'See all settings'")
        print("3. Go to 'Forwarding and POP/IMAP' tab")
        print("4. Under 'IMAP access', select 'Enable IMAP'")
        print("5. Click 'Save Changes'")
        
        input("\nPress Enter when IMAP is enabled...")
        
        print("\n" + "="*70)
        print("STEP 2: Generate App-Specific Password (if 2FA enabled)")
        print("="*70)
        has_2fa = input("\nDo you have 2-Factor Authentication enabled? (y/n): ").strip().lower()
        
        if has_2fa == 'y':
            print("\n1. Go to: https://myaccount.google.com/")
            print("2. Click 'Security' in left sidebar")
            print("3. Under 'How you sign in to Google', find 'App passwords'")
            print("4. Click 'App passwords'")
            print("5. Select 'Mail' as the app")
            print("6. Select 'Mac' as the device")
            print("7. Click 'Generate'")
            print("8. Copy the 16-character password")
            print("\n⚠️  You'll need this password in the next step!")
            input("\nPress Enter when you have the app password...")
        
        print("\n" + "="*70)
        print("STEP 3: Add Gmail to Mac Mail")
        print("="*70)
        print("\n1. Open Mail app on your Mac")
        print("2. Go to Mail → Settings (or Mail → Preferences)")
        print("3. Click the 'Accounts' tab")
        print("4. Click the '+' button at bottom left")
        print("5. Select 'Google' from account type list")
        print("6. Enter your Gmail address")
        print("7. Enter your Gmail password" + (" or app-specific password" if has_2fa == 'y' else ""))
        print("8. Select what to sync (Mail, Contacts, Calendars, Notes)")
        print("9. Click 'Done'")
        
        print("\n" + "="*70)
        print("MANUAL SETUP (if automatic doesn't work)")
        print("="*70)
        print("\nIf automatic setup fails, use these manual settings:")
        print("\n📥 Incoming Mail Server (IMAP):")
        print("   Server:     imap.gmail.com")
        print("   Port:       993")
        print("   Security:   SSL/TLS")
        print("   Username:   yourname@gmail.com")
        print("   Password:   [Your Gmail password or app password]")
        
        print("\n📤 Outgoing Mail Server (SMTP):")
        print("   Server:     smtp.gmail.com")
        print("   Port:       587")
        print("   Security:   STARTTLS")
        print("   Username:   yourname@gmail.com")
        print("   Password:   [Your Gmail password or app password]")
        
        print("\n" + "="*70)
        print("VERIFICATION")
        print("="*70)
        print("\n✅ Check that:")
        print("   • Gmail folders appear in Mail sidebar")
        print("   • You can send test emails")
        print("   • New emails sync automatically")
        
        print("\n" + "="*70)
    
    def add_alternate_email_guide(self):
        """Guide for adding alternate email to Gmail account"""
        print("\n" + "="*70)
        print("ADD ALTERNATE EMAIL TO GMAIL ACCOUNT")
        print("="*70)
        print("\nThis allows you to use your iCloud email (or other email)")
        print("when apps ask you to 'Sign in with Google' or use Gmail login.")
        
        email = input("\nEnter the email to add (e.g., rsplowman@icloud.com): ").strip()
        if not email or "@" not in email:
            print("❌ Invalid email address")
            return
        
        print("\n" + "="*70)
        print("STEP-BY-STEP INSTRUCTIONS")
        print("="*70)
        
        print("\n📧 Adding", email, "as Alternate Email:")
        print("\n1. Go to: https://myaccount.google.com/")
        print("2. Click 'Personal info' in the left sidebar")
        print("3. Under 'Contact info', find 'Email'")
        print("4. Click on 'Email'")
        print("5. Click 'Add alternate email' or 'Add email address'")
        print(f"6. Enter: {email}")
        print("7. Click 'Add'")
        print(f"8. Check {email} for a verification email from Google")
        print("9. Click the verification link in the email")
        print(f"10. ✅ {email} is now added as an alternate email!")
        
        print("\n" + "="*70)
        print("HOW TO USE FOR APP LOGINS")
        print("="*70)
        print("\nWhen apps ask you to 'Sign in with Google':")
        print(f"1. Click 'Sign in with Google'")
        print(f"2. Enter: {email}")
        print("3. Use your Gmail account password (not iCloud password)")
        print("4. Google will recognize it as an alternate email")
        
        print("\n" + "="*70)
        print("IMPORTANT NOTES")
        print("="*70)
        print("\n⚠️  Important:")
        print("   • The email becomes an alternate email for your Google account")
        print("   • You still use your Gmail account password to sign in")
        print("   • This doesn't forward emails - it's for account identification")
        print("   • Some apps may still show your primary Gmail address")
        
        print("\n" + "="*70)
        print("ALTERNATIVE: Add as Recovery Email")
        print("="*70)
        print("\nIf you prefer to add it as a recovery email instead:")
        print("\n1. Go to: https://myaccount.google.com/")
        print("2. Click 'Security'")
        print("3. Under 'Ways we can verify it's you', find 'Recovery email'")
        print("4. Click 'Recovery email'")
        print(f"5. Add {email}")
        print("6. Verify it via the email sent to your account")
        
        print("\n" + "="*70)
    
    def run(self):
        """Run email setup wizard"""
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.setup_email("gmail")
            elif choice == "2":
                self.setup_email("icloud")
            elif choice == "3":
                self.setup_email("outlook")
            elif choice == "4":
                self.setup_email("yahoo")
            elif choice == "5":
                self.setup_email("custom")
            elif choice == "6":
                self.view_saved_emails()
            elif choice == "7":
                self.gmail_integration_wizard()
            elif choice == "8":
                self.macmail_gmail_setup()
            elif choice == "9":
                self.add_alternate_email_guide()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")

