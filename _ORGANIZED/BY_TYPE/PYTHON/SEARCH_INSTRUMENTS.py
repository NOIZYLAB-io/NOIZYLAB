#!/usr/bin/env python3
"""
EXS24 Master Library - Instrument Search Tool
Search for instruments by name, collection, or other criteria
"""

import json
import re
from pathlib import Path
from datetime import datetime

class InstrumentSearch:
    def __init__(self, scan_data_file=None):
        if scan_data_file is None:
            scan_data_file = Path(__file__).parent / "SCAN_DATA.json"
        self.scan_data_file = Path(scan_data_file)
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load scan data"""
        if not self.scan_data_file.exists():
            print(f"⚠️  Scan data not found: {self.scan_data_file}")
            print("   Run SCAN_AND_ORGANIZE.py first to generate scan data.")
            return False
        
        try:
            with open(self.scan_data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"✅ Loaded scan data ({len(self.data.get('exs_files', []))} files)")
            return True
        except Exception as e:
            print(f"⚠️  Error loading scan data: {e}")
            return False
    
    def search_by_name(self, query, case_sensitive=False):
        """Search instruments by name"""
        if not self.data:
            return []
        
        results = []
        query_lower = query.lower() if not case_sensitive else query
        
        for file_info in self.data.get('exs_files_detailed', []):
            file_name = file_info.get('name', '')
            file_path = file_info.get('path', '')
            
            search_name = file_name if case_sensitive else file_name.lower()
            search_path = file_path if case_sensitive else file_path.lower()
            
            if query_lower in search_name or query_lower in search_path:
                results.append(file_info)
        
        return results
    
    def search_by_collection(self, collection_name):
        """Search instruments by collection"""
        if not self.data:
            return []
        
        results = []
        collection_lower = collection_name.lower()
        
        for file_info in self.data.get('exs_files_detailed', []):
            collection = file_info.get('collection', '').lower()
            if collection_lower in collection:
                results.append(file_info)
        
        return results
    
    def search_by_pattern(self, pattern):
        """Search using regex pattern"""
        if not self.data:
            return []
        
        results = []
        try:
            regex = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            print(f"⚠️  Invalid regex pattern: {e}")
            return []
        
        for file_info in self.data.get('exs_files_detailed', []):
            file_name = file_info.get('name', '')
            file_path = file_info.get('path', '')
            
            if regex.search(file_name) or regex.search(file_path):
                results.append(file_info)
        
        return results
    
    def list_collections(self):
        """List all collections"""
        if not self.data:
            return []
        
        collections = {}
        for file_info in self.data.get('exs_files_detailed', []):
            collection = file_info.get('collection', 'UNKNOWN')
            if collection not in collections:
                collections[collection] = 0
            collections[collection] += 1
        
        return sorted(collections.items(), key=lambda x: x[1], reverse=True)
    
    def format_results(self, results, max_results=50):
        """Format search results for display"""
        if not results:
            return "No results found."
        
        output = []
        output.append(f"Found {len(results)} result(s):")
        output.append("")
        
        for i, file_info in enumerate(results[:max_results], 1):
            path = file_info.get('path', '')
            name = file_info.get('name', '')
            collection = file_info.get('collection', 'UNKNOWN')
            size_kb = file_info.get('size', 0) / 1024
            
            output.append(f"{i}. {name}")
            output.append(f"   Collection: {collection}")
            output.append(f"   Path: {path}")
            output.append(f"   Size: {size_kb:.2f} KB")
            output.append("")
        
        if len(results) > max_results:
            output.append(f"... and {len(results) - max_results} more results")
        
        return "\n".join(output)


def main():
    import sys
    
    search = InstrumentSearch()
    
    if not search.data:
        return
    
    if len(sys.argv) < 2:
        print("EXS24 Instrument Search Tool")
        print("")
        print("Usage:")
        print("  python3 SEARCH_INSTRUMENTS.py <query>           - Search by name")
        print("  python3 SEARCH_INSTRUMENTS.py --collection <name> - Search by collection")
        print("  python3 SEARCH_INSTRUMENTS.py --pattern <regex>  - Search by regex")
        print("  python3 SEARCH_INSTRUMENTS.py --list            - List all collections")
        print("")
        return
    
    if sys.argv[1] == '--list':
        print("📚 Collections:")
        print("-" * 80)
        collections = search.list_collections()
        for collection, count in collections:
            print(f"  {collection:40s} {count:5,} files")
    
    elif sys.argv[1] == '--collection' and len(sys.argv) > 2:
        collection = sys.argv[2]
        results = search.search_by_collection(collection)
        print(search.format_results(results))
    
    elif sys.argv[1] == '--pattern' and len(sys.argv) > 2:
        pattern = sys.argv[2]
        results = search.search_by_pattern(pattern)
        print(search.format_results(results))
    
    else:
        query = ' '.join(sys.argv[1:])
        results = search.search_by_name(query)
        print(search.format_results(results))


if __name__ == "__main__":
    main()

