#!/usr/bin/env python3
"""
BFD Move Preview - Preview what would be moved without actually moving
Optimized version with error handling and logging
"""

import os
import logging
from pathlib import Path
from datetime import datetime

# Configuration
SRC = Path("/Volumes/4TB Big Fish/BFD")
DST = Path("/Volumes/MAG 4TB/FXpansion")

# Setup logging
log_dir = Path(__file__).parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / f"bfd_preview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def is_bfd_folder(name: str) -> bool:
    """Check if folder name starts with BFD"""
    return name.upper().startswith('BFD')


def get_folder_size(path: Path) -> int:
    """Calculate total size of folder in bytes"""
    total = 0
    try:
        for entry in path.rglob('*'):
            if entry.is_file():
                total += entry.stat().st_size
    except Exception as e:
        logger.warning(f"Error calculating size for {path}: {e}")
    return total


def format_size(bytes: int) -> str:
    """Format bytes to human readable string"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"


def preview_bfd_move():
    """Preview what would be moved without actually moving"""
    try:
        # Validate paths
        if not SRC.exists():
            logger.error(f"Source path does not exist: {SRC}")
            return False
        
        if not DST.exists():
            logger.error(f"Destination path does not exist: {DST}")
            return False
        
        # List folders
        src_folders = [f.name for f in SRC.iterdir() if f.is_dir()]
        
        # Filter BFD folders
        src_bfd_folders = [f for f in src_folders if is_bfd_folder(f)]
        
        logger.info(f"Found {len(src_bfd_folders)} BFD folders in source")
        logger.info(f"\n{'='*60}")
        logger.info("BFD MOVE PREVIEW")
        logger.info(f"{'='*60}\n")
        
        to_move = []
        already_exist = []
        
        # Check each folder
        for folder in src_bfd_folders:
            src_path = SRC / folder
            dst_path = DST / folder
            
            size = get_folder_size(src_path)
            
            if dst_path.exists():
                logger.info(f"✗ Already exists: {folder} ({format_size(size)})")
                already_exist.append((folder, size))
            else:
                logger.info(f"✓ Would move: {folder} ({format_size(size)})")
                to_move.append((folder, size))
        
        # Summary
        total_size = sum(s for _, s in to_move)
        logger.info(f"\n{'='*60}")
        logger.info(f"PREVIEW SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"  Folders to move: {len(to_move)}")
        logger.info(f"  Total size to move: {format_size(total_size)}")
        logger.info(f"  Already exist: {len(already_exist)}")
        logger.info(f"  Log file: {log_file}")
        logger.info(f"{'='*60}")
        
        return True
        
    except Exception as e:
        logger.error(f"Fatal error during preview: {e}")
        return False


if __name__ == "__main__":
    logger.info("Starting BFD Move Preview")
    success = preview_bfd_move()
    exit(0 if success else 1)
