#!/usr/bin/env python3
# ==============================================================================
# METABEAST_CC - Sample Organization Tool
# ==============================================================================
# Organize sample libraries to SAMPLE_MASTER drive
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

"""
Sample Library Organization Tool

Organizes sample libraries to a structured folder system on the SAMPLE_MASTER drive.
Supports multiple platforms and customizable destination paths.

Usage:
    python organize_samples.py --source ~/Downloads --dest /Volumes/SAMPLE_MASTER
    python organize_samples.py --scan --dest /Volumes/SAMPLE_MASTER
    python organize_samples.py --report
"""

import os
import sys
import json
import shutil
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

# ==============================================================================
# CONFIGURATION
# ==============================================================================

VERSION = "1.0.0"
PROGRAM_NAME = "METABEAST_CC Sample Organizer"

# Default paths by platform
DEFAULT_DESTINATIONS = {
    "darwin": "/Volumes/SAMPLE_MASTER",     # macOS
    "win32": "D:\\SAMPLE_MASTER",            # Windows
    "linux": "/mnt/SAMPLE_MASTER"            # Linux
}

# Sample library folder structure
FOLDER_STRUCTURE = {
    "01_Orchestral": {
        "01_Strings": [],
        "02_Brass": [],
        "03_Woodwinds": [],
        "04_Percussion": [],
        "05_Full_Ensemble": [],
        "06_Solo_Instruments": []
    },
    "02_Cinematic": {
        "01_Epic": [],
        "02_Hybrid": [],
        "03_Choir": [],
        "04_Textures": [],
        "05_Hits_Impacts": [],
        "06_Risers_Downers": []
    },
    "03_Drums": {
        "01_Acoustic_Kits": [],
        "02_Electronic": [],
        "03_Percussion": [],
        "04_Loops": [],
        "05_One_Shots": []
    },
    "04_Keys": {
        "01_Piano_Acoustic": [],
        "02_Piano_Electric": [],
        "03_Organs": [],
        "04_Vintage_Keys": []
    },
    "05_Synths": {
        "01_Analog": [],
        "02_Digital": [],
        "03_Wavetable": [],
        "04_FM": [],
        "05_Granular": []
    },
    "06_Bass": {
        "01_Acoustic": [],
        "02_Electric": [],
        "03_Synth": []
    },
    "07_Guitar": {
        "01_Acoustic": [],
        "02_Electric": [],
        "03_Bass": [],
        "04_Amps_Cabs": []
    },
    "08_Vocals": {
        "01_Choirs": [],
        "02_Solo": [],
        "03_Phrases": [],
        "04_FX": [],
        "05_Acapellas": []
    },
    "09_World_Ethnic": {
        "01_Asian": [],
        "02_Middle_Eastern": [],
        "03_African": [],
        "04_Latin": [],
        "05_Celtic": []
    },
    "10_FX_Foley": {
        "01_Foley": [],
        "02_Ambience": [],
        "03_SFX": [],
        "04_Transitions": []
    },
    "11_Loops_Construction": {
        "01_Genre_Packs": [],
        "02_Construction_Kits": [],
        "03_Stems": [],
        "04_MIDI": []
    },
    "_Archive": {
        "Backups": [],
        "Installers": [],
        "Legacy": []
    },
    "_Unsorted": {}
}

# Known library patterns for auto-detection
LIBRARY_PATTERNS = {
    "spitfire": {
        "folder": "01_Orchestral",
        "keywords": ["spitfire", "bbc", "albion", "labs", "abbey road"]
    },
    "orchestral_tools": {
        "folder": "01_Orchestral",
        "keywords": ["berlin", "metropolis", "sine", "orchestral tools"]
    },
    "heavyocity": {
        "folder": "02_Cinematic",
        "keywords": ["heavyocity", "damage", "gravity", "novo"]
    },
    "8dio": {
        "folder": "02_Cinematic",
        "keywords": ["8dio", "hybrid tools", "century", "lacrimosa"]
    },
    "native_instruments": {
        "folder": "03_Drums",
        "keywords": ["battery", "maschine", "kontakt factory"]
    },
    "toontrack": {
        "folder": "03_Drums",
        "keywords": ["superior drummer", "ezdrummer", "sdx", "ezx"]
    },
    "spectrasonics": {
        "folder": "04_Keys",
        "keywords": ["keyscape", "omnisphere", "trilian"]
    },
    "output": {
        "folder": "11_Loops_Construction",
        "keywords": ["output", "exhale", "signal", "substance", "analog strings"]
    }
}


# ==============================================================================
# COLORS
# ==============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}  {text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")


def print_success(text: str):
    print(f"{Colors.GREEN}[SUCCESS]{Colors.END} {text}")


def print_warning(text: str):
    print(f"{Colors.YELLOW}[WARNING]{Colors.END} {text}")


def print_error(text: str):
    print(f"{Colors.RED}[ERROR]{Colors.END} {text}")


def print_info(text: str):
    print(f"{Colors.BLUE}[INFO]{Colors.END} {text}")


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class LibraryInfo:
    name: str
    path: str
    size_bytes: int
    file_count: int
    format: str  # kontakt, wav, native, etc.
    category: str
    developer: str
    detected_at: str


@dataclass
class OrganizationReport:
    timestamp: str
    source_path: str
    dest_path: str
    libraries_found: int
    libraries_moved: int
    total_size_bytes: int
    errors: List[str]
    libraries: List[Dict]


# ==============================================================================
# SAMPLE ORGANIZER CLASS
# ==============================================================================

class SampleOrganizer:
    """Main class for organizing sample libraries."""

    def __init__(self, destination: str = None):
        self.destination = Path(destination) if destination else self._get_default_dest()
        self.report_data = []
        self.errors = []

    def _get_default_dest(self) -> Path:
        """Get default destination based on platform."""
        import platform
        system = platform.system().lower()
        if system == "darwin":
            return Path(DEFAULT_DESTINATIONS["darwin"])
        elif system == "windows":
            return Path(DEFAULT_DESTINATIONS["win32"])
        else:
            return Path(DEFAULT_DESTINATIONS["linux"])

    def create_structure(self) -> bool:
        """Create the folder structure on destination drive."""
        print_header(f"Creating folder structure on {self.destination}")

        if not self.destination.exists():
            print_error(f"Destination drive not found: {self.destination}")
            print_info("Please mount the SAMPLE_MASTER drive and try again.")
            print_info(f"Or specify a different path with --dest")
            return False

        def create_folders(base: Path, structure: dict):
            for folder, subfolders in structure.items():
                folder_path = base / folder
                folder_path.mkdir(parents=True, exist_ok=True)
                print_info(f"Created: {folder_path}")
                if isinstance(subfolders, dict):
                    create_folders(folder_path, subfolders)

        try:
            create_folders(self.destination, FOLDER_STRUCTURE)
            print_success("Folder structure created successfully!")
            return True
        except Exception as e:
            print_error(f"Failed to create structure: {e}")
            return False

    def detect_library(self, path: Path) -> Optional[LibraryInfo]:
        """Detect library type and metadata from a folder."""
        name = path.name.lower()

        # Count files and get size
        total_size = 0
        file_count = 0
        formats = set()

        try:
            for item in path.rglob("*"):
                if item.is_file():
                    file_count += 1
                    total_size += item.stat().st_size
                    ext = item.suffix.lower()
                    if ext in [".nki", ".nkm", ".nkc", ".nkx"]:
                        formats.add("kontakt")
                    elif ext in [".wav", ".aif", ".aiff"]:
                        formats.add("wav")
                    elif ext == ".ncw":
                        formats.add("kontakt_ncw")
                    elif ext in [".rex", ".rx2"]:
                        formats.add("rex")
                    elif ext == ".exs":
                        formats.add("exs24")
        except PermissionError:
            pass

        # Detect developer and category
        developer = "Unknown"
        category = "_Unsorted"

        for dev, info in LIBRARY_PATTERNS.items():
            for keyword in info["keywords"]:
                if keyword.lower() in name:
                    developer = dev.replace("_", " ").title()
                    category = info["folder"]
                    break

        primary_format = list(formats)[0] if formats else "unknown"

        return LibraryInfo(
            name=path.name,
            path=str(path),
            size_bytes=total_size,
            file_count=file_count,
            format=primary_format,
            category=category,
            developer=developer,
            detected_at=datetime.now().isoformat()
        )

    def scan_source(self, source_path: str) -> List[LibraryInfo]:
        """Scan source folder for sample libraries."""
        source = Path(source_path)
        print_header(f"Scanning: {source}")

        if not source.exists():
            print_error(f"Source path not found: {source}")
            return []

        libraries = []

        for item in source.iterdir():
            if item.is_dir():
                lib_info = self.detect_library(item)
                if lib_info and lib_info.file_count > 0:
                    libraries.append(lib_info)
                    size_mb = lib_info.size_bytes / (1024 * 1024)
                    print_info(f"Found: {lib_info.name} ({size_mb:.1f} MB) -> {lib_info.category}")

        print_success(f"Found {len(libraries)} libraries")
        return libraries

    def move_library(self, lib_info: LibraryInfo, dry_run: bool = True) -> bool:
        """Move a library to the organized destination."""
        source = Path(lib_info.path)
        dest_folder = self.destination / lib_info.category / lib_info.name

        if dry_run:
            print_info(f"[DRY RUN] Would move: {source} -> {dest_folder}")
            return True

        try:
            if dest_folder.exists():
                print_warning(f"Destination exists: {dest_folder}")
                return False

            dest_folder.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(dest_folder))
            print_success(f"Moved: {lib_info.name}")
            return True

        except Exception as e:
            print_error(f"Failed to move {lib_info.name}: {e}")
            self.errors.append(f"{lib_info.name}: {str(e)}")
            return False

    def organize(self, source_path: str, dry_run: bool = True) -> OrganizationReport:
        """Organize libraries from source to destination."""
        print_header(PROGRAM_NAME)

        # Create structure first
        if not dry_run:
            self.create_structure()

        # Scan source
        libraries = self.scan_source(source_path)

        if not libraries:
            print_warning("No libraries found to organize")
            return None

        # Move libraries
        moved_count = 0
        total_size = 0

        print_header("Organizing Libraries" + (" (DRY RUN)" if dry_run else ""))

        for lib in libraries:
            if self.move_library(lib, dry_run):
                moved_count += 1
                total_size += lib.size_bytes

        # Generate report
        report = OrganizationReport(
            timestamp=datetime.now().isoformat(),
            source_path=source_path,
            dest_path=str(self.destination),
            libraries_found=len(libraries),
            libraries_moved=moved_count,
            total_size_bytes=total_size,
            errors=self.errors,
            libraries=[asdict(lib) for lib in libraries]
        )

        # Print summary
        print_header("Summary")
        print(f"  Libraries Found:  {report.libraries_found}")
        print(f"  Libraries Moved:  {report.libraries_moved}")
        print(f"  Total Size:       {total_size / (1024**3):.2f} GB")
        print(f"  Errors:           {len(report.errors)}")

        if dry_run:
            print(f"\n  {Colors.YELLOW}This was a DRY RUN. No files were moved.{Colors.END}")
            print(f"  {Colors.YELLOW}Run with --execute to actually move files.{Colors.END}")

        return report

    def export_report(self, report: OrganizationReport, output_path: str):
        """Export organization report to JSON."""
        with open(output_path, 'w') as f:
            json.dump(asdict(report), f, indent=2)
        print_success(f"Report exported to: {output_path}")

    def generate_inventory(self) -> Dict:
        """Generate inventory of current SAMPLE_MASTER contents."""
        print_header(f"Generating Inventory: {self.destination}")

        if not self.destination.exists():
            print_error(f"Destination not found: {self.destination}")
            return {}

        inventory = {
            "timestamp": datetime.now().isoformat(),
            "path": str(self.destination),
            "categories": {}
        }

        total_size = 0
        total_libs = 0

        for category_dir in self.destination.iterdir():
            if category_dir.is_dir() and not category_dir.name.startswith('.'):
                category_name = category_dir.name
                libraries = []

                for lib_dir in category_dir.iterdir():
                    if lib_dir.is_dir():
                        lib_info = self.detect_library(lib_dir)
                        if lib_info:
                            libraries.append(asdict(lib_info))
                            total_size += lib_info.size_bytes
                            total_libs += 1

                inventory["categories"][category_name] = {
                    "count": len(libraries),
                    "libraries": libraries
                }

                print_info(f"{category_name}: {len(libraries)} libraries")

        inventory["total_libraries"] = total_libs
        inventory["total_size_bytes"] = total_size
        inventory["total_size_gb"] = round(total_size / (1024**3), 2)

        print_success(f"Total: {total_libs} libraries, {inventory['total_size_gb']:.2f} GB")

        return inventory


# ==============================================================================
# CLI
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        prog='organize_samples',
        description=f'{PROGRAM_NAME} v{VERSION}',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Scan and preview organization (dry run)
  python organize_samples.py --source ~/Downloads/Samples --dest /Volumes/SAMPLE_MASTER

  # Actually organize files
  python organize_samples.py --source ~/Downloads/Samples --dest /Volumes/SAMPLE_MASTER --execute

  # Create folder structure only
  python organize_samples.py --dest /Volumes/SAMPLE_MASTER --init

  # Generate inventory report
  python organize_samples.py --dest /Volumes/SAMPLE_MASTER --inventory

Fish Music Inc. / MissionControl96 / NOIZYLAB
'''
    )

    parser.add_argument('--source', '-s', type=str, help='Source folder to scan')
    parser.add_argument('--dest', '-d', type=str, help='Destination SAMPLE_MASTER path')
    parser.add_argument('--execute', '-x', action='store_true', help='Actually move files (default is dry run)')
    parser.add_argument('--init', action='store_true', help='Create folder structure only')
    parser.add_argument('--inventory', action='store_true', help='Generate inventory of destination')
    parser.add_argument('--export', '-e', type=str, help='Export report to JSON file')

    args = parser.parse_args()

    # Initialize organizer
    organizer = SampleOrganizer(args.dest)

    # Handle commands
    if args.init:
        organizer.create_structure()
        return

    if args.inventory:
        inventory = organizer.generate_inventory()
        if args.export:
            with open(args.export, 'w') as f:
                json.dump(inventory, f, indent=2)
            print_success(f"Inventory exported to: {args.export}")
        return

    if args.source:
        dry_run = not args.execute
        report = organizer.organize(args.source, dry_run)

        if report and args.export:
            organizer.export_report(report, args.export)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
