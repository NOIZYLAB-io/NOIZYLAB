#!/usr/bin/env python3
"""
GOD Archive Manager - Smart archive organization & external drive management
CB_01 - Fish Music Inc
For ROB's 80TB music archive quest
GORUNFREE! 🎸🔥
"""

import os
import sys
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict
import subprocess

# Colors
class C:
    R = '\033[0;31m'
    G = '\033[0;32m'
    Y = '\033[1;33m'
    B = '\033[0;34m'
    M = '\033[0;35m'
    C = '\033[0;36m'
    W = '\033[1;37m'
    BOLD = '\033[1m'
    NC = '\033[0m'


class ArchiveManager:
    """Manage archives between local and external storage"""

    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or Path.home() / ".god-archive"
        self.config_dir.mkdir(exist_ok=True)
        self.index_file = self.config_dir / "archive_index.json"
        self.log_file = self.config_dir / f"archive_{datetime.now().strftime('%Y%m%d')}.log"
        self.index = self._load_index()

    def _load_index(self) -> dict:
        """Load archive index"""
        if self.index_file.exists():
            try:
                with open(self.index_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"archives": [], "external_drives": [], "last_updated": None}

    def _save_index(self):
        """Save archive index"""
        self.index["last_updated"] = datetime.now().isoformat()
        with open(self.index_file, 'w') as f:
            json.dump(self.index, f, indent=2)

    def _log(self, message: str):
        """Log operation"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"{C.C}[LOG]{C.NC} {message}")

    def _get_size(self, path: Path) -> int:
        """Get directory size in bytes"""
        total = 0
        try:
            for entry in path.rglob('*'):
                if entry.is_file():
                    total += entry.stat().st_size
        except:
            pass
        return total

    def _format_size(self, bytes: int) -> str:
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.1f}{unit}"
            bytes /= 1024
        return f"{bytes:.1f}PB"

    def _get_file_hash(self, filepath: Path, quick: bool = True) -> str:
        """Get file hash (quick mode: first 1MB only)"""
        hasher = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                if quick:
                    hasher.update(f.read(1024 * 1024))  # First 1MB
                else:
                    for chunk in iter(lambda: f.read(8192), b''):
                        hasher.update(chunk)
            return hasher.hexdigest()[:12]
        except:
            return "unknown"

    def list_external_drives(self) -> List[Path]:
        """List mounted external drives"""
        volumes = Path("/Volumes")
        drives = []

        # Skip system volumes
        skip = ["Macintosh HD", "Macintosh HD - Data", "Recovery", "Preboot", "VM", "Update"]

        if volumes.exists():
            for vol in volumes.iterdir():
                if vol.name not in skip and vol.is_dir():
                    drives.append(vol)

        return drives

    def scan_directory(self, path: Path, min_size_mb: int = 100) -> List[Dict]:
        """Scan directory for archive candidates"""
        candidates = []

        if not path.exists():
            print(f"{C.R}Path not found: {path}{C.NC}")
            return candidates

        print(f"{C.C}Scanning: {path}{C.NC}")
        print(f"{C.C}Min size: {min_size_mb}MB{C.NC}")
        print()

        for item in path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                size = self._get_size(item)
                size_mb = size / (1024 * 1024)

                if size_mb >= min_size_mb:
                    # Count files
                    file_count = sum(1 for _ in item.rglob('*') if _.is_file())

                    # Get modification time
                    try:
                        mtime = datetime.fromtimestamp(item.stat().st_mtime)
                    except:
                        mtime = datetime.now()

                    candidates.append({
                        "name": item.name,
                        "path": str(item),
                        "size_bytes": size,
                        "size_human": self._format_size(size),
                        "file_count": file_count,
                        "modified": mtime.isoformat(),
                        "days_old": (datetime.now() - mtime).days
                    })

        # Sort by size descending
        candidates.sort(key=lambda x: x['size_bytes'], reverse=True)
        return candidates

    def create_archive_manifest(self, source: Path) -> Dict:
        """Create manifest for archive"""
        manifest = {
            "source": str(source),
            "name": source.name,
            "created": datetime.now().isoformat(),
            "total_size": self._get_size(source),
            "files": []
        }

        print(f"{C.C}Creating manifest for: {source.name}{C.NC}")

        for filepath in source.rglob('*'):
            if filepath.is_file():
                rel_path = filepath.relative_to(source)
                manifest["files"].append({
                    "path": str(rel_path),
                    "size": filepath.stat().st_size,
                    "hash": self._get_file_hash(filepath, quick=True)
                })

        manifest["file_count"] = len(manifest["files"])
        manifest["size_human"] = self._format_size(manifest["total_size"])

        return manifest

    def archive_to_external(self, source: Path, dest_drive: Path,
                           delete_source: bool = False,
                           verify: bool = True) -> bool:
        """Move/copy directory to external drive"""

        if not source.exists():
            print(f"{C.R}Source not found: {source}{C.NC}")
            return False

        if not dest_drive.exists():
            print(f"{C.R}Destination drive not found: {dest_drive}{C.NC}")
            return False

        # Create archive destination
        archive_name = source.name
        dest_path = dest_drive / "GOD_ARCHIVES" / archive_name

        # Check if already exists
        if dest_path.exists():
            print(f"{C.Y}Archive already exists at: {dest_path}{C.NC}")
            response = input("Overwrite? (y/n): ")
            if response.lower() != 'y':
                return False
            shutil.rmtree(dest_path)

        # Create manifest before archiving
        manifest = self.create_archive_manifest(source)

        # Create archive directory
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"\n{C.G}Archiving: {source.name}{C.NC}")
        print(f"{C.C}Size: {manifest['size_human']} ({manifest['file_count']} files){C.NC}")
        print(f"{C.C}To: {dest_path}{C.NC}")
        print()

        # Use rsync for reliable copy with progress
        try:
            cmd = [
                "rsync", "-avh", "--progress",
                str(source) + "/",
                str(dest_path) + "/"
            ]
            subprocess.run(cmd, check=True)

            # Save manifest
            manifest_path = dest_path / "_ARCHIVE_MANIFEST.json"
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)

            self._log(f"Archived {source.name} to {dest_path}")

            # Add to index
            self.index["archives"].append({
                "name": archive_name,
                "original_path": str(source),
                "archive_path": str(dest_path),
                "drive": str(dest_drive),
                "size": manifest["total_size"],
                "size_human": manifest["size_human"],
                "file_count": manifest["file_count"],
                "archived_date": datetime.now().isoformat()
            })
            self._save_index()

            # Verify if requested
            if verify:
                print(f"\n{C.C}Verifying archive...{C.NC}")
                dest_size = self._get_size(dest_path)
                if abs(dest_size - manifest["total_size"]) < 1024:  # 1KB tolerance
                    print(f"{C.G}✅ Verification passed{C.NC}")
                else:
                    print(f"{C.Y}⚠️  Size mismatch - verify manually{C.NC}")
                    return False

            # Delete source if requested
            if delete_source:
                print(f"\n{C.Y}Removing source: {source}{C.NC}")
                response = input("Confirm deletion? (type 'DELETE'): ")
                if response == 'DELETE':
                    shutil.rmtree(source)
                    # Create stub with archive info
                    stub_file = source.parent / f"{source.name}_ARCHIVED.txt"
                    with open(stub_file, 'w') as f:
                        f.write(f"ARCHIVED TO: {dest_path}\n")
                        f.write(f"DATE: {datetime.now().isoformat()}\n")
                        f.write(f"SIZE: {manifest['size_human']}\n")
                        f.write(f"FILES: {manifest['file_count']}\n")
                    print(f"{C.G}✅ Source removed, stub created{C.NC}")
                else:
                    print(f"{C.Y}Deletion cancelled{C.NC}")

            return True

        except subprocess.CalledProcessError as e:
            print(f"{C.R}Archive failed: {e}{C.NC}")
            self._log(f"FAILED: Archive {source.name} - {e}")
            return False

    def search_archives(self, query: str) -> List[Dict]:
        """Search archive index"""
        results = []
        query_lower = query.lower()

        for archive in self.index.get("archives", []):
            if query_lower in archive["name"].lower():
                results.append(archive)
            elif query_lower in archive.get("original_path", "").lower():
                results.append(archive)

        return results

    def list_archives(self):
        """List all indexed archives"""
        archives = self.index.get("archives", [])

        if not archives:
            print(f"{C.Y}No archives indexed yet{C.NC}")
            return

        print(f"\n{C.BOLD}{C.M}📦 INDEXED ARCHIVES{C.NC}")
        print(f"{C.C}{'=' * 70}{C.NC}\n")

        total_size = 0
        for arch in archives:
            total_size += arch.get("size", 0)
            print(f"{C.G}{arch['name']}{C.NC}")
            print(f"  Size: {arch['size_human']} | Files: {arch['file_count']}")
            print(f"  Location: {arch['archive_path']}")
            print(f"  Archived: {arch['archived_date'][:10]}")
            print()

        print(f"{C.C}{'=' * 70}{C.NC}")
        print(f"{C.BOLD}Total: {len(archives)} archives, {self._format_size(total_size)}{C.NC}\n")

    def interactive_archive(self, source_dir: Path):
        """Interactive archive wizard"""
        print(f"\n{C.BOLD}{C.M}🗄️  GOD ARCHIVE WIZARD{C.NC}")
        print(f"{C.C}{'=' * 50}{C.NC}\n")

        # Scan for candidates
        candidates = self.scan_directory(source_dir, min_size_mb=100)

        if not candidates:
            print(f"{C.Y}No large directories found (>100MB){C.NC}")
            return

        # Show candidates
        print(f"\n{C.BOLD}{C.Y}ARCHIVE CANDIDATES:{C.NC}\n")
        for i, cand in enumerate(candidates, 1):
            age = f"{cand['days_old']} days old"
            print(f"  {C.G}{i:2d}){C.NC} {cand['name']}")
            print(f"      {cand['size_human']} | {cand['file_count']} files | {age}")

        # List external drives
        print(f"\n{C.BOLD}{C.Y}AVAILABLE DRIVES:{C.NC}\n")
        drives = self.list_external_drives()

        if not drives:
            print(f"{C.Y}  No external drives detected{C.NC}")
            print(f"{C.C}  Connect an external drive and try again{C.NC}")
            return

        for i, drive in enumerate(drives, 1):
            try:
                # Get drive space
                stat = os.statvfs(drive)
                free = stat.f_frsize * stat.f_bavail
                total = stat.f_frsize * stat.f_blocks
                print(f"  {C.G}{i}){C.NC} {drive.name}")
                print(f"     Free: {self._format_size(free)} / {self._format_size(total)}")
            except:
                print(f"  {C.G}{i}){C.NC} {drive.name} (couldn't read space)")

        # Get user selection
        print(f"\n{C.C}Enter directory number to archive (or 'q' to quit):{C.NC} ", end="")
        choice = input().strip()

        if choice.lower() == 'q':
            return

        try:
            dir_idx = int(choice) - 1
            selected = candidates[dir_idx]
        except:
            print(f"{C.R}Invalid selection{C.NC}")
            return

        print(f"\n{C.C}Select destination drive number:{C.NC} ", end="")
        drive_choice = input().strip()

        try:
            drive_idx = int(drive_choice) - 1
            dest_drive = drives[drive_idx]
        except:
            print(f"{C.R}Invalid drive selection{C.NC}")
            return

        # Confirm
        print(f"\n{C.BOLD}{C.Y}CONFIRM ARCHIVE:{C.NC}")
        print(f"  Source: {selected['path']}")
        print(f"  Size: {selected['size_human']}")
        print(f"  Destination: {dest_drive}/GOD_ARCHIVES/{selected['name']}")
        print()

        confirm = input(f"{C.C}Proceed? (y/n):{C.NC} ").strip().lower()

        if confirm == 'y':
            source = Path(selected['path'])
            self.archive_to_external(source, dest_drive, delete_source=False, verify=True)
        else:
            print(f"{C.Y}Archive cancelled{C.NC}")


def main():
    manager = ArchiveManager()

    if len(sys.argv) < 2:
        # Default: show help
        print(f"""
{C.BOLD}{C.M}🗄️  GOD ARCHIVE MANAGER{C.NC}
{C.C}Smart archive organization for 80TB music archive quest{C.NC}
{C.C}Fish Music Inc - CB_01{C.NC}

{C.BOLD}Usage:{C.NC}
  {C.G}python3 god-archive.py scan [path]{C.NC}      Scan directory for archive candidates
  {C.G}python3 god-archive.py drives{C.NC}           List external drives
  {C.G}python3 god-archive.py list{C.NC}             List indexed archives
  {C.G}python3 god-archive.py search [query]{C.NC}   Search archives
  {C.G}python3 god-archive.py wizard [path]{C.NC}    Interactive archive wizard
  {C.G}python3 god-archive.py archive [src] [drive]{C.NC}  Archive directory to drive

{C.BOLD}Examples:{C.NC}
  {C.C}python3 god-archive.py scan ~/NOIZYLAB{C.NC}
  {C.C}python3 god-archive.py wizard ~/NOIZYLAB/ARCHIVES{C.NC}
  {C.C}python3 god-archive.py archive ~/NOIZYLAB/ARCHIVES /Volumes/MyDrive{C.NC}

{C.BOLD}{C.M}GORUNFREE! 🎸🔥{C.NC}
""")
        return

    cmd = sys.argv[1].lower()

    if cmd == "scan":
        path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.home()
        candidates = manager.scan_directory(path)

        if candidates:
            print(f"\n{C.BOLD}{C.Y}ARCHIVE CANDIDATES (>100MB):{C.NC}\n")
            for cand in candidates:
                print(f"  {C.G}{cand['size_human']:>8}{C.NC}  {cand['name']}")
                print(f"           {cand['file_count']} files, {cand['days_old']} days old")
            print()

    elif cmd == "drives":
        drives = manager.list_external_drives()
        print(f"\n{C.BOLD}{C.M}📀 EXTERNAL DRIVES:{C.NC}\n")

        if not drives:
            print(f"{C.Y}  No external drives detected{C.NC}")
        else:
            for drive in drives:
                try:
                    stat = os.statvfs(drive)
                    free = stat.f_frsize * stat.f_bavail
                    total = stat.f_frsize * stat.f_blocks
                    print(f"  {C.G}{drive.name}{C.NC}")
                    print(f"    Path: {drive}")
                    print(f"    Free: {manager._format_size(free)} / {manager._format_size(total)}")
                    print()
                except:
                    print(f"  {C.G}{drive.name}{C.NC} - {drive}")
        print()

    elif cmd == "list":
        manager.list_archives()

    elif cmd == "search":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        if not query:
            print(f"{C.R}Please provide a search query{C.NC}")
            return

        results = manager.search_archives(query)
        if results:
            print(f"\n{C.BOLD}{C.M}🔍 SEARCH RESULTS: '{query}'{C.NC}\n")
            for arch in results:
                print(f"  {C.G}{arch['name']}{C.NC}")
                print(f"    {arch['archive_path']}")
                print(f"    {arch['size_human']} | {arch['file_count']} files")
                print()
        else:
            print(f"{C.Y}No archives found matching '{query}'{C.NC}")

    elif cmd == "wizard":
        path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.home() / "NOIZYLAB"
        manager.interactive_archive(path)

    elif cmd == "archive":
        if len(sys.argv) < 4:
            print(f"{C.R}Usage: god-archive.py archive [source] [drive]{C.NC}")
            return

        source = Path(sys.argv[2])
        dest = Path(sys.argv[3])
        manager.archive_to_external(source, dest)

    else:
        print(f"{C.R}Unknown command: {cmd}{C.NC}")
        print(f"{C.C}Run without arguments for help{C.NC}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.Y}Cancelled{C.NC}")
    except Exception as e:
        print(f"{C.R}Error: {e}{C.NC}")
