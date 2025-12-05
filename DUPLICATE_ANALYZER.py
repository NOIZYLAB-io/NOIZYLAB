#!/usr/bin/env python3
"""
EXS24 Master Library - Duplicate Analyzer & Remover
Analyzes and optionally removes duplicate files
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DuplicateAnalyzer:
    def __init__(self, scan_data_file=None, dry_run=True):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.dry_run = dry_run
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print(f"⚠️  Scan data not found: {self.scan_data_file}")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"⚠️  Error loading scan data: {e}")
            return False
    
    def analyze_duplicates(self):
        """Analyze duplicate files"""
        if not self.data:
            return None
        
        # Get duplicates by hash (true duplicates)
        hash_duplicates = self.data.get('duplicates_by_hash', {})
        
        # Get duplicates by filename
        filename_duplicates = self.data.get('duplicates', {})
        
        analysis = {
            'true_duplicates': {},
            'filename_duplicates': {},
            'total_space_wasted': 0,
            'recommendations': []
        }
        
        # Analyze true duplicates
        for file_hash, paths in hash_duplicates.items():
            if len(paths) > 1:
                # Get file sizes
                file_sizes = {}
                for path_str in paths:
                    file_path = Path(__file__).parent / path_str
                    if file_path.exists():
                        size = file_path.stat().st_size
                        file_sizes[path_str] = size
                
                if file_sizes:
                    # Calculate space that could be saved
                    sizes = list(file_sizes.values())
                    if sizes:
                        space_wasted = sum(sizes[1:])  # Keep first, remove rest
                        analysis['total_space_wasted'] += space_wasted
                        
                        # Determine which to keep (prefer shorter path or specific location)
                        sorted_paths = sorted(file_sizes.items(), key=lambda x: (len(x[0]), x[0]))
                        keep = sorted_paths[0][0]
                        remove = [p for p in paths if p != keep]
                        
                        analysis['true_duplicates'][file_hash] = {
                            'keep': keep,
                            'remove': remove,
                            'space_savings': space_wasted,
                            'count': len(paths)
                        }
        
        # Analyze filename duplicates (may not be true duplicates)
        for filename, paths in filename_duplicates.items():
            if len(paths) > 1:
                analysis['filename_duplicates'][filename] = {
                    'paths': paths,
                    'count': len(paths),
                    'note': 'Same filename but may have different content - verify before removing'
                }
        
        # Generate recommendations
        if analysis['true_duplicates']:
            total_dups = sum(d['count'] - 1 for d in analysis['true_duplicates'].values())
            analysis['recommendations'].append(
                f"Found {len(analysis['true_duplicates'])} groups of true duplicates "
                f"({total_dups} files can be removed, saving {analysis['total_space_wasted'] / (1024*1024):.2f} MB)"
            )
        
        if analysis['filename_duplicates']:
            analysis['recommendations'].append(
                f"Found {len(analysis['filename_duplicates'])} files with duplicate names "
                f"(verify content before removing)"
            )
        
        return analysis
    
    def generate_report(self, analysis):
        """Generate duplicate analysis report"""
        report = []
        report.append("=" * 80)
        report.append("EXS24 DUPLICATE ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary
        report.append("📊 SUMMARY")
        report.append("-" * 80)
        report.append(f"True Duplicate Groups: {len(analysis['true_duplicates'])}")
        total_removable = sum(d['count'] - 1 for d in analysis['true_duplicates'].values())
        report.append(f"Files That Can Be Removed: {total_removable}")
        report.append(f"Potential Space Savings: {analysis['total_space_wasted'] / (1024*1024):.2f} MB")
        report.append(f"Filename Duplicates: {len(analysis['filename_duplicates'])}")
        report.append("")
        
        # True Duplicates
        if analysis['true_duplicates']:
            report.append("🔄 TRUE DUPLICATES (Identical Content)")
            report.append("-" * 80)
            
            sorted_dups = sorted(
                analysis['true_duplicates'].items(),
                key=lambda x: x[1]['space_savings'],
                reverse=True
            )[:20]  # Top 20
            
            for file_hash, dup_info in sorted_dups:
                report.append(f"\nGroup ({dup_info['count']} files, {dup_info['space_savings'] / 1024:.2f} KB savings):")
                report.append(f"  KEEP: {dup_info['keep']}")
                for path in dup_info['remove']:
                    report.append(f"  REMOVE: {path}")
            report.append("")
        
        # Filename Duplicates
        if analysis['filename_duplicates']:
            report.append("📝 FILENAME DUPLICATES (Verify Content)")
            report.append("-" * 80)
            
            sorted_name_dups = sorted(
                analysis['filename_duplicates'].items(),
                key=lambda x: x[1]['count'],
                reverse=True
            )[:20]  # Top 20
            
            for filename, dup_info in sorted_name_dups:
                report.append(f"\n{filename} ({dup_info['count']} copies):")
                for path in dup_info['paths'][:5]:
                    report.append(f"  - {path}")
                if len(dup_info['paths']) > 5:
                    report.append(f"  ... and {len(dup_info['paths']) - 5} more")
            report.append("")
        
        # Recommendations
        if analysis['recommendations']:
            report.append("💡 RECOMMENDATIONS")
            report.append("-" * 80)
            for rec in analysis['recommendations']:
                report.append(f"  • {rec}")
            report.append("")
        
        return "\n".join(report)
    
    def remove_duplicates(self, analysis, confirm_each=False):
        """Remove duplicate files"""
        if not self.data:
            return 0, []
        
        removed_count = 0
        errors = []
        
        if self.dry_run:
            print("🔍 [DRY RUN MODE - No files will be deleted]")
        
        for file_hash, dup_info in analysis['true_duplicates'].items():
            for path_to_remove in dup_info['remove']:
                file_path = Path(__file__).parent / path_to_remove
                
                if confirm_each and not self.dry_run:
                    response = input(f"Remove {path_to_remove}? (y/n): ")
                    if response.lower() != 'y':
                        continue
                
                if not self.dry_run:
                    try:
                        if file_path.exists():
                            file_path.unlink()
                            removed_count += 1
                    except Exception as e:
                        errors.append(f"Error removing {path_to_remove}: {e}")
                else:
                    removed_count += 1
        
        return removed_count, errors


def main():
    import sys
    
    dry_run = '--live' not in sys.argv
    analyzer = DuplicateAnalyzer(dry_run=dry_run)
    
    if not analyzer.data:
        return
    
    print("🔍 Analyzing duplicates...")
    analysis = analyzer.analyze_duplicates()
    
    if analysis:
        # Generate report
        report = analyzer.generate_report(analysis)
        print("\n" + report)
        
        # Save report
        report_path = Path(__file__).parent / f"DUPLICATE_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n💾 Report saved to: {report_path}")
        
        # Option to remove duplicates
        if analysis['true_duplicates'] and not dry_run:
            total_removable = sum(d['count'] - 1 for d in analysis['true_duplicates'].values())
            response = input(f"\n⚠️  Remove {total_removable} duplicate files? (yes/no): ")
            if response.lower() == 'yes':
                removed, errors = analyzer.remove_duplicates(analysis)
                print(f"\n✅ Removed {removed} duplicate files")
                if errors:
                    print(f"⚠️  {len(errors)} errors occurred")


if __name__ == "__main__":
    main()




