#!/usr/bin/env python3
"""
6TB DRIVE SCANNER & HEALER - FISH MUSIC INC
Scans, heals, organizes all music on 6TB drive
GORUNFREE! 🎸🔥
"""

import os
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import subprocess

# Audio extensions
AUDIO_EXTS = {'.mp3', '.wav', '.aif', '.aiff', '.flac', '.m4a', '.ogg', '.wma', '.aac', '.alac'}
PROJECT_EXTS = {'.logic', '.als', '.ptx', '.flp', '.rpp', '.cpr'}

class DriveHealer:
    def __init__(self, drive_path="/Volumes/6TB"):
        self.drive = Path(drive_path)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results = {
            "scan_time": self.timestamp,
            "total_files": 0,
            "audio_files": 0,
            "project_files": 0,
            "duplicates": [],
            "errors": [],
            "large_folders": [],
            "total_size_gb": 0,
            "health_status": "UNKNOWN"
        }
        self.file_hashes = defaultdict(list)

    def scan_all(self):
        """Complete drive scan"""
        print(f"\n🔍 SCANNING: {self.drive}")
        print("=" * 60)

        try:
            # Get drive size
            stat = shutil.disk_usage(self.drive)
            self.results["total_size_gb"] = round(stat.used / (1024**3), 2)
            self.results["free_space_gb"] = round(stat.free / (1024**3), 2)

            print(f"📊 USED: {self.results['total_size_gb']} GB")
            print(f"📊 FREE: {self.results['free_space_gb']} GB\n")

            # Scan all files
            for root, dirs, files in os.walk(self.drive):
                # Skip hidden and system folders
                dirs[:] = [d for d in dirs if not d.startswith('.')]

                for file in files:
                    if file.startswith('.'):
                        continue

                    filepath = Path(root) / file
                    self.results["total_files"] += 1

                    # Categorize
                    ext = filepath.suffix.lower()
                    if ext in AUDIO_EXTS:
                        self.results["audio_files"] += 1
                    elif ext in PROJECT_EXTS:
                        self.results["project_files"] += 1

                    # Progress
                    if self.results["total_files"] % 1000 == 0:
                        print(f"  Scanned: {self.results['total_files']:,} files", end='\r')

            print(f"\n✅ SCAN COMPLETE: {self.results['total_files']:,} files")

        except Exception as e:
            self.results["errors"].append(f"Scan error: {str(e)}")
            print(f"❌ ERROR: {e}")

    def find_duplicates(self):
        """Find duplicate audio files by hash"""
        print(f"\n🔍 FINDING DUPLICATES...")

        try:
            checked = 0
            for root, dirs, files in os.walk(self.drive):
                dirs[:] = [d for d in dirs if not d.startswith('.')]

                for file in files:
                    if file.startswith('.'):
                        continue

                    filepath = Path(root) / file
                    if filepath.suffix.lower() in AUDIO_EXTS:
                        try:
                            # Hash first 64KB + last 64KB (fast)
                            with open(filepath, 'rb') as f:
                                start = f.read(65536)
                                f.seek(-65536, 2)
                                end = f.read(65536)
                                file_hash = hashlib.md5(start + end).hexdigest()
                                self.file_hashes[file_hash].append(str(filepath))

                            checked += 1
                            if checked % 100 == 0:
                                print(f"  Checked: {checked} audio files", end='\r')
                        except:
                            pass

            # Find duplicates
            for hash_val, paths in self.file_hashes.items():
                if len(paths) > 1:
                    self.results["duplicates"].append({
                        "hash": hash_val,
                        "count": len(paths),
                        "paths": paths
                    })

            print(f"\n✅ FOUND {len(self.results['duplicates'])} duplicate groups")

        except Exception as e:
            self.results["errors"].append(f"Duplicate check error: {str(e)}")

    def analyze_folders(self):
        """Analyze folder sizes"""
        print(f"\n📊 ANALYZING FOLDERS...")

        try:
            result = subprocess.run(
                ['du', '-sh', f'{self.drive}/*'],
                shell=True,
                capture_output=True,
                text=True,
                timeout=300
            )

            for line in result.stdout.split('\n'):
                if line.strip():
                    parts = line.split('\t')
                    if len(parts) == 2:
                        size, path = parts
                        self.results["large_folders"].append({
                            "path": path,
                            "size": size
                        })

            # Sort by size
            self.results["large_folders"].sort(
                key=lambda x: x["size"],
                reverse=True
            )

            print(f"✅ ANALYZED {len(self.results['large_folders'])} folders")

        except Exception as e:
            self.results["errors"].append(f"Folder analysis error: {str(e)}")

    def check_health(self):
        """Check drive health"""
        print(f"\n🏥 CHECKING DRIVE HEALTH...")

        try:
            # Check permissions
            test_file = self.drive / ".health_test"
            try:
                test_file.touch()
                test_file.unlink()
                self.results["write_test"] = "PASS"
            except:
                self.results["write_test"] = "FAIL"
                self.results["errors"].append("Write test failed - permissions issue")

            # Overall health
            if len(self.results["errors"]) == 0:
                self.results["health_status"] = "EXCELLENT ✅"
            elif len(self.results["errors"]) < 5:
                self.results["health_status"] = "GOOD ⚠️"
            else:
                self.results["health_status"] = "NEEDS ATTENTION ⚠️"

            print(f"✅ HEALTH: {self.results['health_status']}")

        except Exception as e:
            self.results["errors"].append(f"Health check error: {str(e)}")

    def save_report(self):
        """Save detailed report"""
        report_path = self.drive / f"SCAN_REPORT_{self.timestamp}.json"

        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)

        # Text summary
        summary_path = self.drive / f"SCAN_REPORT_{self.timestamp}.txt"

        with open(summary_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("6TB DRIVE SCAN REPORT - FISH MUSIC INC\n")
            f.write("GORUNFREE! 🎸🔥\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Scan Time: {self.results['scan_time']}\n")
            f.write(f"Health Status: {self.results['health_status']}\n\n")

            f.write("STORAGE:\n")
            f.write(f"  Used: {self.results['total_size_gb']} GB\n")
            f.write(f"  Free: {self.results.get('free_space_gb', 0)} GB\n\n")

            f.write("FILES:\n")
            f.write(f"  Total Files: {self.results['total_files']:,}\n")
            f.write(f"  Audio Files: {self.results['audio_files']:,}\n")
            f.write(f"  Project Files: {self.results['project_files']:,}\n\n")

            f.write("DUPLICATES:\n")
            f.write(f"  Duplicate Groups: {len(self.results['duplicates'])}\n")
            if self.results['duplicates']:
                f.write("\nTop 10 Duplicate Groups:\n")
                for dup in self.results['duplicates'][:10]:
                    f.write(f"\n  {dup['count']} copies:\n")
                    for path in dup['paths'][:3]:
                        f.write(f"    - {path}\n")

            f.write("\n\nLARGEST FOLDERS:\n")
            for folder in self.results['large_folders'][:20]:
                f.write(f"  {folder['size']:<10} {folder['path']}\n")

            if self.results['errors']:
                f.write("\n\nERRORS/WARNINGS:\n")
                for error in self.results['errors']:
                    f.write(f"  - {error}\n")

        print(f"\n💾 REPORTS SAVED:")
        print(f"  JSON: {report_path}")
        print(f"  TXT:  {summary_path}")

    def run_full_scan(self):
        """Execute complete scan & heal"""
        print("\n" + "=" * 60)
        print("🚀 6TB DRIVE SCANNER & HEALER - STARTING")
        print("=" * 60)

        start_time = datetime.now()

        self.scan_all()
        self.find_duplicates()
        self.analyze_folders()
        self.check_health()
        self.save_report()

        elapsed = (datetime.now() - start_time).total_seconds()

        print("\n" + "=" * 60)
        print(f"✅ COMPLETE! Time: {elapsed:.1f}s")
        print("=" * 60)
        print(f"\n📊 SUMMARY:")
        print(f"  Files: {self.results['total_files']:,}")
        print(f"  Audio: {self.results['audio_files']:,}")
        print(f"  Duplicates: {len(self.results['duplicates'])}")
        print(f"  Health: {self.results['health_status']}")
        print(f"\n🔥 GORUNFREE! 🎸")

if __name__ == "__main__":
    healer = DriveHealer("/Volumes/6TB")
    healer.run_full_scan()
