#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║            TOONTRACK EZDRUMMER MASTER LIBRARY MANAGEMENT SYSTEM              ║
║                    TEST • SCAN • HEAL • OPTIMIZE • ORGANIZE                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

Features:
  - Multi-drive scanning for all Toontrack content
  - File integrity testing with hash verification
  - Automatic healing of permissions and structure
  - Deep scan with duplicate detection
  - Smart rename and reorganization into master library
  - Comprehensive reporting

Author: NOIZYLAB
Version: 1.0.0
"""

import os
import sys
import json
import hashlib
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Set, Tuple
from collections import defaultdict
import re


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Config:
    """Master configuration for Toontrack library management"""
    
    # Drives to scan
    SCAN_VOLUMES: List[str] = field(default_factory=lambda: [
        "/Volumes/6TB",
        "/Volumes/4TBSG",
        "/Volumes/SAMPLE_MASTER",
        "/Volumes/4TB Lacie",
        "/Volumes/SOUND_DESIGN",
        "/Volumes/EW",
        "/Volumes/12TB",
        "/Volumes/FISH",
    ])
    
    # Master library destination
    MASTER_LIBRARY: str = "/Volumes/SAMPLE_MASTER/06_Drums_Percussion/Toontrack_Master"
    
    # Toontrack file patterns
    TOONTRACK_EXTENSIONS: Set[str] = field(default_factory=lambda: {
        '.ezx', '.ezd', '.tci', '.sdx', '.sd3p',  # Sound data
        '.ezdrummer', '.ezdrummer2', '.ezdrummer3',  # Presets
        '.midi', '.mid',  # MIDI files
        '.wav', '.aif', '.aiff',  # Audio samples
        '.xml', '.dat', '.db', '.ezdb',  # Databases
    })
    
    # Folder patterns to identify Toontrack content
    FOLDER_PATTERNS: List[str] = field(default_factory=lambda: [
        'toontrack', 'ezdrummer', 'ezx', 'superior', 'sdx', 
        'ez_drummer', 'sd3', 'sd2', 'drummer'
    ])
    
    # Category mappings for organization
    CATEGORY_MAP: Dict[str, str] = field(default_factory=lambda: {
        'ezx2': 'EZDrummer2_Expansions',
        'ezx3': 'EZDrummer3_Expansions',
        'ezx_': 'EZDrummer_Classic_Expansions',
        'ezxp': 'EZDrummer_Percussion',
        'sdx': 'Superior_Drummer_Expansions',
        'core': 'Core_Libraries',
        'midi': 'MIDI_Grooves',
        'database': 'Databases',
    })
    
    # Report output
    REPORT_DIR: str = "/Users/m2ultra/NOIZYLAB/CODE_MASTER/Toontrack_EZDrummer/reports"
    
    # Cache file for faster repeat scans
    CACHE_FILE: str = "/Users/m2ultra/NOIZYLAB/CODE_MASTER/Toontrack_EZDrummer/.scan_cache.json"


# ═══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ToontrackItem:
    """Represents a single Toontrack file or folder"""
    path: str
    name: str
    item_type: str  # 'file' or 'folder'
    size: int = 0
    extension: str = ""
    category: str = "uncategorized"
    hash_md5: str = ""
    last_modified: str = ""
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)
    
    def to_dict(self):
        return asdict(self)


@dataclass
class ScanResult:
    """Results from a scan operation"""
    timestamp: str
    total_items: int = 0
    total_size_gb: float = 0.0
    files: List[ToontrackItem] = field(default_factory=list)
    folders: List[ToontrackItem] = field(default_factory=list)
    duplicates: Dict[str, List[str]] = field(default_factory=dict)
    issues: List[Dict] = field(default_factory=list)
    volumes_scanned: List[str] = field(default_factory=list)


# ═══════════════════════════════════════════════════════════════════════════════
# SCANNER ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class ToontrackScanner:
    """Multi-drive scanner for Toontrack content"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.results = ScanResult(timestamp=datetime.now().isoformat())
        self._hash_cache = {}
        
    def scan(self, quick: bool = False) -> ScanResult:
        """Perform full scan across all configured volumes"""
        print("\n" + "═" * 70)
        print("   🔍 TOONTRACK SCANNER - Starting Multi-Volume Scan")
        print("═" * 70)
        
        for volume in self.config.SCAN_VOLUMES:
            if os.path.exists(volume):
                print(f"\n📂 Scanning: {volume}")
                self._scan_volume(volume, quick)
            else:
                print(f"⚠️  Volume not mounted: {volume}")
        
        # Calculate totals
        self.results.total_items = len(self.results.files) + len(self.results.folders)
        self.results.total_size_gb = sum(f.size for f in self.results.files) / (1024**3)
        
        return self.results
    
    def _scan_volume(self, volume: str, quick: bool = False):
        """Scan a single volume for Toontrack content"""
        toontrack_paths = self._find_toontrack_paths(volume)
        
        for path in toontrack_paths:
            self._process_path(path, quick)
            
    def _find_toontrack_paths(self, volume: str) -> List[str]:
        """Find all Toontrack-related paths in a volume"""
        paths = []
        
        # Search common locations
        search_dirs = [
            os.path.join(volume, "_ORGANIZED"),
            os.path.join(volume, "Sample_Libraries"),
            os.path.join(volume, "Applications"),
            os.path.join(volume, "Toontrack"),
            os.path.join(volume, "EZDrummer"),
            volume,
        ]
        
        for search_dir in search_dirs:
            if not os.path.exists(search_dir):
                continue
                
            try:
                for entry in os.scandir(search_dir):
                    name_lower = entry.name.lower()
                    if any(pattern in name_lower for pattern in self.config.FOLDER_PATTERNS):
                        paths.append(entry.path)
                        self.results.volumes_scanned.append(entry.path)
            except PermissionError:
                continue
                
        return paths
    
    def _process_path(self, path: str, quick: bool = False):
        """Process a Toontrack path and catalog its contents"""
        if os.path.isfile(path):
            self._process_file(path, quick)
        elif os.path.isdir(path):
            self._process_folder(path, quick)
            
    def _process_folder(self, folder_path: str, quick: bool = False):
        """Process a folder and all its contents"""
        try:
            folder_size = 0
            
            for root, dirs, files in os.walk(folder_path):
                # Skip hidden folders
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                for file in files:
                    if file.startswith('.'):
                        continue
                    file_path = os.path.join(root, file)
                    item = self._process_file(file_path, quick)
                    if item:
                        folder_size += item.size
            
            # Create folder item
            folder_item = ToontrackItem(
                path=folder_path,
                name=os.path.basename(folder_path),
                item_type='folder',
                size=folder_size,
                category=self._categorize(folder_path),
                last_modified=datetime.fromtimestamp(os.path.getmtime(folder_path)).isoformat()
            )
            self.results.folders.append(folder_item)
            print(f"   ✓ {folder_item.name}: {folder_size / (1024**3):.2f} GB")
            
        except Exception as e:
            self.results.issues.append({
                'path': folder_path,
                'error': str(e),
                'type': 'scan_error'
            })
    
    def _process_file(self, file_path: str, quick: bool = False) -> Optional[ToontrackItem]:
        """Process a single file"""
        try:
            stat = os.stat(file_path)
            ext = os.path.splitext(file_path)[1].lower()
            
            item = ToontrackItem(
                path=file_path,
                name=os.path.basename(file_path),
                item_type='file',
                size=stat.st_size,
                extension=ext,
                category=self._categorize(file_path),
                last_modified=datetime.fromtimestamp(stat.st_mtime).isoformat()
            )
            
            # Calculate hash for duplicate detection (skip for large files in quick mode)
            if not quick and stat.st_size < 100 * 1024 * 1024:  # < 100MB
                item.hash_md5 = self._calculate_hash(file_path)
                
                # Track for duplicate detection
                if item.hash_md5:
                    if item.hash_md5 not in self.results.duplicates:
                        self.results.duplicates[item.hash_md5] = []
                    self.results.duplicates[item.hash_md5].append(file_path)
            
            self.results.files.append(item)
            return item
            
        except Exception as e:
            self.results.issues.append({
                'path': file_path,
                'error': str(e),
                'type': 'file_error'
            })
            return None
    
    def _categorize(self, path: str) -> str:
        """Determine category based on path/name"""
        path_lower = path.lower()
        
        for pattern, category in self.config.CATEGORY_MAP.items():
            if pattern in path_lower:
                return category
                
        return "uncategorized"
    
    def _calculate_hash(self, file_path: str, chunk_size: int = 8192) -> str:
        """Calculate MD5 hash of a file"""
        if file_path in self._hash_cache:
            return self._hash_cache[file_path]
            
        try:
            hasher = hashlib.md5()
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
            hash_value = hasher.hexdigest()
            self._hash_cache[file_path] = hash_value
            return hash_value
        except:
            return ""


# ═══════════════════════════════════════════════════════════════════════════════
# INTEGRITY TESTER
# ═══════════════════════════════════════════════════════════════════════════════

class IntegrityTester:
    """Test file integrity and identify issues"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.test_results = []
        
    def test(self, scan_result: ScanResult) -> List[Dict]:
        """Run integrity tests on scanned content"""
        print("\n" + "═" * 70)
        print("   🧪 INTEGRITY TESTER - Verifying File Health")
        print("═" * 70)
        
        total = len(scan_result.files)
        tested = 0
        issues_found = 0
        
        for item in scan_result.files:
            tested += 1
            issues = self._test_item(item)
            
            if issues:
                issues_found += len(issues)
                item.issues.extend(issues)
                item.is_valid = False
                self.test_results.extend(issues)
            
            if tested % 100 == 0:
                print(f"   Progress: {tested}/{total} files tested...")
        
        print(f"\n   ✓ Tested {tested} files")
        print(f"   {'⚠️' if issues_found else '✓'} Found {issues_found} issues")
        
        return self.test_results
    
    def _test_item(self, item: ToontrackItem) -> List[Dict]:
        """Test a single item for issues"""
        issues = []
        
        # Check file exists
        if not os.path.exists(item.path):
            issues.append({
                'path': item.path,
                'type': 'missing',
                'message': 'File does not exist'
            })
            return issues
        
        # Check permissions
        if not os.access(item.path, os.R_OK):
            issues.append({
                'path': item.path,
                'type': 'permission',
                'message': 'File is not readable'
            })
        
        # Check for zero-size files (potential corruption)
        if item.size == 0 and item.extension in {'.ezx', '.tci', '.sdx', '.wav', '.mid'}:
            issues.append({
                'path': item.path,
                'type': 'empty',
                'message': 'File is empty (possible corruption)'
            })
        
        # Check for broken symlinks
        if os.path.islink(item.path) and not os.path.exists(os.path.realpath(item.path)):
            issues.append({
                'path': item.path,
                'type': 'broken_link',
                'message': 'Broken symbolic link'
            })
        
        # Check for naming issues
        if any(c in item.name for c in ['<', '>', ':', '"', '|', '?', '*']):
            issues.append({
                'path': item.path,
                'type': 'invalid_chars',
                'message': 'Filename contains invalid characters'
            })
        
        return issues


# ═══════════════════════════════════════════════════════════════════════════════
# HEALER
# ═══════════════════════════════════════════════════════════════════════════════

class ToontrackHealer:
    """Heal and fix issues in the library"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.healed = []
        self.failed = []
        
    def heal(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        """Heal issues found in scan"""
        print("\n" + "═" * 70)
        print(f"   🔧 HEALER - {'DRY RUN' if dry_run else 'APPLYING FIXES'}")
        print("═" * 70)
        
        # Fix permissions
        self._heal_permissions(scan_result, dry_run)
        
        # Fix broken links
        self._heal_broken_links(scan_result, dry_run)
        
        # Fix folder structure
        self._heal_structure(scan_result, dry_run)
        
        return {
            'healed': self.healed,
            'failed': self.failed,
            'dry_run': dry_run
        }
    
    def _heal_permissions(self, scan_result: ScanResult, dry_run: bool):
        """Fix permission issues"""
        print("\n   📝 Fixing Permissions...")
        
        for item in scan_result.files + scan_result.folders:
            if any(i['type'] == 'permission' for i in item.issues):
                if dry_run:
                    print(f"      Would fix: {item.path}")
                    self.healed.append({'path': item.path, 'action': 'chmod', 'dry_run': True})
                else:
                    try:
                        os.chmod(item.path, 0o644 if item.item_type == 'file' else 0o755)
                        print(f"      Fixed: {item.path}")
                        self.healed.append({'path': item.path, 'action': 'chmod', 'success': True})
                    except Exception as e:
                        self.failed.append({'path': item.path, 'error': str(e)})
    
    def _heal_broken_links(self, scan_result: ScanResult, dry_run: bool):
        """Remove or relink broken symbolic links"""
        print("\n   🔗 Fixing Broken Links...")
        
        for item in scan_result.files:
            if any(i['type'] == 'broken_link' for i in item.issues):
                if dry_run:
                    print(f"      Would remove: {item.path}")
                    self.healed.append({'path': item.path, 'action': 'unlink', 'dry_run': True})
                else:
                    try:
                        os.unlink(item.path)
                        print(f"      Removed: {item.path}")
                        self.healed.append({'path': item.path, 'action': 'unlink', 'success': True})
                    except Exception as e:
                        self.failed.append({'path': item.path, 'error': str(e)})
    
    def _heal_structure(self, scan_result: ScanResult, dry_run: bool):
        """Create missing required directories"""
        print("\n   📁 Verifying Structure...")
        
        master_lib = Path(self.config.MASTER_LIBRARY)
        required_dirs = [
            master_lib / "EZDrummer2_Expansions",
            master_lib / "EZDrummer3_Expansions",
            master_lib / "EZDrummer_Classic_Expansions",
            master_lib / "Superior_Drummer_Expansions",
            master_lib / "Core_Libraries",
            master_lib / "MIDI_Grooves",
            master_lib / "Databases",
        ]
        
        for dir_path in required_dirs:
            if not dir_path.exists():
                if dry_run:
                    print(f"      Would create: {dir_path}")
                else:
                    dir_path.mkdir(parents=True, exist_ok=True)
                    print(f"      Created: {dir_path}")


# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZER
# ═══════════════════════════════════════════════════════════════════════════════

class ToontrackOptimizer:
    """Optimize library by removing duplicates and consolidating"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def optimize(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        """Optimize the library"""
        print("\n" + "═" * 70)
        print(f"   ⚡ OPTIMIZER - {'DRY RUN' if dry_run else 'APPLYING OPTIMIZATION'}")
        print("═" * 70)
        
        results = {
            'duplicates_removed': [],
            'space_saved_gb': 0,
            'recommendations': []
        }
        
        # Find and handle duplicates
        duplicates = self._find_duplicates(scan_result)
        
        print(f"\n   Found {len(duplicates)} duplicate groups")
        
        for hash_val, paths in duplicates.items():
            if len(paths) > 1:
                # Keep the one in master library or first one
                master_paths = [p for p in paths if self.config.MASTER_LIBRARY in p]
                keep = master_paths[0] if master_paths else paths[0]
                
                for path in paths:
                    if path != keep:
                        try:
                            size = os.path.getsize(path)
                            if dry_run:
                                print(f"      Would remove duplicate: {path}")
                            else:
                                os.remove(path)
                                print(f"      Removed duplicate: {path}")
                            results['duplicates_removed'].append(path)
                            results['space_saved_gb'] += size / (1024**3)
                        except Exception as e:
                            print(f"      Error: {e}")
        
        print(f"\n   💾 Potential space savings: {results['space_saved_gb']:.2f} GB")
        
        return results
    
    def _find_duplicates(self, scan_result: ScanResult) -> Dict[str, List[str]]:
        """Find actual duplicates (same hash, multiple locations)"""
        return {
            hash_val: paths 
            for hash_val, paths in scan_result.duplicates.items() 
            if len(paths) > 1 and hash_val
        }


# ═══════════════════════════════════════════════════════════════════════════════
# DEEP SCANNER
# ═══════════════════════════════════════════════════════════════════════════════

class DeepScanner:
    """Deep scan with comprehensive analysis"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def deep_scan(self, scan_result: ScanResult) -> Dict:
        """Perform deep analysis"""
        print("\n" + "═" * 70)
        print("   🔬 DEEP SCANNER - Comprehensive Analysis")
        print("═" * 70)
        
        analysis = {
            'summary': self._generate_summary(scan_result),
            'by_category': self._analyze_by_category(scan_result),
            'by_extension': self._analyze_by_extension(scan_result),
            'by_volume': self._analyze_by_volume(scan_result),
            'largest_files': self._find_largest(scan_result),
            'oldest_files': self._find_oldest(scan_result),
            'recommendations': self._generate_recommendations(scan_result),
        }
        
        # Print analysis
        self._print_analysis(analysis)
        
        return analysis
    
    def _generate_summary(self, result: ScanResult) -> Dict:
        """Generate summary statistics"""
        return {
            'total_files': len(result.files),
            'total_folders': len(result.folders),
            'total_size_gb': result.total_size_gb,
            'unique_extensions': len(set(f.extension for f in result.files)),
            'issues_count': len(result.issues),
            'duplicate_groups': len([d for d in result.duplicates.values() if len(d) > 1]),
        }
    
    def _analyze_by_category(self, result: ScanResult) -> Dict:
        """Analyze content by category"""
        categories = defaultdict(lambda: {'count': 0, 'size': 0})
        
        for item in result.files:
            categories[item.category]['count'] += 1
            categories[item.category]['size'] += item.size
            
        return dict(categories)
    
    def _analyze_by_extension(self, result: ScanResult) -> Dict:
        """Analyze content by file extension"""
        extensions = defaultdict(lambda: {'count': 0, 'size': 0})
        
        for item in result.files:
            ext = item.extension or 'no_extension'
            extensions[ext]['count'] += 1
            extensions[ext]['size'] += item.size
            
        return dict(extensions)
    
    def _analyze_by_volume(self, result: ScanResult) -> Dict:
        """Analyze content by volume"""
        volumes = defaultdict(lambda: {'count': 0, 'size': 0})
        
        for item in result.files:
            # Extract volume from path
            parts = item.path.split('/')
            if len(parts) > 2:
                volume = '/'.join(parts[:3])
                volumes[volume]['count'] += 1
                volumes[volume]['size'] += item.size
                
        return dict(volumes)
    
    def _find_largest(self, result: ScanResult, limit: int = 10) -> List[Dict]:
        """Find largest files"""
        sorted_files = sorted(result.files, key=lambda x: x.size, reverse=True)
        return [
            {'path': f.path, 'size_gb': f.size / (1024**3), 'category': f.category}
            for f in sorted_files[:limit]
        ]
    
    def _find_oldest(self, result: ScanResult, limit: int = 10) -> List[Dict]:
        """Find oldest files"""
        sorted_files = sorted(result.files, key=lambda x: x.last_modified)
        return [
            {'path': f.path, 'modified': f.last_modified, 'category': f.category}
            for f in sorted_files[:limit]
        ]
    
    def _generate_recommendations(self, result: ScanResult) -> List[str]:
        """Generate optimization recommendations"""
        recs = []
        
        # Check for duplicates
        dup_count = len([d for d in result.duplicates.values() if len(d) > 1])
        if dup_count > 0:
            recs.append(f"Remove {dup_count} duplicate file groups to save space")
        
        # Check for issues
        if result.issues:
            recs.append(f"Fix {len(result.issues)} identified issues using heal command")
        
        # Check for uncategorized content
        uncategorized = [f for f in result.files if f.category == 'uncategorized']
        if len(uncategorized) > 10:
            recs.append(f"Organize {len(uncategorized)} uncategorized files")
        
        # Check library spread
        volumes = set(f.path.split('/')[2] for f in result.files if len(f.path.split('/')) > 2)
        if len(volumes) > 2:
            recs.append("Consider consolidating content to fewer drives for better performance")
        
        return recs
    
    def _print_analysis(self, analysis: Dict):
        """Print analysis results"""
        print("\n   📊 SUMMARY")
        print("   " + "-" * 40)
        summary = analysis['summary']
        print(f"   Total Files: {summary['total_files']:,}")
        print(f"   Total Folders: {summary['total_folders']:,}")
        print(f"   Total Size: {summary['total_size_gb']:.2f} GB")
        print(f"   Unique Extensions: {summary['unique_extensions']}")
        print(f"   Issues Found: {summary['issues_count']}")
        print(f"   Duplicate Groups: {summary['duplicate_groups']}")
        
        print("\n   📁 BY CATEGORY")
        print("   " + "-" * 40)
        for cat, data in sorted(analysis['by_category'].items(), key=lambda x: x[1]['size'], reverse=True):
            size_gb = data['size'] / (1024**3)
            print(f"   {cat}: {data['count']} files, {size_gb:.2f} GB")
        
        print("\n   💡 RECOMMENDATIONS")
        print("   " + "-" * 40)
        for i, rec in enumerate(analysis['recommendations'], 1):
            print(f"   {i}. {rec}")


# ═══════════════════════════════════════════════════════════════════════════════
# ORGANIZER
# ═══════════════════════════════════════════════════════════════════════════════

class ToontrackOrganizer:
    """Rename and reorganize into master library"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def organize(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        """Organize content into master library"""
        print("\n" + "═" * 70)
        print(f"   📦 ORGANIZER - {'DRY RUN' if dry_run else 'REORGANIZING'}")
        print("═" * 70)
        
        results = {
            'moved': [],
            'renamed': [],
            'errors': [],
            'structure_created': []
        }
        
        master_lib = Path(self.config.MASTER_LIBRARY)
        
        # Create master library structure
        if not dry_run:
            master_lib.mkdir(parents=True, exist_ok=True)
            
        # Organize folders
        for folder in scan_result.folders:
            if self.config.MASTER_LIBRARY in folder.path:
                continue  # Skip if already in master library
                
            new_name = self._normalize_name(folder.name)
            category = folder.category
            dest_path = master_lib / category / new_name
            
            if dry_run:
                print(f"   Would move: {folder.name} → {dest_path}")
                results['moved'].append({
                    'source': folder.path,
                    'destination': str(dest_path),
                    'dry_run': True
                })
            else:
                try:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    if not dest_path.exists():
                        shutil.copytree(folder.path, dest_path)
                        print(f"   Moved: {folder.name} → {dest_path}")
                        results['moved'].append({
                            'source': folder.path,
                            'destination': str(dest_path),
                            'success': True
                        })
                except Exception as e:
                    results['errors'].append({
                        'source': folder.path,
                        'error': str(e)
                    })
        
        return results
    
    def _normalize_name(self, name: str) -> str:
        """Normalize folder/file names for consistency"""
        # Remove common prefixes
        name = re.sub(r'^(EZX[23]?_|SDX_|EZXP_)', '', name)
        
        # Convert to title case with underscores
        name = re.sub(r'[\s\-]+', '_', name)
        name = re.sub(r'[^\w\-_]', '', name)
        
        # Capitalize words
        parts = name.split('_')
        name = '_'.join(p.capitalize() for p in parts if p)
        
        return name


# ═══════════════════════════════════════════════════════════════════════════════
# REPORT GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

class ReportGenerator:
    """Generate comprehensive reports"""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def generate(self, 
                 scan_result: ScanResult,
                 test_results: List = None,
                 deep_analysis: Dict = None) -> str:
        """Generate and save a comprehensive report"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = Path(self.config.REPORT_DIR)
        report_dir.mkdir(parents=True, exist_ok=True)
        
        report_path = report_dir / f"toontrack_report_{timestamp}.md"
        
        report = self._build_report(scan_result, test_results, deep_analysis)
        
        with open(report_path, 'w') as f:
            f.write(report)
            
        # Also save JSON data
        json_path = report_dir / f"toontrack_data_{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump({
                'scan_result': {
                    'timestamp': scan_result.timestamp,
                    'total_items': scan_result.total_items,
                    'total_size_gb': scan_result.total_size_gb,
                    'files_count': len(scan_result.files),
                    'folders_count': len(scan_result.folders),
                    'issues_count': len(scan_result.issues),
                },
                'deep_analysis': deep_analysis,
            }, f, indent=2)
        
        print(f"\n   📄 Report saved: {report_path}")
        print(f"   📄 Data saved: {json_path}")
        
        return str(report_path)
    
    def _build_report(self, scan_result, test_results, deep_analysis) -> str:
        """Build markdown report"""
        lines = [
            "# 🥁 TOONTRACK EZDRUMMER LIBRARY REPORT",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            "",
            "## 📊 Summary",
            "",
            f"- **Total Items:** {scan_result.total_items:,}",
            f"- **Total Size:** {scan_result.total_size_gb:.2f} GB",
            f"- **Files:** {len(scan_result.files):,}",
            f"- **Folders:** {len(scan_result.folders):,}",
            f"- **Issues Found:** {len(scan_result.issues)}",
            "",
        ]
        
        if deep_analysis:
            lines.extend([
                "## 📁 Content by Category",
                "",
                "| Category | Files | Size (GB) |",
                "|----------|-------|-----------|",
            ])
            
            for cat, data in sorted(
                deep_analysis.get('by_category', {}).items(),
                key=lambda x: x[1]['size'],
                reverse=True
            ):
                size_gb = data['size'] / (1024**3)
                lines.append(f"| {cat} | {data['count']} | {size_gb:.2f} |")
            
            lines.extend(["", "## 💡 Recommendations", ""])
            for rec in deep_analysis.get('recommendations', []):
                lines.append(f"- {rec}")
        
        if scan_result.issues:
            lines.extend(["", "## ⚠️ Issues", ""])
            for issue in scan_result.issues[:20]:  # Limit to 20
                lines.append(f"- **{issue.get('type', 'unknown')}**: {issue.get('path', 'N/A')}")
        
        lines.extend([
            "",
            "---",
            "",
            "*Generated by TOONTRACK MASTER LIBRARY MANAGEMENT SYSTEM*",
        ])
        
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CLI
# ═══════════════════════════════════════════════════════════════════════════════

def print_banner():
    """Print application banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ████████╗ ██████╗  ██████╗ ███╗   ██╗████████╗██████╗  █████╗  ██████╗██╗  ║
║   ╚══██╔══╝██╔═══██╗██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║  ║
║      ██║   ██║   ██║██║   ██║██╔██╗ ██║   ██║   ██████╔╝███████║██║     ██║  ║
║      ██║   ██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║██║     ██║  ║
║      ██║   ╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██║  ██║██║  ██║╚██████╗██║  ║
║      ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ║
║                                                                              ║
║          🥁 EZDRUMMER MASTER LIBRARY MANAGEMENT SYSTEM 🥁                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Main entry point"""
    import argparse
    
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="Toontrack EZDrummer Master Library Management"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Scan for Toontrack content')
    scan_parser.add_argument('--quick', action='store_true', help='Quick scan (skip hashing)')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Test file integrity')
    
    # Heal command
    heal_parser = subparsers.add_parser('heal', help='Heal issues')
    heal_parser.add_argument('--apply', action='store_true', help='Apply fixes (default: dry run)')
    
    # Optimize command
    opt_parser = subparsers.add_parser('optimize', help='Optimize library')
    opt_parser.add_argument('--apply', action='store_true', help='Apply optimizations')
    
    # Deep scan command
    deep_parser = subparsers.add_parser('deep', help='Deep scan with analysis')
    
    # Organize command
    org_parser = subparsers.add_parser('organize', help='Reorganize into master library')
    org_parser.add_argument('--apply', action='store_true', help='Apply reorganization')
    
    # Full command (run everything)
    full_parser = subparsers.add_parser('full', help='Run full pipeline')
    full_parser.add_argument('--apply', action='store_true', help='Apply all changes')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate report only')
    
    args = parser.parse_args()
    
    config = Config()
    
    if args.command == 'scan' or not args.command:
        scanner = ToontrackScanner(config)
        result = scanner.scan(quick=getattr(args, 'quick', False))
        print(f"\n✓ Scan complete: {result.total_items} items, {result.total_size_gb:.2f} GB")
        
    elif args.command == 'test':
        scanner = ToontrackScanner(config)
        result = scanner.scan(quick=True)
        tester = IntegrityTester(config)
        issues = tester.test(result)
        
    elif args.command == 'heal':
        scanner = ToontrackScanner(config)
        result = scanner.scan(quick=True)
        healer = ToontrackHealer(config)
        healer.heal(result, dry_run=not getattr(args, 'apply', False))
        
    elif args.command == 'optimize':
        scanner = ToontrackScanner(config)
        result = scanner.scan()
        optimizer = ToontrackOptimizer(config)
        optimizer.optimize(result, dry_run=not getattr(args, 'apply', False))
        
    elif args.command == 'deep':
        scanner = ToontrackScanner(config)
        result = scanner.scan()
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        
        # Generate report
        reporter = ReportGenerator(config)
        reporter.generate(result, deep_analysis=analysis)
        
    elif args.command == 'organize':
        scanner = ToontrackScanner(config)
        result = scanner.scan(quick=True)
        organizer = ToontrackOrganizer(config)
        organizer.organize(result, dry_run=not getattr(args, 'apply', False))
        
    elif args.command == 'full':
        apply = getattr(args, 'apply', False)
        
        # 1. Scan
        scanner = ToontrackScanner(config)
        result = scanner.scan()
        
        # 2. Test
        tester = IntegrityTester(config)
        test_results = tester.test(result)
        
        # 3. Deep scan
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        
        # 4. Heal
        healer = ToontrackHealer(config)
        healer.heal(result, dry_run=not apply)
        
        # 5. Optimize
        optimizer = ToontrackOptimizer(config)
        optimizer.optimize(result, dry_run=not apply)
        
        # 6. Organize
        organizer = ToontrackOrganizer(config)
        organizer.organize(result, dry_run=not apply)
        
        # 7. Generate report
        reporter = ReportGenerator(config)
        reporter.generate(result, test_results, analysis)
        
        print("\n" + "═" * 70)
        print("   ✅ FULL PIPELINE COMPLETE")
        print("═" * 70)
        
    elif args.command == 'report':
        scanner = ToontrackScanner(config)
        result = scanner.scan()
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        reporter = ReportGenerator(config)
        reporter.generate(result, deep_analysis=analysis)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
