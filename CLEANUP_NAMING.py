#!/usr/bin/env python3
"""
EXS24 Master Library - Naming Cleanup Tool
Fixes naming inconsistencies (e.g., .exs.EXS -> .exs)
"""

import os
from pathlib import Path
from datetime import datetime

class NamingCleanup:
    def __init__(self, root_path, dry_run=True):
        self.root_path = Path(root_path)
        self.dry_run = dry_run
        self.fixed_files = []
        self.errors = []
        
    def fix_naming(self):
        """Fix naming inconsistencies"""
        print("🔧 Fixing naming inconsistencies...")
        if self.dry_run:
            print("   [DRY RUN MODE - No files will be modified]")
        
        fixed_count = 0
        
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                if file.lower().endswith(('.exs', '.exs24')):
                    file_path = Path(root) / file
                    
                    # Check for double extensions
                    if file.endswith('.exs.EXS') or file.endswith('.EXS.exs'):
                        # Fix to .exs
                        new_name = file.rsplit('.', 2)[0] + '.exs'
                        new_path = file_path.parent / new_name
                        
                        if new_path.exists() and new_path != file_path:
                            self.errors.append(f"Target exists: {file_path} -> {new_path}")
                            continue
                        
                        self.fixed_files.append({
                            'old': str(file_path.relative_to(self.root_path)),
                            'new': str(new_path.relative_to(self.root_path))
                        })
                        
                        if not self.dry_run:
                            try:
                                file_path.rename(new_path)
                                fixed_count += 1
                            except Exception as e:
                                self.errors.append(f"Error renaming {file_path}: {e}")
                        else:
                            fixed_count += 1
        
        print(f"✅ Found {fixed_count} files to fix")
        
        if self.dry_run:
            print("\n📋 Files that would be renamed:")
            for item in self.fixed_files[:20]:
                print(f"  {item['old']}")
                print(f"    -> {item['new']}")
            if len(self.fixed_files) > 20:
                print(f"  ... and {len(self.fixed_files) - 20} more")
        else:
            print(f"✅ Successfully renamed {fixed_count} files")
        
        if self.errors:
            print(f"\n⚠️  {len(self.errors)} errors encountered:")
            for error in self.errors[:10]:
                print(f"  {error}")
        
        return len(self.fixed_files), len(self.errors)
    
    def generate_report(self):
        """Generate cleanup report"""
        report = []
        report.append("=" * 80)
        report.append("EXS24 NAMING CLEANUP REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        report.append("")
        report.append(f"Files Fixed: {len(self.fixed_files)}")
        report.append(f"Errors: {len(self.errors)}")
        report.append("")
        
        if self.fixed_files:
            report.append("FIXED FILES:")
            report.append("-" * 80)
            for item in self.fixed_files:
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
        response = input("⚠️  This will rename files. Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            return
    
    cleanup = NamingCleanup(root_path, dry_run=dry_run)
    fixed, errors = cleanup.fix_naming()
    
    # Save report
    report = cleanup.generate_report()
    report_path = root_path / f"CLEANUP_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n💾 Report saved to: {report_path}")


if __name__ == "__main__":
    main()

