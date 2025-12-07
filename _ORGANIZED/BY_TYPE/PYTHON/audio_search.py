#!/usr/bin/env python3
"""
Advanced Audio File Search Tool
Fast search using SQLite database with fuzzy matching and advanced filters.
"""

import sqlite3
import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional

class AudioSearch:
    def __init__(self, db_path=None):
        self.db_path = Path(db_path) if db_path else Path("/Volumes/4TB_Utility/Waves To Sort/audio_database.db")
    
    def search(self, query=None, category=None, location=None, file_type=None, 
               min_duration=None, max_duration=None, min_sample_rate=None,
               min_file_size=None, max_file_size=None, limit=100):
        """Search audio files with multiple criteria."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        conditions = []
        params = []
        
        if query:
            conditions.append('''
                (filename LIKE ? OR description LIKE ? OR tags LIKE ? OR keywords LIKE ?)
            ''')
            search_term = f'%{query}%'
            params.extend([search_term, search_term, search_term, search_term])
        
        if category:
            conditions.append('category = ?')
            params.append(category)
        
        if location:
            conditions.append('location = ?')
            params.append(location)
        
        if file_type:
            conditions.append('type = ?')
            params.append(file_type)
        
        if min_duration:
            conditions.append('duration >= ?')
            params.append(min_duration)
        
        if max_duration:
            conditions.append('duration <= ?')
            params.append(max_duration)
        
        if min_sample_rate:
            conditions.append('sample_rate >= ?')
            params.append(min_sample_rate)
        
        if min_file_size:
            conditions.append('file_size >= ?')
            params.append(min_file_size)
        
        if max_file_size:
            conditions.append('file_size <= ?')
            params.append(max_file_size)
        
        where_clause = ' AND '.join(conditions) if conditions else '1=1'
        
        sql = f'''
            SELECT * FROM audio_files 
            WHERE {where_clause}
            ORDER BY filename
            LIMIT ?
        '''
        params.append(limit)
        
        results = [dict(row) for row in cursor.execute(sql, params)]
        conn.close()
        
        return results
    
    def get_statistics(self):
        """Get search statistics."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {
            'total_files': cursor.execute('SELECT COUNT(*) FROM audio_files').fetchone()[0],
            'total_size': cursor.execute('SELECT SUM(file_size) FROM audio_files').fetchone()[0] or 0,
            'total_duration': cursor.execute('SELECT SUM(duration) FROM audio_files').fetchone()[0] or 0,
            'categories': {},
            'locations': {},
            'types': {},
            'sample_rates': {},
            'avg_file_size': 0,
            'avg_duration': 0
        }
        
        # Category distribution
        for row in cursor.execute('SELECT category, COUNT(*) as count FROM audio_files WHERE category IS NOT NULL GROUP BY category'):
            stats['categories'][row[0]] = row[1]
        
        # Location distribution
        for row in cursor.execute('SELECT location, COUNT(*) as count FROM audio_files WHERE location IS NOT NULL GROUP BY location'):
            stats['locations'][row[0]] = row[1]
        
        # Type distribution
        for row in cursor.execute('SELECT type, COUNT(*) as count FROM audio_files WHERE type IS NOT NULL GROUP BY type'):
            stats['types'][row[0]] = row[1]
        
        # Sample rate distribution
        for row in cursor.execute('SELECT sample_rate, COUNT(*) as count FROM audio_files WHERE sample_rate IS NOT NULL GROUP BY sample_rate'):
            stats['sample_rates'][row[0]] = row[1]
        
        if stats['total_files'] > 0:
            stats['avg_file_size'] = stats['total_size'] / stats['total_files']
            stats['avg_duration'] = stats['total_duration'] / stats['total_files']
        
        conn.close()
        return stats
    
    def export_results(self, results, format='json', output_file=None):
        """Export search results to file."""
        if format == 'json':
            output = json.dumps(results, indent=2, ensure_ascii=False)
        elif format == 'csv':
            import csv
            from io import StringIO
            output = StringIO()
            if results:
                writer = csv.DictWriter(output, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
                output = output.getvalue()
            else:
                output = ''
        else:
            output = '\n'.join([f"{r['filename']} - {r.get('description', '')}" for r in results])
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Exported {len(results)} results to {output_file}")
        else:
            print(output)
        
        return output


def main():
    parser = argparse.ArgumentParser(description='Search audio files')
    parser.add_argument('query', nargs='?', help='Search query')
    parser.add_argument('--category', help='Filter by category')
    parser.add_argument('--location', help='Filter by location')
    parser.add_argument('--type', help='Filter by type (Indoor/Outdoor)')
    parser.add_argument('--min-duration', type=float, help='Minimum duration in seconds')
    parser.add_argument('--max-duration', type=float, help='Maximum duration in seconds')
    parser.add_argument('--min-sample-rate', type=int, help='Minimum sample rate')
    parser.add_argument('--min-size', type=int, help='Minimum file size in bytes')
    parser.add_argument('--max-size', type=int, help='Maximum file size in bytes')
    parser.add_argument('--limit', type=int, default=100, help='Maximum results')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    parser.add_argument('--export', help='Export results to file')
    parser.add_argument('--format', choices=['json', 'csv', 'text'], default='text', help='Export format')
    
    args = parser.parse_args()
    
    search = AudioSearch()
    
    if args.stats:
        stats = search.get_statistics()
        print(json.dumps(stats, indent=2))
    else:
        results = search.search(
            query=args.query,
            category=args.category,
            location=args.location,
            file_type=args.type,
            min_duration=args.min_duration,
            max_duration=args.max_duration,
            min_sample_rate=args.min_sample_rate,
            min_file_size=args.min_size,
            max_file_size=args.max_size,
            limit=args.limit
        )
        
        print(f"Found {len(results)} results\n")
        
        for result in results:
            print(f"File: {result['filename']}")
            if result.get('description'):
                print(f"  Description: {result['description']}")
            if result.get('category'):
                print(f"  Category: {result['category']}")
            if result.get('location'):
                print(f"  Location: {result['location']}")
            if result.get('duration'):
                print(f"  Duration: {result['duration']:.2f}s")
            if result.get('sample_rate'):
                print(f"  Sample Rate: {result['sample_rate']}Hz")
            print()
        
        if args.export:
            search.export_results(results, format=args.format, output_file=args.export)

if __name__ == '__main__':
    main()

