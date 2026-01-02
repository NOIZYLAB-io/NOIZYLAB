#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/mission_control_scanner.py
"""
NOIZYGENIE: MISSION CONTROL - SYSTEM-WIDE INSTRUMENT & SAMPLE SCANNER
Scans ENTIRE Mac system for ALL instruments, samples, and libraries
Finds everything hiding in Applications, Library, Volumes, and user directories! 🎵🔍
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# ULTIMATE VENDOR DETECTION PATTERNS - EXPANDED FOR SYSTEM-WIDE SCAN
COMPREHENSIVE_VENDOR_PATTERNS = {
    # Native Instruments & Kontakt
    "Native Instruments": [
        "native instruments", "kontakt", "komplete", "massive", "reaktor", 
        "absynth", "battery", "maschine", "traktor", "ni_", "guitar rig",
        "fm8", "razor", "the finger", "transient master", "pulse", "native access"
    ],
    
    # MASSIVELY ENHANCED SPITFIRE AUDIO - ALL LIBRARIES! 🎼
    "Spitfire Audio": [
        "spitfire", "spitfire audio", "spitfire_audio", "sfa", "sf_", "spf_",
        "labs", "bbc", "abbey road", "albion", "hans zimmer", "originals",
        "studio", "chamber", "solo", "symphony", "orchestral"
    ],
    
    # LA Scoring & String Libraries
    "LA Scoring Strings": [
        "la scoring", "la scoring strings", "la_scoring", "lass", "scoring strings",
        "los angeles", "legato sordino", "sordino", "legato"
    ],
    
    # Genesis & Children's Choirs
    "Genesis Children's Choir": [
        "genesis", "children", "choir", "children's choir", "childrens choir",
        "boys choir", "girls choir", "youth choir"
    ],
    
    # Major Orchestral Libraries
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
    "Spectrasonics": [
        "spectrasonics", "omnisphere", "trilogy", "keyscapes", "stylus rmx",
        "stylus", "rmx", "omnisphere 2", "trilian", "keyscape"
    ],
    "SampleLogic": [
        "samplelogic", "sample logic", "infinity", "morphestra", "cinemorphx",
        "cinematic guitars", "trailer toolkit", "electrify", "drum fury"
    ],
    "reFX": [
        "refx", "nexus", "nexus2", "nexus3", "nexus 2", "nexus 3", "vanguard"
    ],
    "Arturia": [
        "arturia", "analog lab", "pigments", "minilab", "keylab", "minimoog"
    ],
    "Sugar Bytes": ["sugar bytes", "turnado", "wow", "effectrix", "cyclop"],
    "LennarDigital": ["lennardigital", "sylenth", "sylenth1"],
    
    # Drum Libraries
    "Toontrack": [
        "toontrack", "superior drummer", "ezdrummer", "ezx", "sdx", "superior"
    ],
    "XLN Audio": [
        "xln audio", "addictive drums", "addictive keys", "ad2"
    ],
    "Slate Digital": [
        "slate digital", "trigger", "drums", "slate drums", "trigger 2"
    ],
    "FXpansion": ["fxpansion", "bfd", "geist", "bfd3", "bfd eco"],
    
    # Audio Processing
    "iZotope": [
        "izotope", "ozone", "neutron", "nectar", "rx", "iris", "trash"
    ],
    "Waves": [
        "waves", "ssl", "api", "abbey road", "cla", "kramer", "puigtec"
    ],
    "Line6": [
        "line6", "line 6", "pod farm", "helix", "amplifi", "spider"
    ],
    "Plugin Alliance": [
        "plugin alliance", "brainworx", "elysia", "lindell", "shadow hills"
    ],
    
    # Guitar & Bass
    "Orange Tree Samples": [
        "orange tree", "evolution", "strawberry", "mandolin", "guitar"
    ],
    "Ample Sound": [
        "ample", "guitar", "bass", "agf", "agm", "abf", "abm"
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
        "soundiron", "vocal", "choir", "voice", "mars", "venus", "olympus"
    ],
    "Strezov Sampling": [
        "strezov", "choir", "vocal", "wotan", "freyja", "storm choir"
    ],
    
    # World & Ethnic
    "Best Service": [
        "best service", "ethnoworld", "ethnic", "chris hein"
    ],
    "Zero-G": [
        "zero-g", "zerog", "datafile", "ambient", "world vocals"
    ],
    "Impact Soundworks": [
        "impact soundworks", "shreddage", "ventus", "rhapsody"
    ],
    
    # Additional Major Vendors
    "Heavyocity": [
        "heavyocity", "damage", "evolve", "mosaic", "gravity", "novo"
    ],
    "IK Multimedia": [
        "ik multimedia", "amplitube", "sampletank", "modo", "syntronik"
    ],
    "Garritan": [
        "garritan", "personal orchestra", "jazz", "world", "aria"
    ],
    "Two Notes": ["two notes", "torpedo", "wall of sound"]
}

# Audio file extensions to look for
AUDIO_EXTENSIONS = {
    '.wav', '.aiff', '.aif', '.mp3', '.flac', '.ogg', '.m4a', '.caf',
    '.nki', '.nkm', '.nkc', '.nks', '.kontakt',  # Kontakt
    '.exs24', '.exs', '.logic',  # Logic
    '.reason', '.rfl', '.rex', '.rx2',  # Reason
    '.sfz', '.sf2', '.sf3', '.gig',  # SoundFonts & Giga
    '.akai', '.akp', '.pgm',  # Akai
    '.nnxt', '.sxt',  # Reason NN-XT
    '.dxi', '.vst', '.vst3', '.component', '.aax'  # Plugin formats
}

# Common library/sample directories to scan
SCAN_LOCATIONS = [
    # Applications
    "/Applications",
    
    # System Library
    "/Library/Audio",
    "/Library/Application Support",
    
    # User directories
    "~/Library/Audio",
    "~/Library/Application Support",
    "~/Documents",
    "~/Music",
    "~/Desktop",
    
    # Common sample locations
    "/Library/Application Support/Native Instruments",
    "/Library/Application Support/Arturia",
    "/Library/Application Support/iZotope",
    "/Library/Application Support/Waves",
    "/Library/Application Support/Output",
    "/Library/Application Support/Spectrasonics",
    
    # External volumes
    "/Volumes",
    
    # User-specific paths
    "~/Documents/Native Instruments",
    "~/Music/Audio Music Apps",
    "~/Library/Containers",
    
    # Logic Pro content
    "/Library/Application Support/Logic",
    "~/Library/Application Support/Logic",
    
    # Pro Tools content
    "/Library/Application Support/Avid",
    "~/Library/Application Support/Avid"
]

def get_directory_size(path):
    """Calculate directory size safely"""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except (OSError, IOError):
                    continue
    except (OSError, IOError):
        pass
    return total_size

def format_size(size_bytes):
    """Format bytes to human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"

def scan_location(location_path, mission_data, max_depth=4, current_depth=0):
    """Scan a specific location for instruments and samples"""
    if current_depth > max_depth:
        return
    
    try:
        location = Path(location_path).expanduser()
        if not location.exists() or not location.is_dir():
            return
        
        print(f"🔍 Scanning: {location} (depth {current_depth})")
        
        for item in location.iterdir():
            try:
                if item.is_dir():
                    item_name = item.name.lower()
                    
                    # Skip system directories and hidden files
                    if (item_name.startswith('.') or 
                        item_name in ['system', 'private', 'tmp', 'var', 'dev', 'cores', 'bin', 'sbin', 'usr']):
                        continue
                    
                    # Check for vendor patterns
                    vendor_found = None
                    for vendor, patterns in COMPREHENSIVE_VENDOR_PATTERNS.items():
                        for pattern in patterns:
                            if pattern.lower() in item_name:
                                vendor_found = vendor
                                break
                        if vendor_found:
                            break
                    
                    # Check for common audio/sample indicators
                    audio_indicators = [
                        'samples', 'library', 'libraries', 'instruments', 'kontakt',
                        'audio', 'sounds', 'presets', 'banks', 'loops', 'midi',
                        'piano', 'drums', 'strings', 'brass', 'woodwinds', 'synth',
                        'orchestra', 'choir', 'vocal', 'guitar', 'bass'
                    ]
                    
                    is_audio_related = any(indicator in item_name for indicator in audio_indicators)
                    
                    # Check for audio files in directory
                    has_audio_files = False
                    try:
                        for child in item.iterdir():
                            if child.suffix.lower() in AUDIO_EXTENSIONS:
                                has_audio_files = True
                                break
                    except (PermissionError, OSError):
                        pass
                    
                    if vendor_found or is_audio_related or has_audio_files:
                        # Calculate size
                        size = get_directory_size(item)
                        
                        library_info = {
                            "name": item.name,
                            "path": str(item),
                            "size_bytes": size,
                            "size_formatted": format_size(size),
                            "vendor": vendor_found or "Unknown",
                            "type": "directory",
                            "location_category": str(location_path),
                            "depth": current_depth,
                            "has_audio_files": has_audio_files
                        }
                        
                        mission_data["discovered_libraries"].append(library_info)
                        
                        if vendor_found:
                            mission_data["by_vendor"][vendor_found].append(library_info)
                            
                            # Special highlighting for priority vendors
                            if vendor_found in ["Spitfire Audio", "LA Scoring Strings", "Genesis Children's Choir"]:
                                mission_data["priority_finds"].append(library_info)
                        
                        mission_data["total_size_bytes"] += size
                        
                        vendor_emoji = {
                            "Spitfire Audio": "🎼",
                            "LA Scoring Strings": "🎻", 
                            "Genesis Children's Choir": "👶",
                            "Native Instruments": "🎵",
                            "EastWest": "🎭",
                            "Spectrasonics": "🎹",
                            "Output": "⚡",
                            "Toontrack": "🥁"
                        }.get(vendor_found, "📦")
                        
                        print(f"  {vendor_emoji} FOUND: {item.name} ({format_size(size)}) - {vendor_found or 'Audio Content'}")
                    
                    # Recursively scan subdirectories (with depth limit)
                    if current_depth < max_depth:
                        scan_location(item, mission_data, max_depth, current_depth + 1)
                
                elif item.is_file() and item.suffix.lower() in AUDIO_EXTENSIONS:
                    # Individual audio files
                    try:
                        size = item.stat().st_size
                        file_info = {
                            "name": item.name,
                            "path": str(item),
                            "size_bytes": size,
                            "size_formatted": format_size(size),
                            "type": "file",
                            "extension": item.suffix.lower(),
                            "location_category": str(location_path)
                        }
                        mission_data["audio_files"].append(file_info)
                        mission_data["total_size_bytes"] += size
                    except (OSError, IOError):
                        pass
            
            except (PermissionError, OSError) as e:
                # Skip items we can't access
                continue
    
    except (PermissionError, OSError) as e:
        print(f"  ⚠️  No access to {location_path}")

def mission_control_scan():
    """Execute Mission Control system-wide scan"""
    print("🚀 MISSION CONTROL: SYSTEM-WIDE INSTRUMENT & SAMPLE SCAN")
    print("🔍 Scanning ENTIRE Mac system for ALL your expensive gear!")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    mission_data = {
        "scan_date": start_time.isoformat(),
        "total_libraries": 0,
        "total_size_bytes": 0,
        "discovered_libraries": [],
        "audio_files": [],
        "by_vendor": defaultdict(list),
        "priority_finds": [],
        "scan_locations": [],
        "scan_stats": {
            "locations_scanned": 0,
            "locations_accessible": 0,
            "errors": []
        }
    }
    
    # Scan all locations
    for location in SCAN_LOCATIONS:
        location_path = Path(location).expanduser()
        mission_data["scan_stats"]["locations_scanned"] += 1
        
        try:
            if location_path.exists():
                mission_data["scan_stats"]["locations_accessible"] += 1
                mission_data["scan_locations"].append(str(location_path))
                
                # Limit scan depth based on location type
                max_depth = 2 if str(location_path).startswith('/Applications') else 3
                scan_location(location_path, mission_data, max_depth=max_depth)
            else:
                print(f"⚠️  Location not found: {location}")
        except Exception as e:
            error_msg = f"Error scanning {location}: {str(e)}"
            mission_data["scan_stats"]["errors"].append(error_msg)
            print(f"❌ {error_msg}")
    
    # Update totals
    mission_data["total_libraries"] = len(mission_data["discovered_libraries"])
    
    # Save results
    output_dir = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/MISSION_CONTROL_RESULTS")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results_file = output_dir / f"MISSION_CONTROL_SCAN_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Convert defaultdict to regular dict for JSON serialization
    mission_data["by_vendor"] = dict(mission_data["by_vendor"])
    
    with open(results_file, 'w') as f:
        json.dump(mission_data, f, indent=2, default=str)
    
    # Generate summary report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🚀 MISSION CONTROL SCAN COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"📦 Total Libraries Found: {mission_data['total_libraries']}")
    print(f"🎵 Audio Files Found: {len(mission_data['audio_files'])}")
    print(f"💾 Total Size: {format_size(mission_data['total_size_bytes'])}")
    print(f"📁 Locations Scanned: {mission_data['scan_stats']['locations_scanned']}")
    print(f"✅ Accessible Locations: {mission_data['scan_stats']['locations_accessible']}")
    print(f"📄 Results Saved: {results_file}")
    
    print("\n🎼 PRIORITY VENDOR FINDINGS:")
    for find in mission_data["priority_finds"]:
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "LA Scoring Strings": "🎻",
            "Genesis Children's Choir": "👶"
        }.get(find["vendor"], "💰")
        print(f"{vendor_emoji} {find['vendor']}: {find['name']} ({find['size_formatted']})")
    
    print("\n📊 VENDOR BREAKDOWN:")
    vendor_stats = Counter()
    for vendor, libraries in mission_data["by_vendor"].items():
        vendor_stats[vendor] = len(libraries)
    
    for vendor, count in vendor_stats.most_common(10):
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "Native Instruments": "🎵",
            "EastWest": "🎭",
            "Spectrasonics": "🎹",
            "Output": "⚡",
            "Toontrack": "🥁",
            "iZotope": "🎛️",
            "Waves": "🌊"
        }.get(vendor, "📦")
        print(f"{vendor_emoji} {vendor}: {count} libraries")
    
    print(f"\n🏆 YOUR ENTIRE MUSIC PRODUCTION ARSENAL HAS BEEN MAPPED!")
    print(f"💰 Time to see exactly how much you've spent! 💰")
    
    return mission_data

def main():
    """Execute Mission Control scan"""
    return mission_control_scan()

if __name__ == "__main__":
    main()