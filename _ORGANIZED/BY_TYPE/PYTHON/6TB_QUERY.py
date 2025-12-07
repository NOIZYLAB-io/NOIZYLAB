#!/usr/bin/env python3
"""
🔍 6TB DATABASE QUERY TOOL 🔍

Query and search the 6TB WAV file database
"""

import sqlite3
import sys
from pathlib import Path
from datetime import datetime

DATABASE_FILE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_index.db")

def connect_db():
    """Connect to database"""
    if not DATABASE_FILE.exists():
        print(f"❌ Database not found: {DATABASE_FILE}")
        print("Run 6TB_SCANNER.py first!")
        sys.exit(1)
    return sqlite3.connect(DATABASE_FILE)

def show_stats():
    """Show database statistics"""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("="*80)
    print("📊 6TB DATABASE STATISTICS")
    print("="*80 + "\n")
    
    # Total files
    cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files")
    total_files, total_size = cursor.fetchone()
    
    print(f"Total WAV files: {total_files:,}")
    print(f"Total size: {(total_size or 0)/(1024**3):.2f} GB\n")
    
    # Originals vs Commercial
    print("⭐⭐⭐ HARD RULE RESULTS ⭐⭐⭐\n")
    
    cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files WHERE is_original = 1")
    orig_count, orig_size = cursor.fetchone()
    print(f"⭐ ORIGINAL COMPOSITIONS: {orig_count:,} files ({(orig_size or 0)/(1024**3):.2f} GB)")
    
    cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files WHERE is_original = 0")
    comm_count, comm_size = cursor.fetchone()
    print(f"📦 Commercial Samples: {comm_count:,} files ({(comm_size or 0)/(1024**3):.2f} GB)\n")
    
    # By category
    print("="*80)
    print("📁 BY CATEGORY:")
    print("="*80)
    
    cursor.execute("""
        SELECT category, COUNT(*), SUM(size)
        FROM wav_files
        GROUP BY category
        ORDER BY COUNT(*) DESC
    """)
    
    for category, count, size in cursor.fetchall():
        print(f"  {category:40s} {count:6,} files ({(size or 0)/(1024**2):8.1f} MB)")
    
    print()
    conn.close()

def search_files(query):
    """Search for files by name"""
    conn = connect_db()
    cursor = conn.cursor()
    
    print(f"\n🔍 Searching for: '{query}'\n")
    
    cursor.execute("""
        SELECT filename, path, size, is_original, category
        FROM wav_files
        WHERE filename LIKE ?
        ORDER BY is_original DESC, filename
        LIMIT 100
    """, (f"%{query}%",))
    
    results = cursor.fetchall()
    
    if not results:
        print("No files found.")
    else:
        print(f"Found {len(results)} files:\n")
        for filename, path, size, is_original, category in results:
            icon = "⭐" if is_original else "📦"
            print(f"{icon} {filename}")
            print(f"   Path: {path}")
            print(f"   Size: {size/(1024**2):.2f} MB | Category: {category}\n")
    
    conn.close()

def list_originals(limit=50):
    """List original compositions"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 1")
    total = cursor.fetchone()[0]
    
    print(f"\n⭐⭐⭐ YOUR ORIGINAL COMPOSITIONS ⭐⭐⭐")
    print(f"Total: {total:,} files\n")
    
    cursor.execute("""
        SELECT filename, path, size
        FROM wav_files
        WHERE is_original = 1
        ORDER BY filename
        LIMIT ?
    """, (limit,))
    
    for i, (filename, path, size) in enumerate(cursor.fetchall(), 1):
        print(f"{i:3d}. {filename}")
        print(f"     {path}")
        print(f"     Size: {size/(1024**2):.2f} MB\n")
    
    if total > limit:
        print(f"... and {total - limit} more originals!\n")
    
    conn.close()

def find_duplicates():
    """Find duplicate files by fingerprint"""
    conn = connect_db()
    cursor = conn.cursor()
    
    print("\n🔍 Finding duplicates...\n")
    
    cursor.execute("""
        SELECT audio_fingerprint, COUNT(*), GROUP_CONCAT(filename, '|||')
        FROM wav_files
        WHERE audio_fingerprint IS NOT NULL
        GROUP BY audio_fingerprint
        HAVING COUNT(*) > 1
    """)
    
    duplicates = cursor.fetchall()
    
    if not duplicates:
        print("✓ No duplicates found!")
    else:
        print(f"⚠️  Found {len(duplicates)} sets of duplicates:\n")
        
        for fingerprint, count, filenames in duplicates[:20]:
            files = filenames.split('|||')
            print(f"Duplicate set ({count} files):")
            for f in files:
                print(f"  • {f}")
            print()
        
        if len(duplicates) > 20:
            print(f"... and {len(duplicates) - 20} more duplicate sets\n")
    
    conn.close()

def export_originals():
    """Export list of originals to file"""
    conn = connect_db()
    cursor = conn.cursor()
    
    output_file = Path("/Volumes/4TBSG/KTK 2026 TO SORT/ORIGINALS_LIST.txt")
    
    cursor.execute("""
        SELECT path, filename, size
        FROM wav_files
        WHERE is_original = 1
        ORDER BY path
    """)
    
    with open(output_file, 'w') as f:
        f.write("⭐⭐⭐ YOUR ORIGINAL COMPOSITIONS ⭐⭐⭐\n\n")
        
        for path, filename, size in cursor.fetchall():
            f.write(f"{path}\n")
    
    count = cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 1").fetchone()[0]
    
    print(f"\n✓ Exported {count:,} originals to: {output_file}\n")
    conn.close()

def menu():
    """Interactive menu"""
    print("="*80)
    print("🔍 6TB DATABASE QUERY TOOL")
    print("="*80)
    print("\n1. Show statistics")
    print("2. List original compositions")
    print("3. Search files")
    print("4. Find duplicates")
    print("5. Export originals list")
    print("6. Exit")
    print()
    
    choice = input("Choose option (1-6): ").strip()
    
    if choice == '1':
        show_stats()
    elif choice == '2':
        try:
            limit = int(input("How many to show? (default 50): ") or "50")
        except:
            limit = 50
        list_originals(limit)
    elif choice == '3':
        query = input("Search term: ").strip()
        if query:
            search_files(query)
    elif choice == '4':
        find_duplicates()
    elif choice == '5':
        export_originals()
    elif choice == '6':
        sys.exit(0)
    else:
        print("Invalid option")
    
    print("\nPress Enter to continue...")
    input()
    menu()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'stats':
            show_stats()
        elif command == 'originals':
            list_originals()
        elif command == 'duplicates':
            find_duplicates()
        elif command == 'export':
            export_originals()
        elif command == 'search' and len(sys.argv) > 2:
            search_files(sys.argv[2])
        else:
            print("Usage: python3 6TB_QUERY.py [stats|originals|duplicates|export|search TERM]")
    else:
        menu()

