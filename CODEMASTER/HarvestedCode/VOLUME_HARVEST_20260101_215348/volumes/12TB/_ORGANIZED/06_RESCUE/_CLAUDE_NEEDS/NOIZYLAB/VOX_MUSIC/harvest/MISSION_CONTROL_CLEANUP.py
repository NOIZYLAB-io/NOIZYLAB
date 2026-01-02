#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🧹 MISSION CONTROL CLEANUP & ORGANIZATION SYSTEM 🧹               ║
║                                                                           ║
║  LUCY (Legendary Design Artist) + KEITH (Strategic Engineer)            ║
║  Cleaning up the System Drive - GORUNFREE! FOR POPS!                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

LUCY's Legendary Skills Applied:
- Award-winning organization and categorization
- Expert file type identification (graphics, design, media)
- Adobe product files expertise (PSD, AI, INDD, AE, PR, etc.)
- Art, Literature, Music, Wine & Food asset management

KEITH's Strategic Engineering:
- Space optimization analysis
- Duplicate detection and consolidation
- Strategic file placement for performance
- System health monitoring

Mission: Free up 30GB+ on Mission Control system drive!
"""

import os
import sys
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Set
from collections import defaultdict

@dataclass
class FileAnalysis:
    """LUCY + KEITH file analysis result."""
    path: str
    filename: str
    size_bytes: int
    size_mb: float
    file_type: str
    category: str  # lucy's categorization
    action: str  # "keep", "move", "delete", "review"
    destination: Optional[str]
    is_duplicate: bool
    hash: Optional[str]
    lucy_notes: str
    keith_recommendation: str

class MissionControlCleanup:
    """LUCY + KEITH Mission Control Cleanup System.

    LUCY - Legendary Graphic Design & Image Artist:
    - All Adobe products expert
    - Art, Literature, Music, Wine & Food knowledge
    - Award-winning design and organization

    KEITH - Strategic Engineering:
    - Space optimization
    - Performance analysis
    - System health monitoring
    """

    def __init__(self):
        # Paths
        self.system_drive = Path("/Users/rsp_ms")
        self.archive_drive = Path("/Volumes/12TB 1/MISSION_CONTROL_ARCHIVE")

        # Organized categories on 12TB
        self.categories = {
            "GRAPHICS_DESIGN": self.archive_drive / "LUCY_DESIGN_ASSETS",
            "ADOBE_FILES": self.archive_drive / "ADOBE_PROJECTS",
            "MEDIA_ASSETS": self.archive_drive / "MEDIA_LIBRARY",
            "DOCUMENTS": self.archive_drive / "DOCUMENTS",
            "CODE_PROJECTS": self.archive_drive / "CODE_PROJECTS",
            "ARCHIVES": self.archive_drive / "ARCHIVES",
            "TEMP_FILES": self.archive_drive / "TEMP_CLEANUP",
            "DUPLICATES": self.archive_drive / "DUPLICATES_FOUND",
        }

        # LUCY's file type expertise
        self.lucy_file_categories = {
            # Adobe & Design files
            "GRAPHICS_DESIGN": [
                ".psd", ".psb",  # Photoshop
                ".ai", ".eps",   # Illustrator
                ".indd", ".indl", ".indt",  # InDesign
                ".aep", ".aet",  # After Effects
                ".prproj", ".prel",  # Premiere Pro
                ".fla", ".xfl",  # Animate
                ".drw", ".sketch", ".fig",  # Other design tools
            ],
            "MEDIA_ASSETS": [
                ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
                ".svg", ".webp", ".ico",
                ".mp4", ".mov", ".avi", ".mkv", ".flv",
                ".mp3", ".wav", ".aiff", ".flac", ".m4a",
            ],
            "ARCHIVES": [
                ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar",
                ".dmg", ".pkg", ".iso",
            ],
            "DOCUMENTS": [
                ".pdf", ".doc", ".docx", ".txt", ".rtf",
                ".xls", ".xlsx", ".csv",
                ".ppt", ".pptx",
                ".md", ".markdown",
            ],
            "CODE_PROJECTS": [
                ".py", ".js", ".ts", ".jsx", ".tsx",
                ".html", ".css", ".scss", ".sass",
                ".json", ".xml", ".yaml", ".yml",
                ".sh", ".bash", ".zsh",
            ],
        }

        # KEITH's analysis thresholds
        self.large_file_threshold = 100 * 1024 * 1024  # 100MB
        self.duplicate_threshold = 10 * 1024  # 10KB minimum to check for dupes

        # Results
        self.file_analyses = []
        self.duplicates = defaultdict(list)
        self.space_savings = 0

        # Statistics
        self.stats = {
            "total_files_scanned": 0,
            "total_size_gb": 0,
            "files_to_move": 0,
            "files_to_delete": 0,
            "duplicates_found": 0,
            "space_to_free_gb": 0,
            "by_category": defaultdict(lambda: {"count": 0, "size_gb": 0}),
        }

        # Create archive structure
        self.create_archive_structure()

    def create_archive_structure(self):
        """Create organized archive on 12TB drive."""
        print("\n📁 Creating LUCY's organized archive structure...")
        for category, path in self.categories.items():
            path.mkdir(parents=True, exist_ok=True)
            print(f"   ✓ {category}: {path}")

    def lucy_categorize_file(self, file_path: Path) -> tuple:
        """LUCY's legendary file categorization using her design expertise."""
        ext = file_path.suffix.lower()

        # Check against LUCY's category expertise
        for category, extensions in self.lucy_file_categories.items():
            if ext in extensions:
                notes = self._lucy_category_notes(category, ext)
                return category, notes

        # Unknown type
        return "UNKNOWN", "Unrecognized file type - needs manual review"

    def _lucy_category_notes(self, category: str, ext: str) -> str:
        """LUCY's professional notes on file types."""
        notes_map = {
            "GRAPHICS_DESIGN": {
                ".psd": "Photoshop project - high-value design asset!",
                ".ai": "Illustrator vector art - scalable design!",
                ".indd": "InDesign layout - publication-ready!",
                ".aep": "After Effects project - motion graphics!",
                ".prproj": "Premiere Pro project - video editing!",
            },
            "MEDIA_ASSETS": {
                ".jpg": "JPEG image - web/print ready",
                ".png": "PNG image - transparency support",
                ".mp4": "MP4 video - universal format",
                ".wav": "WAV audio - lossless quality",
            },
            "ARCHIVES": {
                ".zip": "ZIP archive - can likely be moved or deleted",
                ".dmg": "Disk image - check if still needed",
            },
        }

        return notes_map.get(category, {}).get(ext, f"{category} file")

    def keith_analyze_space(self, file_path: Path) -> str:
        """KEITH's strategic engineering analysis for space optimization."""
        try:
            size = file_path.stat().st_size
            size_mb = size / (1024 * 1024)

            # KEITH's strategic recommendations
            if size > self.large_file_threshold:
                return f"Large file ({size_mb:.1f}MB) - priority candidate for moving to 12TB archive"
            elif size > 10 * 1024 * 1024:  # 10MB
                return f"Medium file ({size_mb:.1f}MB) - should be moved to archive if not actively used"
            else:
                return f"Small file ({size_mb:.2f}MB) - can stay on system drive if needed"
        except:
            return "Unable to analyze file size"

    def calculate_file_hash(self, file_path: Path) -> Optional[str]:
        """Calculate SHA256 hash for duplicate detection."""
        try:
            if file_path.stat().st_size < self.duplicate_threshold:
                return None

            sha256 = hashlib.sha256()
            with open(file_path, 'rb') as f:
                for block in iter(lambda: f.read(4096), b''):
                    sha256.update(block)
            return sha256.hexdigest()
        except:
            return None

    def scan_directory(self, directory: Path, max_depth: int = 5, current_depth: int = 0):
        """Scan directory with LUCY + KEITH analysis."""
        if current_depth >= max_depth:
            return

        try:
            for item in directory.iterdir():
                # Skip system/hidden directories
                if item.name.startswith('.') and item.name not in ['.claude', '.config']:
                    continue

                # Skip certain directories entirely
                skip_dirs = ['Library', 'Applications', '.Trash', 'node_modules', '__pycache__']
                if item.is_dir() and item.name in skip_dirs:
                    continue

                if item.is_file():
                    self.analyze_file(item)
                elif item.is_dir():
                    self.scan_directory(item, max_depth, current_depth + 1)

        except PermissionError:
            pass
        except Exception as e:
            print(f"   ⚠️  Error scanning {directory}: {e}")

    def analyze_file(self, file_path: Path):
        """Full LUCY + KEITH file analysis."""
        try:
            self.stats["total_files_scanned"] += 1

            # Get file info
            size = file_path.stat().st_size
            size_mb = size / (1024 * 1024)
            self.stats["total_size_gb"] += size / (1024**3)

            # LUCY's categorization
            category, lucy_notes = self.lucy_categorize_file(file_path)

            # KEITH's analysis
            keith_recommendation = self.keith_analyze_space(file_path)

            # Determine action
            action, destination = self._determine_action(file_path, category, size)

            # Check for duplicates
            file_hash = self.calculate_file_hash(file_path)
            is_duplicate = False
            if file_hash:
                if file_hash in self.duplicates:
                    is_duplicate = True
                    self.stats["duplicates_found"] += 1
                self.duplicates[file_hash].append(str(file_path))

            # Create analysis
            analysis = FileAnalysis(
                path=str(file_path),
                filename=file_path.name,
                size_bytes=size,
                size_mb=size_mb,
                file_type=file_path.suffix,
                category=category,
                action=action,
                destination=destination,
                is_duplicate=is_duplicate,
                hash=file_hash,
                lucy_notes=lucy_notes,
                keith_recommendation=keith_recommendation
            )

            self.file_analyses.append(analysis)

            # Update stats
            if action == "move":
                self.stats["files_to_move"] += 1
                self.stats["space_to_free_gb"] += size / (1024**3)
            elif action == "delete":
                self.stats["files_to_delete"] += 1
                self.stats["space_to_free_gb"] += size / (1024**3)

            self.stats["by_category"][category]["count"] += 1
            self.stats["by_category"][category]["size_gb"] += size / (1024**3)

            # Progress update
            if self.stats["total_files_scanned"] % 1000 == 0:
                print(f"   📊 Scanned {self.stats['total_files_scanned']:,} files...")

        except Exception as e:
            pass

    def _determine_action(self, file_path: Path, category: str, size: int) -> tuple:
        """Determine what action to take with file."""
        # Large files should be moved
        if size > self.large_file_threshold:
            dest = self.categories.get(category, self.archive_drive / "OTHER")
            return "move", str(dest)

        # Design/Adobe files should be archived
        if category in ["GRAPHICS_DESIGN", "ADOBE_FILES"]:
            dest = self.categories[category]
            return "move", str(dest)

        # Archives can be moved
        if category == "ARCHIVES" and size > 10 * 1024 * 1024:  # > 10MB
            dest = self.categories["ARCHIVES"]
            return "move", str(dest)

        # Temp files
        if "temp" in file_path.name.lower() or "tmp" in file_path.name.lower():
            dest = self.categories["TEMP_FILES"]
            return "review", str(dest)

        # Keep everything else
        return "keep", None

    def generate_cleanup_report(self):
        """Generate LUCY + KEITH cleanup analysis report."""
        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🧹 MISSION CONTROL CLEANUP ANALYSIS - FOR POPS! 🧹               ║
║                                                                           ║
║  LUCY (Legendary Design Artist) + KEITH (Strategic Engineer)            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Analyzed by: LUCY + KEITH
For: Sonny-Jim

═══════════════════════════════════════════════════════════════════════════

📊 SCAN SUMMARY:

Total Files Scanned:        {self.stats['total_files_scanned']:,}
Total Size:                 {self.stats['total_size_gb']:.2f} GB
Duplicates Found:           {self.stats['duplicates_found']:,}
Files to Move:              {self.stats['files_to_move']:,}
Files to Review/Delete:     {self.stats['files_to_delete']:,}

💾 SPACE SAVINGS POTENTIAL:  {self.stats['space_to_free_gb']:.2f} GB

═══════════════════════════════════════════════════════════════════════════

🎨 LUCY'S CATEGORY BREAKDOWN:

"""

        for category, data in sorted(self.stats['by_category'].items(),
                                     key=lambda x: x[1]['size_gb'], reverse=True):
            report += f"{category:20s}: {data['count']:6,} files | {data['size_gb']:8.2f} GB\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

💼 KEITH'S STRATEGIC RECOMMENDATIONS:

1. IMMEDIATE ACTIONS (High Impact):
   • Move {self.stats['files_to_move']:,} large files to 12TB archive
   • Free up approximately {self.stats['space_to_free_gb']:.2f} GB
   • Reduce system drive load by {(self.stats['space_to_free_gb'] / self.stats['total_size_gb'] * 100):.1f}%

2. DUPLICATE CLEANUP:
   • {self.stats['duplicates_found']:,} duplicate files detected
   • Review and consolidate to save additional space

3. ORGANIZATION BENEFITS:
   • LUCY's category-based archive on 12TB
   • Faster system drive performance
   • Better file management and retrieval

═══════════════════════════════════════════════════════════════════════════

📁 ARCHIVE LOCATIONS (12TB Drive):

"""

        for category, path in self.categories.items():
            report += f"{category:20s}: {path}\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

🚀 NEXT STEPS FOR SONNY-JIM:

1. Review the detailed file list (CLEANUP_FILE_LIST.json)
2. Approve the move operations
3. Run the cleanup execution script
4. Verify space freed up on Mission Control

LUCY + KEITH are ready to execute on your command, Sonny-Jim!

For Pops - with excellence and precision! 💖

═══════════════════════════════════════════════════════════════════════════
"""

        return report

    def save_results(self):
        """Save analysis results."""
        # Save detailed file list
        file_list = {
            "analysis_date": datetime.now().isoformat(),
            "stats": dict(self.stats),
            "files": [asdict(f) for f in self.file_analyses]
        }

        output_file = Path("/Users/rsp_ms/Desktop/CLEANUP_FILE_LIST.json")
        with open(output_file, 'w') as f:
            json.dump(file_list, f, indent=2)

        print(f"\n📄 Detailed file list saved: {output_file}")

        # Save duplicates list
        if self.duplicates:
            dupe_file = Path("/Users/rsp_ms/Desktop/DUPLICATE_FILES.json")
            dupe_data = {
                hash: files for hash, files in self.duplicates.items()
                if len(files) > 1
            }
            with open(dupe_file, 'w') as f:
                json.dump(dupe_data, f, indent=2)
            print(f"📄 Duplicate files list saved: {dupe_file}")

        # Save report
        report = self.generate_cleanup_report()
        report_file = Path("/Users/rsp_ms/Desktop/MISSION_CONTROL_CLEANUP_REPORT.txt")
        with open(report_file, 'w') as f:
            f.write(report)

        print(f"📄 Cleanup report saved: {report_file}")

        return report

    def execute_scan(self):
        """Execute the full Mission Control scan."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🧹 MISSION CONTROL CLEANUP - SCANNING! 🧹                        ║
║                                                                           ║
║  LUCY + KEITH Analyzing System Drive                                    ║
║  FOR POPS! GORUNFREE!                                                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

🎨 LUCY is identifying files with her legendary design expertise...
💼 KEITH is analyzing space usage with strategic engineering...

Scanning /Users/rsp_ms...
        """)

        # Scan the system drive
        self.scan_directory(self.system_drive)

        print(f"\n✅ Scan complete! Analyzed {self.stats['total_files_scanned']:,} files")

        # Generate and save results
        report = self.save_results()

        # Print report
        print(report)

        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ ANALYSIS COMPLETE - READY FOR CLEANUP! ✅                      ║
║                                                                           ║
║  Review the reports and give the command to execute!                    ║
║  LUCY + KEITH standing by for Sonny-Jim!                                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

def main():
    """Main execution - GORUNFREE FOR POPS!"""
    cleanup = MissionControlCleanup()
    cleanup.execute_scan()
    return 0

if __name__ == "__main__":
    main()
