#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/organize_projects.py
"""
NOIZYGENIE: COMPLETE LIBRARY + PLUGIN INVENTORY & ACCOUNTING SYSTEM
True accounting of ALL sample libraries AND plugins - VST, VST3, AAX, Components
INCLUDING Pulse Installer integration and all your expensive gear! 💸💸💸
"""

import os
import shutil
import json
import sqlite3
import plistlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# Pulse Installer paths and data locations
PULSE_LOCATIONS = {
    "pulse_app": "/Applications/Native Instruments/Native Access.app",
    "pulse_data": "~/Library/Application Support/Native Instruments/Native Access",
    "ni_content": "~/Library/Application Support/Native Instruments/Content",
    "ni_database": "~/Library/Application Support/Native Instruments/Native Access/na_user_data.db",
    "installed_products": "~/Documents/Native Instruments/User Content",
    "komplete_content": "/Library/Application Support/Native Instruments/Content",
    "service_center": "~/Library/Application Support/Native Instruments/Service Center"
}

# ULTIMATE VENDOR DETECTION PATTERNS - ALL YOUR EXPENSIVE GEAR! 💸
COMPREHENSIVE_VENDOR_PATTERNS = {
    # Native Instruments & Kontakt (Enhanced with Pulse data)
    "Native Instruments": [
        "native instruments", "kontakt", "komplete", "massive", "reaktor", 
        "absynth", "battery", "maschine", "traktor", "ni_", "guitar rig",
        "fm8", "razor", "the finger", "transient master", "pulse", "native access"
    ],
    
    # Major Orchestral Libraries
    "Spitfire Audio": [
        "spitfire", "british", "london", "abbey road", "bbc", "hans zimmer",
        "albion", "studio", "chamber", "symphonic", "strings", "brass", "labs"
    ],
    "EastWest": [
        "eastwest", "east west", "ewql", "quantum leap", "play engine",
        "hollywood", "stormdrum", "symphonic", "choirs", "voices", "pianos"
    ],
    "Vienna Symphonic Library (VSL)": [
        "vsl", "vienna", "vienna symphonic", "vienna instruments", 
        "synchron", "special edition", "solo strings", "epic orchestra"
    ],
    "ProjectSAM": [
        "project sam", "projectsam", "symphobia", "true strike", 
        "orchestral essentials", "the free orchestra", "swing more"
    ],
    "CineSamples": [
        "cinesamples", "cinestrings", "cinebrass", "cinewinds", 
        "cineperc", "voxos", "piano in blue", "tina guo"
    ],
    "8Dio": [
        "8dio", "adagio", "lacrimosa", "century", "hybrid", "requiem",
        "claire", "epic taiko", "songwriting"
    ],
    "Audio Imperia": [
        "audio imperia", "nucleus", "jaeger", "areia", "talos", "choruss"
    ],
    "Orchestral Tools": [
        "orchestral tools", "berlin", "metropolis", "ark", "sine", "junkie xl"
    ],
    
    # Electronic & Synthesis
    "Output": [
        "output", "analog strings", "rev", "exhale", "signal", "substance",
        "movement", "portal", "thermal", "arcade"
    ],
    "Arturia": [
        "arturia", "analog lab", "pigments", "minilab", "keylab", "minimoog",
        "jupiter", "prophet", "matrix", "cs-80", "sem", "modular v"
    ],
    "Roland": [
        "roland", "jupiter", "juno", "tr-", "tb-", "sh-", "cloud", "zenology"
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
    "reFX": [
        "refx", "nexus", "nexus2", "nexus3", "nexus 2", "nexus 3", "vanguard",
        "quadrasid", "slayer"
    ],
    
    # Superior Drum Libraries & Software
    "Toontrack": [
        "toontrack", "superior drummer", "ezdrummer", "ezx", "sdx", "ez drummer",
        "superior", "drumkit from hell", "metal machine", "new york studios"
    ],
    "XLN Audio": [
        "xln audio", "addictive drums", "addictive keys", "ad2", "retro color",
        "addictive trigger"
    ],
    "FXpansion": [
        "fxpansion", "bfd", "geist", "bfd3", "bfd eco"
    ],
    "Slate Digital": [
        "slate digital", "trigger", "drums", "slate drums", "trigger 2",
        "virtual mix rack", "fg-x"
    ],
    
    # Garritan Libraries
    "Garritan": [
        "garritan", "personal orchestra", "jazz", "world", "instant orchestra",
        "concert & marching band", "aria", "cfx concert grand"
    ],
    
    # iZotope Audio Processing
    "iZotope": [
        "izotope", "ozone", "neutron", "nectar", "rx", "iris", "trash",
        "insight", "alloy", "phoenix", "vinyl", "vocal synth"
    ],
    
    # Waves Audio Processing
    "Waves": [
        "waves", "ssl", "api", "abbey road", "cla", "kramer", "puigtec",
        "renaissance", "vintage", "gold", "diamond", "mercury", "platinum"
    ],
    
    # Line6 Guitar Processing
    "Line6": [
        "line6", "line 6", "pod farm", "helix", "amplifi", "spider", "firehawk",
        "relay", "variax", "dt25", "dt50"
    ],
    
    # Additional vendors from your list
    "Kompose Audio": ["kompose audio", "kompose", "ethnic winds", "world percussion"],
    "Nucleus Soundlab": ["nucleus soundlab", "nucleus", "hypnotic", "serenity"],
    "Sugar Bytes": ["sugar bytes", "turnado", "wow", "effectrix", "cyclop"],
    "LennarDigital": ["lennardigital", "sylenth", "sylenth1", "lennar digital"],
    
    # World & Ethnic Libraries  
    "Best Service": [
        "best service", "ethnoworld", "ethno world", "eduardtaube",
        "forest kingdom", "ancient", "world", "ethnic", "chris hein"
    ],
    "Zero-G": [
        "zero-g", "zerog", "zero_g", "datafile", "ambient", "shamanic",
        "vocal textures", "world vocals", "sacred", "temple"
    ],
    "Impact Soundworks": [
        "impact soundworks", "shreddage", "ventus", "rhapsody", 
        "tokyo scoring", "ethnic", "koto nation", "pearl concert grand"
    ],
    "Soniccouture": [
        "soniccouture", "hang drum", "glass", "bowed", "found sounds",
        "ethnic", "percussion", "konkrete", "morpheus"
    ],
    
    # Guitar & Bass Libraries
    "Orange Tree Samples": [
        "orange tree", "evolution", "strawberry", "mandolin", 
        "guitar", "bass", "stratosphere", "rosette"
    ],
    "Ample Sound": [
        "ample", "guitar", "bass", "agf", "agm", "abf", "abm", "percussion"
    ],
    "Music Lab": [
        "music lab", "real guitar", "real bass", "real strat", "real lpc"
    ],
    
    # Piano Libraries
    "Synthogy": [
        "synthogy", "ivory", "piano", "italian grand", "american grand"
    ],
    "Galaxy Instruments": [
        "galaxy", "vintage d", "piano", "steinway"
    ],
    
    # Vocal Libraries
    "Soundiron": [
        "soundiron", "vocal", "choir", "voice", "mars", "venus", "olympus",
        "requiem", "apocalypse", "mercury"
    ],
    "Strezov Sampling": [
        "strezov", "choir", "vocal", "wotan", "freyja", "storm choir"
    ],
    
    # Additional Major Vendors
    "Heavyocity": [
        "heavyocity", "damage", "evolve", "mosaic", "gravity", "novo"
    ],
    "Two Notes": [
        "two notes", "torpedo", "wall of sound"
    ],
    "IK Multimedia": [
        "ik multimedia", "amplitube", "sampletank", "modo", "syntronik"
    ],
    "Plugin Alliance": [
        "plugin alliance", "brainworx", "elysia", "lindell", "shadow hills"
    ]
}

def scan_pulse_installer_data():
    """Scan Pulse Installer (Native Access) data for installed content"""
    print("\n🔄 SCANNING PULSE INSTALLER (NATIVE ACCESS) DATA...")
    print("🎵 Finding all your Native Instruments content! 🎵")
    
    pulse_data = {
        "scan_date": datetime.now().isoformat(),
        "pulse_installed": False,
        "installed_products": [],
        "content_locations": [],
        "total_ni_content": 0,
        "komplete_version": "Unknown"
    }
    
    # Check if Native Access is installed
    pulse_app = Path(PULSE_LOCATIONS["pulse_app"])
    if pulse_app.exists():
        pulse_data["pulse_installed"] = True
        print("✅ Native Access found!")
        
        # Try to get version info
        try:
            info_plist = pulse_app / "Contents/Info.plist"
            if info_plist.exists():
                with open(info_plist, 'rb') as f:
                    plist_data = plistlib.load(f)
                    version = plist_data.get('CFBundleShortVersionString', 'Unknown')
                    print(f"📱 Native Access Version: {version}")
        except Exception as e:
            print(f"⚠️  Could not read Native Access version: {e}")
    else:
        print("❌ Native Access not found")
    
    # Scan Native Instruments content directories
    content_dirs = [
        Path(PULSE_LOCATIONS["ni_content"]).expanduser(),
        Path(PULSE_LOCATIONS["komplete_content"]),
        Path(PULSE_LOCATIONS["installed_products"]).expanduser()
    ]
    
    for content_dir in content_dirs:
        if content_dir.exists():
            try:
                content_items = list(content_dir.iterdir())
                pulse_data["content_locations"].append({
                    "path": str(content_dir),
                    "item_count": len(content_items),
                    "items": [item.name for item in content_items if item.is_dir()]
                })
                pulse_data["total_ni_content"] += len(content_items)
                print(f"📁 Found {len(content_items)} items in {content_dir}")
                
                # Check for Komplete versions
                for item in content_items:
                    if "komplete" in item.name.lower():
                        pulse_data["komplete_version"] = item.name
                        
            except PermissionError:
                print(f"⚠️  No access to {content_dir}")
            except Exception as e:
                print(f"⚠️  Error scanning {content_dir}: {e}")
    
    # Try to read Native Access database (if accessible)
    db_path = Path(PULSE_LOCATIONS["ni_database"]).expanduser()
    if db_path.exists():
        try:
            print("🗄️  Found Native Access database, attempting to read...")
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()
            
            # Try to get installed products info
            tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            print(f"📊 Database tables found: {len(tables)}")
            
            # Look for product/content tables
            for table in tables:
                table_name = table[0]
                if any(keyword in table_name.lower() for keyword in ["product", "content", "library", "install"]):
                    try:
                        rows = cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;").fetchall()
                        if rows:
                            pulse_data["installed_products"].append({
                                "table": table_name,
                                "sample_data": str(rows[0]) if rows else "No data"
                            })
                            print(f"📋 Found data in table: {table_name}")
                    except Exception as e:
                        print(f"⚠️  Could not read table {table_name}: {e}")
            
            conn.close()
            
        except Exception as e:
            print(f"⚠️  Could not access Native Access database: {e}")
    
    return pulse_data

def scan_plugins():
    """Scan all plugin locations and create inventory with Pulse integration"""
    print("\n🔌 SCANNING ALL PLUGINS (VST, VST3, AAX, Components)...")
    print("💰 Including Native Instruments content from Pulse! 💰")
    
    plugin_inventory = {
        "scan_date": datetime.now().isoformat(),
        "total_plugins": 0,
        "by_format": {},
        "by_vendor": defaultdict(list),
        "expensive_finds": [],
        "pulse_data": scan_pulse_installer_data()
    }
    
    # Plugin scan locations for macOS
    PLUGIN_SCAN_LOCATIONS = {
        "VST": [
            "/Library/Audio/Plug-Ins/VST",
            "/System/Library/Audio/Plug-Ins/VST",
            "~/Library/Audio/Plug-Ins/VST"
        ],
        "VST3": [
            "/Library/Audio/Plug-Ins/VST3",
            "/System/Library/Audio/Plug-Ins/VST3", 
            "~/Library/Audio/Plug-Ins/VST3"
        ],
        "AAX": [
            "/Library/Application Support/Avid/Audio/Plug-Ins",
            "~/Library/Application Support/Avid/Audio/Plug-Ins"
        ],
        "Components": [
            "/Library/Audio/Plug-Ins/Components",
            "/System/Library/Audio/Plug-Ins/Components",
            "~/Library/Audio/Plug-Ins/Components"
        ],
        "RTAS": [
            "/Library/Application Support/Digidesign/Plug-Ins",
            "~/Library/Application Support/Digidesign/Plug-Ins"
        ]
    }
    
    for format_name, locations in PLUGIN_SCAN_LOCATIONS.items():
        format_plugins = []
        
        for location in locations:
            location_path = Path(location).expanduser()
            if location_path.exists():
                try:
                    for plugin in location_path.iterdir():
                        if plugin.is_file() or plugin.is_dir():
                            plugin_name = plugin.name
                            format_plugins.append({
                                "name": plugin_name,
                                "path": str(plugin),
                                "size": plugin.stat().st_size if plugin.is_file() else 0,
                                "modified": datetime.fromtimestamp(plugin.stat().st_mtime).isoformat()
                            })
                            
                            # Check for expensive vendors
                            plugin_upper = plugin_name.upper()
                            for vendor, patterns in COMPREHENSIVE_VENDOR_PATTERNS.items():
                                for pattern in patterns:
                                    if pattern.upper() in plugin_upper:
                                        plugin_inventory["by_vendor"][vendor].append({
                                            "name": plugin_name,
                                            "format": format_name,
                                            "path": str(plugin)
                                        })
                                        
                                        # Mark expensive finds
                                        expensive_vendors = [
                                            "iZotope", "Waves", "Spectrasonics", "Native Instruments", 
                                            "Arturia", "Line6", "Slate Digital", "FXpansion", "reFX",
                                            "Sugar Bytes", "LennarDigital", "Toontrack"
                                        ]
                                        
                                        if vendor in expensive_vendors:
                                            plugin_inventory["expensive_finds"].append({
                                                "vendor": vendor,
                                                "name": plugin_name,
                                                "format": format_name
                                            })
                                        break
                except PermissionError:
                    print(f"⚠️  No access to {location}")
                except Exception as e:
                    print(f"⚠️  Error scanning {location}: {e}")
        
        plugin_inventory["by_format"][format_name] = format_plugins
        plugin_inventory["total_plugins"] += len(format_plugins)
        
        if format_plugins:
            print(f"🔌 {format_name}: Found {len(format_plugins)} plugins")
    
    # Save plugin inventory with Pulse data
    inventory_file = ORGANIZED_ROOT / "COMPLETE_INVENTORY.json"
    ORGANIZED_ROOT.mkdir(parents=True, exist_ok=True)
    
    with open(inventory_file, 'w') as f:
        json.dump(plugin_inventory, f, indent=2, default=str)
    
    print(f"\n💸 EXPENSIVE PLUGIN FINDINGS:")
    for find in plugin_inventory["expensive_finds"]:
        vendor_emoji = {
            "iZotope": "🎛️",
            "Waves": "🌊", 
            "Spectrasonics": "🎹",
            "Native Instruments": "🎵",
            "Arturia": "🎛️",
            "Line6": "🎸",
            "Slate Digital": "🎯",
            "FXpansion": "🔥",
            "reFX": "🔥",
            "Sugar Bytes": "🍭",
            "LennarDigital": "🎛️",
            "Toontrack": "🥁"
        }.get(find["vendor"], "💰")
        
        print(f"{vendor_emoji} {find['vendor']}: {find['name']} ({find['format']})")
    
    # Display Pulse data summary
    pulse_data = plugin_inventory["pulse_data"]
    if pulse_data["pulse_installed"]:
        print(f"\n🎵 NATIVE ACCESS (PULSE) SUMMARY:")
        print(f"📦 Total NI Content Items: {pulse_data['total_ni_content']}")
        print(f"🏆 Komplete Version: {pulse_data['komplete_version']}")
        print(f"📁 Content Locations: {len(pulse_data['content_locations'])}")
    
    print(f"\n📊 COMPLETE INVENTORY SAVED: {inventory_file}")
    return plugin_inventory

# Enhanced project structure with Pulse integration
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
                    "Morphestra", "SampleLogic", "8Dio", "Audio Imperia", "Orchestral Tools"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments", 
                      "project_sam", "cinesamples", "eastwest", "vsl", "samplelogic", "8dio", "audio_imperia"]
    },
    "02_ETHNIC_WORLD": {
        "description": "World ethnic instruments and cultural libraries",
        "patterns": ["WORLD_ETHNIC", "ERHU", "CHINA_SETS", "MID_EAST", "BANSURI", "DIGERIDOO", 
                    "CEYLON", "EGYPTIAN", "ALPINE", "GAOHU", "CUMBUS", "TANBUR", "SAZ",
                    "Heart of Asia", "Heart of Africa", "EthnoWorld", "Best Service", "Garritan"],
        "subfolders": ["asian", "middle_eastern", "european", "african", "american", "best_service", "garritan"]
    },
    "03_ELECTRONIC_SYNTH": {
        "description": "Electronic synthesizers and modern sounds",
        "patterns": ["ELECTRONIC", "SYNTHESIZERS", "Industrial", "Evolve", "FRISKY", 
                    "Output", "Analog Strings", "Rev", "Exhale", "Signal", "Substance", "Zebra",
                    "Spectrasonics", "Omnisphere", "Trilogy", "Keyscapes", "Stylus RMX",
                    "SampleLogic", "Sample Logic", "Infinity", "CinemorphX", "Electrify",
                    "Analog", "Vintage Vault", "Synth Legends", "Psychoacoustica", "Arpology",
                    "reFX", "Nexus", "Arturia", "Sylenth", "Sugar Bytes"],
        "subfolders": ["analog", "digital", "hybrid", "experimental", "industrial", 
                      "output", "zebra", "spectrasonics", "samplelogic", "vintage", 
                      "refx_nexus", "arturia", "sylenth", "sugar_bytes"]
    },
    "04_CINEMATIC_TRAILER": {
        "description": "Cinematic and trailer music libraries",
        "patterns": ["CINEMATIC", "TRAILER", "EPIC", "IMPACT", "RISER", "WHOOSH", 
                    "SampleLogic", "Trailer Toolkit", "Trailer Drums", "CinemorphX",
                    "Morphestra", "Cinemorphx", "Bohemian", "Heavyocity", "Damage"],
        "subfolders": ["trailer_tools", "epic_orchestral", "impacts", "risers", 
                      "samplelogic", "cinematic_keys", "trailer_drums", "heavyocity"]
    },
    "05_DRUMS_PERCUSSION": {
        "description": "Drums, percussion, and rhythmic elements",
        "patterns": ["DRUMS_PERCUSSION", "CLAPS", "BELLTREE", "CASTANETS", "CUICA", 
                    "TAMBORCITO", "GLASSES", "Fury", "Taiko", "Percussion",
                    "Toontrack", "Superior", "XLN Audio", "Addictive Drums", "FXPansion", "BFD",
                    "Steven Slate", "Trigger", "Slate Drums", "Drum Fury"],
        "subfolders": ["acoustic_drums", "electronic_drums", "world_percussion", 
                      "fx_percussion", "orchestral_percussion", "toontrack", 
                      "xln_audio", "slate_digital", "samplelogic_drums", "fxpansion"]
    },
    "06_GUITARS_STRINGS": {
        "description": "Guitar and string instrument libraries",
        "patterns": ["GUITAR", "BASS", "STRING", "ACOUSTIC", "ELECTRIC", "PLECTRUM",
                    "Orange Tree", "Ample Sound", "Music Lab", "Cinematic Guitars",
                    "SampleLogic", "Line6", "POD Farm"],
        "subfolders": ["acoustic_guitars", "electric_guitars", "bass", "exotic_strings", 
                      "cinematic_guitars", "samplelogic_guitars", "line6", "amplifiers"]
    },
    "07_KEYBOARDS_PIANOS": {
        "description": "Keyboard instruments and pianos",
        "patterns": ["PIANO", "KEYBOARD", "KEYS", "ELECTRIC PIANO", "ORGAN",
                    "Scarbee", "HARMONIUM", "Synthogy", "Ivory", "Cinematic Keys",
                    "SampleLogic", "Galaxy", "Alicia Keys"],
        "subfolders": ["acoustic_pianos", "electric_pianos", "organs", "vintage_keys", 
                      "cinematic_keys", "samplelogic_keys", "synthogy", "galaxy"]
    },
    "08_VOCALS_HUMAN": {
        "description": "Vocal libraries and human sounds",
        "patterns": ["VOCALS", "HUMAN_WHISTLING", "CHOIR", "VOICE", "VOCAL", "Soundiron"],
        "subfolders": ["choirs", "solo_vocals", "vocal_fx", "human_sounds", "soundiron"]
    },
    "09_LOOPS_CONSTRUCTION": {
        "description": "Loops, construction kits, and grooves",
        "patterns": ["LOOPS_GROOVES", "CONSTRUCTION_KITS", "MULTIS", "Discolicks", 
                    "Runs_", "SawTooth", "Wavy", "Slow_", "Splice"],
        "subfolders": ["tempo_120", "tempo_140", "tempo_100", "arpeggios", "construction", "splice"]
    },
    "10_SOUNDSCAPES_FX": {
        "description": "Soundscapes, atmospheres, and sound effects",
        "patterns": ["SOUNDSCAPES_FX", "Quirky", "Cinescapes", "RS_Cinescapes", "AMBIENT"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts", "ambient"]
    },
    "11_AUDIO_PLUGINS": {
        "description": "Audio processing plugins - VST, VST3, AAX, Components",
        "patterns": ["PLUGIN", "VST", "VST3", "AAX", "COMPONENT", "AU", "RTAS",
                    "iZotope", "Waves", "Plugin Alliance", "FabFilter"],
        "subfolders": ["eq", "compressor", "reverb", "delay", "distortion", "modulation",
                      "izotope", "waves", "plugin_alliance", "fabfilter", "mastering"]
    },
    "12_KONTAKT_INSTRUMENTS": {
        "description": "Native Kontakt instruments and libraries",
        "patterns": ["KONTAKT", ".nki", ".nkm", ".nkc", "Native Instruments"],
        "subfolders": ["factory", "third_party", "user", "multis"]
    },
    "13_NATIVE_ACCESS_CONTENT": {
        "description": "Content managed by Native Access (Pulse Installer)",
        "patterns": ["KOMPLETE", "MASCHINE", "BATTERY", "MASSIVE", "REAKTOR", "ABSYNTH"],
        "subfolders": ["komplete", "maschine_content", "battery_kits", "massive_presets", 
                      "reaktor_ensembles", "guitar_rig", "kontakt_factory"]
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
    """Organize all KONTAKT_LAB items with comprehensive vendor detection and Pulse integration"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS...")
    print("💸 Including Native Access (Pulse) content! 💸")
    
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
        
        # Find matching category with comprehensive vendor detection
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern.lower() in item_name.lower() or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name.lower() for p in pattern.lower().split("_"))):
                    
                    # Enhanced subfolder detection with ALL vendors + Pulse
                    target_subfolder = "general"
                    
                    if category == "01_ORCHESTRAL_PREMIUM":
                        if any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC", "MORPHESTRA"]):
                            target_subfolder = "samplelogic"
                        elif any(x in item_name.upper() for x in ["8DIO"]):
                            target_subfolder = "8dio"
                        elif any(x in item_name.upper() for x in ["AUDIO IMPERIA"]):
                            target_subfolder = "audio_imperia"
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
                        if any(x in item_name.upper() for x in ["REFX", "NEXUS"]):
                            target_subfolder = "refx_nexus"
                        elif any(x in item_name.upper() for x in ["SYLENTH"]):
                            target_subfolder = "sylenth"
                        elif any(x in item_name.upper() for x in ["SUGAR BYTES"]):
                            target_subfolder = "sugar_bytes"
                        elif any(x in item_name.upper() for x in ["ARTURIA"]):
                            target_subfolder = "arturia"
                        elif any(x in item_name.upper() for x in ["SAMPLELOGIC", "SAMPLE LOGIC", "INFINITY", "CINEMORPHX", "ELECTRIFY", "PSYCHOACOUSTICA", "ARPOLOGY"]):
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
                    
                    elif category == "06_GUITARS_STRINGS":
                        if any(x in item_name.upper() for x in ["LINE6", "POD FARM"]):
                            target_subfolder = "line6"
                        elif "CINEMATIC GUITARS" in item_name.upper():
                            target_subfolder = "cinematic_guitars"
                        elif "SAMPLELOGIC" in item_name.upper():
                            target_subfolder = "samplelogic_guitars"
                        elif "BASS" in item_name.upper():
                            target_subfolder = "bass"
                        else:
                            target_subfolder = "acoustic_guitars"
                    
                    elif category == "13_NATIVE_ACCESS_CONTENT":
                        if any(x in item_name.upper() for x in ["KOMPLETE"]):
                            target_subfolder = "komplete"
                        elif any(x in item_name.upper() for x in ["MASCHINE"]):
                            target_subfolder = "maschine_content"
                        elif any(x in item_name.upper() for x in ["BATTERY"]):
                            target_subfolder = "battery_kits"
                        elif any(x in item_name.upper() for x in ["MASSIVE"]):
                            target_subfolder = "massive_presets"
                        elif any(x in item_name.upper() for x in ["REAKTOR"]):
                            target_subfolder = "reaktor_ensembles"
                        elif any(x in item_name.upper() for x in ["GUITAR RIG"]):
                            target_subfolder = "guitar_rig"
                        else:
                            target_subfolder = "kontakt_factory"
                    
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
                        
                        # Enhanced vendor notifications with ALL your expensive gear! 💸
                        vendor_emojis = {
                            "REFX": "🔥",
                            "NEXUS": "🔥",
                            "SYLENTH": "🎛️",
                            "SUGAR BYTES": "🍭",
                            "ARTURIA": "🎹",
                            "LINE6": "🎸",
                            "POD FARM": "🎸",
                            "SAMPLELOGIC": "💰",
                            "SPECTRASONICS": "🎹",
                            "TOONTRACK": "🥁",
                            "XLN AUDIO": "🎵",
                            "SLATE": "🎯",
                            "FXPANSION": "🔥",
                            "8DIO": "🎼",
                            "AUDIO IMPERIA": "⚔️",
                            "KOMPLETE": "🎵",
                            "MASCHINE": "🥁",
                            "NATIVE INSTRUMENTS": "🎵"
                        }
                        
                        found_vendor = None
                        for vendor_key in vendor_emojis.keys():
                            if vendor_key in item_name.upper():
                                found_vendor = vendor_key
                                break
                        
                        if found_vendor:
                            emoji = vendor_emojis[found_vendor]
                            print(f"{emoji} {found_vendor}: {item_name} → {category}/{target_subfolder}")
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
    """Create the deep organization structure with ALL vendor support + Pulse"""
    print("\n🏗️ CREATING ULTIMATE ORGANIZATION STRUCTURE...")
    print("📁 With Pulse Installer integration and ALL vendor support! 💸")
    
    for category, config in DEEP_PROJECT_STRUCTURE.items():
        category_path = ORGANIZED_ROOT / category
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        for subfolder in config["subfolders"]:
            (category_path / subfolder).mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Created category: {category}")

def main():
    """Execute the ultimate organization with Pulse integration"""
    print("🧙‍♂️ NOIZYGENIE: ULTIMATE LIBRARY + PLUGIN + PULSE ORGANIZATION")
    print("💸 ALL YOUR EXPENSIVE GEAR + NATIVE ACCESS INTEGRATION! 💸")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    # Scan plugins and Pulse data
    plugin_inventory = scan_plugins()
    
    create_deep_organization_structure()
    organized_count, collision_count, orphan_count = organize_kontakt_lab_items()
    
    # Final report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ NOIZYGENIE ULTIMATE ORGANIZATION COMPLETE!")
    print("💰 ALL YOUR EXPENSIVE LIBRARIES + PLUGINS + PULSE DATA! 💰")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"✅ Libraries Organized: {organized_count}")
    print(f"🔌 Plugins Scanned: {plugin_inventory['total_plugins']}")
    print(f"🎵 Native Access Integration: {'✅' if plugin_inventory['pulse_data']['pulse_installed'] else '❌'}")
    print(f"📦 NI Content Items: {plugin_inventory['pulse_data']['total_ni_content']}")
    print(f"⚠️  Name Collisions: {collision_count}")
    print(f"🏠 Orphans Relocated: {orphan_count}")
    print(f"📁 Categories Created: {len(DEEP_PROJECT_STRUCTURE)}")
    print(f"🗂️  Organized Structure: {ORGANIZED_ROOT}")
    
    print("\n💸 ALL VENDORS + PULSE INTEGRATION NOW SUPPORTED:")
    print("🎵 Native Instruments (via Pulse/Native Access)")
    print("🎹 Spectrasonics (Omnisphere, Trilogy, Keyscapes)")
    print("💰 SampleLogic (Infinity, CinemorphX, Trailer Toolkit)")
    print("🥁 Toontrack (Superior Drummer)")
    print("🎵 XLN Audio (Addictive Drums)")
    print("🎯 Slate Digital (Trigger 2)")
    print("🔥 reFX (Nexus)")
    print("🎛️ Arturia (Analog Lab, Pigments)")
    print("🍭 Sugar Bytes (Turnado, Effectrix)")
    print("🎸 Line6 (POD Farm 2)")
    print("🎛️ iZotope (Ozone, Neutron)")
    print("🌊 Waves (SSL, API, Abbey Road)")
    print("🎼 Garritan (Personal Orchestra)")
    print("⚔️ Audio Imperia (Nucleus)")
    print("🔥 FXpansion (BFD)")
    print("🎼 8Dio (Adagio, Century)")
    print("🎼 And SO many more!")
    
    print(f"\n🏆 YOUR ENTIRE EXPENSIVE MUSIC PRODUCTION ARSENAL + PULSE DATA!")
    print(f"🔌 Complete inventory with {len(plugin_inventory['expensive_finds'])} expensive finds!")
    print(f"🎵 Native Access integration with database scanning!")

if __name__ == "__main__":
    main()
