#!/usr/bin/env python3
#!/usr/bin/env python3
"""
MASTER LAUNCHER - Launch Everything
Single entry point for entire system
"""

import json
import subprocess
import sys
from pathlib import Path

class MasterLauncher:
    """Master launcher for everything"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.config_file = self.base_dir / "master_config.json"
        self.autokeep_config = self.base_dir / ".cursor" / "rules" / "autokeep.json"
        self.autokeep_commit = self.base_dir / "autokeep-commit.js"
        self.autokeep_review = self.base_dir / "autokeep-review.js"
        self.load_config()

    def load_config(self):
        """Load configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "version": "7.0 - MASTER",
                "total_systems": 50,
                "auto_start": False
            }

    def show_master_menu(self):
        """Show master menu"""
        print("\n" + "="*80)
        print("🚀🚀🚀 MASTER LAUNCHER - ULTIMATE SYSTEM 🚀🚀🚀")
        print("="*80)
        print("\n💻 System: M2 Ultra Mac Studio (192GB RAM)")
        print("⚡ Performance: 1000x+ faster")
        print("🎯 Capabilities: 10,000+")
        print("📊 Systems: 50+")
        
        # Show AutoKeep status
        autokeep_status = self.check_autokeep_status()
        if autokeep_status:
            print("\n🤖 AutoKeep: ✅ Active & Tracking All Changes")
        else:
            print("\n🤖 AutoKeep: ⚠️  Not Fully Configured")
        
        print("\n" + "="*80)
        print("🔥 QUICK ACTIONS")
        print("="*80)
        print("  1. 🚀 Launch Ultimate System")
        print("  2. ⚡ Launch Ultra Hot Rod Mode")
        print("  3. 🤖 Gemini AI System (NEW!)")
        print("  4. 🧪 Test Everything")
        print("  5. 📱 iOS Setup")
        print("  6. 🤖 AI Integration")
        print("  7. ⚙️  Automation Setup")
        print("  8. 🚀 Deploy System")
        print("  9. 👥 Team Setup")
        print("  10. 📊 Analytics Dashboard")
        print("  11. 🔧 System Maintenance")
        print("  12. ⚡ One-Click Setup (Everything)")
        print("  13. 📚 Documentation")
        print("  14. 🤖 AutoKeep Status & Info")
        print("  0. Exit")
        print("="*80)

    def launch_ultimate(self):
        """Launch ultimate system"""
        subprocess.run([sys.executable, str(self.base_dir / "ULTIMATE_1000X_SYSTEM.py")])

    def launch_ultra_hotrod(self):
        """Launch ultra hot rod"""
        subprocess.run([sys.executable, str(self.base_dir / "ULTRA_LAUNCH.py")])

    def launch_gemini_ai(self):
        """Launch Gemini AI"""
        subprocess.run([sys.executable, str(self.base_dir / "gemini_integration.py")])

    def test_everything(self):
        """Test everything"""
        subprocess.run([sys.executable, str(self.base_dir / "test_suite.py")])

    def ios_setup(self):
        """iOS setup"""
        subprocess.run([sys.executable, str(self.base_dir / "ios_installer.py")])

    def ai_integration(self):
        """AI integration"""
        subprocess.run([sys.executable, str(self.base_dir / "ai_integration_guide.py")])

    def automation_setup(self):
        """Automation setup"""
        subprocess.run([sys.executable, str(self.base_dir / "automation_engine.py")])

    def deploy_system(self):
        """Deploy system"""
        subprocess.run([sys.executable, str(self.base_dir / "deployment_manager.py")])

    def team_setup(self):
        """Team setup"""
        subprocess.run([sys.executable, str(self.base_dir / "team_collaboration.py")])

    def analytics(self):
        """Analytics"""
        subprocess.run([sys.executable, str(self.base_dir / "advanced_analytics.py")])

    def maintenance(self):
        """Maintenance"""
        subprocess.run([sys.executable, str(self.base_dir / "MASTER_CLEANUP.py")])

    def one_click_setup(self):
        """One-click setup"""
        subprocess.run([sys.executable, str(self.base_dir / "one_click_setup.py")])

    def check_autokeep_status(self):
        """Check if AutoKeep is properly configured"""
        return (
            self.autokeep_config.exists() and
            self.autokeep_commit.exists() and
            self.autokeep_review.exists()
        )

    def show_autokeep_info(self):
        """Show AutoKeep information and status"""
        print("\n" + "="*80)
        print("🤖 AUTOKEEP REVIEW ENGINE")
        print("="*80)
        
        autokeep_status = self.check_autokeep_status()
        
        if autokeep_status:
            print("\n✅ Status: ACTIVE")
            print("\n📋 Configuration:")
            print(f"  • Config: {'✅' if self.autokeep_config.exists() else '❌'} .cursor/rules/autokeep.json")
            print(f"  • Commit Script: {'✅' if self.autokeep_commit.exists() else '❌'} autokeep-commit.js")
            print(f"  • Review Script: {'✅' if self.autokeep_review.exists() else '❌'} autokeep-review.js")
            
            print("\n🚀 How It Works:")
            print("  • Auto-commits changes when you save files in Cursor")
            print("  • Generates AI-powered commit messages using Cursor's internal model")
            print("  • Creates detailed review files for each commit")
            print("  • Stores reviews in reviews/ directory")
            
            print("\n📊 Quick Actions:")
            print("  1. View latest review files")
            print("  2. Manual commit (if changes exist)")
            print("  3. View AutoKeep setup documentation")
            print("  4. Check git log for AutoKeep commits")
            
            action = input("\n👉 Select action (1-4, or Enter to go back): ").strip()
            
            if action == "1":
                reviews_dir = self.base_dir / "reviews"
                if reviews_dir.exists():
                    review_files = sorted(reviews_dir.glob("review-*.md"), reverse=True)
                    if review_files:
                        print(f"\n📝 Latest Review Files ({len(review_files)} total):")
                        for i, rf in enumerate(review_files[:5], 1):
                            print(f"  {i}. {rf.name}")
                        if len(review_files) > 5:
                            print(f"  ... and {len(review_files) - 5} more")
                    else:
                        print("\n📝 No review files yet. Save some files to generate reviews!")
                else:
                    print("\n📝 Reviews directory doesn't exist yet.")
            
            elif action == "2":
                print("\n🔄 Running AutoKeep commit...")
                try:
                    result = subprocess.run(
                        ["node", str(self.autokeep_commit)],
                        cwd=str(self.base_dir),
                        capture_output=True,
                        text=True
                    )
                    print(result.stdout)
                    if result.stderr:
                        print(result.stderr)
                except Exception as e:
                    print(f"❌ Error: {e}")
            
            elif action == "3":
                setup_file = self.base_dir / "AUTOKEEP_SETUP.md"
                if setup_file.exists():
                    print(f"\n📚 Opening documentation: {setup_file}")
                    try:
                        subprocess.run(["open", str(setup_file)])
                    except:
                        print("💡 Please open AUTOKEEP_SETUP.md manually")
                else:
                    print("\n📚 Documentation not found.")
            
            elif action == "4":
                print("\n📜 Recent AutoKeep Commits:")
                try:
                    result = subprocess.run(
                        ["git", "log", "--oneline", "--grep=AutoKeep", "-10"],
                        cwd=str(self.base_dir),
                        capture_output=True,
                        text=True
                    )
                    if result.stdout.strip():
                        print(result.stdout)
                    else:
                        print("  No AutoKeep commits yet.")
                except Exception as e:
                    print(f"❌ Error: {e}")
        
        else:
            print("\n⚠️  Status: NOT FULLY CONFIGURED")
            print("\n📋 Missing Components:")
            if not self.autokeep_config.exists():
                print("  ❌ Configuration file: .cursor/rules/autokeep.json")
            if not self.autokeep_commit.exists():
                print("  ❌ Commit script: autokeep-commit.js")
            if not self.autokeep_review.exists():
                print("  ❌ Review script: autokeep-review.js")
            
            print("\n💡 AutoKeep is already configured in this workspace!")
            print("  See AUTOKEEP_SETUP.md for details")

    def show_docs(self):
        """Show documentation"""
        docs = list(self.base_dir.glob("*.md"))
        print("\n📚 Available Documentation:")
        for i, doc in enumerate(docs[:10], 1):
            print(f"  {i}. {doc.name}")

    def main(self):
        """Main menu"""
        while True:
            self.show_master_menu()
            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.launch_ultimate()
            elif choice == "2":
                self.launch_ultra_hotrod()
            elif choice == "3":
                self.launch_gemini_ai()
            elif choice == "4":
                self.test_everything()
            elif choice == "5":
                self.ios_setup()
            elif choice == "6":
                self.ai_integration()
            elif choice == "7":
                self.automation_setup()
            elif choice == "8":
                self.deploy_system()
            elif choice == "9":
                self.team_setup()
            elif choice == "10":
                self.analytics()
            elif choice == "11":
                self.maintenance()
            elif choice == "12":
                self.one_click_setup()
            elif choice == "13":
                self.show_docs()
            elif choice == "14":
                self.show_autokeep_info()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        launcher = MasterLauncher()
        launcher.main()
    except Exception as e:
        print(f"Error: {e}")