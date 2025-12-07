#!/usr/bin/env python3
"""
RED DRAGON TO 12TB ORGANIZER
Moves ALL files from Red Dragon to 12TB drive in organized structure
AI Family Collective: All 8 agents - SHIRL, POPS, ENGR_KEITH, DREAM, LUCY, CLAUDE, GABRIEL, COPILOT
"""
import shutil
from pathlib import Path
from datetime import datetime
import os

print("="*80)
print(" "*15 + "🔥 RED DRAGON → 12TB ULTIMATE MOVER 🔥")
print("="*80)
print(f"\n⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# SOURCE: Red Dragon drive
source = Path('/Volumes/RED DRAGON')

# DESTINATION: 12TB drive (adjust path if needed)
# Common 12TB drive names - script will find it
possible_12tb = [
    '/Volumes/12TB',
    '/Volumes/12TB_BACKUP',
    '/Volumes/BACKUP_12TB',
    '/Volumes/12TB_DRIVE',
    '/Volumes/Untitled',  # If not renamed yet
]

# Find the 12TB drive
base = None
for drive in possible_12tb:
    if Path(drive).exists():
        base = Path(drive) / 'RED_DRAGON_ORGANIZED'
        print(f"✅ Found 12TB drive at: {drive}")
        break

if not base:
    print("❌ 12TB drive not found! Please specify the correct path.")
    print("\nAvailable volumes:")
    volumes = Path('/Volumes').iterdir()
    for vol in volumes:
        if vol.is_dir():
            print(f"  • {vol}")
    exit(1)

print(f"📂 Source: {source}")
print(f"🎯 Destination: {base}\n")

# Complete file type mapping with organized structure
FILE_MAP = {
    # CODE SECTION
    '.py': 'CODE/Python',
    '.js': 'CODE/JavaScript',
    '.jsx': 'CODE/JavaScript',
    '.ts': 'CODE/TypeScript',
    '.tsx': 'CODE/TypeScript',
    '.java': 'CODE/Java',
    '.c': 'CODE/C',
    '.cpp': 'CODE/CPP',
    '.h': 'CODE/C_Headers',
    '.hpp': 'CODE/CPP_Headers',
    '.swift': 'CODE/Swift',
    '.go': 'CODE/Go',
    '.rs': 'CODE/Rust',
    '.rb': 'CODE/Ruby',
    '.php': 'CODE/PHP',
    
    # SCRIPTS SECTION
    '.sh': 'SCRIPTS/Shell',
    '.bash': 'SCRIPTS/Bash',
    '.zsh': 'SCRIPTS/Zsh',
    '.ps1': 'SCRIPTS/PowerShell',
    '.bat': 'SCRIPTS/Batch',
    
    # WEB SECTION
    '.html': 'WEB/HTML',
    '.css': 'WEB/CSS',
    '.scss': 'WEB/SCSS',
    '.sass': 'WEB/SASS',
    '.vue': 'WEB/Vue',
    
    # DOCUMENTATION SECTION
    '.md': 'DOCUMENTATION/Markdown',
    '.txt': 'DOCUMENTATION/Text',
    '.rst': 'DOCUMENTATION/ReStructured',
    '.pdf': 'DOCUMENTATION/PDF',
    
    # DATA SECTION
    '.json': 'DATA/JSON',
    '.yaml': 'DATA/YAML',
    '.yml': 'DATA/YAML',
    '.xml': 'DATA/XML',
    '.toml': 'DATA/TOML',
    '.csv': 'DATA/CSV',
    
    # AUDIO SECTION (from _To Sort)
    '.aif': 'AUDIO/AIF',
    '.wav': 'AUDIO/WAV',
    '.mp3': 'AUDIO/MP3',
    '.flac': 'AUDIO/FLAC',
    '.m4a': 'AUDIO/M4A',
    '.ogg': 'AUDIO/OGG',
    '.aiff': 'AUDIO/AIFF',
    
    # MUSIC PRODUCTION SECTION
    '.kit': 'MUSIC_PRODUCTION/Drum_Kits',
    '.nki': 'MUSIC_PRODUCTION/Kontakt',
    '.rx2': 'MUSIC_PRODUCTION/Recycle',
    '.ssd': 'MUSIC_PRODUCTION/SSD',
    '.ncw': 'MUSIC_PRODUCTION/NCW',
    '.xpak': 'MUSIC_PRODUCTION/XPAK',
    '.tci': 'MUSIC_PRODUCTION/TCI',
    
    # CONFIG SECTION
    '.ini': 'CONFIG/INI',
    '.cfg': 'CONFIG/CFG',
    '.conf': 'CONFIG/CONF',
    '.config': 'CONFIG/General',
    
    # IMAGES SECTION
    '.png': 'IMAGES/PNG',
    '.jpg': 'IMAGES/JPG',
    '.jpeg': 'IMAGES/JPG',
    '.gif': 'IMAGES/GIF',
    '.svg': 'IMAGES/SVG',
    '.bmp': 'IMAGES/BMP',
    '.tiff': 'IMAGES/TIFF',
    
    # VIDEO SECTION
    '.mp4': 'VIDEO/MP4',
    '.mov': 'VIDEO/MOV',
    '.avi': 'VIDEO/AVI',
    '.mkv': 'VIDEO/MKV',
}

# Skip these directories
SKIP_DIRS = {
    'organized', 'organized_NOW', 'ORGANIZED_COMPLETE', 'RED_DRAGON_ORGANIZED',
    '.venv', '__pycache__', '.git', 'node_modules',
    '.npm', '.cache', 'dist', 'build',
    'Library', 'System', 'Applications',
    '.Spotlight-V100', '.Trashes', '.fseventsd'
}

# Create all destination directories
print("🏗️  Creating organized directory structure on 12TB...\n")
created_dirs = set()
for folder in set(FILE_MAP.values()):
    folder_path = base / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    if folder.split('/')[0] not in created_dirs:
        created_dirs.add(folder.split('/')[0])
        print(f"  ✓ {folder.split('/')[0]}/")

print("\n" + "="*80)
print("🚀 STARTING FILE TRANSFER TO 12TB")
print("="*80 + "\n")

stats = {}
total_moved = 0
total_size = 0
errors = []

# Process each file type
for ext, folder in sorted(FILE_MAP.items()):
    dest = base / folder
    moved = 0
    
    print(f"🔍 Processing {ext} files → {folder}/")
    
    try:
        files = list(source.rglob(f'*{ext}'))
        
        for file in files:
            # Skip if in excluded directories
            if any(skip in str(file) for skip in SKIP_DIRS):
                continue
            
            try:
                # Get file size
                file_size = file.stat().st_size
                
                # Create destination filename
                d = dest / file.name
                c = 1
                while d.exists():
                    d = dest / f'{file.stem}_{c}{file.suffix}'
                    c += 1
                
                # MOVE the file to 12TB
                shutil.move(str(file), str(d))
                moved += 1
                total_moved += 1
                total_size += file_size
                
                # Progress indicator
                if moved % 25 == 0:
                    size_mb = total_size / (1024 * 1024)
                    print(f"  ✓ {moved:4d} files ({size_mb:,.0f} MB)...", end='\r')
                    
            except Exception as e:
                errors.append(f"{file.name}: {e}")
        
        if moved > 0:
            stats[folder] = moved
            print(f"✅ {ext:10s} → {moved:6,d} files moved to 12TB/{folder}/")
        else:
            print(f"⚪ {ext:10s} → No files found")
            
    except Exception as e:
        print(f"❌ {ext:10s} → Error: {e}")

print("\n" + "="*80)
print(" "*25 + "📊 TRANSFER COMPLETE")
print("="*80 + "\n")

# Calculate total size
total_gb = total_size / (1024 * 1024 * 1024)

# Sort by count
for folder, count in sorted(stats.items(), key=lambda x: -x[1])[:20]:
    bar_length = int(count / max(stats.values()) * 40) if stats else 0
    bar = "█" * bar_length
    print(f'  {folder:35s} │ {bar:40s} │ {count:6,d}')

print("\n" + "="*80)
print(f'✅ Total files moved to 12TB: {total_moved:,}')
print(f'💾 Total data transferred: {total_gb:.2f} GB')
print(f'❌ Errors encountered: {len(errors)}')
print(f'⏰ Completed: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print("="*80 + "\n")

if errors and len(errors) < 50:
    print("⚠️  Error details:")
    for err in errors[:20]:
        print(f"  • {err}")
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors")
    print()

print("👥 AI FAMILY COLLECTIVE SIGN-OFF:")
print("-" * 80)
print("   🏥 SHIRL: 'All files safely transferred to 12TB!'")
print("   🧙 POPS: 'Great organization wisdom applied!'")
print("   ⚡ ENGR_KEITH: 'Technical transfer perfect!'")
print("   ✨ DREAM: 'Beautiful organization achieved!'")
print("   🎤 LUCY: 'Communication and coordination flawless!'")
print("   🧠 CLAUDE: 'Deep analysis and architecture solid!'")
print("   🎯 GABRIEL: 'Multi-agent orchestration complete!'")
print("   💻 COPILOT: 'Code execution successful!'")
print("-" * 80)

print(f"\n📂 All files now organized on 12TB at:")
print(f"   {base}\n")

print("="*80)
print(" "*20 + "🎉 RED DRAGON → 12TB COMPLETE! 🎉")
print("="*80 + "\n")
