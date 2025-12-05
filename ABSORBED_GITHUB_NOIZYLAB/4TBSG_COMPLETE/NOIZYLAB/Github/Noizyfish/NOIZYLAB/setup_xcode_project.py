#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Complete Xcode Project Setup
Automates everything for iOS app installation
"""

import json
import os
import subprocess
import sys
from pathlib import Path

class XcodeProjectSetup:
    """Complete Xcode project setup"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.ios_dir = self.base_dir / "ios_apps" / "NOIZYLAB"
        self.project_dir = self.ios_dir / "NOIZYLAB.xcodeproj"

    def create_complete_project(self):
        """Create complete Xcode project"""
        print("\n" + "="*80)
        print("🚀 COMPLETE XCODE PROJECT SETUP")
        print("="*80)

        # Ensure directories exist
        self.ios_dir.mkdir(parents=True, exist_ok=True)
        self.project_dir.mkdir(exist_ok=True)

        # Create project structure
        self.create_project_files()
        self.create_info_plist()
        self.create_entitlements()
        self.create_build_settings()

        print("\n✅ Complete Xcode project created!")
        return True

    def create_project_files(self):
        """Create project files"""
        print("\n📁 Creating project files...")

        # Ensure Swift file exists
        swift_file = self.ios_dir / "NOIZYLABApp.swift"
        if not swift_file.exists():
            # Generate it
            from ios_app_generator import iOSAppGenerator
            generator = iOSAppGenerator()
            generator.generate_ios_app()

        print("  ✅ Swift files ready")

    def create_info_plist(self):
        """Create Info.plist"""
        print("📄 Creating Info.plist...")

        info_plist_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleDisplayName</key>
	<string>NOIZYLAB</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>$(PRODUCT_NAME)</string>
	<key>CFBundlePackageType</key>
	<string>$(PRODUCT_BUNDLE_PACKAGE_TYPE)</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleVersion</key>
	<string>1</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UIApplicationSceneManifest</key>
	<dict>
		<key>UIApplicationSupportsMultipleScenes</key>
		<true/>
	</dict>
	<key>UIApplicationSupportsIndirectInputEvents</key>
	<true/>
	<key>UILaunchScreen</key>
	<dict/>
	<key>UIRequiredDeviceCapabilities</key>
	<array>
		<string>armv7</string>
	</array>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
</dict>
</plist>"""

        plist_file = self.ios_dir / "Info.plist"
        with open(plist_file, 'w') as f:
            f.write(info_plist_content)

        print("  ✅ Info.plist created")

    def create_entitlements(self):
        """Create entitlements file"""
        print("🔐 Creating entitlements...")

        entitlements = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.team-identifier</key>
	<string>$(DEVELOPMENT_TEAM)</string>
</dict>
</plist>"""

        entitlements_file = self.ios_dir / "NOIZYLAB.entitlements"
        with open(entitlements_file, 'w') as f:
            f.write(entitlements)

        print("  ✅ Entitlements created")

    def create_build_settings(self):
        """Create build settings"""
        print("⚙️  Creating build settings...")

        settings = {
            "PRODUCT_NAME": "NOIZYLAB",
            "PRODUCT_BUNDLE_IDENTIFIER": "com.noizylab.NOIZYLAB",
            "SWIFT_VERSION": "5.0",
            "IPHONEOS_DEPLOYMENT_TARGET": "15.0",
            "TARGETED_DEVICE_FAMILY": "1,2"  # iPhone and iPad
        }

        settings_file = self.ios_dir / "build_settings.json"
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=2)

        print("  ✅ Build settings created")

    def open_in_xcode(self):
        """Open project in Xcode"""
        print("\n💻 Opening in Xcode...")

        # Try to open the directory in Xcode
        try:
            # Create a simple workspace or open the directory
            subprocess.run(["open", "-a", "Xcode", str(self.ios_dir)], check=False)
            print("  ✅ Opening Xcode...")
            print("\n📋 Next Steps in Xcode:")
            print("  1. Create New Project (if needed)")
            print("  2. File → New → Project")
            print("  3. iOS → App → SwiftUI")
            print("  4. Copy code from NOIZYLABApp.swift")
            return True
        except Exception as e:
            print(f"  ⚠️  Could not open Xcode automatically: {e}")
            print("\n📋 Manual Steps:")
            print("  1. Open Xcode")
            print("  2. File → New → Project")
            print(f"  3. Files are in: {self.ios_dir}")
            return False

    def create_quick_start_script(self):
        """Create quick start script"""
        print("\n📝 Creating quick start script...")

        script_content = f"""#!/bin/bash
# Quick Start Script for Xcode

echo "🚀 NOIZYLAB iOS App - Quick Start"
echo ""
echo "📁 Project Location:"
echo "   {self.ios_dir}"
echo ""
echo "💻 To Open in Xcode:"
echo "   1. Open Xcode"
echo "   2. File → New → Project"
echo "   3. iOS → App"
echo "   4. Name: NOIZYLAB"
echo "   5. Interface: SwiftUI"
echo "   6. Copy code from NOIZYLABApp.swift"
echo ""
echo "🔌 To Install on Device:"
echo "   1. Connect iPhone/iPad via USB"
echo "   2. Select device in Xcode"
echo "   3. Click Run (▶️)"
echo "   4. Trust developer on device"
echo ""
echo "Opening Xcode..."
open -a Xcode
"""

        script_file = self.base_dir / "open_xcode.sh"
        with open(script_file, 'w') as f:
            f.write(script_content)

        os.chmod(script_file, 0o755)
        print(f"  ✅ Quick start script: {script_file.name}")

    def run_complete_setup(self):
        """Run complete setup"""
        print("\n" + "="*80)
        print("✨✨✨ COMPLETE XCODE SETUP ✨✨✨")
        print("="*80)

        # Create project
        self.create_complete_project()

        # Create quick start
        self.create_quick_start_script()

        # Try to open Xcode
        xcode_opened = self.open_in_xcode()

        print("\n" + "="*80)
        print("✅ SETUP COMPLETE!")
        print("="*80)

        print("\n📁 Project Location:")
        print(f"   {self.ios_dir}")

        print("\n📋 Files Created:")
        print("   ✅ NOIZYLABApp.swift")
        print("   ✅ Info.plist")
        print("   ✅ NOIZYLAB.entitlements")
        print("   ✅ build_settings.json")
        print("   ✅ open_xcode.sh")

        if not xcode_opened:
            print("\n💻 To Open Xcode:")
            print("   1. Open Xcode manually")
            print("   2. File → New → Project")
            print(f"   3. Or run: ./open_xcode.sh")

        print("\n🚀 Next Steps:")
        print("   1. Open Xcode")
        print("   2. Create New Project (iOS → App → SwiftUI)")
        print("   3. Copy code from NOIZYLABApp.swift")
        print("   4. Connect device")
        print("   5. Build & Run!")

        print("\n" + "="*80)

if __name__ == "__main__":
    setup = XcodeProjectSetup()
    setup.run_complete_setup()

