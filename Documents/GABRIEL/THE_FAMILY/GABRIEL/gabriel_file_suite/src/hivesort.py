#!/usr/bin/env python3
"""
HiveSort - Intelligent File Organization System
Organizes files by category with support for move, copy, symlink, and hardlink operations
"""

import os
import shutil
import sqlite3
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Literal
from enum import Enum
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OrganizeMode(str, Enum):
    """File organization modes"""
    MOVE = "move"          # Move files to organized structure
    COPY = "copy"          # Copy files (mirror)
    SYMLINK = "symlink"    # Create symbolic links
    HARDLINK = "hardlink"  # Create hard links


class HiveSort:
    """Intelligent file organizer with multiple organization strategies"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        
    def _create_category_structure(self, base_path: str, categories: List[str]):
        """Create organized directory structure"""
        base = Path(base_path)
        base.mkdir(parents=True, exist_ok=True)
        
        for category in categories:
            category_path = base / category
            category_path.mkdir(exist_ok=True)
            logger.info(f"Created category: {category_path}")
    
    def _organize_file(
        self, 
        source: str, 
        dest: str, 
        mode: OrganizeMode,
        preserve_structure: bool = False
    ) -> bool:
        """Organize a single file"""
        try:
            dest_path = Path(dest)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            if mode == OrganizeMode.MOVE:
                shutil.move(source, dest)
                logger.debug(f"Moved: {source} -> {dest}")
                
            elif mode == OrganizeMode.COPY:
                shutil.copy2(source, dest)
                logger.debug(f"Copied: {source} -> {dest}")
                
            elif mode == OrganizeMode.SYMLINK:
                if dest_path.exists():
                    dest_path.unlink()
                os.symlink(os.path.abspath(source), dest)
                logger.debug(f"Symlinked: {source} -> {dest}")
                
            elif mode == OrganizeMode.HARDLINK:
                if dest_path.exists():
                    dest_path.unlink()
                os.link(source, dest)
                logger.debug(f"Hardlinked: {source} -> {dest}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to organize {source}: {e}")
            return False
    
    def organize_by_category(
        self,
        output_base: str,
        mode: OrganizeMode = OrganizeMode.SYMLINK,
        preserve_structure: bool = False,
        dry_run: bool = False
    ) -> Dict:
        """Organize files into category-based structure"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get all categorized files
        cursor.execute('''
            SELECT path, filename, ai_category, size
            FROM files
            WHERE ai_category IS NOT NULL
            ORDER BY ai_category, filename
        ''')
        
        files = cursor.fetchall()
        conn.close()
        
        if not files:
            logger.warning("No categorized files found")
            return {'error': 'No categorized files'}
        
        # Get unique categories
        categories = list(set(f[2] for f in files))
        
        if not dry_run:
            self._create_category_structure(output_base, categories)
        
        stats = {
            'total': len(files),
            'organized': 0,
            'failed': 0,
            'categories': {},
            'mode': mode.value,
            'dry_run': dry_run
        }
        
        for path, filename, category, size in files:
            # Determine destination
            if preserve_structure:
                # Keep original directory structure within category
                rel_path = Path(path).relative_to(Path(path).anchor)
                dest = Path(output_base) / category / rel_path
            else:
                # Flat structure within category
                dest = Path(output_base) / category / filename
            
            # Handle filename conflicts
            if dest.exists() and mode != OrganizeMode.SYMLINK:
                stem = dest.stem
                suffix = dest.suffix
                counter = 1
                while dest.exists():
                    dest = dest.parent / f"{stem}_{counter}{suffix}"
                    counter += 1
            
            if dry_run:
                logger.info(f"Would {mode.value}: {path} -> {dest}")
                stats['organized'] += 1
            else:
                success = self._organize_file(path, str(dest), mode, preserve_structure)
                if success:
                    stats['organized'] += 1
                else:
                    stats['failed'] += 1
            
            # Update category stats
            if category not in stats['categories']:
                stats['categories'][category] = {'count': 0, 'size': 0}
            stats['categories'][category]['count'] += 1
            stats['categories'][category]['size'] += size
        
        # Convert sizes to GB
        for cat_stats in stats['categories'].values():
            cat_stats['size_gb'] = round(cat_stats['size'] / (1024**3), 2)
        
        return stats
    
    def organize_by_extension(
        self,
        output_base: str,
        mode: OrganizeMode = OrganizeMode.SYMLINK,
        dry_run: bool = False
    ) -> Dict:
        """Organize files by file extension"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT path, filename, extension, size
            FROM files
            WHERE extension IS NOT NULL AND extension != ''
            ORDER BY extension, filename
        ''')
        
        files = cursor.fetchall()
        conn.close()
        
        stats = {
            'total': len(files),
            'organized': 0,
            'failed': 0,
            'extensions': {},
            'mode': mode.value,
            'dry_run': dry_run
        }
        
        for path, filename, extension, size in files:
            ext_clean = extension.lstrip('.')
            ext_folder = Path(output_base) / ext_clean
            
            if not dry_run:
                ext_folder.mkdir(parents=True, exist_ok=True)
            
            dest = ext_folder / filename
            
            # Handle conflicts
            if dest.exists() and mode != OrganizeMode.SYMLINK:
                counter = 1
                while dest.exists():
                    stem = Path(filename).stem
                    dest = ext_folder / f"{stem}_{counter}{extension}"
                    counter += 1
            
            if dry_run:
                logger.info(f"Would {mode.value}: {path} -> {dest}")
                stats['organized'] += 1
            else:
                success = self._organize_file(path, str(dest), mode)
                if success:
                    stats['organized'] += 1
                else:
                    stats['failed'] += 1
            
            # Update extension stats
            if ext_clean not in stats['extensions']:
                stats['extensions'][ext_clean] = {'count': 0, 'size': 0}
            stats['extensions'][ext_clean]['count'] += 1
            stats['extensions'][ext_clean]['size'] += size
        
        return stats
    
    def handle_duplicates(
        self,
        action: Literal['list', 'keep_newest', 'keep_largest', 'delete_all_but_one'],
        dry_run: bool = True
    ) -> Dict:
        """Handle duplicate files"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Find duplicates
        cursor.execute('''
            SELECT hash_sha256, COUNT(*) as count
            FROM files
            WHERE hash_sha256 IS NOT NULL
            GROUP BY hash_sha256
            HAVING count > 1
        ''')
        
        duplicate_hashes = [row[0] for row in cursor.fetchall()]
        
        stats = {
            'duplicate_groups': len(duplicate_hashes),
            'action': action,
            'files_removed': 0,
            'space_freed': 0,
            'dry_run': dry_run
        }
        
        for hash_val in duplicate_hashes:
            cursor.execute('''
                SELECT path, size, modified
                FROM files
                WHERE hash_sha256 = ?
                ORDER BY modified DESC
            ''', (hash_val,))
            
            duplicates = cursor.fetchall()
            
            if action == 'list':
                logger.info(f"Duplicate group (hash: {hash_val[:8]}...):")
                for path, size, modified in duplicates:
                    logger.info(f"  - {path} ({size} bytes, modified: {modified})")
            
            elif action in ['keep_newest', 'keep_largest', 'delete_all_but_one']:
                # Keep first (newest) and remove rest
                to_remove = duplicates[1:] if action == 'keep_newest' else []
                
                if action == 'keep_largest':
                    sorted_by_size = sorted(duplicates, key=lambda x: x[1], reverse=True)
                    to_remove = sorted_by_size[1:]
                
                for path, size, _ in to_remove:
                    if dry_run:
                        logger.info(f"Would delete: {path} ({size} bytes)")
                    else:
                        try:
                            os.remove(path)
                            cursor.execute('DELETE FROM files WHERE path = ?', (path,))
                            logger.info(f"Deleted: {path}")
                        except Exception as e:
                            logger.error(f"Failed to delete {path}: {e}")
                    
                    stats['files_removed'] += 1
                    stats['space_freed'] += size
        
        if not dry_run:
            conn.commit()
        conn.close()
        
        stats['space_freed_gb'] = round(stats['space_freed'] / (1024**3), 2)
        
        return stats
    
    def create_manifest(self, output_file: str):
        """Create organization manifest"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT ai_category, COUNT(*), SUM(size)
            FROM files
            WHERE ai_category IS NOT NULL
            GROUP BY ai_category
        ''')
        
        manifest = {
            'created': datetime.now().isoformat(),
            'database': self.db_path,
            'categories': {}
        }
        
        for category, count, total_size in cursor.fetchall():
            manifest['categories'][category] = {
                'count': count,
                'size': total_size,
                'size_gb': round(total_size / (1024**3), 2)
            }
        
        conn.close()
        
        with open(output_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        logger.info(f"Manifest created: {output_file}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python hivesort.py <database_path> <output_path> [--mode MODE] [--dry-run]")
        print("Modes: move, copy, symlink, hardlink")
        sys.exit(1)
    
    db_path = sys.argv[1]
    output_path = sys.argv[2]
    
    mode = OrganizeMode.SYMLINK
    if '--mode' in sys.argv:
        idx = sys.argv.index('--mode')
        if idx + 1 < len(sys.argv):
            mode = OrganizeMode(sys.argv[idx + 1])
    
    dry_run = '--dry-run' in sys.argv
    
    organizer = HiveSort(db_path)
    
    print(f"\nOrganizing files (mode: {mode.value}, dry_run: {dry_run})...")
    stats = organizer.organize_by_category(output_path, mode=mode, dry_run=dry_run)
    
    print(f"\nOrganization Results:")
    print(json.dumps(stats, indent=2))
