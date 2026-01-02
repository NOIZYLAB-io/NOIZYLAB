#!/usr/bin/env python3
"""
🎹 KONTAKT Library Organization Dashboard
Quick overview of your library organization status
"""

from pathlib import Path
from collections import defaultdict

ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"

def analyze_organization():
    """Analyze current organization status"""
    print("🎹 KONTAKT LIBRARY ORGANIZATION DASHBOARD")
    print("=" * 55)
    
    organized = defaultdict(list)
    unorganized = []
    special_folders = []
    
    for item in ROOT.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            if item.name.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_', '13_')):
                # Count items in organized categories
                subfolders = [f for f in item.iterdir() if f.is_dir()]
                organized[item.name] = len(subfolders)
            elif item.name in ['REPORTS', 'BACKUP', 'ORGANIZED_LIBRARIES', 'TEMP_PROCESSING', 'SAMPLE_ARCHIVES']:
                special_folders.append(item.name)
            elif not item.name.startswith('_'):
                unorganized.append(item.name)
    
    # Display organized categories
    print("\n📁 ORGANIZED CATEGORIES:")
    print("─" * 30)
    total_organized = 0
    for category in sorted(organized.keys()):
        count = organized[category]
        total_organized += count
        category_display = category.replace('_', ' ').title()
        print(f"{category_display:.<25} {count:>3} libraries")
    
    print(f"{'Total Organized':.<25} {total_organized:>3} libraries")
    
    # Display unorganized
    if unorganized:
        print(f"\n📦 UNORGANIZED LIBRARIES ({len(unorganized)}):")
        print("─" * 30)
        
        # Group by common patterns
        patterns = defaultdict(list)
        for lib in unorganized:
            if any(x in lib.lower() for x in ['run', 'ascending', 'descending']):
                patterns['Runs/Arpeggios'].append(lib)
            elif 'discolick' in lib.lower():
                patterns['Discolicks'].append(lib)
            elif any(x in lib.lower() for x in ['wavy', 'sawtooth']):
                patterns['Synthesizers'].append(lib)
            elif 'celli' in lib.lower():
                patterns['Cellos/Strings'].append(lib)
            elif any(x in lib.lower() for x in ['slow', 'ambient']):
                patterns['Ambient/Slow'].append(lib)
            else:
                patterns['Other'].append(lib)
        
        for pattern, libs in patterns.items():
            if libs:
                print(f"\n{pattern} ({len(libs)}):")
                for lib in libs[:5]:  # Show first 5
                    print(f"  • {lib}")
                if len(libs) > 5:
                    print(f"  ... and {len(libs) - 5} more")
    
    # Summary
    print(f"\n📊 SUMMARY:")
    print("─" * 15)
    print(f"✅ Organized: {total_organized}")
    print(f"📦 Unorganized: {len(unorganized)}")
    print(f"🗂️  Special Folders: {len(special_folders)}")
    print(f"📚 Total Libraries: {total_organized + len(unorganized)}")
    
    if len(unorganized) > 0:
        percentage = (total_organized / (total_organized + len(unorganized))) * 100
        print(f"📈 Organization Progress: {percentage:.1f}%")
    else:
        print("🎉 100% Organized!")
    
    return len(unorganized)

def suggest_next_steps():
    """Suggest what to do next"""
    unorganized_count = analyze_organization()
    
    print(f"\n💡 SUGGESTED NEXT STEPS:")
    print("─" * 25)
    
    if unorganized_count > 0:
        if unorganized_count > 20:
            print("1. Run quick pattern-based auto-organization first")
            print("2. Then use interactive organizer for remaining libraries")
            print("3. Command: python3 interactive_organizer.py")
        else:
            print("1. Use interactive organizer to categorize remaining libraries")
            print("2. Command: python3 interactive_organizer.py")
    else:
        print("✅ All libraries organized!")
        print("1. Run auto scanner to update reports")
        print("2. Command: python3 auto_scan.py")

if __name__ == "__main__":
    suggest_next_steps()