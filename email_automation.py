#!/usr/bin/env python3
from datetime import datetime, timedelta
from pathlib import Path
import json
import subprocess
import sys
import webbrowser

#!/usr/bin/env python3
"""
Email Automation System
Advanced automation for email management
"""


class EmailAutomation:
    """Email automation system"""

    def __init__(self):
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "email_automation.json"
        self.load_config()

    def load_config(self):
        """Load automation configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "automations": {
                    "auto_label": True,
                    "auto_archive_old": True,
                    "auto_star_important": True,
                    "auto_forward_urgent": False,
                    "auto_reply_out_of_office": False
                },
                "rules": [],
                "schedules": [],
                "last_run": None
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def main_menu(self):
        """Main automation menu"""
        while True:
            print("\n" + "="*80)
            print("🤖 EMAIL AUTOMATION SYSTEM")
            print("="*80)
            print("\n📋 Automation Features:")
            print("  1. 🏷️  Auto-Labeling Rules")
            print("  2. ⭐ Auto-Star Important Emails")
            print("  3. 📦 Auto-Archive Old Emails")
            print("  4. 🔔 Auto-Forward Urgent Emails")
            print("  5. 📧 Auto-Reply (Out of Office)")
            print("  6. 🔍 Smart Filter Generator")
            print("  7. 📊 Email Analytics Dashboard")
            print("  8. 🔄 Batch Operations")
            print("  9. 📝 Export Automation Rules")
            print("  10. ⚙️  Automation Settings")
            print("  0. Exit")
            print("="*80)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.auto_labeling_rules()
            elif choice == "2":
                self.auto_star_important()
            elif choice == "3":
                self.auto_archive_old()
            elif choice == "4":
                self.auto_forward_urgent()
            elif choice == "5":
                self.auto_reply_ooo()
            elif choice == "6":
                self.smart_filter_generator()
            elif choice == "7":
                self.email_analytics()
            elif choice == "8":
                self.batch_operations()
            elif choice == "9":
                self.export_rules()
            elif choice == "10":
                self.automation_settings()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def auto_labeling_rules(self):
        """Auto-labeling rules generator"""
        print("\n" + "="*80)
        print("🏷️  AUTO-LABELING RULES GENERATOR")
        print("="*80)

        print("\n📋 Pre-configured Auto-Labeling Rules:")

        rules = [
            {
                "name": "fishmusicinc.com Auto-Label",
                "criteria": "from:rp@fishmusicinc.com OR from:info@fishmusicinc.com",
                "actions": ["Apply label: fishmusicinc.com", "Never mark as spam", "Mark as important"]
            },
            {
                "name": "noizylab.ca Auto-Label",
                "criteria": "from:rsp@noizylab.ca OR from:help@noizylab.ca OR from:hello@noizylab.ca",
                "actions": ["Apply label: noizylab.ca", "Never mark as spam", "Mark as important"]
            },
            {
                "name": "iCloud Auto-Label",
                "criteria": "from:rsplowman@icloud.com",
                "actions": ["Apply label: iCloud", "Never mark as spam"]
            },
            {
                "name": "Priority Keywords",
                "criteria": "urgent OR important OR asap OR priority OR 'action required'",
                "actions": ["Apply label: Priority", "Star it", "Mark as important"]
            },
            {
                "name": "Attachments",
                "criteria": "has:attachment",
                "actions": ["Apply label: Attachments", "Star it"]
            },
            {
                "name": "Notifications",
                "criteria": "from:noreply OR from:notification OR from:alert",
                "actions": ["Apply label: Notifications", "Skip inbox", "Never mark as spam"]
            }
        ]

        for i, rule in enumerate(rules, 1):
            print(f"\n  {i}. {rule['name']}")
            print(f"     Criteria: {rule['criteria']}")
            print(f"     Actions: {', '.join(rule['actions'])}")

        print("\n🔗 Create these filters in Gmail:")
        print("  https://mail.google.com/mail/u/0/#settings/filters")

        webbrowser.open("https://mail.google.com/mail/u/0/#settings/filters")

    def auto_star_important(self):
        """Auto-star important emails"""
        print("\n" + "="*80)
        print("⭐ AUTO-STAR IMPORTANT EMAILS")
        print("="*80)

        print("\n📋 Star Rules:")
        print("  1. From important senders (rp@fishmusicinc.com, rsp@noizylab.ca)")
        print("  2. Contains priority keywords")
        print("  3. Has attachments")
        print("  4. From your domains")

        print("\n🔍 Filter Criteria:")
        print("  from:rp@fishmusicinc.com OR from:rsp@noizylab.ca OR")
        print("  (urgent OR important OR asap) OR has:attachment")

        print("\n✅ Actions:")
        print("  • Star it")
        print("  • Mark as important")
        print("  • Apply label: Priority")

        print("\n🔗 Create filter:")
        print("  https://mail.google.com/mail/u/0/#settings/filters")

    def auto_archive_old(self):
        """Auto-archive old emails"""
        print("\n" + "="*80)
        print("📦 AUTO-ARCHIVE OLD EMAILS")
        print("="*80)

        print("\n📋 Archive Rules:")
        print("  • Emails older than 30 days (not starred)")
        print("  • Read emails older than 90 days")
        print("  • Newsletters older than 7 days")

        print("\n⚠️  Note: Gmail doesn't support auto-archive by age natively.")
        print("Use filters to skip inbox for specific types of emails.")

        print("\n💡 Alternative: Use Gmail's 'Auto-advance' feature:")
        print("  • Archive emails manually after reading")
        print("  • Use 'Send & Archive' button")
        print("  • Enable auto-advance in settings")

    def auto_forward_urgent(self):
        """Auto-forward urgent emails"""
        print("\n" + "="*80)
        print("🔔 AUTO-FORWARD URGENT EMAILS")
        print("="*80)

        print("\n📋 Forward Rules:")
        print("  • Forward urgent emails to mobile")
        print("  • Forward important emails to backup account")

        print("\n🔍 Filter Criteria:")
        print("  (urgent OR important OR asap) AND is:unread")

        print("\n✅ Actions:")
        print("  • Forward to: rsplowman@gmail.com")
        print("  • Keep in inbox")
        print("  • Mark as important")

        print("\n🔗 Create filter:")
        print("  https://mail.google.com/mail/u/0/#settings/filters")

    def auto_reply_ooo(self):
        """Auto-reply out of office"""
        print("\n" + "="*80)
        print("📧 AUTO-REPLY (OUT OF OFFICE)")
        print("="*80)

        print("\n📋 Out of Office Setup:")
        print("  1. Go to Gmail Settings → General")
        print("  2. Scroll to 'Vacation responder'")
        print("  3. Enable vacation responder")
        print("  4. Set date range")
        print("  5. Write message")

        print("\n📝 Sample Message:")
        print("  Thank you for your email. I am currently out of the office")
        print("  from [start date] to [end date] and will respond when I return.")
        print("  For urgent matters, please contact [contact].")

        print("\n🔗 Settings:")
        print("  https://mail.google.com/mail/u/0/#settings/general")

    def smart_filter_generator(self):
        """Smart filter generator"""
        print("\n" + "="*80)
        print("🔍 SMART FILTER GENERATOR")
        print("="*80)

        print("\n🎯 Generate Custom Filters:")
        print("\n1. Sender-based:")
        sender = input("  Enter sender email (or press Enter to skip): ").strip()
        if sender:
            print(f"  Filter: from:{sender}")
            print(f"  Actions: Apply label, Mark important")

        print("\n2. Keyword-based:")
        keyword = input("  Enter keyword (or press Enter to skip): ").strip()
        if keyword:
            print(f"  Filter: {keyword}")
            print(f"  Actions: Apply label, Star it")

        print("\n3. Attachment-based:")
        has_attach = input("  Filter emails with attachments? (y/n): ").strip().lower()
        if has_attach == 'y':
            print("  Filter: has:attachment")
            print("  Actions: Apply label: Attachments, Star it")

        print("\n🔗 Create filters:")
        print("  https://mail.google.com/mail/u/0/#settings/filters")

    def email_analytics(self):
        """Email analytics dashboard"""
        print("\n" + "="*80)
        print("📊 EMAIL ANALYTICS DASHBOARD")
        print("="*80)

        print("\n📈 Gmail Insights:")
        print("  • Check Gmail's built-in insights")
        print("  • View email volume")
        print("  • Response times")

        print("\n🔍 Search Analytics:")
        print("  • Most common senders")
        print("  • Email volume by domain")
        print("  • Attachment frequency")

        print("\n💡 Use Gmail Search:")
        print("  • 'from:domain.com' - Count emails from domain")
        print("  • 'has:attachment' - Count emails with attachments")
        print("  • 'is:unread' - Count unread emails")

        print("\n📊 Third-Party Tools:")
        print("  • Boomerang - Email analytics")
        print("  • Mixmax - Email tracking")
        print("  • Mailtrack - Read receipts")

    def batch_operations(self):
        """Batch operations"""
        print("\n" + "="*80)
        print("🔄 BATCH OPERATIONS")
        print("="*80)

        print("\n📋 Batch Operations:")
        print("  1. Archive all read emails older than 30 days")
        print("  2. Label all emails from specific domain")
        print("  3. Star all emails with attachments")
        print("  4. Delete all emails from specific sender")

        print("\n🔍 Use Gmail Search + Select All:")
        print("  1. Search for emails")
        print("  2. Select all (checkbox)")
        print("  3. Apply action (archive, label, delete)")

        print("\n⚠️  Warning: Batch operations affect all matching emails!")
        print("  Always test with a small batch first.")

    def export_rules(self):
        """Export automation rules"""
        print("\n" + "="*80)
        print("📝 EXPORT AUTOMATION RULES")
        print("="*80)

        export_file = self.config_dir / "automation_rules_export.json"

        export_data = {
            "export_date": datetime.now().isoformat(),
            "automations": self.config["automations"],
            "rules": self.config["rules"],
            "gmail_filters": [
                {
                    "name": "fishmusicinc.com Auto-Label",
                    "criteria": "from:rp@fishmusicinc.com OR from:info@fishmusicinc.com",
                    "actions": ["Apply label: fishmusicinc.com", "Never spam", "Mark important"]
                },
                {
                    "name": "noizylab.ca Auto-Label",
                    "criteria": "from:rsp@noizylab.ca OR from:help@noizylab.ca OR from:hello@noizylab.ca",
                    "actions": ["Apply label: noizylab.ca", "Never spam", "Mark important"]
                }
            ]
        }

        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"\n✅ Rules exported to: {export_file}")

    def automation_settings(self):
        """Automation settings"""
        print("\n" + "="*80)
        print("⚙️  AUTOMATION SETTINGS")
        print("="*80)

        print("\n📋 Current Settings:")
        for key, value in self.config["automations"].items():
            status = "✅ Enabled" if value else "⏳ Disabled"
            print(f"  {status} - {key.replace('_', ' ').title()}")

        print("\n🔧 Toggle Settings:")
        for key in self.config["automations"]:
            toggle = input(f"\nToggle {key.replace('_', ' ').title()}? (y/n): ").strip().lower()
            if toggle == 'y':
                self.config["automations"][key] = not self.config["automations"][key]
                self.save_config()
                status = "enabled" if self.config["automations"][key] else "disabled"
                print(f"✅ {key.replace('_', ' ').title()} {status}!")

if __name__ == "__main__":
    try:
        automation = EmailAutomation()
            automation.main_menu()


    except Exception as e:
        print(f"Error: {e}")
