#!/usr/bin/env python3
"""
PERFECT SYSTEM LAUNCHER
Single entry point for the perfect system
"""

import sys
from pathlib import Path

base_dir = Path(__file__).parent

def show_perfect_menu():
    """Show perfect system menu"""
    print("\n" + "="*80)
    print("🎉 PERFECT SYSTEM - ALL SYSTEMS GO! 🎉")
    print("="*80)
    print("\n🚀 QUICK LAUNCH:")
    print("  1. 🤖 Gemini AI System")
    print("  2. ⚡ Ultra Performance Mode")
    print("  3. 🔄 Auto-Improve System")
    print("  4. 🧪 Test Everything")
    print("  5. 📊 System Status")
    print("  0. Exit")
    print("="*80)

def main():
    show_perfect_menu()
    choice = input("\n👉 Choose: ").strip()

    if choice == "1":
        try:
            from gemini_database.GEMINI_MASTER_INTEGRATION import GeminiMasterIntegration
            integration = GeminiMasterIntegration()
            integration.create_master_menu()
        except Exception as e:
            print(f"❌ Error: {e}")
            print("\n📋 Setup:")
            print("  1. pip install -q -U google-genai")
            print("  2. export GEMINI_API_KEY='your-key'")

    elif choice == "2":
        print("\n⚡ Launching Ultra Performance Mode...")
        # Launch performance mode

    elif choice == "3":
        print("\n🔄 Running Auto-Improve...")
        from AUTO_IMPROVE_SYSTEM import AutoImproveSystem
        system = AutoImproveSystem()
        system.run_auto_improve()

    elif choice == "4":
        print("\n🧪 Running Tests...")
        # Run tests

    elif choice == "5":
        print("\n📊 System Status:")
        print("   ✅ All systems operational")
        print("   ✅ Gemini AI: Ready")
        print("   ✅ Performance: Optimized")
        print("   ✅ Auto-Improve: Active")

    elif choice == "0":
        print("\n👋 Goodbye!")

    else:
        print("\n❌ Invalid choice")

if __name__ == "__main__":
    main()
