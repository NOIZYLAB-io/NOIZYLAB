#!/usr/bin/env python3
"""
Music Samples Continuity Scanner
Scans for duplicates, missing files, naming inconsistencies, and organization issues
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

MUSIC_SAMPLES = Path("/Volumes/4TB Big Fish/Music Samples")
REPORT_FILE = Path.home() / "NOIZYLAB" / ".music_samples_continuity_report.json"

# Audio file extensions
AUDIO_EXTS = {'.wav', '.aif', '.aiff', '.mp3', '.flac', '.m4a', '.ogg', 
              '.wma', '.mp4', '.m4v', '.aac', '.alac', '.rex', '.rx2', '.nicnt'}

class MusicContinuityScanner:
    def __init__(self):
        self.samples_dir = MUSIC_SAMPLES
        self.file_hashes = {}
        self.duplicates = []
        self.naming_issues = []
        self.empty_dirs = []
        self.broken_symlinks = []
        self.stats = {
            'total_files': 0,
            'total_dirs': 0,
            'audio_files': 0,
            'categories': defaultdict(int),
            'extensions': defaultdict(int),
            'total_size': 0,
            'bpm_dirs': defaultdict(int),
            'file_patterns': defaultdict(int)
        }
    
    def calculate_file_hash(self, file_path, chunk_size=8192, max_size_mb=100):
        """Calculate MD5 hash for file (skip very large files)"""
        try:
            size_mb = file_path.stat().st_size / (1024 * 1024)
            if size_mb > max_size_mb:
                # For very large files, hash first chunk + size
                md5 = hashlib.md5()
                md5.update(str(file_path.stat().st_size).encode())
                with open(file_path, 'rb') as f:
                    md5.update(f.read(chunk_size))
                return md5.hexdigest()
            
            md5 = hashlib.md5()
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    md5.update(chunk)
            return md5.hexdigest()
        except Exception as e:
            return None
    
    def extract_bpm_from_path(self, path_str):
        """Extract BPM from directory or filename"""
        # Look for BPM patterns like "102BPM", "120BPM", etc.
        import re
        bpm_match = re.search(r'(\d{2,3})\s*BPM', path_str, re.IGNORECASE)
        if bpm_match:
            return int(bpm_match.group(1))
        return None
    
    def scan_directory(self):
        """Scan entire directory structure"""
        print("🔍 Scanning Music Samples directory...")
        print("=" * 80)
        print(f"Directory: {self.samples_dir}")
        print()
        
        if not self.samples_dir.exists():
            print(f"❌ Directory not found: {self.samples_dir}")
            return
        
        # Scan for files and duplicates
        print("📊 Analyzing files...")
        
        processed = 0
        
        for root, dirs, files in os.walk(self.samples_dir):
            # Skip system directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            self.stats['total_dirs'] += 1
            
            # Check for BPM in directory name
            bpm = self.extract_bpm_from_path(root)
            if bpm:
                self.stats['bpm_dirs'][bpm] += 1
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                file_path = Path(root) / file
                processed += 1
                
                if processed % 100 == 0:
                    print(f"   Processed {processed} files...", end='\r')
                
                try:
                    size = file_path.stat().st_size
                    self.stats['total_size'] += size
                    self.stats['total_files'] += 1
                    
                    ext = file_path.suffix.lower()
                    self.stats['extensions'][ext] += 1
                    
                    # Track audio files
                    if ext in AUDIO_EXTS:
                        self.stats['audio_files'] += 1
                        
                        # Check for duplicates by hash (only for reasonable sized files)
                        if size < 100 * 1024 * 1024:  # Skip files > 100MB
                            file_hash = self.calculate_file_hash(file_path)
                            if file_hash:
                                if file_hash in self.file_hashes:
                                    self.duplicates.append({
                                        'original': str(self.file_hashes[file_hash]),
                                        'duplicate': str(file_path),
                                        'size': size
                                    })
                                else:
                                    self.file_hashes[file_hash] = str(file_path)
                        
                        # Check naming consistency
                        self.check_naming(file_path)
                        
                        # Track file patterns
                        self.track_patterns(file_path)
                    
                    # Track by category
                    rel_path = Path(root).relative_to(self.samples_dir)
                    category = rel_path.parts[0] if rel_path.parts else "root"
                    self.stats['categories'][category] += 1
                
                except Exception as e:
                    pass
            
            # Check for empty directories (no files, no non-empty subdirs)
            has_files = any(not f.startswith('.') for f in files)
            has_subdirs = any(Path(root) / d for d in dirs if not d.startswith('.'))
            
            if not has_files and not has_subdirs:
                rel_dir = Path(root).relative_to(self.samples_dir)
                if rel_dir.parts:  # Don't count root
                    self.empty_dirs.append(str(rel_dir))
        
        # Find broken symlinks
        self.find_broken_symlinks()
        
        print(f"\n✅ Scanned {self.stats['total_files']} files in {self.stats['total_dirs']} directories")
    
    def check_naming(self, file_path):
        """Check for naming inconsistencies"""
        name = file_path.stem
        issues = []
        
        # Check for common issues
        if '  ' in name:  # Double spaces
            issues.append("Double spaces")
        
        if name.startswith(' ') or name.endswith(' '):  # Leading/trailing spaces
            issues.append("Leading/trailing spaces")
        
        if not any(char.isalnum() for char in name):  # No alphanumeric
            issues.append("No alphanumeric characters")
        
        # Check for inconsistent naming patterns
        if name.lower() != name and name.upper() != name:
            # Mixed case - check if it's intentional
            pass
        
        if issues:
            self.naming_issues.append({
                'file': str(file_path.relative_to(self.samples_dir)),
                'issues': issues
            })
    
    def track_patterns(self, file_path):
        """Track file naming patterns"""
        name = file_path.name.lower()
        
        # Track common patterns
        if '_' in name:
            parts = name.split('_')
            if len(parts) > 2:
                pattern = f"{parts[0]}_{parts[1]}"
                self.stats['file_patterns'][pattern] += 1
    
    def find_broken_symlinks(self):
        """Find broken symbolic links"""
        for root, dirs, files in os.walk(self.samples_dir):
            for item in dirs + files:
                item_path = Path(root) / item
                try:
                    if item_path.is_symlink() and not item_path.exists():
                        rel_path = item_path.relative_to(self.samples_dir)
                        self.broken_symlinks.append(str(rel_path))
                except:
                    pass
    
    def generate_report(self):
        """Generate continuity report"""
        print("\n" + "=" * 80)
        print("📊 CONTINUITY REPORT")
        print("=" * 80)
        
        # Overall stats
        print(f"\n📁 Overall Statistics:")
        print(f"   Total files: {self.stats['total_files']:,}")
        print(f"   Audio files: {self.stats['audio_files']:,}")
        print(f"   Directories: {self.stats['total_dirs']:,}")
        size_gb = self.stats['total_size'] / (1024**3)
        print(f"   Total size: {size_gb:.2f} GB")
        
        # Categories
        print(f"\n📂 Categories:")
        for category, count in sorted(self.stats['categories'].items(), key=lambda x: x[1], reverse=True):
            print(f"   • {category:50s} - {count:6,} files")
        
        # BPM directories
        if self.stats['bpm_dirs']:
            print(f"\n🎵 BPM Organization:")
            for bpm, count in sorted(self.stats['bpm_dirs'].items()):
                print(f"   • {bpm:3d} BPM - {count:3d} directories")
        
        # File types
        print(f"\n📄 File Types:")
        for ext, count in sorted(self.stats['extensions'].items(), key=lambda x: x[1], reverse=True)[:10]:
            ext_name = ext if ext else "(no extension)"
            print(f"   • {ext_name:10s} - {count:6,} files")
        
        # Duplicates
        print(f"\n🔄 Duplicate Files:")
        if self.duplicates:
            print(f"   ⚠️  Found {len(self.duplicates)} duplicate files")
            
            total_duplicate_size = sum(d['size'] for d in self.duplicates)
            duplicate_size_gb = total_duplicate_size / (1024**3)
            
            print(f"   📦 Duplicate size: {duplicate_size_gb:.2f} GB")
            print(f"\n   First 10 duplicates:")
            for i, dup in enumerate(self.duplicates[:10], 1):
                size_mb = dup['size'] / (1024 * 1024)
                rel_orig = Path(dup['original']).relative_to(self.samples_dir)
                rel_dup = Path(dup['duplicate']).relative_to(self.samples_dir)
                print(f"   {i:2}. {size_mb:8.1f} MB")
                print(f"       Original:   {rel_orig}")
                print(f"       Duplicate:  {rel_dup}")
        else:
            print("   ✅ No duplicates found!")
        
        # Naming issues
        print(f"\n📝 Naming Issues:")
        if self.naming_issues:
            print(f"   ⚠️  Found {len(self.naming_issues)} files with naming issues")
            for issue in self.naming_issues[:10]:
                print(f"   • {issue['file']}")
                print(f"     Issues: {', '.join(issue['issues'])}")
            if len(self.naming_issues) > 10:
                print(f"   ... and {len(self.naming_issues) - 10} more")
        else:
            print("   ✅ No naming issues found!")
        
        # Empty directories
        print(f"\n📁 Empty Directories:")
        if self.empty_dirs:
            print(f"   ⚠️  Found {len(self.empty_dirs)} empty directories:")
            for empty_dir in self.empty_dirs[:10]:
                print(f"   • {empty_dir}")
            if len(self.empty_dirs) > 10:
                print(f"   ... and {len(self.empty_dirs) - 10} more")
        else:
            print("   ✅ No empty directories found!")
        
        # Broken symlinks
        if self.broken_symlinks:
            print(f"\n🔗 Broken Symlinks:")
            print(f"   ⚠️  Found {len(self.broken_symlinks)} broken symlinks:")
            for symlink in self.broken_symlinks[:10]:
                print(f"   • {symlink}")
            if len(self.broken_symlinks) > 10:
                print(f"   ... and {len(self.broken_symlinks) - 10} more")
        
        # Continuity assessment
        print("\n" + "=" * 80)
        print("✅ CONTINUITY ASSESSMENT")
        print("=" * 80)
        
        issues_count = (
            len(self.duplicates) + 
            len(self.naming_issues) + 
            len(self.empty_dirs) + 
            len(self.broken_symlinks)
        )
        
        if issues_count == 0:
            print("   ✅ EXCELLENT - No continuity issues found!")
            print("   Collection is well-organized and consistent.")
        elif issues_count < 10:
            print(f"   ✅ GOOD - Only {issues_count} minor issues found")
            print("   Collection is generally well-organized.")
        elif issues_count < 50:
            print(f"   ⚠️  FAIR - {issues_count} issues found")
            print("   Some cleanup recommended.")
        else:
            print(f"   ⚠️  NEEDS ATTENTION - {issues_count} issues found")
            print("   Cleanup recommended.")
        
        # Save report
        report = {
            'timestamp': datetime.now().isoformat(),
            'directory': str(self.samples_dir),
            'statistics': {k: dict(v) if isinstance(v, defaultdict) else v 
                          for k, v in self.stats.items()},
            'duplicates': self.duplicates,
            'naming_issues': self.naming_issues,
            'empty_dirs': self.empty_dirs,
            'broken_symlinks': self.broken_symlinks,
            'continuity_score': 100 - min(issues_count * 2, 100)
        }
        
        REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(REPORT_FILE, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Report saved: {REPORT_FILE}")
        
        # Recommendations
        print("\n" + "=" * 80)
        print("💡 RECOMMENDATIONS")
        print("=" * 80)
        
        recommendations = []
        
        if self.duplicates:
            duplicate_size_gb = sum(d['size'] for d in self.duplicates) / (1024**3)
            recommendations.append(
                f"• Remove {len(self.duplicates)} duplicate files "
                f"(would free up {duplicate_size_gb:.2f} GB)"
            )
        
        if self.naming_issues:
            recommendations.append(
                f"• Fix naming issues in {len(self.naming_issues)} files "
                "(remove double spaces, trailing spaces, etc.)"
            )
        
        if self.empty_dirs:
            recommendations.append(
                f"• Clean up {len(self.empty_dirs)} empty directories"
            )
        
        if self.broken_symlinks:
            recommendations.append(
                f"• Fix or remove {len(self.broken_symlinks)} broken symlinks"
            )
        
        if recommendations:
            for rec in recommendations:
                print(f"   {rec}")
        else:
            print("   ✅ Collection is in excellent condition!")
        
        print()

def main():
    print("=" * 80)
    print(" " * 15 + "MUSIC SAMPLES CONTINUITY SCANNER")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    scanner = MusicContinuityScanner()
    scanner.scan_directory()
    scanner.generate_report()
    
    print("=" * 80)
    print("✅ Continuity scan complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()

