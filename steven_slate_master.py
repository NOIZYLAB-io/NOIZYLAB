#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║            STEVEN SLATE DRUMS MASTER LIBRARY MANAGEMENT SYSTEM               ║
║                  SSD4 • SSD5 • TRIGGER 2 • SLATE DRUMS                       ║
║                TEST • SCAN • HEAL • OPTIMIZE • ORGANIZE                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

Author: NOIZYLAB
Version: 1.0.0
"""

import os
import sys
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Set
from collections import defaultdict
import re


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Config:
    """Master configuration for Steven Slate library management"""
    
    SCAN_VOLUMES: List[str] = field(default_factory=lambda: [
        "/Volumes/6TB",
        "/Volumes/4TBSG",
        "/Volumes/SAMPLE_MASTER",
        "/Volumes/4TB Lacie",
        "/Volumes/4TB_Utility",
        "/Volumes/4TB Big Fish",
        "/Volumes/SOUND_DESIGN",
        "/Volumes/EW",
        "/Volumes/12TB",
        "/Volumes/FISH",
    ])
    
    MASTER_LIBRARY: str = "/Volumes/SAMPLE_MASTER/06_Drums_Percussion/Steven_Slate_Master"
    
    SLATE_EXTENSIONS: Set[str] = field(default_factory=lambda: {
        '.ssd', '.ssi', '.ssd5kit', '.ssd4kit',  # SSD sound/instrument files
        '.kit', '.preset',  # Kit presets
        '.wav', '.aif', '.aiff',  # Audio samples
        '.midi', '.mid',  # MIDI files
        '.xml', '.dat', '.db',  # Databases
        '.trig', '.trigger',  # Trigger files
    })
    
    FOLDER_PATTERNS: List[str] = field(default_factory=lambda: [
        'slate', 'ssd', 'steven_slate', 'trigger2', 'ssd4', 'ssd5'
    ])
    
    PRODUCTS: Dict[str, List[str]] = field(default_factory=lambda: {
        'SSD4': ['ssd4', 'ssd 4'],
        'SSD5': ['ssd5', 'ssd 5', 'ssd5library'],
        'Trigger_2': ['trigger2', 'trigger 2', 'trigger2library'],
        'Slate_Drums': ['slate_drums', 'slatedrums'],
    })
    
    CATEGORY_MAP: Dict[str, str] = field(default_factory=lambda: {
        'ssd4': 'SSD4',
        'ssd5': 'SSD5',
        'trigger': 'Trigger_2',
        'kit': 'Kits',
        'midi': 'MIDI_Grooves',
        'preset': 'Presets',
    })
    
    REPORT_DIR: str = "/Users/m2ultra/NOIZYLAB/CODE_MASTER/Steven_Slate/reports"
    CACHE_FILE: str = "/Users/m2ultra/NOIZYLAB/CODE_MASTER/Steven_Slate/.scan_cache.json"


@dataclass
class SlateItem:
    path: str
    name: str
    item_type: str
    product: str = "unknown"
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
    timestamp: str
    total_items: int = 0
    total_size_gb: float = 0.0
    files: List[SlateItem] = field(default_factory=list)
    folders: List[SlateItem] = field(default_factory=list)
    duplicates: Dict[str, List[str]] = field(default_factory=dict)
    issues: List[Dict] = field(default_factory=list)
    volumes_scanned: List[str] = field(default_factory=list)
    products_found: Dict[str, int] = field(default_factory=dict)


class SlateScanner:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.results = ScanResult(timestamp=datetime.now().isoformat())
        self._hash_cache = {}
        
    def scan(self, quick: bool = False) -> ScanResult:
        print("\n" + "═" * 70)
        print("   🔍 STEVEN SLATE SCANNER - Starting Multi-Volume Scan")
        print("═" * 70)
        
        for volume in self.config.SCAN_VOLUMES:
            if os.path.exists(volume):
                print(f"\n📂 Scanning: {volume}")
                self._scan_volume(volume, quick)
            else:
                print(f"⚠️  Volume not mounted: {volume}")
        
        self.results.total_items = len(self.results.files) + len(self.results.folders)
        self.results.total_size_gb = sum(f.size for f in self.results.files) / (1024**3)
        
        for item in self.results.files:
            if item.product not in self.results.products_found:
                self.results.products_found[item.product] = 0
            self.results.products_found[item.product] += 1
        
        return self.results
    
    def _scan_volume(self, volume: str, quick: bool = False):
        slate_paths = self._find_slate_paths(volume)
        for path in slate_paths:
            self._process_path(path, quick)
            
    def _find_slate_paths(self, volume: str) -> List[str]:
        paths = []
        search_dirs = [
            os.path.join(volume, "_ORGANIZED"),
            os.path.join(volume, "Sample_Libraries"),
            os.path.join(volume, "_MASTER_ARCHIVE"),
            os.path.join(volume, "Applications"),
            os.path.join(volume, "Library", "Application Support"),
            os.path.join(volume, "Steven_Slate"),
            os.path.join(volume, "Steven_Slate_Drums"),
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
                    if '01_drums' in name_lower or '03_drum' in name_lower:
                        if os.path.isdir(entry.path):
                            for sub in os.scandir(entry.path):
                                if 'slate' in sub.name.lower() or 'ssd' in sub.name.lower():
                                    paths.append(sub.path)
                                    self.results.volumes_scanned.append(sub.path)
            except PermissionError:
                continue
        return paths
    
    def _process_path(self, path: str, quick: bool = False):
        if os.path.isfile(path):
            self._process_file(path, quick)
        elif os.path.isdir(path):
            self._process_folder(path, quick)
            
    def _process_folder(self, folder_path: str, quick: bool = False):
        try:
            folder_size = 0
            file_count = 0
            
            for root, dirs, files in os.walk(folder_path):
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                for file in files:
                    if file.startswith('.'):
                        continue
                    file_path = os.path.join(root, file)
                    item = self._process_file(file_path, quick)
                    if item:
                        folder_size += item.size
                        file_count += 1
            
            folder_item = SlateItem(
                path=folder_path,
                name=os.path.basename(folder_path),
                item_type='folder',
                product=self._identify_product(folder_path),
                size=folder_size,
                category=self._categorize(folder_path),
                last_modified=datetime.fromtimestamp(os.path.getmtime(folder_path)).isoformat()
            )
            self.results.folders.append(folder_item)
            print(f"   ✓ {folder_item.name}: {file_count} files, {folder_size / (1024**3):.2f} GB")
            
        except Exception as e:
            self.results.issues.append({'path': folder_path, 'error': str(e), 'type': 'scan_error'})
    
    def _process_file(self, file_path: str, quick: bool = False) -> Optional[SlateItem]:
        try:
            stat = os.stat(file_path)
            ext = os.path.splitext(file_path)[1].lower()
            
            item = SlateItem(
                path=file_path,
                name=os.path.basename(file_path),
                item_type='file',
                product=self._identify_product(file_path),
                size=stat.st_size,
                extension=ext,
                category=self._categorize(file_path),
                last_modified=datetime.fromtimestamp(stat.st_mtime).isoformat()
            )
            
            if not quick and stat.st_size < 100 * 1024 * 1024:
                item.hash_md5 = self._calculate_hash(file_path)
                if item.hash_md5:
                    if item.hash_md5 not in self.results.duplicates:
                        self.results.duplicates[item.hash_md5] = []
                    self.results.duplicates[item.hash_md5].append(file_path)
            
            self.results.files.append(item)
            return item
        except Exception as e:
            self.results.issues.append({'path': file_path, 'error': str(e), 'type': 'file_error'})
            return None
    
    def _identify_product(self, path: str) -> str:
        path_lower = path.lower()
        for product, patterns in self.config.PRODUCTS.items():
            if any(pattern in path_lower for pattern in patterns):
                return product
        return "Steven_Slate_General"
    
    def _categorize(self, path: str) -> str:
        path_lower = path.lower()
        for pattern, category in self.config.CATEGORY_MAP.items():
            if pattern in path_lower:
                return category
        ext = os.path.splitext(path)[1].lower()
        if ext in {'.ssd', '.ssi', '.ssd5kit', '.ssd4kit'}:
            return "Sound_Libraries"
        elif ext in {'.mid', '.midi'}:
            return "MIDI_Grooves"
        elif ext in {'.kit', '.preset'}:
            return "Kits"
        return "uncategorized"
    
    def _calculate_hash(self, file_path: str, chunk_size: int = 8192) -> str:
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


class IntegrityTester:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.test_results = []
        
    def test(self, scan_result: ScanResult) -> List[Dict]:
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
    
    def _test_item(self, item: SlateItem) -> List[Dict]:
        issues = []
        if not os.path.exists(item.path):
            issues.append({'path': item.path, 'type': 'missing', 'message': 'File does not exist'})
            return issues
        if not os.access(item.path, os.R_OK):
            issues.append({'path': item.path, 'type': 'permission', 'message': 'File is not readable'})
        if item.size == 0 and item.extension in {'.ssd', '.ssi', '.wav', '.mid'}:
            issues.append({'path': item.path, 'type': 'empty', 'message': 'File is empty'})
        if os.path.islink(item.path) and not os.path.exists(os.path.realpath(item.path)):
            issues.append({'path': item.path, 'type': 'broken_link', 'message': 'Broken symbolic link'})
        return issues


class SlateHealer:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.healed = []
        self.failed = []
        
    def heal(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        print("\n" + "═" * 70)
        print(f"   🔧 HEALER - {'DRY RUN' if dry_run else 'APPLYING FIXES'}")
        print("═" * 70)
        
        self._heal_permissions(scan_result, dry_run)
        self._heal_broken_links(scan_result, dry_run)
        self._heal_structure(scan_result, dry_run)
        
        return {'healed': self.healed, 'failed': self.failed, 'dry_run': dry_run}
    
    def _heal_permissions(self, scan_result: ScanResult, dry_run: bool):
        print("\n   📝 Fixing Permissions...")
        for item in scan_result.files + scan_result.folders:
            if any(i['type'] == 'permission' for i in item.issues):
                if dry_run:
                    print(f"      Would fix: {item.path}")
                    self.healed.append({'path': item.path, 'action': 'chmod', 'dry_run': True})
                else:
                    try:
                        os.chmod(item.path, 0o644 if item.item_type == 'file' else 0o755)
                        self.healed.append({'path': item.path, 'action': 'chmod', 'success': True})
                    except Exception as e:
                        self.failed.append({'path': item.path, 'error': str(e)})
    
    def _heal_broken_links(self, scan_result: ScanResult, dry_run: bool):
        print("\n   🔗 Fixing Broken Links...")
        for item in scan_result.files:
            if any(i['type'] == 'broken_link' for i in item.issues):
                if dry_run:
                    print(f"      Would remove: {item.path}")
                else:
                    try:
                        os.unlink(item.path)
                        self.healed.append({'path': item.path, 'action': 'unlink', 'success': True})
                    except Exception as e:
                        self.failed.append({'path': item.path, 'error': str(e)})
    
    def _heal_structure(self, scan_result: ScanResult, dry_run: bool):
        print("\n   📁 Verifying Structure...")
        master_lib = Path(self.config.MASTER_LIBRARY)
        required_dirs = [
            master_lib / "SSD4", master_lib / "SSD5",
            master_lib / "Trigger_2", master_lib / "Kits",
            master_lib / "MIDI_Grooves", master_lib / "Presets",
        ]
        for dir_path in required_dirs:
            if not dir_path.exists():
                if dry_run:
                    print(f"      Would create: {dir_path}")
                else:
                    dir_path.mkdir(parents=True, exist_ok=True)
                    print(f"      Created: {dir_path}")


class SlateOptimizer:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def optimize(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        print("\n" + "═" * 70)
        print(f"   ⚡ OPTIMIZER - {'DRY RUN' if dry_run else 'APPLYING OPTIMIZATION'}")
        print("═" * 70)
        
        results = {'duplicates_removed': [], 'space_saved_gb': 0}
        duplicates = {h: p for h, p in scan_result.duplicates.items() if len(p) > 1 and h}
        
        print(f"\n   Found {len(duplicates)} duplicate groups")
        
        for hash_val, paths in duplicates.items():
            if len(paths) > 1:
                master_paths = [p for p in paths if self.config.MASTER_LIBRARY in p]
                keep = master_paths[0] if master_paths else paths[0]
                for path in paths:
                    if path != keep:
                        try:
                            size = os.path.getsize(path)
                            if dry_run:
                                print(f"      Would remove: {path}")
                            else:
                                os.remove(path)
                            results['duplicates_removed'].append(path)
                            results['space_saved_gb'] += size / (1024**3)
                        except Exception as e:
                            print(f"      Error: {e}")
        
        print(f"\n   💾 Potential space savings: {results['space_saved_gb']:.2f} GB")
        return results


class DeepScanner:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def deep_scan(self, scan_result: ScanResult) -> Dict:
        print("\n" + "═" * 70)
        print("   🔬 DEEP SCANNER - Comprehensive Analysis")
        print("═" * 70)
        
        analysis = {
            'summary': self._generate_summary(scan_result),
            'by_product': self._analyze_by_product(scan_result),
            'by_category': self._analyze_by_category(scan_result),
            'by_extension': self._analyze_by_extension(scan_result),
            'largest_files': self._find_largest(scan_result),
            'recommendations': self._generate_recommendations(scan_result),
        }
        self._print_analysis(analysis)
        return analysis
    
    def _generate_summary(self, result: ScanResult) -> Dict:
        return {
            'total_files': len(result.files),
            'total_folders': len(result.folders),
            'total_size_gb': result.total_size_gb,
            'unique_extensions': len(set(f.extension for f in result.files)),
            'issues_count': len(result.issues),
            'duplicate_groups': len([d for d in result.duplicates.values() if len(d) > 1]),
        }
    
    def _analyze_by_product(self, result: ScanResult) -> Dict:
        products = defaultdict(lambda: {'count': 0, 'size': 0})
        for item in result.files:
            products[item.product]['count'] += 1
            products[item.product]['size'] += item.size
        return dict(products)
    
    def _analyze_by_category(self, result: ScanResult) -> Dict:
        categories = defaultdict(lambda: {'count': 0, 'size': 0})
        for item in result.files:
            categories[item.category]['count'] += 1
            categories[item.category]['size'] += item.size
        return dict(categories)
    
    def _analyze_by_extension(self, result: ScanResult) -> Dict:
        extensions = defaultdict(lambda: {'count': 0, 'size': 0})
        for item in result.files:
            ext = item.extension or 'no_extension'
            extensions[ext]['count'] += 1
            extensions[ext]['size'] += item.size
        return dict(extensions)
    
    def _find_largest(self, result: ScanResult, limit: int = 10) -> List[Dict]:
        sorted_files = sorted(result.files, key=lambda x: x.size, reverse=True)
        return [{'path': f.path, 'size_gb': f.size / (1024**3), 'product': f.product} for f in sorted_files[:limit]]
    
    def _generate_recommendations(self, result: ScanResult) -> List[str]:
        recs = []
        dup_count = len([d for d in result.duplicates.values() if len(d) > 1])
        if dup_count > 0:
            recs.append(f"Remove {dup_count} duplicate file groups to save space")
        if result.issues:
            recs.append(f"Fix {len(result.issues)} identified issues using heal command")
        volumes = set(f.path.split('/')[2] for f in result.files if len(f.path.split('/')) > 2)
        if len(volumes) > 2:
            recs.append("Consider consolidating Steven Slate content to fewer drives")
        return recs
    
    def _print_analysis(self, analysis: Dict):
        print("\n   📊 SUMMARY")
        print("   " + "-" * 40)
        summary = analysis['summary']
        print(f"   Total Files: {summary['total_files']:,}")
        print(f"   Total Folders: {summary['total_folders']:,}")
        print(f"   Total Size: {summary['total_size_gb']:.2f} GB")
        print(f"   Issues Found: {summary['issues_count']}")
        print(f"   Duplicate Groups: {summary['duplicate_groups']}")
        
        print("\n   🥁 BY PRODUCT")
        print("   " + "-" * 40)
        for prod, data in sorted(analysis['by_product'].items(), key=lambda x: x[1]['size'], reverse=True):
            size_gb = data['size'] / (1024**3)
            print(f"   {prod}: {data['count']} files, {size_gb:.2f} GB")
        
        print("\n   💡 RECOMMENDATIONS")
        print("   " + "-" * 40)
        for i, rec in enumerate(analysis['recommendations'], 1):
            print(f"   {i}. {rec}")


class SlateOrganizer:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def organize(self, scan_result: ScanResult, dry_run: bool = True) -> Dict:
        print("\n" + "═" * 70)
        print(f"   📦 ORGANIZER - {'DRY RUN' if dry_run else 'REORGANIZING'}")
        print("═" * 70)
        
        results = {'moved': [], 'errors': []}
        master_lib = Path(self.config.MASTER_LIBRARY)
        
        if not dry_run:
            master_lib.mkdir(parents=True, exist_ok=True)
            
        for folder in scan_result.folders:
            if self.config.MASTER_LIBRARY in folder.path:
                continue
            new_name = self._normalize_name(folder.name)
            product = folder.product
            dest_path = master_lib / product / new_name
            
            if dry_run:
                print(f"   Would move: {folder.name} → {dest_path}")
                results['moved'].append({'source': folder.path, 'destination': str(dest_path), 'dry_run': True})
            else:
                try:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    if not dest_path.exists():
                        shutil.copytree(folder.path, dest_path)
                        results['moved'].append({'source': folder.path, 'destination': str(dest_path), 'success': True})
                except Exception as e:
                    results['errors'].append({'source': folder.path, 'error': str(e)})
        return results
    
    def _normalize_name(self, name: str) -> str:
        name = re.sub(r'^(SSD[45]_|Trigger[2]?_)', '', name)
        name = re.sub(r'[\s\-]+', '_', name)
        name = re.sub(r'[^\w\-_]', '', name)
        parts = name.split('_')
        return '_'.join(p.capitalize() for p in parts if p)


class ReportGenerator:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def generate(self, scan_result: ScanResult, test_results: List = None, deep_analysis: Dict = None) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = Path(self.config.REPORT_DIR)
        report_dir.mkdir(parents=True, exist_ok=True)
        
        report_path = report_dir / f"steven_slate_report_{timestamp}.md"
        report = self._build_report(scan_result, test_results, deep_analysis)
        
        with open(report_path, 'w') as f:
            f.write(report)
            
        json_path = report_dir / f"steven_slate_data_{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump({
                'scan_result': {
                    'timestamp': scan_result.timestamp,
                    'total_items': scan_result.total_items,
                    'total_size_gb': scan_result.total_size_gb,
                    'products_found': scan_result.products_found,
                },
                'deep_analysis': deep_analysis,
            }, f, indent=2)
        
        print(f"\n   📄 Report saved: {report_path}")
        print(f"   📄 Data saved: {json_path}")
        return str(report_path)
    
    def _build_report(self, scan_result, test_results, deep_analysis) -> str:
        lines = [
            "# 🥁 STEVEN SLATE DRUMS LIBRARY REPORT",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "", "---", "",
            "## 📊 Summary", "",
            f"- **Total Items:** {scan_result.total_items:,}",
            f"- **Total Size:** {scan_result.total_size_gb:.2f} GB",
            f"- **Files:** {len(scan_result.files):,}",
            f"- **Folders:** {len(scan_result.folders):,}",
            f"- **Issues Found:** {len(scan_result.issues)}",
            "", "## 🥁 Products Found", "",
        ]
        for product, count in scan_result.products_found.items():
            lines.append(f"- **{product}:** {count} files")
        
        if deep_analysis:
            lines.extend(["", "## 💡 Recommendations", ""])
            for rec in deep_analysis.get('recommendations', []):
                lines.append(f"- {rec}")
        
        lines.extend(["", "---", "", "*Generated by STEVEN SLATE MASTER LIBRARY MANAGEMENT SYSTEM*"])
        return "\n".join(lines)


def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███████╗████████╗███████╗██╗   ██╗███████╗███╗   ██╗                       ║
║   ██╔════╝╚══██╔══╝██╔════╝██║   ██║██╔════╝████╗  ██║                       ║
║   ███████╗   ██║   █████╗  ██║   ██║█████╗  ██╔██╗ ██║                       ║
║   ╚════██║   ██║   ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║                       ║
║   ███████║   ██║   ███████╗ ╚████╔╝ ███████╗██║ ╚████║                       ║
║   ╚══════╝   ╚═╝   ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝                       ║
║                                                                              ║
║   ███████╗██╗      █████╗ ████████╗███████╗    ██████╗ ██████╗ ██╗   ██╗     ║
║   ██╔════╝██║     ██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║   ██║     ║
║   ███████╗██║     ███████║   ██║   █████╗      ██║  ██║██████╔╝██║   ██║     ║
║   ╚════██║██║     ██╔══██║   ██║   ██╔══╝      ██║  ██║██╔══██╗██║   ██║     ║
║   ███████║███████╗██║  ██║   ██║   ███████╗    ██████╔╝██║  ██║╚██████╔╝     ║
║   ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝      ║
║                                                                              ║
║            🥁 SSD4 • SSD5 • TRIGGER 2 • SLATE DRUMS 🥁                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    import argparse
    print_banner()
    
    parser = argparse.ArgumentParser(description="Steven Slate Drums Master Library Management")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    scan_parser = subparsers.add_parser('scan', help='Scan for Steven Slate content')
    scan_parser.add_argument('--quick', action='store_true', help='Quick scan')
    
    subparsers.add_parser('test', help='Test file integrity')
    
    heal_parser = subparsers.add_parser('heal', help='Heal issues')
    heal_parser.add_argument('--apply', action='store_true', help='Apply fixes')
    
    opt_parser = subparsers.add_parser('optimize', help='Optimize library')
    opt_parser.add_argument('--apply', action='store_true', help='Apply optimizations')
    
    subparsers.add_parser('deep', help='Deep scan with analysis')
    
    org_parser = subparsers.add_parser('organize', help='Reorganize into master library')
    org_parser.add_argument('--apply', action='store_true', help='Apply reorganization')
    
    full_parser = subparsers.add_parser('full', help='Run full pipeline')
    full_parser.add_argument('--apply', action='store_true', help='Apply all changes')
    
    subparsers.add_parser('report', help='Generate report only')
    
    args = parser.parse_args()
    config = Config()
    
    if args.command == 'scan' or not args.command:
        scanner = SlateScanner(config)
        result = scanner.scan(quick=getattr(args, 'quick', False))
        print(f"\n✓ Scan complete: {result.total_items} items, {result.total_size_gb:.2f} GB")
    elif args.command == 'test':
        scanner = SlateScanner(config)
        result = scanner.scan(quick=True)
        tester = IntegrityTester(config)
        tester.test(result)
    elif args.command == 'heal':
        scanner = SlateScanner(config)
        result = scanner.scan(quick=True)
        healer = SlateHealer(config)
        healer.heal(result, dry_run=not getattr(args, 'apply', False))
    elif args.command == 'optimize':
        scanner = SlateScanner(config)
        result = scanner.scan()
        optimizer = SlateOptimizer(config)
        optimizer.optimize(result, dry_run=not getattr(args, 'apply', False))
    elif args.command == 'deep':
        scanner = SlateScanner(config)
        result = scanner.scan()
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        reporter = ReportGenerator(config)
        reporter.generate(result, deep_analysis=analysis)
    elif args.command == 'organize':
        scanner = SlateScanner(config)
        result = scanner.scan(quick=True)
        organizer = SlateOrganizer(config)
        organizer.organize(result, dry_run=not getattr(args, 'apply', False))
    elif args.command == 'full':
        apply = getattr(args, 'apply', False)
        scanner = SlateScanner(config)
        result = scanner.scan()
        tester = IntegrityTester(config)
        test_results = tester.test(result)
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        healer = SlateHealer(config)
        healer.heal(result, dry_run=not apply)
        optimizer = SlateOptimizer(config)
        optimizer.optimize(result, dry_run=not apply)
        organizer = SlateOrganizer(config)
        organizer.organize(result, dry_run=not apply)
        reporter = ReportGenerator(config)
        reporter.generate(result, test_results, analysis)
        print("\n" + "═" * 70)
        print("   ✅ FULL PIPELINE COMPLETE")
        print("═" * 70)
    elif args.command == 'report':
        scanner = SlateScanner(config)
        result = scanner.scan()
        deep = DeepScanner(config)
        analysis = deep.deep_scan(result)
        reporter = ReportGenerator(config)
        reporter.generate(result, deep_analysis=analysis)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()



