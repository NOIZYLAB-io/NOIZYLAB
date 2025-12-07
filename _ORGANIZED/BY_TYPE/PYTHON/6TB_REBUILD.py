#!/usr/bin/env python3
"""
🔨 6TB COMPLETE REBUILD SYSTEM 🔨

Rebuild and reorganize entire 6TB drive structure
"""

import sqlite3
import shutil
from pathlib import Path
from datetime import datetime

DATABASE_FILE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_index.db")
OUTPUT_BASE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_ORGANIZED")

def connect_db():
    """Connect to database"""
    if not DATABASE_FILE.exists():
        print(f"❌ Database not found!")
        print("Run 6TB_SCANNER.py first!")
        return None
    return sqlite3.connect(DATABASE_FILE)

def rebuild_structure():
    """Rebuild entire organized structure"""
    conn = connect_db()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    print("="*80)
    print("🔨 6TB COMPLETE REBUILD")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE ENFORCEMENT ⭐⭐⭐")
    print("Rebuilding entire structure based on metadata analysis\n")
    
    # Get stats
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 1")
    orig_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 0")
    comm_count = cursor.fetchone()[0]
    
    print(f"Files to organize:")
    print(f"  ⭐ Originals: {orig_count:,}")
    print(f"  📦 Commercial: {comm_count:,}")
    print(f"  Total: {orig_count + comm_count:,}\n")
    
    # Create base structure
    print("📁 Creating directory structure...")
    
    originals_dir = OUTPUT_BASE / "ORIGINAL_COMPOSITIONS"
    originals_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all categories
    cursor.execute("SELECT DISTINCT category FROM wav_files WHERE category IS NOT NULL")
    for (category,) in cursor.fetchall():
        if category and category != "ORIGINAL_COMPOSITIONS":
            (OUTPUT_BASE / category).mkdir(parents=True, exist_ok=True)
    
    print("✓ Structure created\n")
    
    # Rebuild by priority: originals first!
    print("⭐ Phase 1: Organizing ORIGINAL COMPOSITIONS...")
    
    cursor.execute("""
        SELECT path, filename, category
        FROM wav_files
        WHERE is_original = 1
        ORDER BY filename
    """)
    
    orig_organized = 0
    for path, filename, category in cursor.fetchall():
        try:
            dest_folder = OUTPUT_BASE / "ORIGINAL_COMPOSITIONS"
            dest_file = dest_folder / filename
            
            counter = 1
            original_dest = dest_file
            while dest_file.exists():
                dest_file = dest_folder / f"{original_dest.stem}_{counter}{original_dest.suffix}"
                counter += 1
            
            shutil.copy2(path, dest_file)
            orig_organized += 1
            
            if orig_organized % 10 == 0:
                print(f"  Organized {orig_organized:,} originals...")
        except Exception as e:
            print(f"  Error: {filename}: {e}")
    
    print(f"✓ Organized {orig_organized:,} originals!\n")
    
    # Organize commercial
    print("📦 Phase 2: Organizing commercial samples...")
    
    cursor.execute("""
        SELECT path, filename, category
        FROM wav_files
        WHERE is_original = 0
        ORDER BY category, filename
    """)
    
    comm_organized = 0
    for path, filename, category in cursor.fetchall():
        try:
            dest_folder = OUTPUT_BASE / (category or "Commercial/Other")
            dest_folder.mkdir(parents=True, exist_ok=True)
            
            dest_file = dest_folder / filename
            
            counter = 1
            original_dest = dest_file
            while dest_file.exists():
                dest_file = dest_folder / f"{original_dest.stem}_{counter}{original_dest.suffix}"
                counter += 1
            
            shutil.copy2(path, dest_file)
            comm_organized += 1
            
            if comm_organized % 100 == 0:
                print(f"  Organized {comm_organized:,} commercial files...")
        except Exception as e:
            pass
    
    print(f"✓ Organized {comm_organized:,} commercial files!\n")
    
    # Generate summary
    print("="*80)
    print("✅ REBUILD COMPLETE!")
    print("="*80)
    print(f"\n⭐ Originals organized: {orig_organized:,}")
    print(f"📦 Commercial organized: {comm_organized:,}")
    print(f"\nOutput: {OUTPUT_BASE}/\n")
    
    conn.close()

def verify_structure():
    """Verify the organized structure"""
    print("="*80)
    print("🔍 VERIFYING ORGANIZED STRUCTURE")
    print("="*80 + "\n")
    
    if not OUTPUT_BASE.exists():
        print("❌ Output directory doesn't exist!")
        print("Run rebuild first.")
        return
    
    # Count files in organized structure
    originals_dir = OUTPUT_BASE / "ORIGINAL_COMPOSITIONS"
    
    if originals_dir.exists():
        originals = list(originals_dir.rglob('*.wav')) + list(originals_dir.rglob('*.WAV'))
        print(f"⭐ ORIGINAL_COMPOSITIONS/: {len(originals):,} files")
    else:
        print("⚠️  ORIGINAL_COMPOSITIONS/ not found!")
    
    # Count commercial
    commercial_count = 0
    for item in OUTPUT_BASE.iterdir():
        if item.is_dir() and item.name != "ORIGINAL_COMPOSITIONS":
            files = list(item.rglob('*.wav')) + list(item.rglob('*.WAV'))
            commercial_count += len(files)
            if files:
                print(f"📦 {item.name}/: {len(files):,} files")
    
    print(f"\nTotal commercial: {commercial_count:,} files")
    print("\n✓ Verification complete\n")

def create_index_html():
    """Create HTML index of organized files"""
    print("🌐 Creating HTML index...")
    
    conn = connect_db()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    html_file = OUTPUT_BASE / "INDEX.html"
    
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>6TB WAV Organization Index</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        .category {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .file-list {
            max-height: 300px;
            overflow-y: auto;
        }
        .file-item {
            padding: 5px;
            border-bottom: 1px solid #eee;
            font-size: 0.9em;
        }
        .originals {
            border-left: 5px solid #ffd700;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🗄️ 6TB WAV Organization Index</h1>
        <p>Generated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    </div>
    
    <div class="stats">"""
    
    # Stats
    cursor.execute("SELECT COUNT(*) FROM wav_files")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 1")
    originals = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 0")
    commercial = cursor.fetchone()[0]
    
    html += f"""
        <div class="stat-card">
            <div class="stat-value">{total:,}</div>
            <div>Total Files</div>
        </div>
        <div class="stat-card">
            <div class="stat-value" style="color: #ffd700;">⭐ {originals:,}</div>
            <div>Originals</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{commercial:,}</div>
            <div>Commercial</div>
        </div>
    </div>
    
    <div class="category originals">
        <h2>⭐⭐⭐ ORIGINAL COMPOSITIONS</h2>
        <p>Files WITHOUT metadata = YOUR music!</p>
        <div class="file-list">"""
    
    cursor.execute("""
        SELECT filename
        FROM wav_files
        WHERE is_original = 1
        ORDER BY filename
    """)
    
    for (filename,) in cursor.fetchall():
        html += f'<div class="file-item">⭐ {filename}</div>'
    
    html += """
        </div>
    </div>
    
    <h2>📦 Commercial Samples by Category</h2>"""
    
    # By category
    cursor.execute("""
        SELECT category, COUNT(*)
        FROM wav_files
        WHERE is_original = 0
        GROUP BY category
        ORDER BY COUNT(*) DESC
    """)
    
    for category, count in cursor.fetchall():
        html += f"""
    <div class="category">
        <h3>{category} ({count:,} files)</h3>
        <div class="file-list">"""
        
        cursor.execute("""
            SELECT filename
            FROM wav_files
            WHERE category = ?
            ORDER BY filename
            LIMIT 100
        """, (category,))
        
        for (filename,) in cursor.fetchall():
            html += f'<div class="file-item">📦 {filename}</div>'
        
        if count > 100:
            html += f'<div class="file-item">... and {count - 100} more files</div>'
        
        html += """
        </div>
    </div>"""
    
    html += """
</body>
</html>"""
    
    with open(html_file, 'w') as f:
        f.write(html)
    
    print(f"✓ HTML index created: {html_file}\n")
    conn.close()

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'verify':
        verify_structure()
    elif len(sys.argv) > 1 and sys.argv[1] == 'html':
        create_index_html()
    else:
        print("\n⚠️  WARNING: This will rebuild the entire organized structure!")
        print("Press Enter to continue, or Ctrl+C to cancel...")
        input()
        
        rebuild_structure()
        create_index_html()
        verify_structure()

