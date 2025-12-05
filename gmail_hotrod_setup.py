#!/usr/bin/env python3
from pathlib import Path
import json
import webbrowser

#!/usr/bin/env python3
"""
Gmail HOT ROD Setup Wizard
Helps you configure rsplowman@gmail.com for maximum performance
"""


class GmailHotRodSetup:
    """Gmail Hot Rod Setup Wizard"""

    def __init__(self):
        self.gmail = "rsplowman@gmail.com"
        self.accounts = [
            "rp@fishmusicinc.com",
            "info@fishmusicinc.com",
            "rsp@noizylab.ca",
            "help@noizylab.ca",
            "hello@noizylab.ca",
            "rsplowman@icloud.com"
        ]
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "gmail_hotrod_config.json"
        self.load_config()

    def load_config(self):
        """Load configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "gmail": self.gmail,
                "accounts_added": [],
                "labels_created": [],
                "filters_created": [],
                "features_enabled": {
                    "keyboard_shortcuts": False,
                    "smart_compose": False,
                    "undo_send": False,
                    "multiple_inboxes": False,
                    "two_factor": False
                },
                "setup_complete": False
            }

    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def main_menu(self):
        """Main menu"""
        while True:
            print("\n" + "="*70)
            print("🔥 GMAIL HOT ROD SETUP WIZARD")
            print("="*70)
            print(f"\nYour Gmail: {self.gmail}")
            print("\n📋 Setup Phases:")
            print("  1. 🔗 Open Gmail Settings (Add Accounts)")
            print("  2. 📧 Add Email Accounts to Gmail")
            print("  3. 🏷️  Create Labels & Filters")
            print("  4. ⚡ Enable Power Features")
            print("  5. 🔒 Security Setup (2FA)")
            print("  6. 📊 View Setup Progress")
            print("  7. 🚀 Complete Setup Guide")
            print("  0. Exit")
            print("="*70)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.open_gmail_settings()
            elif choice == "2":
                self.add_accounts_guide()
            elif choice == "3":
                self.labels_filters_guide()
            elif choice == "4":
                self.power_features_guide()
            elif choice == "5":
                self.security_setup()
            elif choice == "6":
                self.view_progress()
            elif choice == "7":
                self.complete_guide()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def open_gmail_settings(self):
        """Open Gmail settings in browser"""
        print("\n" + "="*70)
        print("🔗 OPENING GMAIL SETTINGS")
        print("="*70)

        url = "https://mail.google.com/mail/u/0/#settings/accounts"
        print(f"\nOpening: {url}")
        print("\nMake sure you're signed in as:", self.gmail)

        open_browser = input("\nOpen in browser? (y/n): ").strip().lower()
        if open_browser == 'y':
            webbrowser.open(url)
            print("✅ Browser opened!")

        print("\n" + "="*70)
        print("WHAT TO DO:")
        print("="*70)
        print("1. Scroll to 'Check mail from other accounts'")
        print("2. Click 'Add a mail account'")
        print("3. Follow the prompts to add each account")

    def add_accounts_guide(self):
        """Guide for adding accounts"""
        print("\n" + "="*70)
        print("📧 ADD EMAIL ACCOUNTS TO GMAIL")
        print("="*70)

        print(f"\nAdding accounts to: {self.gmail}")
        print("\nAccounts to add:")
        for i, account in enumerate(self.accounts, 1):
            status = "✅" if account in self.config["accounts_added"] else "⏳"
            print(f"  {status} {i}. {account}")

        print("\n" + "="*70)
        print("SERVER SETTINGS:")
        print("="*70)

        print("\n📧 fishmusicinc.com emails:")
        print("   POP Server: mail.fishmusicinc.com")
        print("   Port: 995 (SSL)")
        print("   Username: Full email address")

        print("\n📧 noizylab.ca emails:")
        print("   POP Server: mail.noizylab.ca")
        print("   Port: 995 (SSL)")
        print("   Username: Full email address")

        print("\n📧 rsplowman@icloud.com:")
        print("   POP Server: pop.mail.me.com")
        print("   Port: 995 (SSL)")
        print("   Username: rsplowman@icloud.com")

        print("\n" + "="*70)
        print("SETUP STEPS:")
        print("="*70)
        print("1. Go to: https://mail.google.com/mail/u/0/#settings/accounts")
        print("2. Under 'Check mail from other accounts' → 'Add a mail account'")
        print("3. Enter email address")
        print("4. Enter server settings above")
        print("5. ✅ Check 'Leave a copy on server'")
        print("6. Create a label (e.g., 'fishmusicinc.com')")
        print("7. ✅ Check 'Always use SSL'")
        print("8. Repeat for all 6 accounts")

        print("\n" + "="*70)
        print("SEND MAIL AS:")
        print("="*70)
        print("1. Under 'Send mail as' → 'Add another email address'")
        print("2. Add all 6 email addresses")
        print("3. Verify each one")
        print("4. Set default address")

        # Track progress
        for account in self.accounts:
            if account not in self.config["accounts_added"]:
                added = input(f"\nHave you added {account}? (y/n): ").strip().lower()
                if added == 'y':
                    self.config["accounts_added"].append(account)
                    self.save_config()
                    print(f"✅ {account} marked as added!")

    def labels_filters_guide(self):
        """Guide for labels and filters"""
        print("\n" + "="*70)
        print("🏷️  CREATE LABELS & FILTERS")
        print("="*70)

        url_labels = "https://mail.google.com/mail/u/0/#settings/labels"
        url_filters = "https://mail.google.com/mail/u/0/#settings/filters"

        print("\n📋 CREATE LABELS:")
        print(f"   Link: {url_labels}")
        print("\n   Create these labels:")
        print("   • fishmusicinc.com")
        print("   • noizylab.ca")
        print("   • iCloud")
        print("   • Priority")
        print("   • To Do")
        print("   • Attachments")
        print("   • Notifications")

        print("\n🔍 CREATE FILTERS:")
        print(f"   Link: {url_filters}")
        print("\n   Filter 1: Auto-Label fishmusicinc.com")
        print("   • From: rp@fishmusicinc.com OR info@fishmusicinc.com")
        print("   • Actions: Apply label 'fishmusicinc.com', Never spam, Mark important")

        print("\n   Filter 2: Auto-Label noizylab.ca")
        print("   • From: rsp@noizylab.ca OR help@noizylab.ca OR hello@noizylab.ca")
        print("   • Actions: Apply label 'noizylab.ca', Never spam, Mark important")

        print("\n   Filter 3: Auto-Label iCloud")
        print("   • From: rsplowman@icloud.com")
        print("   • Actions: Apply label 'iCloud', Never spam")

        print("\n   Filter 4: Priority Keywords")
        print("   • Has words: urgent, important, asap, priority, action required")
        print("   • Actions: Apply label 'Priority', Star it, Never spam")

        print("\n   Filter 5: Attachments")
        print("   • Has attachment: yes")
        print("   • Actions: Apply label 'Attachments', Star it")

        print("\n   Filter 6: Notifications")
        print("   • From contains: notification OR alert OR noreply")
        print("   • Actions: Apply label 'Notifications', Skip inbox, Never spam")

        open_browser = input("\nOpen labels page? (y/n): ").strip().lower()
        if open_browser == 'y':
            webbrowser.open(url_labels)
            print("✅ Opened labels page!")

    def power_features_guide(self):
        """Guide for power features"""
        print("\n" + "="*70)
        print("⚡ ENABLE POWER FEATURES")
        print("="*70)

        url_general = "https://mail.google.com/mail/u/0/#settings/general"
        url_inbox = "https://mail.google.com/mail/u/0/#settings/inbox"

        print("\n✅ FEATURES TO ENABLE:")
        print("="*70)

        print("\n1. Keyboard Shortcuts")
        print(f"   Link: {url_general}")
        print("   • Scroll to 'Keyboard shortcuts'")
        print("   • ✅ Turn on keyboard shortcuts")

        print("\n2. Smart Compose & Smart Reply")
        print(f"   Link: {url_general}")
        print("   • ✅ Enable Smart Compose")
        print("   • ✅ Enable Smart Reply")

        print("\n3. Undo Send")
        print(f"   Link: {url_general}")
        print("   • ✅ Enable Undo Send")
        print("   • Set cancel period: 30 seconds")

        print("\n4. Multiple Inboxes")
        print(f"   Link: {url_inbox}")
        print("   • Enable 'Multiple Inboxes'")
        print("   • Create sections: Priority, Unread, Today")

        print("\n5. Stars")
        print(f"   Link: {url_general}")
        print("   • Enable all star types (6 colors)")

        print("\n6. Importance Markers")
        print(f"   Link: {url_inbox}")
        print("   • ✅ Show importance markers")

        open_browser = input("\nOpen general settings? (y/n): ").strip().lower()
        if open_browser == 'y':
            webbrowser.open(url_general)
            print("✅ Opened settings!")

    def security_setup(self):
        """Security setup guide"""
        print("\n" + "="*70)
        print("🔒 SECURITY SETUP")
        print("="*70)

        url_security = "https://myaccount.google.com/security"

        print("\n1. Enable 2-Step Verification")
        print(f"   Link: {url_security}")
        print("   • Go to Security settings")
        print("   • ✅ Enable 2-Step Verification")
        print("   • Generate app passwords for email clients")

        print("\n2. Review Account Activity")
        print(f"   Link: {url_security}")
        print("   • Check 'Recent security activity'")
        print("   • Review 'Your devices'")

        print("\n3. App-Specific Passwords")
        print("   • Generate passwords for:")
        print("     - Mac Mail")
        print("     - Other email clients")
        print("     - Gmail POP3 access")

        if not self.config["features_enabled"]["two_factor"]:
            enabled = input("\nHave you enabled 2-Step Verification? (y/n): ").strip().lower()
            if enabled == 'y':
                self.config["features_enabled"]["two_factor"] = True
                self.save_config()
                print("✅ 2FA marked as enabled!")

        open_browser = input("\nOpen security settings? (y/n): ").strip().lower()
        if open_browser == 'y':
            webbrowser.open(url_security)
            print("✅ Opened security page!")

    def view_progress(self):
        """View setup progress"""
        print("\n" + "="*70)
        print("📊 SETUP PROGRESS")
        print("="*70)

        total_accounts = len(self.accounts)
        added_accounts = len(self.config["accounts_added"])

        print(f"\n📧 Email Accounts: {added_accounts}/{total_accounts}")
        for account in self.accounts:
            status = "✅" if account in self.config["accounts_added"] else "⏳"
            print(f"   {status} {account}")

        print(f"\n🏷️  Labels Created: {len(self.config['labels_created'])}")
        print(f"🔍 Filters Created: {len(self.config['filters_created'])}")

        print("\n⚡ Features Enabled:")
        features = self.config["features_enabled"]
        for feature, enabled in features.items():
            status = "✅" if enabled else "⏳"
            print(f"   {status} {feature.replace('_', ' ').title()}")

        completion = (added_accounts / total_accounts) * 100
        print(f"\n📈 Overall Progress: {completion:.0f}%")

        if completion == 100:
            print("\n🎉 All accounts added! Continue with labels, filters, and features.")

    def complete_guide(self):
        """Show complete setup guide"""
        print("\n" + "="*70)
        print("🚀 COMPLETE HOT ROD SETUP GUIDE")
        print("="*70)

        print("\n📖 See the complete guide:")
        print("   GMAIL_HOT_ROD_SETUP.md")

        print("\n🔗 Quick Links:")
        print("   • Accounts: https://mail.google.com/mail/u/0/#settings/accounts")
        print("   • Labels: https://mail.google.com/mail/u/0/#settings/labels")
        print("   • Filters: https://mail.google.com/mail/u/0/#settings/filters")
        print("   • General: https://mail.google.com/mail/u/0/#settings/general")
        print("   • Security: https://myaccount.google.com/security")

        print("\n✅ Setup Checklist:")
        print("   1. Add all 6 email accounts")
        print("   2. Set up 'Send mail as' for all")
        print("   3. Create labels")
        print("   4. Create filters")
        print("   5. Enable keyboard shortcuts")
        print("   6. Enable Smart Compose")
        print("   7. Enable Undo Send")
        print("   8. Enable 2-Step Verification")
        print("   9. Set up multiple inboxes")
        print("   10. Enable all star types")

        print("\n🎯 Result: Maximum performance Gmail setup!")

if __name__ == "__main__":
    try:
        wizard = GmailHotRodSetup()
            wizard.main_menu()


    except Exception as e:
        print(f"Error: {e}")
