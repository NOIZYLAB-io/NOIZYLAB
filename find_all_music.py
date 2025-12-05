#!/usr/bin/env python3
"""
FISH MUSIC INC - COMPLETE MUSIC ARCHIVE FINDER
Find ROB's ENTIRE 40 YEARS of creative work across all volumes
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import hashlib

class CompleteMusicFinder:
    """Find and catalog ROB's complete music archive"""
    
    def __init__(self):
        self.volumes_path = Path('/Volumes')
        self.output_dir = Path('/Users/m2ultra/CB-01-FISHMUSICINC/music')
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Client/project keywords to search for
        self.client_keywords = [
            'FUEL', 'fuel',
            'McDonald', 'McDonalds',
            'Microsoft', 'Tinker',
            'Deadwood', 'deadwood',
            'Design', 'design', 'Design 2025', 'Design Reunion'
        ]
        
        # Music file extensions
        self.audio_extensions = [
            '.wav', '.aif', '.aiff', '.mp3', '.m4a',
            '.flac', '.ogg', '.aac', '.wma'
        ]
        
        # Session file extensions
        self.session_extensions = [
            '.ptx', '.ptf',  # Pro Tools
            '.logic',        # Logic Pro
            '.als',          # Ableton
            '.flp',          # FL Studio
            '.rpp'           # Reaper
        ]
        
        self.results = {
            'scan_date': datetime.now().isoformat(),
            'volumes': {},
            'client_projects': {},
            'originals': [],
            'library_samples': [],
            'summary': {}
        }
    
    def get_all_volumes(self) -> List[Path]:
        """Get all mounted volumes"""
        if not self.volumes_path.exists():
            return []
        
        volumes = []
        for item in self.volumes_path.iterdir():
            if item.is_dir() and not item.is_symlink():
                # Skip system volumes
                if item.name not in ['M2Ultra', 'Macintosh HD']:
                    volumes.append(item)
        return volumes
    
    def get_volume_info(self, volume: Path) -> Dict:
        """Get volume size and usage info"""
        try:
            result = subprocess.run(
                ['df', '-h', str(volume)],
                capture_output=True,
                text=True
            )
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 2:
                parts = lines[1].split()
                if len(parts) >= 5:
                    return {
                        'name': volume.name,
                        'path': str(volume),
                        'size': parts[1],
                        'used': parts[2],
                        'available': parts[3],
                        'use_percent': parts[4],
                        'accessible': True
                    }
        except Exception as e:
            return {
                'name': volume.name,
                'path': str(volume),
                'error': str(e),
                'accessible': False
            }
        return {'name': volume.name, 'path': str(volume), 'accessible': False}
    
    def check_audio_metadata(self, file_path: Path) -> Dict:
        """Check if audio file has metadata (library) or not (original)"""
        try:
            # Use mdls on macOS to check for metadata
            result = subprocess.run(
                ['mdls', '-name', 'kMDItemAuthors', '-name', 'kMDItemComment', 
                 '-name', 'kMDItemAlbum', str(file_path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # If all values are (null), likely an original
            has_metadata = 'null' not in result.stdout.lower()
            
            return {
                'has_metadata': has_metadata,
                'type': 'library_sample' if has_metadata else 'original'
            }
        except:
            return {'has_metadata': False, 'type': 'unknown'}
    
    def find_client_projects(self, volume: Path, max_depth: int = 4) -> List[Dict]:
        """Find client project directories"""
        projects = []
        
        try:
            for root, dirs, files in os.walk(volume, topdown=True):
                # Limit depth
                depth = str(root)[len(str(volume)):].count(os.sep)
                if depth > max_depth:
                    dirs[:] = []
                    continue
                
                # Check if directory name matches client keywords
                dir_name = os.path.basename(root)
                for keyword in self.client_keywords:
                    if keyword.lower() in dir_name.lower():
                        try:
                            size = subprocess.run(
                                ['du', '-sh', root],
                                capture_output=True,
                                text=True,
                                timeout=30
                            )
                            size_str = size.stdout.split()[0] if size.returncode == 0 else 'Unknown'
                        except:
                            size_str = 'Unknown'
                        
                        projects.append({
                            'name': dir_name,
                            'path': root,
                            'keyword_match': keyword,
                            'size': size_str,
                            'volume': volume.name
                        })
                        break  # Don't match multiple keywords for same dir
                
        except PermissionError:
            pass
        except Exception as e:
            print(f"  ⚠️  Error scanning {volume.name}: {e}")
        
        return projects
    
    def count_audio_files(self, volume: Path, sample_size: int = 100) -> Dict:
        """Count audio files and sample for metadata"""
        counts = {
            'wav': 0, 'aif': 0, 'mp3': 0, 'm4a': 0, 'flac': 0,
            'other': 0, 'sessions': 0
        }
        
        originals_count = 0
        library_count = 0
        sampled = 0
        
        try:
            for root, dirs, files in os.walk(volume, topdown=True):
                # Skip system directories
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                for file in files:
                    file_lower = file.lower()
                    
                    # Count audio files
                    if file_lower.endswith('.wav'):
                        counts['wav'] += 1
                    elif file_lower.endswith(('.aif', '.aiff')):
                        counts['aif'] += 1
                    elif file_lower.endswith('.mp3'):
                        counts['mp3'] += 1
                    elif file_lower.endswith('.m4a'):
                        counts['m4a'] += 1
                    elif file_lower.endswith('.flac'):
                        counts['flac'] += 1
                    elif any(file_lower.endswith(ext) for ext in self.audio_extensions):
                        counts['other'] += 1
                    
                    # Count session files
                    if any(file_lower.endswith(ext) for ext in self.session_extensions):
                        counts['sessions'] += 1
                    
                    # Sample WAV files for metadata check
                    if file_lower.endswith('.wav') and sampled < sample_size:
                        file_path = Path(root) / file
                        metadata_info = self.check_audio_metadata(file_path)
                        if metadata_info['type'] == 'original':
                            originals_count += 1
                        elif metadata_info['type'] == 'library_sample':
                            library_count += 1
                        sampled += 1
        
        except PermissionError:
            pass
        except Exception as e:
            print(f"  ⚠️  Error counting files on {volume.name}: {e}")
        
        total_audio = sum([counts['wav'], counts['aif'], counts['mp3'], 
                          counts['m4a'], counts['flac'], counts['other']])
        
        return {
            'counts': counts,
            'total_audio': total_audio,
            'total_sessions': counts['sessions'],
            'sample_analysis': {
                'sampled': sampled,
                'originals_detected': originals_count,
                'library_detected': library_count,
                'original_percentage': round(originals_count / sampled * 100) if sampled > 0 else 0
            }
        }
    
    def scan_volume(self, volume: Path) -> Dict:
        """Complete scan of a single volume"""
        print(f"\n📀 Scanning: {volume.name}")
        print("=" * 60)
        
        volume_info = self.get_volume_info(volume)
        
        if not volume_info.get('accessible', False):
            print(f"  ⚠️  Volume not accessible")
            return volume_info
        
        print(f"  Size: {volume_info.get('size', 'Unknown')}")
        print(f"  Used: {volume_info.get('used', 'Unknown')} ({volume_info.get('use_percent', '?')})")
        
        # Find client projects
        print(f"  🔍 Looking for client projects...")
        projects = self.find_client_projects(volume)
        if projects:
            print(f"  ✅ Found {len(projects)} client project(s)!")
            for proj in projects[:5]:  # Show first 5
                print(f"     • {proj['name']} ({proj['size']})")
        else:
            print(f"  ℹ️  No client projects found")
        
        # Count audio files
        print(f"  🎵 Counting audio files...")
        audio_stats = self.count_audio_files(volume)
        print(f"  ✅ Found {audio_stats['total_audio']:,} audio files")
        if audio_stats['counts']['wav'] > 0:
            print(f"     WAV: {audio_stats['counts']['wav']:,}")
        if audio_stats['counts']['aif'] > 0:
            print(f"     AIF: {audio_stats['counts']['aif']:,}")
        if audio_stats['counts']['mp3'] > 0:
            print(f"     MP3: {audio_stats['counts']['mp3']:,}")
        if audio_stats['total_sessions'] > 0:
            print(f"  📁 Sessions: {audio_stats['total_sessions']:,}")
        
        # Show original vs library estimate
        if audio_stats['sample_analysis']['sampled'] > 0:
            orig_pct = audio_stats['sample_analysis']['original_percentage']
            print(f"  💎 Estimated originals: ~{orig_pct}% (sampled {audio_stats['sample_analysis']['sampled']} files)")
        
        volume_info['client_projects'] = projects
        volume_info['audio_stats'] = audio_stats
        
        return volume_info
    
    def scan_all_volumes(self):
        """Scan all mounted volumes"""
        print("\n🔥 FISH MUSIC INC - COMPLETE ARCHIVE SCANNER")
        print("=" * 60)
        print("Finding ROB's ENTIRE 40 YEARS of creative work!")
        print("=" * 60)
        
        volumes = self.get_all_volumes()
        print(f"\n✅ Found {len(volumes)} volume(s) to scan\n")
        
        for volume in volumes:
            volume_result = self.scan_volume(volume)
            self.results['volumes'][volume.name] = volume_result
            
            # Aggregate client projects
            if 'client_projects' in volume_result:
                for proj in volume_result['client_projects']:
                    keyword = proj['keyword_match']
                    if keyword not in self.results['client_projects']:
                        self.results['client_projects'][keyword] = []
                    self.results['client_projects'][keyword].append(proj)
        
        self.generate_summary()
        self.save_results()
    
    def generate_summary(self):
        """Generate summary statistics"""
        total_audio = 0
        total_sessions = 0
        total_projects = 0
        
        for vol_name, vol_data in self.results['volumes'].items():
            if 'audio_stats' in vol_data:
                total_audio += vol_data['audio_stats']['total_audio']
                total_sessions += vol_data['audio_stats']['total_sessions']
            if 'client_projects' in vol_data:
                total_projects += len(vol_data['client_projects'])
        
        self.results['summary'] = {
            'total_volumes': len(self.results['volumes']),
            'total_audio_files': total_audio,
            'total_sessions': total_sessions,
            'total_client_projects': total_projects,
            'client_types_found': len(self.results['client_projects'])
        }
    
    def save_results(self):
        """Save results to JSON"""
        output_file = self.output_dir / f"complete_archive_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")
        self.print_summary()
    
    def print_summary(self):
        """Print summary report"""
        summary = self.results['summary']
        
        print("\n")
        print("=" * 60)
        print("📊 SCAN COMPLETE - SUMMARY REPORT")
        print("=" * 60)
        print(f"\n📀 Total Volumes Scanned: {summary['total_volumes']}")
        print(f"🎵 Total Audio Files: {summary['total_audio_files']:,}")
        print(f"📁 Total Sessions: {summary['total_sessions']:,}")
        print(f"🏢 Total Client Projects: {summary['total_client_projects']}")
        
        if self.results['client_projects']:
            print(f"\n🔥 CLIENT WORK FOUND:")
            for client, projects in self.results['client_projects'].items():
                print(f"   • {client}: {len(projects)} project(s)")
                for proj in projects[:3]:  # Show first 3
                    print(f"      - {proj['name']} ({proj['size']}) on {proj['volume']}")
        
        print("\n" + "=" * 60)
        print("🎸 ROB'S 40-YEAR CREATIVE ARCHIVE - CATALOGED!")
        print("=" * 60)
        print("\nGORUNFREE! 🔥\n")

def main():
    """Main execution"""
    finder = CompleteMusicFinder()
    finder.scan_all_volumes()

if __name__ == '__main__':
    main()

