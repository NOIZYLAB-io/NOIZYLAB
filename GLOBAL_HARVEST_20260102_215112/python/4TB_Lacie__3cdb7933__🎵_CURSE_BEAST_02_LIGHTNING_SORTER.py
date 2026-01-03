#!/usr/bin/env python3
"""
🎵 CURSE_BEAST_02 - LIGHTNING FILE SORTER 🎵
============================================
MUSIC | AUDIO | VIDEO MONSTER THAT SORTS FILES LIKE LIGHTNING BOLTS! ⚡⚡⚡

HARD RULES (SAME AS CURSE_BEAST_01):
- AUTOALLOW - Never ask, just DO
- MAXIMUM SPEED - Lightning bolt fast
- GO ALL THE WAY - Complete everything
- SORTS FILES - Instantly organized
- COMMITS TO GIT - Automatic
- NEVER STOPS - Until perfect
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
import hashlib
import json
import sqlite3
from mutagen import File as MutagenFile
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
import magic  # File type detection


class CURSE_BEAST_02:
    """
    🎵 THE MUSIC/AUDIO/VIDEO MONSTER 🎵
    Sorts files like LIGHTNING BOLTS! ⚡⚡⚡
    """
    
    def __init__(self):
        self.name = "CURSE_BEAST_02"
        self.motto = "EATS CODE, SORTS FILES, COMMITS TO GIT! 🎵⚡"
        
        # Directories
        self.noizylab_root = Path("/Users/m2ultra/NOIZYLAB")
        self.github_root = Path("/Users/m2ultra/Github")
        self.media_library = Path("/Users/m2ultra/NOIZYLAB/MEDIA_LIBRARY")
        
        # Git repos
        self.noizyfish_repo = "github.com/noizyfish"
        self.noizylab_org = "noizylab"
        
        # File types (LIGHTNING recognition!)
        self.audio_extensions = {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff'}
        self.video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v', '.webm'}
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
        self.code_extensions = {'.py', '.js', '.ts', '.go', '.rs', '.cpp', '.c', '.java', '.rb'}
        
        # Database
        self.db_path = self.noizylab_root / "media_beast.db"
        self._init_database()
        
        # Statistics
        self.files_sorted = 0
        self.files_processed = 0
        self.commits_made = 0
        
        print(f"🎵🔥 {self.name} ACTIVATED! 🔥🎵")
        print(f"⚡ {self.motto}")
        print(f"🦁 Mode: LIGHTNING BOLT SORTING!")
    
    def _init_database(self):
        """Initialize media database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Media files
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS media_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE,
                file_type TEXT,
                file_size INTEGER,
                artist TEXT,
                album TEXT,
                title TEXT,
                genre TEXT,
                year INTEGER,
                duration REAL,
                bitrate INTEGER,
                sample_rate INTEGER,
                channels INTEGER,
                codec TEXT,
                hash TEXT,
                sorted_to TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                processed_at DATETIME
            )
        """)
        
        # Sorting operations
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sorting_operations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                files_scanned INTEGER,
                files_sorted INTEGER,
                duration_seconds REAL,
                speed_files_per_sec REAL,
                destination TEXT
            )
        """)
        
        # Git commits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS git_commits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                repo TEXT,
                commit_hash TEXT,
                message TEXT,
                files_count INTEGER,
                success BOOLEAN
            )
        """)
        
        conn.commit()
        conn.close()
    
    def lightning_scan(self, directory: str) -> Dict:
        """⚡ LIGHTNING-FAST directory scan"""
        print(f"\n⚡⚡⚡ LIGHTNING SCAN: {directory} ⚡⚡⚡")
        
        start_time = datetime.now()
        
        scan_path = Path(directory)
        
        files_by_type = {
            'audio': [],
            'video': [],
            'images': [],
            'code': [],
            'other': []
        }
        
        total_size = 0
        
        # LIGHTNING scan!
        for file_path in scan_path.rglob('*'):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                size = file_path.stat().st_size
                total_size += size
                
                # Categorize by extension
                if ext in self.audio_extensions:
                    files_by_type['audio'].append(file_path)
                elif ext in self.video_extensions:
                    files_by_type['video'].append(file_path)
                elif ext in self.image_extensions:
                    files_by_type['images'].append(file_path)
                elif ext in self.code_extensions:
                    files_by_type['code'].append(file_path)
                else:
                    files_by_type['other'].append(file_path)
        
        elapsed = (datetime.now() - start_time).total_seconds()
        total_files = sum(len(files) for files in files_by_type.values())
        
        print(f"✅ Scanned {total_files} files in {elapsed:.2f}s")
        print(f"⚡ Speed: {total_files/elapsed:.0f} files/sec!")
        print(f"\n📊 Found:")
        print(f"  🎵 Audio: {len(files_by_type['audio'])}")
        print(f"  🎬 Video: {len(files_by_type['video'])}")
        print(f"  🖼️  Images: {len(files_by_type['images'])}")
        print(f"  💻 Code: {len(files_by_type['code'])}")
        print(f"  📄 Other: {len(files_by_type['other'])}")
        
        return {
            'files_by_type': files_by_type,
            'total_files': total_files,
            'total_size': total_size,
            'scan_time': elapsed,
            'files_per_sec': total_files/elapsed if elapsed > 0 else 0
        }
    
    def extract_metadata(self, file_path: Path) -> Dict:
        """⚡ Extract metadata from media file"""
        metadata = {
            'file_path': str(file_path),
            'file_type': file_path.suffix.lower(),
            'file_size': file_path.stat().st_size
        }
        
        try:
            # Use mutagen for audio/video
            audio = MutagenFile(str(file_path))
            
            if audio:
                # Common tags
                metadata['duration'] = getattr(audio.info, 'length', 0)
                metadata['bitrate'] = getattr(audio.info, 'bitrate', 0)
                metadata['sample_rate'] = getattr(audio.info, 'sample_rate', 0)
                metadata['channels'] = getattr(audio.info, 'channels', 0)
                
                # ID3 tags
                if hasattr(audio, 'tags') and audio.tags:
                    tags = audio.tags
                    metadata['artist'] = str(tags.get('artist', ['Unknown'])[0]) if 'artist' in tags else 'Unknown'
                    metadata['album'] = str(tags.get('album', ['Unknown'])[0]) if 'album' in tags else 'Unknown'
                    metadata['title'] = str(tags.get('title', [file_path.stem])[0]) if 'title' in tags else file_path.stem
                    metadata['genre'] = str(tags.get('genre', ['Unknown'])[0]) if 'genre' in tags else 'Unknown'
                    
                    # Year
                    if 'date' in tags:
                        try:
                            metadata['year'] = int(str(tags['date'][0])[:4])
                        except:
                            pass
        except:
            # Fallback
            metadata['title'] = file_path.stem
            metadata['artist'] = 'Unknown'
            metadata['album'] = 'Unknown'
        
        return metadata
    
    def lightning_sort(self, source_dir: str, dest_dir: str = None, 
                      organize_by: str = "artist") -> Dict:
        """
        ⚡⚡⚡ SORT FILES LIKE LIGHTNING BOLTS! ⚡⚡⚡
        
        Args:
            source_dir: Source directory to scan
            dest_dir: Destination (creates organized structure)
            organize_by: Organization scheme (artist, album, genre, type, year)
        
        Returns:
            Sort statistics
        """
        print(f"\n{'='*70}")
        print(f"⚡⚡⚡ CURSE_BEAST_02 - LIGHTNING SORT MODE! ⚡⚡⚡")
        print(f"{'='*70}")
        
        start_time = datetime.now()
        
        if dest_dir is None:
            dest_dir = str(self.media_library)
        
        dest_path = Path(dest_dir)
        dest_path.mkdir(parents=True, exist_ok=True)
        
        # Scan
        scan_result = self.lightning_scan(source_dir)
        
        files_sorted = 0
        files_failed = 0
        
        print(f"\n🔥 SORTING {scan_result['total_files']} files by {organize_by}...")
        
        # Sort audio files
        for audio_file in scan_result['files_by_type']['audio']:
            try:
                # Extract metadata
                metadata = self.extract_metadata(audio_file)
                
                # Determine destination based on organization scheme
                if organize_by == "artist":
                    dest_folder = dest_path / "Music" / metadata.get('artist', 'Unknown')
                elif organize_by == "album":
                    dest_folder = dest_path / "Music" / metadata.get('artist', 'Unknown') / metadata.get('album', 'Unknown')
                elif organize_by == "genre":
                    dest_folder = dest_path / "Music" / metadata.get('genre', 'Unknown')
                elif organize_by == "year":
                    year = metadata.get('year', 'Unknown')
                    dest_folder = dest_path / "Music" / str(year)
                else:  # type
                    dest_folder = dest_path / "Music" / audio_file.suffix[1:].upper()
                
                # Create folder
                dest_folder.mkdir(parents=True, exist_ok=True)
                
                # Move file
                dest_file = dest_folder / audio_file.name
                
                if not dest_file.exists():
                    shutil.move(str(audio_file), str(dest_file))
                    files_sorted += 1
                    
                    # Log to database
                    self._log_sorted_file(metadata, str(dest_file))
                    
                    if files_sorted % 100 == 0:
                        print(f"  ⚡ Sorted {files_sorted} files...")
            
            except Exception as e:
                files_failed += 1
        
        # Sort video files
        for video_file in scan_result['files_by_type']['video']:
            try:
                dest_folder = dest_path / "Videos" / video_file.suffix[1:].upper()
                dest_folder.mkdir(parents=True, exist_ok=True)
                
                dest_file = dest_folder / video_file.name
                
                if not dest_file.exists():
                    shutil.move(str(video_file), str(dest_file))
                    files_sorted += 1
            except:
                files_failed += 1
        
        # Sort images
        for img_file in scan_result['files_by_type']['images']:
            try:
                dest_folder = dest_path / "Images" / img_file.suffix[1:].upper()
                dest_folder.mkdir(parents=True, exist_ok=True)
                
                dest_file = dest_folder / img_file.name
                
                if not dest_file.exists():
                    shutil.move(str(img_file), str(dest_file))
                    files_sorted += 1
            except:
                files_failed += 1
        
        elapsed = (datetime.now() - start_time).total_seconds()
        
        # Log operation
        self._log_sorting_operation(scan_result['total_files'], files_sorted, elapsed, dest_dir)
        
        print(f"\n{'='*70}")
        print(f"✅ LIGHTNING SORT COMPLETE!")
        print(f"{'='*70}")
        print(f"  Files scanned: {scan_result['total_files']}")
        print(f"  Files sorted: {files_sorted}")
        print(f"  Files failed: {files_failed}")
        print(f"  Time: {elapsed:.2f}s")
        print(f"  ⚡ Speed: {files_sorted/elapsed:.0f} files/sec!")
        print(f"  📁 Destination: {dest_dir}")
        print(f"\n🎵 CURSE_BEAST_02 COMPLETED SORTING! 🎵")
        
        return {
            'files_scanned': scan_result['total_files'],
            'files_sorted': files_sorted,
            'files_failed': files_failed,
            'elapsed_seconds': elapsed,
            'files_per_second': files_sorted/elapsed if elapsed > 0 else 0,
            'destination': dest_dir
        }
    
    def organize_music_library(self, source: str) -> Dict:
        """🎵 Organize complete music library"""
        print(f"\n🎵🎵🎵 ORGANIZING MUSIC LIBRARY! 🎵🎵🎵")
        
        # Multi-level organization
        result = self.lightning_sort(source, organize_by="album")
        
        print(f"\n✅ Music library organized by Artist/Album!")
        
        return result
    
    def deduplicate_files(self, directory: str) -> Dict:
        """⚡ Find and remove duplicate files (by hash)"""
        print(f"\n⚡ DEDUPLICATING: {directory}")
        
        file_hashes = {}
        duplicates = []
        
        for file_path in Path(directory).rglob('*'):
            if file_path.is_file():
                # Calculate hash
                file_hash = self._calculate_hash(file_path)
                
                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                else:
                    file_hashes[file_hash] = file_path
        
        print(f"✅ Found {len(duplicates)} duplicates")
        
        # Remove duplicates
        removed = 0
        for dup_file, original_file in duplicates:
            try:
                dup_file.unlink()
                removed += 1
                print(f"  🗑️  Removed: {dup_file.name}")
            except:
                pass
        
        print(f"✅ Removed {removed} duplicate files")
        
        return {'duplicates_found': len(duplicates), 'removed': removed}
    
    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate file hash"""
        hash_md5 = hashlib.md5()
        
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except:
            return ""
    
    def auto_commit_to_git(self, repo_path: str, message: str = None) -> bool:
        """
        🔥 EATS CODE AND COMMITS TO GIT! 🔥
        
        Args:
            repo_path: Path to git repository
            message: Commit message
        
        Returns:
            Success boolean
        """
        print(f"\n🔥 EATING CODE AND COMMITTING TO GIT!")
        
        repo = Path(repo_path)
        
        if not (repo / ".git").exists():
            print(f"  ⚠️  Not a git repo - initializing...")
            subprocess.run(["git", "init"], cwd=repo, capture_output=True)
        
        # Auto message if not provided
        if message is None:
            message = f"🎵 CURSE_BEAST_02 auto-commit - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        try:
            # Add all files
            subprocess.run(["git", "add", "."], cwd=repo, timeout=30)
            
            # Commit
            result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=repo,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Get commit hash
                hash_result = subprocess.run(
                    ["git", "rev-parse", "HEAD"],
                    cwd=repo,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                commit_hash = hash_result.stdout.strip() if hash_result.returncode == 0 else "unknown"
                
                print(f"  ✅ Committed: {commit_hash[:8]}")
                print(f"  💬 Message: {message}")
                
                # Log commit
                self._log_git_commit(str(repo), commit_hash, message, True)
                
                self.commits_made += 1
                
                # Try to push
                print(f"  🚀 Attempting push...")
                push_result = subprocess.run(
                    ["git", "push"],
                    cwd=repo,
                    capture_output=True,
                    timeout=60
                )
                
                if push_result.returncode == 0:
                    print(f"  ✅ PUSHED TO REMOTE!")
                else:
                    print(f"  ℹ️  Push skipped (no remote or auth needed)")
                
                return True
            else:
                if "nothing to commit" in result.stdout:
                    print(f"  ℹ️  Nothing to commit (already up to date)")
                    return True
                else:
                    print(f"  ❌ Commit failed: {result.stderr}")
                    return False
        
        except Exception as e:
            print(f"  ❌ Git error: {e}")
            return False
    
    def beast_mode_organize(self, source: str, commit: bool = True) -> Dict:
        """
        🦁 BEAST MODE - Full organization with git commit!
        
        DOES EVERYTHING:
        - Scans directory
        - Extracts metadata
        - Sorts files
        - Removes duplicates
        - Commits to git
        - ALL AT LIGHTNING SPEED! ⚡
        """
        print(f"\n{'='*70}")
        print(f"🦁🦁🦁 CURSE_BEAST_02 - FULL BEAST MODE! 🦁🦁🦁")
        print(f"{'='*70}")
        print(f"\n🎵 Source: {source}")
        print(f"🎯 Mode: COMPLETE ORGANIZATION")
        print(f"⚡ Speed: LIGHTNING BOLT!")
        
        total_start = datetime.now()
        
        # Step 1: LIGHTNING SCAN
        print(f"\n1️⃣ LIGHTNING SCAN...")
        scan = self.lightning_scan(source)
        
        # Step 2: DEDUPLICATE
        print(f"\n2️⃣ DEDUPLICATING...")
        dedup = self.deduplicate_files(source)
        
        # Step 3: SORT FILES
        print(f"\n3️⃣ SORTING FILES...")
        sort_result = self.lightning_sort(source, organize_by="album")
        
        # Step 4: COMMIT TO GIT
        if commit and (self.github_root / "noizyfish").exists():
            print(f"\n4️⃣ COMMITTING TO GIT...")
            
            commit_msg = f"🎵 CURSE_BEAST_02: Organized {sort_result['files_sorted']} files"
            self.auto_commit_to_git(str(self.github_root / "noizyfish"), commit_msg)
        
        total_elapsed = (datetime.now() - total_start).total_seconds()
        
        # Final report
        print(f"\n{'='*70}")
        print(f"🎉 BEAST MODE COMPLETE!")
        print(f"{'='*70}")
        print(f"\n📊 Summary:")
        print(f"  Files scanned: {scan['total_files']}")
        print(f"  Files sorted: {sort_result['files_sorted']}")
        print(f"  Duplicates removed: {dedup['removed']}")
        print(f"  Git commits: {self.commits_made}")
        print(f"  Total time: {total_elapsed:.2f}s")
        print(f"  ⚡ Overall speed: {scan['total_files']/total_elapsed:.0f} files/sec!")
        print(f"\n🎵 CURSE_BEAST_02 - MISSION COMPLETE! 🎵")
        
        return {
            'total_files': scan['total_files'],
            'files_sorted': sort_result['files_sorted'],
            'duplicates_removed': dedup['removed'],
            'commits': self.commits_made,
            'total_time': total_elapsed,
            'speed': scan['total_files']/total_elapsed if total_elapsed > 0 else 0
        }
    
    def _log_sorted_file(self, metadata: Dict, destination: str):
        """Log sorted file to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO media_files
            (file_path, file_type, file_size, artist, album, title, genre, 
             year, duration, bitrate, sample_rate, sorted_to, processed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            metadata.get('file_path'),
            metadata.get('file_type'),
            metadata.get('file_size'),
            metadata.get('artist'),
            metadata.get('album'),
            metadata.get('title'),
            metadata.get('genre'),
            metadata.get('year'),
            metadata.get('duration'),
            metadata.get('bitrate'),
            metadata.get('sample_rate'),
            destination,
            datetime.now()
        ))
        
        conn.commit()
        conn.close()
    
    def _log_sorting_operation(self, scanned: int, sorted: int, duration: float, dest: str):
        """Log sorting operation"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO sorting_operations
            (files_scanned, files_sorted, duration_seconds, speed_files_per_sec, destination)
            VALUES (?, ?, ?, ?, ?)
        """, (scanned, sorted, duration, sorted/duration if duration > 0 else 0, dest))
        
        conn.commit()
        conn.close()
    
    def _log_git_commit(self, repo: str, commit_hash: str, message: str, success: bool):
        """Log git commit"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO git_commits
            (repo, commit_hash, message, success)
            VALUES (?, ?, ?, ?)
        """, (repo, commit_hash, message, success))
        
        conn.commit()
        conn.close()


def main():
    """Main entry point for CURSE_BEAST_02"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🎵 CURSE_BEAST_02 - Music/Audio/Video Monster!"
    )
    parser.add_argument("action", choices=["scan", "sort", "organize", "dedupe", "commit", "beast"])
    parser.add_argument("--source", required=True, help="Source directory")
    parser.add_argument("--dest", help="Destination directory")
    parser.add_argument("--organize-by", default="album", choices=["artist", "album", "genre", "type", "year"])
    parser.add_argument("--repo", help="Git repository path")
    parser.add_argument("--message", help="Git commit message")
    
    args = parser.parse_args()
    
    beast = CURSE_BEAST_02()
    
    if args.action == "scan":
        beast.lightning_scan(args.source)
    
    elif args.action == "sort":
        beast.lightning_sort(args.source, args.dest, args.organize_by)
    
    elif args.action == "organize":
        beast.organize_music_library(args.source)
    
    elif args.action == "dedupe":
        beast.deduplicate_files(args.source)
    
    elif args.action == "commit":
        if not args.repo:
            print("❌ Please specify --repo")
        else:
            beast.auto_commit_to_git(args.repo, args.message)
    
    elif args.action == "beast":
        # FULL BEAST MODE!
        beast.beast_mode_organize(args.source, commit=True)


if __name__ == "__main__":
    print(f"\n🎵⚡ CURSE_BEAST_02 - MUSIC/AUDIO/VIDEO MONSTER! ⚡🎵")
    print(f"🔥 SORTS FILES LIKE LIGHTNING BOLTS! 🔥")
    print()
    
    main()

