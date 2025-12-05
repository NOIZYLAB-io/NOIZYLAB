#!/usr/bin/env python3
"""
ULTIMATE INSTRUMENT PALETTE CREATOR
Scans all volumes for Native Instruments files and creates a massive organized palette for creative work
"""

import os
import shutil
import re
import json
from pathlib import Path
from collections import defaultdict
import time

class InstrumentPaletteCreator:
    def __init__(self):
        self.desktop_path = Path.home() / "Desktop"
        self.kontakt_lab_path = self.desktop_path / "KONTAKT_LAB"
        self.palette_path = self.kontakt_lab_path / "INSTRUMENT_PALETTE"
        
        self.ni_extensions = ['.nki', '.nkm', '.nkc']
        self.instrument_catalog = defaultdict(lambda: defaultdict(list))
        self.total_palette = []
        
        # All your volumes for maximum coverage
        self.scan_volumes = [
            "/Volumes/6TB",
            "/Volumes/4TB BLK", 
            "/Volumes/4TB Lacie",
            "/Volumes/4TB_Utility",
            "/Volumes/4TBSG",
            "/Volumes/12TB",
            "/Volumes/JOE",
            "/Volumes/MAG 4TB",
            "/Volumes/RED DRAGON",
            "/Volumes/SIDNEY"
        ]
        
        # Instrument categories for creative organization
        self.categories = {
            'orchestral': ['orchestra', 'strings', 'violin', 'cello', 'viola', 'bass', 'contrabass', 'brass', 'horn', 'trumpet', 'trombone', 'tuba', 'woodwind', 'flute', 'clarinet', 'oboe', 'bassoon', 'harp', 'timpani'],
            'kirk_hunter': ['kirk', 'hunter'],
            'percussion': ['drums', 'percussion', 'cymbal', 'snare', 'kick', 'tom', 'hihat', 'perc'],
            'piano': ['piano', 'grand', 'upright', 'electric piano', 'rhodes', 'wurlitzer', 'cp80'],
            'synth': ['synth', 'lead', 'pad', 'bass', 'arp', 'sequence', 'analog'],
            'ethnic': ['ethnic', 'world', 'sitar', 'tabla', 'koto', 'gamelan', 'duduk', 'shakuhachi'],
            'choir': ['choir', 'vocal', 'voice', 'soprano', 'alto', 'tenor', 'bass', 'ahh', 'ohh'],
            'guitar': ['guitar', 'acoustic', 'electric', 'bass guitar', 'banjo', 'mandolin', 'ukulele'],
            'organ': ['organ', 'hammond', 'church', 'pipe', 'rotary'],
            'fx': ['fx', 'sound effect', 'ambient', 'texture', 'noise', 'sweep', 'rise']
        }
        
    def create_palette_structure(self):
        """Create the main palette folder structure"""
        self.kontakt_lab_path.mkdir(exist_ok=True)
        self.palette_path.mkdir(exist_ok=True)
        
        # Create category folders
        for category in self.categories.keys():
            (self.palette_path / category.title()).mkdir(exist_ok=True)
        
        print(f"🎨 ULTIMATE INSTRUMENT PALETTE CREATOR")
        print(f"=" * 60)
        print(f"✓ Palette structure ready: {self.palette_path}")
        
    def scan_all_volumes(self):
        """Scan all available volumes for instruments"""
        print(f"\n🔍 SCANNING ALL VOLUMES FOR MASSIVE INSTRUMENT PALETTE...")
        
        available_volumes = [vol for vol in self.scan_volumes if Path(vol).exists()]
        print(f"�� Found {len(available_volumes)} available volumes:")
        for vol in available_volumes:
            print(f"   📀 {vol}")
        
        for volume in available_volumes:
            volume_path = Path(volume)
            print(f"\n📂 Deep scanning: {volume_path.name}")
            self.deep_scan_volume(volume_path)
    
    def deep_scan_volume(self, volume_path):
        """Deep scan a volume for all instrument files"""
        scanned_count = 0
        try:
            for root, dirs, files in os.walk(volume_path):
                # Progress indicator
                scanned_count += 1
                if scanned_count % 1000 == 0:
                    print(f"    🔍 Scanned {scanned_count} directories...")
                
                for file in files:
                    if any(file.lower().endswith(ext) for ext in self.ni_extensions):
                        file_path = Path(root) / file
                        self.catalog_instrument(file_path)
                        
        except (PermissionError, OSError):
            print(f"    ⚠️  Access denied: {volume_path}")
        except Exception as e:
            print(f"    ❌ Error: {e}")
    
    def catalog_instrument(self, file_path):
        """Catalog each instrument and categorize it"""
        file_name = file_path.name.lower()
        path_str = str(file_path).lower()
        
        # Determine category
        categories_found = []
        for category, keywords in self.categories.items():
            if any(keyword in file_name or keyword in path_str for keyword in keywords):
                categories_found.append(category)
        
        # If no specific category found, categorize by location/type
        if not categories_found:
            if 'kontakt factory' in path_str or 'native instruments' in path_str:
                categories_found = ['native_instruments']
            elif 'garritan' in path_str:
                categories_found = ['garritan']
            elif 'heavyocity' in path_str:
                categories_found = ['heavyocity']
            else:
                categories_found = ['uncategorized']
        
        # Add to catalog
        library_name = self.extract_library_name(file_path)
        
        for category in categories_found:
            self.instrument_catalog[category][library_name].append(file_path)
        
        self.total_palette.append({
            'file': file_path,
            'name': file_path.name,
            'library': library_name,
            'categories': categories_found,
            'path': str(file_path)
        })
        
        # Progress with special callouts
        if len(self.total_palette) % 100 == 0:
            print(f"    🎵 Cataloged {len(self.total_palette)} instruments...")
        
        # Special notifications for key finds
        if 'kirk' in path_str and 'hunter' in path_str:
            print(f"    🎼 KIRK HUNTER FOUND: {file_path.name}")
        elif 'heavyocity' in path_str:
            print(f"    🥁 HEAVYOCITY FOUND: {file_path.name}")
    
    def extract_library_name(self, file_path):
        """Extract library name from path"""
        path_parts = file_path.parts
        
        # Look for known library indicators
        for part in reversed(path_parts):
            part_lower = part.lower()
            
            # Check for specific libraries
            if 'kirk' in part_lower and 'hunter' in part_lower:
                return "Kirk_Hunter_Orchestra"
            elif 'heavyocity' in part_lower:
                return "Heavyocity"
            elif 'garritan' in part_lower:
                return "Garritan"
            elif 'kontakt factory' in part_lower:
                return "Kontakt_Factory_Library"
            elif 'native instruments' in part_lower:
                return "Native_Instruments"
            
            # Skip common folder names
            if part_lower in ['kontakt', 'instruments', 'samples', 'libraries', 'library']:
                continue
                
            # Skip UUID-like strings
            if len(part) > 30 and '-' in part:
                continue
                
            if len(part) > 3 and not part.startswith('.'):
                return self.clean_name(part)
        
        return "Unknown_Library"
    
    def clean_name(self, name):
        """Clean up names for folder creation"""
        cleaned = re.sub(r'[^\w\s\-]', '', name)
        cleaned = re.sub(r'\s+', '_', cleaned.strip())
        return cleaned[:50] if cleaned else "Unknown"
    
    def create_massive_palette(self):
        """Create the organized instrument palette"""
        if not self.total_palette:
            print("❌ No instruments found!")
            return
            
        print(f"\n🎨 CREATING MASSIVE INSTRUMENT PALETTE...")
        print(f"📊 Total instruments found: {len(self.total_palette)}")
        
        # Show category breakdown
        category_counts = defaultdict(int)
        for instrument in self.total_palette:
            for category in instrument['categories']:
                category_counts[category] += 1
        
        print(f"\n📈 MASSIVE PALETTE BREAKDOWN:")
        for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            if category == 'kirk_hunter':
                print(f"  🎼 {category.title()}: {count} instruments ⭐")
            elif count > 50:
                print(f"  🎵 {category.title()}: {count} instruments 🔥")
            else:
                print(f"  🎵 {category.title()}: {count} instruments")
        
        # Organize files into palette
        moved_count = 0
        
        for category, libraries in self.instrument_catalog.items():
            category_folder = self.palette_path / category.title()
            category_folder.mkdir(exist_ok=True)
            
            total_in_category = sum(len(files) for files in libraries.values())
            print(f"\n🎨 Creating {category.title()} palette ({total_in_category} instruments)...")
            
            for library_name, files in libraries.items():
                library_folder = category_folder / library_name
                library_folder.mkdir(exist_ok=True)
                
                for file_path in files:
                    try:
                        dest_path = library_folder / file_path.name
                        
                        # Handle duplicates
                        counter = 1
                        original_dest = dest_path
                        while dest_path.exists():
                            stem = original_dest.stem
                            suffix = original_dest.suffix
                            dest_path = library_folder / f"{stem}_{counter}{suffix}"
                            counter += 1
                        
                        # Copy to palette
                        shutil.copy2(file_path, dest_path)
                        moved_count += 1
                        
                    except Exception as e:
                        print(f"    ❌ Error adding {file_path.name}: {e}")
        
        print(f"\n🎉 MASSIVE PALETTE CREATION COMPLETE!")
        print(f"   🎵 Total instruments in palette: {moved_count}")
        print(f"   📁 Categories created: {len(category_counts)}")
        print(f"   📍 Palette location: {self.palette_path}")
        
        return moved_count > 0
    
    def create_palette_catalog(self):
        """Create comprehensive catalog files"""
        print(f"\n📋 Creating comprehensive palette documentation...")
        
        # Quick reference by category
        quick_ref_file = self.palette_path / "PALETTE_OVERVIEW.txt"
        with open(quick_ref_file, 'w') as f:
            f.write("🎨 ULTIMATE INSTRUMENT PALETTE OVERVIEW\n")
            f.write("=" * 60 + "\n")
            f.write(f"Created: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Instruments: {len(self.total_palette)}\n\n")
            
            f.write("PALETTE CATEGORIES:\n")
            for category in sorted(self.instrument_catalog.keys()):
                count = sum(len(files) for files in self.instrument_catalog[category].values())
                libraries = len(self.instrument_catalog[category])
                if category == 'kirk_hunter':
                    f.write(f"🎼 {category.title()}: {count} instruments from {libraries} libraries ⭐\n")
                else:
                    f.write(f"🎵 {category.title()}: {count} instruments from {libraries} libraries\n")
            
            f.write(f"\n💡 CREATIVE TIPS:\n")
            f.write(f"- Each category folder contains organized libraries\n")
            f.write(f"- Mix instruments from different categories for unique sounds\n")
            f.write(f"- Kirk Hunter Orchestra provides premium orchestral colors\n")
            f.write(f"- Use the palette as your creative starting point\n")
        
        print(f"   ✓ Palette Overview: {quick_ref_file}")
    
    def run(self):
        """Execute the complete palette creation"""
        self.create_palette_structure()
        self.scan_all_volumes()
        success = self.create_massive_palette()
        
        if success:
            self.create_palette_catalog()
            
            # Open the palette
            print(f"\n🚀 Opening massive instrument palette...")
            os.system(f'open "{self.palette_path}"')
            
            print(f"\n✨ MASSIVE INSTRUMENT PALETTE READY!")
            print(f"🎨 You now have {len(self.total_palette)} instruments organized for creative work")
            print(f"🎵 Ready to paint with an incredible palette of sounds!")
        
        return success

# Execute the palette creator
if __name__ == "__main__":
    creator = InstrumentPaletteCreator()
    creator.run()
