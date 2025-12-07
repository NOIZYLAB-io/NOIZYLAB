#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick Email Setup Wizard for All Your Accounts
Handles: Gmail, iCloud, noizylab.ca, and fishmusicinc.com
"""

import json
from pathlib import Path

class QuickEmailSetup:
    """Quick setup wizard for all email accounts"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "email_config.json"
        self.load_config()
    
    def load_config(self):
        """Load saved email configurations"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "accounts": {},
                "gmail_alternates": [],
                "verification_emails": []
            }
    
    def save_config(self):
        """Save configurations"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def main_menu(self):
        """Main menu"""
        while True:
            print("\n" + "="*70)
            print("🚀 QUICK EMAIL SETUP WIZARD")
            print("="*70)
            print("\nYour Email Accounts:")
            print("  1. rsplowman@outlook.com → Microsoft 365 Primary Setup")
            print("  2. rsplowman@icloud.com → Add to Services")
            print("  3. rsp@noizylab.ca → Setup")
            print("  4. help@noizylab.ca → Setup")
            print("  5. rp@fishmusicinc.com → Check Verification Emails")
            print("  6. View All Saved Configurations")
            print("  7. Complete Setup (All Accounts)")
            print("  0. Exit")
            print("="*70)
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.m365_setup()
            elif choice == "2":
                self.add_icloud_to_services()
            elif choice == "3":
                self.setup_noizylab("rsp@noizylab.ca")
            elif choice == "4":
                self.setup_noizylab("help@noizylab.ca")
            elif choice == "5":
                self.check_verification_emails()
            elif choice == "6":
                self.view_configs()
            elif choice == "7":
                self.complete_setup()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def m365_setup(self):
        """Microsoft 365 in Email Client setup"""
        print("\n" + "="*70)
        print("📧 MICROSOFT 365 PRIMARY SETUP")
        print("="*70)
        
        print("\nSTEP 1: Configure Microsoft 365")
        print("-" * 70)
        print("1. Open your email client (Outlook, Mail app, etc.)")
        print("2. Go to: Settings → Accounts")
        print("3. Add Account → Microsoft 365")
        print("4. Sign in with rsplowman@outlook.com")
        print("5. Allow access when prompted")
        
        input("\n✅ Press Enter when M365 is configured...")
        
        print("\nSTEP 2: Manual Settings (if auto-config fails)")
        print("-" * 70)
        print("IMAP Server: outlook.office365.com")
        print("IMAP Port: 993 (SSL/TLS)")
        print("SMTP Server: smtp.office365.com")
        print("SMTP Port: 587 (STARTTLS)")
        print("Username: rsplowman@outlook.com")
        print("Password: (Use your M365 Password or App Password)")
        
        print("\nSTEP 3: App-Specific Password (if 2FA enabled)")
        print("-" * 70)
        has_2fa = input("Do you have 2-Factor Authentication? (y/n): ").strip().lower()
        
        if has_2fa == 'y':
            print("\n1. Go to: https://account.microsoft.com/security")
            print("2. Click 'Advanced security options'")
            print("3. Under 'App passwords', generate new password")
            print("4. Use this password in your email client")
            app_pass = input("\nPaste app password (or press Enter to skip): ").strip()
            if app_pass:
                self.config["m365_app_password"] = app_pass
                self.save_config()
        
        m365 = "rsplowman@outlook.com"
        self.config["accounts"]["m365_primary"] = {
            "email": m365,
            "imap": "outlook.office365.com:993",
            "smtp": "smtp.office365.com:587",
            "status": "configured"
        }
        self.save_config()
        print("✅ Microsoft 365 configuration saved!")
        
        print("\n" + "="*70)
    
    def add_icloud_to_services(self):
        """Add iCloud email to various services"""
        print("\n" + "="*70)
        print("📧 ADD rsplowman@icloud.com TO SERVICES")
        print("="*70)
        
        print("\nThis email should be used for:")
        print("- Apple services and iCloud")
        print("- Passkey authentication")
        print("- Apple ecosystem services")
        
        print("\nFor Microsoft services, use: rsplowman@outlook.com")
        print("For general services, choose based on compatibility")
        
        confirm = input("\nHave you set up rsplowman@icloud.com where needed? (y/n): ").strip().lower()
        if confirm == 'y':
            if "rsplowman@icloud.com" not in self.config.get("configured_emails", []):
                if "configured_emails" not in self.config:
                    self.config["configured_emails"] = []
                self.config["configured_emails"].append("rsplowman@icloud.com")
                self.save_config()
            print("✅ Saved to configuration!")
        
        print("\n" + "="*70)
    
    def gmail_macmail(self):
        """Gmail in Mac Mail setup"""
        print("\n" + "="*70)
        print("📧 GMAIL IN MAC MAIL SETUP")
        print("="*70)
        
        print("\nSTEP 1: Enable IMAP in Gmail")
        print("-" * 70)
        print("1. Go to: https://mail.google.com/mail/u/0/#settings/general")
        print("2. Click 'See all settings'")
        print("3. Go to 'Forwarding and POP/IMAP' tab")
        print("4. Enable IMAP")
        print("5. Save Changes")
        
        input("\n✅ Press Enter when IMAP is enabled...")
        
        print("\nSTEP 2: App-Specific Password (if 2FA enabled)")
        print("-" * 70)
        has_2fa = input("Do you have 2-Factor Authentication? (y/n): ").strip().lower()
        
        if has_2fa == 'y':
            print("\n1. Go to: https://myaccount.google.com/security")
            print("2. Click 'App passwords'")
            print("3. Select 'Mail' → 'Mac'")
            print("4. Generate and copy the password")
            app_pass = input("\nPaste app password (or press Enter to skip): ").strip()
            if app_pass:
                self.config["gmail_app_password"] = app_pass
                self.save_config()
        
        print("\nSTEP 3: Add to Mac Mail")
        print("-" * 70)
        print("1. Open Mail app")
        print("2. Mail → Settings → Accounts")
        print("3. Click '+' → Select 'Google'")
        print("4. Enter Gmail address and password")
        print("5. Select what to sync")
        print("6. Done!")
        
        gmail = input("\nEnter your Gmail address: ").strip()
        if gmail:
            self.config["accounts"]["gmail"] = {
                "email": gmail,
                "imap": "imap.gmail.com:993",
                "smtp": "smtp.gmail.com:587",
                "status": "configured"
            }
            self.save_config()
            print("✅ Gmail configuration saved!")
        
        print("\n" + "="*70)
    
    def add_icloud_to_gmail(self):
        """Add iCloud email to Gmail account"""
        print("\n" + "="*70)
        print("📧 ADD rsplowman@icloud.com TO GMAIL")
        print("="*70)
        
        print("\nThis allows you to use rsplowman@icloud.com when")
        print("apps ask you to 'Sign in with Google'")
        
        print("\nSTEP-BY-STEP:")
        print("-" * 70)
        print("1. Go to: https://myaccount.google.com/")
        print("2. Click 'Personal info' → 'Email'")
        print("3. Click 'Add alternate email'")
        print("4. Enter: rsplowman@icloud.com")
        print("5. Click 'Add'")
        print("6. Check rsplowman@icloud.com for verification email")
        print("7. Click verification link")
        print("8. ✅ Done!")
        
        print("\n" + "="*70)
        print("HOW TO USE:")
        print("="*70)
        print("When apps ask 'Sign in with Google':")
        print("  • Enter: rsplowman@icloud.com")
        print("  • Use your Gmail password")
        
        confirm = input("\nHave you added rsplowman@icloud.com? (y/n): ").strip().lower()
        if confirm == 'y':
            if "rsplowman@icloud.com" not in self.config["gmail_alternates"]:
                self.config["gmail_alternates"].append("rsplowman@icloud.com")
                self.save_config()
            print("✅ Saved to configuration!")
        
        print("\n" + "="*70)
    
    def setup_noizylab(self, email):
        """Setup noizylab.ca email"""
        print("\n" + "="*70)
        print(f"📧 SETUP {email}")
        print("="*70)
        
        print("\nFirst, we need to determine your email provider.")
        print("\nCommon options:")
        print("  1. Standard Web Hosting (cPanel)")
        print("  2. Google Workspace")
        print("  3. Microsoft 365")
        print("  4. Zoho Mail")
        print("  5. I know the server settings")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            # Standard web hosting
            print("\n📋 Standard Web Hosting Settings:")
            print("   IMAP Server: mail.noizylab.ca (or imap.noizylab.ca)")
            print("   IMAP Port: 993 (SSL/TLS)")
            print("   SMTP Server: mail.noizylab.ca (or smtp.noizylab.ca)")
            print("   SMTP Port: 587 (STARTTLS)")
            print("   Username: " + email)
            print("   Password: [Your email password]")
            
            imap_server = input("\nEnter IMAP server (default: mail.noizylab.ca): ").strip() or "mail.noizylab.ca"
            smtp_server = input("Enter SMTP server (default: mail.noizylab.ca): ").strip() or "mail.noizylab.ca"
            
        elif choice == "2":
            # Google Workspace
            imap_server = "imap.gmail.com"
            smtp_server = "smtp.gmail.com"
            print(f"\n📋 Google Workspace Settings:")
            print(f"   IMAP: {imap_server}:993")
            print(f"   SMTP: {smtp_server}:587")
            
        elif choice == "3":
            # Microsoft 365
            imap_server = "outlook.office365.com"
            smtp_server = "smtp.office365.com"
            print(f"\n📋 Microsoft 365 Settings:")
            print(f"   IMAP: {imap_server}:993")
            print(f"   SMTP: {smtp_server}:587")
            
        elif choice == "4":
            # Zoho
            imap_server = "imap.zoho.com"
            smtp_server = "smtp.zoho.com"
            print(f"\n📋 Zoho Mail Settings:")
            print(f"   IMAP: {imap_server}:993")
            print(f"   SMTP: {smtp_server}:587")
            
        elif choice == "5":
            # Custom settings
            imap_server = input("Enter IMAP server: ").strip()
            smtp_server = input("Enter SMTP server: ").strip()
        else:
            print("❌ Invalid option")
            return
        
        print("\n" + "="*70)
        print(f"CONFIGURATION FOR {email}")
        print("="*70)
        print(f"\n📥 INCOMING (IMAP):")
        print(f"   Server: {imap_server}")
        print(f"   Port: 993")
        print(f"   Security: SSL/TLS")
        print(f"   Username: {email}")
        
        print(f"\n📤 OUTGOING (SMTP):")
        print(f"   Server: {smtp_server}")
        print(f"   Port: 587")
        print(f"   Security: STARTTLS")
        print(f"   Username: {email}")
        
        print("\n" + "="*70)
        print("ADDING TO MAC MAIL:")
        print("="*70)
        print("1. Mail → Settings → Accounts")
        print("2. Click '+' → 'Other Mail Account'")
        print(f"3. Enter: {email}")
        print("4. If auto-detect fails, click 'Configure Manually'")
        print(f"5. Use the settings above")
        
        save = input(f"\nSave configuration for {email}? (y/n): ").strip().lower()
        if save == 'y':
            self.config["accounts"][email] = {
                "imap_server": imap_server,
                "imap_port": 993,
                "smtp_server": smtp_server,
                "smtp_port": 587,
                "status": "configured"
            }
            self.save_config()
            print("✅ Configuration saved!")
        
        print("\n" + "="*70)
    
    def check_verification_emails(self):
        """Guide for checking verification emails"""
        print("\n" + "="*70)
        print("📧 CHECK VERIFICATION EMAILS - rp@fishmusicinc.com")
        print("="*70)
        
        print("\nWHERE TO CHECK:")
        print("-" * 70)
        print("1. Mac Mail App:")
        print("   • Open Mail app")
        print("   • Select rp@fishmusicinc.com account in sidebar")
        print("   • Check Inbox")
        print("   • Check Spam/Junk folder")
        
        print("\n2. Webmail:")
        print("   • Log into your email provider's webmail")
        print("   • Common URLs:")
        print("     - cPanel: fishmusicinc.com/webmail")
        print("     - Google Workspace: mail.google.com")
        print("     - Microsoft 365: outlook.office365.com")
        
        print("\n3. Search for Verification:")
        print("   • Search for: 'verification' or 'verify'")
        print("   • Look for emails from:")
        print("     - Google (if adding to Gmail)")
        print("     - Microsoft (if Office 365)")
        print("     - Your hosting provider")
        
        print("\n" + "="*70)
        print("WHAT TO LOOK FOR:")
        print("="*70)
        print("• Subject: 'Verify your email' or 'Email verification'")
        print("• From: Google, Microsoft, or hosting provider")
        print("• Usually arrives within 1-5 minutes")
        print("• Contains a verification link or code")
        
        print("\n" + "="*70)
        print("TROUBLESHOOTING:")
        print("="*70)
        print("• Not in inbox? Check Spam/Junk folder")
        print("• Still not found? Check other email folders")
        print("• Request a new verification email if needed")
        print("• Check email provider's status page")
        
        # Save to tracking
        self.config["verification_emails"].append({
            "email": "rp@fishmusicinc.com",
            "checked": False,
            "timestamp": None
        })
        self.save_config()
        
        found = input("\nDid you find the verification email? (y/n): ").strip().lower()
        if found == 'y':
            print("✅ Great! Click the verification link to complete setup.")
        else:
            print("💡 Try checking Spam folder or request a new verification email.")
        
        print("\n" + "="*70)
    
    def view_configs(self):
        """View all saved configurations"""
        print("\n" + "="*70)
        print("📋 SAVED EMAIL CONFIGURATIONS")
        print("="*70)
        
        if self.config.get("accounts"):
            print("\n📧 Email Accounts:")
            for email, settings in self.config["accounts"].items():
                print(f"\n   {email}:")
                print(f"      IMAP: {settings.get('imap_server', 'N/A')}:{settings.get('imap_port', 'N/A')}")
                print(f"      SMTP: {settings.get('smtp_server', 'N/A')}:{settings.get('smtp_port', 'N/A')}")
                print(f"      Status: {settings.get('status', 'Unknown')}")
        else:
            print("\n   No email accounts configured yet.")
        
        if self.config.get("gmail_alternates"):
            print("\n🔗 Gmail Alternate Emails:")
            for email in self.config["gmail_alternates"]:
                print(f"   • {email}")
        
        if self.config.get("verification_emails"):
            print("\n✉️  Verification Emails to Check:")
            for vemail in self.config["verification_emails"]:
                print(f"   • {vemail.get('email', 'Unknown')}")
        
        print("\n" + "="*70)
    
    def complete_setup(self):
        """Complete setup wizard for all accounts"""
        print("\n" + "="*70)
        print("🚀 COMPLETE EMAIL SETUP WIZARD")
        print("="*70)
        print("\nThis will guide you through setting up all your email accounts.")
        
        input("\nPress Enter to start...")
        
        # 1. Microsoft 365 Primary
        print("\n" + "="*70)
        print("STEP 1: Microsoft 365 Primary")
        print("="*70)
        self.m365_setup()
        
        # 2. Add iCloud to services
        print("\n" + "="*70)
        print("STEP 2: Configure rsplowman@icloud.com")
        print("="*70)
        self.add_icloud_to_services()
        
        # 3. Setup noizylab.ca emails
        print("\n" + "="*70)
        print("STEP 3: Setup rsp@noizylab.ca")
        print("="*70)
        self.setup_noizylab("rsp@noizylab.ca")
        
        print("\n" + "="*70)
        print("STEP 4: Setup help@noizylab.ca")
        print("="*70)
        self.setup_noizylab("help@noizylab.ca")
        
        # 4. Check verification emails
        print("\n" + "="*70)
        print("STEP 5: Check Verification Emails")
        print("="*70)
        self.check_verification_emails()
        
        print("\n" + "="*70)
        print("✅ COMPLETE SETUP FINISHED!")
        print("="*70)
        print("\nAll configurations have been saved.")
        print("You can view them anytime using option 6 in the main menu.")
        print("\n" + "="*70)

if __name__ == "__main__":
    wizard = QuickEmailSetup()
    wizard.main_menu()

