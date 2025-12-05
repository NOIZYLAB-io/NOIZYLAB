#!/usr/bin/env python3
"""
FACTORY ORGANIZER - Professional Library Rebuild System
Reorganize entire multi-drive setup to pristine factory state
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# DRIVE CONFIGURATION
PRIMARY_DRIVE = Path("/Volumes/6TB")
SECONDARY_DRIVE = Path("/Volumes/4TBSG")

# FACTORY ORGANIZATION STRUCTURE
FACTORY_STRUCTURE = {
    "KONTAKT_LIBRARIES": {
        "path": PRIMARY_DRIVE / "KONTAKT_LIBRARIES",
        "types": ['.nki', '.nkm', '.nkc', '.nkr', '.ncw', '.nkx'],
        "subdirs": {
            "Orchestral": ["string", "brass", "woodwind", "orchestra", "symphonic"],
            "Cinematic": ["cinematic", "epic", "trailer", "score", "film"],
            "Ethnic_World": ["ethnic", "world", "exotic", "tribal", "global"],
            "Percussion": ["percussion", "drum", "cymbal", "perc", "rhythmic"],
            "Keys_Mallets": ["piano", "keys", "marimba", "xylophone", "vibes", "bells"],
            "Guitars_Bass": ["guitar", "bass", "acoustic", "electric"],
            "Vocals_Choir": ["vocal", "voice", "choir", "vox"],
            "Synths_Pads": ["synth", "pad", "lead", "ambient", "texture"],
            "Effects_SFX": ["sfx", "effect", "sound design", "fx"],
        }
    },
    
    "AUDIO_SAMPLES": {
        "path": PRIMARY_DRIVE / "AUDIO_SAMPLES",
        "types": ['.wav', '.aif', '.aiff', '.flac', '.mp3'],
        "subdirs": {
            "Drums": ["drum", "kick", "snare", "hat", "clap", "perc"],
            "Bass": ["bass", "sub", "808", "low"],
            "Loops": ["loop", "beat", "groove", "rhyth"],
            "Melody": ["melody", "melodic", "lead", "riff"],
            "Vocal_Samples": ["vocal", "vox", "acapella", "speech"],
            "FX_Samples": ["fx", "effect", "transition", "impact", "sweep"],
            "Foley": ["foley", "ambience", "atmosphere", "environment"],
            "Music_Loops": ["music", "musical", "composition"],
        }
    },
    
    "PLUGIN_PRESETS": {
        "path": PRIMARY_DRIVE / "PLUGIN_PRESETS",
        "types": ['.fxp', '.fxb', '.nka', '.nksn', '.vstpreset'],
        "subdirs": {
            "Synths": ["sylenth", "serum", "massive", "nexus", "omnisphere"],
            "Effects": ["reverb", "delay", "compressor", "eq", "distortion"],
            "Samplers": ["kontakt", "battery", "machine"],
        }
    },
    
    "SAMPLER_INSTRUMENTS": {
        "path": PRIMARY_DRIVE / "SAMPLER_INSTRUMENTS",
        "types": ['.exs', '.sfz', '.sxt', '.gig', '.sf2'],
        "subdirs": {
            "EXS24": ['.exs'],
            "SFZ": ['.sfz'],
            "Halion": ['.sxt'],
            "GigaStudio": ['.gig'],
            "SoundFonts": ['.sf2'],
        }
    },
    
    "PROJECTS": {
        "path": SECONDARY_DRIVE / "PROJECTS",
        "types": ['.ptx', '.logic', '.als', '.flp', '.cpr'],
        "subdirs": {
            "ProTools": ['.ptx'],
            "Logic": ['.logic'],
            "Ableton": ['.als'],
            "FL_Studio": ['.flp'],
            "Cubase": ['.cpr'],
        }
    },
    
    "INSTALLERS": {
        "path": SECONDARY_DRIVE / "INSTALLERS",
        "types": ['.dmg', '.pkg', '.zip', '.rar', '.iso'],
        "subdirs": {
            "Plugins": ["vst", "au", "aax", "plugin"],
            "DAW": ["protools", "logic", "ableton", "cubase", "fl studio"],
            "Libraries": ["kontakt", "library", "expansion"],
            "Utilities": ["utility", "tool", "helper"],
        }
    },
    
    "DOCUMENTATION": {
        "path": SECONDARY_DRIVE / "DOCUMENTATION",
        "types": ['.pdf', '.txt', '.doc', '.docx', '.rtf'],
        "subdirs": {
            "Manuals": ["manual", "guide", "instruction"],
            "Licenses": ["license", "serial", "key"],
            "ReadMe": ["readme", "read me", "info"],
        }
    },
}

# VENDOR MAPPINGS
KNOWN_VENDORS = {
    "Native Instruments": ["native instruments", "ni_", "kontakt", "massive", "battery"],
    "Spitfire Audio": ["spitfire", "spitfire audio"],
    "8Dio": ["8dio"],
    "ProjectSam": ["projectsam", "project sam"],
    "EastWest": ["eastwest", "east west", "ew_"],
    "Heavyocity": ["heavyocity"],
    "Output": ["output"],
    "Soundiron": ["soundiron"],
    "Audiobro": ["audiobro"],
    "CineSamples": ["cinesamples", "cine samples"],
    "Big Fish Audio": ["big fish", "bigfish"],
    "Samples From Mars": ["samples from mars", "mars"],
    "Toontrack": ["toontrack", "superior drummer", "ezdrummer"],
    "XLN Audio": ["xln", "addictive drums"],
    "Spectrasonics": ["spectrasonics", "omnisphere", "trilian"],
    "Arturia": ["arturia"],
    "reFX": ["refx", "nexus"],
    "Vengeance": ["vengeance"],
    "Splice": ["splice"],
}

class FactoryOrganizer:
    def __init__(self):
        self.file_moves = []
        self.stats = defaultdict(int)
        self.errors = []
        
    def detect_vendor(self, filepath):
        """Detect vendor from filepath"""
        path_lower = str(filepath).lower()
        
        for vendor, keywords in KNOWN_VENDORS.items():
            if any(kw in path_lower for kw in keywords):
                return vendor
        
        return "Other"
    
    def detect_category(self, filepath, filename):
        """Intelligently detect file category"""
        path_lower = str(filepath).lower()
        name_lower = filename.lower()
        ext = os.path.splitext(filename)[1].lower()
        
        # Match against factory structure
        for category, config in FACTORY_STRUCTURE.items():
            if ext in config['types']:
                # Find best subcategory
                for subdir, keywords in config.get('subdirs', {}).items():
                    if any(kw in path_lower or kw in name_lower for kw in keywords):
                        return category, subdir
                
                return category, "Uncategorized"
        
        return "OTHER", "Misc"
    
    def get_organized_path(self, filepath):
        """Determine where file should be organized to"""
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()
        
        # Detect category and subcategory
        category, subcategory = self.detect_category(filepath, filename)
        
        if category == "OTHER":
            return None
        
        # Get base path for this category
        config = FACTORY_STRUCTURE.get(category, {})
        base_path = config.get('path')
        
        if not base_path:
            return None
        
        # Detect vendor
        vendor = self.detect_vendor(filepath)
        
        # Build organized path
        if vendor != "Other":
            organized_path = base_path / vendor / subcategory / filename
        else:
            organized_path = base_path / subcategory / filename
        
        return organized_path
    
    def scan_and_plan(self, source_dirs):
        """Scan directories and plan organization"""
        print("\n" + "="*70)
        print("🔍 SCANNING & PLANNING ORGANIZATION")
        print("="*70 + "\n")
        
        all_files = []
        
        for source_dir in source_dirs:
            if not source_dir.exists():
                print(f"⚠️  Skipping {source_dir} (not found)")
                continue
            
            print(f"📂 Scanning: {source_dir}")
            
            for root, dirs, files in os.walk(source_dir):
                # Skip hidden and system directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and 
                          d not in ['System', 'Library', '.Spotlight-V100', '.Trashes']]
                
                for filename in files:
                    if filename.startswith('.'):
                        continue
                    
                    filepath = Path(root) / filename
                    all_files.append(filepath)
        
        print(f"\n✓ Found {len(all_files):,} files to organize\n")
        
        # Plan moves
        print("🎯 Planning organization...")
        
        for filepath in all_files:
            try:
                new_path = self.get_organized_path(filepath)
                
                if new_path and new_path != filepath:
                    self.file_moves.append({
                        'from': str(filepath),
                        'to': str(new_path),
                        'size': os.path.getsize(filepath)
                    })
                    
                    # Update stats
                    category = new_path.parts[3] if len(new_path.parts) > 3 else "Unknown"
                    self.stats[category] += 1
                    
            except Exception as e:
                self.errors.append({'file': str(filepath), 'error': str(e)})
        
        print(f"✓ Planned {len(self.file_moves):,} file moves")
        print(f"⚠️  {len(self.errors)} errors")
        
        return self.file_moves
    
    def create_factory_structure(self):
        """Create the factory directory structure"""
        print("\n" + "="*70)
        print("🏗️  CREATING FACTORY STRUCTURE")
        print("="*70 + "\n")
        
        for category, config in FACTORY_STRUCTURE.items():
            base_path = config['path']
            
            print(f"📁 Creating: {category}")
            print(f"   Location: {base_path}")
            
            # Create base directory
            base_path.mkdir(parents=True, exist_ok=True)
            
            # Create subdirectories
            for subdir in config.get('subdirs', {}).keys():
                subdir_path = base_path / subdir
                subdir_path.mkdir(parents=True, exist_ok=True)
                print(f"   ✓ {subdir}")
        
        print("\n✓ Factory structure created!")
    
    def execute_organization(self, dry_run=True):
        """Execute the file organization"""
        print("\n" + "="*70)
        if dry_run:
            print("🔄 DRY RUN - PREVIEW MODE")
        else:
            print("🔄 EXECUTING ORGANIZATION")
        print("="*70 + "\n")
        
        if dry_run:
            print("⚠️  This is a DRY RUN - no files will be moved")
            print("Set dry_run=False to actually move files\n")
        
        moved = 0
        failed = 0
        
        # Show sample moves
        print("📋 Sample moves (first 20):\n")
        for i, move in enumerate(self.file_moves[:20], 1):
            print(f"{i}. {Path(move['from']).name}")
            print(f"   FROM: {move['from']}")
            print(f"   TO:   {move['to']}\n")
        
        if len(self.file_moves) > 20:
            print(f"... and {len(self.file_moves) - 20} more files\n")
        
        if not dry_run:
            print("🚀 Moving files...")
            
            for i, move in enumerate(self.file_moves, 1):
                try:
                    src = Path(move['from'])
                    dst = Path(move['to'])
                    
                    # Create destination directory
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Move file
                    shutil.move(str(src), str(dst))
                    moved += 1
                    
                    if i % 100 == 0:
                        print(f"  Progress: {i}/{len(self.file_moves)} ({i/len(self.file_moves)*100:.1f}%)")
                    
                except Exception as e:
                    failed += 1
                    self.errors.append({'move': move, 'error': str(e)})
        
        print("\n" + "="*70)
        print("📊 ORGANIZATION SUMMARY")
        print("="*70)
        print(f"Total files to organize: {len(self.file_moves):,}")
        
        if not dry_run:
            print(f"Successfully moved: {moved:,}")
            print(f"Failed: {failed:,}")
        
        print("\n📂 Files by category:")
        for category, count in sorted(self.stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {category:30} {count:>8,} files")

def format_size(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def main():
    print("\n" + "🏭"*35)
    print("  FACTORY ORGANIZER - Professional Library Rebuild")
    print("🏭"*35 + "\n")
    
    print("Target Drives:")
    print(f"  PRIMARY:   {PRIMARY_DRIVE} (Kontakt, Samples, Presets)")
    print(f"  SECONDARY: {SECONDARY_DRIVE} (Projects, Installers, Docs)")
    
    print("\n📋 Factory Structure Categories:")
    for category in FACTORY_STRUCTURE.keys():
        print(f"  ✓ {category}")
    
    print("\n⚠️  WARNING: This will reorganize your entire library!")
    print("Make sure you have backups before proceeding.\n")
    
    # Create organizer
    organizer = FactoryOrganizer()
    
    # Create factory structure
    organizer.create_factory_structure()
    
    # Scan and plan
    sources = [
        PRIMARY_DRIVE / "KONTAKT_LAB",
        PRIMARY_DRIVE / "Native_Instruments_2026",
        PRIMARY_DRIVE / "EXS24_MASTER",
        PRIMARY_DRIVE / "WAVE_MASTER",
        SECONDARY_DRIVE / "KTK 2026 TO SORT",
        SECONDARY_DRIVE / "2026_SFX",
    ]
    
    print("\n📂 Source directories to organize:")
    for src in sources:
        if src.exists():
            print(f"  ✓ {src}")
        else:
            print(f"  ⚠️  {src} (not found)")
    
    input("\nPress Enter to scan and plan organization...")
    
    organizer.scan_and_plan(sources)
    
    # Execute in dry-run mode
    organizer.execute_organization(dry_run=True)
    
    print("\n" + "="*70)
    print("✅ PLANNING COMPLETE!")
    print("="*70)
    print("\nTo actually execute the organization:")
    print("1. BACKUP your drives first!")
    print("2. Edit this script and set dry_run=False")
    print("3. Run again")
    print("\n💡 Review the planned moves above before proceeding!")

if __name__ == "__main__":
    main()

