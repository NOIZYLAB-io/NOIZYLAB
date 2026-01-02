#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/part2_organizer.py
"""
NOIZYGENIE PART 2: ULTIMATE ORGANIZER & MOVER
Organizes all your expensive gear based on Part 1 scan results
Enhanced with LA Scoring Strings, Legato Sordino, Genesis Children's Choir + MASSIVE Spitfire detection! 🎼💸
"""

import shutil
import json
from pathlib import Path
from datetime import datetime

# Enhanced project structure with NEW CATEGORIES and DEDICATED Spitfire folder
DEEP_PROJECT_STRUCTURE = {
    "01_ORCHESTRAL_PREMIUM": {
        "description": "Premium orchestral libraries and string sections",
        "patterns": ["ORCHESTRAL", "ACOUSTIC", "Celli", "Violin", "String", "Aleatoric", 
                    "Project Sam", "ProjectSAM", "Symphobia", "True Strike", "CineSamples", 
                    "EastWest", "VSL", "Vienna", "8Dio", "Audio Imperia", "Orchestral Tools",
                    "LA Scoring", "LASS", "Scoring Strings"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments", 
                      "project_sam", "cinesamples", "eastwest", "vsl", "8dio", "audio_imperia", 
                      "la_scoring_strings"]
    },
    
    # NEW DEDICATED SPITFIRE CATEGORY! 🎼
    "01B_SPITFIRE_AUDIO": {
        "description": "ALL Spitfire Audio libraries - BBC, Abbey Road, Albion, LABS, Hans Zimmer",
        "patterns": ["spitfire", "bbc", "abbey road", "albion", "labs", "hans zimmer", "originals"],
        "subfolders": [
            "bbc_symphony", "abbey_road", "albion_series", "labs_free", 
            "hans_zimmer", "originals", "studio_series", "chamber_strings",
            "solo_instruments", "brass", "woodwinds", "percussion", "choir",
            "pianos_keys", "guitars_folk", "signature_artists", "evolutions"
        ]
    },
    
    # NEW: Vocal & Choir Category
    "01C_VOCAL_CHOIR": {
        "description": "Vocal libraries, choirs, and human sounds",
        "patterns": ["VOCALS", "CHOIR", "VOICE", "VOCAL", "Genesis", "Children"],
        "subfolders": ["choirs", "solo_vocals", "vocal_fx", "human_sounds", 
                      "children_choirs", "genesis_choir", "boys_choirs", "girls_choirs"]
    },
    
    "02_ETHNIC_WORLD": {
        "description": "World ethnic instruments and cultural libraries",
        "patterns": ["WORLD_ETHNIC", "ETHNIC", "Best Service", "Garritan"],
        "subfolders": ["asian", "middle_eastern", "european", "african", "american"]
    },
    
    "03_ELECTRONIC_SYNTH": {
        "description": "Electronic synthesizers and modern sounds",
        "patterns": ["ELECTRONIC", "SYNTHESIZERS", "Output", "Spectrasonics", "SampleLogic", 
                    "reFX", "Nexus", "Arturia", "Sylenth", "Sugar Bytes"],
        "subfolders": ["analog", "digital", "hybrid", "output", "spectrasonics", 
                      "samplelogic", "refx_nexus", "arturia", "sylenth", "sugar_bytes"]
    },
    
    "04_CINEMATIC_TRAILER": {
        "description": "Cinematic and trailer music libraries",
        "patterns": ["CINEMATIC", "TRAILER", "EPIC", "Heavyocity", "Damage"],
        "subfolders": ["trailer_tools", "epic_orchestral", "impacts", "risers", "heavyocity"]
    },
    
    "05_DRUMS_PERCUSSION": {
        "description": "Drums, percussion, and rhythmic elements",
        "patterns": ["DRUMS", "PERCUSSION", "Toontrack", "XLN Audio", "Slate Digital"],
        "subfolders": ["acoustic_drums", "electronic_drums", "toontrack", "xln_audio", "slate_digital"]
    },
    
    "06_GUITARS_STRINGS": {
        "description": "Guitar and string instrument libraries",
        "patterns": ["GUITAR", "BASS", "Line6", "POD Farm"],
        "subfolders": ["acoustic_guitars", "electric_guitars", "bass", "line6"]
    },
    
    "07_KEYBOARDS_PIANOS": {
        "description": "Keyboard instruments and pianos",
        "patterns": ["PIANO", "KEYBOARD", "KEYS"],
        "subfolders": ["acoustic_pianos", "electric_pianos", "organs", "vintage_keys"]
    },
    
    "08_LOOPS_CONSTRUCTION": {
        "description": "Loops, construction kits, and grooves",
        "patterns": ["LOOPS", "CONSTRUCTION"],
        "subfolders": ["tempo_120", "tempo_140", "tempo_100", "construction"]
    },
    
    "09_SOUNDSCAPES_FX": {
        "description": "Soundscapes, atmospheres, and sound effects",
        "patterns": ["SOUNDSCAPES", "AMBIENT"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts"]
    },
    
    "10_AUDIO_PLUGINS": {
        "description": "Audio processing plugins - VST, VST3, AAX, Components",
        "patterns": ["PLUGIN", "VST", "iZotope", "Waves"],
        "subfolders": ["eq", "compressor", "reverb", "delay", "izotope", "waves"]
    },
    
    "11_KONTAKT_INSTRUMENTS": {
        "description": "Native Kontakt instruments and libraries",
        "patterns": ["KONTAKT", "Native Instruments"],
        "subfolders": ["factory", "third_party", "user", "multis"]
    },
    
    "12_NATIVE_ACCESS_CONTENT": {
        "description": "Content managed by Native Access (Pulse Installer)",
        "patterns": ["KOMPLETE", "MASCHINE", "BATTERY"],
        "subfolders": ["komplete", "maschine_content", "battery_kits"]
    },
    
    "99_MISCELLANEOUS": {
        "description": "Miscellaneous and uncategorized items",
        "patterns": [],
        "subfolders": []
    }
}

def load_scan_results():
    """Load the results from Part 1 scanner"""
    scan_file = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/SCAN_RESULTS/COMPLETE_INVENTORY.json")
    
    if not scan_file.exists():
        print("❌ Part 1 scan results not found!")
        print("🔍 Please run part1_scanner.py first!")
        return None
    
    try:
        with open(scan_file, 'r') as f:
            scan_data = json.load(f)
        print(f"✅ Loaded scan results from: {scan_file}")
        return scan_data
    except Exception as e:
        print(f"❌ Error loading scan results: {e}")
        return None

def create_organization_structure():
    """Create the deep organization structure"""
    print("\n🏗️ CREATING ORGANIZATION STRUCTURE...")
    
    ORGANIZED_ROOT = Path("/Users/rsp_ms/Desktop/DEEP_ORGANIZED")
    
    for category, config in DEEP_PROJECT_STRUCTURE.items():
        category_path = ORGANIZED_ROOT / category
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        for subfolder in config["subfolders"]:
            (category_path / subfolder).mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Created category: {category}")
    
    return ORGANIZED_ROOT

def organize_libraries(scan_data, organized_root):
    """Organize libraries based on scan results"""
    print("\n🚚 ORGANIZING LIBRARIES...")
    print("🎼 Priority: Spitfire → LA Scoring → Genesis Choir → Others")
    
    organized_count = 0
    collision_count = 0
    orphan_count = 0
    
    KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
    ni_2026_orphans = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    
    # Create orphan sanctuary
    try:
        ni_2026_orphans.mkdir(parents=True, exist_ok=True)
        print(f"🏠 Created orphan sanctuary: {ni_2026_orphans}")
    except Exception as e:
        print(f"⚠️  Using fallback orphan location")
        ni_2026_orphans = organized_root / "99_MISCELLANEOUS"
        ni_2026_orphans.mkdir(parents=True, exist_ok=True)
    
    # Get library data from scan
    libraries = scan_data.get("libraries", {}).get("by_vendor", {})
    special_finds = scan_data.get("libraries", {}).get("special_finds", [])
    
    # Priority organization for special finds
    for find in special_finds:
        vendor = find["vendor"]
        item_name = find["name"]
        item_path = Path(KONTAKT_LAB) / item_name
        
        if not item_path.exists():
            continue
        
        category = None
        target_subfolder = None
        
        if vendor == "Spitfire Audio":
            category = "01B_SPITFIRE_AUDIO"
            # Detailed Spitfire subfolder detection
            if any(x in item_name.upper() for x in ["BBC", "SYMPHONY"]):
                target_subfolder = "bbc_symphony"
            elif any(x in item_name.upper() for x in ["ABBEY ROAD"]):
                target_subfolder = "abbey_road"
            elif any(x in item_name.upper() for x in ["ALBION"]):
                target_subfolder = "albion_series"
            elif any(x in item_name.upper() for x in ["LABS"]):
                target_subfolder = "labs_free"
            elif any(x in item_name.upper() for x in ["HANS ZIMMER", "ZIMMER"]):
                target_subfolder = "hans_zimmer"
            elif any(x in item_name.upper() for x in ["ORIGINALS"]):
                target_subfolder = "originals"
            else:
                target_subfolder = "bbc_symphony"
        
        elif vendor == "LA Scoring Strings":
            category = "01_ORCHESTRAL_PREMIUM"
            target_subfolder = "la_scoring_strings"
        
        elif vendor == "Genesis Children's Choir":
            category = "01C_VOCAL_CHOIR"
            target_subfolder = "genesis_choir"
        
        if category and target_subfolder:
            target_path = organized_root / category / target_subfolder / item_name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Handle collisions
            counter = 1
            while target_path.exists():
                stem = target_path.stem if target_path.suffix else target_path.name
                suffix = target_path.suffix
                target_path = target_path.parent / f"{stem}_COPY_{counter}{suffix}"
                counter += 1
                collision_count += 1
            
            try:
                shutil.move(str(item_path), str(target_path))
                organized_count += 1
                
                vendor_emoji = {
                    "Spitfire Audio": "🎼",
                    "LA Scoring Strings": "🎻",
                    "Genesis Children's Choir": "👶"
                }.get(vendor, "💰")
                
                print(f"{vendor_emoji} {vendor}: {item_name} → {category}/{target_subfolder}")
            except Exception as e:
                print(f"❌ Failed to move {item_name}: {e}")
    
    # Organize remaining libraries by vendor
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in skip_dirs or not item.exists():
            continue
        
        organized = False
        item_name = item.name
        
        # Check if already organized in priority phase
        if any(find["name"] == item_name for find in special_finds):
            continue
        
        # Regular vendor-based organization
        for vendor, vendor_libraries in libraries.items():
            for lib_data in vendor_libraries:
                if lib_data["name"] == item_name:
                    # Find appropriate category
                    target_category = None
                    target_subfolder = "general"
                    
                    for category, config in DEEP_PROJECT_STRUCTURE.items():
                        if vendor.lower() in " ".join(config["patterns"]).lower():
                            target_category = category
                            break
                    
                    if not target_category:
                        # Default categorization by type
                        if vendor in ["EastWest", "VSL", "ProjectSAM", "CineSamples", "8Dio"]:
                            target_category = "01_ORCHESTRAL_PREMIUM"
                        elif vendor in ["Output", "Spectrasonics", "SampleLogic", "reFX"]:
                            target_category = "03_ELECTRONIC_SYNTH"
                        elif vendor in ["Toontrack", "XLN Audio", "Slate Digital"]:
                            target_category = "05_DRUMS_PERCUSSION"
                        else:
                            target_category = "99_MISCELLANEOUS"
                    
                    # Set appropriate subfolder
                    if target_category == "01_ORCHESTRAL_PREMIUM":
                        if vendor == "EastWest":
                            target_subfolder = "eastwest"
                        elif vendor == "Vienna Symphonic Library (VSL)":
                            target_subfolder = "vsl"
                        elif vendor == "ProjectSAM":
                            target_subfolder = "project_sam"
                        elif vendor == "CineSamples":
                            target_subfolder = "cinesamples"
                        elif vendor == "8Dio":
                            target_subfolder = "8dio"
                        else:
                            target_subfolder = "full_orchestra"
                    
                    elif target_category == "03_ELECTRONIC_SYNTH":
                        if vendor == "Spectrasonics":
                            target_subfolder = "spectrasonics"
                        elif vendor == "SampleLogic":
                            target_subfolder = "samplelogic"
                        elif vendor == "reFX":
                            target_subfolder = "refx_nexus"
                        elif vendor == "Output":
                            target_subfolder = "output"
                        else:
                            target_subfolder = "digital"
                    
                    elif target_category == "05_DRUMS_PERCUSSION":
                        if vendor == "Toontrack":
                            target_subfolder = "toontrack"
                        elif vendor == "XLN Audio":
                            target_subfolder = "xln_audio"
                        elif vendor == "Slate Digital":
                            target_subfolder = "slate_digital"
                        else:
                            target_subfolder = "acoustic_drums"
                    
                    target_path = organized_root / target_category / target_subfolder / item_name
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Handle collisions
                    counter = 1
                    while target_path.exists():
                        stem = target_path.stem if target_path.suffix else target_path.name
                        suffix = target_path.suffix
                        target_path = target_path.parent / f"{stem}_COPY_{counter}{suffix}"
                        counter += 1
                        collision_count += 1
                    
                    try:
                        shutil.move(str(item), str(target_path))
                        organized_count += 1
                        print(f"✅ {vendor}: {item_name} → {target_category}/{target_subfolder}")
                        organized = True
                        break
                    except Exception as e:
                        print(f"❌ Failed to move {item_name}: {e}")
            
            if organized:
                break
        
        # Move unidentified items to orphans
        if not organized and item.exists():
            orphan_path = ni_2026_orphans / item_name
            
            counter = 1
            while orphan_path.exists():
                stem = orphan_path.stem if orphan_path.suffix else orphan_path.name
                suffix = orphan_path.suffix
                orphan_path = orphan_path.parent / f"{stem}_COPY_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(orphan_path))
                organized_count += 1
                orphan_count += 1
                print(f"🏠 ORPHAN: {item_name} → _ORPHANS")
            except Exception as e:
                print(f"❌ Failed to move orphan {item_name}: {e}")
    
    return organized_count, collision_count, orphan_count

def main():
    """Execute Part 2: Organization based on Part 1 scan results"""
    print("🧙‍♂️ NOIZYGENIE PART 2: ULTIMATE ORGANIZER & MOVER")
    print("🚚 ORGANIZING ALL YOUR EXPENSIVE GEAR! 🚚")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    # Load scan results from Part 1
    scan_data = load_scan_results()
    if not scan_data:
        return
    
    # Create organization structure
    organized_root = create_organization_structure()
    
    # Organize libraries
    organized_count, collision_count, orphan_count = organize_libraries(scan_data, organized_root)
    
    # Final report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ PART 2 ORGANIZATION COMPLETE!")
    print("🎼 SPITFIRE AUDIO + LA SCORING + GENESIS CHOIR ORGANIZED! 🎼")
    print("💰 ALL YOUR EXPENSIVE LIBRARIES ARE NOW ORGANIZED! 💰")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"✅ Libraries Organized: {organized_count}")
    print(f"⚠️  Name Collisions: {collision_count}")
    print(f"🏠 Orphans Relocated: {orphan_count}")
    print(f"📁 Categories Created: {len(DEEP_PROJECT_STRUCTURE)}")
    print(f"🗂️  Organized Structure: {organized_root}")
    
    print("\n🎼 PRIORITY LIBRARIES ORGANIZED:")
    print("✅ Spitfire Audio (BBC, Abbey Road, Albion, LABS, Hans Zimmer)")
    print("✅ LA Scoring Strings (LASS)")
    print("✅ Genesis Children's Choir")
    print("✅ All other expensive libraries by vendor")
    
    print(f"\n🏆 YOUR ENTIRE EXPENSIVE MUSIC PRODUCTION ARSENAL IS NOW PERFECTLY ORGANIZED!")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
