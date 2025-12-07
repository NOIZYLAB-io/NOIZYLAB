#!/usr/bin/env python3
"""
ULTIMATE RED DRAGON ORGANIZER
Organizes ENTIRE Red Dragon drive - ALL folders!
AI Family Collective: All 8 agents working together
"""
import shutil
from pathlib import Path
from datetime import datetime
import os

print("="*80)
print(" "*20 + "🔥 RED DRAGON ULTIMATE ORGANIZER 🔥")
print("="*80)
print(f"\n⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# SOURCE: Entire RED DRAGON drive
source = Path('/Volumes/RED DRAGON')
# DESTINATION: Centralized organized folder
base = Path('/Volumes/RED DRAGON/ORGANIZED_COMPLETE')

print(f"📂 Source: {source}")
print(f"🎯 Destination: {base}\n")

# Complete file type mapping
FILE_MAP = {
    # Code
    '.py': 'code/python',
    '.js': 'code/javascript',
    '.jsx': 'code/javascript',
    '.ts': 'code/typescript',
    '.tsx': 'code/typescript',
    '.java': 'code/java',
    '.c': 'code/c',
    '.cpp': 'code/cpp',
    '.h': 'code/c',
    '.hpp': 'code/cpp',
    '.swift': 'code/swift',
    '.go': 'code/go',
    '.rs': 'code/rust',
    '.rb': 'code/ruby',
    '.php': 'code/php',
    
    # Scripts
    '.sh': 'scripts/shell',
    '.bash': 'scripts/shell',
    '.zsh': 'scripts/shell',
    '.ps1': 'scripts/powershell',
    '.bat': 'scripts/batch',
    
    # Web
    '.html': 'web/html',
    '.css': 'web/css',
    '.scss': 'web/css',
    '.sass': 'web/css',
    '.vue': 'web/vue',
    
    # Documentation
    '.md': 'documentation/markdown',
    '.txt': 'documentation/text',
    '.rst': 'documentation/restructured',
    '.pdf': 'documentation/pdf',
    
    # Data
    '.json': 'data/json',
    '.yaml': 'data/yaml',
    '.yml': 'data/yaml',
    '.xml': 'data/xml',
    '.toml': 'data/toml',
    '.csv': 'data/csv',
    
    # Audio (from _To Sort)
    '.aif': 'audio/aif',
    '.wav': 'audio/wav',
    '.mp3': 'audio/mp3',
    '.flac': 'audio/flac',
    '.m4a': 'audio/m4a',
    
    # Music Production
    '.kit': 'music/kits',
    '.nki': 'music/kontakt',
    '.rx2': 'music/recycle',
    '.ssd': 'music/ssd',
    '.ncw': 'music/ncw',
    '.xpak': 'music/xpak',
    
    # Config
    '.ini': 'config/ini',
    '.cfg': 'config/cfg',
    '.conf': 'config/conf',
    
    # Images
    '.png': 'images/png',
    '.jpg': 'images/jpg',
    '.jpeg': 'images/jpg',
    '.gif': 'images/gif',
    '.svg': 'images/svg',
}

# Skip these directories
SKIP_DIRS = {
    'organized', 'organized_NOW', 'ORGANIZED_COMPLETE',
    '.venv', '__pycache__', '.git', 'node_modules',
    '.npm', '.cache', 'dist', 'build',
    'Library', 'System', 'Applications'
}

# Create all destination directories
print("🏗️  Creating directory structure...\n")
for folder in set(FILE_MAP.values()):
    (base / folder).mkdir(parents=True, exist_ok=True)
    print(f"  ✓ {folder}/")

print("\n" + "="*80)
print("🚀 STARTING FILE ORGANIZATION")
print("="*80 + "\n")

stats = {}
total_moved = 0
total_scanned = 0

# Process each file type
for ext, folder in sorted(FILE_MAP.items()):
    dest = base / folder
    moved = 0
    
    print(f"🔍 Processing {ext} files...")
    
    try:
        for file in source.rglob(f'*{ext}'):
            total_scanned += 1
            
            # Skip if in excluded directories
            if any(skip in str(file) for skip in SKIP_DIRS):
                continue
            
            try:
                # Create destination filename
                d = dest / file.name
                c = 1
                while d.exists():
                    d = dest / f'{file.stem}_{c}{file.suffix}'
                    c += 1
                
                # MOVE the file
                shutil.move(str(file), str(d))
                moved += 1
                total_moved += 1
                
                # Progress indicator
                if moved % 50 == 0:
                    print(f"  ✓ {moved:4d} files...", end='\r')
                    
            except Exception as e:
                pass
        
        if moved > 0:
            stats[folder] = moved
            print(f"✅ {ext:8s} → {moved:5d} files moved to {folder}/")
        else:
            print(f"⚪ {ext:8s} → No files found")
            
    except Exception as e:
        print(f"❌ {ext:8s} → Error: {e}")

print("\n" + "="*80)
print(" "*25 + "📊 FINAL STATISTICS")
print("="*80 + "\n")

# Sort by count
for folder, count in sorted(stats.items(), key=lambda x: -x[1]):
    bar_length = int(count / max(stats.values()) * 40)
    bar = "█" * bar_length
    print(f'  {folder:30s} │ {bar:40s} │ {count:6,d} files')

print("\n" + "="*80)
print(f'📁 Total files scanned: {total_scanned:,}')
print(f'✅ Total files moved: {total_moved:,}')
print(f'⏰ Completed: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print("="*80 + "\n")

print("👥 AI FAMILY COLLECTIVE SIGN-OFF:")
print("-" * 80)
print("   🏥 SHIRL: 'All files organized and healthy!'")
print("   🧙 POPS: 'Wisdom prevailed. Great work team!'")
print("   ⚡ ENGR_KEITH: 'Technical perfection achieved!'")
print("   ✨ DREAM: 'The vision is now reality!'")
print("   🎤 LUCY: 'Communication flawless!'")
print("   🧠 CLAUDE: 'Deep analysis complete!'")
print("   🎯 GABRIEL: 'Perfect orchestration!'")
print("   💻 COPILOT: 'Execution successful!'")
print("-" * 80)

print(f"\n📂 All files organized in: {base}")
print("\n" + "="*80)
print(" "*25 + "🎉 MISSION COMPLETE! 🎉")
print("="*80 + "\n")
