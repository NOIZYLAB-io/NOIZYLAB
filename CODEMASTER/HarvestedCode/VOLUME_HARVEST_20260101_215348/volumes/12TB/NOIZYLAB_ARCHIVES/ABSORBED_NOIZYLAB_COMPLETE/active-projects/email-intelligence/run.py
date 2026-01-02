#!/usr/bin/env python3
"""
NoizyLab Email Intelligence - Main Entry Point
==============================================
Convenient entry point script for running the system
"""

import sys
import os
from pathlib import Path

# Add project root to path
_project_root = Path(__file__).parent
sys.path.insert(0, str(_project_root))

def show_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("  📧 NoizyLab Email Intelligence System")
    print("="*60)
    print("\nSelect an option:")
    print()
    print("  [1] Main CLI Application (NoizyLab CORE)")
    print("  [2] Email Intelligence CLI V2")
    print("  [3] Email CLI")
    print("  [4] API Server (v2.0)")
    print("  [5] API Server (v3.0 Enhanced)")
    print("  [6] API Server (v4.0 Enterprise)")
    print("  [7] Dashboard")
    print("  [8] Email Account Setup")
    print()
    print("  [Q] Quit")
    print()

def main():
    """Main entry point"""
    while True:
        show_menu()
        choice = input("Enter choice: ").strip().upper()
        
        if choice == 'Q':
            print("\n👋 Goodbye!\n")
            break
        elif choice == '1':
            os.chdir(_project_root / "core")
            os.system(f"{sys.executable} main.py")
        elif choice == '2':
            os.chdir(_project_root / "core")
            os.system(f"{sys.executable} email_intelligence_v2.py")
        elif choice == '3':
            os.chdir(_project_root / "core")
            os.system(f"{sys.executable} email_cli.py")
        elif choice == '4':
            os.chdir(_project_root / "api")
            os.system(f"{sys.executable} api_server.py")
        elif choice == '5':
            os.chdir(_project_root / "api")
            os.system(f"{sys.executable} api_server_v3.py")
        elif choice == '6':
            os.chdir(_project_root / "api")
            os.system(f"{sys.executable} api_server_v4.py")
        elif choice == '7':
            os.chdir(_project_root / "dashboards")
            os.system("./start_dashboard.sh")
        elif choice == '8':
            os.chdir(_project_root / "scripts")
            os.system(f"{sys.executable} setup-email-accounts.py")
        else:
            print("\n❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)

