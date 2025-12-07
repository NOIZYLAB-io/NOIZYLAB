#!/usr/bin/env python3
"""
Intelligent Regrouper - Regroups files based on ALL possible clues:
- ID3 tags (album, artist, publisher, date)
- Filename patterns
- Audio characteristics (sample rate, duration, channels)
- Metadata similarity
- Location data
- Category patterns
"""

import sqlite3
import json
import shutil
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set
import re

class IntelligentRegrouper:
    def __init__(self, db_path=None, sample_master_dir=None):
        self.db_path = Path(db_path) if db_path else Path("/Volumes/4TB_Utility/Waves To Sort/ultra_audio_database.db")
        self.sample_master_dir = Path(sample_master_dir) if sample_master_dir else Path("/Volumes/4TB_Utility/SAMPLE_MASTER")
    
    def get_all_files(self):
        """Get all files from database."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        files = [dict(row) for row in cursor.execute('SELECT * FROM audio_files')]
        conn.close()
        return files
    
    def regroup_by_album(self):
        """Regroup files by album (from ID3 tags)."""
        files = self.get_all_files()
        album_groups = defaultdict(list)
        
        for file_info in files:
            id3_tags = json.loads(file_info.get('id3_tags', '{}') or '{}')
            album = id3_tags.get('TALB') or file_info.get('album')
            if album:
                album_groups[album].append(file_info)
        
        return self._create_regroup_structure(album_groups, 'By_Album')
    
    def regroup_by_artist(self):
        """Regroup files by artist."""
        files = self.get_all_files()
        artist_groups = defaultdict(list)
        
        for file_info in files:
            id3_tags = json.loads(file_info.get('id3_tags', '{}') or '{}')
            artist = id3_tags.get('TPE1') or file_info.get('artist')
            if artist:
                artist_groups[artist].append(file_info)
        
        return self._create_regroup_structure(artist_groups, 'By_Artist')
    
    def regroup_by_publisher(self):
        """Regroup files by publisher."""
        files = self.get_all_files()
        publisher_groups = defaultdict(list)
        
        for file_info in files:
            id3_tags = json.loads(file_info.get('id3_tags', '{}') or '{}')
            publisher = id3_tags.get('TPUB') or file_info.get('publisher')
            if publisher:
                publisher_groups[publisher].append(file_info)
        
        return self._create_regroup_structure(publisher_groups, 'By_Publisher')
    
    def regroup_by_date(self):
        """Regroup files by recording date."""
        files = self.get_all_files()
        date_groups = defaultdict(list)
        
        for file_info in files:
            id3_tags = json.loads(file_info.get('id3_tags', '{}') or '{}')
            date = id3_tags.get('TDRC') or file_info.get('date_recorded')
            if date:
                # Extract year
                year_match = re.search(r'\d{4}', str(date))
                if year_match:
                    year = year_match.group(0)
                    date_groups[year].append(file_info)
        
        return self._create_regroup_structure(date_groups, 'By_Date')
    
    def regroup_by_audio_quality(self):
        """Regroup files by audio quality characteristics."""
        files = self.get_all_files()
        quality_groups = defaultdict(list)
        
        for file_info in files:
            sample_rate = file_info.get('sample_rate', 0) or 0
            bit_depth = file_info.get('bit_depth', 0) or 0
            channels = file_info.get('channels', 0) or 0
            
            quality_key = f"{sample_rate}Hz_{bit_depth}bit_{channels}ch"
            quality_groups[quality_key].append(file_info)
        
        return self._create_regroup_structure(quality_groups, 'By_Quality')
    
    def regroup_by_duration_range(self):
        """Regroup files by duration ranges."""
        files = self.get_all_files()
        duration_groups = defaultdict(list)
        
        for file_info in files:
            duration = file_info.get('duration', 0) or 0
            if duration < 5:
                group = 'Very_Short_0-5s'
            elif duration < 15:
                group = 'Short_5-15s'
            elif duration < 30:
                group = 'Medium_15-30s'
            elif duration < 60:
                group = 'Medium_Long_30-60s'
            elif duration < 180:
                group = 'Long_1-3min'
            else:
                group = 'Very_Long_3min+'
            
            duration_groups[group].append(file_info)
        
        return self._create_regroup_structure(duration_groups, 'By_Duration')
    
    def regroup_by_similarity(self):
        """Regroup files with similar audio fingerprints."""
        files = self.get_all_files()
        fingerprint_groups = defaultdict(list)
        
        for file_info in files:
            fingerprint = file_info.get('audio_fingerprint')
            if fingerprint:
                fingerprint_groups[fingerprint].append(file_info)
        
        # Only return groups with multiple files
        similar_groups = {k: v for k, v in fingerprint_groups.items() if len(v) > 1}
        return self._create_regroup_structure(similar_groups, 'By_Similarity')
    
    def regroup_by_keywords(self):
        """Regroup files by common keywords."""
        files = self.get_all_files()
        keyword_groups = defaultdict(list)
        
        for file_info in files:
            keywords = json.loads(file_info.get('keywords', '[]') or '[]')
            # Group by first significant keyword
            if keywords:
                primary_keyword = keywords[0] if keywords else None
                if primary_keyword and len(primary_keyword) > 3:
                    keyword_groups[primary_keyword].append(file_info)
        
        return self._create_regroup_structure(keyword_groups, 'By_Keywords')
    
    def _create_regroup_structure(self, groups: Dict, base_name: str):
        """Create regrouping structure and return statistics."""
        base_dir = self.sample_master_dir / base_name
        base_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'total_groups': len(groups),
            'total_files': sum(len(files) for files in groups.values()),
            'groups': {}
        }
        
        for group_name, files in groups.items():
            # Sanitize group name
            safe_name = re.sub(r'[<>:"|?*\x00-\x1f]', '_', str(group_name))
            safe_name = safe_name[:100]  # Limit length
            
            group_dir = base_dir / safe_name
            group_dir.mkdir(parents=True, exist_ok=True)
            
            moved = 0
            for file_info in files:
                source_path = Path(file_info.get('organized_path') or file_info.get('original_path'))
                if source_path and source_path.exists():
                    dest_path = group_dir / source_path.name
                    if not dest_path.exists():
                        try:
                            shutil.copy2(str(source_path), str(dest_path))
                            moved += 1
                        except Exception as e:
                            print(f"Error copying {source_path}: {e}")
            
            stats['groups'][group_name] = {
                'files': len(files),
                'moved': moved,
                'path': str(group_dir)
            }
        
        return stats
    
    def regroup_all(self):
        """Perform all regrouping operations."""
        print("=" * 80)
        print("INTELLIGENT REGROUPING - ALL CLUES")
        print("=" * 80)
        
        results = {}
        
        print("\n1. Regrouping by Album...")
        results['by_album'] = self.regroup_by_album()
        print(f"   Created {results['by_album']['total_groups']} album groups")
        
        print("\n2. Regrouping by Artist...")
        results['by_artist'] = self.regroup_by_artist()
        print(f"   Created {results['by_artist']['total_groups']} artist groups")
        
        print("\n3. Regrouping by Publisher...")
        results['by_publisher'] = self.regroup_by_publisher()
        print(f"   Created {results['by_publisher']['total_groups']} publisher groups")
        
        print("\n4. Regrouping by Date...")
        results['by_date'] = self.regroup_by_date()
        print(f"   Created {results['by_date']['total_groups']} date groups")
        
        print("\n5. Regrouping by Audio Quality...")
        results['by_quality'] = self.regroup_by_audio_quality()
        print(f"   Created {results['by_quality']['total_groups']} quality groups")
        
        print("\n6. Regrouping by Duration...")
        results['by_duration'] = self.regroup_by_duration_range()
        print(f"   Created {results['by_duration']['total_groups']} duration groups")
        
        print("\n7. Regrouping by Similarity...")
        results['by_similarity'] = self.regroup_by_similarity()
        print(f"   Created {results['by_similarity']['total_groups']} similarity groups")
        
        print("\n8. Regrouping by Keywords...")
        results['by_keywords'] = self.regroup_by_keywords()
        print(f"   Created {results['by_keywords']['total_groups']} keyword groups")
        
        # Save results
        results_path = Path(self.sample_master_dir.parent) / 'regrouping_results.json'
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\n" + "=" * 80)
        print("REGROUPING COMPLETE")
        print("=" * 80)
        print(f"Results saved to: {results_path}")
        
        return results


def main():
    """Main execution."""
    db_path = "/Volumes/4TB_Utility/Waves To Sort/ultra_audio_database.db"
    sample_master_dir = "/Volumes/4TB_Utility/SAMPLE_MASTER"
    
    regrouper = IntelligentRegrouper(db_path, sample_master_dir)
    regrouper.regroup_all()

if __name__ == '__main__':
    main()

