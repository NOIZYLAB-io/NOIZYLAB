#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import json
import subprocess
import sys
import webbrowser

#!/usr/bin/env python3
"""
Email Master Control Center
Ultimate email management system for all accounts
"""


class EmailMasterControl:
    """Master control center for all email accounts"""

    def __init__(self):
        self.gmail = "rsplowman@gmail.com"
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "email_master_config.json"
        self.load_config()

    def load_config(self):
        """Load master configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "gmail": self.gmail,
                "domains": {
                    "fishmusicinc.com": {
                        "emails": ["rp@fishmusicinc.com", "info@fishmusicinc.com"],
                        "pop_server": "mail.fishmusicinc.com",
                        "smtp_server": "mail.fishmusicinc.com",
                        "status": "active"
                    },
                    "noizylab.ca": {
                        "emails": ["rsp@noizylab.ca", "help@noizylab.ca", "hello@noizylab.ca"],
                        "pop_server": "mail.noizylab.ca",
                        "smtp_server": "mail.noizylab.ca",
                        "status": "active"
                    },
                    "icloud.com": {
                        "emails": ["rsplowman@icloud.com"],
                        "pop_server": "pop.mail.me.com",
                        "smtp_server": "smtp.mail.me.com",
                        "status": "active"
                    }
                },
                "all_emails": [
                    "rsplowman@gmail.com",
                    "rp@fishmusicinc.com",
                    "info@fishmusicinc.com",
                    "rsp@noizylab.ca",
                    "help@noizylab.ca",
                    "hello@noizylab.ca",
                    "rsplowman@icloud.com"
                ],
                "gmail_setup": {
                    "accounts_added": [],
                    "labels_created": [],
                    "filters_created": [],
                    "features_enabled": {}
                },
                "last_updated": datetime.now().isoformat()
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        self.config["last_updated"] = datetime.now().isoformat()
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def main_menu(self):
        """Main control center menu"""
        while True:
            print("\n" + "="*80)
            print("🚀 EMAIL MASTER CONTROL CENTER")
            print("="*80)
            print(f"\n📧 Main Gmail: {self.gmail}")
            print(f"📊 Total Accounts: {len(self.config['all_emails'])}")
            print(f"🌐 Domains: {len(self.config['domains'])}")

            print("\n" + "="*80)
            print("🔥 QUICK ACTIONS")
            print("="*80)
            print("  1. 🚀 Gmail Hot Rod Setup (Complete)")
            print("  2. 📧 Quick Email Setup Wizard")
            print("  3. 🔗 Open Gmail Settings")
            print("  4. 🏷️  Manage Labels & Filters")
            print("  5. ⚡ Power Features Dashboard")

            print("\n" + "="*80)
            print("📋 ACCOUNT MANAGEMENT")
            print("="*80)
            print("  6. 📊 View All Accounts & Status")
            print("  7. 🔍 Test Email Connections")
            print("  8. 📝 Export Email Configuration")
            print("  9. 🔄 Sync Status Check")

            print("\n" + "="*80)
            print("🛠️  ADVANCED TOOLS")
            print("="*80)
            print("  10. 🤖 Auto-Setup Wizard (All-in-One)")
            print("  11. 📧 Email Templates Manager")
            print("  12. 🔔 Notification Setup")
            print("  13. 📱 Mobile Setup Guide")
            print("  14. 🔒 Security Audit")
            print("  15. 📈 Performance Monitor")

            print("\n" + "="*80)
            print("📚 DOCUMENTATION")
            print("="*80)
            print("  16. 📖 View All Guides")
            print("  17. 🎯 Quick Reference Card")
            print("  18. ❓ Help & Troubleshooting")

            print("\n  0. Exit")
            print("="*80)

            choice = input("\n🎯 Select option: ").strip()

            if choice == "1":
                self.gmail_hotrod_setup()
            elif choice == "2":
                self.quick_email_setup()
            elif choice == "3":
                self.open_gmail_settings()
            elif choice == "4":
                self.manage_labels_filters()
            elif choice == "5":
                self.power_features_dashboard()
            elif choice == "6":
                self.view_all_accounts()
            elif choice == "7":
                self.test_connections()
            elif choice == "8":
                self.export_config()
            elif choice == "9":
                self.sync_status_check()
            elif choice == "10":
                self.auto_setup_wizard()
            elif choice == "11":
                self.email_templates_manager()
            elif choice == "12":
                self.notification_setup()
            elif choice == "13":
                self.mobile_setup_guide()
            elif choice == "14":
                self.security_audit()
            elif choice == "15":
                self.performance_monitor()
            elif choice == "16":
                self.view_all_guides()
            elif choice == "17":
                self.quick_reference_card()
            elif choice == "18":
                self.help_troubleshooting()
            elif choice == "0":
                print("\n👋 Goodbye! Your email setup is ready to go!")
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def gmail_hotrod_setup(self):
        """Launch Gmail Hot Rod Setup"""
        print("\n" + "="*80)
        print("🔥 LAUNCHING GMAIL HOT ROD SETUP")
        print("="*80)
        print("\nStarting Hot Rod Setup Wizard...")
        try:
            subprocess.run([sys.executable, str(Path(__file__).parent / "gmail_hotrod_setup.py")])
        except Exception as e:
            print(f"❌ Error: {e}")
            print("\nOpening guide instead...")
            self.open_guide("GMAIL_HOT_ROD_SETUP.md")

    def quick_email_setup(self):
        """Launch Quick Email Setup"""
        print("\n" + "="*80)
        print("📧 LAUNCHING QUICK EMAIL SETUP")
        print("="*80)
        print("\nStarting Quick Email Setup Wizard...")
        try:
            subprocess.run([sys.executable, str(Path(__file__).parent / "quick_email_setup.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def open_gmail_settings(self):
        """Open Gmail settings with quick links"""
        print("\n" + "="*80)
        print("🔗 GMAIL SETTINGS QUICK LINKS")
        print("="*80)

        links = {
            "1": ("Accounts & Import", "https://mail.google.com/mail/u/0/#settings/accounts"),
            "2": ("Labels", "https://mail.google.com/mail/u/0/#settings/labels"),
            "3": ("Filters", "https://mail.google.com/mail/u/0/#settings/filters"),
            "4": ("General Settings", "https://mail.google.com/mail/u/0/#settings/general"),
            "5": ("Inbox Settings", "https://mail.google.com/mail/u/0/#settings/inbox"),
            "6": ("Forwarding & POP/IMAP", "https://mail.google.com/mail/u/0/#settings/fwdandpop"),
            "7": ("Themes", "https://mail.google.com/mail/u/0/#settings/themes"),
            "8": ("Security", "https://myaccount.google.com/security"),
            "9": ("All Settings", "https://mail.google.com/mail/u/0/#settings/all")
        }

        print("\nQuick Links:")
        for key, (name, url) in links.items():
            print(f"  {key}. {name}")

        choice = input("\nSelect link to open (or 'all' for all): ").strip()

        if choice == "all":
            for name, url in links.values():
                print(f"Opening {name}...")
                webbrowser.open(url)
        elif choice in links:
            name, url = links[choice]
            print(f"\nOpening {name}...")
            webbrowser.open(url)
        else:
            print("❌ Invalid choice")

    def manage_labels_filters(self):
        """Manage labels and filters"""
        print("\n" + "="*80)
        print("🏷️  LABELS & FILTERS MANAGER")
        print("="*80)

        print("\n📋 Recommended Labels:")
        labels = [
            "fishmusicinc.com",
            "noizylab.ca",
            "iCloud",
            "Priority",
            "To Do",
            "Attachments",
            "Notifications",
            "Archived",
            "Waiting For",
            "Follow Up"
        ]

        for i, label in enumerate(labels, 1):
            status = "✅" if label in self.config["gmail_setup"]["labels_created"] else "⏳"
            print(f"  {status} {i}. {label}")

        print("\n🔍 Recommended Filters:")
        filters = [
            "Auto-label fishmusicinc.com emails",
            "Auto-label noizylab.ca emails",
            "Auto-label iCloud emails",
            "Priority keywords (urgent, important)",
            "Emails with attachments",
            "Notification emails (skip inbox)"
        ]

        for i, filter_name in enumerate(filters, 1):
            status = "✅" if filter_name in self.config["gmail_setup"]["filters_created"] else "⏳"
            print(f"  {status} {i}. {filter_name}")

        print("\n🔗 Quick Links:")
        print("  • Labels: https://mail.google.com/mail/u/0/#settings/labels")
        print("  • Filters: https://mail.google.com/mail/u/0/#settings/filters")

        open_labels = input("\nOpen labels page? (y/n): ").strip().lower()
        if open_labels == 'y':
            webbrowser.open("https://mail.google.com/mail/u/0/#settings/labels")

        open_filters = input("Open filters page? (y/n): ").strip().lower()
        if open_filters == 'y':
            webbrowser.open("https://mail.google.com/mail/u/0/#settings/filters")

    def power_features_dashboard(self):
        """Power features dashboard"""
        print("\n" + "="*80)
        print("⚡ POWER FEATURES DASHBOARD")
        print("="*80)

        features = {
            "Keyboard Shortcuts": {
                "enabled": self.config["gmail_setup"]["features_enabled"].get("keyboard_shortcuts", False),
                "link": "https://mail.google.com/mail/u/0/#settings/general",
                "section": "Keyboard shortcuts"
            },
            "Smart Compose": {
                "enabled": self.config["gmail_setup"]["features_enabled"].get("smart_compose", False),
                "link": "https://mail.google.com/mail/u/0/#settings/general",
                "section": "Smart Compose"
            },
            "Undo Send": {
                "enabled": self.config["gmail_setup"]["features_enabled"].get("undo_send", False),
                "link": "https://mail.google.com/mail/u/0/#settings/general",
                "section": "Undo Send"
            },
            "Multiple Inboxes": {
                "enabled": self.config["gmail_setup"]["features_enabled"].get("multiple_inboxes", False),
                "link": "https://mail.google.com/mail/u/0/#settings/inbox",
                "section": "Multiple Inboxes"
            },
            "2-Step Verification": {
                "enabled": self.config["gmail_setup"]["features_enabled"].get("two_factor", False),
                "link": "https://myaccount.google.com/security",
                "section": "2-Step Verification"
            }
        }

        print("\nFeature Status:")
        for feature, info in features.items():
            status = "✅ ENABLED" if info["enabled"] else "⏳ NOT ENABLED"
            print(f"  {status} - {feature}")

        print("\n🔗 Enable Features:")
        for feature, info in features.items():
            if not info["enabled"]:
                enable = input(f"\nEnable {feature}? (y/n): ").strip().lower()
                if enable == 'y':
                    webbrowser.open(info["link"])
                    confirmed = input(f"Have you enabled {feature}? (y/n): ").strip().lower()
                    if confirmed == 'y':
                        self.config["gmail_setup"]["features_enabled"][feature.lower().replace(" ", "_")] = True
                        self.save_config()
                        print(f"✅ {feature} marked as enabled!")

    def view_all_accounts(self):
        """View all accounts and status"""
        print("\n" + "="*80)
        print("📊 ALL ACCOUNTS & STATUS")
        print("="*80)

        print(f"\n📧 Main Gmail Account:")
        print(f"  ✅ {self.gmail} (Central Inbox)")

        print(f"\n🌐 Domain Accounts:")
        for domain, info in self.config["domains"].items():
            print(f"\n  📧 {domain}:")
            print(f"     Status: {info['status']}")
            print(f"     POP Server: {info['pop_server']}")
            print(f"     SMTP Server: {info['smtp_server']}")
            print(f"     Emails:")
            for email in info["emails"]:
                added = "✅" if email in self.config["gmail_setup"]["accounts_added"] else "⏳"
                print(f"       {added} {email}")

        print(f"\n📈 Summary:")
        total = len(self.config["all_emails"])
        added = len(self.config["gmail_setup"]["accounts_added"])
        print(f"  Total Accounts: {total}")
        print(f"  Added to Gmail: {added}")
        print(f"  Progress: {(added/total*100):.0f}%")

    def test_connections(self):
        """Test email connections"""
        print("\n" + "="*80)
        print("🔍 EMAIL CONNECTION TEST")
        print("="*80)

        print("\n⚠️  This feature requires network access and credentials.")
        print("For security, test connections manually in Gmail settings.")

        print("\n🔗 Test in Gmail:")
        print("  1. Go to: https://mail.google.com/mail/u/0/#settings/accounts")
        print("  2. Check each account status")
        print("  3. Look for error messages")
        print("  4. Verify server settings")

        print("\n📋 Server Settings Reference:")
        for domain, info in self.config["domains"].items():
            print(f"\n  {domain}:")
            print(f"    POP: {info['pop_server']}:995")
            print(f"    SMTP: {info['smtp_server']}:587")

    def export_config(self):
        """Export email configuration"""
        print("\n" + "="*80)
        print("📝 EXPORT EMAIL CONFIGURATION")
        print("="*80)

        export_file = self.config_dir / "email_config_export.json"

        export_data = {
            "export_date": datetime.now().isoformat(),
            "gmail": self.gmail,
            "domains": self.config["domains"],
            "all_emails": self.config["all_emails"],
            "server_settings": {
                domain: {
                    "pop": f"{info['pop_server']}:995",
                    "smtp": f"{info['smtp_server']}:587"
                }
                for domain, info in self.config["domains"].items()
            }
        }

        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"\n✅ Configuration exported to:")
        print(f"   {export_file}")
        print(f"\n📋 Exported Data:")
        print(f"   • Gmail: {self.gmail}")
        print(f"   • Domains: {len(self.config['domains'])}")
        print(f"   • Total Emails: {len(self.config['all_emails'])}")
        print(f"   • Server Settings: Included")

    def sync_status_check(self):
        """Check sync status"""
        print("\n" + "="*80)
        print("🔄 SYNC STATUS CHECK")
        print("="*80)

        print("\n📊 Gmail Sync Status:")
        print("  • Check: https://mail.google.com/mail/u/0/#settings/accounts")
        print("  • Look for 'Last checked' timestamps")
        print("  • Verify all accounts are syncing")

        print("\n⏰ Sync Frequency:")
        print("  • Gmail checks every few minutes")
        print("  • You can manually check by refreshing")
        print("  • Check 'Check mail now' option")

        print("\n🔍 Troubleshooting:")
        print("  • If not syncing, check server settings")
        print("  • Verify passwords are correct")
        print("  • Check POP3/IMAP is enabled")
        print("  • Review error messages in Gmail")

    def auto_setup_wizard(self):
        """Auto-setup wizard (all-in-one)"""
        print("\n" + "="*80)
        print("🤖 AUTO-SETUP WIZARD (ALL-IN-ONE)")
        print("="*80)

        print("\nThis wizard will guide you through complete setup:")
        print("  1. Add all email accounts to Gmail")
        print("  2. Create labels")
        print("  3. Create filters")
        print("  4. Enable power features")
        print("  5. Security setup")

        start = input("\nStart auto-setup? (y/n): ").strip().lower()
        if start != 'y':
            return

        # Step 1: Add accounts
        print("\n" + "="*80)
        print("STEP 1: Add Email Accounts")
        print("="*80)
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/accounts")
        input("Press Enter when you've added all accounts...")

        # Step 2: Create labels
        print("\n" + "="*80)
        print("STEP 2: Create Labels")
        print("="*80)
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/labels")
        input("Press Enter when you've created labels...")

        # Step 3: Create filters
        print("\n" + "="*80)
        print("STEP 3: Create Filters")
        print("="*80)
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/filters")
        input("Press Enter when you've created filters...")

        # Step 4: Power features
        print("\n" + "="*80)
        print("STEP 4: Enable Power Features")
        print("="*80)
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/general")
        input("Press Enter when you've enabled features...")

        print("\n✅ Auto-setup complete!")
        print("See GMAIL_HOT_ROD_SETUP.md for detailed instructions.")

    def email_templates_manager(self):
        """Email templates manager"""
        print("\n" + "="*80)
        print("📧 EMAIL TEMPLATES MANAGER")
        print("="*80)

        print("\n💡 Gmail Canned Responses:")
        print("  1. Enable in Labs: https://mail.google.com/mail/u/0/#settings/labs")
        print("  2. Search for 'Canned Responses'")
        print("  3. Enable it")
        print("  4. Create templates for common replies")

        print("\n📋 Suggested Templates:")
        templates = [
            "Quick Reply - Acknowledged",
            "Out of Office",
            "Meeting Confirmation",
            "Follow Up",
            "Thank You",
            "Request for Information"
        ]

        for i, template in enumerate(templates, 1):
            print(f"  {i}. {template}")

        print("\n🔗 Enable Canned Responses:")
        print("  https://mail.google.com/mail/u/0/#settings/labs")

        open_labs = input("\nOpen Labs settings? (y/n): ").strip().lower()
        if open_labs == 'y':
            webbrowser.open("https://mail.google.com/mail/u/0/#settings/labs")

    def notification_setup(self):
        """Notification setup"""
        print("\n" + "="*80)
        print("🔔 NOTIFICATION SETUP")
        print("="*80)

        print("\n📱 Desktop Notifications:")
        print("  • Enable in Gmail Settings → General")
        print("  • Choose: All new mail, Important mail, or None")

        print("\n📧 Email Notifications:")
        print("  • Configure in Gmail Settings → General")
        print("  • Set frequency and importance")

        print("\n🔗 Settings Link:")
        print("  https://mail.google.com/mail/u/0/#settings/general")

        open_settings = input("\nOpen notification settings? (y/n): ").strip().lower()
        if open_settings == 'y':
            webbrowser.open("https://mail.google.com/mail/u/0/#settings/general")

    def mobile_setup_guide(self):
        """Mobile setup guide"""
        print("\n" + "="*80)
        print("📱 MOBILE SETUP GUIDE")
        print("="*80)

        print("\n📲 Gmail Mobile App:")
        print("  1. Download Gmail app (iOS/Android)")
        print("  2. Sign in with: rsplowman@gmail.com")
        print("  3. All accounts will sync automatically")
        print("  4. Enable notifications in app settings")

        print("\n⚙️  Mobile App Settings:")
        print("  • Enable Smart Reply")
        print("  • Configure swipe actions")
        print("  • Set up notifications")
        print("  • Enable 'Send & Archive'")

        print("\n🔗 Download Links:")
        print("  • iOS: https://apps.apple.com/app/gmail/id422689480")
        print("  • Android: https://play.google.com/store/apps/details?id=com.google.android.gm")

    def security_audit(self):
        """Security audit"""
        print("\n" + "="*80)
        print("🔒 SECURITY AUDIT")
        print("="*80)

        print("\n✅ Security Checklist:")
        checks = {
            "2-Step Verification": self.config["gmail_setup"]["features_enabled"].get("two_factor", False),
            "App Passwords": False,  # Would need to check
            "Recent Activity Review": False,
            "Device Management": False,
            "Recovery Email": False,
            "Recovery Phone": False
        }

        for check, status in checks.items():
            status_icon = "✅" if status else "⏳"
            print(f"  {status_icon} {check}")

        print("\n🔗 Security Settings:")
        print("  https://myaccount.google.com/security")

        print("\n📋 Recommended Actions:")
        print("  1. Enable 2-Step Verification")
        print("  2. Review recent security activity")
        print("  3. Check connected devices")
        print("  4. Set up recovery options")
        print("  5. Review app permissions")

        open_security = input("\nOpen security settings? (y/n): ").strip().lower()
        if open_security == 'y':
            webbrowser.open("https://myaccount.google.com/security")

    def performance_monitor(self):
        """Performance monitor"""
        print("\n" + "="*80)
        print("📈 PERFORMANCE MONITOR")
        print("="*80)

        total_accounts = len(self.config["all_emails"])
        added_accounts = len(self.config["gmail_setup"]["accounts_added"])
        labels_created = len(self.config["gmail_setup"]["labels_created"])
        filters_created = len(self.config["gmail_setup"]["filters_created"])
        features_enabled = sum(1 for v in self.config["gmail_setup"]["features_enabled"].values() if v)

        print("\n📊 Setup Progress:")
        print(f"  Accounts Added: {added_accounts}/{total_accounts} ({(added_accounts/total_accounts*100):.0f}%)")
        print(f"  Labels Created: {labels_created}/10")
        print(f"  Filters Created: {filters_created}/6")
        print(f"  Features Enabled: {features_enabled}/5")

        overall = (
            (added_accounts/total_accounts) +
            (labels_created/10) +
            (filters_created/6) +
            (features_enabled/5)
        ) / 4 * 100
        print(f"\n  Overall Progress: {overall:.0f}%")

        if overall >= 90:
            print("\n🎉 Excellent! Your setup is nearly complete!")
        elif overall >= 50:
            print("\n👍 Good progress! Keep going!")
        else:
            print("\n💪 Getting started! Follow the setup guides.")

    def view_all_guides(self):
        """View all guides"""
        print("\n" + "="*80)
        print("📚 ALL AVAILABLE GUIDES")
        print("="*80)

        guides = {
            "GMAIL_HOT_ROD_SETUP.md": "Complete Hot Rod setup guide",
            "GMAIL_CENTRAL_EMAIL_SETUP.md": "Gmail central email setup",
            "GMAIL_DIRECT_LINKS.md": "Direct links reference",
            "email_quick_reference.md": "Quick reference card",
            "noizylab_email_setup.md": "Email setup documentation",
            "DOMAINS_EMAILS_UPDATE_SUMMARY.md": "Update summary"
        }

        print("\nAvailable Guides:")
        for i, (guide, description) in enumerate(guides.items(), 1):
            guide_path = Path(__file__).parent / guide
            exists = "✅" if guide_path.exists() else "⏳"
            print(f"  {exists} {i}. {guide}")
            print(f"     {description}")

        choice = input("\nOpen which guide? (number or name): ").strip()
        # Implementation for opening guides would go here

    def quick_reference_card(self):
        """Quick reference card"""
        print("\n" + "="*80)
        print("🎯 QUICK REFERENCE CARD")
        print("="*80)

        print("\n📧 Your Emails:")
        for email in self.config["all_emails"]:
            print(f"  • {email}")

        print("\n🔗 Quick Links:")
        print("  • Gmail: https://mail.google.com")
        print("  • Settings: https://mail.google.com/mail/u/0/#settings/all")
        print("  • Security: https://myaccount.google.com/security")

        print("\n⌨️  Keyboard Shortcuts:")
        print("  • c = Compose")
        print("  • r = Reply")
        print("  • e = Archive")
        print("  • # = Delete")
        print("  • j/k = Next/Previous")
        print("  • / = Search")

    def help_troubleshooting(self):
        """Help and troubleshooting"""
        print("\n" + "="*80)
        print("❓ HELP & TROUBLESHOOTING")
        print("="*80)

        print("\n🔧 Common Issues:")
        print("  1. Emails not syncing?")
        print("     → Check server settings")
        print("     → Verify passwords")
        print("     → Check POP3/IMAP enabled")

        print("\n  2. Can't send from other addresses?")
        print("     → Verify email addresses in 'Send mail as'")
        print("     → Check verification emails")

        print("\n  3. Filters not working?")
        print("     → Check filter criteria")
        print("     → Verify labels exist")

        print("\n📚 Documentation:")
        print("  • See GMAIL_HOT_ROD_SETUP.md for complete guide")
        print("  • See email_quick_reference.md for quick help")

        print("\n🔗 Gmail Help:")
        print("  https://support.google.com/mail")

    def open_guide(self, filename):
        """Open a guide file"""
        guide_path = Path(__file__).parent / filename
        if guide_path.exists():
            try:
                subprocess.run(["open", str(guide_path)])
            except:
                print(f"Guide location: {guide_path}")

if __name__ == "__main__":
    control = EmailMasterControl()
    control.main_menu()

