#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick Next Steps - Interactive Guide
"""

import subprocess
import sys
from pathlib import Path

class QuickNextSteps:
    """Quick next steps guide"""

    def __init__(self):
        self.base_dir = Path(__file__).parent

    def show_menu(self):
        """Show next steps menu"""
        print("\n" + "="*80)
        print("🚀 NEXT STEPS - WHAT TO DO NOW")
        print("="*80)
        print("\nWhat would you like to do?")
        print("  1. 🧪 Test the System")
        print("  2. 📱 Install on iOS (Web App)")
        print("  3. 📧 Set Up Email Profiles")
        print("  4. 💻 Build iOS App (Xcode)")
        print("  5. 🤖 Integrate AI (OpenAI)")
        print("  6. 🧠 Integrate AI (Core ML)")
        print("  7. 📊 View System Status")
        print("  8. 📚 View Documentation")
        print("  9. 🎯 Show Full Checklist")
        print("  0. Exit")
        print("="*80)

    def test_system(self):
        """Test the system"""
        print("\n🧪 Testing System...")
        print("\nLaunching START_HERE.py...")
        subprocess.run([sys.executable, str(self.base_dir / "START_HERE.py")])

    def install_web_app(self):
        """Install web app"""
        print("\n📱 Installing Web App on iOS...")
        print("\nSteps:")
        print("  1. Open Safari on iPhone")
        print("  2. Navigate to dashboard")
        print("  3. Tap Share → Add to Home Screen")
        print("  4. Done!")

        dashboard = self.base_dir / "dashboard_database" / "dashboard.html"
        if dashboard.exists():
            print(f"\n✅ Dashboard found: {dashboard}")
            open_file = input("\nOpen dashboard file location? (y/n): ").strip().lower()
            if open_file == 'y':
                subprocess.run(["open", "-R", str(dashboard)])

    def setup_email(self):
        """Set up email"""
        print("\n📧 Setting Up Email Profiles...")
        script = self.base_dir / "create_ios_email_profiles.py"
        if script.exists():
            print("\nGenerating email profiles...")
            subprocess.run([sys.executable, str(script)])
            print("\n✅ Profiles generated!")
            print("   Next: AirDrop .mobileconfig files to iPhone")
        else:
            print("\n⚠️  Email profile generator not found")

    def build_ios_app(self):
        """Build iOS app"""
        print("\n💻 Building iOS App...")
        print("\nSteps:")
        print("  1. Open Xcode")
        print("  2. File → New → Project")
        print("  3. iOS → App → SwiftUI")
        print("  4. Copy code from ios_apps/NOIZYLAB/NOIZYLABApp.swift")
        print("  5. Connect device, build & run")

        app_file = self.base_dir / "ios_apps" / "NOIZYLAB" / "NOIZYLABApp.swift"
        if app_file.exists():
            print(f"\n✅ App code ready: {app_file}")
            open_file = input("\nOpen app directory? (y/n): ").strip().lower()
            if open_file == 'y':
                subprocess.run(["open", str(app_file.parent)])

    def integrate_openai(self):
        """Integrate OpenAI"""
        print("\n🤖 Integrating OpenAI API...")
        print("\nSteps:")
        print("  1. Get API key from openai.com")
        print("  2. Add to your system securely")
        print("  3. Make API calls")
        print("\nSee: AI_INTEGRATION_RECOMMENDATIONS.md")

        guide = self.base_dir / "AI_INTEGRATION_RECOMMENDATIONS.md"
        if guide.exists():
            open_file = input("\nOpen AI integration guide? (y/n): ").strip().lower()
            if open_file == 'y':
                subprocess.run(["open", str(guide)])

    def integrate_coreml(self):
        """Integrate Core ML"""
        print("\n🧠 Integrating Core ML...")
        print("\nSteps:")
        print("  1. Open Xcode")
        print("  2. Use Create ML to train models")
        print("  3. Or convert existing models")
        print("  4. Add .mlmodel to project")
        print("\nSee: AI_INTEGRATION_RECOMMENDATIONS.md")

    def view_status(self):
        """View system status"""
        print("\n📊 System Status...")
        subprocess.run([sys.executable, str(self.base_dir / "advanced_monitoring.py")])

    def view_docs(self):
        """View documentation"""
        print("\n📚 Documentation...")
        docs = [
            "QUICK_START.md",
            "NEXT_STEPS.md",
            "AI_INTEGRATION_RECOMMENDATIONS.md",
            "IOS_INSTALLATION_GUIDE.md"
        ]

        print("\nAvailable Documentation:")
        for i, doc in enumerate(docs, 1):
            doc_file = self.base_dir / doc
            exists = "✅" if doc_file.exists() else "⏳"
            print(f"  {exists} {i}. {doc}")

        choice = input("\nOpen which? (number or name): ").strip()
        for doc in docs:
            if choice in doc.lower() or choice == str(docs.index(doc) + 1):
                doc_file = self.base_dir / doc
                if doc_file.exists():
                    subprocess.run(["open", str(doc_file)])
                break

    def show_checklist(self):
        """Show full checklist"""
        print("\n" + "="*80)
        print("📋 FULL CHECKLIST")
        print("="*80)

        print("\n✅ TODAY:")
        print("  [ ] Test system: python3 START_HERE.py")
        print("  [ ] Install web app on iPhone")
        print("  [ ] Set up email profiles")
        print("  [ ] Review AI options")

        print("\n✅ THIS WEEK:")
        print("  [ ] Build iOS app in Xcode")
        print("  [ ] Integrate AI (Core ML or OpenAI)")
        print("  [ ] Add custom data")
        print("  [ ] Train first AI model")

        print("\n✅ THIS MONTH:")
        print("  [ ] Deploy to team")
        print("  [ ] Set up cloud sync")
        print("  [ ] Customize for business")
        print("  [ ] Start production use")

    def main(self):
        """Main menu"""
        while True:
            self.show_menu()
            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.test_system()
            elif choice == "2":
                self.install_web_app()
            elif choice == "3":
                self.setup_email()
            elif choice == "4":
                self.build_ios_app()
            elif choice == "5":
                self.integrate_openai()
            elif choice == "6":
                self.integrate_coreml()
            elif choice == "7":
                self.view_status()
            elif choice == "8":
                self.view_docs()
            elif choice == "9":
                self.show_checklist()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        steps = QuickNextSteps()
            steps.main()


    except Exception as e:
        print(f"Error: {e}")
