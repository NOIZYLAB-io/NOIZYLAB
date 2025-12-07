#!/usr/bin/env python3
"""
ADVANCED DUPLICATE REMOVER - Intelligent Duplicate Management
AI-powered duplicate detection with smart keeping algorithms
"""

import os
import json
import hashlib
import shutil
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
REPORT_FILE = WORKSPACE / "organization_report.json"
DUPES_DIR = Path("/Volumes/4TBSG/_DUPLICATES_REMOVED")
REMOVAL_LOG = Path("/Volumes/4TBSG/SCAN_RESULTS/advanced_removal_log.json")

class AdvancedDuplicateRemover:
    def __init__(self):
        self.duplicates = defaultdict(list)
        self.space_to_recover = 0
        self.files_to_remove = []
        self.kept_files = []
        
    def intelligent_scoring(self, filepath):
        """Advanced AI-like scoring for which file to keep"""
        score = 1000  # Base score
        path_lower = str(filepath).lower()
        
        # PRIORITY 1: Location Quality (highest weight)
        if 'organized_libraries' in path_lower:
            score += 500  # Already organized
        if 'kontakt_libraries' in path_lower:
            score += 400
        if 'audio_samples' in path_lower:
            score += 350
        
        # PENALTY: Bad locations
        if any(bad in path_lower for bad in ['duplicate', 'backup', 'copy', 'old', 'temp', 'trash', 'delete', 'sfx dupes']):
            score -= 800
        
        # PRIORITY 2: Path Length (shorter = more organized)
        path_depth = len(Path(filepath).parts)
        score -= path_depth * 10
        
        # PRIORITY 3: Naming Quality
        filename = os.path.basename(filepath)
        if any(marker in filename.lower() for marker in ['copy', ' (1)', ' (2)', '_copy', '-copy']):
            score -= 300
        if filename.startswith('.'):
            score -= 400
        
        # PRIORITY 4: Vendor/Brand indicators
        premium_vendors = ['spitfire', 'native instruments', 'output', '8dio', 'projectsam', 
                          'eastwest', 'cinesamples', 'soundiron', 'audiobro']
        if any(vendor in path_lower for vendor in premium_vendors):
            score += 200
        
        # PRIORITY 5: File accessibility
        try:
            # Check if file is actually readable
            with open(filepath, 'rb') as f:
                f.read(1)
            score += 50
        except:
            score -= 1000  # Heavily penalize unreadable files
        
        # PRIORITY 6: Metadata quality
        try:
            stat = os.stat(filepath)
            # Prefer files with more recent access (likely being used)
            import time
            days_since_access = (time.time() - stat.st_atime) / 86400
            if days_since_access < 30:
                score += 100
            elif days_since_access < 90:
                score += 50
        except:
            pass
        
        # PRIORITY 7: Drive preference
        if '/6TB/' in str(filepath):
            score += 150  # Prefer primary drive
        
        return score
    
    def find_duplicates_parallel(self, max_workers=24):
        """Find duplicates with parallel processing"""
        print("\n🔍 Scanning for duplicates with advanced detection...")
        
        file_hashes = defaultdict(list)
        files_scanned = 0
        
        # Scan both drives
        scan_paths = [
            Path("/Volumes/6TB"),
            Path("/Volumes/4TBSG/KTK 2026 TO SORT"),
        ]
        
        all_files = []
        for base_path in scan_paths:
            if not base_path.exists():
                continue
                
            for root, dirs, files in os.walk(base_path):
                # Skip already processed folders
                dirs[:] = [d for d in dirs if not d.startswith('.') and 
                          d not in ['_DUPLICATES_REMOVED', 'SCAN_RESULTS']]
                
                for filename in files:
                    if filename.startswith('.'):
                        continue
                    
                    filepath = os.path.join(root, filename)
                    all_files.append(filepath)
        
        print(f"📊 Found {len(all_files):,} files to check")
        print(f"⚡ Using {max_workers} parallel workers\n")
        
        # Hash files in parallel
        def hash_file(filepath):
            try:
                size = os.path.getsize(filepath)
                if size < 100 * 1024:  # Skip files < 100KB
                    return None
                
                hasher = hashlib.md5()
                hasher.update(str(size).encode())
                
                with open(filepath, 'rb') as f:
                    # Sample-based hashing for speed
                    chunk = f.read(16384)
                    hasher.update(chunk)
                    
                    if size > 32768:
                        f.seek(size // 2)
                        chunk = f.read(16384)
                        hasher.update(chunk)
                    
                    if size > 32768:
                        f.seek(-16384, 2)
                        chunk = f.read(16384)
                        hasher.update(chunk)
                
                return (hasher.hexdigest(), filepath, size)
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(hash_file, fp): fp for fp in all_files}
            
            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                if result:
                    file_hash, filepath, size = result
                    file_hashes[file_hash].append((filepath, size))
                
                if i % 500 == 0:
                    print(f"  Progress: {i:,}/{len(all_files):,} ({i/len(all_files)*100:.1f}%)", end='\r')
        
        print(f"\n✅ Scan complete!")
        
        # Find duplicates
        for file_hash, files in file_hashes.items():
            if len(files) > 1:
                self.duplicates[file_hash] = files
        
        print(f"🔄 Found {len(self.duplicates):,} duplicate groups")
        
        return self.duplicates
    
    def analyze_and_plan_removal(self):
        """Analyze duplicates and plan intelligent removal"""
        print("\n🎯 Analyzing duplicates with AI-powered scoring...")
        
        for file_hash, files in self.duplicates.items():
            # Score all files
            scored_files = []
            for filepath, size in files:
                score = self.intelligent_scoring(filepath)
                scored_files.append((score, filepath, size))
            
            # Sort by score (highest = best to keep)
            scored_files.sort(reverse=True, key=lambda x: x[0])
            
            # Keep the best one
            best_score, best_file, best_size = scored_files[0]
            self.kept_files.append(best_file)
            
            # Remove the rest
            for score, filepath, size in scored_files[1:]:
                self.files_to_remove.append({
                    'file': filepath,
                    'size': size,
                    'kept': best_file,
                    'score_difference': best_score - score
                })
                self.space_to_recover += size
        
        print(f"✅ Analysis complete!")
        print(f"📊 Files to keep: {len(self.kept_files):,}")
        print(f"🗑️  Files to remove: {len(self.files_to_remove):,}")
        print(f"💾 Space to recover: {self.format_size(self.space_to_recover)}")
    
    def format_size(self, bytes_val):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    def execute_removal(self, dry_run=True, backup=True):
        """Execute the removal with optional backup"""
        print("\n" + "="*70)
        print("🗑️  ADVANCED DUPLICATE REMOVAL")
        print("="*70)
        
        if dry_run:
            print("\n⚠️  DRY RUN MODE - Preview only, no files deleted")
        else:
            print("\n🔴 LIVE MODE - Files will be removed!")
            if backup:
                print(f"📦 Backup location: {DUPES_DIR}")
                DUPES_DIR.mkdir(parents=True, exist_ok=True)
        
        # Show sample removals
        print(f"\n📋 Sample removals (first 20):\n")
        for i, item in enumerate(self.files_to_remove[:20], 1):
            print(f"{i}. {os.path.basename(item['file'])}")
            print(f"   Size: {self.format_size(item['size'])}")
            print(f"   KEEPING: {item['kept']}")
            print(f"   REMOVING: {item['file']}\n")
        
        if len(self.files_to_remove) > 20:
            print(f"... and {len(self.files_to_remove) - 20} more files\n")
        
        if not dry_run:
            print("🚀 Removing duplicates...")
            
            removed_count = 0
            errors = []
            
            for item in self.files_to_remove:
                try:
                    filepath = Path(item['file'])
                    
                    if backup:
                        # Move to backup
                        rel_path = filepath.name
                        backup_path = DUPES_DIR / rel_path
                        
                        # Handle name conflicts
                        counter = 1
                        while backup_path.exists():
                            backup_path = DUPES_DIR / f"{filepath.stem}_{counter}{filepath.suffix}"
                            counter += 1
                        
                        shutil.move(str(filepath), str(backup_path))
                    else:
                        # Permanent deletion
                        os.remove(filepath)
                    
                    removed_count += 1
                    
                    if removed_count % 100 == 0:
                        print(f"  Progress: {removed_count:,}/{len(self.files_to_remove):,}", end='\r')
                
                except Exception as e:
                    errors.append({'file': item['file'], 'error': str(e)})
            
            print(f"\n✅ Removed {removed_count:,} duplicate files")
            if errors:
                print(f"⚠️  {len(errors)} errors occurred")
            
            # Save log
            log_data = {
                'timestamp': datetime.now().isoformat(),
                'removed': removed_count,
                'space_recovered': self.space_to_recover,
                'backup_enabled': backup,
                'errors': errors,
                'files_removed': self.files_to_remove[:100]  # Sample
            }
            
            with open(REMOVAL_LOG, 'w') as f:
                json.dump(log_data, f, indent=2)
            
            print(f"📄 Removal log saved: {REMOVAL_LOG}")
        
        print(f"\n💾 Total space that would be recovered: {self.format_size(self.space_to_recover)}")
        print("="*70)

def main():
    print("\n" + "🗑️ "*35)
    print("  ADVANCED DUPLICATE REMOVER - AI-Powered")
    print("🗑️ "*35 + "\n")
    
    remover = AdvancedDuplicateRemover()
    
    # Step 1: Find duplicates
    duplicates = remover.find_duplicates_parallel()
    
    if not duplicates:
        print("\n✅ No duplicates found! Library is clean!")
        return
    
    # Step 2: Analyze and plan
    remover.analyze_and_plan_removal()
    
    # Step 3: Execute (dry-run by default)
    remover.execute_removal(dry_run=True, backup=True)
    
    print("\n💡 To actually remove duplicates:")
    print("   1. Review the plan above")
    print("   2. BACKUP your drives!")
    print("   3. Run with --live flag: python3 advanced_duplicate_remover.py --live")

if __name__ == "__main__":
    import sys
    dry_run = '--live' not in sys.argv
    
    if not dry_run:
        print("\n🔴 LIVE MODE ENABLED!")
        response = input("Type 'DELETE' to confirm: ")
        if response != 'DELETE':
            print("❌ Cancelled")
            sys.exit(0)
    
    main()

