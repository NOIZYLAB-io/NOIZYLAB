#!/usr/bin/env python3
"""
🧹 ADVANCED CLEANUP UTILITIES
- Delete empty folders
- Fix/clean all filenames and folder names
- Move duplicates to quarantine folder
"""

import os
import sys
import re
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import hashlib
import json

# Configuration
WORKSPACE_DIRS = [
    Path("/Volumes/4TBSG/KTK 2026 TO SORT"),
    Path("/Volumes/4TBSG/2026_SFX"),
    Path("/Volumes/4TBSG/MASTER_CONSOLIDATED_ARCHIVE")
]

DUPLICATES_FOLDER = Path("/Volumes/4TBSG/_DUPLICATES_QUARANTINE")
REPORT_DIR = Path("/Volumes/4TBSG/NOIZYLAB/REPORTS")

class AdvancedCleaner:
    """Advanced cleanup operations"""
    
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.stats = {
            'folders_deleted': 0,
            'files_renamed': 0,
            'folders_renamed': 0,
            'duplicates_moved': 0,
            'space_recovered': 0,
            'errors': []
        }
        self.rename_log = []
        self.file_hashes = defaultdict(list)
    
    # ==================== NAME CLEANING ====================
    
    @staticmethod
    def clean_name(name: str) -> str:
        """Clean and standardize file/folder names"""
        # Remove file extension for processing
        path = Path(name)
        ext = path.suffix
        base_name = path.stem
        
        # Apply cleaning rules
        cleaned = base_name
        
        # Remove multiple spaces and special characters
        cleaned = re.sub(r'[^\w\s\-_().]', '', cleaned)
        
        # Fix common issues
        cleaned = cleaned.replace('  ', ' ')  # Double spaces
        cleaned = cleaned.replace(' _', '_')  # Space before underscore
        cleaned = cleaned.replace('_ ', '_')  # Space after underscore
        cleaned = cleaned.replace(' -', '-')  # Space before dash
        cleaned = cleaned.replace('- ', '-')  # Space after dash
        
        # Remove leading/trailing spaces and special chars
        cleaned = cleaned.strip(' -_.')
        
        # Fix common naming patterns
        cleaned = re.sub(r'\s+', ' ', cleaned)  # Multiple spaces to single
        cleaned = re.sub(r'[-_]{2,}', '_', cleaned)  # Multiple dashes/underscores
        
        # Capitalize properly
        # Keep existing case but fix obvious issues
        if cleaned.isupper() and len(cleaned) > 10:
            # Convert ALLCAPS to Title Case for long names
            cleaned = cleaned.title()
        elif cleaned.islower() and len(cleaned) > 10:
            # Convert alllower to Title Case for long names
            cleaned = cleaned.title()
        
        # Fix common abbreviations
        replacements = {
            ' V0': ' V0',  # Version numbers
            ' V ': ' V',
            'Kli': 'KLI',
            'Sfx': 'SFX',
            'Fx': 'FX',
            'Eq': 'EQ',
            'Vst': 'VST',
            'Daw': 'DAW',
            'Midi': 'MIDI',
            'Wav': 'WAV',
            'Mp3': 'MP3',
            'Aif': 'AIF',
        }
        
        for old, new in replacements.items():
            cleaned = cleaned.replace(old, new)
        
        # Remove weird artifacts
        cleaned = re.sub(r'(?i)(copy|duplicate|backup)(\s+\d+)?$', '', cleaned).strip()
        
        # Reassemble with extension
        if ext:
            return f"{cleaned}{ext}"
        return cleaned
    
    def rename_item(self, item_path: Path, is_file=True):
        """Rename a file or folder with cleaned name"""
        original_name = item_path.name
        cleaned_name = self.clean_name(original_name)
        
        # Skip if no change needed
        if original_name == cleaned_name:
            return False
        
        new_path = item_path.parent / cleaned_name
        
        # Handle conflicts
        if new_path.exists():
            # Add timestamp suffix
            if is_file:
                stem = Path(cleaned_name).stem
                ext = Path(cleaned_name).suffix
                cleaned_name = f"{stem}_{int(datetime.now().timestamp())}{ext}"
            else:
                cleaned_name = f"{cleaned_name}_{int(datetime.now().timestamp())}"
            new_path = item_path.parent / cleaned_name
        
        try:
            if self.dry_run:
                print(f"[DRY RUN] Rename: {original_name} → {cleaned_name}")
                self.rename_log.append({
                    'original': str(item_path),
                    'new': str(new_path),
                    'type': 'file' if is_file else 'folder'
                })
            else:
                item_path.rename(new_path)
                print(f"✓ Renamed: {original_name} → {cleaned_name}")
                self.rename_log.append({
                    'original': str(item_path),
                    'new': str(new_path),
                    'type': 'file' if is_file else 'folder'
                })
            
            if is_file:
                self.stats['files_renamed'] += 1
            else:
                self.stats['folders_renamed'] += 1
            
            return True
        except Exception as e:
            self.stats['errors'].append(f"Rename error for {item_path}: {e}")
            return False
    
    def clean_names_in_directory(self, directory: Path):
        """Clean all names in directory recursively"""
        print(f"\n🧹 Cleaning names in: {directory}")
        
        # Process files first, then folders (bottom-up)
        for root, dirs, files in os.walk(directory, topdown=False):
            root_path = Path(root)
            
            # Rename files
            for filename in files:
                if filename.startswith('.'):
                    continue
                file_path = root_path / filename
                self.rename_item(file_path, is_file=True)
            
            # Rename folders (after their contents)
            for dirname in dirs:
                if dirname.startswith('.'):
                    continue
                dir_path = root_path / dirname
                self.rename_item(dir_path, is_file=False)
    
    # ==================== EMPTY FOLDER REMOVAL ====================
    
    def is_folder_empty(self, folder: Path) -> bool:
        """Check if folder is truly empty (ignoring system files)"""
        try:
            items = list(folder.iterdir())
            # Filter out system files
            non_system_items = [
                item for item in items 
                if not item.name.startswith('.') 
                and item.name not in ['Thumbs.db', 'desktop.ini']
            ]
            return len(non_system_items) == 0
        except Exception:
            return False
    
    def delete_empty_folders(self, directory: Path):
        """Recursively delete empty folders"""
        print(f"\n🗑️  Deleting empty folders in: {directory}")
        
        deleted_count = 0
        
        # Multiple passes to handle nested empty folders
        for _ in range(10):  # Max 10 levels deep
            pass_deleted = 0
            
            for root, dirs, files in os.walk(directory, topdown=False):
                root_path = Path(root)
                
                # Skip system directories
                if any(part.startswith('.') for part in root_path.parts):
                    continue
                
                if self.is_folder_empty(root_path):
                    try:
                        if self.dry_run:
                            print(f"[DRY RUN] Would delete: {root_path}")
                        else:
                            shutil.rmtree(root_path)
                            print(f"✓ Deleted empty: {root_path}")
                        
                        pass_deleted += 1
                        deleted_count += 1
                    except Exception as e:
                        self.stats['errors'].append(f"Delete error for {root_path}: {e}")
            
            # Stop if no more empty folders found
            if pass_deleted == 0:
                break
        
        self.stats['folders_deleted'] = deleted_count
        print(f"✓ Deleted {deleted_count} empty folders")
    
    # ==================== DUPLICATE HANDLING ====================
    
    def calculate_hash(self, filepath: Path, sample_size=65536) -> str:
        """Calculate file hash"""
        hasher = hashlib.sha256()
        try:
            file_size = filepath.stat().st_size
            
            # For large files, use sampling
            if file_size > 100 * 1024 * 1024:  # > 100MB
                with open(filepath, 'rb') as f:
                    # Sample beginning, middle, end
                    hasher.update(f.read(sample_size))
                    f.seek(file_size // 2)
                    hasher.update(f.read(sample_size))
                    f.seek(-sample_size, 2)
                    hasher.update(f.read(sample_size))
                    hasher.update(str(file_size).encode())
            else:
                # Full hash for smaller files
                with open(filepath, 'rb') as f:
                    while chunk := f.read(sample_size):
                        hasher.update(chunk)
            
            return hasher.hexdigest()
        except Exception as e:
            self.stats['errors'].append(f"Hash error for {filepath}: {e}")
            return None
    
    def scan_for_duplicates(self, directory: Path):
        """Scan directory for duplicate files"""
        print(f"\n🔍 Scanning for duplicates in: {directory}")
        
        file_count = 0
        for root, dirs, files in os.walk(directory):
            # Skip system directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                if filename.startswith('.'):
                    continue
                
                filepath = Path(root) / filename
                
                try:
                    file_size = filepath.stat().st_size
                    
                    # Skip small files (< 500KB)
                    if file_size < 500 * 1024:
                        continue
                    
                    file_hash = self.calculate_hash(filepath)
                    if file_hash:
                        self.file_hashes[file_hash].append({
                            'path': filepath,
                            'size': file_size,
                            'modified': filepath.stat().st_mtime
                        })
                    
                    file_count += 1
                    if file_count % 500 == 0:
                        print(f"  Scanned {file_count:,} files...", end='\r')
                
                except Exception as e:
                    self.stats['errors'].append(f"Scan error for {filepath}: {e}")
        
        print(f"  Scanned {file_count:,} files")
    
    def move_duplicates(self):
        """Move duplicate files to quarantine folder"""
        print(f"\n📦 Moving duplicates to: {DUPLICATES_FOLDER}")
        
        if not self.dry_run:
            DUPLICATES_FOLDER.mkdir(parents=True, exist_ok=True)
        
        duplicate_count = 0
        
        for file_hash, file_list in self.file_hashes.items():
            if len(file_list) < 2:
                continue
            
            # Sort to keep the best version (most recent, shortest path)
            sorted_files = sorted(
                file_list,
                key=lambda x: (-x['modified'], len(str(x['path'])))
            )
            
            # Keep first, move others
            keep = sorted_files[0]
            duplicates = sorted_files[1:]
            
            for dup_info in duplicates:
                dup_path = dup_info['path']
                
                # Create organized structure in duplicates folder
                relative_path = str(dup_path).replace('/Volumes/4TBSG/', '')
                target_path = DUPLICATES_FOLDER / relative_path
                
                try:
                    if self.dry_run:
                        print(f"[DRY RUN] Would move duplicate: {dup_path.name}")
                    else:
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Handle naming conflicts
                        if target_path.exists():
                            stem = target_path.stem
                            ext = target_path.suffix
                            target_path = target_path.parent / f"{stem}_{int(datetime.now().timestamp())}{ext}"
                        
                        shutil.move(str(dup_path), str(target_path))
                        print(f"✓ Moved duplicate: {dup_path.name}")
                    
                    duplicate_count += 1
                    self.stats['duplicates_moved'] += 1
                    self.stats['space_recovered'] += dup_info['size']
                
                except Exception as e:
                    self.stats['errors'].append(f"Move error for {dup_path}: {e}")
        
        print(f"✓ Moved {duplicate_count} duplicate files")
    
    # ==================== REPORTING ====================
    
    def generate_report(self):
        """Generate cleanup report"""
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        report_file = REPORT_DIR / f"cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'statistics': {
                'folders_deleted': self.stats['folders_deleted'],
                'files_renamed': self.stats['files_renamed'],
                'folders_renamed': self.stats['folders_renamed'],
                'duplicates_moved': self.stats['duplicates_moved'],
                'space_recovered_bytes': self.stats['space_recovered'],
                'space_recovered_human': self.format_size(self.stats['space_recovered']),
                'errors': len(self.stats['errors'])
            },
            'rename_log_sample': self.rename_log[:100],  # First 100 renames
            'errors': self.stats['errors'][:100]
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Also save full rename log
        rename_log_file = REPORT_DIR / f"rename_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(rename_log_file, 'w') as f:
            json.dump(self.rename_log, f, indent=2)
        
        print(f"\n📄 Report saved: {report_file}")
        print(f"📄 Rename log saved: {rename_log_file}")
    
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
        print("🧹 CLEANUP SUMMARY")
        print("="*80)
        
        print(f"\n✓ Empty Folders Deleted: {self.stats['folders_deleted']:,}")
        print(f"✓ Files Renamed: {self.stats['files_renamed']:,}")
        print(f"✓ Folders Renamed: {self.stats['folders_renamed']:,}")
        print(f"✓ Duplicates Moved: {self.stats['duplicates_moved']:,}")
        print(f"✓ Space Recovered: {self.format_size(self.stats['space_recovered'])}")
        
        if self.stats['errors']:
            print(f"\n⚠️  Errors: {len(self.stats['errors'])}")
        
        print("\n" + "="*80)

# ==================== MAIN EXECUTION ====================

def main():
    """Main execution"""
    print("\n" + "🧹" * 40)
    print("  ADVANCED CLEANUP UTILITIES")
    print("  - Delete Empty Folders")
    print("  - Fix All Names")
    print("  - Move Duplicates to Quarantine")
    print("🧹" * 40 + "\n")
    
    # Parse arguments
    dry_run = '--execute' not in sys.argv
    skip_duplicates = '--skip-duplicates' in sys.argv
    skip_names = '--skip-names' in sys.argv
    skip_empty = '--skip-empty' in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print("   Add --execute flag to perform actual cleanup\n")
    else:
        print("⚠️  EXECUTION MODE - Changes will be made!")
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
    
    # Initialize cleaner
    cleaner = AdvancedCleaner(dry_run=dry_run)
    
    try:
        for workspace in WORKSPACE_DIRS:
            if not workspace.exists():
                print(f"⚠️  Skipping non-existent: {workspace}")
                continue
            
            print(f"\n{'='*80}")
            print(f"Processing: {workspace.name}")
            print(f"{'='*80}")
            
            # Step 1: Clean names
            if not skip_names:
                cleaner.clean_names_in_directory(workspace)
            
            # Step 2: Scan for duplicates
            if not skip_duplicates:
                cleaner.scan_for_duplicates(workspace)
            
            # Step 3: Delete empty folders
            if not skip_empty:
                cleaner.delete_empty_folders(workspace)
        
        # Step 4: Move duplicates (after scanning all workspaces)
        if not skip_duplicates:
            cleaner.move_duplicates()
        
        # Generate report
        cleaner.generate_report()
        cleaner.print_summary()
        
        print("\n✅ CLEANUP COMPLETE!")
        if cleaner.stats['duplicates_moved'] > 0:
            print(f"\n📁 Duplicates moved to: {DUPLICATES_FOLDER}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Critical error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

