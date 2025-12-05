#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import json
import subprocess
import sys
import webbrowser

#!/usr/bin/env python3
"""
Email System Manager - Ultimate Control Center
Advanced management and monitoring for all email accounts
"""


class EmailSystemManager:
    """Ultimate email system manager"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "system_manager.json"
        self.load_config()

    def load_config(self):
        """Load system configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "gmail": "rsplowman@gmail.com",
                "domains": {
                    "fishmusicinc.com": ["rp@fishmusicinc.com", "info@fishmusicinc.com"],
                    "noizylab.ca": ["rsp@noizylab.ca", "help@noizylab.ca", "hello@noizylab.ca"],
                    "icloud.com": ["rsplowman@icloud.com"]
                },
                "system_status": {
                    "gmail_configured": False,
                    "accounts_added": [],
                    "labels_created": [],
                    "filters_created": [],
                    "ios_profiles_generated": False
                },
                "last_updated": datetime.now().isoformat()
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        self.config["last_updated"] = datetime.now().isoformat()
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def system_dashboard(self):
        """System dashboard"""
        print("\n" + "="*80)
        print("🎯 EMAIL SYSTEM MANAGER - DASHBOARD")
        print("="*80)

        total_accounts = sum(len(emails) for emails in self.config["domains"].values())
        added_accounts = len(self.config["system_status"]["accounts_added"])

        print(f"\n📧 Email Accounts:")
        print(f"  Total: {total_accounts + 1} (1 main + {total_accounts} domain)")
        print(f"  Added to Gmail: {added_accounts}/{total_accounts}")
        print(f"  Progress: {(added_accounts/total_accounts*100):.0f}%")

        print(f"\n🏷️  Organization:")
        print(f"  Labels: {len(self.config['system_status']['labels_created'])}")
        print(f"  Filters: {len(self.config['system_status']['filters_created'])}")

        print(f"\n📱 iOS Deployment:")
        ios_status = "✅" if self.config["system_status"]["ios_profiles_generated"] else "⏳"
        print(f"  Profiles: {ios_status}")

        print(f"\n🔗 Quick Actions:")
        print("  1. Open Gmail Settings")
        print("  2. Generate iOS Profiles")
        print("  3. System Health Check")
        print("  4. Backup Configuration")
        print("  5. View All Tools")

    def health_check(self):
        """System health check"""
        print("\n" + "="*80)
        print("🏥 SYSTEM HEALTH CHECK")
        print("="*80)

        checks = {
            "Configuration Files": self.config_file.exists(),
            "iOS Profiles": Path(self.config_dir / "ios_profiles").exists(),
            "Email Config": Path(self.config_dir / "email_config.json").exists(),
            "Master Config": (self.base_dir / "domains_and_emails_master.json").exists(),
        }

        print("\n✅ System Checks:")
        for check, status in checks.items():
            icon = "✅" if status else "❌"
            print(f"  {icon} {check}")

        print("\n📊 File Status:")
        scripts = list(self.base_dir.glob("*.py"))
        docs = list(self.base_dir.glob("*.md"))
        configs = list(self.base_dir.glob("*.json"))

        print(f"  ✅ Python Scripts: {len(scripts)}")
        print(f"  ✅ Documentation: {len(docs)}")
        print(f"  ✅ Config Files: {len(configs)}")

        if all(checks.values()):
            print("\n🎉 System Health: EXCELLENT!")
        else:
            print("\n⚠️  Some checks failed. Review above.")

    def quick_setup_wizard(self):
        """Quick setup wizard"""
        print("\n" + "="*80)
        print("🚀 QUICK SETUP WIZARD")
        print("="*80)

        print("\nThis wizard will guide you through:")
        print("  1. Gmail central setup")
        print("  2. Adding all email accounts")
        print("  3. Creating labels and filters")
        print("  4. iOS profile generation")

        start = input("\nStart quick setup? (y/n): ").strip().lower()
        if start != 'y':
            return

        # Step 1: Gmail
        print("\n" + "="*80)
        print("STEP 1: Gmail Setup")
        print("="*80)
        webbrowser.open("https://mail.google.com/mail/u/0/#settings/accounts")
        input("Press Enter when Gmail is configured...")

        # Step 2: iOS Profiles
        print("\n" + "="*80)
        print("STEP 2: Generate iOS Profiles")
        print("="*80)
        generate = input("Generate iOS profiles? (y/n): ").strip().lower()
        if generate == 'y':
            try:
                subprocess.run([sys.executable, str(self.base_dir / "create_ios_email_profiles.py")])
                self.config["system_status"]["ios_profiles_generated"] = True
                self.save_config()
            except Exception as e:
                print(f"Error: {e}")

        print("\n✅ Quick setup complete!")

    def main_menu(self):
        """Main menu"""
        while True:
            print("\n" + "="*80)
            print("🎯 EMAIL SYSTEM MANAGER")
            print("="*80)
            print(f"\n📧 Main Gmail: {self.config['gmail']}")
            print(f"📁 Location: {self.base_dir}")

            print("\n" + "="*80)
            print("🔥 MAIN ACTIONS")
            print("="*80)
            print("  1. 📊 System Dashboard")
            print("  2. 🚀 Quick Setup Wizard")
            print("  3. 🏥 Health Check")
            print("  4. 🔗 Open Gmail Settings")
            print("  5. 📱 Generate iOS Profiles")
            print("  6. 💾 Backup System")
            print("  7. 🔄 Restore System")
            print("  8. 🛠️  Launch Master Control")
            print("  9. 📚 View Documentation")
            print("  0. Exit")
            print("="*80)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.system_dashboard()
            elif choice == "2":
                self.quick_setup_wizard()
            elif choice == "3":
                self.health_check()
            elif choice == "4":
                webbrowser.open("https://mail.google.com/mail/u/0/#settings/all")
            elif choice == "5":
                self.generate_ios_profiles()
            elif choice == "6":
                self.backup_system()
            elif choice == "7":
                self.restore_system()
            elif choice == "8":
                self.launch_master_control()
            elif choice == "9":
                self.view_documentation()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def generate_ios_profiles(self):
        """Generate iOS profiles"""
        print("\n" + "="*80)
        print("📱 GENERATING iOS PROFILES")
        print("="*80)
        try:
            subprocess.run([sys.executable, str(self.base_dir / "create_ios_email_profiles.py")])
            self.config["system_status"]["ios_profiles_generated"] = True
            self.save_config()
            print("\n✅ iOS profiles generated!")
        except Exception as e:
            print(f"❌ Error: {e}")

    def backup_system(self):
        """Backup entire system"""
        print("\n" + "="*80)
        print("💾 BACKING UP SYSTEM")
        print("="*80)
        try:
            subprocess.run([sys.executable, str(self.base_dir / "email_backup_restore.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def restore_system(self):
        """Restore system"""
        print("\n" + "="*80)
        print("🔄 RESTORING SYSTEM")
        print("="*80)
        try:
            subprocess.run([sys.executable, str(self.base_dir / "email_backup_restore.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def launch_master_control(self):
        """Launch master control"""
        print("\n🚀 Launching Master Control...")
        try:
            subprocess.run([sys.executable, str(self.base_dir / "email_master_control.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def view_documentation(self):
        """View documentation"""
        print("\n" + "="*80)
        print("📚 DOCUMENTATION")
        print("="*80)

        docs = {
            "1": ("README_MASTER.md", "Main Documentation"),
            "2": ("QUICK_START_COMPLETE.md", "Quick Start Guide"),
            "3": ("GMAIL_HOT_ROD_SETUP.md", "Hot Rod Setup"),
            "4": ("INDEX.md", "File Index"),
        }

        for key, (doc, desc) in docs.items():
            exists = "✅" if (self.base_dir / doc).exists() else "⏳"
            print(f"  {exists} {key}. {doc} - {desc}")

        choice = input("\nOpen which document? (number): ").strip()
        if choice in docs:
            doc_file = self.base_dir / docs[choice][0]
            if doc_file.exists():
                try:
                    subprocess.run(["open", str(doc_file)])
                except:
                    print(f"File: {doc_file}")

if __name__ == "__main__":
    manager = EmailSystemManager()
    manager.main_menu()

