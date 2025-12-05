#!/usr/bin/env python3
"""
MASTER CONTROL - Central hub for all file management tools
One script to rule them all!
"""

import os
import sys
import subprocess
import time
from pathlib import Path

ROOT = '/Volumes/MAG 4TB'
TOOLS_DIR = '/Volumes/MAG 4TB/NoizyWorkspace/noizyfish_aquarium/PY'

BANNER = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║            🚀 NOIZY FILE MANAGEMENT SUITE v2.0 🚀             ║
║                                                               ║
║              Master Control - All Tools Unified               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

MENU = """
═══════════════════════════════════════════════════════════════

SCANNING & ANALYSIS
  1. Ultra-Fast Scan (Shell-based, ~10 min)
  2. Advanced Scan (Python, deep analysis, ~30 min)
  3. Storage Analysis

CLEANUP OPERATIONS
  4. Clean Empty Directories
  5. Clean Exact Duplicates
  6. Review Suspicious Files
  7. Full Cleanup Suite

ORGANIZATION
  8. Analyze File Organization
  9. Auto-Organize Files
 10. Smart Rename Files

MAINTENANCE
 11. Generate Report
 12. View Previous Scans
 13. Backup Configuration

POWER OPTIONS
 14. Run ALL Scans
 15. Run ALL Cleanup
 16. Full Optimization (Scan + Clean + Organize)

═══════════════════════════════════════════════════════════════
 0. Exit

Enter choice (0-16): """

def run_command(cmd, description):
    """Run a command and display progress"""
    print(f"\n{'='*70}")
    print(f"  {description}")
    print(f"{'='*70}\n")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=False, text=True)
        elapsed = time.time() - start_time
        print(f"\n✅ Completed in {elapsed:.1f} seconds")
        return True
    except subprocess.CalledProcessError as e:
        elapsed = time.time() - start_time
        print(f"\n❌ Error after {elapsed:.1f} seconds")
        print(f"   {str(e)}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        return False

def ultra_fast_scan():
    """Run ultra-fast shell scan"""
    cmd = f'bash "{TOOLS_DIR}/ultra_fast_scan.sh"'
    return run_command(cmd, "ULTRA-FAST SCAN (Shell)")

def advanced_scan():
    """Run advanced Python scan"""
    cmd = f'cd "{TOOLS_DIR}" && python3 advanced_file_scanner.py'
    return run_command(cmd, "ADVANCED DEEP SCAN (Python)")

def storage_analysis():
    """Run storage analysis"""
    cmd = f'python3 "{TOOLS_DIR}/smart_cleanup.py" --analyze'
    return run_command(cmd, "STORAGE ANALYSIS")

def clean_empty_dirs(live=False):
    """Clean empty directories"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_cleanup.py" --empty-dirs {mode}'
    return run_command(cmd, f"CLEAN EMPTY DIRECTORIES ({'LIVE' if live else 'DRY RUN'})")

def clean_duplicates(live=False):
    """Clean exact duplicates"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_cleanup.py" --duplicates {mode}'
    return run_command(cmd, f"CLEAN EXACT DUPLICATES ({'LIVE' if live else 'DRY RUN'})")

def review_suspicious(live=False):
    """Review suspicious files"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_cleanup.py" --suspicious {mode}'
    return run_command(cmd, f"REVIEW SUSPICIOUS FILES ({'LIVE' if live else 'DRY RUN'})")

def full_cleanup(live=False):
    """Run full cleanup suite"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_cleanup.py" --all {mode}'
    return run_command(cmd, f"FULL CLEANUP SUITE ({'LIVE' if live else 'DRY RUN'})")

def analyze_organization():
    """Analyze file organization"""
    cmd = f'python3 "{TOOLS_DIR}/smart_organizer.py" --analyze'
    return run_command(cmd, "ANALYZE FILE ORGANIZATION")

def auto_organize(live=False):
    """Auto-organize files"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_organizer.py" --organize {mode}'
    return run_command(cmd, f"AUTO-ORGANIZE FILES ({'LIVE' if live else 'DRY RUN'})")

def smart_rename(live=False):
    """Smart rename files"""
    mode = "--live" if live else ""
    cmd = f'python3 "{TOOLS_DIR}/smart_organizer.py" --rename {mode}'
    return run_command(cmd, f"SMART RENAME FILES ({'LIVE' if live else 'DRY RUN'})")

def generate_report():
    """Generate comprehensive report"""
    print("\n" + "="*70)
    print("  GENERATING COMPREHENSIVE REPORT")
    print("="*70)
    
    report_path = '/Volumes/MAG 4TB/NoizyWorkspace/MASTER_REPORT.txt'
    
    with open(report_path, 'w') as f:
        f.write("NOIZY FILE MANAGEMENT SUITE - MASTER REPORT\n")
        f.write("="*70 + "\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Root: {ROOT}\n")
        f.write("="*70 + "\n\n")
        
        # Check for existing reports
        workspace = '/Volumes/MAG 4TB/NoizyWorkspace'
        
        reports = {
            'Scan Results': f'{workspace}/scan_results.txt',
            'Advanced Scan': f'{workspace}/advanced_scan_report.json',
            'Cleanup Log': f'{workspace}/cleanup_log.json',
            'Deleted Folders': f'{workspace}/deleted_empty_folders.log'
        }
        
        for name, path in reports.items():
            f.write(f"\n### {name} ###\n")
            if os.path.exists(path):
                f.write(f"Location: {path}\n")
                f.write(f"Size: {os.path.getsize(path)} bytes\n")
                f.write(f"Modified: {time.ctime(os.path.getmtime(path))}\n")
            else:
                f.write("Not generated yet\n")
    
    print(f"\n✅ Report saved to: {report_path}")
    print("\nOpening report...")
    os.system(f'open "{report_path}"')
    return True

def view_previous_scans():
    """View previous scan results"""
    workspace = '/Volumes/MAG 4TB/NoizyWorkspace'
    
    print("\n" + "="*70)
    print("  PREVIOUS SCAN RESULTS")
    print("="*70 + "\n")
    
    files = [
        'scan_results.txt',
        'advanced_scan_report.json',
        'cleanup_log.json',
        'deleted_empty_folders.log',
        'scan_output.log'
    ]
    
    for f in files:
        path = os.path.join(workspace, f)
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            mtime = time.ctime(os.path.getmtime(path))
            print(f"  📄 {f}")
            print(f"     Size: {size_kb:.2f} KB")
            print(f"     Modified: {mtime}")
            print(f"     Path: {path}")
            print()
    
    input("\nPress Enter to continue...")
    return True

def run_all_scans():
    """Run all scanning operations"""
    print("\n" + "="*70)
    print("  🚀 RUNNING ALL SCANS")
    print("="*70)
    
    tasks = [
        ("Ultra-Fast Scan", ultra_fast_scan),
        ("Advanced Scan", advanced_scan),
        ("Storage Analysis", storage_analysis)
    ]
    
    for name, func in tasks:
        print(f"\n\n▶️  Starting: {name}")
        if not func():
            print(f"⚠️  {name} failed, continuing...")
        time.sleep(1)
    
    print("\n" + "="*70)
    print("  ✅ ALL SCANS COMPLETE")
    print("="*70)
    return True

def run_all_cleanup():
    """Run all cleanup operations"""
    print("\n" + "="*70)
    print("  🧹 RUNNING ALL CLEANUP (DRY RUN)")
    print("="*70)
    
    response = input("\nRun in LIVE mode? (yes/no): ")
    live = response.lower() == 'yes'
    
    if live:
        confirm = input("⚠️  CONFIRM: This will modify files. Type 'CONFIRM': ")
        if confirm != 'CONFIRM':
            print("Cancelled.")
            return False
    
    tasks = [
        ("Clean Empty Directories", lambda: clean_empty_dirs(live)),
        ("Review Suspicious Files", lambda: review_suspicious(live)),
    ]
    
    for name, func in tasks:
        print(f"\n\n▶️  Starting: {name}")
        if not func():
            print(f"⚠️  {name} failed, continuing...")
        time.sleep(1)
    
    print("\n" + "="*70)
    print("  ✅ ALL CLEANUP COMPLETE")
    print("="*70)
    return True

def full_optimization():
    """Run full optimization pipeline"""
    print("\n" + "="*70)
    print("  🌟 FULL OPTIMIZATION PIPELINE")
    print("="*70)
    print("\nThis will run:")
    print("  1. All scans")
    print("  2. All cleanup (dry run)")
    print("  3. Organization analysis")
    print("  4. Generate report")
    print("\nEstimated time: 1-2 hours")
    
    response = input("\nProceed? (yes/no): ")
    if response.lower() != 'yes':
        return False
    
    # Run pipeline
    steps = [
        ("Scanning", run_all_scans),
        ("Cleanup", run_all_cleanup),
        ("Organization Analysis", analyze_organization),
        ("Report Generation", generate_report)
    ]
    
    start_time = time.time()
    
    for name, func in steps:
        print(f"\n\n{'='*70}")
        print(f"  PIPELINE STEP: {name}")
        print(f"{'='*70}")
        
        if not func():
            print(f"\n⚠️  {name} failed, stopping pipeline")
            return False
        
        time.sleep(2)
    
    elapsed = time.time() - start_time
    
    print("\n\n" + "="*70)
    print("  🎉 FULL OPTIMIZATION COMPLETE!")
    print("="*70)
    print(f"\nTotal time: {elapsed/60:.1f} minutes")
    return True

def main():
    """Main menu loop"""
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print(BANNER)
        
        choice = input(MENU).strip()
        
        if choice == '0':
            print("\n👋 Goodbye!")
            break
        
        elif choice == '1':
            ultra_fast_scan()
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            advanced_scan()
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            storage_analysis()
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            response = input("Run in LIVE mode? (yes/no): ")
            clean_empty_dirs(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '5':
            response = input("Run in LIVE mode? (yes/no): ")
            clean_duplicates(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '6':
            response = input("Run in LIVE mode? (yes/no): ")
            review_suspicious(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '7':
            response = input("Run in LIVE mode? (yes/no): ")
            full_cleanup(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '8':
            analyze_organization()
            input("\nPress Enter to continue...")
        
        elif choice == '9':
            response = input("Run in LIVE mode? (yes/no): ")
            auto_organize(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '10':
            response = input("Run in LIVE mode? (yes/no): ")
            smart_rename(live=(response.lower() == 'yes'))
            input("\nPress Enter to continue...")
        
        elif choice == '11':
            generate_report()
            input("\nPress Enter to continue...")
        
        elif choice == '12':
            view_previous_scans()
        
        elif choice == '13':
            print("\n⚠️  Backup not implemented yet")
            input("\nPress Enter to continue...")
        
        elif choice == '14':
            run_all_scans()
            input("\nPress Enter to continue...")
        
        elif choice == '15':
            run_all_cleanup()
            input("\nPress Enter to continue...")
        
        elif choice == '16':
            full_optimization()
            input("\nPress Enter to continue...")
        
        else:
            print("\n❌ Invalid choice")
            time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)

