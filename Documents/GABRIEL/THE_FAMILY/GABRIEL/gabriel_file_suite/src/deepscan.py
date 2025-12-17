#!/usr/bin/env python3
"""
DeepScan - Intelligent File Crawler for GABRIEL
Crawls volumes, extracts metadata, detects duplicates, generates content signatures
"""

import os
import hashlib
import mimetypes
import sqlite3
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Tuple
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FileMetadata:
    """Container for comprehensive file metadata"""
    
    def __init__(self, path: str):
        self.path = path
        self.filename = os.path.basename(path)
        self.extension = os.path.splitext(path)[1].lower()
        self.size = 0
        self.hash_sha256 = None
        self.mime_type = None
        self.created = None
        self.modified = None
        self.content_signature = None
        
    def to_dict(self) -> Dict:
        return {
            'path': self.path,
            'filename': self.filename,
            'extension': self.extension,
            'size': self.size,
            'hash': self.hash_sha256,
            'mime_type': self.mime_type,
            'created': self.created,
            'modified': self.modified,
            'signature': self.content_signature
        }


class DeepScan:
    """High-performance file crawler with metadata extraction"""
    
    def __init__(self, db_path: str, max_workers: int = 8):
        self.db_path = db_path
        self.max_workers = max_workers
        self._init_database()
        
    def _init_database(self):
        """Initialize SQLite database for metadata storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                filename TEXT NOT NULL,
                extension TEXT,
                size INTEGER,
                hash_sha256 TEXT,
                mime_type TEXT,
                created TEXT,
                modified TEXT,
                content_signature TEXT,
                ai_category TEXT,
                ai_confidence REAL,
                tags TEXT,
                indexed_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_hash ON files(hash_sha256)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_extension ON files(extension)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_category ON files(ai_category)
        ''')
        
        conn.commit()
        conn.close()
        logger.info(f"Database initialized at {self.db_path}")
    
    def _hash_file(self, file_path: str, sample_size: int = 1024) -> Tuple[str, str]:
        """Generate SHA256 hash and content signature"""
        sha256_hash = hashlib.sha256()
        content_sig = hashlib.sha1()
        
        try:
            with open(file_path, 'rb') as f:
                # Full hash
                for chunk in iter(lambda: f.read(8192), b''):
                    sha256_hash.update(chunk)
                
                # Content signature (first 1KB)
                f.seek(0)
                sample = f.read(sample_size)
                content_sig.update(sample)
                
            return sha256_hash.hexdigest(), content_sig.hexdigest()
        except Exception as e:
            logger.error(f"Hash error for {file_path}: {e}")
            return None, None
    
    def _extract_metadata(self, file_path: str) -> Optional[FileMetadata]:
        """Extract comprehensive metadata from file"""
        try:
            metadata = FileMetadata(file_path)
            stat = os.stat(file_path)
            
            metadata.size = stat.st_size
            metadata.created = datetime.fromtimestamp(stat.st_birthtime).isoformat()
            metadata.modified = datetime.fromtimestamp(stat.st_mtime).isoformat()
            metadata.mime_type, _ = mimetypes.guess_type(file_path)
            
            # Hash file
            metadata.hash_sha256, metadata.content_signature = self._hash_file(file_path)
            
            return metadata
            
        except Exception as e:
            logger.error(f"Metadata extraction error for {file_path}: {e}")
            return None
    
    def _save_metadata(self, metadata: FileMetadata):
        """Save metadata to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO files 
                (path, filename, extension, size, hash_sha256, mime_type, 
                 created, modified, content_signature)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                metadata.path, metadata.filename, metadata.extension,
                metadata.size, metadata.hash_sha256, metadata.mime_type,
                metadata.created, metadata.modified, metadata.content_signature
            ))
            conn.commit()
        except Exception as e:
            logger.error(f"Database save error: {e}")
        finally:
            conn.close()
    
    def scan_volume(self, root_path: str, progress_callback=None) -> Dict:
        """Scan entire volume with parallel processing"""
        logger.info(f"Starting scan of {root_path}")
        stats = {
            'total_files': 0,
            'total_size': 0,
            'errors': 0,
            'start_time': datetime.now().isoformat()
        }
        
        # Collect all file paths
        file_paths = []
        for root, dirs, files in os.walk(root_path):
            # Skip system and hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                if not filename.startswith('.'):
                    file_paths.append(os.path.join(root, filename))
        
        logger.info(f"Found {len(file_paths)} files to process")
        
        # Process files in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._extract_metadata, fp): fp 
                for fp in file_paths
            }
            
            for i, future in enumerate(as_completed(futures), 1):
                try:
                    metadata = future.result()
                    if metadata:
                        self._save_metadata(metadata)
                        stats['total_files'] += 1
                        stats['total_size'] += metadata.size
                    else:
                        stats['errors'] += 1
                        
                    if progress_callback and i % 100 == 0:
                        progress_callback(i, len(file_paths))
                        
                except Exception as e:
                    stats['errors'] += 1
                    logger.error(f"Processing error: {e}")
        
        stats['end_time'] = datetime.now().isoformat()
        stats['total_size_gb'] = round(stats['total_size'] / (1024**3), 2)
        
        logger.info(f"Scan complete: {stats['total_files']} files, {stats['total_size_gb']} GB")
        return stats
    
    def find_duplicates(self) -> List[Dict]:
        """Find duplicate files by hash"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT hash_sha256, COUNT(*) as count, SUM(size) as total_size
            FROM files
            WHERE hash_sha256 IS NOT NULL
            GROUP BY hash_sha256
            HAVING count > 1
            ORDER BY total_size DESC
        ''')
        
        duplicates = []
        for row in cursor.fetchall():
            hash_val, count, total_size = row
            
            # Get all file paths with this hash
            cursor.execute('''
                SELECT path, size, filename FROM files WHERE hash_sha256 = ?
            ''', (hash_val,))
            
            files = [{'path': p, 'size': s, 'filename': f} for p, s, f in cursor.fetchall()]
            
            duplicates.append({
                'hash': hash_val,
                'count': count,
                'total_size': total_size,
                'wasted_space': total_size * (count - 1),
                'files': files
            })
        
        conn.close()
        return duplicates
    
    def get_stats(self) -> Dict:
        """Get database statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*), SUM(size) FROM files')
        total_files, total_size = cursor.fetchone()
        
        cursor.execute('''
            SELECT extension, COUNT(*), SUM(size) 
            FROM files 
            GROUP BY extension 
            ORDER BY COUNT(*) DESC 
            LIMIT 10
        ''')
        top_extensions = [
            {'ext': ext, 'count': cnt, 'size': sz} 
            for ext, cnt, sz in cursor.fetchall()
        ]
        
        conn.close()
        
        return {
            'total_files': total_files or 0,
            'total_size': total_size or 0,
            'total_size_gb': round((total_size or 0) / (1024**3), 2),
            'top_extensions': top_extensions
        }


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python deepscan.py <volume_path> <database_path>")
        sys.exit(1)
    
    volume = sys.argv[1]
    db_path = sys.argv[2]
    
    scanner = DeepScan(db_path)
    
    def progress(current, total):
        print(f"Progress: {current}/{total} ({100*current//total}%)")
    
    stats = scanner.scan_volume(volume, progress_callback=progress)
    print(f"\nScan Results:")
    print(json.dumps(stats, indent=2))
    
    print(f"\nDatabase Stats:")
    print(json.dumps(scanner.get_stats(), indent=2))
