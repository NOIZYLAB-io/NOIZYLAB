#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Device Viewer - See and manage connected iOS devices
"""

import json
import subprocess
import sys
from pathlib import Path

class DeviceViewer:
    """Device viewer and manager"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.device_db = self.base_dir / "device_database"
        self.device_db.mkdir(exist_ok=True)

    def show_available_apps(self):
        """Show apps that can view devices"""
        print("\n" + "="*80)
        print("📱 APPS TO SEE iOS DEVICES")
        print("="*80)

        apps = {
            "1. Finder": {
                "description": "Built-in Mac app - shows connected devices",
                "how_to": "Connect device → Open Finder → Device appears in sidebar",
                "features": ["View device", "Access files", "Sync", "Backup"]
            },
            "2. Xcode": {
                "description": "Apple's development tool - best for development",
                "how_to": "Window → Devices and Simulators (Shift+Cmd+2)",
                "features": ["View devices", "Install apps", "View logs", "Screenshots"]
            },
            "3. Apple Configurator 2": {
                "description": "Professional device management - FREE from App Store",
                "how_to": "Download from App Store → Connect device → See in app",
                "features": ["Manage devices", "Install profiles", "View info", "Backup"]
            },
            "4. System Information": {
                "description": "Built-in Mac utility - shows hardware info",
                "how_to": "Apple menu → About This Mac → System Report → USB",
                "features": ["View device info", "Hardware details", "USB info"]
            },
            "5. Image Capture": {
                "description": "Built-in Mac app - view photos and device",
                "how_to": "Applications → Image Capture → Device appears",
                "features": ["View device", "Import photos", "Device info"]
            }
        }

        for app_name, details in apps.items():
            print(f"\n{app_name}")
            print(f"  Description: {details['description']}")
            print(f"  How to use: {details['how_to']}")
            print(f"  Features: {', '.join(details['features'])}")

        return apps

    def check_connected_devices(self):
        """Check for connected devices"""
        print("\n" + "="*80)
        print("🔍 CHECKING FOR CONNECTED DEVICES")
        print("="*80)

        # Try system_profiler
        try:
            result = subprocess.run(
                ["system_profiler", "SPUSBDataType"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if "iPhone" in result.stdout or "iPad" in result.stdout:
                print("\n✅ iOS Device Detected!")
                print("   Check Finder sidebar or Xcode")
            else:
                print("\n⏳ No iOS devices detected")
                print("   Connect iPhone/iPad via USB")
        except Exception as e:
            print(f"\n⚠️  Could not check: {e}")

        print("\n💡 To see devices:")
        print("   1. Connect iPhone/iPad via USB")
        print("   2. Unlock device")
        print("   3. Tap 'Trust This Computer'")
        print("   4. Open Finder → Device appears in sidebar")
        print("   5. OR Open Xcode → Window → Devices and Simulators")

    def recommend_app(self):
        """Recommend best app"""
        print("\n" + "="*80)
        print("⭐ RECOMMENDED APP")
        print("="*80)
        print("\n🎯 For Development (Xcode):")
        print("   • Best for installing apps")
        print("   • View device logs")
        print("   • Take screenshots")
        print("   • Window → Devices and Simulators (Shift+Cmd+2)")

        print("\n🎯 For Management (Apple Configurator 2):")
        print("   • Best for managing multiple devices")
        print("   • Install profiles")
        print("   • View device info")
        print("   • FREE from App Store")

        print("\n🎯 For Quick View (Finder):")
        print("   • Easiest - built into Mac")
        print("   • Just connect device")
        print("   • Appears in Finder sidebar")

    def open_finder_devices(self):
        """Open Finder to show devices"""
        print("\n📂 Opening Finder...")
        try:
            subprocess.run(["open", "-R", "/"])
            print("   Device will appear in sidebar when connected")
        except:
            pass

    def open_xcode_devices(self):
        """Open Xcode devices window"""
        print("\n💻 Opening Xcode Devices...")
        print("   If Xcode is installed:")
        print("   Window → Devices and Simulators (Shift+Cmd+2)")
        try:
            subprocess.run(["open", "-a", "Xcode"])
            print("   ✅ Xcode opened")
            print("   Press Shift+Cmd+2 to see devices")
        except:
            print("   ⚠️  Xcode not installed")
            print("   Install from App Store")

if __name__ == "__main__":
    viewer = DeviceViewer()
    viewer.show_available_apps()
    viewer.check_connected_devices()
    viewer.recommend_app()

    print("\n" + "="*80)
    choice = input("\nOpen Finder? (y/n): ").strip().lower()
    if choice == 'y':
        viewer.open_finder_devices()

    choice = input("Open Xcode Devices? (y/n): ").strip().lower()
    if choice == 'y':
        viewer.open_xcode_devices()

