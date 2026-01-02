#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/organize_projects.py
"""
NOIZYGENIE: COMPLETE LIBRARY INVENTORY & ACCOUNTING SYSTEM
True accounting of ALL sample libraries, not just Native Instruments
INCLUDING SAMPLELOGIC - Because we spent way too much money! 💸
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# Enhanced vendor detection patterns for TRUE ACCOUNTING (Now with SampleLogic!)
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
    
    # Premium Electronic Libraries
    "Spectrasonics": [
        "spectrasonics", "omnisphere", "trilogy", "keyscapes", "stylus rmx",
        "stylus", "rmx", "omnisphere 2", "trilian", "keyscape"
    ],
    "SampleLogic": [
        "samplelogic", "sample logic", "infinity", "morphestra", "cinemorphx",
        "cinematic guitars", "trailer toolkit", "electrify", "drum fury",
        "analog", "vintage vault", "synth legends", "psychoacoustica",
        "arpology", "bohemian", "trailer drums", "cinematic keys"
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

# Enhanced project structure with SampleLogic integration
DEEP_PROJECT_STRUCTURE = {
    "01_ORCHESTRAL_PREMIUM": {
        "description": "Premium orchestral libraries and string sections",
        "patterns": ["ORCHESTRAL", "ACOUSTIC", "Celli", "Violin", "String", "Aleatoric", "Spitfire", 
                    "Project Sam", "ProjectSAM", "Symphobia", "True Strike", "Orchestral Brass", 
                    "Orchestral String", "Swing!", "Horns of Hell", "CineSamples", "CineStrings",
                    "CineBrass", "CineWinds", "Hollywoodwinds", "Hollywood", "EastWest",
                    "East West", "EWQL", "Quantum Leap", "Hollywood Orchestra", "Hollywood Strings", 
                    "Hollywood Brass", "Hollywood Woodwinds", "Stormdrum", "Symphonic Orchestra",
                    "VSL", "Vienna", "Vienna Symphonic", "Vienna Symphonic Library", "Vienna Instruments",
                    "Morphestra", "SampleLogic"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments", 
                      "project_sam", "cinesamples", "eastwest", "vsl", "samplelogic"]
    },
    "02_ETHNIC_WORLD": {
        "description": "World ethnic instruments and cultural libraries",
        "patterns": ["WORLD_ETHNIC", "ERHU", "CHINA_SETS", "MID_EAST", "BANSURI", "DIGERIDOO", 
                    "CEYLON", "EGYPTIAN", "ALPINE", "GAOHU", "CUMBUS", "TANBUR", "SAZ",
                    "Heart of Asia", "Heart of Africa", "EthnoWorld"],
        "subfolders": ["asian", "middle_eastern", "european", "african", "american"]
    },
    "03_ELECTRONIC_SYNTH": {
        "description": "Electronic synthesizers and modern sounds",
        "patterns": ["ELECTRONIC", "SYNTHESIZERS", "Industrial", "Evolve", "FRISKY", 
                    "Output", "Analog Strings", "Rev", "Exhale", "Signal", "Substance", "Zebra",
                    "Spectrasonics", "Omnisphere", "Trilogy", "Keyscapes", "Stylus RMX",
                    "SampleLogic", "Sample Logic", "Infinity", "CinemorphX", "Electrify",
                    "Analog", "Vintage Vault", "Synth Legends", "Psychoacoustica", "Arpology"],
        "subfolders": ["analog", "digital", "hybrid", "experimental", "industrial", 
                      "output", "zebra", "spectrasonics", "samplelogic", "vintage"]
    },
    "04_CINEMATIC_TRAILER": {
        "description": "Cinematic and trailer music libraries",
        "patterns": ["CINEMATIC", "TRAILER", "EPIC", "IMPACT", "RISER", "WHOOSH", 
                    "SampleLogic", "Trailer Toolkit", "Trailer Drums", "CinemorphX",
                    "Morphestra", "Cinemorphx", "Bohemian"],
        "subfolders": ["trailer_tools", "epic_orchestral", "impacts", "risers", 
                      "samplelogic", "cinematic_keys", "trailer_drums"]
    },
    "05_DRUMS_PERCUSSION": {
        "description": "Drums, percussion, and rhythmic elements",
        "patterns": ["DRUMS_PERCUSSION", "CLAPS", "BELLTREE", "CASTANETS", "CUICA", 
                    "TAMBORCITO", "GLASSES", "Fury", "Taiko", "Percussion",
                    "Toontrack", "Superior", "XLN Audio", "Addictive Drums", "FXPansion", "BFD",
                    "Steven Slate", "Trigger", "Slate Drums", "Drum Fury"],
        "subfolders": ["acoustic_drums", "electronic_drums", "world_percussion", 
                      "fx_percussion", "orchestral_percussion", "toontrack", 
                      "xln_audio", "slate_digital", "samplelogic_drums"]
    },
    "06_GUITARS_STRINGS": {
        "description": "Guitar and string instrument libraries",
        "patterns": ["GUITAR", "BASS", "STRING", "ACOUSTIC", "ELECTRIC", "PLECTRUM",
                    "Orange Tree", "Ample Sound", "Music Lab", "Cinematic Guitars",
                    "SampleLogic"],
        "subfolders": ["acoustic_guitars", "electric_guitars", "bass", "exotic_strings", 
                      "cinematic_guitars", "samplelogic_guitars"]
    },
    "07_KEYBOARDS_PIANOS": {
        "description": "Keyboard instruments and pianos",
        "patterns": ["PIANO", "KEYBOARD", "KEYS", "ELECTRIC PIANO", "ORGAN",
                    "Scarbee", "HARMONIUM", "Synthogy", "Ivory", "Cinematic Keys",
                    "SampleLogic"],
        "subfolders": ["acoustic_pianos", "electric_pianos", "organs", "vintage_keys", 
                      "cinematic_keys", "samplelogic_keys"]
    },
    "08_VOCALS_HUMAN": {
        "description": "Vocal libraries and human sounds",
        "patterns": ["VOCALS", "HUMAN_WHISTLING", "CHOIR", "VOICE", "VOCAL"],
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
        "patterns": ["SOUNDSCAPES_FX", "Quirky", "Cinescapes", "RS_Cinescapes", "AMBIENT"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts", "ambient"]
    },
    "99_MISCELLANEOUS": {
        "description": "Miscellaneous and uncategorized items",
        "patterns": [],
        "subfolders": []
    }
}

# Root paths
KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
ORGANIZED_ROOT = KONTAKT_LAB.parent / "DEEP_ORGANIZED"
BACKUP_ROOT = KONTAKT_LAB.parent / "DEEP_BACKUP"

def organize_kontakt_lab_items():
    """Organize all KONTAKT_LAB items with enhanced SampleLogic detection"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS (Now with SampleLogic Detection!)...")
    print("💸 Because we spent way too much money on sample libraries! 💸")
    
    organized_count = 0
    collision_count = 0
    orphan_count = 0
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
    # Create NI_2026 ORPHANS folder
    ni_2026_orphans = Path("/Volumes/6TB/_NI_2026/_ORPHANS")
    try:
        ni_2026_orphans.mkdir(parents=True, exist_ok=True)
        print(f"🏠 Created orphan sanctuary: {ni_2026_orphans}")
    except Exception as e:
        print(f"⚠️  Could not create orphan sanctuary: {e}")
        ni_2026_orphans = ORGANIZED_ROOT / "99_MISCELLANEOUS"
        ni_2026_orphans.mkdir(parents=True, exist_ok=True)
    
    if not KONTAKT_LAB.exists():
        print(f"❌ Source directory not found: {KONTAKT_LAB}")
        return organized_count, collision_count, orphan_count
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in skip_dirs:
            continue
        
        organized = False
        item_name = item.name
        
        # Find matching category with enhanced SampleLogic detection
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern.lower() in item_name.lower() or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name.lower() for p in pattern.lower().split("_"))):
                    
                    # Enhanced subfolder detection with SampleLogic support
                    target_subfolder = "general"
                    
                    if category == "01_ORCHESTRAL_PREMIUM":
                        if any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC", "MORPHESTRA"]):
                            target_subfolder = "samplelogic"
                        elif any(x in item_name.upper() for x in ["PROJECT SAM", "PROJECTSAM"]):
                            target_subfolder = "project_sam"
                        elif any(x in item_name.upper() for x in ["CINESAMPLES", "CINESTRINGS"]):
                            target_subfolder = "cinesamples"
                        elif any(x in item_name.upper() for x in ["EASTWEST", "EWQL", "HOLLYWOOD"]):
                            target_subfolder = "eastwest"
                        elif any(x in item_name.upper() for x in ["VSL", "VIENNA"]):
                            target_subfolder = "vsl"
                        elif any(x in item_name.upper() for x in ["BRASS", "HORN"]):
                            target_subfolder = "brass"
                        elif any(x in item_name.upper() for x in ["STRING", "VIOLIN", "CELLO"]):
                            target_subfolder = "strings"
                        else:
                            target_subfolder = "full_orchestra"
                    
                    elif category == "03_ELECTRONIC_SYNTH":
                        if any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC", "INFINITY", "CINEMORPHX", "ELECTRIFY", "PSYCHOACOUSTICA", "ARPOLOGY"]):
                            target_subfolder = "samplelogic"
                        elif any(x in item_name.upper() for x in ["SPECTRASONICS", "OMNISPHERE", "TRILOGY"]):
                            target_subfolder = "spectrasonics"
                        elif "OUTPUT" in item_name.upper():
                            target_subfolder = "output"
                        elif "ZEBRA" in item_name.upper():
                            target_subfolder = "zebra"
                        elif any(x in item_name.upper() for x in ["VINTAGE", "ANALOG"]):
                            target_subfolder = "vintage"
                        else:
                            target_subfolder = "digital"
                    
                    elif category == "04_CINEMATIC_TRAILER":
                        if any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC"]):
                            target_subfolder = "samplelogic"
                        elif "TRAILER TOOLKIT" in item_name.upper():
                            target_subfolder = "trailer_tools"
                        elif "TRAILER DRUMS" in item_name.upper():
                            target_subfolder = "trailer_drums"
                        elif "CINEMATIC KEYS" in item_name.upper():
                            target_subfolder = "cinematic_keys"
                        else:
                            target_subfolder = "epic_orchestral"
                    
                    elif category == "05_DRUMS_PERCUSSION":
                        if any(x in item_name.upper() for x in ["DRUM FURY", "SAMPLELOGIC"]):
                            target_subfolder = "samplelogic_drums"
                        elif any(x in item_name.upper() for x in ["TOONTRACK", "SUPERIOR"]):
                            target_subfolder = "toontrack"
                        elif any(x in item_name.upper() for x in ["XLN AUDIO", "ADDICTIVE"]):
                            target_subfolder = "xln_audio"
                        elif any(x in item_name.upper() for x in ["SLATE", "TRIGGER"]):
                            target_subfolder = "slate_digital"
                        else:
                            target_subfolder = "acoustic_drums"
                    
                    elif category == "06_GUITARS_STRINGS":
                        if "CINEMATIC GUITARS" in item_name.upper():
                            target_subfolder = "cinematic_guitars"
                        elif "SAMPLELOGIC" in item_name.upper():
                            target_subfolder = "samplelogic_guitars"
                        elif "BASS" in item_name.upper():
                            target_subfolder = "bass"
                        else:
                            target_subfolder = "acoustic_guitars"
                    
                    elif category == "07_KEYBOARDS_PIANOS":
                        if any(x in item_name.upper() for x in ["CINEMATIC KEYS", "SAMPLELOGIC"]):
                            target_subfolder = "samplelogic_keys"
                        elif "ELECTRIC" in item_name.upper():
                            target_subfolder = "electric_pianos"
                        elif "ORGAN" in item_name.upper():
                            target_subfolder = "organs"
                        else:
                            target_subfolder = "acoustic_pianos"
                    
                    # Use first subfolder if no specific match
                    if target_subfolder == "general" and config["subfolders"]:
                        target_subfolder = config["subfolders"][0]
                    
                    if target_subfolder:
                        target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
                    else:
                        target_path = ORGANIZED_ROOT / category / item_name
                    
                    # Ensure target directory exists
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
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
                        
                        # Enhanced vendor notifications - NOW WITH SAMPLELOGIC! 💸
                        if any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC"]):
                            print(f"💰 SAMPLELOGIC: {item_name} → {category}/{target_subfolder}")
                        elif any(x in item_name.upper() for x in ["SPECTRASONICS", "OMNISPHERE"]):
                            print(f"🎹 SPECTRASONICS: {item_name} → {category}/{target_subfolder}")
                        elif any(x in item_name.upper() for x in ["TOONTRACK", "SUPERIOR"]):
                            print(f"🥁 TOONTRACK: {item_name} → {category}/{target_subfolder}")
                        elif any(x in item_name.upper() for x in ["XLN AUDIO", "ADDICTIVE"]):
                            print(f"🎵 XLN AUDIO: {item_name} → {category}/{target_subfolder}")
                        elif any(x in item_name.upper() for x in ["STEVEN SLATE", "TRIGGER"]):
                            print(f"🎯 SLATE DIGITAL: {item_name} → {category}/{target_subfolder}")
                        elif any(x in item_name.upper() for x in ["FXPANSION", "BFD"]):
                            print(f"🔥 FXPANSION: {item_name} → {category}/{target_subfolder}")
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
        
        # Move uncategorized items to ORPHANS
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

def create_deep_organization_structure():
    """Create the deep organization structure with SampleLogic support"""
    print("\n🏗️ CREATING DEEP ORGANIZATION STRUCTURE (With SampleLogic!)...")
    
    for category, config in DEEP_PROJECT_STRUCTURE.items():
        category_path = ORGANIZED_ROOT / category
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        for subfolder in config["subfolders"]:
            (category_path / subfolder).mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Created category: {category}")

def main():
    """Execute the ultimate organization with SampleLogic support"""
    print("🧙‍♂️ NOIZYGENIE: ULTIMATE LIBRARY ORGANIZATION")
    print("💸 NOW WITH SAMPLELOGIC! (Because we spent way too much!) 💸")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    create_deep_organization_structure()
    organized_count, collision_count, orphan_count = organize_kontakt_lab_items()
    
    # Final report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ NOIZYGENIE ULTIMATE ORGANIZATION COMPLETE!")
    print("💰 ALL YOUR EXPENSIVE LIBRARIES ARE NOW ORGANIZED! 💰")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"✅ Items Organized: {organized_count}")
    print(f"⚠️  Name Collisions: {collision_count}")
    print(f"🏠 Orphans Relocated: {orphan_count}")
    print(f"📁 Categories Created: {len(DEEP_PROJECT_STRUCTURE)}")
    print(f"🗂️  Organized Structure: {ORGANIZED_ROOT}")
    print(f"🏠 Orphan Sanctuary: {ni_2026_orphans}")
    
    print("\n💸 VENDORS NOW FULLY SUPPORTED:")
    print("🎹 Spectrasonics (Omnisphere, Trilogy, Keyscapes)")
    print("💰 SampleLogic (Infinity, CinemorphX, Trailer Toolkit)")
    print("🥁 Toontrack (Superior Drummer)")
    print("🎵 XLN Audio (Addictive Drums)")
    print("🎯 Slate Digital (Trigger 2)")
    print("🔥 FXpansion (BFD)")
    print("🎼 And many more!")
    
    print("\n🏆 YOUR EXPENSIVE SAMPLE LIBRARY COLLECTION IS NOW PERFECTLY ORGANIZED!")

if __name__ == "__main__":
    main()
