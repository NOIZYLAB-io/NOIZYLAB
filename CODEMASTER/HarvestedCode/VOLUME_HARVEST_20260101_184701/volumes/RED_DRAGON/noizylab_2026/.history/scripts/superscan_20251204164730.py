#!/usr/bin/env python3
"""
NoizyLab SuperScan - Multi-Drive Audio Library Scanner
Comprehensive scan of all connected audio drives.
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional
from collections import defaultdict


@dataclass
class DriveInfo:
    name: str
    path: str
    total_gb: float = 0
    used_gb: float = 0
    free_gb: float = 0
    percent_used: int = 0
    status: str = "unknown"


@dataclass
class LibraryInfo:
    name: str
    path: str
    file_count: int = 0
    size_gb: float = 0
    category: str = ""
    vendor: str = ""


@dataclass
class ScanReport:
    timestamp: str
    drives: List[DriveInfo] = field(default_factory=list)
    libraries: List[LibraryInfo] = field(default_factory=list)
    total_files: int = 0
    total_size_gb: float = 0
    warnings: List[str] = field(default_factory=list)


# Drive configurations
DRIVES = {
    "MAG 4TB": {
        "path": "/Volumes/MAG 4TB",
        "organized": "/Volumes/MAG 4TB/_ORGANIZED",
        "categories": {
            "01_Drums": ["FXpansion", "Toontrack_EZDrummer"],
            "02_EastWest": ["EW"],
        }
    },
    "4TBSG": {
        "path": "/Volumes/4TBSG",
        "organized": "/Volumes/4TBSG/_ORGANIZED",
        "categories": {
            "01_Toontrack": ["Superior Drummer", "Toontrack"],
            "02_Factory_Libraries": ["FACTORY_FRESH_ORGANIZED"],
        }
    },
    "RED DRAGON": {
        "path": "/Volumes/RED DRAGON",
        "organized": "/Volumes/RED DRAGON/_ORGANIZED",
        "categories": {}
    }
}

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', 
                    '.m4a', '.ewi', '.opus', '.nki', '.nkm', '.ncw'}


def get_drive_info(drive_name: str, drive_path: str) -> Optional[DriveInfo]:
    """Get drive statistics using df command."""
    try:
        result = subprocess.run(
            ['df', '-h', drive_path],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 2:
                parts = lines[1].split()
                if len(parts) >= 5:
                    # Parse sizes (remove 'G', 'T' suffixes)
                    def parse_size(s):
                        s = s.strip()
                        if s.endswith('Ti') or s.endswith('T'):
                            return float(s[:-2] if s.endswith('Ti') else s[:-1]) * 1024
                        elif s.endswith('Gi') or s.endswith('G'):
                            return float(s[:-2] if s.endswith('Gi') else s[:-1])
                        elif s.endswith('Mi') or s.endswith('M'):
                            return float(s[:-2] if s.endswith('Mi') else s[:-1]) / 1024
                        return float(s)
                    
                    total = parse_size(parts[1])
                    used = parse_size(parts[2])
                    free = parse_size(parts[3])
                    percent = int(parts[4].rstrip('%'))
                    
                    status = "OK"
                    if percent >= 95:
                        status = "CRITICAL"
                    elif percent >= 90:
                        status = "WARNING"
                    elif percent >= 80:
                        status = "WATCH"
                    
                    return DriveInfo(
                        name=drive_name,
                        path=drive_path,
                        total_gb=round(total, 1),
                        used_gb=round(used, 1),
                        free_gb=round(free, 1),
                        percent_used=percent,
                        status=status
                    )
    except Exception as e:
        print(f"  ⚠️  Error reading drive {drive_name}: {e}")
    return None


def count_files(path: str) -> int:
    """Count files in a directory."""
    count = 0
    try:
        for _ in Path(path).rglob('*'):
            if _.is_file():
                count += 1
    except (PermissionError, OSError):
        pass
    return count


def get_dir_size(path: str) -> float:
    """Get directory size in GB using du command."""
    try:
        result = subprocess.run(
            ['du', '-sk', path],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            kb = int(result.stdout.split()[0])
            return round(kb / (1024 * 1024), 2)
    except Exception:
        pass
    return 0


def scan_library(lib_path: str, category: str, vendor: str) -> LibraryInfo:
    """Scan a single library directory."""
    path = Path(lib_path)
    if not path.exists():
        return LibraryInfo(name=path.name, path=str(path), category=category, vendor=vendor)
    
    file_count = count_files(str(path))
    size_gb = get_dir_size(str(path))
    
    return LibraryInfo(
        name=path.name,
        path=str(path),
        file_count=file_count,
        size_gb=size_gb,
        category=category,
        vendor=vendor
    )


def superscan(drives_to_scan: List[str] = None, quick: bool = False) -> ScanReport:
    """Perform a comprehensive scan of all drives."""
    
    report = ScanReport(timestamp=datetime.now().isoformat())
    
    if drives_to_scan is None:
        drives_to_scan = list(DRIVES.keys())
    
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           🚀 NOIZYLAB SUPERSCAN                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    
    # Scan each drive
    for drive_name in drives_to_scan:
        if drive_name not in DRIVES:
            continue
            
        config = DRIVES[drive_name]
        drive_path = config["path"]
        
        print(f"📀 Scanning: {drive_name}")
        
        # Check if drive is mounted
        if not Path(drive_path).exists():
            print(f"   ⚠️  Drive not mounted: {drive_path}")
            report.warnings.append(f"Drive not mounted: {drive_name}")
            continue
        
        # Get drive info
        drive_info = get_drive_info(drive_name, drive_path)
        if drive_info:
            report.drives.append(drive_info)
            status_icon = "✅" if drive_info.status == "OK" else "⚠️" if drive_info.status in ["WATCH", "WARNING"] else "🔴"
            print(f"   {status_icon} {drive_info.used_gb}GB / {drive_info.total_gb}GB ({drive_info.percent_used}% used)")
            
            if drive_info.percent_used >= 90:
                report.warnings.append(f"{drive_name}: {drive_info.percent_used}% full - consider cleanup")
        
        # Scan organized folder
        organized_path = config.get("organized", "")
        if organized_path and Path(organized_path).exists():
            for category, vendors in config.get("categories", {}).items():
                category_path = Path(organized_path) / category
                if category_path.exists():
                    print(f"   📁 {category}")
                    for vendor in vendors:
                        vendor_path = category_path / vendor
                        if vendor_path.exists():
                            if quick:
                                lib = LibraryInfo(
                                    name=vendor,
                                    path=str(vendor_path),
                                    category=category,
                                    vendor=vendor
                                )
                            else:
                                lib = scan_library(str(vendor_path), category, vendor)
                            report.libraries.append(lib)
                            report.total_files += lib.file_count
                            report.total_size_gb += lib.size_gb
                            print(f"      • {vendor}: {lib.file_count:,} files ({lib.size_gb}GB)")
        print()
    
    return report


def print_summary(report: ScanReport):
    """Print scan summary."""
    print("═══════════════════════════════════════════════════════════════")
    print("                      📊 SUMMARY")
    print("═══════════════════════════════════════════════════════════════")
    print()
    
    print("💾 DRIVES:")
    for drive in report.drives:
        status_icon = {"OK": "✅", "WATCH": "👀", "WARNING": "⚠️", "CRITICAL": "🔴"}.get(drive.status, "❓")
        print(f"   {status_icon} {drive.name}: {drive.free_gb}GB free ({drive.percent_used}% used)")
    
    print()
    print(f"📁 Total Libraries: {len(report.libraries)}")
    print(f"🎵 Total Files: {report.total_files:,}")
    print(f"💽 Total Size: {report.total_size_gb:.1f}GB ({report.total_size_gb/1024:.2f}TB)")
    
    if report.warnings:
        print()
        print("⚠️  WARNINGS:")
        for warning in report.warnings:
            print(f"   • {warning}")


def save_report(report: ScanReport, output_path: str):
    """Save report to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(asdict(report), f, indent=2)
    print(f"\n📄 Report saved: {output_path}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='NoizyLab SuperScan')
    parser.add_argument('--all', action='store_true', help='Scan all drives')
    parser.add_argument('--quick', action='store_true', help='Quick scan (skip file counting)')
    parser.add_argument('--drives', nargs='+', help='Specific drives to scan')
    parser.add_argument('--output', default='superscan_report.json', help='Output file')
    
    args = parser.parse_args()
    
    drives = args.drives if args.drives else (list(DRIVES.keys()) if args.all else None)
    
    if not drives:
        print("Usage: superscan.py --all  OR  superscan.py --drives 'MAG 4TB' 4TBSG")
        print("\nAvailable drives:")
        for name, config in DRIVES.items():
            mounted = "✅" if Path(config["path"]).exists() else "❌"
            print(f"  {mounted} {name}: {config['path']}")
        return
    
    report = superscan(drives, quick=args.quick)
    print_summary(report)
    save_report(report, args.output)


if __name__ == '__main__':
    main()
