#!/usr/bin/env python3
"""
SUPERIOR DRUMMER 3 - QUICK ACCESS
Ultra-fast groove finder without heavy indexing
"""

import os
import sys
import glob

SD3 = '/Volumes/MAG 4TB/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3'

BANNER = """
╔════════════════════════════════════════════════════════════════╗
║       🥁 SUPERIOR DRUMMER 3 - QUICK GROOVE FINDER 🥁           ║
╚════════════════════════════════════════════════════════════════╝
"""

MENU = """
═══════════════════════════════════════════════════════════════

QUICK CATEGORIES
  1. Ballad Grooves (Slow)
  2. Midtempo Grooves (Medium) ⭐ MOST
  3. Uptempo Grooves (Fast)
  4. Straight 4/4 (Rock/Pop)
  5. Swing Grooves (Jazz)
  6. Brushes
  7. Fills & Extras
  8. All Grooves

SMART SEARCH
  9. Search by Name
 10. Browse Folder

═══════════════════════════════════════════════════════════════
 0. Exit

Choice: """

def list_grooves(pattern, title, limit=30):
    """Quick list of grooves"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")
    
    files = glob.glob(f"{SD3}/{pattern}", recursive=True)
    
    if not files:
        print("No grooves found")
        return
    
    print(f"Found {len(files)} grooves\n")
    
    for i, f in enumerate(sorted(files)[:limit], 1):
        name = os.path.basename(f).replace('.mid', '')
        rel = f.replace(SD3, '').strip('/')
        parts = rel.split('/')
        cat = parts[0] if parts else ''
        
        print(f"{i:3d}. {name}")
        if len(parts) > 1:
            print(f"      {parts[1]}")
    
    if len(files) > limit:
        print(f"\n... and {len(files) - limit} more")
    
    print(f"\n📁 Location: {SD3}")

def search_by_name(query):
    """Search grooves by name"""
    print(f"\n🔍 Searching for: {query}\n")
    
    files = glob.glob(f"{SD3}/**/*.mid", recursive=True)
    matches = [f for f in files if query.lower() in os.path.basename(f).lower()]
    
    if not matches:
        print("No matches found")
        return
    
    print(f"Found {len(matches)} matches:\n")
    
    for i, f in enumerate(sorted(matches)[:30], 1):
        name = os.path.basename(f).replace('.mid', '')
        print(f"{i:3d}. {name}")
        print(f"      {f}")
    
    if len(matches) > 30:
        print(f"\n... and {len(matches) - 30} more")

def browse_folder():
    """Browse the groove folder in Finder"""
    os.system(f'open "{SD3}"')
    print("\n✅ Opened in Finder!")

def quick_stats():
    """Super quick stats"""
    ballad = len(glob.glob(f"{SD3}/*200@*/**/*.mid", recursive=True))
    midtempo = len(glob.glob(f"{SD3}/*400@*/**/*.mid", recursive=True))
    uptempo = len(glob.glob(f"{SD3}/*500@*/**/*.mid", recursive=True))
    straight = len(glob.glob(f"{SD3}/*STRAIGHT*4#4*/**/*.mid", recursive=True))
    swing = len(glob.glob(f"{SD3}/*SWING*/**/*.mid", recursive=True))
    brushes = len(glob.glob(f"{SD3}/*BRUSHES*/**/*.mid", recursive=True))
    
    print(f"\n📊 QUICK STATS")
    print(f"   Ballad:        {ballad:4d} grooves")
    print(f"   Midtempo:      {midtempo:4d} grooves ⭐")
    print(f"   Uptempo:       {uptempo:4d} grooves")
    print(f"   Straight 4/4:  {straight:4d} grooves")
    print(f"   Swing:         {swing:4d} grooves")
    print(f"   Brushes:       {brushes:4d} grooves")

def main():
    """Main menu"""
    while True:
        print(BANNER)
        quick_stats()
        
        choice = input(MENU).strip()
        
        if choice == '0':
            print("\n👋 Done!")
            break
        
        elif choice == '1':
            list_grooves("*200@*/**/*.mid", "BALLAD GROOVES (Slow)")
            input("\nPress Enter...")
        
        elif choice == '2':
            list_grooves("*400@*/**/*.mid", "MIDTEMPO GROOVES (Medium)")
            input("\nPress Enter...")
        
        elif choice == '3':
            list_grooves("*500@*/**/*.mid", "UPTEMPO GROOVES (Fast)")
            input("\nPress Enter...")
        
        elif choice == '4':
            list_grooves("*STRAIGHT*4#4*/**/*.mid", "STRAIGHT 4/4 (Rock/Pop)")
            input("\nPress Enter...")
        
        elif choice == '5':
            list_grooves("*SWING*/**/*.mid", "SWING GROOVES (Jazz)")
            input("\nPress Enter...")
        
        elif choice == '6':
            list_grooves("*BRUSHES*/**/*.mid", "BRUSHES")
            input("\nPress Enter...")
        
        elif choice == '7':
            print("\n📂 FILLS & EXTRAS")
            print("\nSnare Rolls:")
            list_grooves("*SNARE*ROLL*/**/*.mid", "Snare Rolls", 10)
            print("\nCymbal Stuff:")
            list_grooves("*CYMBAL*/**/*.mid", "Cymbal Patterns", 10)
            print("\nOne Shots:")
            list_grooves("*ONE*SHOT*/**/*.mid", "One Shots", 10)
            input("\nPress Enter...")
        
        elif choice == '8':
            list_grooves("**/*.mid", "ALL GROOVES", 50)
            input("\nPress Enter...")
        
        elif choice == '9':
            query = input("\n🔍 Search term: ").strip()
            if query:
                search_by_name(query)
            input("\nPress Enter...")
        
        elif choice == '10':
            browse_folder()
            input("\nPress Enter...")
        
        else:
            print("\n❌ Invalid choice")
            input("Press Enter...")
        
        # Clear screen
        os.system('clear' if os.name != 'nt' else 'cls')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Bye!")
        sys.exit(0)

