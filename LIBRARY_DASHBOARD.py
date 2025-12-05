#!/usr/bin/env python3
"""
EXS24 Master Library - Dashboard
Real-time library status and health monitoring
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class LibraryDashboard:
    def __init__(self, scan_data_file=None):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print("⚠️  No scan data found. Run SCAN_AND_ORGANIZE.py first.")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"⚠️  Error loading data: {e}")
            return False
    
    def get_health_score(self):
        """Calculate library health score (0-100)"""
        if not self.data:
            return 0
        
        score = 100
        issues = []
        
        # Check naming inconsistencies
        naming_issues = len(self.data.get('naming_inconsistencies', []))
        if naming_issues > 0:
            penalty = min(naming_issues / 10, 20)  # Max 20 point penalty
            score -= penalty
            issues.append(f"Naming issues: {naming_issues} files")
        
        # Check loose files
        loose_files = len(self.data.get('loose_files', []))
        if loose_files > 0:
            penalty = min(loose_files, 10)  # Max 10 point penalty
            score -= penalty
            issues.append(f"Loose files: {loose_files}")
        
        # Check duplicates
        duplicates = len(self.data.get('duplicates', {}))
        if duplicates > 1000:
            penalty = min((duplicates - 1000) / 100, 15)  # Max 15 point penalty
            score -= penalty
            issues.append(f"Many duplicate filenames: {duplicates}")
        
        # Check empty directories
        empty_dirs = len(self.data.get('empty_dirs', []))
        if empty_dirs > 100:
            penalty = min((empty_dirs - 100) / 50, 10)  # Max 10 point penalty
            score -= penalty
            issues.append(f"Empty directories: {empty_dirs}")
        
        return max(0, int(score)), issues
    
    def display_dashboard(self):
        """Display comprehensive dashboard"""
        if not self.data:
            return
        
        print("=" * 80)
        print("🎹 EXS24 MASTER LIBRARY - DASHBOARD")
        print("=" * 80)
        print()
        
        # Health Score
        health_score, issues = self.get_health_score()
        health_emoji = "🟢" if health_score >= 80 else "🟡" if health_score >= 60 else "🔴"
        print(f"{health_emoji} Library Health Score: {health_score}/100")
        if issues:
            print("   Issues:")
            for issue in issues:
                print(f"     • {issue}")
        print()
        
        # Quick Stats
        print("📊 QUICK STATS")
        print("-" * 80)
        total_files = self.data.get('exs_file_count', 0)
        total_dirs = self.data.get('total_dirs', 0)
        total_size_mb = self.data.get('file_sizes', {}).get('total', 0) / (1024 * 1024)
        collections = len(self.data.get('collections', {}))
        
        print(f"  Total Instruments:    {total_files:,}")
        print(f"  Collections:          {collections:,}")
        print(f"  Total Directories:   {total_dirs:,}")
        print(f"  Library Size:        {total_size_mb:,.2f} MB")
        print()
        
        # Top Collections
        collections_data = self.data.get('collections', {})
        if collections_data:
            print("📚 TOP 10 COLLECTIONS")
            print("-" * 80)
            sorted_collections = sorted(
                collections_data.items(),
                key=lambda x: x[1] if isinstance(x[1], int) else len(x[1]),
                reverse=True
            )[:10]
            
            for i, (collection, count) in enumerate(sorted_collections, 1):
                if isinstance(count, list):
                    count = len(count)
                size_mb = self.data.get('file_sizes', {}).get('by_collection', {}).get(collection, 0) / (1024 * 1024)
                print(f"  {i:2d}. {collection:40s} {count:5,} files  {size_mb:6.2f} MB")
            print()
        
        # Issues Summary
        print("⚠️  ISSUES SUMMARY")
        print("-" * 80)
        naming = len(self.data.get('naming_inconsistencies', []))
        loose = len(self.data.get('loose_files', []))
        dupes = len(self.data.get('duplicates', {}))
        true_dupes = len(self.data.get('duplicates_by_hash', {}))
        empty = len(self.data.get('empty_dirs', []))
        
        if naming > 0:
            print(f"  • Naming inconsistencies: {naming:,} files")
        if loose > 0:
            print(f"  • Loose files: {loose:,} files")
        if dupes > 0:
            print(f"  • Duplicate filenames: {dupes:,} groups")
        if true_dupes > 0:
            print(f"  • True duplicates: {true_dupes:,} groups")
        if empty > 0:
            print(f"  • Empty directories: {empty:,}")
        
        if naming == 0 and loose == 0 and dupes == 0 and true_dupes == 0 and empty == 0:
            print("  ✅ No issues detected!")
        print()
        
        # Recent Scan Info
        scan_date = self.data.get('scan_date', 'Unknown')
        print(f"📅 Last Scan: {scan_date}")
        print()
        
        # Recommendations
        print("💡 RECOMMENDATIONS")
        print("-" * 80)
        recommendations = []
        
        if naming > 0:
            recommendations.append(f"Run CLEANUP_NAMING.py to fix {naming:,} naming issues")
        if loose > 0:
            recommendations.append(f"Run ORGANIZE_LOOSE_FILES.py to organize {loose:,} loose files")
        if true_dupes > 0:
            recommendations.append(f"Run DUPLICATE_ANALYZER.py to review {true_dupes:,} duplicate groups")
        if not recommendations:
            recommendations.append("Library is in excellent condition! ✅")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
        print()
        
        print("=" * 80)


def main():
    dashboard = LibraryDashboard()
    dashboard.display_dashboard()


if __name__ == "__main__":
    main()




