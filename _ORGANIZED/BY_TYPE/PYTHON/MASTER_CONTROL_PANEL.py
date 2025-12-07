#!/usr/bin/env python3
"""
🎛️ MASTER CONTROL PANEL 🎛️

Central hub for all WAV organization tools!

⭐⭐⭐ HARD RULE ENFORCED EVERYWHERE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!
"""

import sys
from pathlib import Path

def show_banner():
    """Display banner"""
    print("="*80)
    print("🎛️ MASTER CONTROL PANEL - WAV ORGANIZATION SYSTEM 🎛️")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
    print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!")
    print("\n" + "="*80 + "\n")

def show_menu():
    """Show main menu"""
    print("QUICK ACTIONS:")
    print("-" * 80)
    print("  1. ⚡ TURBO Organize (5-10s) - Fastest folder organization")
    print("  2. 🤖 AI Organize (30s) - Smart categorization + analysis")
    print("  3. 🗄️  6TB Full Scan (30m) - Scan entire drive")
    print()
    print("ADVANCED:")
    print("-" * 80)
    print("  4. 📊 MEGA Organize - Full featured analysis")
    print("  5. 💾 Auto Backup - Backup originals to multiple locations")
    print("  6. 👁️  File Monitor - Real-time auto-organization")
    print("  7. 🔍 6TB Query - Search database")
    print("  8. 🔨 6TB Rebuild - Rebuild organized structure")
    print()
    print("UTILITIES:")
    print("-" * 80)
    print("  9. 📈 Quick Stats - View collection overview")
    print(" 10. 👁️  Preview - Safe preview (no changes)")
    print(" 11. 💾 Backup Check - Check backup status")
    print(" 12. 📊 Generate Reports - Create all reports")
    print()
    print("DOCUMENTATION:")
    print("-" * 80)
    print(" 13. 📚 View Guide - Open complete system guide")
    print(" 14. 🎯 Execution Guide - How to run everything")
    print(" 15. ⚡ Speed Comparison - Compare all tools")
    print()
    print(" 0. Exit")
    print()
    print("="*80)

def execute_choice(choice):
    """Execute selected option"""
    
    if choice == '1':
        print("\n⚡ Launching TURBO ORGANIZER...")
        import TURBO_ORGANIZER
        TURBO_ORGANIZER.main()
    
    elif choice == '2':
        print("\n🤖 Launching AI ORGANIZER...")
        try:
            import ADVANCED_AI_ORGANIZER
            ADVANCED_AI_ORGANIZER.ai_organize()
        except ImportError:
            print("❌ NumPy required for AI features")
            print("Install: pip install numpy")
    
    elif choice == '3':
        print("\n🗄️  Launching 6TB SCANNER...")
        print("This will take 20-40 minutes. Continue? (y/n): ", end='')
        if input().lower() == 'y':
            import importlib.util
            spec = importlib.util.spec_from_file_location("scanner", "6TB_SCANNER.py")
            scanner = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(scanner)
            scanner.main()
    
    elif choice == '4':
        print("\n📊 Launching MEGA ORGANIZER...")
        import MEGA_ULTIMATE_ORGANIZER
        MEGA_ULTIMATE_ORGANIZER.main()
    
    elif choice == '5':
        print("\n💾 Launching AUTO BACKUP...")
        import AUTO_BACKUP_SYSTEM
        AUTO_BACKUP_SYSTEM.run_backup_system()
    
    elif choice == '6':
        print("\n👁️  Launching FILE MONITOR...")
        import FILE_MONITOR
        FILE_MONITOR.monitor_continuous()
    
    elif choice == '7':
        print("\n🔍 Launching 6TB QUERY...")
        import importlib.util
        spec = importlib.util.spec_from_file_location("query", "6TB_QUERY.py")
        query = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(query)
        query.menu()
    
    elif choice == '8':
        print("\n🔨 Launching 6TB REBUILD...")
        import importlib.util
        spec = importlib.util.spec_from_file_location("rebuild", "6TB_REBUILD.py")
        rebuild = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rebuild)
        rebuild.rebuild_structure()
    
    elif choice == '9':
        print("\n📈 Quick Stats...")
        import quick_stats
        quick_stats.get_quick_stats()
    
    elif choice == '10':
        print("\n👁️  Preview Mode...")
        import preview_organization
        # Would need to import and run
        print("Run: python3 preview_organization.py")
    
    elif choice == '11':
        print("\n💾 Backup Check...")
        import AUTO_BACKUP_SYSTEM
        AUTO_BACKUP_SYSTEM.quick_backup_check()
    
    elif choice == '12':
        print("\n📊 Generating reports...")
        print("Run MEGA or 6TB organizers to generate reports")
    
    elif choice == '13':
        guide = Path("🎉_COMPLETE_SYSTEM_GUIDE.md")
        if guide.exists():
            import subprocess
            subprocess.run(['open', str(guide)])
            print("✓ Opened guide")
        else:
            print("Guide not found")
    
    elif choice == '14':
        guide = Path("🎯_EXECUTION_GUIDE.md")
        if guide.exists():
            import subprocess
            subprocess.run(['open', str(guide)])
            print("✓ Opened execution guide")
        else:
            print("Guide not found")
    
    elif choice == '15':
        guide = Path("SPEED_COMPARISON.md")
        if guide.exists():
            import subprocess
            subprocess.run(['open', str(guide)])
            print("✓ Opened speed comparison")
        else:
            print("Guide not found")
    
    elif choice == '0':
        print("\nGoodbye!")
        sys.exit(0)
    
    else:
        print("\n❌ Invalid choice!")

def main():
    """Main control panel loop"""
    while True:
        show_banner()
        show_menu()
        
        choice = input("Enter choice (0-15): ").strip()
        
        try:
            execute_choice(choice)
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted!")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
        
        print("\n\nPress Enter to return to menu...")
        input()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")

