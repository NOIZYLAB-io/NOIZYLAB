#!/usr/bin/env python3
"""
🎵 MUSIC vs SFX SCANNER - Intelligent Categorization!
Separates music tracks from sound effects automatically!
MAXIMUM VELOCITY!
"""

import os
from pathlib import Path
import json

# Read all found audio
with open('/tmp/all_audio.txt', 'r') as f:
    all_audio = [line.strip() for line in f if line.strip()]

print(f"🔍 Analyzing {len(all_audio)} audio files...")
print()

# Categorize
music_tracks = []
sfx_samples = []
unknown = []

SFX_KEYWORDS = ['sfx', 'sound effect', 'fx', 'sample', 'one shot', 'loop', 
                'kick', 'snare', 'hihat', 'clap', 'percussion', 'foley',
                'ambience', 'atmosphere', 'texture', 'riser', 'impact',
                'transition', 'whoosh', 'sweep', 'vinyl', 'noise']

MUSIC_KEYWORDS = ['song', 'track', 'mix', 'master', 'final', 'version',
                  'vocal', 'instrumental', 'demo', 'rough', 'stereo',
                  'bounce', 'export', 'album', 'single', 'ep']

for audio_file in all_audio:
    path_lower = audio_file.lower()
    filename = Path(audio_file).name.lower()
    parent = Path(audio_file).parent.name.lower()
    
    # Check for SFX indicators
    is_sfx = any(kw in path_lower for kw in SFX_KEYWORDS)
    
    # Check for music indicators
    is_music = any(kw in path_lower for kw in MUSIC_KEYWORDS)
    
    # Additional heuristics
    if 'library' in path_lower or 'samples' in path_lower:
        is_sfx = True
    if 'design' in path_lower or 'by song' in path_lower:
        is_music = True
    
    # Categorize
    if is_music and not is_sfx:
        music_tracks.append(audio_file)
    elif is_sfx and not is_music:
        sfx_samples.append(audio_file)
    elif is_music and is_sfx:
        # Both indicators - check file size
        try:
            size = Path(audio_file).stat().st_size
            if size > 5_000_000:  # > 5 MB = likely music
                music_tracks.append(audio_file)
            else:
                sfx_samples.append(audio_file)
        except:
            unknown.append(audio_file)
    else:
        unknown.append(audio_file)

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  ✅ CATEGORIZATION COMPLETE!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print(f"🎵 MUSIC TRACKS: {len(music_tracks)}")
print(f"🔊 SFX/SAMPLES: {len(sfx_samples)}")
print(f"❓ UNKNOWN: {len(unknown)}")
print()

# Save categorized lists
with open('/tmp/music_tracks.txt', 'w') as f:
    f.write('\n'.join(music_tracks))

with open('/tmp/sfx_samples.txt', 'w') as f:
    f.write('\n'.join(sfx_samples))

with open('/tmp/unknown_audio.txt', 'w') as f:
    f.write('\n'.join(unknown))

# Save catalog
catalog = {
    'total_audio': len(all_audio),
    'music_tracks': len(music_tracks),
    'sfx_samples': len(sfx_samples),
    'unknown': len(unknown),
    'scanned_volumes': [
        '/Volumes/SIDNEY',
        '/Volumes/4TB Lacie',
        '/Volumes/6TB',
        '/Volumes/4TBSG',
        '/Volumes/MAG 4TB'
    ]
}

with open('/Volumes/6TB/FISH_MUSIC_MASTER_LIBRARY/COMPLETE_CATALOG.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("📋 Results saved:")
print("   /tmp/music_tracks.txt")
print("   /tmp/sfx_samples.txt")
print("   /tmp/unknown_audio.txt")
print("   /Volumes/6TB/FISH_MUSIC_MASTER_LIBRARY/COMPLETE_CATALOG.json")
print()
print("🎯 YOUR MUSIC CATALOG IS READY!")
print()

# Show some examples
print("🎵 Sample Music Tracks:")
for track in music_tracks[:10]:
    print(f"   {Path(track).name}")

print()
print("🔊 Sample SFX:")
for sfx in sfx_samples[:10]:
    print(f"   {Path(sfx).name}")

print()
print("✅ COMPLETE! Your music is cataloged and ready!")
print()
print("🚀 Next: Select best tracks for release!")
print("💜 GORUNFREE!")

