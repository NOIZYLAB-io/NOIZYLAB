#!/usr/bin/env python3
"""
REALTIME MONITOR - Live Organization Dashboard
Monitor your library organization in real-time with live updates
"""

import os
import time
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

PRIMARY = Path("/Volumes/6TB")
SECONDARY = Path("/Volumes/4TBSG")

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def format_size(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def get_drive_stats(drive_path):
    """Get drive statistics"""
    try:
        stat = os.statvfs(drive_path)
        total = stat.f_blocks * stat.f_frsize
        used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
        free = stat.f_bavail * stat.f_frsize
        return {
            'total': total,
            'used': used,
            'free': free,
            'percent': (used / total * 100) if total > 0 else 0
        }
    except:
        return None

def count_directory_files(directory):
    """Quick count of files in directory"""
    try:
        count = 0
        for root, dirs, files in os.walk(directory):
            if root.endswith('_Samples'):  # Skip sample subdirs for speed
                continue
            count += len([f for f in files if not f.startswith('.')])
            if count > 10000:  # Quick estimate
                return f"{count//1000}K+"
        return f"{count:,}"
    except:
        return "?"

def monitor_loop():
    """Main monitoring loop"""
    
    while True:
        clear_screen()
        
        print("╔" + "═"*76 + "╗")
        print("║" + " "*24 + "REALTIME LIBRARY MONITOR" + " "*28 + "║")
        print("╚" + "═"*76 + "╝")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n⏰ {timestamp}")
        
        # Drive statistics
        print("\n" + "━"*78)
        print("💾 DRIVE STATUS")
        print("━"*78)
        
        for drive_name, drive_path in [("6TB", PRIMARY), ("4TBSG", SECONDARY)]:
            stats = get_drive_stats(drive_path)
            if stats:
                bar_width = 40
                used_bars = int((stats['percent'] / 100) * bar_width)
                bar = "█" * used_bars + "░" * (bar_width - used_bars)
                
                print(f"\n{drive_name}:")
                print(f"  {bar} {stats['percent']:.1f}%")
                print(f"  Used: {format_size(stats['used'])} / {format_size(stats['total'])}")
                print(f"  Free: {format_size(stats['free'])}")
        
        # Library structure status
        print("\n" + "━"*78)
        print("📁 LIBRARY STRUCTURE STATUS")
        print("━"*78)
        
        structures = {
            "KONTAKT_LIBRARIES": PRIMARY / "KONTAKT_LIBRARIES",
            "AUDIO_SAMPLES": PRIMARY / "AUDIO_SAMPLES",
            "PLUGIN_PRESETS": PRIMARY / "PLUGIN_PRESETS",
            "SAMPLER_INSTRUMENTS": PRIMARY / "SAMPLER_INSTRUMENTS",
            "PROJECTS": SECONDARY / "PROJECTS",
            "INSTALLERS": SECONDARY / "INSTALLERS",
            "DOCUMENTATION": SECONDARY / "DOCUMENTATION",
        }
        
        for name, path in structures.items():
            if path.exists():
                file_count = count_directory_files(path)
                status = "✅"
                print(f"{status} {name:25} {file_count:>8} files")
            else:
                print(f"❌ {name:25} {'NOT FOUND':>8}")
        
        # Old directories to organize
        print("\n" + "━"*78)
        print("⏳ DIRECTORIES TO ORGANIZE")
        print("━"*78)
        
        old_dirs = {
            "KTK 2026 TO SORT": SECONDARY / "KTK 2026 TO SORT",
            "KONTAKT_LAB": PRIMARY / "KONTAKT_LAB",
            "WAVE_MASTER": PRIMARY / "WAVE_MASTER",
            "EXS24_MASTER": PRIMARY / "EXS24_MASTER",
        }
        
        for name, path in old_dirs.items():
            if path.exists():
                file_count = count_directory_files(path)
                print(f"⏳ {name:25} {file_count:>8} files")
            else:
                print(f"✅ {name:25} {'ORGANIZED':>8}")
        
        # Quick stats
        print("\n" + "━"*78)
        print("📊 QUICK STATS")
        print("━"*78)
        
        total_kontakt = count_directory_files(PRIMARY / "KONTAKT_LIBRARIES") if (PRIMARY / "KONTAKT_LIBRARIES").exists() else "0"
        total_audio = count_directory_files(PRIMARY / "AUDIO_SAMPLES") if (PRIMARY / "AUDIO_SAMPLES").exists() else "0"
        total_old = count_directory_files(SECONDARY / "KTK 2026 TO SORT") if (SECONDARY / "KTK 2026 TO SORT").exists() else "0"
        
        print(f"  Kontakt Libraries Organized: {total_kontakt}")
        print(f"  Audio Samples Organized: {total_audio}")
        print(f"  Files Still To Sort: {total_old}")
        
        print("\n" + "━"*78)
        print("Press Ctrl+C to exit | Updates every 5 seconds")
        print("━"*78)
        
        time.sleep(5)

if __name__ == "__main__":
    try:
        print("\n🎯 Starting Real-Time Monitor...")
        print("This will update every 5 seconds\n")
        time.sleep(2)
        monitor_loop()
    except KeyboardInterrupt:
        print("\n\n✅ Monitor stopped")

