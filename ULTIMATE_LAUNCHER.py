#!/usr/bin/env python3
"""
Ultimate System Launcher - Python version that avoids path issues
"""

import os
import subprocess
import sys
from pathlib import Path

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")

def show_menu():
    """Display main menu"""
    print("\n" + "=" * 80)
    print(" " * 25 + "🚀 ULTIMATE SYSTEM CONTROL CENTER")
    print("=" * 80)
    print("\n📊 DASHBOARD & MONITORING")
    print("  1) Unified Dashboard          - Complete system overview")
    print("  2) Health Monitor             - Project health check")
    print("  3) Performance Monitor        - System performance")
    print("\n🤖 AUTOMATION & WORKFLOWS")
    print("  4) Automation Setup           - Setup automation")
    print("  5) List Workflows             - Show workflows")
    print("  6) Run Workflow               - Execute workflow")
    print("\n📁 ORGANIZATION")
    print("  7) Organize NOIZYLAB          - Clean & organize")
    print("  8) Analyze _ORGANIZED         - Analyze organized")
    print("  9) Smart Migrator             - Archive/restore projects")
    print("\n🔍 ANALYSIS")
    print("  10) Find Archive Candidates   - Find inactive projects")
    print("  11) Check Agents              - Check running processes")
    print("  12) Disk Usage Analyzer       - Analyze disk usage")
    print("\n📚 DOCUMENTATION")
    print("  13) Quick Reference           - Command reference")
    print("  14) View Status               - System status")
    print("\n  0) Exit")
    print("=" * 80)

def run_command(command):
    """Run a command"""
    os.chdir(str(NOIZYLAB))
    
    if command == "1":
        if (NOIZYLAB / "UNIFIED_DASHBOARD.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "UNIFIED_DASHBOARD.py")])
        else:
            print("❌ UNIFIED_DASHBOARD.py not found")
    
    elif command == "2":
        if (NOIZYLAB / "HEALTH_MONITOR.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "HEALTH_MONITOR.py")])
        else:
            print("❌ HEALTH_MONITOR.py not found")
    
    elif command == "3":
        if (NOIZYLAB / "PERFORMANCE_MONITOR.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "PERFORMANCE_MONITOR.py")])
        else:
            print("❌ PERFORMANCE_MONITOR.py not found")
    
    elif command == "4":
        if (NOIZYLAB / "ADVANCED_AUTOMATION.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "ADVANCED_AUTOMATION.py"), "setup"])
        else:
            print("❌ ADVANCED_AUTOMATION.py not found")
    
    elif command == "5":
        if (NOIZYLAB / "ADVANCED_AUTOMATION.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "ADVANCED_AUTOMATION.py"), "workflows"])
        else:
            print("❌ ADVANCED_AUTOMATION.py not found")
    
    elif command == "6":
        workflow = input("Enter workflow name: ").strip()
        if workflow and (NOIZYLAB / "ADVANCED_AUTOMATION.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "ADVANCED_AUTOMATION.py"), "run", workflow])
        else:
            print("❌ Workflow name required or file not found")
    
    elif command == "7":
        if (NOIZYLAB / "FAST_CLEANUP.sh").exists():
            subprocess.run(["bash", str(NOIZYLAB / "FAST_CLEANUP.sh")])
        elif (NOIZYLAB / "QUICK_ORGANIZE.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "QUICK_ORGANIZE.py")])
        else:
            print("❌ Cleanup tools not found")
    
    elif command == "8":
        if ORGANIZED.exists() and (ORGANIZED / "ANALYZE_ORGANIZED.py").exists():
            subprocess.run([sys.executable, str(ORGANIZED / "ANALYZE_ORGANIZED.py")])
        else:
            print(f"❌ _ORGANIZED not found or ANALYZE_ORGANIZED.py missing")
    
    elif command == "9":
        if (NOIZYLAB / "SMART_MIGRATOR.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "SMART_MIGRATOR.py"), "find", "90"])
        else:
            print("❌ SMART_MIGRATOR.py not found")
    
    elif command == "10":
        if (NOIZYLAB / "SMART_MIGRATOR.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "SMART_MIGRATOR.py"), "find", "90"])
        else:
            print("❌ SMART_MIGRATOR.py not found")
    
    elif command == "11":
        if (NOIZYLAB / "CHECK_AGENTS.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "CHECK_AGENTS.py")])
        else:
            print("❌ CHECK_AGENTS.py not found")
    
    elif command == "12":
        if (NOIZYLAB / "IMPROVED_DISK_ANALYZER.py").exists():
            subprocess.run([sys.executable, str(NOIZYLAB / "IMPROVED_DISK_ANALYZER.py")])
        else:
            print("❌ IMPROVED_DISK_ANALYZER.py not found")
    
    elif command == "13":
        ref_file = NOIZYLAB / "QUICK_REFERENCE.md"
        if ref_file.exists():
            with open(ref_file) as f:
                print(f.read())
        else:
            print("📚 Quick Reference not found. Here are key commands:")
            print("\n  python3 UNIFIED_DASHBOARD.py")
            print("  python3 HEALTH_MONITOR.py")
            print("  python3 ADVANCED_AUTOMATION.py setup")
            print("  python3 SMART_MIGRATOR.py find 90")
    
    elif command == "14":
        print("\n📊 System Status:")
        print("=" * 80)
        print(f"\nNOIZYLAB: {'✅ Found' if NOIZYLAB.exists() else '❌ Not found'}")
        print(f"_ORGANIZED: {'✅ Found' if ORGANIZED.exists() else '❌ Not found'}")
        
        # Check key files
        key_files = [
            "UNIFIED_DASHBOARD.py",
            "HEALTH_MONITOR.py",
            "ADVANCED_AUTOMATION.py",
            "SMART_MIGRATOR.py",
            "ULTIMATE_SYSTEM.sh"
        ]
        
        print("\n📁 Key Files:")
        for file in key_files:
            status = "✅" if (NOIZYLAB / file).exists() else "❌"
            print(f"  {status} {file}")
        
        print()
    
    else:
        print("❌ Invalid option")

def main():
    """Main loop"""
    if len(sys.argv) > 1:
        # Direct command execution
        run_command(sys.argv[1])
        return
    
    # Interactive menu
    while True:
        show_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == "0" or choice.lower() in ["q", "exit", "quit"]:
            print("\n👋 Goodbye!")
            break
        
        if choice:
            print()
            run_command(choice)
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

