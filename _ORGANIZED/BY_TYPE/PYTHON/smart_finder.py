#!/usr/bin/env python3
"""
SMART FINDER - Quickly search your library
Lightning-fast search across all scanned files
"""

import json
import re
from pathlib import Path
from collections import defaultdict

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
REPORT_FILE = WORKSPACE / "organization_report.json"

def load_file_database():
    """Load all files from scan report"""
    print("📂 Loading file database...")
    
    with open(REPORT_FILE, 'r') as f:
        report = json.load(f)
    
    # Build searchable file list
    files = []
    for category, info in report['categories'].items():
        if 'sample_files' in info:
            for filepath in info['sample_files']:
                files.append({
                    'path': filepath,
                    'name': Path(filepath).name,
                    'category': category
                })
    
    return files

def format_size(bytes_val):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} TB"

def search_files(query, files, category=None, limit=50):
    """Search files by name or path"""
    query_lower = query.lower()
    results = []
    
    for file_info in files:
        # Category filter
        if category and file_info['category'] != category:
            continue
        
        # Search in filename and path
        if (query_lower in file_info['name'].lower() or 
            query_lower in file_info['path'].lower()):
            results.append(file_info)
            
            if len(results) >= limit:
                break
    
    return results

def search_by_vendor(vendor, files):
    """Find all files from a specific vendor"""
    vendor_lower = vendor.lower()
    results = []
    
    for file_info in files:
        if vendor_lower in file_info['path'].lower():
            results.append(file_info)
    
    return results

def search_by_type(instrument_type, files):
    """Find files by instrument type"""
    keywords = {
        'strings': ['string', 'violin', 'cello', 'viola'],
        'brass': ['brass', 'trumpet', 'trombone', 'horn'],
        'percussion': ['drum', 'percussion', 'kick', 'snare'],
        'keys': ['piano', 'keys', 'organ'],
        'guitar': ['guitar', 'bass'],
        'synth': ['synth', 'pad', 'lead']
    }
    
    search_terms = keywords.get(instrument_type.lower(), [instrument_type])
    results = []
    
    for file_info in files:
        path_lower = file_info['path'].lower()
        if any(term in path_lower for term in search_terms):
            results.append(file_info)
    
    return results

def display_results(results, show_paths=True):
    """Display search results"""
    if not results:
        print("❌ No results found")
        return
    
    print(f"\n✅ Found {len(results)} results:\n")
    
    # Group by category
    by_category = defaultdict(list)
    for result in results:
        by_category[result['category']].append(result)
    
    for category, items in sorted(by_category.items()):
        print(f"📂 {category.upper()} ({len(items)} files)")
        print("-" * 70)
        
        for item in items[:20]:  # Show first 20 per category
            print(f"  • {item['name']}")
            if show_paths:
                print(f"    {item['path']}")
        
        if len(items) > 20:
            print(f"  ... and {len(items) - 20} more")
        
        print()

def interactive_search(files):
    """Interactive search mode"""
    print("\n" + "🔍"*35)
    print("  SMART FINDER - Interactive Search")
    print("🔍"*35 + "\n")
    
    while True:
        print("\nSearch Options:")
        print("  1. Search by name")
        print("  2. Search by vendor")
        print("  3. Search by instrument type")
        print("  4. Search by category")
        print("  5. Show statistics")
        print("  0. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '0':
            break
        
        elif choice == '1':
            query = input("Enter search term: ").strip()
            if query:
                results = search_files(query, files)
                display_results(results)
        
        elif choice == '2':
            vendor = input("Enter vendor name (e.g., Spitfire, Native Instruments): ").strip()
            if vendor:
                results = search_by_vendor(vendor, files)
                display_results(results, show_paths=False)
        
        elif choice == '3':
            print("\nAvailable types: strings, brass, percussion, keys, guitar, synth")
            inst_type = input("Enter instrument type: ").strip()
            if inst_type:
                results = search_by_type(inst_type, files)
                display_results(results, show_paths=False)
        
        elif choice == '4':
            print("\nCategories:")
            categories = set(f['category'] for f in files)
            for i, cat in enumerate(sorted(categories), 1):
                print(f"  {i}. {cat}")
            
            cat_choice = input("\nEnter category name: ").strip()
            if cat_choice:
                results = search_files("", files, category=cat_choice)
                print(f"\n✅ {len(results)} files in category '{cat_choice}'")
        
        elif choice == '5':
            show_statistics(files)

def show_statistics(files):
    """Show quick statistics"""
    print("\n" + "="*70)
    print("📊 QUICK STATISTICS")
    print("="*70 + "\n")
    
    # Count by category
    by_category = defaultdict(int)
    for file_info in files:
        by_category[file_info['category']] += 1
    
    print("Files by category:")
    for category, count in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:25} {count:>8,} files")
    
    print(f"\n{'Total:':25} {len(files):>8,} files")

def quick_search(query):
    """Quick command-line search"""
    files = load_file_database()
    results = search_files(query, files, limit=100)
    display_results(results)

def main():
    import sys
    
    if not REPORT_FILE.exists():
        print("❌ No scan data found!")
        print("Please run fast_organizer.py first to scan your library.")
        return
    
    files = load_file_database()
    print(f"✅ Loaded {len(files)} files from database\n")
    
    # Command-line mode
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        print(f"🔍 Searching for: {query}\n")
        quick_search(query)
    else:
        # Interactive mode
        interactive_search(files)

if __name__ == "__main__":
    main()

