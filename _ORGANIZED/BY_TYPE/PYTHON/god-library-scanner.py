#!/usr/bin/env python3
"""
GOD LIBRARY SCANNER - Scan & Regroup Sample Libraries by Metadata
CB_01 - Fish Music Inc
Scans NI, Spectrasonics, Kontakt libraries for metadata/tags
GORUNFREE! 🎸🔥
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Optional
import xml.etree.ElementTree as ET

# Colors
class C:
    R = '\033[0;31m'
    G = '\033[0;32m'
    Y = '\033[1;33m'
    B = '\033[0;34m'
    M = '\033[0;35m'
    C = '\033[0;36m'
    BOLD = '\033[1m'
    NC = '\033[0m'


class LibraryScanner:
    """Scan sample libraries for metadata and grouping"""

    # Known vendors/manufacturers
    VENDORS = {
        'native instruments': 'Native Instruments',
        'ni': 'Native Instruments',
        'kontakt': 'Native Instruments',
        'spectrasonics': 'Spectrasonics',
        'omnisphere': 'Spectrasonics',
        'keyscape': 'Spectrasonics',
        'trilian': 'Spectrasonics',
        'refx': 'reFX',
        'nexus': 'reFX',
        'eastwest': 'EastWest',
        'ew': 'EastWest',
        'spitfire': 'Spitfire Audio',
        'orchestral tools': 'Orchestral Tools',
        'ot': 'Orchestral Tools',
        'output': 'Output',
        'arturia': 'Arturia',
        'ik multimedia': 'IK Multimedia',
        'toontrack': 'Toontrack',
        'superior drummer': 'Toontrack',
        'ezdrummer': 'Toontrack',
        'ujam': 'UJAM',
        'heavyocity': 'Heavyocity',
        '8dio': '8Dio',
        'cinesamples': 'Cinesamples',
        'soundiron': 'Soundiron',
        'audioimperia': 'Audio Imperia',
        'audio imperia': 'Audio Imperia',
        'audiobro': 'Audiobro',
        'projectsam': 'ProjectSAM',
        'project sam': 'ProjectSAM',
        'vienna': 'Vienna Symphonic Library',
        'vsl': 'Vienna Symphonic Library',
        'labs': 'Spitfire LABS',
        'bfd': 'FXpansion',
        'fxpansion': 'FXpansion',
        'xln audio': 'XLN Audio',
        'addictive': 'XLN Audio',
        'garritan': 'Garritan',
        'ivory': 'Synthogy',
        'synthogy': 'Synthogy',
    }

    # Instrument categories
    CATEGORIES = {
        'drums': ['drum', 'percussion', 'kit', 'beats', 'groove', 'snare', 'kick', 'hihat', 'cymbal', 'tom'],
        'keys': ['piano', 'keys', 'keyboard', 'organ', 'rhodes', 'wurlitzer', 'clav', 'electric piano'],
        'strings': ['string', 'violin', 'viola', 'cello', 'bass', 'orchestra', 'ensemble', 'legato'],
        'brass': ['brass', 'trumpet', 'trombone', 'horn', 'tuba', 'french horn'],
        'woodwinds': ['woodwind', 'flute', 'clarinet', 'oboe', 'bassoon', 'sax', 'saxophone'],
        'synth': ['synth', 'analog', 'digital', 'pad', 'lead', 'arp', 'sequence', 'electronic'],
        'guitar': ['guitar', 'acoustic guitar', 'electric guitar', 'bass guitar', 'strat', 'tele'],
        'bass': ['bass', 'sub', 'low end', '808'],
        'vocals': ['vocal', 'voice', 'choir', 'singer'],
        'fx': ['fx', 'effect', 'sound design', 'texture', 'ambient', 'atmosphere', 'foley'],
        'world': ['world', 'ethnic', 'african', 'asian', 'indian', 'middle east', 'latin'],
        'cinematic': ['cinematic', 'film', 'score', 'epic', 'trailer', 'hybrid', 'orchestral'],
    }

    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = output_dir or Path.home() / ".god-library-scan"
        self.output_dir.mkdir(exist_ok=True)
        self.libraries = []
        self.scan_time = None

    def detect_vendor(self, path: str, name: str) -> str:
        """Detect vendor from path or name"""
        text = f"{path} {name}".lower()
        for keyword, vendor in self.VENDORS.items():
            if keyword in text:
                return vendor
        return "Unknown"

    def detect_category(self, path: str, name: str) -> List[str]:
        """Detect instrument categories from path or name"""
        text = f"{path} {name}".lower()
        found = []
        for category, keywords in self.CATEGORIES.items():
            for kw in keywords:
                if kw in text:
                    found.append(category)
                    break
        return found if found else ["uncategorized"]

    def parse_nicnt(self, filepath: Path) -> Optional[Dict]:
        """Parse Native Instruments .nicnt file"""
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            info = {}
            for elem in root.iter():
                if elem.tag == 'Name':
                    info['name'] = elem.text
                elif elem.tag == 'Company':
                    info['vendor'] = elem.text
                elif elem.tag == 'HU':
                    info['id'] = elem.text
                elif elem.tag == 'Version':
                    info['version'] = elem.text
            return info if info else None
        except:
            return None

    def parse_nkx_nki(self, filepath: Path) -> Optional[Dict]:
        """Try to extract info from Kontakt files"""
        # NKI/NKX are binary, just get name from filename
        return {
            'name': filepath.stem,
            'type': filepath.suffix.upper()[1:]
        }

    def scan_library_folder(self, folder: Path) -> Dict:
        """Scan a single library folder"""
        lib = {
            'name': folder.name,
            'path': str(folder),
            'vendor': self.detect_vendor(str(folder), folder.name),
            'categories': self.detect_category(str(folder), folder.name),
            'size_bytes': 0,
            'file_count': 0,
            'sample_formats': set(),
            'has_kontakt': False,
            'has_nicnt': False,
            'metadata': {}
        }

        try:
            for item in folder.rglob('*'):
                if item.is_file():
                    lib['file_count'] += 1
                    try:
                        lib['size_bytes'] += item.stat().st_size
                    except:
                        pass

                    suffix = item.suffix.lower()

                    # Check for Kontakt files
                    if suffix in ['.nki', '.nkm', '.nkx', '.nkc', '.nkr']:
                        lib['has_kontakt'] = True
                        lib['sample_formats'].add('Kontakt')

                    # Check for .nicnt metadata
                    elif suffix == '.nicnt':
                        lib['has_nicnt'] = True
                        meta = self.parse_nicnt(item)
                        if meta:
                            lib['metadata'].update(meta)
                            if 'vendor' in meta and meta['vendor']:
                                lib['vendor'] = meta['vendor']
                            if 'name' in meta and meta['name']:
                                lib['display_name'] = meta['name']

                    # Track sample formats
                    elif suffix in ['.wav', '.aif', '.aiff']:
                        lib['sample_formats'].add('WAV/AIFF')
                    elif suffix in ['.ncw']:
                        lib['sample_formats'].add('NCW (NI Compressed)')
                    elif suffix == '.rex':
                        lib['sample_formats'].add('REX')
                    elif suffix == '.sf2':
                        lib['sample_formats'].add('SoundFont')

        except PermissionError:
            lib['error'] = 'Permission denied'
        except Exception as e:
            lib['error'] = str(e)

        lib['sample_formats'] = list(lib['sample_formats'])
        lib['size_human'] = self._format_size(lib['size_bytes'])
        return lib

    def _format_size(self, bytes: int) -> str:
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.1f}{unit}"
            bytes /= 1024
        return f"{bytes:.1f}PB"

    def scan_drive(self, drive_path: Path, subfolders: List[str] = None):
        """Scan a drive for libraries"""
        print(f"\n{C.BOLD}{C.M}🔍 SCANNING: {drive_path}{C.NC}")
        print(f"{C.C}{'=' * 60}{C.NC}\n")

        if subfolders:
            scan_paths = [drive_path / sf for sf in subfolders]
        else:
            scan_paths = [drive_path]

        for scan_path in scan_paths:
            if not scan_path.exists():
                print(f"{C.Y}Skipping (not found): {scan_path}{C.NC}")
                continue

            print(f"{C.C}Scanning: {scan_path.name}{C.NC}")

            for item in scan_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    print(f"  {C.G}→{C.NC} {item.name}", end='', flush=True)
                    lib = self.scan_library_folder(item)
                    lib['source_drive'] = str(drive_path)
                    self.libraries.append(lib)
                    print(f" ({lib['size_human']})")

        self.scan_time = datetime.now().isoformat()

    def group_by_vendor(self) -> Dict[str, List[Dict]]:
        """Group libraries by vendor"""
        groups = defaultdict(list)
        for lib in self.libraries:
            groups[lib['vendor']].append(lib)
        return dict(sorted(groups.items()))

    def group_by_category(self) -> Dict[str, List[Dict]]:
        """Group libraries by category"""
        groups = defaultdict(list)
        for lib in self.libraries:
            for cat in lib['categories']:
                groups[cat].append(lib)
        return dict(sorted(groups.items()))

    def find_duplicates(self) -> List[Dict]:
        """Find potential duplicate libraries"""
        by_name = defaultdict(list)
        for lib in self.libraries:
            # Normalize name
            name = lib['name'].lower()
            name = re.sub(r'[\s_-]+', ' ', name)
            name = re.sub(r'\b(library|lib)\b', '', name).strip()
            by_name[name].append(lib)

        duplicates = []
        for name, libs in by_name.items():
            if len(libs) > 1:
                duplicates.append({
                    'name': name,
                    'count': len(libs),
                    'locations': [l['path'] for l in libs],
                    'total_size': sum(l['size_bytes'] for l in libs)
                })
        return duplicates

    def generate_report(self) -> str:
        """Generate full scan report"""
        report = []
        report.append(f"\n{'=' * 70}")
        report.append(f"🐟 GOD LIBRARY SCAN REPORT")
        report.append(f"Fish Music Inc - CB_01")
        report.append(f"Scan time: {self.scan_time}")
        report.append(f"{'=' * 70}\n")

        # Summary
        total_size = sum(l['size_bytes'] for l in self.libraries)
        report.append(f"📊 SUMMARY:")
        report.append(f"   Libraries found: {len(self.libraries)}")
        report.append(f"   Total size: {self._format_size(total_size)}")
        report.append("")

        # By Vendor
        report.append(f"📦 BY VENDOR:")
        report.append("-" * 50)
        by_vendor = self.group_by_vendor()
        for vendor, libs in by_vendor.items():
            size = sum(l['size_bytes'] for l in libs)
            report.append(f"   {vendor}: {len(libs)} libraries ({self._format_size(size)})")
        report.append("")

        # By Category
        report.append(f"🎹 BY CATEGORY:")
        report.append("-" * 50)
        by_cat = self.group_by_category()
        for cat, libs in by_cat.items():
            report.append(f"   {cat.title()}: {len(libs)} libraries")
        report.append("")

        # Duplicates
        dupes = self.find_duplicates()
        if dupes:
            report.append(f"⚠️  POTENTIAL DUPLICATES:")
            report.append("-" * 50)
            for d in dupes[:20]:
                report.append(f"   {d['name']}: {d['count']} copies ({self._format_size(d['total_size'])})")
            report.append("")

        report.append(f"{'=' * 70}")
        report.append("GORUNFREE! 🎸🔥")
        report.append("")

        return "\n".join(report)

    def save_results(self):
        """Save scan results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save full JSON
        json_file = self.output_dir / f"library_scan_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump({
                'scan_time': self.scan_time,
                'libraries': self.libraries,
                'by_vendor': self.group_by_vendor(),
                'by_category': self.group_by_category(),
                'duplicates': self.find_duplicates()
            }, f, indent=2, default=str)

        # Save report
        report_file = self.output_dir / f"library_report_{timestamp}.txt"
        with open(report_file, 'w') as f:
            f.write(self.generate_report())

        print(f"\n{C.G}✅ Results saved:{C.NC}")
        print(f"   {C.C}JSON: {json_file}{C.NC}")
        print(f"   {C.C}Report: {report_file}{C.NC}")

        return json_file, report_file


def main():
    scanner = LibraryScanner()

    print(f"\n{C.BOLD}{C.M}╔{'═' * 58}╗{C.NC}")
    print(f"{C.BOLD}{C.M}║  🐟 GOD LIBRARY SCANNER - Metadata & Tag Analysis        ║{C.NC}")
    print(f"{C.BOLD}{C.M}║  Fish Music Inc - CB_01                                  ║{C.NC}")
    print(f"{C.BOLD}{C.M}╚{'═' * 58}╝{C.NC}")

    # Scan Fish drives
    drives_to_scan = [
        ("/Volumes/4TB Blue Fish", ["Native Instruments", "Spectrasonics", "reFX"]),
        ("/Volumes/4TB Big Fish", None),
        ("/Volumes/4TB FISH SG", None),
    ]

    for drive_path, subfolders in drives_to_scan:
        drive = Path(drive_path)
        if drive.exists():
            scanner.scan_drive(drive, subfolders)
        else:
            print(f"{C.Y}Drive not mounted: {drive_path}{C.NC}")

    # Generate and display report
    print(scanner.generate_report())

    # Save results
    scanner.save_results()

    print(f"\n{C.BOLD}{C.M}GORUNFREE! 🎸🔥{C.NC}\n")


if __name__ == "__main__":
    main()
