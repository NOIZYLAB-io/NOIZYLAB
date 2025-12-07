#!/usr/bin/env python3
#!/usr/bin/env python3
"""
iOS Installer - Automated Installation Helper
Guides you through installing everything on iOS
"""

import json
import subprocess
import sys
from pathlib import Path

class iOSInstaller:
    """iOS installation helper"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.ios_apps_dir = self.base_dir / "ios_apps"
        self.profiles_dir = self.base_dir / "ios_profiles"

    def show_installation_menu(self):
        """Show installation menu"""
        print("\n" + "="*80)
        print("📱 iOS INSTALLATION HELPER")
        print("="*80)
        print("\nWhat would you like to install?")
        print("  1. 📧 Email Configuration Profiles")
        print("  2. 📱 Native iOS App (Xcode)")
        print("  3. ⚡ iOS Shortcuts")
        print("  4. 📊 iOS Widgets")
        print("  5. 🌐 Web App (PWA)")
        print("  6. 📋 Show All Instructions")
        print("  0. Exit")
        print("="*80)

    def install_email_profiles(self):
        """Install email profiles"""
        print("\n" + "="*80)
        print("📧 EMAIL PROFILE INSTALLATION")
        print("="*80)

        # Check if profiles exist
        if not (self.base_dir / "create_ios_email_profiles.py").exists():
            print("\n⚠️  Profile generator not found. Creating...")
            # Would create it here if needed

        print("\n📋 Steps:")
        print("  1. Generate profiles:")
        print("     python3 create_ios_email_profiles.py")
        print("\n  2. AirDrop to iPhone:")
        print("     • Open Finder")
        print("     • Navigate to generated .mobileconfig files")
        print("     • Right-click → Share → AirDrop")
        print("     • Select your iPhone")
        print("\n  3. On iPhone:")
        print("     • Tap 'Accept' when AirDrop appears")
        print("     • Go to Settings → Profile Downloaded")
        print("     • Tap 'Install'")
        print("     • Enter passcode if prompted")
        print("\n  4. Verify:")
        print("     • Settings → Mail → Accounts")
        print("     • Your email should be listed")

        # Generate if requested
        generate = input("\nGenerate profiles now? (y/n): ").strip().lower()
        if generate == 'y':
            try:
                subprocess.run([sys.executable, str(self.base_dir / "create_ios_email_profiles.py")])
                print("\n✅ Profiles generated!")
                print("   Location: Check for .mobileconfig files")
            except Exception as e:
                print(f"\n⚠️  Error: {e}")

    def install_native_app(self):
        """Install native app"""
        print("\n" + "="*80)
        print("📱 NATIVE iOS APP INSTALLATION")
        print("="*80)

        app_dir = self.ios_apps_dir / "NOIZYLAB"

        if not app_dir.exists():
            print("\n⚠️  App not generated yet.")
            generate = input("Generate app now? (y/n): ").strip().lower()
            if generate == 'y':
                try:
                    subprocess.run([sys.executable, str(self.base_dir / "ios_app_generator.py")])
                except Exception as e:
                    print(f"⚠️  Error: {e}")
            return

        print("\n📋 Steps:")
        print("  1. Open in Xcode:")
        print(f"     cd {app_dir}")
        print("     open -a Xcode .")
        print("\n  2. In Xcode:")
        print("     • Connect iPhone/iPad via USB")
        print("     • Select device in Xcode")
        print("     • Click Run (▶️) or Cmd+R")
        print("\n  3. On Device:")
        print("     • Trust computer if prompted")
        print("     • App will install automatically")
        print("\n  4. First Launch:")
        print("     • Settings → General → VPN & Device Management")
        print("     • Tap your developer account")
        print("     • Tap 'Trust'")
        print("     • App will now open")

        open_xcode = input("\nOpen in Xcode now? (y/n): ").strip().lower()
        if open_xcode == 'y' and app_dir.exists():
            try:
                subprocess.run(["open", "-a", "Xcode", str(app_dir)])
                print("\n✅ Opening in Xcode...")
            except Exception as e:
                print(f"\n⚠️  Xcode not found. Install Xcode from App Store.")

    def install_shortcuts(self):
        """Install shortcuts"""
        print("\n" + "="*80)
        print("⚡ iOS SHORTCUTS INSTALLATION")
        print("="*80)

        shortcuts_file = self.ios_apps_dir / "ios_shortcuts.json"

        print("\n📋 Steps:")
        print("  1. Install Shortcuts app:")
        print("     • Open App Store on iPhone")
        print("     • Search 'Shortcuts'")
        print("     • Install (free)")
        print("\n  2. Import Shortcuts:")
        print("     • Open Shortcuts app")
        print("     • Tap '+' to create new")
        print("     • OR use Gallery")
        print(f"     • Reference: {shortcuts_file}")
        print("\n  3. Add to Siri:")
        print("     • Open shortcut")
        print("     • Tap '...' (three dots)")
        print("     • Tap 'Add to Siri'")
        print("     • Record voice command")
        print("\n  4. Add to Home Screen:")
        print("     • Open shortcut")
        print("     • Tap '...' → 'Add to Home Screen'")
        print("     • Customize icon and name")
        print("     • Tap 'Add'")

        if shortcuts_file.exists():
            print(f"\n✅ Shortcuts file found: {shortcuts_file.name}")

    def install_widgets(self):
        """Install widgets"""
        print("\n" + "="*80)
        print("📊 iOS WIDGETS INSTALLATION")
        print("="*80)

        print("\n📋 Steps:")
        print("  1. Build Widget Extension:")
        print("     • In Xcode: File → New → Target")
        print("     • Select 'Widget Extension'")
        print("     • Add to your app")
        print("\n  2. Add to Home Screen:")
        print("     • Long press on Home Screen")
        print("     • Tap '+' in top left")
        print("     • Search 'NOIZYLAB'")
        print("     • Select widget size")
        print("     • Tap 'Add Widget'")
        print("\n  3. Customize:")
        print("     • Long press widget")
        print("     • Tap 'Edit Widget'")
        print("     • Choose configuration")
        print("     • Tap 'Done'")

    def install_web_app(self):
        """Install web app (PWA)"""
        print("\n" + "="*80)
        print("🌐 WEB APP (PWA) INSTALLATION")
        print("="*80)

        print("\n📋 Steps:")
        print("  1. Open in Safari:")
        print("     • Navigate to your web dashboard")
        print("     • Or open: dashboard_database/dashboard.html")
        print("\n  2. Add to Home Screen:")
        print("     • Tap Share button (square with arrow)")
        print("     • Scroll down")
        print("     • Tap 'Add to Home Screen'")
        print("     • Customize name if desired")
        print("     • Tap 'Add'")
        print("\n  3. Use:")
        print("     • Tap icon on Home Screen")
        print("     • Opens like native app")
        print("     • Works offline (if configured)")

    def show_all_instructions(self):
        """Show all installation instructions"""
        self.install_email_profiles()
        input("\nPress Enter to continue...")
        self.install_native_app()
        input("\nPress Enter to continue...")
        self.install_shortcuts()
        input("\nPress Enter to continue...")
        self.install_widgets()
        input("\nPress Enter to continue...")
        self.install_web_app()

    def main(self):
        """Main menu"""
        while True:
            self.show_installation_menu()
            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.install_email_profiles()
            elif choice == "2":
                self.install_native_app()
            elif choice == "3":
                self.install_shortcuts()
            elif choice == "4":
                self.install_widgets()
            elif choice == "5":
                self.install_web_app()
            elif choice == "6":
                self.show_all_instructions()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    installer = iOSInstaller()
    installer.main()

