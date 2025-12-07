#!/usr/bin/env python3
"""
Advanced Tag Editor for batch editing ID3 tags in audio files.
Supports bulk operations, tag validation, and preview before applying.
"""

import os
import json
import sqlite3
from pathlib import Path
from typing import List, Dict, Optional
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TCON, TPE1, TALB, TDRC, TXXX

class TagEditor:
    def __init__(self, db_path=None, sample_master_dir=None):
        self.db_path = Path(db_path) if db_path else Path("/Volumes/4TB_Utility/Waves To Sort/audio_database.db")
        self.sample_master_dir = Path(sample_master_dir) if sample_master_dir else Path("/Volumes/4TB_Utility/SAMPLE_MASTER")
    
    def get_files_by_criteria(self, category=None, location=None, file_type=None, limit=None):
        """Get files from database matching criteria."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        conditions = []
        params = []
        
        if category:
            conditions.append('category = ?')
            params.append(category)
        if location:
            conditions.append('location = ?')
            params.append(location)
        if file_type:
            conditions.append('type = ?')
            params.append(file_type)
        
        where = ' AND '.join(conditions) if conditions else '1=1'
        sql = f'SELECT * FROM audio_files WHERE {where}'
        
        if limit:
            sql += f' LIMIT {limit}'
        
        results = [dict(row) for row in cursor.execute(sql, params)]
        conn.close()
        
        return results
    
    def read_tags(self, filepath):
        """Read all tags from a file."""
        tags = {}
        try:
            audio = WAVE(str(filepath))
            try:
                id3 = ID3(str(filepath))
                for frame_id, frame in id3.items():
                    if hasattr(frame, 'text'):
                        if isinstance(frame.text, list):
                            tags[str(frame_id)] = frame.text[0] if frame.text else ''
                        else:
                            tags[str(frame_id)] = str(frame.text)
                    else:
                        tags[str(frame_id)] = str(frame)
            except ID3NoHeaderError:
                pass
        except Exception as e:
            return {'error': str(e)}
        
        return tags
    
    def write_tags(self, filepath, tags: Dict[str, str], dry_run=False):
        """Write tags to a file."""
        if dry_run:
            return {'status': 'preview', 'file': str(filepath), 'tags': tags}
        
        try:
            audio = WAVE(str(filepath))
            try:
                id3 = ID3(str(filepath))
            except ID3NoHeaderError:
                audio.add_tags()
                id3 = ID3(str(filepath))
            
            # Map tag names to ID3 frames
            tag_mapping = {
                'TIT2': TIT2,
                'TCON': TCON,
                'TPE1': TPE1,
                'TALB': TALB,
                'TDRC': TDRC
            }
            
            for tag_name, tag_value in tags.items():
                if tag_name in tag_mapping:
                    id3[tag_name] = tag_mapping[tag_name](encoding=3, text=[tag_value])
                elif tag_name.startswith('TXXX:'):
                    desc = tag_name.split(':', 1)[1]
                    id3[tag_name] = TXXX(encoding=3, desc=desc, text=[tag_value])
            
            id3.save()
            return {'status': 'success', 'file': str(filepath)}
        except Exception as e:
            return {'status': 'error', 'file': str(filepath), 'error': str(e)}
    
    def batch_update_tags(self, file_list: List[str], tags: Dict[str, str], dry_run=True):
        """Batch update tags for multiple files."""
        results = []
        for filepath in file_list:
            result = self.write_tags(filepath, tags, dry_run=dry_run)
            results.append(result)
        return results
    
    def update_category_batch(self, old_category, new_category, dry_run=True):
        """Update category for all files with a specific category."""
        files = self.get_files_by_criteria(category=old_category)
        results = []
        
        for file_info in files:
            filepath = file_info.get('organized_path') or file_info.get('original_path')
            if filepath and os.path.exists(filepath):
                result = self.write_tags(filepath, {'TCON': new_category}, dry_run=dry_run)
                results.append(result)
        
        return results
    
    def add_location_to_files(self, location, category=None, dry_run=True):
        """Add location tag to files matching criteria."""
        files = self.get_files_by_criteria(category=category)
        results = []
        
        for file_info in files:
            filepath = file_info.get('organized_path') or file_info.get('original_path')
            if filepath and os.path.exists(filepath):
                result = self.write_tags(filepath, {'TXXX:Location': location}, dry_run=dry_run)
                results.append(result)
        
        return results
    
    def validate_tags(self, filepath):
        """Validate tags in a file."""
        tags = self.read_tags(filepath)
        issues = []
        
        if 'TIT2' not in tags:
            issues.append('Missing title (TIT2)')
        if 'TCON' not in tags:
            issues.append('Missing category/genre (TCON)')
        
        return {
            'file': str(filepath),
            'tags': tags,
            'issues': issues,
            'valid': len(issues) == 0
        }


def main():
    """CLI interface for tag editor."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Edit ID3 tags in audio files')
    parser.add_argument('--file', help='Single file to edit')
    parser.add_argument('--category', help='Filter by category')
    parser.add_argument('--location', help='Filter by location')
    parser.add_argument('--set-title', help='Set title tag')
    parser.add_argument('--set-category', help='Set category tag')
    parser.add_argument('--set-location', help='Set location tag')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    parser.add_argument('--validate', action='store_true', help='Validate tags')
    
    args = parser.parse_args()
    
    editor = TagEditor()
    
    if args.validate:
        if args.file:
            result = editor.validate_tags(args.file)
            print(json.dumps(result, indent=2))
        else:
            print("--file required for validation")
    
    elif args.file:
        if args.set_title or args.set_category or args.set_location:
            tags = {}
            if args.set_title:
                tags['TIT2'] = args.set_title
            if args.set_category:
                tags['TCON'] = args.set_category
            if args.set_location:
                tags['TXXX:Location'] = args.set_location
            
            result = editor.write_tags(args.file, tags, dry_run=args.dry_run)
            print(json.dumps(result, indent=2))
        else:
            tags = editor.read_tags(args.file)
            print(json.dumps(tags, indent=2))
    
    elif args.category or args.location:
        files = editor.get_files_by_criteria(category=args.category, location=args.location)
        print(f"Found {len(files)} files")
        
        if args.set_category or args.set_location:
            tags = {}
            if args.set_category:
                tags['TCON'] = args.set_category
            if args.set_location:
                tags['TXXX:Location'] = args.set_location
            
            filepaths = [f.get('organized_path') or f.get('original_path') for f in files]
            results = editor.batch_update_tags(filepaths, tags, dry_run=args.dry_run)
            print(f"Updated {len([r for r in results if r['status'] == 'success'])} files")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

