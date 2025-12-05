#!/usr/bin/env python3
"""
🗑️ INTELLIGENT DUPLICATE REMOVER
Safely removes duplicate files while preserving best quality versions
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import sqlite3

DATABASE_PATH = Path("/Volumes/4TBSG/NOIZYLAB/library_master.db")
REPORT_DIR = Path("/Volumes/4TBSG/NOIZYLAB/REPORTS")

class DuplicateRemover:
    """Smart duplicate file removal"""
    
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.stats = {
            'files_scanned': 0,
            'duplicates_found': 0,
            'duplicates_removed': 0,
            'space_saved': 0,
            'errors': []
        }
        self.file_hashes = defaultdict(list)
    
    def calculate_hash(self, filepath: Path, chunk_size=65536) -> str:
        """Calculate full file hash"""
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            self.stats['errors'].append(f"Hash error for {filepath}: {e}")
            return None
    
    def scan_directory(self, directory: Path):
        """Scan directory for files"""
        print(f"\n🔍 Scanning: {directory}")
        
        for root, dirs, files in os.walk(directory):
            # Skip system directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                if filename.startswith('.'):
                    continue
                
                filepath = Path(root) / filename
                
                try:
                    file_size = filepath.stat().st_size
                    
                    # Skip small files (< 1MB) - likely not worth deduplicating
                    if file_size < 1024 * 1024:
                        continue
                    
                    file_hash = self.calculate_hash(filepath)
                    if file_hash:
                        self.file_hashes[file_hash].append({
                            'path': filepath,
                            'size': file_size,
                            'modified': filepath.stat().st_mtime
                        })
                    
                    self.stats['files_scanned'] += 1
                    
                    if self.stats['files_scanned'] % 1000 == 0:
                        print(f"  Scanned {self.stats['files_scanned']:,} files...", end='\r')
                
                except Exception as e:
                    self.stats['errors'].append(f"Scan error for {filepath}: {e}")
        
        print(f"  Scanned {self.stats['files_scanned']:,} files")
    
    def choose_best_version(self, duplicates: list) -> tuple:
        """Choose which duplicate to keep"""
        # Sorting priority:
        # 1. Prefer files in "Organized" directories
        # 2. Prefer newer files (higher modified time)
        # 3. Prefer shorter paths (closer to root)
        
        def score_file(file_info):
            path_str = str(file_info['path']).lower()
            score = 0
            
            # Bonus for organized locations
            if 'organized' in path_str or 'factory' in path_str:
                score += 1000
            
            # Bonus for shorter paths
            score -= len(str(file_info['path']).split(os.sep))
            
            # Bonus for newer files
            score += file_info['modified'] / 1000000000  # Normalize timestamp
            
            return score
        
        sorted_dupes = sorted(duplicates, key=score_file, reverse=True)
        keep = sorted_dupes[0]
        remove = sorted_dupes[1:]
        
        return keep, remove
    
    def remove_duplicates(self):
        """Remove duplicate files"""
        print("\n🗑️  Processing duplicates...")
        
        duplicate_report = []
        
        for file_hash, file_list in self.file_hashes.items():
            if len(file_list) < 2:
                continue
            
            self.stats['duplicates_found'] += len(file_list) - 1
            
            # Choose best version
            keep, remove = self.choose_best_version(file_list)
            
            duplicate_info = {
                'hash': file_hash,
                'keep': str(keep['path']),
                'remove': [],
                'space_saved': 0
            }
            
            for file_info in remove:
                filepath = file_info['path']
                file_size = file_info['size']
                
                if self.dry_run:
                    print(f"[DRY RUN] Would remove: {filepath}")
                    duplicate_info['remove'].append(str(filepath))
                    duplicate_info['space_saved'] += file_size
                    self.stats['space_saved'] += file_size
                else:
                    try:
                        os.remove(filepath)
                        print(f"✓ Removed: {filepath}")
                        duplicate_info['remove'].append(str(filepath))
                        duplicate_info['space_saved'] += file_size
                        self.stats['space_saved'] += file_size
                        self.stats['duplicates_removed'] += 1
                    except Exception as e:
                        self.stats['errors'].append(f"Remove error for {filepath}: {e}")
                        print(f"✗ Error removing {filepath}: {e}")
            
            if duplicate_info['remove']:
                duplicate_report.append(duplicate_info)
        
        return duplicate_report
    
    def generate_report(self, duplicate_report: list):
        """Generate duplicate removal report"""
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        report_file = REPORT_DIR / f"duplicate_removal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'statistics': {
                'files_scanned': self.stats['files_scanned'],
                'duplicates_found': self.stats['duplicates_found'],
                'duplicates_removed': self.stats['duplicates_removed'],
                'space_saved_bytes': self.stats['space_saved'],
                'space_saved_human': self.format_size(self.stats['space_saved']),
                'errors': len(self.stats['errors'])
            },
            'duplicates': duplicate_report[:1000],  # Limit to first 1000
            'errors': self.stats['errors'][:100]
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Report saved: {report_file}")
        return report
    
    @staticmethod
    def format_size(bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def print_summary(self):
        """Print summary"""
        print("\n" + "="*80)
        print("🗑️  DUPLICATE REMOVAL SUMMARY")
        print("="*80)
        
        print(f"\n✓ Files Scanned: {self.stats['files_scanned']:,}")
        print(f"✓ Duplicates Found: {self.stats['duplicates_found']:,}")
        print(f"✓ Duplicates Removed: {self.stats['duplicates_removed']:,}")
        print(f"✓ Space Saved: {self.format_size(self.stats['space_saved'])}")
        
        if self.stats['errors']:
            print(f"\n⚠️  Errors: {len(self.stats['errors'])}")
        
        print("\n" + "="*80)

def main():
    """Main execution"""
    print("\n" + "🗑️ " * 40)
    print("  INTELLIGENT DUPLICATE REMOVER")
    print("🗑️ " * 40 + "\n")
    
    if len(sys.argv) < 2:
        print("Usage: python duplicate_remover.py <directory> [--execute]")
        print("\nExample:")
        print("  python duplicate_remover.py /Volumes/4TBSG/KTK\\ 2026\\ TO\\ SORT")
        print("  python duplicate_remover.py /Volumes/4TBSG/KTK\\ 2026\\ TO\\ SORT --execute")
        sys.exit(1)
    
    target_dir = Path(sys.argv[1])
    dry_run = '--execute' not in sys.argv
    
    if not target_dir.exists():
        print(f"❌ Directory not found: {target_dir}")
        sys.exit(1)
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be removed")
        print("   Add --execute flag to perform actual removal\n")
    else:
        print("⚠️  EXECUTION MODE - Files will be removed!")
        print("   Press Ctrl+C within 5 seconds to cancel...")
        import time
        try:
            for i in range(5, 0, -1):
                print(f"   Starting in {i}...", end='\r')
                time.sleep(1)
            print("\n")
        except KeyboardInterrupt:
            print("\n\n❌ Cancelled by user")
            sys.exit(0)
    
    # Run duplicate removal
    remover = DuplicateRemover(dry_run=dry_run)
    
    try:
        remover.scan_directory(target_dir)
        duplicate_report = remover.remove_duplicates()
        remover.generate_report(duplicate_report)
        remover.print_summary()
        
        print("\n✅ DUPLICATE REMOVAL COMPLETE!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Critical error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

