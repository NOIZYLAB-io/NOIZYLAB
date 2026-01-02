#!/usr/bin/env python3
"""
🔍 Simple Master Search - NoizyFish Edition
Fast file search across your entire workspace
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import argparse

class SimpleSearch:
    def __init__(self):
        self.workspace = Path("/Users/rsp_ms/NoizyFish_Aquarium")
        self.file_types = {
            'audio': ['.wav', '.mp3', '.m4a', '.flac', '.aif', '.aiff'],
            'code': ['.py', '.js', '.ts', '.html', '.css', '.json', '.md'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.txt', '.md', '.pdf', '.doc', '.docx'],
            'data': ['.csv', '.json', '.xml', '.yaml', '.yml']
        }
    
    def search_files(self, query: str, category: str = 'all') -> List[Dict]:
        """Search for files matching the query"""
        results = []
        
        # Determine which extensions to search
        if category == 'all':
            extensions = []
            for ext_list in self.file_types.values():
                extensions.extend(ext_list)
        elif category in self.file_types:
            extensions = self.file_types[category]
        else:
            extensions = []
        
        print(f"🔍 Searching for '{query}' in {self.workspace}")
        if extensions:
            print(f"📁 Looking for: {', '.join(extensions)}")
        
        # Search through files
        found_count = 0
        for file_path in self.workspace.rglob("*"):
            if file_path.is_file():
                # Skip if extension doesn't match
                if extensions and file_path.suffix.lower() not in extensions:
                    continue
                
                # Check if query matches filename
                if query.lower() in file_path.name.lower():
                    try:
                        file_info = {
                            'name': file_path.name,
                            'path': str(file_path),
                            'size': file_path.stat().st_size,
                            'type': self._get_file_type(file_path),
                            'modified': datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                        }
                        results.append(file_info)
                        found_count += 1
                        
                        # Show progress for large searches
                        if found_count % 10 == 0:
                            print(f"  📄 Found {found_count} matches...")
                            
                    except (OSError, PermissionError):
                        continue
                
                # Limit results to prevent overwhelming output
                if found_count >= 100:
                    print(f"  ⚠️  Limited to first 100 results")
                    break
        
        # Sort by relevance (exact matches first, then by modification date)
        results.sort(key=lambda x: (
            query.lower() != x['name'].lower(),  # Exact matches first
            -os.path.getmtime(x['path'])  # Then by newest first
        ))
        
        return results
    
    def _get_file_type(self, file_path: Path) -> str:
        """Get the category of a file"""
        ext = file_path.suffix.lower()
        for category, extensions in self.file_types.items():
            if ext in extensions:
                return category
        return 'other'
    
    def format_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"

def main():
    parser = argparse.ArgumentParser(description="🔍 Simple Master Search")
    parser.add_argument("query", help="Search term")
    parser.add_argument("--category", choices=['all', 'audio', 'code', 'images', 'documents', 'data'], 
                       default='all', help="File category to search")
    parser.add_argument("--save", action="store_true", help="Save results to JSON file")
    
    args = parser.parse_args()
    
    search = SimpleSearch()
    
    print(f"🔍 NoizyFish Master Search")
    print(f"{'='*60}")
    
    # Perform search
    start_time = datetime.now()
    results = search.search_files(args.query, args.category)
    search_time = (datetime.now() - start_time).total_seconds()
    
    # Display results
    print(f"\n📊 Search Results for '{args.query}'")
    print(f"{'='*60}")
    print(f"Found: {len(results)} files")
    print(f"Category: {args.category}")
    print(f"Search time: {search_time:.2f} seconds")
    
    if results:
        print(f"\n📁 Files Found:")
        print(f"{'-'*60}")
        
        total_size = 0
        for i, result in enumerate(results, 1):
            size_str = search.format_size(result['size'])
            total_size += result['size']
            
            print(f"{i:2d}. 📄 {result['name']}")
            print(f"    📂 {result['path']}")
            print(f"    💾 {size_str} | 🏷️  {result['type']} | 📅 {result['modified']}")
            print()
            
            # Show first 20 results in detail, then summarize
            if i == 20 and len(results) > 20:
                remaining = len(results) - 20
                print(f"    ... and {remaining} more files")
                print()
                break
        
        print(f"{'-'*60}")
        print(f"Total size: {search.format_size(total_size)}")
        
        # Show file type breakdown
        type_counts = {}
        for result in results:
            type_counts[result['type']] = type_counts.get(result['type'], 0) + 1
        
        if len(type_counts) > 1:
            print(f"\n📊 File Types:")
            for file_type, count in sorted(type_counts.items()):
                print(f"  {file_type}: {count} files")
    
    else:
        print(f"\n❌ No files found matching '{args.query}'")
        print(f"\n💡 Suggestions:")
        print(f"  - Try a shorter or more general search term")
        print(f"  - Check spelling")
        print(f"  - Try searching 'all' categories")
        print(f"  - Use partial words (e.g., 'H30' instead of 'H3000')")
    
    # Save results if requested
    if args.save and results:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"search_results_{args.query}_{timestamp}.json"
        
        search_data = {
            'query': args.query,
            'category': args.category,
            'timestamp': datetime.now().isoformat(),
            'total_results': len(results),
            'search_time_seconds': search_time,
            'results': results
        }
        
        with open(filename, 'w') as f:
            json.dump(search_data, f, indent=2)
        
        print(f"\n💾 Results saved to: {filename}")

if __name__ == "__main__":
    main()