#!/usr/bin/env python3
"""
🎹 NOIZYGENIE Advanced Library Organizer
Smart organization system for KONTAKT libraries
"""

import os
import shutil
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Configuration
ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
ORGANIZED_LIBS_DIR = ROOT / "ORGANIZED_LIBRARIES"
BACKUP_DIR = ROOT / "BACKUP"

# Category mappings with intelligent keywords
CATEGORY_MAPPING = {
    "01_ELECTRONIC": {
        "keywords": ["electronic", "edm", "techno", "house", "trance", "electro", "synth", "digital", "cyber", "future"],
        "subcategories": ["BASS", "LEADS", "PADS", "DRUMS", "FX", "ARPEGGIOS"]
    },
    "02_ORCHESTRAL": {
        "keywords": ["orchestra", "symphonic", "classical", "strings", "brass", "woodwind", "timpani", "harp", "violin", "cello", "trumpet", "flute"],
        "subcategories": ["STRINGS", "BRASS", "WOODWINDS", "PERCUSSION", "CHOIR", "ENSEMBLES"]
    },
    "03_ACOUSTIC": {
        "keywords": ["acoustic", "piano", "guitar", "organ", "folk", "natural", "unplugged", "live"],
        "subcategories": ["PIANO", "GUITAR", "ORGAN", "ETHNIC", "MALLETS", "PLUCKED"]
    },
    "04_URBAN": {
        "keywords": ["urban", "hip hop", "rap", "trap", "rnb", "soul", "funk", "street"],
        "subcategories": ["DRUMS", "BASS", "KEYS", "VOCAL", "BRASS", "GUITAR"]
    },
    "05_ROCK_POP": {
        "keywords": ["rock", "pop", "metal", "punk", "indie", "alternative", "grunge", "blues"],
        "subcategories": ["GUITAR", "BASS", "DRUMS", "KEYS", "VOCAL", "EFFECTS"]
    },
    "06_WORLD_ETHNIC": {
        "keywords": ["world", "ethnic", "traditional", "folk", "tribal", "cultural", "native", "indigenous"],
        "subcategories": ["ASIAN", "AFRICAN", "MIDDLE_EASTERN", "LATIN", "EUROPEAN", "NATIVE"]
    },
    "07_SYNTHESIZERS": {
        "keywords": ["synthesizer", "moog", "analog", "vintage", "retro", "classic", "modular"],
        "subcategories": ["ANALOG", "DIGITAL", "WAVETABLE", "VINTAGE", "MODERN", "MODULAR"]
    },
    "08_DRUMS_PERCUSSION": {
        "keywords": ["drums", "percussion", "beats", "rhythm", "kit", "snare", "kick", "cymbal"],
        "subcategories": ["ACOUSTIC_KITS", "ELECTRONIC", "ETHNIC_PERC", "ORCHESTRAL", "LOOPS", "ONE_SHOTS"]
    },
    "09_LOOPS_GROOVES": {
        "keywords": ["loop", "groove", "cycle", "pattern", "sequence", "repetitive"],
        "subcategories": ["DRUM_LOOPS", "BASS_LOOPS", "MELODIC", "CHORD", "RHYTHMIC", "FULL_MIX"]
    },
    "10_SOUNDSCAPES_FX": {
        "keywords": ["soundscape", "ambient", "atmosphere", "texture", "fx", "effect", "cinematic", "film"],
        "subcategories": ["AMBIENT", "RISERS", "IMPACTS", "TRANSITIONS", "TEXTURES", "ATMOSPHERES"]
    },
    "11_VOCALS": {
        "keywords": ["vocal", "voice", "singer", "choir", "chant", "human", "spoken"],
        "subcategories": ["LEAD_VOCALS", "BACKING", "CHOIR", "SPOKEN", "PROCESSED", "ETHNIC"]
    },
    "12_CONSTRUCTION_KITS": {
        "keywords": ["construction", "kit", "complete", "full", "project", "song", "track"],
        "subcategories": ["ELECTRONIC", "HIP_HOP", "ROCK", "POP", "CINEMATIC", "WORLD"]
    },
    "13_MULTIS_COMBIS": {
        "keywords": ["multi", "combi", "layer", "split", "complex", "performance"],
        "subcategories": ["LAYERED", "SPLIT", "PERFORMANCE", "COMPLEX", "SIMPLE", "SPECIALTY"]
    }
}

def get_unorganized_libraries():
    """Get all libraries that aren't in organized categories"""
    all_items = []
    for item in ROOT.iterdir():
        if (item.is_dir() and 
            not item.name.startswith('.') and 
            not item.name.startswith('_') and
            not re.match(r'^\d{2}_', item.name) and
            item.name not in ['REPORTS', 'BACKUP', 'ORGANIZED_LIBRARIES', 'TEMP_PROCESSING', 'SAMPLE_ARCHIVES']):
            all_items.append(item.name)
    return sorted(all_items)

def categorize_library(lib_name):
    """Intelligently categorize a library based on its name"""
    lib_lower = lib_name.lower()
    
    scores = {}
    for category, info in CATEGORY_MAPPING.items():
        score = 0
        for keyword in info["keywords"]:
            if keyword in lib_lower:
                score += 1
        scores[category] = score
    
    # Find best match
    if scores:
        best_category = max(scores.items(), key=lambda x: x[1])
        if best_category[1] > 0:
            return best_category[0]
    
    return None

def smart_organize():
    """Smart organization with user interaction"""
    print("🎹 NOIZYGENIE Advanced Library Organizer")
    print("=" * 50)
    
    unorganized = get_unorganized_libraries()
    
    if not unorganized:
        print("✅ All libraries are already organized!")
        return
    
    print(f"📚 Found {len(unorganized)} unorganized libraries")
    print("\n🤖 Analyzing libraries for smart categorization...")
    
    suggestions = {}
    for lib in unorganized:
        category = categorize_library(lib)
        if category:
            if category not in suggestions:
                suggestions[category] = []
            suggestions[category].append(lib)
    
    print(f"\n📊 Smart Analysis Results:")
    print(f"   Categorizable: {sum(len(libs) for libs in suggestions.values())}")
    print(f"   Need Manual Review: {len(unorganized) - sum(len(libs) for libs in suggestions.values())}")
    
    return suggestions, unorganized

def show_organization_preview():
    """Show what the organization would look like"""
    suggestions, unorganized = smart_organize()
    
    print("\n📋 ORGANIZATION PREVIEW:")
    print("=" * 30)
    
    for category, libs in suggestions.items():
        category_name = category.replace("_", " ").title()
        print(f"\n{category_name}:")
        for lib in libs[:5]:  # Show first 5
            print(f"   → {lib}")
        if len(libs) > 5:
            print(f"   ... and {len(libs) - 5} more")
    
    # Show unmatched
    unmatched = [lib for lib in unorganized if not any(lib in libs for libs in suggestions.values())]
    if unmatched:
        print(f"\n❓ NEEDS MANUAL REVIEW ({len(unmatched)}):")
        for lib in unmatched[:10]:
            print(f"   ? {lib}")
        if len(unmatched) > 10:
            print(f"   ... and {len(unmatched) - 10} more")

if __name__ == "__main__":
    show_organization_preview()