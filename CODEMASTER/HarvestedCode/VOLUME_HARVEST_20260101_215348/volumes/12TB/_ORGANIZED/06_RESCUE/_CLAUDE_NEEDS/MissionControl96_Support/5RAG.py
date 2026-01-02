#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/part1_scanner.py
"""
NOIZYGENIE PART 1: ULTIMATE LIBRARY & PLUGIN SCANNER
Scans and catalogs ALL your expensive gear - Libraries, Plugins, Pulse data
Enhanced with LA Scoring Strings, Legato Sordino, Genesis Children's Choir + MASSIVE Spitfire detection! 🎼💸
"""

import os
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
        
        # Hans Zimmer collaborations - COMPLETE
        "hans zimmer", "zimmer", "hzss", "hans zimmer strings", "hans zimmer brass",
        "hans zimmer percussion", "professional", "piano", "hzp", "hz",
        "hans zimmer piano", "hans zimmer strings professional",
        
        # Originals series - MASSIVE EXPANSION
        "originals", "cimbalom", "dulcimer", "firewood piano", "glass marimba",
        "intimate strings", "intimate grand piano", "jangle box", "mandolin",
        "scandi folk", "banjo", "harmonium", "music box", "epic tom toms",
        "vintage funk machine", "kalimba", "rock organ", "tape piano",
        "felt piano", "soft piano", "vintage upright", "vintage electric",
        
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
    
    # Native Instruments & Kontakt
    "Native Instruments": [
        "native instruments", "kontakt", "komplete", "massive", "reaktor", 
        "absynth", "battery", "maschine", "traktor", "ni_", "guitar rig",
        "fm8", "razor", "the finger", "transient master", "pulse", "native access"
    ],
    
    # Major Orchestral Libraries
    "EastWest": [
        "eastwest", "east west", "ewql", "quantum leap", "play engine",
        "hollywood", "stormdrum", "symphonic", "choirs", "voices", "pianos",
        "hollywood orchestra", "hollywood strings", "hollywood brass"
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
    
    # Audio Processing
    "iZotope": [
        "izotope", "ozone", "neutron", "nectar", "rx", "iris"
    ],
    "Waves": [
        "waves", "ssl", "api", "abbey road", "cla", "kramer"
    ],
    "Line6": [
        "line6", "line 6", "pod farm", "helix", "amplifi"
    ],
    
    # Additional vendors
    "Sugar Bytes": ["sugar bytes", "turnado", "wow", "effectrix"],
    "LennarDigital": ["lennardigital", "sylenth", "sylenth1"],
    "Heavyocity": ["heavyocity", "damage", "evolve", "mosaic"],
    "Best Service": ["best service", "ethnoworld", "ethnic"],
    "Garritan": ["garritan", "personal orchestra", "jazz", "world"]
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
    
    return pulse_data

def scan_plugins():
    """Scan all plugin locations and create inventory"""
    print("\n🔌 SCANNING ALL PLUGINS (VST, VST3, AAX, Components)...")
    print("💰 Time to see how much you spent on plugins! 💰")
    
    plugin_inventory = {
        "scan_date": datetime.now().isoformat(),
        "total_plugins": 0,
        "by_format": {},
        "by_vendor": defaultdict(list),
        "expensive_finds": []
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
                                            "Arturia", "Line6", "Slate Digital", "reFX",
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
    
    return plugin_inventory

def scan_kontakt_lab_content():
    """Scan KONTAKT_LAB directory and categorize content"""
    print("\n📂 SCANNING KONTAKT_LAB CONTENT...")
    print("🎼 Detecting Spitfire, LA Scoring, Genesis Choir, and MORE! 🎼")
    
    KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
    skip_dirs = {"DEEP_ORGANIZED", "DEEP_BACKUP", "DEEP_ANALYSIS", "PROJECT_ORGANIZER"}
    
    library_inventory = {
        "scan_date": datetime.now().isoformat(),
        "total_libraries": 0,
        "by_vendor": defaultdict(list),
        "by_category": defaultdict(list),
        "special_finds": [],
        "unidentified": []
    }
    
    if not KONTAKT_LAB.exists():
        print(f"❌ Source directory not found: {KONTAKT_LAB}")
        return library_inventory
    
    for item in KONTAKT_LAB.iterdir():
        if item.name in skip_dirs:
            continue
        
        library_inventory["total_libraries"] += 1
        item_name = item.name
        identified = False
        
        # Check against all vendor patterns
        for vendor, patterns in COMPREHENSIVE_VENDOR_PATTERNS.items():
            for pattern in patterns:
                if pattern.lower() in item_name.lower():
                    library_inventory["by_vendor"][vendor].append({
                        "name": item_name,
                        "path": str(item),
                        "size": sum(f.stat().st_size for f in item.rglob('*') if f.is_file()) if item.is_dir() else item.stat().st_size,
                        "type": "directory" if item.is_dir() else "file"
                    })
                    
                    # Special finds highlighting
                    if vendor in ["Spitfire Audio", "LA Scoring Strings", "Genesis Children's Choir"]:
                        library_inventory["special_finds"].append({
                            "vendor": vendor,
                            "name": item_name,
                            "category": "priority"
                        })
                    
                    identified = True
                    break
            
            if identified:
                break
        
        if not identified:
            library_inventory["unidentified"].append({
                "name": item_name,
                "path": str(item)
            })
    
    return library_inventory

def main():
    """Execute Part 1: Complete scanning and inventory"""
    print("🧙‍♂️ NOIZYGENIE PART 1: ULTIMATE SCANNER & DETECTOR")
    print("🔍 SCANNING ALL YOUR EXPENSIVE GEAR! 🔍")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    # Create output directory
    output_dir = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/SCAN_RESULTS")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Scan everything
    pulse_data = scan_pulse_installer_data()
    plugin_inventory = scan_plugins()
    library_inventory = scan_kontakt_lab_content()
    
    # Combine all data
    complete_inventory = {
        "scan_date": datetime.now().isoformat(),
        "pulse_data": pulse_data,
        "plugins": plugin_inventory,
        "libraries": library_inventory,
        "summary": {
            "total_plugins": plugin_inventory["total_plugins"],
            "total_libraries": library_inventory["total_libraries"],
            "expensive_plugins": len(plugin_inventory["expensive_finds"]),
            "special_libraries": len(library_inventory["special_finds"]),
            "ni_content": pulse_data["total_ni_content"]
        }
    }
    
    # Save complete inventory
    inventory_file = output_dir / "COMPLETE_INVENTORY.json"
    with open(inventory_file, 'w') as f:
        json.dump(complete_inventory, f, indent=2, default=str)
    
    # End report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ PART 1 SCANNING COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"🔌 Plugins Found: {plugin_inventory['total_plugins']}")
    print(f"📚 Libraries Found: {library_inventory['total_libraries']}")
    print(f"💰 Expensive Plugins: {len(plugin_inventory['expensive_finds'])}")
    print(f"🎼 Special Libraries: {len(library_inventory['special_finds'])}")
    print(f"🎵 NI Content: {pulse_data['total_ni_content']}")
    print(f"📄 Inventory Saved: {inventory_file}")
    
    print("\n🎼 SPECIAL LIBRARY FINDINGS:")
    for find in library_inventory["special_finds"]:
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "LA Scoring Strings": "🎻",
            "Genesis Children's Choir": "👶"
        }.get(find["vendor"], "💰")
        print(f"{vendor_emoji} {find['vendor']}: {find['name']}")
    
    print(f"\n✅ PART 1 COMPLETE! Ready for PART 2: Organization")
    print(f"🗂️  Run part2_organizer.py to organize everything!")

if __name__ == "__main__":
    main()
