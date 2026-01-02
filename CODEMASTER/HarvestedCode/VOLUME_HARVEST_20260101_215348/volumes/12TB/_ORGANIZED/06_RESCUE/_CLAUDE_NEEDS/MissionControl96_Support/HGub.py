#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/organize_existing_projects.py
"""
NOIZYGENIE: COMPLETE LIBRARY + PLUGIN INVENTORY & ACCOUNTING SYSTEM
Enhanced with LA Scoring Strings, Legato Sordino, Genesis Children's Choir + MASSIVE Spitfire detection! 🎼💸
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
    
    # MASSIVELY ENHANCED SPITFIRE AUDIO - ALL LIBRARIES! 🎼
    "Spitfire Audio": [
        # Core brand names & variations
        "spitfire", "spitfire audio", "spitfire_audio", "sfa", "sf_", "spf_",
        
        # LABS series (Free libraries) - COMPLETE LIST
        "labs", "spitfire labs", "amplify", "soft piano", "strings", "brass", 
        "woodwinds", "choir", "percussion", "felt piano", "electric piano",
        "frozen strings", "scary strings", "drums", "vocals", "guitars",
        "tape", "music box", "kalimba", "dulcimer", "cimbalom", "banjo",
        "harmonium", "glass marimba", "jangle box", "intimate strings",
        "scandi folk", "rock organ", "vintage funk machine", "epic tom toms",
        
        # Abbey Road series - COMPLETE
        "abbey road", "abbey_road", "abbey", "studios", "one", "two", "late night sessions",
        "vintage drummer", "modern drummer", "abbey road chambers", "reverb plates",
        "abbey road orchestral foundations", "abbey road low strings",
        
        # Albion series - ALL VARIANTS
        "albion", "albion one", "albion neo", "albion tundra", "albion loegria",
        "albion solstice", "albion uist", "albion colossus", "albion iceni",
        "albion", "legacy", "earth", "modern", "cinematic",
        
        # BBC Symphony Orchestra - ALL VERSIONS
        "bbc", "bbc symphony", "bbc so", "symphony orchestra", "discover", "core", "professional",
        "bbc symphony orchestra discover", "bbc symphony orchestra core", "bbc symphony orchestra professional",
        
        # Studio series - COMPLETE
        "studio", "studio strings", "studio brass", "studio woodwinds", 
        "studio percussion", "studio drums", "studio choir", "studio orchestra",
        
        # Chamber series & Evolutions
        "chamber", "chamber strings", "chamber evolve", "evolutions", "evolution",
        "chamber strings evolve", "evolutions",
        
        # Solo instruments - COMPLETE LIST
        "solo strings", "solo violin", "solo cello", "solo viola", "solo bass",
        "solo", "virtuoso", "first chair",
        
        # Symphonic series - ALL
        "symphonic", "symphonic strings", "symphonic brass", "symphonic woodwinds",
        "symphonic metals", "symphonic motions", "symphonic series",
        
        # Originals series - MASSIVE EXPANSION
        "originals", "cimbalom", "dulcimer", "firewood piano", "glass marimba",
        "intimate strings", "intimate grand piano", "jangle box", "mandolin",
        "scandi folk", "banjo", "harmonium", "music box", "epic tom toms",
        "vintage funk machine", "kalimba", "rock organ", "tape piano",
        "felt piano", "soft piano", "vintage upright", "vintage electric",
        "dusty piano", "vintage keys", "retro keys", "analogue strings",
        
        # Hans Zimmer collaborations - COMPLETE
        "hans zimmer", "zimmer", "hzss", "hans zimmer strings", "hans zimmer brass",
        "hans zimmer percussion", "professional", "piano", "hzp", "hz",
        "hans zimmer piano", "hans zimmer strings professional",
        
        # Signature series & Artist collaborations
        "olafur arnalds", "keaton henson", "max richter", "christian henson",
        "ólafur", "arnalds", "composer toolkit", "evolution", "signature",
        "artist", "collaboration", "eric whitacre", "paul thomson",
        
        # Percussion & Drums - EXPANDED
        "percussion", "drums", "epic", "orchestral percussion", "thunderous",
        "cinematic percussion", "hybrid", "drum machines", "epic tom toms",
        "timpani", "taiko", "ethnic percussion", "found percussion",
        
        # Brass libraries - COMPLETE
        "brass", "horns", "trumpets", "trombones", "tubas", "french horns",
        "cimbasso", "flugelhorn", "cornet", "euphonium", "low brass",
        "high brass", "solo brass", "section brass",
        
        # Woodwinds - COMPLETE
        "woodwinds", "flutes", "clarinets", "oboes", "bassoons", "piccolo",
        "bass clarinet", "english horn", "contrabassoon", "alto flute",
        "solo woodwinds", "section woodwinds",
        
        # Vocal libraries - EXPANDED
        "choir", "vocal", "voices", "chorus", "cathedral", "gospel",
        "london voices", "children", "boys choir", "female choir",
        "male choir", "mixed choir", "vocal textures", "wordbuilder",
        
        # Guitars & Folk - COMPLETE
        "guitars", "acoustic", "electric", "folk", "mandolin", "banjo",
        "ukulele", "12-string", "steel string", "nylon string",
        "fingerpicked", "strummed", "plucked",
        
        # Pianos & Keys - MASSIVE EXPANSION
        "piano", "grand piano", "upright", "felt piano", "soft piano",
        "electric piano", "vintage keys", "organ", "harmonium",
        "celeste", "glockenspiel", "vibraphone", "marimba", "prepared piano",
        "toy piano", "honky tonk", "vintage electric piano",
        
        # Cinematic & Trailer - EXPANDED
        "cinematic", "trailer", "epic", "massive", "huge", "powerful",
        "dramatic", "tension", "suspense", "action", "horror", "thriller",
        "emotional", "intimate", "melancholic",
        
        # Hybrid & Electronic - EXPANDED
        "hybrid", "electronic", "synth", "pads", "textures", "atmospheres",
        "pulses", "arpeggios", "sequences", "ambient", "soundscape",
        
        # Regional collections - EXPANDED
        "british", "london", "english", "scottish", "irish", "celtic",
        "european", "scandinavian", "scandi", "nordic", "folk",
        
        # Special editions & collaborations - EXPANDED
        "signature", "artist", "composer", "professional", "core", "discover",
        "expansion", "collection", "library", "kontakt", "plugin",
        "special edition", "limited edition", "exclusive",
        
        # File naming patterns - COMPREHENSIVE
        "sf_", "spf_", "sfa_", "_sf_", "_spitfire_", "spitfire_",
        ".spitfire", "spitfire.", "[spitfire]", "(spitfire)",
        "SpitfireAudio", "SPITFIRE", "Spitfire_Audio",
        
        # Common abbreviations & codes
        "sao", "sao_", "sf", "sfa", "sal", "spf", "spi", "spa"
    ],
    
    # NEW: LA Scoring Strings & Related
    "LA Scoring Strings": [
        "la scoring", "la scoring strings", "la_scoring", "lass", "scoring strings",
        "los angeles", "hollywood strings", "scoring", "legato sordino",
        "sordino", "legato", "first chair", "section", "divisi"
    ],
    
    # NEW: Genesis Children's Choir & Related Choirs
    "Genesis Children's Choir": [
        "genesis", "children", "choir", "children's choir", "childrens choir",
        "boys choir", "girls choir", "youth choir", "young voices",
        "soprano choir", "treble voices"
    ],
    
    # Major Orchestral Libraries
    "EastWest": [
        "eastwest", "east west", "ewql", "quantum leap", "play engine",
        "hollywood", "stormdrum", "symphonic", "choirs", "voices", "pianos",
        "hollywood orchestra", "hollywood strings", "hollywood brass",
        "hollywood woodwinds", "hollywood percussion", "voices of passion"
    ],
    "Vienna Symphonic Library (VSL)": [
        "vsl", "vienna", "vienna symphonic", "vienna instruments", 
        "synchron", "special edition", "solo strings", "epic orchestra",
        "vienna imperial", "vienna ensemble", "dimension strings"
    ],
    "ProjectSAM": [
        "project sam", "projectsam", "symphobia", "true strike", 
        "orchestral essentials", "the free orchestra", "swing more",
        "symphobia colours", "true strike 1", "true strike 2"
    ],
    "CineSamples": [
        "cinesamples", "cinestrings", "cinebrass", "cinewinds", 
        "cineperc", "voxos", "piano in blue", "tina guo",
        "cinestrings core", "cinestrings solo", "cinebrass core"
    ],
    "8Dio": [
        "8dio", "adagio", "lacrimosa", "century", "hybrid", "requiem",
        "claire", "epic taiko", "songwriting", "8dio adagio strings",
        "8dio century strings", "8dio lacrimosa"
    ],
    "Audio Imperia": [
        "audio imperia", "nucleus", "jaeger", "areia", "talos", "choruss",
        "impero", "phoenix orchestra"
    ],
    "Orchestral Tools": [
        "orchestral tools", "berlin", "metropolis", "ark", "sine", "junkie xl",
        "berlin strings", "berlin brass", "berlin woodwinds"
    ],
    
    # Electronic & Synthesis
    "Output": [
        "output", "analog strings", "rev", "exhale", "signal", "substance",
        "movement", "portal", "thermal", "arcade", "bass", "analog brass & winds"
    ],
    "Arturia": [
        "arturia", "analog lab", "pigments", "minilab", "keylab", "minimoog",
        "jupiter", "prophet", "matrix", "cs-80", "sem", "modular v",
        "collection", "v collection"
    ],
    "Roland": [
        "roland", "jupiter", "juno", "tr-", "tb-", "sh-", "cloud", "zenology",
        "roland cloud", "lifetime key"
    ],
    
    # Premium Electronic Libraries
    "Spectrasonics": [
        "spectrasonics", "omnisphere", "trilogy", "keyscapes", "stylus rmx",
        "stylus", "rmx", "omnisphere 2", "trilian", "keyscape",
        "omnisphere 2.8"
    ],
    "SampleLogic": [
        "samplelogic", "sample logic", "infinity", "morphestra", "cinemorphx",
        "cinematic guitars", "trailer toolkit", "electrify", "drum fury",
        "analog", "vintage vault", "synth legends", "psychoacoustica",
        "arpology", "bohemian", "trailer drums", "cinematic keys"
    ],
    "reFX": [
        "refx", "nexus", "nexus2", "nexus3", "nexus 2", "nexus 3", "vanguard",
        "quadrasid", "slayer", "nexus4", "nexus 4"
    ],
    
    # Superior Drum Libraries & Software
    "Toontrack": [
        "toontrack", "superior drummer", "ezdrummer", "ezx", "sdx", "ez drummer",
        "superior", "drumkit from hell", "metal machine", "new york studios",
        "superior drummer 3", "ezdrummer 3"
    ],
    "XLN Audio": [
        "xln audio", "addictive drums", "addictive keys", "ad2", "retro color",
        "addictive trigger", "addictive drums 2"
    ],
    "FXpansion": [
        "fxpansion", "bfd", "geist", "bfd3", "bfd eco", "strobe2"
    ],
    "Slate Digital": [
        "slate digital", "trigger", "drums", "slate drums", "trigger 2",
        "virtual mix rack", "fg-x", "all access pass"
    ],
    
    # Garritan Libraries
    "Garritan": [
        "garritan", "personal orchestra", "jazz", "world", "instant orchestra",
        "concert & marching band", "aria", "cfx concert grand", "gpo"
    ],
    
    # iZotope Audio Processing
    "iZotope": [
        "izotope", "ozone", "neutron", "nectar", "rx", "iris", "trash",
        "insight", "alloy", "phoenix", "vinyl", "vocal synth", "music production suite"
    ],
    
    # Waves Audio Processing
    "Waves": [
        "waves", "ssl", "api", "abbey road", "cla", "kramer", "puigtec",
        "renaissance", "vintage", "gold", "diamond", "mercury", "platinum",
        "horizon", "signature series"
    ],
    
    # Line6 Guitar Processing
    "Line6": [
        "line6", "line 6", "pod farm", "helix", "amplifi", "spider", "firehawk",
        "relay", "variax", "dt25", "dt50", "pod farm 2.5"
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

# Enhanced project structure with NEW CATEGORIES and DEDICATED Spitfire folder
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
                    "Morphestra", "SampleLogic", "8Dio", "Audio Imperia", "Orchestral Tools",
                    "LA Scoring", "LASS", "Scoring Strings"],
        "subfolders": ["strings", "brass", "woodwinds", "full_orchestra", "solo_instruments", 
                      "spitfire_audio", "project_sam", "cinesamples", "eastwest", "vsl", 
                      "samplelogic", "8dio", "audio_imperia", "la_scoring_strings"]
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
        "patterns": ["VOCALS", "HUMAN_WHISTLING", "CHOIR", "VOICE", "VOCAL", "Soundiron", 
                    "Genesis", "Children", "Boys Choir", "Girls Choir"],
        "subfolders": ["choirs", "solo_vocals", "vocal_fx", "human_sounds", "soundiron", 
                      "children_choirs", "genesis_choir", "boys_choirs", "girls_choirs"]
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
    "08_LOOPS_CONSTRUCTION": {
        "description": "Loops, construction kits, and grooves",
        "patterns": ["LOOPS_GROOVES", "CONSTRUCTION_KITS", "MULTIS", "Discolicks", 
                    "Runs_", "SawTooth", "Wavy", "Slow_", "Splice"],
        "subfolders": ["tempo_120", "tempo_140", "tempo_100", "arpeggios", "construction", "splice"]
    },
    "09_SOUNDSCAPES_FX": {
        "description": "Soundscapes, atmospheres, and sound effects",
        "patterns": ["SOUNDSCAPES_FX", "Quirky", "Cinescapes", "RS_Cinescapes", "AMBIENT"],
        "subfolders": ["atmospheres", "textures", "transitions", "impacts", "ambient"]
    },
    "10_AUDIO_PLUGINS": {
        "description": "Audio processing plugins - VST, VST3, AAX, Components",
        "patterns": ["PLUGIN", "VST", "VST3", "AAX", "COMPONENT", "AU", "RTAS",
                    "iZotope", "Waves", "Plugin Alliance", "FabFilter"],
        "subfolders": ["eq", "compressor", "reverb", "delay", "distortion", "modulation",
                      "izotope", "waves", "plugin_alliance", "fabfilter", "mastering"]
    },
    "11_KONTAKT_INSTRUMENTS": {
        "description": "Native Kontakt instruments and libraries",
        "patterns": ["KONTAKT", ".nki", ".nkm", ".nkc", "Native Instruments"],
        "subfolders": ["factory", "third_party", "user", "multis"]
    },
    "12_NATIVE_ACCESS_CONTENT": {
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
                                            "Sugar Bytes", "LennarDigital", "Toontrack", "Spitfire Audio"
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
            "Toontrack": "🥁",
            "Spitfire Audio": "🎼"
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

# Root paths
KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
ORGANIZED_ROOT = KONTAKT_LAB.parent / "DEEP_ORGANIZED"
BACKUP_ROOT = KONTAKT_LAB.parent / "DEEP_BACKUP"

def organize_kontakt_lab_items():
    """Organize all KONTAKT_LAB items with ENHANCED detection for LA Scoring, Genesis Choir, and MASSIVE Spitfire support"""
    print("\n🔄 ORGANIZING KONTAKT_LAB ITEMS...")
    print("🎼 ENHANCED: Spitfire, LA Scoring Strings, Genesis Children's Choir! 🎼")
    
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
        
        # PRIORITY DETECTION ORDER:
        # 1. SPITFIRE AUDIO (highest priority)
        # 2. LA SCORING STRINGS  
        # 3. GENESIS CHILDREN'S CHOIR
        # 4. Regular categories
        
        # 1. PRIORITY SPITFIRE DETECTION FIRST! 🎼
        spitfire_patterns = COMPREHENSIVE_VENDOR_PATTERNS["Spitfire Audio"]
        for pattern in spitfire_patterns:
            if pattern.lower() in item_name.lower():
                category = "01B_SPITFIRE_AUDIO"
                
                # DETAILED SPITFIRE SUBFOLDER DETECTION
                target_subfolder = "bbc_symphony"  # Default
                
                if any(x in item_name.upper() for x in ["BBC", "SYMPHONY"]):
                    target_subfolder = "bbc_symphony"
                elif any(x in item_name.upper() for x in ["ABBEY ROAD", "ABBEY_ROAD"]):
                    target_subfolder = "abbey_road"
                elif any(x in item_name.upper() for x in ["ALBION"]):
                    target_subfolder = "albion_series"
                elif any(x in item_name.upper() for x in ["LABS", "AMPLIFY"]):
                    target_subfolder = "labs_free"
                elif any(x in item_name.upper() for x in ["HANS ZIMMER", "ZIMMER", "HZSS", "HZP"]):
                    target_subfolder = "hans_zimmer"
                elif any(x in item_name.upper() for x in ["ORIGINALS"]):
                    target_subfolder = "originals"
                elif any(x in item_name.upper() for x in ["STUDIO"]):
                    target_subfolder = "studio_series"
                elif any(x in item_name.upper() for x in ["CHAMBER"]):
                    target_subfolder = "chamber_strings"
                elif any(x in item_name.upper() for x in ["SOLO"]):
                    target_subfolder = "solo_instruments"
                elif any(x in item_name.upper() for x in ["BRASS", "TRUMPET", "TROMBONE", "HORN"]):
                    target_subfolder = "brass"
                elif any(x in item_name.upper() for x in ["WOODWIND", "FLUTE", "CLARINET", "OBOE"]):
                    target_subfolder = "woodwinds"
                elif any(x in item_name.upper() for x in ["PERCUSSION", "DRUM", "TIMPANI"]):
                    target_subfolder = "percussion"
                elif any(x in item_name.upper() for x in ["CHOIR", "VOCAL", "VOICE"]):
                    target_subfolder = "choir"
                elif any(x in item_name.upper() for x in ["PIANO", "KEYS", "ORGAN", "HARMONIUM"]):
                    target_subfolder = "pianos_keys"
                elif any(x in item_name.upper() for x in ["GUITAR", "MANDOLIN", "BANJO", "FOLK"]):
                    target_subfolder = "guitars_folk"
                elif any(x in item_name.upper() for x in ["OLAFUR", "KEATON", "RICHTER", "SIGNATURE"]):
                    target_subfolder = "signature_artists"
                elif any(x in item_name.upper() for x in ["EVOLUTION", "EVOL"]):
                    target_subfolder = "evolutions"
                
                target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
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
                    print(f"🎼 SPITFIRE: {item_name} → {category}/{target_subfolder}")
                    organized = True
                    break
                except Exception as e:
                    print(f"❌ Failed to move Spitfire item {item_name}: {e}")
        
        if organized:
            continue
        
        # 2. LA SCORING STRINGS DETECTION
        la_scoring_patterns = COMPREHENSIVE_VENDOR_PATTERNS["LA Scoring Strings"]
        for pattern in la_scoring_patterns:
            if pattern.lower() in item_name.lower():
                category = "01_ORCHESTRAL_PREMIUM"
                target_subfolder = "la_scoring_strings"
                
                target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
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
                    print(f"🎻 LA SCORING: {item_name} → {category}/{target_subfolder}")
                    organized = True
                    break
                except Exception as e:
                    print(f"❌ Failed to move LA Scoring item {item_name}: {e}")
        
        if organized:
            continue
        
        # 3. GENESIS CHILDREN'S CHOIR DETECTION
        genesis_patterns = COMPREHENSIVE_VENDOR_PATTERNS["Genesis Children's Choir"]
        for pattern in genesis_patterns:
            if pattern.lower() in item_name.lower():
                category = "01C_VOCAL_CHOIR"
                target_subfolder = "children_choirs"
                
                if "genesis" in item_name.lower():
                    target_subfolder = "genesis_choir"
                elif "boys" in item_name.lower():
                    target_subfolder = "boys_choirs"
                elif "girls" in item_name.lower():
                    target_subfolder = "girls_choirs"
                
                target_path = ORGANIZED_ROOT / category / target_subfolder / item_name
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
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
                    print(f"👶 GENESIS CHOIR: {item_name} → {category}/{target_subfolder}")
                    organized = True
                    break
                except Exception as e:
                    print(f"❌ Failed to move Genesis Choir item {item_name}: {e}")
        
        if organized:
            continue
        
        # 4. Continue with regular detection for other items
        for category, config in DEEP_PROJECT_STRUCTURE.items():
            if category in ["01B_SPITFIRE_AUDIO", "01C_VOCAL_CHOIR"]:  # Skip already processed
                continue
                
            patterns = config["patterns"]
            for pattern in patterns:
                if (pattern.lower() in item_name.lower() or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name.lower() for p in pattern.lower().split("_"))):
                    
                    # Enhanced subfolder detection
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
                    
                    elif category == "12_NATIVE_ACCESS_CONTENT":
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
                            "SPITFIRE": "🎼",
                            "BBC": "🎼", 
                            "ABBEY ROAD": "🎼",
                            "ALBION": "🎼",
                            "LABS": "🎼",
                            "HANS ZIMMER": "🎼",
                            "LA SCORING": "🎻",
                            "LASS": "🎻",
                            "GENESIS": "👶",
                            "CHILDREN": "👶",
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
    """Create the deep organization structure with ALL vendor support + new categories"""
    print("\n🏗️ CREATING ULTIMATE ORGANIZATION STRUCTURE...")
    print("🎼 With Spitfire, LA Scoring, Genesis Choir, and ALL vendor support! 💸")
    
    for category, config in DEEP_PROJECT_STRUCTURE.items():
        category_path = ORGANIZED_ROOT / category
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Create subfolders
        for subfolder in config["subfolders"]:
            (category_path / subfolder).mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Created category: {category}")

def main():
    """Execute the ultimate organization with enhanced Spitfire + new libraries"""
    print("🧙‍♂️ NOIZYGENIE: ULTIMATE LIBRARY + PLUGIN + PULSE ORGANIZATION")
    print("🎼 ENHANCED: Spitfire Audio + LA Scoring + Genesis Choir! 🎼")
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
    print("🎼 SPITFIRE AUDIO + LA SCORING + GENESIS CHOIR ENHANCED! 🎼")
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
    
    print("\n🎼 ENHANCED SPITFIRE AUDIO DETECTION:")
    print("✅ BBC Symphony Orchestra (Discover, Core, Professional)")
    print("✅ Abbey Road Studios (One, Two, Late Night Sessions)")
    print("✅ Albion Series (One, Neo, Tundra, Loegria, Solstice, etc.)")
    print("✅ LABS (ALL free libraries)")
    print("✅ Hans Zimmer Collaborations (Strings, Brass, Percussion, Piano)")
    print("✅ Originals Series (ALL libraries)")
    print("✅ Studio & Chamber Series")
    print("✅ Solo Instruments & Signature Artists")
    
    print("\n🎻 NEW LIBRARY SUPPORT:")
    print("✅ LA Scoring Strings (LASS)")
    print("✅ Legato Sordino Libraries")
    print("✅ Genesis Children's Choir")
    print("✅ Enhanced Vocal & Choir Category")
    
    print("\n💸 ALL VENDORS + PULSE INTEGRATION NOW SUPPORTED:")
    print("🎵 Native Instruments (via Pulse/Native Access)")
    print("🎼 Spitfire Audio (MASSIVELY ENHANCED)")
    print("🎻 LA Scoring Strings")
    print("👶 Genesis Children's Choir")
