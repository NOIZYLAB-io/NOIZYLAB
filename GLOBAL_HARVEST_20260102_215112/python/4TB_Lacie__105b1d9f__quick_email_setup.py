#!/usr/bin/env python3
from pathlib import Path
import json

#!/usr/bin/env python3
"""
Quick Email Setup Wizard for All Your Accounts
Handles: Gmail, iCloud, noizylab.ca, and fishmusicinc.com
Complete Email List:
- rp@fishmusicinc.com
- info@fishmusicinc.com
- rsp@noizylab.ca
- help@noizylab.ca
- hello@noizylab.ca
"""


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
                "verification_emails": [],
                "domains": {
                    "fishmusicinc.com": {
                        "emails": ["rp@fishmusicinc.com", "info@fishmusicinc.com"]
                    },
                    "noizylab.ca": {
                        "emails": ["rsp@noizylab.ca", "help@noizylab.ca", "hello@noizylab.ca"]
                    }
                }
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
            print("  1. Gmail → Mac Mail Setup")
            print("  2. rsplowman@icloud.com → Add to Gmail Account")
            print("\n  📧 fishmusicinc.com:")
            print("  3. rp@fishmusicinc.com → Setup")
            print("  4. info@fishmusicinc.com → Setup")
            print("\n  📧 noizylab.ca:")
            print("  5. rsp@noizylab.ca → Setup")
            print("  6. help@noizylab.ca → Setup")
            print("  7. hello@noizylab.ca → Setup")
            print("\n  📬 Verification Emails:")
            print("  8. Check Verification Emails (fishmusicinc.com)")
            print("\n  📋 Other:")
            print("  9. View All Saved Configurations")
            print("  10. Complete Setup (All Accounts)")
            print("  0. Exit")
            print("="*70)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.gmail_macmail()
            elif choice == "2":
                self.add_icloud_to_gmail()
            elif choice == "3":
                self.setup_fishmusicinc("rp@fishmusicinc.com")
            elif choice == "4":
                self.setup_fishmusicinc("info@fishmusicinc.com")
            elif choice == "5":
                self.setup_noizylab("rsp@noizylab.ca")
            elif choice == "6":
                self.setup_noizylab("help@noizylab.ca")
            elif choice == "7":
                self.setup_noizylab("hello@noizylab.ca")
            elif choice == "8":
                self.check_verification_emails()
            elif choice == "9":
                self.view_configs()
            elif choice == "10":
                self.complete_setup()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

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

    def setup_fishmusicinc(self, email):
        """Setup fishmusicinc.com email"""
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
            print("   IMAP Server: mail.fishmusicinc.com (or imap.fishmusicinc.com)")
            print("   IMAP Port: 993 (SSL/TLS)")
            print("   SMTP Server: mail.fishmusicinc.com (or smtp.fishmusicinc.com)")
            print("   SMTP Port: 587 (STARTTLS)")
            print("   Username: " + email)
            print("   Password: [Your email password]")

            default_server = "mail.fishmusicinc.com"
            imap_prompt = f"\nEnter IMAP server (default: {default_server}): "
            imap_server = input(imap_prompt).strip() or default_server
            smtp_prompt = f"Enter SMTP server (default: {default_server}): "
            smtp_server = input(smtp_prompt).strip() or default_server

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
        print("📧 CHECK VERIFICATION EMAILS - fishmusicinc.com")
        print("="*70)

        print("\nWHERE TO CHECK:")
        print("-" * 70)
        print("1. Mac Mail App:")
        print("   • Open Mail app")
        print("   • Select rp@fishmusicinc.com or info@fishmusicinc.com account in sidebar")
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
        for email in ["rp@fishmusicinc.com", "info@fishmusicinc.com"]:
            self.config["verification_emails"].append({
                "email": email,
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
        print("📋 ALL DOMAINS & EMAILS:")
        print("="*70)
        print("\n🌐 fishmusicinc.com:")
        print("   • rp@fishmusicinc.com")
        print("   • info@fishmusicinc.com")
        print("\n🌐 noizylab.ca:")
        print("   • rsp@noizylab.ca")
        print("   • help@noizylab.ca")
        print("   • hello@noizylab.ca")

        print("\n" + "="*70)

    def complete_setup(self):
        """Complete setup wizard for all accounts"""
        print("\n" + "="*70)
        print("🚀 COMPLETE EMAIL SETUP WIZARD")
        print("="*70)
        print("\nThis will guide you through setting up all your email accounts.")
        print("\n📧 All Email Accounts:")
        print("   • rp@fishmusicinc.com")
        print("   • info@fishmusicinc.com")
        print("   • rsp@noizylab.ca")
        print("   • help@noizylab.ca")
        print("   • hello@noizylab.ca")

        input("\nPress Enter to start...")

        # 1. Gmail in Mac Mail
        print("\n" + "="*70)
        print("STEP 1: Gmail in Mac Mail")
        print("="*70)
        self.gmail_macmail()

        # 2. Add iCloud to Gmail
        print("\n" + "="*70)
        print("STEP 2: Add rsplowman@icloud.com to Gmail")
        print("="*70)
        self.add_icloud_to_gmail()

        # 3. Setup fishmusicinc.com emails
        print("\n" + "="*70)
        print("STEP 3: Setup rp@fishmusicinc.com")
        print("="*70)
        self.setup_fishmusicinc("rp@fishmusicinc.com")

        print("\n" + "="*70)
        print("STEP 4: Setup info@fishmusicinc.com")
        print("="*70)
        self.setup_fishmusicinc("info@fishmusicinc.com")

        # 4. Setup noizylab.ca emails
        print("\n" + "="*70)
        print("STEP 5: Setup rsp@noizylab.ca")
        print("="*70)
        self.setup_noizylab("rsp@noizylab.ca")

        print("\n" + "="*70)
        print("STEP 6: Setup help@noizylab.ca")
        print("="*70)
        self.setup_noizylab("help@noizylab.ca")

        print("\n" + "="*70)
        print("STEP 7: Setup hello@noizylab.ca")
        print("="*70)
        self.setup_noizylab("hello@noizylab.ca")

        # 5. Check verification emails
        print("\n" + "="*70)
        print("STEP 8: Check Verification Emails")
        print("="*70)
        self.check_verification_emails()

        print("\n" + "="*70)
        print("✅ COMPLETE SETUP FINISHED!")
        print("="*70)
        print("\nAll configurations have been saved.")
        print("You can view them anytime using option 9 in the main menu.")
        print("\n" + "="*70)

if __name__ == "__main__":
    try:
        wizard = QuickEmailSetup()
            wizard.main_menu()


    except Exception as e:
        print(f"Error: {e}")
