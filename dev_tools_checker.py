#!/usr/bin/env python3
"""
Developer Tools Checker for macOS
- Checks for Xcode, Swift (SPM), CocoaPods, and Apple Configurator 2
- Prints versions and installation hints
"""

import subprocess
import shutil
import os

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return None

def check_xcode():
    print("🔍 Checking Xcode...")
    out = run_cmd(["xcodebuild", "-version"])
    if out:
        print("✅ Xcode found:\n" + out)
    else:
        print("❌ Xcode not found. Install from the Mac App Store.")

def check_swift():
    print("\n🔍 Checking Swift / Swift Package Manager...")
    out = run_cmd(["swift", "--version"])
    if out:
        print("✅ Swift toolchain found:\n" + out)
        print("ℹ️ Swift Package Manager is included with Swift.")
    else:
        print("❌ Swift not found. Install Xcode from the Mac App Store.")

def check_cocoapods():
    print("\n🔍 Checking CocoaPods...")
    pod_path = shutil.which("pod")
    if pod_path:
        out = run_cmd(["pod", "--version"])
        print(f"✅ CocoaPods found at {pod_path}, version {out}")
    else:
        print("❌ CocoaPods not found. Install with:\n   sudo gem install cocoapods")

def check_configurator():
    print("\n🔍 Checking Apple Configurator 2...")
    out = run_cmd(["mdfind", "kMDItemCFBundleIdentifier == 'com.apple.configurator.ui'"])
    if out:
        print("✅ Apple Configurator 2 is installed.")
    else:
        print("❌ Apple Configurator 2 not found. Install free from the Mac App Store.")

def main():
    print("=== Developer Tools Environment Check ===\n")
    check_xcode()
    check_swift()
    check_cocoapods()
    check_configurator()
    print("\n✅ Check complete.")

if __name__ == "__main__":
    main()