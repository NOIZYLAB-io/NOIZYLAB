#!/usr/bin/env python3
"""
EXS24 Master Library - Advanced Scan & Organize Tool
Comprehensive analysis and organization of EXS24 sampler instrument library
Enhanced with file size analysis, collection statistics, and more
"""

import os
import json
import hashlib
from collections import defaultdict
from pathlib import Path
from datetime import datetime

class EXS24Scanner:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.stats = {
            'total_files': 0,
            'total_dirs': 0,
            'exs_files': [],
            'exs_files_detailed': [],  # New: detailed file info
            'dir_structure': defaultdict(list),
            'issues': [],
            'duplicates': defaultdict(list),
            'duplicates_by_hash': defaultdict(list),  # New: true duplicates
            'loose_files': [],
            'naming_inconsistencies': [],
            'collections': defaultdict(list),  # New: collection stats
            'file_sizes': {'total': 0, 'by_collection': defaultdict(int)},  # New: size tracking
            'empty_dirs': []  # New: empty directories
        }
        
    def get_file_hash(self, file_path, chunk_size=8192):
        """Calculate MD5 hash of file for duplicate detection"""
        try:
            hash_md5 = hashlib.md5()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(chunk_size), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except (IOError, OSError):
            return None
    
    def get_collection_name(self, file_path):
        """Extract collection name from file path"""
        parts = Path(file_path).parts
        # Look for collection name (usually at depth 3-4)
        # Path structure: 12TB_ROOT/FLIP 4TB 01/__2025 PROJECT EXS24/[COLLECTION]/...
        for i, part in enumerate(parts):
            if part == '__2025 PROJECT EXS24' and i + 1 < len(parts):
                return parts[i + 1]
            # Also check for direct collection folders
            if 'PROJECT EXS24' in part and i + 1 < len(parts):
                # Check if next part is a collection (not a subfolder like "SAMPLER INST")
                next_part = parts[i + 1]
                if next_part not in ['SAMPLER INST.', 'INSTRUMENTS', 'EXS24', 'INSTRUMENTS_EXS']:
                    return next_part
        # Fallback: try to get collection from path structure
        if len(parts) >= 4:
            # Usually collection is at index 3
            if parts[2] == '__2025 PROJECT EXS24' or 'PROJECT EXS24' in parts[2]:
                return parts[3] if len(parts) > 3 else 'UNKNOWN'
        return 'UNKNOWN'
    
    def scan(self):
        """Perform comprehensive scan of the directory structure"""
        print("🔍 Scanning EXS24 Master Library...")
        print("   Analyzing files, sizes, collections, and duplicates...")
        
        file_hashes = {}  # Track file hashes for true duplicate detection
        
        # Scan all files and directories
        for root, dirs, files in os.walk(self.root_path):
            root_path = Path(root)
            rel_path = root_path.relative_to(self.root_path)
            
            self.stats['total_dirs'] += 1
            
            # Check if directory is empty
            if not files and not dirs and rel_path != Path('.'):
                self.stats['empty_dirs'].append(str(rel_path))
            
            # Check for EXS24 files
            for file in files:
                self.stats['total_files'] += 1
                file_path = root_path / file
                
                if file.lower().endswith(('.exs', '.exs24')):
                    rel_file_path = file_path.relative_to(self.root_path)
                    rel_file_str = str(rel_file_path)
                    self.stats['exs_files'].append(rel_file_str)
                    
                    # Get file details
                    try:
                        file_size = file_path.stat().st_size
                        collection = self.get_collection_name(rel_file_str)
                        
                        file_info = {
                            'path': rel_file_str,
                            'name': file,
                            'size': file_size,
                            'collection': collection,
                            'depth': len(rel_path.parts)
                        }
                        self.stats['exs_files_detailed'].append(file_info)
                        
                        # Track file sizes
                        self.stats['file_sizes']['total'] += file_size
                        self.stats['file_sizes']['by_collection'][collection] += file_size
                        
                        # Track collections
                        self.stats['collections'][collection].append(rel_file_str)
                        
                    except (OSError, IOError):
                        pass
                    
                    # Track directory structure
                    depth = len(rel_path.parts)
                    self.stats['dir_structure'][depth].append(rel_file_str)
                    
                    # Check for loose files (at shallow depth)
                    if depth <= 3:
                        self.stats['loose_files'].append(rel_file_str)
                    
                    # Check for naming inconsistencies
                    if file.endswith('.exs.EXS') or file.endswith('.EXS.exs'):
                        self.stats['naming_inconsistencies'].append(rel_file_str)
                    
                    # Calculate file hash for true duplicate detection
                    file_hash = self.get_file_hash(file_path)
                    if file_hash:
                        if file_hash not in file_hashes:
                            file_hashes[file_hash] = []
                        file_hashes[file_hash].append(rel_file_str)
        
        # Find potential duplicates by filename
        filename_map = defaultdict(list)
        for exs_file in self.stats['exs_files']:
            filename = os.path.basename(exs_file)
            filename_map[filename.lower()].append(exs_file)
        
        for filename, paths in filename_map.items():
            if len(paths) > 1:
                self.stats['duplicates'][filename] = paths
        
        # Find true duplicates by hash
        for file_hash, paths in file_hashes.items():
            if len(paths) > 1:
                self.stats['duplicates_by_hash'][file_hash] = paths
        
        print(f"✅ Scan complete: {len(self.stats['exs_files'])} EXS24 files found")
        print(f"   {len(self.stats['collections'])} collections identified")
        print(f"   {len(self.stats['duplicates_by_hash'])} true duplicate groups found")
        return self.stats
    
    def analyze_structure(self):
        """Analyze directory structure for organizational issues"""
        print("\n📊 Analyzing structure...")
        
        # Check for common organizational issues
        issues = []
        
        # Check depth distribution
        depth_dist = defaultdict(int)
        for depth, files in self.stats['dir_structure'].items():
            depth_dist[depth] = len(files)
        
        max_depth = max(depth_dist.keys()) if depth_dist else 0
        if max_depth > 10:
            issues.append(f"⚠️  Very deep nesting detected (max depth: {max_depth})")
        
        # Check for inconsistent naming patterns
        if self.stats['naming_inconsistencies']:
            issues.append(f"⚠️  Found {len(self.stats['naming_inconsistencies'])} files with inconsistent extensions")
        
        # Check for duplicates
        if self.stats['duplicates']:
            issues.append(f"⚠️  Found {len(self.stats['duplicates'])} potentially duplicate filenames")
        
        # Check for loose files
        if self.stats['loose_files']:
            issues.append(f"⚠️  Found {len(self.stats['loose_files'])} files at shallow depth (may need organization)")
        
        self.stats['issues'] = issues
        return issues
    
    def generate_report(self):
        """Generate comprehensive organization report"""
        report = []
        report.append("=" * 80)
        report.append("EXS24 MASTER LIBRARY - SCAN & ORGANIZE REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary Statistics
        report.append("📈 SUMMARY STATISTICS")
        report.append("-" * 80)
        report.append(f"Total Files:           {self.stats['total_files']:,}")
        report.append(f"Total Directories:    {self.stats['total_dirs']:,}")
        report.append(f"EXS24 Files:          {len(self.stats['exs_files']):,}")
        report.append("")
        
        # Directory Depth Analysis
        report.append("📁 DIRECTORY DEPTH ANALYSIS")
        report.append("-" * 80)
        depth_dist = defaultdict(int)
        for depth, files in self.stats['dir_structure'].items():
            depth_dist[depth] = len(files)
        
        for depth in sorted(depth_dist.keys()):
            count = depth_dist[depth]
            bar = "█" * (count // 100) if count > 100 else "▌" * (count // 10)
            report.append(f"Depth {depth:2d}: {count:6,} files {bar}")
        report.append("")
        
        # Issues Found
        if self.stats['issues']:
            report.append("⚠️  ISSUES DETECTED")
            report.append("-" * 80)
            for issue in self.stats['issues']:
                report.append(f"  {issue}")
            report.append("")
        
        # Duplicates
        if self.stats['duplicates']:
            report.append("🔄 POTENTIAL DUPLICATES (Top 20)")
            report.append("-" * 80)
            sorted_dups = sorted(self.stats['duplicates'].items(), 
                               key=lambda x: len(x[1]), reverse=True)[:20]
            for filename, paths in sorted_dups:
                report.append(f"  {filename} ({len(paths)} copies)")
                for path in paths[:3]:  # Show first 3 paths
                    report.append(f"    - {path}")
                if len(paths) > 3:
                    report.append(f"    ... and {len(paths) - 3} more")
            report.append("")
        
        # Loose Files
        if self.stats['loose_files']:
            report.append("📦 LOOSE FILES (at depth ≤ 3)")
            report.append("-" * 80)
            for file in self.stats['loose_files'][:20]:
                report.append(f"  {file}")
            if len(self.stats['loose_files']) > 20:
                report.append(f"  ... and {len(self.stats['loose_files']) - 20} more")
            report.append("")
        
        # Naming Inconsistencies
        if self.stats['naming_inconsistencies']:
            report.append("📝 NAMING INCONSISTENCIES")
            report.append("-" * 80)
            for file in self.stats['naming_inconsistencies'][:20]:
                report.append(f"  {file}")
            if len(self.stats['naming_inconsistencies']) > 20:
                report.append(f"  ... and {len(self.stats['naming_inconsistencies']) - 20} more")
            report.append("")
        
        # Collection Statistics
        report.append("📚 COLLECTION STATISTICS (Top 20)")
        report.append("-" * 80)
        sorted_collections = sorted(
            self.stats['collections'].items(),
            key=lambda x: len(x[1]),
            reverse=True
        )[:20]
        
        for collection, files in sorted_collections:
            file_count = len(files)
            size_mb = self.stats['file_sizes']['by_collection'][collection] / (1024 * 1024)
            report.append(f"  {collection:40s} {file_count:5,} files  {size_mb:7.2f} MB")
        report.append("")
        
        # True Duplicates (by hash)
        if self.stats['duplicates_by_hash']:
            report.append("🔄 TRUE DUPLICATES (by file content)")
            report.append("-" * 80)
            sorted_hash_dups = sorted(
                self.stats['duplicates_by_hash'].items(),
                key=lambda x: len(x[1]),
                reverse=True
            )[:10]
            for file_hash, paths in sorted_hash_dups:
                report.append(f"  Hash: {file_hash[:16]}... ({len(paths)} identical files)")
                for path in paths[:3]:
                    report.append(f"    - {path}")
                if len(paths) > 3:
                    report.append(f"    ... and {len(paths) - 3} more")
            report.append("")
        
        # File Size Statistics
        total_size_mb = self.stats['file_sizes']['total'] / (1024 * 1024)
        avg_size_kb = (self.stats['file_sizes']['total'] / len(self.stats['exs_files']) / 1024) if self.stats['exs_files'] else 0
        report.append("💾 FILE SIZE STATISTICS")
        report.append("-" * 80)
        report.append(f"Total Library Size:    {total_size_mb:,.2f} MB")
        report.append(f"Average File Size:     {avg_size_kb:.2f} KB")
        if self.stats['exs_files_detailed']:
            sizes = [f['size'] for f in self.stats['exs_files_detailed']]
            report.append(f"Largest File:          {max(sizes) / 1024:.2f} KB")
            report.append(f"Smallest File:         {min(sizes) / 1024:.2f} KB")
        report.append("")
        
        # Top Level Structure
        report.append("🗂️  TOP-LEVEL STRUCTURE")
        report.append("-" * 80)
        top_level_dirs = set()
        for exs_file in self.stats['exs_files']:
            parts = Path(exs_file).parts
            if len(parts) > 0:
                top_level_dirs.add(parts[0])
        
        for dir_name in sorted(top_level_dirs):
            count = sum(1 for f in self.stats['exs_files'] 
                       if Path(f).parts[0] == dir_name)
            report.append(f"  {dir_name}/ ({count:,} files)")
        report.append("")
        
        # Empty Directories
        if self.stats['empty_dirs']:
            report.append("📁 EMPTY DIRECTORIES")
            report.append("-" * 80)
            for empty_dir in self.stats['empty_dirs'][:20]:
                report.append(f"  {empty_dir}")
            if len(self.stats['empty_dirs']) > 20:
                report.append(f"  ... and {len(self.stats['empty_dirs']) - 20} more")
            report.append("")
        
        report.append("=" * 80)
        report.append("END OF REPORT")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_report(self, output_file="SCAN_REPORT.txt"):
        """Save report to file"""
        report = self.generate_report()
        report_path = self.root_path / output_file
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n💾 Report saved to: {report_path}")
        return report_path
    
    def save_json(self, output_file="SCAN_DATA.json"):
        """Save detailed data as JSON"""
        json_path = self.root_path / output_file
        # Convert Path objects to strings for JSON serialization
        json_data = {
            'scan_date': datetime.now().isoformat(),
            'total_files': self.stats['total_files'],
            'total_dirs': self.stats['total_dirs'],
            'exs_file_count': len(self.stats['exs_files']),
            'exs_files': self.stats['exs_files'],
            'exs_files_detailed': self.stats['exs_files_detailed'],
            'duplicates': {k: v for k, v in self.stats['duplicates'].items()},
            'duplicates_by_hash': {k: v for k, v in self.stats['duplicates_by_hash'].items()},
            'loose_files': self.stats['loose_files'],
            'naming_inconsistencies': self.stats['naming_inconsistencies'],
            'collections': {k: len(v) for k, v in self.stats['collections'].items()},
            'file_sizes': {
                'total': self.stats['file_sizes']['total'],
                'by_collection': dict(self.stats['file_sizes']['by_collection'])
            },
            'empty_dirs': self.stats['empty_dirs'],
            'issues': self.stats['issues']
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        print(f"💾 JSON data saved to: {json_path}")
        return json_path
    
    def generate_collection_report(self):
        """Generate detailed collection statistics report"""
        report = []
        report.append("=" * 80)
        report.append("EXS24 MASTER LIBRARY - COLLECTION DETAILS")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        sorted_collections = sorted(
            self.stats['collections'].items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        for collection, files in sorted_collections:
            file_count = len(files)
            size_mb = self.stats['file_sizes']['by_collection'][collection] / (1024 * 1024)
            report.append(f"{collection}")
            report.append(f"  Files: {file_count:,}  |  Size: {size_mb:.2f} MB")
            report.append("")
        
        return "\n".join(report)
    
    def save_collection_report(self, output_file="COLLECTION_REPORT.txt"):
        """Save collection report to file"""
        report = self.generate_collection_report()
        report_path = self.root_path / output_file
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"💾 Collection report saved to: {report_path}")
        return report_path


def main():
    root_path = Path(__file__).parent
    scanner = EXS24Scanner(root_path)
    
    # Perform scan
    scanner.scan()
    
    # Analyze structure
    scanner.analyze_structure()
    
    # Generate and save reports
    scanner.save_report()
    scanner.save_json()
    scanner.save_collection_report()
    
    # Print summary
    print("\n" + scanner.generate_report())
    
    print("\n✨ Advanced scan complete! Check the generated reports for details.")


if __name__ == "__main__":
    main()

