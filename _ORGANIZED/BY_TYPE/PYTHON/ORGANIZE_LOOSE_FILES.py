#!/usr/bin/env python3
"""
EXS24 Master Library - Loose Files Organizer
Organizes loose files into appropriate collection folders
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class LooseFilesOrganizer:
    def __init__(self, root_path, dry_run=True):
        self.root_path = Path(root_path)
        self.dry_run = dry_run
        self.moved_files = []
        self.errors = []
        self.exs24_path = self.root_path / "12TB_ROOT/FLIP 4TB 01/__2025 PROJECT EXS24"
        
    def organize_loose_files(self):
        """Organize loose EXS24 files into collections"""
        print("📦 Organizing loose files...")
        if self.dry_run:
            print("   [DRY RUN MODE - No files will be moved]")
        
        if not self.exs24_path.exists():
            print(f"⚠️  EXS24 path not found: {self.exs24_path}")
            return 0, 0
        
        # Find loose files (at depth <= 3)
        loose_files = []
        for root, dirs, files in os.walk(self.exs24_path):
            root_path = Path(root)
            rel_path = root_path.relative_to(self.exs24_path)
            depth = len(rel_path.parts)
            
            if depth <= 1:  # Files directly in collection folders or root
                for file in files:
                    if file.lower().endswith(('.exs', '.exs24')):
                        file_path = root_path / file
                        # Check if it's actually a file (not a directory)
                        if file_path.is_file():
                            loose_files.append(file_path)
        
        print(f"   Found {len(loose_files)} loose files")
        
        # Create EB COLLECTION folder for EB-prefixed files
        eb_collection = self.exs24_path / "EB COLLECTION"
        if not eb_collection.exists() and not self.dry_run:
            eb_collection.mkdir(exist_ok=True)
            (eb_collection / "SAMPLER INST.").mkdir(exist_ok=True)
        
        moved_count = 0
        
        for file_path in loose_files:
            file_name = file_path.name
            
            # Determine destination
            if file_name.upper().startswith('EB '):
                # Move to EB COLLECTION
                dest_dir = eb_collection / "SAMPLER INST."
                dest_path = dest_dir / file_name
            else:
                # Try to find appropriate collection or create MISC
                dest_dir = self.exs24_path / "MISC INSTRUMENTS" / "SAMPLER INST."
                dest_path = dest_dir / file_name
            
            if dest_path.exists() and dest_path != file_path:
                self.errors.append(f"Target exists: {file_path} -> {dest_path}")
                continue
            
            self.moved_files.append({
                'old': str(file_path.relative_to(self.root_path)),
                'new': str(dest_path.relative_to(self.root_path))
            })
            
            if not self.dry_run:
                try:
                    # Create destination directory if needed
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    # Move file
                    shutil.move(str(file_path), str(dest_path))
                    moved_count += 1
                except Exception as e:
                    self.errors.append(f"Error moving {file_path}: {e}")
            else:
                moved_count += 1
        
        print(f"✅ Would move {moved_count} files")
        
        if self.dry_run:
            print("\n📋 Files that would be moved:")
            for item in self.moved_files[:20]:
                print(f"  {item['old']}")
                print(f"    -> {item['new']}")
            if len(self.moved_files) > 20:
                print(f"  ... and {len(self.moved_files) - 20} more")
        else:
            print(f"✅ Successfully moved {moved_count} files")
        
        if self.errors:
            print(f"\n⚠️  {len(self.errors)} errors encountered:")
            for error in self.errors[:10]:
                print(f"  {error}")
        
        return moved_count, len(self.errors)
    
    def generate_report(self):
        """Generate organization report"""
        report = []
        report.append("=" * 80)
        report.append("EXS24 LOOSE FILES ORGANIZATION REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        report.append("")
        report.append(f"Files Moved: {len(self.moved_files)}")
        report.append(f"Errors: {len(self.errors)}")
        report.append("")
        
        if self.moved_files:
            report.append("MOVED FILES:")
            report.append("-" * 80)
            for item in self.moved_files:
                report.append(f"  {item['old']}")
                report.append(f"    -> {item['new']}")
        
        if self.errors:
            report.append("")
            report.append("ERRORS:")
            report.append("-" * 80)
            for error in self.errors:
                report.append(f"  {error}")
        
        return "\n".join(report)


def main():
    import sys
    
    root_path = Path(__file__).parent
    dry_run = '--live' not in sys.argv
    
    if not dry_run:
        response = input("⚠️  This will move files. Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            return
    
    organizer = LooseFilesOrganizer(root_path, dry_run=dry_run)
    moved, errors = organizer.organize_loose_files()
    
    # Save report
    report = organizer.generate_report()
    report_path = root_path / f"ORGANIZE_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n💾 Report saved to: {report_path}")


if __name__ == "__main__":
    main()

