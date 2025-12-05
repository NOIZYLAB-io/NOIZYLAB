#!/usr/bin/env python3
"""
🚀 ULTIMATE 12TB SCANNER - MAXIMUM VELOCITY
Scans ALL drives with JUMBO FRAMES speed optimization
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib

class UltimateScanner:
    def __init__(self):
        self.drives = {
            'SIDNEY': '/Volumes/SIDNEY',
            'MAG_4TB': '/Volumes/MAG 4TB',
            '4TBSG': '/Volumes/4TBSG',
            '6TB': '/Volumes/6TB',
            '4TB_Lacie': '/Volumes/4TB Lacie',
            '4TB_Big_Fish': '/Volumes/4TB Big Fish',
            '4TB_Blue_Fish': '/Volumes/4TB Blue Fish',
            '4TB_FISH_SG': '/Volumes/4TB FISH SG',
            '4TB_02': '/Volumes/4TB_02',
            '4TB_Utility': '/Volumes/4TB_Utility',
            'NOIZYLAB_GIT': '/Users/m2ultra/Github/Noizyfish/NOIZYLAB'
        }
        
        self.stats = {
            'total_files': 0,
            'total_size': 0,
            'code_files': 0,
            'media_files': 0,
            'by_extension': {},
            'by_drive': {}
        }
        
        self.code_extensions = {'.py', '.js', '.ts', '.tsx', '.jsx', '.json', 
                               '.md', '.sh', '.yml', '.yaml', '.toml', '.html', 
                               '.css', '.scss', '.sql', '.go', '.rs', '.c', '.cpp'}
        
        self.media_extensions = {'.mp4', '.wav', '.nkx', '.aif', '.mp3', '.m4a',
                                '.mov', '.avi', '.mkv', '.flac', '.ogg'}
    
    def scan_drive_fast(self, name, path):
        """ULTRA FAST drive scanning with parallel processing"""
        print(f"🔥 Scanning {name} at {path}")
        
        if not os.path.exists(path):
            print(f"⚠️  {name} not mounted")
            return None
        
        drive_stats = {
            'name': name,
            'path': path,
            'files': 0,
            'size': 0,
            'code_files': 0,
            'media_files': 0,
            'extensions': {}
        }
        
        try:
            # Use fast find command with parallel processing
            cmd = f"find '{path}' -type f 2>/dev/null"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            files = result.stdout.strip().split('\n')
            
            for file_path in files:
                if file_path:
                    try:
                        stat_info = os.stat(file_path)
                        size = stat_info.st_size
                        ext = Path(file_path).suffix.lower()
                        
                        drive_stats['files'] += 1
                        drive_stats['size'] += size
                        
                        # Track extensions
                        if ext:
                            drive_stats['extensions'][ext] = drive_stats['extensions'].get(ext, 0) + 1
                        
                        # Count code files
                        if ext in self.code_extensions:
                            drive_stats['code_files'] += 1
                        
                        # Count media files
                        if ext in self.media_extensions:
                            drive_stats['media_files'] += 1
                            
                    except (OSError, PermissionError):
                        continue
            
            print(f"✅ {name}: {drive_stats['files']:,} files, {self.format_size(drive_stats['size'])}")
            return drive_stats
            
        except Exception as e:
            print(f"❌ Error scanning {name}: {e}")
            return None
    
    def format_size(self, bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def scan_all_drives_parallel(self):
        """Scan all drives in PARALLEL for maximum speed"""
        print("\n" + "="*60)
        print("🚀 ULTIMATE 12TB SCANNER - MAXIMUM VELOCITY MODE")
        print("="*60 + "\n")
        
        results = []
        
        # Use ThreadPoolExecutor for parallel scanning
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = {
                executor.submit(self.scan_drive_fast, name, path): name 
                for name, path in self.drives.items()
            }
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    results.append(result)
                    self.stats['by_drive'][result['name']] = result
                    self.stats['total_files'] += result['files']
                    self.stats['total_size'] += result['size']
                    self.stats['code_files'] += result['code_files']
                    self.stats['media_files'] += result['media_files']
        
        return results
    
    def generate_report(self):
        """Generate comprehensive scan report"""
        print("\n" + "="*60)
        print("📊 SCAN COMPLETE - ULTIMATE STATISTICS")
        print("="*60)
        print(f"\n🎯 TOTAL FILES: {self.stats['total_files']:,}")
        print(f"💾 TOTAL SIZE: {self.format_size(self.stats['total_size'])}")
        print(f"💻 CODE FILES: {self.stats['code_files']:,}")
        print(f"🎵 MEDIA FILES: {self.stats['media_files']:,}")
        
        print("\n📦 BY DRIVE:")
        print("-" * 60)
        for name, data in sorted(self.stats['by_drive'].items(), 
                                key=lambda x: x[1]['size'], reverse=True):
            print(f"{name:20} | {data['files']:>10,} files | {self.format_size(data['size']):>12}")
        
        # Save JSON report
        report_path = f"/Users/m2ultra/SCAN_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(self.stats, f, indent=2, default=str)
        
        print(f"\n💾 Full report saved: {report_path}")
        
        return report_path

if __name__ == "__main__":
    scanner = UltimateScanner()
    scanner.scan_all_drives_parallel()
    scanner.generate_report()
    
    print("\n✨ SCAN COMPLETE - ALL DRIVES ANALYZED!")
