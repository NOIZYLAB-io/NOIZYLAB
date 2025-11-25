#!/usr/bin/env python3
# ==============================================================================
# METABEAST_CC - Backup & Sync Tool
# ==============================================================================
# Automated backup and synchronization for Audio Registry
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

"""
Backup & Sync Tool for METABEAST_CC

Features:
- Automated backups with MD5 verification
- Cloud sync support (iCloud, Dropbox, Google Drive)
- Incremental backup detection
- Restore functionality
- Scheduled backup automation

Usage:
    python backup_sync.py backup --dest ~/Backups/METABEAST
    python backup_sync.py restore --source ~/Backups/METABEAST/latest.tar.gz
    python backup_sync.py sync --provider icloud
    python backup_sync.py verify --backup ~/Backups/METABEAST/latest.tar.gz
"""

import os
import sys
import json
import shutil
import hashlib
import tarfile
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict

# ==============================================================================
# CONFIGURATION
# ==============================================================================

VERSION = "1.0.0"
PROGRAM_NAME = "METABEAST_CC Backup & Sync"

REGISTRY_ROOT = Path(__file__).parent.parent
DATA_DIR = REGISTRY_ROOT / "data"
MANIFESTS_DIR = REGISTRY_ROOT / "manifests"
TOOLS_DIR = REGISTRY_ROOT / "tools"
SNAPSHOTS_DIR = REGISTRY_ROOT / "snapshots"
CHECKSUMS_DIR = REGISTRY_ROOT / "checksums"

# Files to always backup
CRITICAL_FILES = [
    "data/catalog.yaml",
    "data/index.json",
    "RULES.md",
    "CONTRIBUTING.md",
    "README.md",
    "CHANGELOG.md"
]

# Directories to backup
BACKUP_DIRS = [
    "data",
    "manifests",
    "templates",
    "integrations"
]

# Cloud sync paths by provider
CLOUD_PATHS = {
    "icloud": {
        "darwin": "~/Library/Mobile Documents/com~apple~CloudDocs/METABEAST_CC",
        "default": None
    },
    "dropbox": {
        "darwin": "~/Dropbox/METABEAST_CC",
        "win32": "C:\\Users\\{user}\\Dropbox\\METABEAST_CC",
        "linux": "~/Dropbox/METABEAST_CC"
    },
    "google_drive": {
        "darwin": "~/Google Drive/My Drive/METABEAST_CC",
        "win32": "G:\\My Drive\\METABEAST_CC",
        "linux": "~/Google Drive/METABEAST_CC"
    },
    "onedrive": {
        "darwin": "~/OneDrive/METABEAST_CC",
        "win32": "C:\\Users\\{user}\\OneDrive\\METABEAST_CC",
        "linux": "~/OneDrive/METABEAST_CC"
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
class BackupInfo:
    timestamp: str
    filename: str
    path: str
    size_bytes: int
    file_count: int
    checksum: str
    version: str


@dataclass
class BackupReport:
    timestamp: str
    source: str
    destination: str
    backup_file: str
    size_bytes: int
    file_count: int
    checksum: str
    duration_seconds: float
    success: bool
    errors: List[str]


# ==============================================================================
# BACKUP MANAGER CLASS
# ==============================================================================

class BackupManager:
    """Main class for backup and sync operations."""

    def __init__(self):
        self.registry_root = REGISTRY_ROOT
        self.errors = []

    def calculate_checksum(self, file_path: Path) -> str:
        """Calculate MD5 checksum of a file."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_files_to_backup(self) -> List[Path]:
        """Get list of all files to backup."""
        files = []

        for dir_name in BACKUP_DIRS:
            dir_path = self.registry_root / dir_name
            if dir_path.exists():
                for item in dir_path.rglob("*"):
                    if item.is_file() and not item.name.startswith('.'):
                        files.append(item)

        for file_name in CRITICAL_FILES:
            file_path = self.registry_root / file_name
            if file_path.exists() and file_path not in files:
                files.append(file_path)

        return files

    def create_backup(self, dest_path: str, compress: bool = True) -> BackupReport:
        """Create a backup archive."""
        start_time = datetime.now()
        print_header(f"{PROGRAM_NAME} - Creating Backup")

        dest = Path(dest_path)
        dest.mkdir(parents=True, exist_ok=True)

        # Generate backup filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        extension = ".tar.gz" if compress else ".tar"
        backup_filename = f"metabeast_cc_backup_{timestamp}{extension}"
        backup_path = dest / backup_filename

        # Get files
        files = self.get_files_to_backup()
        print_info(f"Found {len(files)} files to backup")

        # Create archive
        mode = "w:gz" if compress else "w"
        try:
            with tarfile.open(backup_path, mode) as tar:
                for file_path in files:
                    arcname = file_path.relative_to(self.registry_root)
                    tar.add(file_path, arcname=arcname)
                    print_info(f"Added: {arcname}")

            # Calculate checksum
            checksum = self.calculate_checksum(backup_path)
            size = backup_path.stat().st_size

            # Save checksum file
            checksum_file = backup_path.with_suffix(backup_path.suffix + ".md5")
            with open(checksum_file, 'w') as f:
                f.write(f"{checksum}  {backup_filename}\n")

            # Create 'latest' symlink
            latest_link = dest / f"latest{extension}"
            if latest_link.exists() or latest_link.is_symlink():
                latest_link.unlink()
            latest_link.symlink_to(backup_path.name)

            duration = (datetime.now() - start_time).total_seconds()

            print_success(f"Backup created: {backup_path}")
            print_info(f"Size: {size / (1024*1024):.2f} MB")
            print_info(f"Checksum: {checksum}")
            print_info(f"Duration: {duration:.2f} seconds")

            return BackupReport(
                timestamp=timestamp,
                source=str(self.registry_root),
                destination=str(dest),
                backup_file=str(backup_path),
                size_bytes=size,
                file_count=len(files),
                checksum=checksum,
                duration_seconds=duration,
                success=True,
                errors=[]
            )

        except Exception as e:
            print_error(f"Backup failed: {e}")
            return BackupReport(
                timestamp=timestamp,
                source=str(self.registry_root),
                destination=str(dest),
                backup_file="",
                size_bytes=0,
                file_count=0,
                checksum="",
                duration_seconds=0,
                success=False,
                errors=[str(e)]
            )

    def restore_backup(self, backup_path: str, dest_path: str = None, verify: bool = True) -> bool:
        """Restore from a backup archive."""
        print_header(f"{PROGRAM_NAME} - Restoring Backup")

        backup = Path(backup_path)
        if not backup.exists():
            print_error(f"Backup file not found: {backup}")
            return False

        dest = Path(dest_path) if dest_path else self.registry_root

        # Verify checksum if available
        if verify:
            checksum_file = backup.with_suffix(backup.suffix + ".md5")
            if checksum_file.exists():
                with open(checksum_file, 'r') as f:
                    expected = f.read().split()[0]
                actual = self.calculate_checksum(backup)
                if expected != actual:
                    print_error(f"Checksum mismatch! Expected: {expected}, Got: {actual}")
                    return False
                print_success("Checksum verified")

        # Extract archive
        try:
            print_info(f"Extracting to: {dest}")
            with tarfile.open(backup, "r:*") as tar:
                tar.extractall(dest)

            print_success("Backup restored successfully!")
            return True

        except Exception as e:
            print_error(f"Restore failed: {e}")
            return False

    def verify_backup(self, backup_path: str) -> bool:
        """Verify backup integrity."""
        print_header(f"{PROGRAM_NAME} - Verifying Backup")

        backup = Path(backup_path)
        if not backup.exists():
            print_error(f"Backup file not found: {backup}")
            return False

        # Check checksum
        checksum_file = backup.with_suffix(backup.suffix + ".md5")
        if checksum_file.exists():
            with open(checksum_file, 'r') as f:
                expected = f.read().split()[0]
            actual = self.calculate_checksum(backup)
            if expected != actual:
                print_error(f"Checksum FAILED! Expected: {expected}, Got: {actual}")
                return False
            print_success(f"Checksum OK: {actual}")
        else:
            print_warning("No checksum file found")
            actual = self.calculate_checksum(backup)
            print_info(f"Calculated checksum: {actual}")

        # Try to open and list contents
        try:
            with tarfile.open(backup, "r:*") as tar:
                members = tar.getmembers()
                print_info(f"Archive contains {len(members)} files")

                # Check for critical files
                member_names = [m.name for m in members]
                for critical in CRITICAL_FILES:
                    if critical in member_names:
                        print_success(f"Found: {critical}")
                    else:
                        print_warning(f"Missing: {critical}")

            print_success("Backup verification complete!")
            return True

        except Exception as e:
            print_error(f"Verification failed: {e}")
            return False

    def sync_to_cloud(self, provider: str) -> bool:
        """Sync backup to cloud storage."""
        print_header(f"{PROGRAM_NAME} - Syncing to {provider.title()}")

        import platform
        system = platform.system().lower()
        if system == "darwin":
            platform_key = "darwin"
        elif system == "windows":
            platform_key = "win32"
        else:
            platform_key = "linux"

        if provider not in CLOUD_PATHS:
            print_error(f"Unknown cloud provider: {provider}")
            print_info(f"Available: {', '.join(CLOUD_PATHS.keys())}")
            return False

        cloud_path = CLOUD_PATHS[provider].get(platform_key)
        if not cloud_path:
            print_error(f"{provider} is not available on {platform_key}")
            return False

        # Expand path
        cloud_path = Path(os.path.expanduser(cloud_path.format(user=os.environ.get("USER", ""))))

        if not cloud_path.parent.exists():
            print_error(f"Cloud sync folder not found: {cloud_path.parent}")
            print_info(f"Make sure {provider} is installed and configured")
            return False

        # Create backup and sync
        cloud_path.mkdir(parents=True, exist_ok=True)
        report = self.create_backup(str(cloud_path))

        if report.success:
            print_success(f"Synced to {provider}: {cloud_path}")
            return True
        else:
            print_error("Sync failed")
            return False

    def list_backups(self, backup_dir: str) -> List[BackupInfo]:
        """List all backups in a directory."""
        print_header(f"{PROGRAM_NAME} - Available Backups")

        backup_path = Path(backup_dir)
        if not backup_path.exists():
            print_error(f"Backup directory not found: {backup_dir}")
            return []

        backups = []
        for tar_file in sorted(backup_path.glob("metabeast_cc_backup_*.tar*"), reverse=True):
            size = tar_file.stat().st_size
            checksum_file = tar_file.with_suffix(tar_file.suffix + ".md5")
            checksum = ""
            if checksum_file.exists():
                with open(checksum_file, 'r') as f:
                    checksum = f.read().split()[0]

            backup_info = BackupInfo(
                timestamp=tar_file.stem.replace("metabeast_cc_backup_", ""),
                filename=tar_file.name,
                path=str(tar_file),
                size_bytes=size,
                file_count=0,
                checksum=checksum,
                version=VERSION
            )
            backups.append(backup_info)

            # Print info
            size_mb = size / (1024 * 1024)
            print(f"  {Colors.CYAN}{tar_file.name}{Colors.END}")
            print(f"    Size: {size_mb:.2f} MB | Checksum: {checksum[:8]}...")

        print(f"\n  Total: {len(backups)} backups")
        return backups

    def cleanup_old_backups(self, backup_dir: str, keep: int = 5) -> int:
        """Remove old backups, keeping the most recent ones."""
        print_header(f"{PROGRAM_NAME} - Cleanup Old Backups")

        backup_path = Path(backup_dir)
        backups = sorted(backup_path.glob("metabeast_cc_backup_*.tar*"), reverse=True)

        if len(backups) <= keep:
            print_info(f"Only {len(backups)} backups found, nothing to clean")
            return 0

        removed = 0
        for backup_file in backups[keep:]:
            print_info(f"Removing: {backup_file.name}")
            backup_file.unlink()

            # Remove checksum file too
            checksum_file = backup_file.with_suffix(backup_file.suffix + ".md5")
            if checksum_file.exists():
                checksum_file.unlink()

            removed += 1

        print_success(f"Removed {removed} old backups")
        return removed


# ==============================================================================
# CLI
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        prog='backup_sync',
        description=f'{PROGRAM_NAME} v{VERSION}',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Create backup
  python backup_sync.py backup --dest ~/Backups/METABEAST

  # Restore from backup
  python backup_sync.py restore --source ~/Backups/METABEAST/latest.tar.gz

  # Verify backup integrity
  python backup_sync.py verify --backup ~/Backups/METABEAST/latest.tar.gz

  # Sync to cloud
  python backup_sync.py sync --provider dropbox

  # List backups
  python backup_sync.py list --dir ~/Backups/METABEAST

  # Cleanup old backups
  python backup_sync.py cleanup --dir ~/Backups/METABEAST --keep 5

Fish Music Inc. / MissionControl96 / NOIZYLAB
'''
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Create backup')
    backup_parser.add_argument('--dest', '-d', required=True, help='Destination directory')
    backup_parser.add_argument('--no-compress', action='store_true', help='Skip compression')

    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore from backup')
    restore_parser.add_argument('--source', '-s', required=True, help='Backup file')
    restore_parser.add_argument('--dest', '-d', help='Destination (default: registry root)')
    restore_parser.add_argument('--no-verify', action='store_true', help='Skip checksum verification')

    # Verify command
    verify_parser = subparsers.add_parser('verify', help='Verify backup integrity')
    verify_parser.add_argument('--backup', '-b', required=True, help='Backup file')

    # Sync command
    sync_parser = subparsers.add_parser('sync', help='Sync to cloud')
    sync_parser.add_argument('--provider', '-p', required=True,
                            choices=['icloud', 'dropbox', 'google_drive', 'onedrive'],
                            help='Cloud provider')

    # List command
    list_parser = subparsers.add_parser('list', help='List backups')
    list_parser.add_argument('--dir', '-d', required=True, help='Backup directory')

    # Cleanup command
    cleanup_parser = subparsers.add_parser('cleanup', help='Remove old backups')
    cleanup_parser.add_argument('--dir', '-d', required=True, help='Backup directory')
    cleanup_parser.add_argument('--keep', '-k', type=int, default=5, help='Number to keep')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    manager = BackupManager()

    if args.command == 'backup':
        report = manager.create_backup(args.dest, compress=not args.no_compress)
        if report.success:
            # Export report
            report_file = Path(args.dest) / f"backup_report_{report.timestamp}.json"
            with open(report_file, 'w') as f:
                json.dump(asdict(report), f, indent=2)

    elif args.command == 'restore':
        manager.restore_backup(args.source, args.dest, verify=not args.no_verify)

    elif args.command == 'verify':
        manager.verify_backup(args.backup)

    elif args.command == 'sync':
        manager.sync_to_cloud(args.provider)

    elif args.command == 'list':
        manager.list_backups(args.dir)

    elif args.command == 'cleanup':
        manager.cleanup_old_backups(args.dir, args.keep)


if __name__ == '__main__':
    main()
