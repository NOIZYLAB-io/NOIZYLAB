#!/usr/bin/env python3
"""
Auto-Save + Run On Save Demo
This file demonstrates VS Code auto-save with automatic command execution.
"""

import datetime
import os

def main():
    print("🚀 Auto-Save + Run On Save Demo")
    print("=" * 40)
    print(f"⏰ Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"📄 File: {__file__}")
    print()
    print("✨ This script runs automatically when you save the file!")
    print("💡 Try editing this file and saving - it will auto-run!")
    print()
    
    # Try changing this message and save the file to see it run automatically
    message = "Hello from auto-executed Python!"
    print(f"💬 Message: {message}")

if __name__ == "__main__":
    main()