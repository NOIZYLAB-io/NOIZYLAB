#!/usr/bin/env python3
"""
SUPERIOR DRUMMER MANAGER - Advanced MIDI Groove Management
Features:
- Complete groove library indexing
- Smart search by tempo, style, time signature
- Groove recommendations
- Batch copy/export
- Usage analytics
- Collection management
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
import shutil

ROOT = '/Volumes/MAG 4TB/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3'
EXPORT_DIR = '/Volumes/MAG 4TB/NoizyWorkspace/SD3_Exported_Grooves'
INDEX_FILE = '/Volumes/MAG 4TB/NoizyWorkspace/sd3_groove_index.json'

def parse_tempo(dirname):
    """Extract tempo from directory name"""
    match = re.search(r'(\d{2,3})[_-]?BPM', dirname, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def parse_time_signature(dirname):
    """Extract time signature from directory name"""
    match = re.search(r'(\d+)#(\d+)', dirname)
    if match:
        return f"{match.group(1)}/{match.group(2)}"
    return None

def parse_style(dirname):
    """Extract style from directory name"""
    styles = {
        'SWING': 'Swing',
        'STRAIGHT': 'Straight',
        'BALLAD': 'Ballad',
        'HALF_TIME': 'Half Time',
        'MIDTEMPO': 'Midtempo',
        'UPTEMPO': 'Uptempo',
        'BRUSHES': 'Brushes',
        'SLOW': 'Slow'
    }
    
    for key, value in styles.items():
        if key in dirname.upper():
            return value
    return 'Other'

def index_all_grooves():
    """Create comprehensive index of all grooves"""
    print("🔍 Indexing Superior Drummer 3 Grooves...")
    
    grooves = []
    categories = defaultdict(int)
    
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith('.mid'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, ROOT)
                
                # Parse metadata from path
                parts = rel_path.split(os.sep)
                
                groove_info = {
                    'name': os.path.splitext(file)[0],
                    'file': file,
                    'path': filepath,
                    'relative_path': rel_path,
                    'category': parts[0] if len(parts) > 0 else 'Unknown',
                    'subcategory': parts[1] if len(parts) > 1 else None,
                    'tempo': None,
                    'time_signature': None,
                    'style': 'Unknown',
                    'size': os.path.getsize(filepath)
                }
                
                # Extract metadata from directory names
                for part in parts:
                    if tempo := parse_tempo(part):
                        groove_info['tempo'] = tempo
                    if ts := parse_time_signature(part):
                        groove_info['time_signature'] = ts
                    if style := parse_style(part):
                        groove_info['style'] = style
                
                grooves.append(groove_info)
                categories[groove_info['category']] += 1
    
    # Save index
    index_data = {
        'total_grooves': len(grooves),
        'categories': dict(categories),
        'grooves': grooves,
        'indexed_at': str(Path(INDEX_FILE).stat().st_mtime if os.path.exists(INDEX_FILE) else 'Never')
    }
    
    with open(INDEX_FILE, 'w') as f:
        json.dump(index_data, f, indent=2)
    
    print(f"✅ Indexed {len(grooves)} grooves")
    print(f"📊 Categories: {len(categories)}")
    
    return index_data

def load_index():
    """Load groove index"""
    if not os.path.exists(INDEX_FILE):
        return index_all_grooves()
    
    with open(INDEX_FILE, 'r') as f:
        return json.load(f)

def search_grooves(query=None, tempo_min=None, tempo_max=None, 
                   time_sig=None, style=None, category=None):
    """Search grooves with filters"""
    index = load_index()
    results = index['grooves']
    
    # Apply filters
    if query:
        query_lower = query.lower()
        results = [g for g in results if query_lower in g['name'].lower()]
    
    if tempo_min:
        results = [g for g in results if g['tempo'] and g['tempo'] >= tempo_min]
    
    if tempo_max:
        results = [g for g in results if g['tempo'] and g['tempo'] <= tempo_max]
    
    if time_sig:
        results = [g for g in results if g['time_signature'] == time_sig]
    
    if style:
        results = [g for g in results if style.lower() in g['style'].lower()]
    
    if category:
        results = [g for g in results if category.lower() in g['category'].lower()]
    
    return results

def analyze_collection():
    """Analyze the groove collection"""
    print("\n" + "="*70)
    print("SUPERIOR DRUMMER 3 - COLLECTION ANALYSIS")
    print("="*70)
    
    index = load_index()
    grooves = index['grooves']
    
    # Tempo analysis
    tempos = [g['tempo'] for g in grooves if g['tempo']]
    if tempos:
        print(f"\n### TEMPO ANALYSIS ###")
        print(f"Grooves with tempo info: {len(tempos)}")
        print(f"Tempo range: {min(tempos)} - {max(tempos)} BPM")
        print(f"Average tempo: {sum(tempos)/len(tempos):.1f} BPM")
        
        # Tempo ranges
        ranges = {
            'Slow (60-90)': len([t for t in tempos if 60 <= t <= 90]),
            'Medium (91-120)': len([t for t in tempos if 91 <= t <= 120]),
            'Fast (121-150)': len([t for t in tempos if 121 <= t <= 150]),
            'Very Fast (151+)': len([t for t in tempos if t > 150])
        }
        print("\nTempo Distribution:")
        for range_name, count in ranges.items():
            print(f"  {range_name:20s}: {count:4d} grooves")
    
    # Time signature analysis
    time_sigs = defaultdict(int)
    for g in grooves:
        if g['time_signature']:
            time_sigs[g['time_signature']] += 1
    
    if time_sigs:
        print(f"\n### TIME SIGNATURE ANALYSIS ###")
        for sig, count in sorted(time_sigs.items(), key=lambda x: -x[1]):
            print(f"  {sig:10s}: {count:4d} grooves")
    
    # Style analysis
    styles = defaultdict(int)
    for g in grooves:
        styles[g['style']] += 1
    
    print(f"\n### STYLE ANALYSIS ###")
    for style, count in sorted(styles.items(), key=lambda x: -x[1]):
        print(f"  {style:20s}: {count:4d} grooves")
    
    # Category analysis
    print(f"\n### CATEGORY ANALYSIS ###")
    for cat, count in sorted(index['categories'].items(), key=lambda x: -x[1]):
        cat_clean = cat.split('@')[1] if '@' in cat else cat
        cat_clean = cat_clean.replace('_', ' ').replace('#', '/')
        print(f"  {cat_clean:30s}: {count:4d} grooves")
    
    # Size analysis
    total_size = sum(g['size'] for g in grooves)
    avg_size = total_size / len(grooves) if grooves else 0
    print(f"\n### SIZE ANALYSIS ###")
    print(f"Total size: {total_size / (1024*1024):.2f} MB")
    print(f"Average groove size: {avg_size / 1024:.2f} KB")
    print(f"Largest groove: {max(g['size'] for g in grooves) / 1024:.2f} KB")
    print(f"Smallest groove: {min(g['size'] for g in grooves) / 1024:.2f} KB")

def recommend_grooves(tempo=None, style=None, limit=10):
    """Recommend grooves based on criteria"""
    print(f"\n🎵 GROOVE RECOMMENDATIONS")
    
    if tempo:
        print(f"Tempo: ~{tempo} BPM")
    if style:
        print(f"Style: {style}")
    
    # Search with some tolerance for tempo
    tempo_min = tempo - 10 if tempo else None
    tempo_max = tempo + 10 if tempo else None
    
    results = search_grooves(tempo_min=tempo_min, tempo_max=tempo_max, style=style)
    
    if not results:
        print("\n❌ No grooves found matching criteria")
        return
    
    print(f"\nFound {len(results)} matching grooves")
    print(f"Showing top {min(limit, len(results))}:\n")
    
    for i, groove in enumerate(results[:limit], 1):
        tempo_str = f"{groove['tempo']} BPM" if groove['tempo'] else "Unknown BPM"
        ts_str = groove['time_signature'] or "Unknown"
        print(f"{i:2d}. {groove['name']}")
        print(f"    {tempo_str} | {ts_str} | {groove['style']}")
        print(f"    {groove['relative_path']}")
        print()

def export_grooves(search_params, export_name):
    """Export matching grooves to a folder"""
    results = search_grooves(**search_params)
    
    if not results:
        print("❌ No grooves found matching criteria")
        return
    
    export_path = os.path.join(EXPORT_DIR, export_name)
    os.makedirs(export_path, exist_ok=True)
    
    print(f"\n📦 Exporting {len(results)} grooves to:")
    print(f"   {export_path}")
    
    for groove in results:
        dest = os.path.join(export_path, groove['file'])
        shutil.copy2(groove['path'], dest)
    
    # Create index file
    with open(os.path.join(export_path, '_INDEX.txt'), 'w') as f:
        f.write(f"Superior Drummer 3 - {export_name}\n")
        f.write("="*70 + "\n\n")
        f.write(f"Total Grooves: {len(results)}\n")
        f.write(f"Exported: {export_name}\n\n")
        
        for i, groove in enumerate(results, 1):
            f.write(f"{i}. {groove['file']}\n")
            if groove['tempo']:
                f.write(f"   Tempo: {groove['tempo']} BPM\n")
            if groove['time_signature']:
                f.write(f"   Time Sig: {groove['time_signature']}\n")
            f.write(f"   Style: {groove['style']}\n")
            f.write("\n")
    
    print(f"✅ Export complete!")
    print(f"   Files: {len(results)}")
    print(f"   Location: {export_path}")

def create_quick_collections():
    """Create commonly used groove collections"""
    print("\n" + "="*70)
    print("CREATING QUICK COLLECTIONS")
    print("="*70)
    
    collections = {
        'Rock_120_140_BPM': {
            'tempo_min': 120,
            'tempo_max': 140,
            'style': 'straight',
            'time_sig': '4/4'
        },
        'Ballads_Slow': {
            'tempo_min': 60,
            'tempo_max': 90,
            'style': 'ballad'
        },
        'Jazz_Swing': {
            'style': 'swing'
        },
        'Brushes_All': {
            'category': 'brushes'
        },
        'Fast_Grooves_150_Plus': {
            'tempo_min': 150
        },
        'Half_Time_Grooves': {
            'style': 'half time'
        }
    }
    
    for name, params in collections.items():
        print(f"\n📁 Creating: {name}")
        export_grooves(params, name)
    
    print(f"\n✅ All collections created in:")
    print(f"   {EXPORT_DIR}")

def interactive_search():
    """Interactive search interface"""
    print("\n" + "="*70)
    print("INTERACTIVE GROOVE SEARCH")
    print("="*70)
    
    print("\nFilters (press Enter to skip):")
    
    query = input("  Search term: ").strip() or None
    
    tempo_input = input("  Tempo (e.g., 120 or 100-130): ").strip()
    tempo_min = tempo_max = None
    if tempo_input:
        if '-' in tempo_input:
            parts = tempo_input.split('-')
            tempo_min = int(parts[0]) if parts[0] else None
            tempo_max = int(parts[1]) if parts[1] else None
        else:
            tempo_min = int(tempo_input) - 10
            tempo_max = int(tempo_input) + 10
    
    time_sig = input("  Time signature (e.g., 4/4): ").strip() or None
    style = input("  Style (e.g., swing, straight): ").strip() or None
    category = input("  Category (e.g., ballad, midtempo): ").strip() or None
    
    # Search
    results = search_grooves(query, tempo_min, tempo_max, time_sig, style, category)
    
    print(f"\n{'='*70}")
    print(f"SEARCH RESULTS: {len(results)} grooves found")
    print(f"{'='*70}\n")
    
    if results:
        for i, groove in enumerate(results[:20], 1):
            tempo_str = f"{groove['tempo']} BPM" if groove['tempo'] else "?"
            ts_str = groove['time_signature'] or "?"
            print(f"{i:2d}. {groove['name']:40s} | {tempo_str:10s} | {ts_str:5s} | {groove['style']}")
        
        if len(results) > 20:
            print(f"\n... and {len(results) - 20} more")
        
        # Export option
        export = input("\n📦 Export these grooves? (yes/no): ").strip().lower()
        if export == 'yes':
            name = input("Collection name: ").strip()
            if name:
                export_grooves({
                    'query': query,
                    'tempo_min': tempo_min,
                    'tempo_max': tempo_max,
                    'time_sig': time_sig,
                    'style': style,
                    'category': category
                }, name)

def main():
    """Main menu"""
    while True:
        print("\n" + "="*70)
        print("SUPERIOR DRUMMER 3 - GROOVE MANAGER")
        print("="*70)
        print("\n1. Index/Re-index Grooves")
        print("2. Analyze Collection")
        print("3. Interactive Search")
        print("4. Get Recommendations")
        print("5. Create Quick Collections")
        print("6. View Statistics")
        print("7. Export Custom Collection")
        print("0. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '0':
            break
        
        elif choice == '1':
            index_all_grooves()
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            analyze_collection()
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            interactive_search()
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            tempo = input("Tempo (BPM): ").strip()
            tempo = int(tempo) if tempo else None
            style = input("Style: ").strip() or None
            recommend_grooves(tempo, style)
            input("\nPress Enter to continue...")
        
        elif choice == '5':
            create_quick_collections()
            input("\nPress Enter to continue...")
        
        elif choice == '6':
            index = load_index()
            print(f"\n📊 STATISTICS")
            print(f"Total Grooves: {index['total_grooves']}")
            print(f"Categories: {len(index['categories'])}")
            print(f"Last Indexed: {index['indexed_at']}")
            input("\nPress Enter to continue...")
        
        elif choice == '7':
            name = input("Collection name: ").strip()
            print("\nFilters (Enter to skip):")
            tempo_min = input("  Min tempo: ").strip()
            tempo_max = input("  Max tempo: ").strip()
            style = input("  Style: ").strip() or None
            
            export_grooves({
                'tempo_min': int(tempo_min) if tempo_min else None,
                'tempo_max': int(tempo_max) if tempo_max else None,
                'style': style
            }, name)
            input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()

