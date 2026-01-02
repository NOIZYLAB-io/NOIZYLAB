#!/usr/bin/env python3
"""
NOIZYGENIE Progress Monitor Dashboard
Real-time tracking of all VS Code tasks and operations
"""

import os
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime
import threading
import sys
sys.path.append('/Users/rsp_ms')
from palatino_terminal import PalatinoTerminal

class ProgressMonitor:
    def __init__(self):
        self.pt = PalatinoTerminal()
        self.kontakt_lab = Path.home() / "Desktop" / "KONTAKT_LAB"
        self.reports_dir = self.kontakt_lab / "REPORTS"
        self.six_tb = Path("/Volumes/6TB")
        self.ni_2026 = self.six_tb / "Native_Instruments_2026"
        
        # Progress tracking
        self.active_tasks = {}
        self.completed_tasks = {}
        self.task_history = []
        
        # File locations to monitor
        self.monitor_locations = {
            "KONTAKT_LAB": self.kontakt_lab,
            "6TB_Native_Instruments": self.six_tb / "Native Instruments",
            "Native_Instruments_2026": self.ni_2026,
            "BFA_Libraries": self.six_tb / "BFA Libraries",
            "Quality_Check_Logs": self.reports_dir / "quality_checks"
        }
        
    def get_terminal_processes(self):
        """Get all running terminal processes related to NOIZYGENIE"""
        try:
            # Get VS Code terminal processes
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            processes = []
            
            for line in result.stdout.split('\n'):
                if any(keyword in line.lower() for keyword in [
                    'python3', 'quality_check', 'migration', 'noizygenie', 
                    'library', 'organization', 'repair'
                ]):
                    processes.append(line.strip())
            
            return processes
        except Exception as e:
            return [f"Error getting processes: {e}"]
    
    def check_task_progress(self):
        """Check progress of various NOIZYGENIE tasks"""
        progress_report = {}
        
        # 1. Check KONTAKT_LAB organization status
        if self.kontakt_lab.exists():
            organized_dirs = len([d for d in self.kontakt_lab.iterdir() 
                                if d.is_dir() and d.name.startswith(('01_', '02_', '03_'))])
            total_files = sum(1 for f in self.kontakt_lab.rglob("*") if f.is_file())
            
            progress_report["KONTAKT_LAB_Organization"] = {
                "status": "✅ COMPLETE" if organized_dirs > 0 else "⏳ IN PROGRESS",
                "organized_categories": organized_dirs,
                "total_files": total_files,
                "last_update": datetime.now().strftime('%H:%M:%S')
            }
        
        # 2. Check Native Instruments 2026 migration
        if self.ni_2026.exists():
            ni_2026_libs = len(list(self.ni_2026.rglob("*Library*")))
            ni_2026_size = sum(f.stat().st_size for f in self.ni_2026.rglob("*") if f.is_file())
            
            progress_report["NI_2026_Migration"] = {
                "status": "⏳ IN PROGRESS" if ni_2026_libs > 0 else "⭕ PENDING",
                "libraries_migrated": ni_2026_libs,
                "total_size_gb": round(ni_2026_size / (1024**3), 2),
                "last_update": datetime.now().strftime('%H:%M:%S')
            }
        
        # 3. Check BFA Libraries status
        bfa_path = self.six_tb / "BFA Libraries"
        if bfa_path.exists():
            bfa_libs = len([d for d in bfa_path.iterdir() if d.is_dir()])
            
            progress_report["BFA_Libraries"] = {
                "status": "📊 DISCOVERED",
                "total_libraries": bfa_libs,
                "location": str(bfa_path),
                "last_update": datetime.now().strftime('%H:%M:%S')
            }
        
        # 4. Check quality check logs
        quality_logs = self.reports_dir / "quality_checks"
        if quality_logs.exists():
            recent_logs = len([f for f in quality_logs.iterdir() 
                             if f.is_file() and 
                             (datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)).seconds < 3600])
            
            progress_report["Quality_Checks"] = {
                "status": "🔍 ACTIVE" if recent_logs > 0 else "💤 IDLE",
                "recent_checks": recent_logs,
                "log_location": str(quality_logs),
                "last_update": datetime.now().strftime('%H:%M:%S')
            }
        
        return progress_report
    
    def monitor_file_operations(self):
        """Monitor file operations across all locations"""
        file_stats = {}
        
        for location_name, location_path in self.monitor_locations.items():
            if location_path.exists():
                try:
                    # Count files and directories
                    total_files = sum(1 for f in location_path.rglob("*") if f.is_file())
                    total_dirs = sum(1 for d in location_path.rglob("*") if d.is_dir())
                    
                    # Calculate total size
                    total_size = sum(f.stat().st_size for f in location_path.rglob("*") 
                                   if f.is_file() and f.exists())
                    
                    file_stats[location_name] = {
                        "files": total_files,
                        "directories": total_dirs,
                        "size_gb": round(total_size / (1024**3), 2),
                        "path": str(location_path),
                        "last_modified": max([f.stat().st_mtime for f in location_path.rglob("*") 
                                            if f.is_file() and f.exists()], default=0)
                    }
                except Exception as e:
                    file_stats[location_name] = {"error": str(e)}
        
        return file_stats
    
    def display_live_dashboard(self):
        """Display real-time progress dashboard"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        self.pt.header("NOIZYGENIE PROGRESS MONITOR DASHBOARD")
        print(f"🕐 Live Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Task Progress Section
        self.pt.subheader("Active Task Progress")
        task_progress = self.check_task_progress()
        
        for task_name, task_info in task_progress.items():
            status = task_info.get('status', 'UNKNOWN')
            print(f"   {status} {task_name.replace('_', ' ')}")
            
            for key, value in task_info.items():
                if key != 'status':
                    print(f"      📊 {key.replace('_', ' ').title()}: {value}")
            print()
        
        # File Operations Section
        self.pt.subheader("File System Monitoring")
        file_stats = self.monitor_file_operations()
        
        for location, stats in file_stats.items():
            if 'error' not in stats:
                print(f"   📁 {location.replace('_', ' ')}")
                print(f"      Files: {stats['files']:,} | Dirs: {stats['directories']:,} | Size: {stats['size_gb']} GB")
                print(f"      Path: {stats['path']}")
                
                # Show recent activity
                if stats['last_modified'] > 0:
                    mod_time = datetime.fromtimestamp(stats['last_modified'])
                    time_diff = datetime.now() - mod_time
                    if time_diff.seconds < 300:  # 5 minutes
                        print(f"      🔥 Recent Activity: {time_diff.seconds}s ago")
                print()
        
        # Running Processes Section
        self.pt.subheader("Active Python Processes")
        processes = self.get_terminal_processes()
        
        if processes:
            for i, process in enumerate(processes[:5], 1):  # Show top 5
                if 'python3' in process.lower():
                    print(f"   {i}. {process[:80]}...")
        else:
            print("   💤 No active NOIZYGENIE processes detected")
        
        print(f"\n{'─' * 70}")
        print(f"⏰ Dashboard refreshes every 5 seconds | Press Ctrl+C to exit")
    
    def continuous_monitoring(self, refresh_interval=5):
        """Run continuous monitoring dashboard"""
        try:
            while True:
                self.display_live_dashboard()
                time.sleep(refresh_interval)
        except KeyboardInterrupt:
            print(f"\n\n✅ Progress monitoring stopped.")
            self.pt.timestamp()
    
    def generate_progress_report(self):
        """Generate detailed progress report"""
        report_file = self.reports_dir / f"progress_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.reports_dir.mkdir(exist_ok=True, parents=True)
        
        with open(report_file, 'w') as f:
            f.write("🎹 NOIZYGENIE PROGRESS REPORT\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Task progress
            f.write("TASK PROGRESS:\n")
            f.write("-" * 20 + "\n")
            task_progress = self.check_task_progress()
            for task, info in task_progress.items():
                f.write(f"\n{task}:\n")
                for key, value in info.items():
                    f.write(f"  {key}: {value}\n")
            
            # File statistics
            f.write(f"\nFILE SYSTEM STATUS:\n")
            f.write("-" * 20 + "\n")
            file_stats = self.monitor_file_operations()
            for location, stats in file_stats.items():
                f.write(f"\n{location}:\n")
                for key, value in stats.items():
                    f.write(f"  {key}: {value}\n")
        
        self.pt.success(f"Progress report saved: {report_file.name}")
        return report_file

def main():
    """Main function with options"""
    monitor = ProgressMonitor()
    
    print("🎹 NOIZYGENIE Progress Monitor")
    print("=" * 40)
    print("1. Live Dashboard (continuous)")
    print("2. Single Status Check")
    print("3. Generate Progress Report")
    print("4. BFA Libraries Scan")
    
    try:
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            print("\n🔄 Starting live dashboard... (Press Ctrl+C to stop)")
            time.sleep(2)
            monitor.continuous_monitoring()
            
        elif choice == "2":
            monitor.display_live_dashboard()
            
        elif choice == "3":
            report_file = monitor.generate_progress_report()
            print(f"\n📄 Report generated: {report_file}")
            
        elif choice == "4":
            bfa_path = Path("/Volumes/6TB/BFA Libraries")
            if bfa_path.exists():
                bfa_libs = [d.name for d in bfa_path.iterdir() if d.is_dir()]
                print(f"\n📚 BFA Libraries Found ({len(bfa_libs)}):")
                for i, lib in enumerate(bfa_libs[:20], 1):  # Show first 20
                    print(f"   {i:2d}. {lib}")
                if len(bfa_libs) > 20:
                    print(f"   ... and {len(bfa_libs) - 20} more libraries")
            else:
                print("\n❌ BFA Libraries folder not found")
                
        else:
            print("Invalid choice")
            
    except KeyboardInterrupt:
        print("\n\n✅ Exiting...")

if __name__ == "__main__":
    main()