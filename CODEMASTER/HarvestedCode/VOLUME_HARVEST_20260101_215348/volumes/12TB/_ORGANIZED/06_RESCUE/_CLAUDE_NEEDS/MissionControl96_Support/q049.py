#!/usr/bin/env python3
"""
NOIZYGENIE: COMPLETE LIBRARY INVENTORY & ACCOUNTING SYSTEM
True accounting of ALL sample libraries, not just Native Instruments
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# Enhanced vendor detection patterns for TRUE ACCOUNTING
COMPREHENSIVE_VENDOR_PATTERNS = {
    # Native Instruments & Kontakt
    "Native Instruments": [
        "native instruments", "kontakt", "komplete", "massive", "reaktor", 
        "absynth", "battery", "maschine", "traktor", "ni_"
    ],
    
    # Major Orchestral Libraries
    "Spitfire Audio": [
        "spitfire", "british", "london", "abbey road", "bbc", "hans zimmer",
        "albion", "studio", "chamber", "symphonic", "strings", "brass"
    ],
    "EastWest": [
        "eastwest", "east west", "ewql", "quantum leap", "play engine",
        "hollywood", "stormdrum", "symphonic", "choirs", "voices"
    ],
    "Vienna Symphonic Library (VSL)": [
        "vsl", "vienna", "vienna symphonic", "vienna instruments", 
        "synchron", "special edition", "solo strings"
    ],
    "ProjectSAM": [
        "project sam", "projectsam", "symphobia", "true strike", 
        "orchestral essentials", "the free orchestra"
    ],
    "CineSamples": [
        "cinesamples", "cinestrings", "cinebrass", "cinewinds", 
        "cineperc", "voxos", "piano in blue"
    ],
    "8Dio": [
        "8dio", "adagio", "lacrimosa", "century", "hybrid", "requiem"
    ],
    "Audio Imperia": [
        "audio imperia", "nucleus", "jaeger", "areia", "talos"
    ],
    "Orchestral Tools": [
        "orchestral tools", "berlin", "metropolis", "ark", "sine"
    ],
    
    # Electronic & Synthesis
    "Output": [
        "output", "analog strings", "rev", "exhale", "signal", "substance",
        "movement", "portal", "thermal"
    ],
    "Native Instruments (Synths)": [
        "zebra", "diva", "repro", "monark", "razor", "reaktor"
    ],
    "Arturia": [
        "arturia", "analog lab", "pigments", "minilab", "keylab"
    ],
    "Roland": [
        "roland", "jupiter", "juno", "tr-", "tb-", "sh-"
    ],
    
    # World & Ethnic Libraries  
    "Best Service": [
        "best service", "ethnoworld", "ethno world", "eduardtaube",
        "forest kingdom", "ancient", "world", "ethnic"
    ],
    "Zero-G": [
        "zero-g", "zerog", "zero_g", "datafile", "ambient", "shamanic",
        "vocal textures", "world vocals", "sacred", "temple"
    ],
    "Impact Soundworks": [
        "impact soundworks", "shreddage", "ventus", "rhapsody", 
        "tokyo scoring", "ethnic"
    ],
    "Soniccouture": [
        "soniccouture", "hang drum", "glass", "bowed", "found sounds",
        "ethnic", "percussion"
    ],
    
    # Guitar & Bass Libraries
    "Orange Tree Samples": [
        "orange tree", "evolution", "strawberry", "mandolin", 
        "guitar", "bass"
    ],
    "Ample Sound": [
        "ample", "guitar", "bass", "agf", "agm", "abf", "abm"
    ],
    "Music Lab": [
        "music lab", "real guitar", "real bass", "real strat"
    ],
    
    # Drum Libraries
    "Toontrack": [
        "toontrack", "superior drummer", "ezdrummer", "ezx", "sdx"
    ],
    "XLN Audio": [
        "xln audio", "addictive drums", "addictive keys", "ad2"
    ],
    "FXpansion": [
        "fxpansion", "bfd", "geist"
    ],
    "Slate Digital": [
        "slate digital", "trigger", "drums"
    ],
    
    # Piano Libraries
    "Synthogy": [
        "synthogy", "ivory", "piano"
    ],
    "Galaxy Instruments": [
        "galaxy", "vintage d", "piano"
    ],
    "Native Instruments (Piano)": [
        "alicia keys", "the gentleman", "the maverick", "noire"
    ],
    
    # Vocal Libraries
    "EastWest (Vocal)": [
        "voices of", "hollywood choirs", "vocal", "choir"
    ],
    "Soundiron": [
        "soundiron", "vocal", "choir", "voice", "mars", "venus"
    ],
    "Strezov Sampling": [
        "strezov", "choir", "vocal", "wotan", "freyja"
    ],
    
    # Indie & Boutique
    "Pianobook": [
        "pianobook", "samples from mars", "spitfire labs"
    ],
    "Splice": [
        "splice", "sounds", "samples", "loops"
    ],
    "Loopmasters": [
        "loopmasters", "loop", "sample"
    ],
    
    # Legacy & Rare
    "Quantum Leap": [
        "quantum leap", "ql", "brass", "rare instruments"
    ],
    "Garritan": [
        "garritan", "personal orchestra", "jazz", "world"
    ],
    "Kirk Hunter": [
        "kirk hunter", "diamond", "solo violin", "string"
    ],
    
    # Free Libraries
    "Spitfire LABS": [
        "labs", "spitfire labs", "free", "amplify"
    ],
    "Versilian Studios": [
        "versilian", "community sample library", "vcsl"
    ]
}

def create_comprehensive_library_scanner():
    """Create a comprehensive library scanner for ALL vendors"""
    scanner_content = f"""#!/usr/bin/env python3
'''
NOIZYGENIE: ULTIMATE LIBRARY INVENTORY SCANNER
Complete accounting of ALL sample libraries across all volumes
'''

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# Comprehensive vendor patterns
VENDOR_PATTERNS = {json.dumps(COMPREHENSIVE_VENDOR_PATTERNS, indent=4)}

def detect_vendor_advanced(item_path: Path) -> str:
    '''Advanced vendor detection using multiple heuristics'''
    item_name = item_path.name.lower()
    parent_path = str(item_path.parent).lower()
    full_path = str(item_path).lower()
    
    # Direct vendor detection
    for vendor, patterns in VENDOR_PATTERNS.items():
        for pattern in patterns:
            if (pattern in item_name or 
                pattern in parent_path or
                pattern in full_path):
                return vendor
    
    # File extension analysis
    if item_path.suffix.lower() in ['.nki', '.nkm', '.nkx']:
        return "Native Instruments (Kontakt)"
    elif item_path.suffix.lower() in ['.exs24', '.exs']:
        return "Apple Logic EXS24"
    elif item_path.suffix.lower() == '.sfz':
        return "SFZ Format"
    elif item_path.suffix.lower() == '.sf2':
        return "SoundFont"
    elif item_path.suffix.lower() == '.gig':
        return "GigaStudio"
    
    # Content analysis for common patterns
    content_indicators = {{
        "orchestral": ["string", "brass", "wood", "percussion", "orchestra", "symphon"],
        "electronic": ["synth", "lead", "pad", "bass", "electronic", "edm"],
        "ethnic": ["world", "ethnic", "traditional", "folk", "tribal"],
        "vocal": ["voice", "vocal", "choir", "sung", "spoken"],
        "guitar": ["guitar", "acoustic", "electric", "strum"],
        "piano": ["piano", "key", "ivory", "grand", "upright"],
        "drum": ["drum", "percussion", "beat", "rhythm", "kit"]
    }}
    
    for category, indicators in content_indicators.items():
        if any(indicator in item_name for indicator in indicators):
            return f"Unknown {{category.title()}} Library"
    
    return "Unknown Vendor"

def scan_volume_comprehensive(volume_path: Path):
    '''Comprehensive scan of a volume for ALL libraries'''
    print(f"🔍 Deep scanning: {{volume_path}}")
    
    inventory = {{
        "volume_path": str(volume_path),
        "scan_timestamp": datetime.now().isoformat(),
        "vendors": defaultdict(list),
        "file_types": Counter(),
        "total_items": 0,
        "library_formats": Counter(),
        "size_analysis": {{}},
        "directory_structure": {{}}
    }}
    
    # Scan everything recursively
    for root, dirs, files in os.walk(volume_path):
        root_path = Path(root)
        
        # Skip system directories
        if any(skip in str(root_path).lower() for skip in 
               ['.trash', 'system volume information', '$recycle.bin', 
                '.spotlight', '.fseventsd', '.temporaryitems']):
            continue
        
        # Analyze directories (potential libraries)
        for dir_name in dirs:
            dir_path = root_path / dir_name
            
            # Skip small directories (likely not libraries)
            try:
                dir_size = sum(f.stat().st_size for f in dir_path.rglob('*') if f.is_file())
                if dir_size < 1024 * 1024:  # Skip < 1MB directories
                    continue
            except:
                continue
            
            vendor = detect_vendor_advanced(dir_path)
            inventory["vendors"][vendor].append({{
                "name": dir_name,
                "path": str(dir_path),
                "type": "directory",
                "size_mb": round(dir_size / (1024 * 1024), 2)
            }})
            inventory["total_items"] += 1
        
        # Analyze files (instruments, samples, etc.)
        for file_name in files:
            file_path = root_path / file_name
            
            # Focus on library-relevant files
            relevant_extensions = {{
                '.nki', '.nkm', '.nkx', '.nks', '.nkc',  # Kontakt
                '.exs24', '.exs',  # Logic EXS24
                '.sfz',  # SFZ
                '.sf2',  # SoundFont
                '.gig',  # GigaStudio
                '.wav', '.aif', '.aiff',  # Audio
                '.rex', '.rx2',  # REX
                '.kontakt', '.monolith'  # Other Kontakt
            }}
            
            if file_path.suffix.lower() in relevant_extensions:
                vendor = detect_vendor_advanced(file_path)
                
                try:
                    file_size = file_path.stat().st_size
                except:
                    file_size = 0
                
                inventory["vendors"][vendor].append({{
                    "name": file_name,
                    "path": str(file_path),
                    "type": "file",
                    "extension": file_path.suffix,
                    "size_mb": round(file_size / (1024 * 1024), 2)
                }})
                
                inventory["file_types"][file_path.suffix.lower()] += 1
                inventory["library_formats"][vendor] += 1
                inventory["total_items"] += 1
    
    return inventory

def generate_ultimate_library_report(inventories):
    '''Generate the ultimate library accounting report'''
    print("\\n🎯 ULTIMATE LIBRARY ACCOUNTING REPORT")
    print("=" * 80)
    
    # Aggregate all vendors across all volumes
    all_vendors = defaultdict(list)
    total_libraries = 0
    total_size_gb = 0
    
    for inventory in inventories:
        for vendor, items in inventory["vendors"].items():
            all_vendors[vendor].extend(items)
            total_libraries += len(items)
            
            for item in items:
                total_size_gb += item.get("size_mb", 0) / 1024
    
    print(f"📊 TOTAL LIBRARIES DISCOVERED: {{total_libraries}}")
    print(f"💾 TOTAL SIZE: {{total_size_gb:.2f}} GB")
    print(f"🏢 UNIQUE VENDORS: {{len(all_vendors)}}")
    print()
    
    # Sort vendors by library count
    sorted_vendors = sorted(all_vendors.items(), 
                          key=lambda x: len(x[1]), reverse=True)
    
    print("🏆 VENDOR BREAKDOWN (Top Libraries):")
    print("-" * 60)
    
    for vendor, items in sorted_vendors[:20]:  # Top 20 vendors
        total_size = sum(item.get("size_mb", 0) for item in items) / 1024
        print(f"📦 {{vendor}}: {{len(items)}} libraries ({{total_size:.1f}} GB)")
        
        # Show top 3 largest libraries for this vendor
        sorted_items = sorted(items, key=lambda x: x.get("size_mb", 0), reverse=True)
        for item in sorted_items[:3]:
            print(f"    └── {{item['name']}} ({{item.get('size_mb', 0):.1f}} MB)")
        
        if len(items) > 3:
            print(f"    └── ... and {{len(items) - 3}} more")
        print()
    
    # Format analysis
    print("\\n🎹 LIBRARY FORMAT ANALYSIS:")
    print("-" * 40)
    
    format_counts = Counter()
    for inventory in inventories:
        format_counts.update(inventory["file_types"])
    
    for ext, count in format_counts.most_common(10):
        print(f"{{ext}}: {{count}} files")
    
    return all_vendors, total_libraries, total_size_gb

def main():
    '''Execute ultimate library inventory across all volumes'''
    print("🧙‍♂️ NOIZYGENIE: ULTIMATE LIBRARY INVENTORY")
    print("🎯 TRUE ACCOUNTING OF ALL SAMPLE LIBRARIES")
    print("=" * 80)
    
    # Volumes to scan
    volumes_to_scan = []
    
    # Add all mounted volumes
    volumes_path = Path("/Volumes")
    if volumes_path.exists():
        for volume in volumes_path.iterdir():
            if volume.is_dir() and not volume.name.startswith('.'):
                volumes_to_scan.append(volume)
    
    # Add user directories
    user_areas = [
        Path.home() / "Music",
        Path.home() / "Documents",
        Path.home() / "Desktop",
        Path("/Library/Audio"),
        Path("/Library/Application Support")
    ]
    
    for area in user_areas:
        if area.exists():
            volumes_to_scan.append(area)
    
    print(f"🔍 Scanning {{len(volumes_to_scan)}} volumes/directories...")
    print()
    
    all_inventories = []
    
    for volume in volumes_to_scan:
        try:
            inventory = scan_volume_comprehensive(volume)
            if inventory["total_items"] > 0:
                all_inventories.append(inventory)
                
                # Save individual volume report
                report_file = Path(f"library_inventory_{{volume.name.replace(' ', '_')}}.json")
                with open(report_file, 'w') as f:
                    json.dump(inventory, f, indent=2, default=str)
                
                print(f"✅ {{volume.name}}: {{inventory['total_items']}} libraries found")
            else:
                print(f"📭 {{volume.name}}: No libraries found")
        
        except Exception as e:
            print(f"❌ Error scanning {{volume}}: {{e}}")
    
    # Generate comprehensive report
    if all_inventories:
        all_vendors, total_libs, total_size = generate_ultimate_library_report(all_inventories)
        
        # Save master report
        master_report = {{
            "scan_timestamp": datetime.now().isoformat(),
            "total_libraries": total_libs,
            "total_size_gb": total_size,
            "unique_vendors": len(all_vendors),
            "vendor_breakdown": {{vendor: len(items) for vendor, items in all_vendors.items()}},
            "detailed_inventory": all_inventories
        }}
        
        master_file = Path("ULTIMATE_LIBRARY_INVENTORY.json")
        with open(master_file, 'w') as f:
            json.dump(master_report, f, indent=2, default=str)
        
        print(f"\\n💾 Master inventory saved: {{master_file}}")
        print("🏆 ULTIMATE LIBRARY ACCOUNTING COMPLETE!")
        
        # Generate human-readable summary
        summary_file = Path("LIBRARY_SUMMARY.txt")
        with open(summary_file, 'w') as f:
            f.write("NOIZYGENIE ULTIMATE LIBRARY INVENTORY SUMMARY\\n")
            f.write("=" * 60 + "\\n\\n")
            f.write(f"Scan Date: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}\\n")
            f.write(f"Total Libraries: {{total_libs}}\\n")
            f.write(f"Total Size: {{total_size:.2f}} GB\\n")
            f.write(f"Unique Vendors: {{len(all_vendors)}}\\n\\n")
            
            f.write("VENDOR BREAKDOWN:\\n")
            f.write("-" * 30 + "\\n")
            
            sorted_vendors = sorted(all_vendors.items(), 
                                  key=lambda x: len(x[1]), reverse=True)
            
            for vendor, items in sorted_vendors:
                vendor_size = sum(item.get("size_mb", 0) for item in items) / 1024
                f.write(f"{{vendor}}: {{len(items)}} libraries ({{vendor_size:.1f}} GB)\\n")
        
        print(f"📄 Human-readable summary: {{summary_file}}")
    
    else:
        print("❌ No libraries found on any volume!")

if __name__ == "__main__":
    main()
"""

    scanner_path = NEW_PROJECT_ROOT / "05_PLUGIN_MANAGEMENT" / "ultimate_library_scanner.py"
    scanner_path.parent.mkdir(parents=True, exist_ok=True)
    scanner_path.write_text(scanner_content)
    os.chmod(scanner_path, 0o755)
    
    return scanner_path

# Enhanced project structure with deep categorization
DEEP_PROJECT_STRUCTURE = {
    "01_ORCHESTRAL_PREMIUM": {
        "description": "Premium orchestral libraries and string sections",
        "patterns": ["ORCHESTRAL", "ACOUSTIC", "Celli", "Violin", "String", "Aleatoric", "Spitfire"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments"]
    },
    "02_ETHNIC_WORLD": {
        "description": "World ethnic instruments and cultural libraries",
        "patterns": ["WORLD_ETHNIC", "ERHU", "CHINA_SETS", "MID_EAST", "BANSURI", "DIGERIDOO", 
                    "CEYLON", "EGYPTIAN", "ALPINE", "GAOHU", "CUMBUS", "TANBUR", "SAZ",
                    "Heart of Asia", "Heart of Africa", "EthnoWorld"],
        "subfolders": ["asian", "middle_eastern", "european", "african", "american"]
    },
    "03_WIND_INSTRUMENTS": {
        "description": "Wind instruments - flutes, whistles, brass",
        "patterns": ["BAWU", "HOTCHIKU", "HULUSI", "KENA", "SHAKUHACHI", "SHAWN", "SHENAI", 
                    "SHENG", "WHISTLE", "CIARAMELLA", "DOUCAINE", "MANCOSEDDA", "SUSATO"],
        "subfolders": ["flutes", "whistles", "reed", "brass_wind", "ethnic_wind"]
    },
    "04_STRING_INSTRUMENTS": {
        "description": "Plucked and bowed string instruments",
        "patterns": ["RENAISSANCE_LUTE", "SAZ", "TIMPLE", "Lutes", "Reeds", "PLECTRUM"],
        "subfolders": ["guitars", "lutes", "exotic_strings", "bowed_strings"]
    },
    "05_ELECTRONIC_SYNTH": {
        "description": "Electronic synthesizers and modern sounds",
        "patterns": ["ELECTRONIC", "SYNTHESIZERS", "Industrial", "Evolve", "FRISKY"],
        "subfolders": ["analog", "digital", "hybrid", "experimental", "industrial"]
    },
    "06_DRUMS_PERCUSSION": {
        "description": "Drums, percussion, and rhythmic elements",
        "patterns": ["DRUMS_PERCUSSION", "CLAPS", "BELLTREE", "CASTANETS", "CUICA", 
                    "TAMBORCITO", "GLASSES"],
        "subfolders": ["acoustic_drums", "electronic_drums", "world_percussion", "fx_percussion"]
    },
    "07_KEYBOARDS_PIANOS": {
        "description": "Keyboard instruments and pianos",
        "patterns": ["Scarbee", "HARMONIUM", "Piano", "Keyboard"],
        "subfolders": ["acoustic_pianos", "electric_pianos", "organs", "vintage_keys"]
    },
    "08_VOCALS_HUMAN": {
        "description": "Vocal libraries and human sounds",
        "patterns": ["VOCALS", "HUMAN_WHISTLING", "Spitfire"],
        "subfolders": ["choirs", "solo_vocals", "vocal_fx", "human_sounds"]
    },
    "09_LOOPS_CONSTRUCTION": {
        "description": "Loops, construction kits, and grooves",
        "patterns": ["LOOPS_GROOVES", "CONSTRUCTION_KITS", "MULTIS", "Discolicks", 
                    "Runs_", "SawTooth", "Wavy", "Slow_"],
        "subfolders": ["tempo_120", "tempo_140", "tempo_100", "arpeggios", "construction"]
    },
    "10_SOUNDSCAPES_FX": {
        "description": "Soundscapes, atmospheres, and sound effects",
        "patterns": ["SOUNDSCAPES_FX", "Quirky", "Cinescapes", "RS_Cinescapes"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts", "ambient"]
    },
    "11_FACTORY_LIBRARIES": {
        "description": "Official Native Instruments and vendor factory content",
        "patterns": ["Kontakt_Factory", "Native_Instruments", "KONTAKT_LAB_2026", "NI2026", 
                    "Best Service", "Engine"],
        "subfolders": ["factory_content", "demos", "presets", "best_service", "third_party"]
    },
    "12_SYSTEM_UTILITIES": {
        "description": "System files, utilities, and maintenance",
        "patterns": ["_FIX", "_NKI", "_Staccato", "_TWEAKABLE", "BACKUP", "Data", 
                    "REPORTS", "PY_Scripts", "TEMP", "SAMPLE_ARCHIVES", "ORGANIZED", 
                    "Auxiliary", "Lite_Patches", "Excerpts", "PROJECT_ORGANIZER"],
        "subfolders": ["scripts", "backups", "temp_files", "utilities", "patches"]
    },
    "13_DOCUMENTATION": {
        "description": "Documentation, logs, and reports",
        "patterns": [".txt", ".html", ".json", "LOG", "MASTER", "REPAIR", "MIGRATION"],
        "subfolders": ["logs", "reports", "manuals", "migration_data"]
    }
}

def organize_kontakt_lab_items():
    """Organize all KONTAKT_LAB items into deep structure with ORPHAN sanctuary"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS...")
    
    organized_count = 0
    collision_count = 0
    orphan_count = 0
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
    # Create NI_2026 ORPHANS folder
    ni_2026_orphans = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    ni_2026_orphans.mkdir(parents=True, exist_ok=True)
    print(f"🏠 Created orphan sanctuary: {ni_2026_orphans}")
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in skip_dirs:
            continue
        
        organized = False
        item_name = item.name
        
        # Find matching category
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern in item_name or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name for p in pattern.split("_"))):
                    
                    # Determine best subfolder with enhanced logic
                    target_subfolder = "general"  # default
                    if category == "02_ETHNIC_WORLD":
                        if any(x in item_name.upper() for x in ["CHINA", "ERHU", "GAOHU"]):
                            target_subfolder = "asian"
                        elif "HEART OF ASIA" in item_name.upper():
                            target_subfolder = "asian"
                        elif any(x in item_name.upper() for x in ["MID_EAST", "EGYPTIAN"]):
                            target_subfolder = "middle_eastern"
                        elif "HEART OF AFRICA" in item_name.upper():
                            target_subfolder = "african"
                        elif "ALPINE" in item_name.upper():
                            target_subfolder = "european"
                        elif "ETHNOWORLD" in item_name.upper():
                            # Determine EthnoWorld specific region if possible
                            if any(x in item_name.upper() for x in ["ASIA", "ORIENT"]):
                                target_subfolder = "asian"
                            elif any(x in item_name.upper() for x in ["AFRICA", "SAHARA"]):
                                target_subfolder = "african"
                            else:
                                target_subfolder = "asian"  # Default for EthnoWorld
                    elif category == "03_WIND_INSTRUMENTS":
                        if "WHISTLE" in item_name.upper():
                            target_subfolder = "whistles"
                        elif any(x in item_name.upper() for x in ["FLUTE", "BAWU", "HULUSI"]):
                            target_subfolder = "flutes"
                    elif category == "09_LOOPS_CONSTRUCTION":
                        if "120" in item_name:
                            target_subfolder = "tempo_120"
                        elif "140" in item_name:
                            target_subfolder = "tempo_140"
                        elif "100" in item_name:
                            target_subfolder = "tempo_100"
                        elif "CONSTRUCTION" in item_name.upper():
                            target_subfolder = "construction"
                    
                    # Use first subfolder if no specific match
                    if target_subfolder == "general":
                        target_subfolder = config["subfolders"][0]
                    
                    target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
                    
                    # Handle name collisions
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
                        
                        # Special notification for Heart collections
                        if "Heart of Asia" in item_name or "Heart of Africa" in item_name:
                            print(f"🌏 HEART COLLECTION: {item_name} → {category}/{target_subfolder}")
                        else:
                            print(f"✅ {item_name} → {category}/{target_subfolder}")
                        organized = True
                        break
                    except Exception as e:
                        print(f"❌ Failed to move {item_name}: {e}")
                
                if organized:
                    break
            
            if organized:
                break
        
        # Move uncategorized items to ORPHANS in NI_2026
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
                # Last resort - try local miscellaneous
                try:
                    misc_path = ORGANIZED_ROOT / "99_MISCELLANEOUS" / item_name
                    shutil.move(str(item), str(misc_path))
                    organized_count += 1
                    print(f"📦 BACKUP: {item_name} → MISCELLANEOUS")
                except Exception as e2:
                    print(f"❌ FINAL FAILURE: {item_name} - {e2}")
    
    return organized_count, collision_count, orphan_count
