#!/usr/bin/env python3
# filepath: /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/artwork_hunter.py
"""
NOIZYGENIE: ARTWORK HUNTER - VISUAL ASSET & ARTWORK SCANNER
Finds ALL artwork, graphics, covers, icons, and visual assets
Enhanced Mission Control with artwork detection for your music libraries! 🎨🖼️
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

# ARTWORK & IMAGE FILE EXTENSIONS
ARTWORK_EXTENSIONS = {
    # Standard image formats
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp',
    '.svg', '.eps', '.psd', '.ai', '.ico', '.icns',
    
    # Raw formats
    '.raw', '.cr2', '.nef', '.arw', '.dng',
    
    # PDF with potential artwork
    '.pdf'
}

# ARTWORK-SPECIFIC NAMING PATTERNS
ARTWORK_PATTERNS = [
    # Album/Library covers
    'cover', 'artwork', 'album', 'front', 'back', 'booklet', 'sleeve',
    'poster', 'banner', 'header', 'thumb', 'thumbnail', 'preview',
    
    # Music-specific artwork
    'vinyl', 'cd', 'disc', 'label', 'inlay', 'insert', 'liner',
    'gatefold', 'digipak', 'jewel', 'case',
    
    # Library artwork
    'library', 'instrument', 'plugin', 'preset', 'sample', 'loop',
    'pack', 'collection', 'bundle', 'kit',
    
    # Generic artwork terms
    'image', 'photo', 'picture', 'graphic', 'visual', 'design',
    'logo', 'icon', 'badge', 'emblem', 'symbol',
    
    # Specific vendor artwork patterns
    'spitfire', 'native', 'kontakt', 'eastwest', 'output', 'spectrasonics',
    'labs', 'bbc', 'abbey', 'albion', 'hans', 'zimmer',
    
    # Wallpapers and backgrounds
    'wallpaper', 'background', 'backdrop', 'desktop', 'screen',
    'splash', 'loading', 'intro'
]

# ENHANCED VENDOR PATTERNS (from original scanner)
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
    "Output": [
        "output", "analog strings", "rev", "exhale", "signal", "substance",
        "movement", "portal", "thermal", "arcade"
    ],
    "Spectrasonics": [
        "spectrasonics", "omnisphere", "trilogy", "keyscapes", "stylus rmx",
        "stylus", "rmx", "omnisphere 2", "trilian", "keyscape"
    ]
}

# ARTWORK SCAN LOCATIONS
ARTWORK_SCAN_LOCATIONS = [
    # Applications (app icons and resources)
    "/Applications",
    
    # User directories
    "~/Pictures",
    "~/Desktop",
    "~/Documents",
    "~/Downloads",
    "~/Music",
    
    # Library locations
    "~/Library/Application Support",
    "/Library/Application Support",
    
    # Common artwork locations
    "~/Library/Application Support/Native Instruments",
    "~/Library/Application Support/Arturia", 
    "~/Library/Application Support/iZotope",
    "~/Library/Application Support/Output",
    "~/Library/Application Support/Spectrasonics",
    
    # External volumes
    "/Volumes",
    
    # Specific music software locations
    "~/Music/Audio Music Apps",
    "~/Library/Containers",
    
    # Web browsers (downloaded artwork)
    "~/Library/Safari",
    "~/Library/Application Support/Google/Chrome",
    
    # System artwork
    "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources",
    "~/Library/Caches"
]

def get_image_info(image_path):
    """Get detailed information about an image file"""
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            return {
                "dimensions": f"{img.width}x{img.height}",
                "format": img.format,
                "mode": img.mode,
                "width": img.width,
                "height": img.height
            }
    except ImportError:
        # PIL not available, basic info only
        return {
            "dimensions": "Unknown",
            "format": "Unknown", 
            "mode": "Unknown",
            "width": 0,
            "height": 0
        }
    except Exception:
        return {
            "dimensions": "Error",
            "format": "Error",
            "mode": "Error", 
            "width": 0,
            "height": 0
        }

def is_artwork_related(file_path, filename):
    """Determine if a file is likely artwork/visual content"""
    filename_lower = filename.lower()
    path_lower = str(file_path).lower()
    
    # Check filename patterns
    for pattern in ARTWORK_PATTERNS:
        if pattern in filename_lower or pattern in path_lower:
            return True, pattern
    
    # Check if in artwork-related directories
    artwork_dirs = [
        'artwork', 'images', 'pictures', 'graphics', 'icons', 'covers',
        'resources', 'assets', 'media', 'visuals', 'art', 'design'
    ]
    
    for artwork_dir in artwork_dirs:
        if artwork_dir in path_lower:
            return True, f"directory:{artwork_dir}"
    
    return False, None

def get_vendor_from_path(file_path):
    """Identify vendor from file path"""
    path_lower = str(file_path).lower()
    
    for vendor, patterns in COMPREHENSIVE_VENDOR_PATTERNS.items():
        for pattern in patterns:
            if pattern.lower() in path_lower:
                return vendor
    
    return "Unknown"

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

def scan_artwork_location(location_path, artwork_data, max_depth=4, current_depth=0):
    """Scan a specific location for artwork and visual assets"""
    if current_depth > max_depth:
        return
    
    try:
        location = Path(location_path).expanduser()
        if not location.exists() or not location.is_dir():
            return
        
        print(f"🎨 Scanning for artwork: {location} (depth {current_depth})")
        
        for item in location.iterdir():
            try:
                if item.is_file() and item.suffix.lower() in ARTWORK_EXTENSIONS:
                    # Found an image file
                    filename = item.name
                    is_artwork, pattern = is_artwork_related(item, filename)
                    
                    try:
                        size = item.stat().st_size
                        created = datetime.fromtimestamp(item.stat().st_ctime)
                        modified = datetime.fromtimestamp(item.stat().st_mtime)
                    except (OSError, IOError):
                        size = 0
                        created = datetime.now()
                        modified = datetime.now()
                    
                    # Get image details
                    image_info = get_image_info(item)
                    
                    # Determine vendor
                    vendor = get_vendor_from_path(item)
                    
                    artwork_info = {
                        "name": filename,
                        "path": str(item),
                        "size_bytes": size,
                        "size_formatted": format_size(size),
                        "extension": item.suffix.lower(),
                        "vendor": vendor,
                        "is_artwork": is_artwork,
                        "artwork_pattern": pattern,
                        "location_category": str(location_path),
                        "depth": current_depth,
                        "created": created.isoformat(),
                        "modified": modified.isoformat(),
                        "image_info": image_info
                    }
                    
                    artwork_data["all_images"].append(artwork_info)
                    artwork_data["total_size_bytes"] += size
                    
                    if is_artwork:
                        artwork_data["artwork_files"].append(artwork_info)
                        artwork_data["by_pattern"][pattern].append(artwork_info)
                        
                        if vendor != "Unknown":
                            artwork_data["by_vendor"][vendor].append(artwork_info)
                            
                            # Special highlighting for priority vendors
                            if vendor in ["Spitfire Audio", "LA Scoring Strings", "Genesis Children's Choir", "Native Instruments"]:
                                artwork_data["priority_artwork"].append(artwork_info)
                        
                        vendor_emoji = {
                            "Spitfire Audio": "🎼",
                            "LA Scoring Strings": "🎻",
                            "Genesis Children's Choir": "👶",
                            "Native Instruments": "🎵",
                            "EastWest": "🎭",
                            "Spectrasonics": "🎹",
                            "Output": "⚡"
                        }.get(vendor, "🎨")
                        
                        print(f"  {vendor_emoji} ARTWORK: {filename} ({format_size(size)}) - {vendor} - {image_info['dimensions']}")
                    
                    # Check for high-resolution artwork
                    if image_info.get('width', 0) >= 1000 or image_info.get('height', 0) >= 1000:
                        artwork_data["high_res_artwork"].append(artwork_info)
                
                elif item.is_dir():
                    # Skip system directories and hidden files
                    item_name = item.name.lower()
                    if (item_name.startswith('.') or 
                        item_name in ['system', 'private', 'tmp', 'var', 'dev', 'cores', 'bin', 'sbin', 'usr']):
                        continue
                    
                    # Recursively scan subdirectories (with depth limit)
                    if current_depth < max_depth:
                        scan_artwork_location(item, artwork_data, max_depth, current_depth + 1)
            
            except (PermissionError, OSError):
                # Skip items we can't access
                continue
    
    except (PermissionError, OSError) as e:
        print(f"  ⚠️  No access to {location_path}")

def artwork_hunter_scan():
    """Execute Artwork Hunter system-wide scan"""
    print("🎨 ARTWORK HUNTER: SYSTEM-WIDE VISUAL ASSET SCANNER")
    print("🖼️  Finding ALL artwork, covers, graphics, and visual assets!")
    print("⚡" * 80)
    
    start_time = datetime.now()
    
    artwork_data = {
        "scan_date": start_time.isoformat(),
        "total_images": 0,
        "total_artwork": 0,
        "total_size_bytes": 0,
        "all_images": [],
        "artwork_files": [],
        "high_res_artwork": [],
        "by_vendor": defaultdict(list),
        "by_pattern": defaultdict(list),
        "priority_artwork": [],
        "scan_locations": [],
        "scan_stats": {
            "locations_scanned": 0,
            "locations_accessible": 0,
            "errors": []
        }
    }
    
    # Scan all locations
    for location in ARTWORK_SCAN_LOCATIONS:
        location_path = Path(location).expanduser()
        artwork_data["scan_stats"]["locations_scanned"] += 1
        
        try:
            if location_path.exists():
                artwork_data["scan_stats"]["locations_accessible"] += 1
                artwork_data["scan_locations"].append(str(location_path))
                
                # Limit scan depth based on location type
                if str(location_path).startswith('/Applications'):
                    max_depth = 3  # Deeper for apps to find resources
                elif 'Pictures' in str(location_path) or 'Desktop' in str(location_path):
                    max_depth = 5  # Deeper for user image directories
                else:
                    max_depth = 3
                
                scan_artwork_location(location_path, artwork_data, max_depth=max_depth)
            else:
                print(f"⚠️  Location not found: {location}")
        except Exception as e:
            error_msg = f"Error scanning {location}: {str(e)}"
            artwork_data["scan_stats"]["errors"].append(error_msg)
            print(f"❌ {error_msg}")
    
    # Update totals
    artwork_data["total_images"] = len(artwork_data["all_images"])
    artwork_data["total_artwork"] = len(artwork_data["artwork_files"])
    
    # Save results
    output_dir = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/ARTWORK_HUNTER_RESULTS")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results_file = output_dir / f"ARTWORK_SCAN_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Convert defaultdict to regular dict for JSON serialization
    artwork_data["by_vendor"] = dict(artwork_data["by_vendor"])
    artwork_data["by_pattern"] = dict(artwork_data["by_pattern"])
    
    with open(results_file, 'w') as f:
        json.dump(artwork_data, f, indent=2, default=str)
    
    # Generate summary report
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "🎉" * 80)
    print("🎨 ARTWORK HUNTER SCAN COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Duration: {duration:.1f} seconds")
    print(f"🖼️  Total Images Found: {artwork_data['total_images']}")
    print(f"🎨 Artwork Files: {artwork_data['total_artwork']}")
    print(f"📐 High-Res Artwork: {len(artwork_data['high_res_artwork'])}")
    print(f"💾 Total Size: {format_size(artwork_data['total_size_bytes'])}")
    print(f"📁 Locations Scanned: {artwork_data['scan_stats']['locations_scanned']}")
    print(f"✅ Accessible Locations: {artwork_data['scan_stats']['locations_accessible']}")
    print(f"📄 Results Saved: {results_file}")
    
    print("\n🎼 PRIORITY VENDOR ARTWORK:")
    for artwork in artwork_data["priority_artwork"][:10]:  # Show top 10
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "LA Scoring Strings": "🎻",
            "Genesis Children's Choir": "👶",
            "Native Instruments": "🎵"
        }.get(artwork["vendor"], "🎨")
        
        dimensions = artwork["image_info"]["dimensions"]
        print(f"{vendor_emoji} {artwork['vendor']}: {artwork['name']} ({dimensions})")
    
    print("\n📊 ARTWORK BY PATTERN:")
    pattern_stats = Counter()
    for pattern, artworks in artwork_data["by_pattern"].items():
        pattern_stats[pattern] = len(artworks)
    
    for pattern, count in pattern_stats.most_common(10):
        print(f"🎨 {pattern}: {count} files")
    
    print("\n🏆 HIGH-RESOLUTION ARTWORK FINDINGS:")
    for artwork in sorted(artwork_data["high_res_artwork"], 
                         key=lambda x: x["image_info"].get("width", 0) * x["image_info"].get("height", 0), 
                         reverse=True)[:5]:
        dimensions = artwork["image_info"]["dimensions"]
        vendor = artwork["vendor"]
        print(f"📐 {artwork['name']} - {dimensions} - {vendor}")
    
    print("\n📈 VENDOR ARTWORK BREAKDOWN:")
    vendor_stats = Counter()
    for vendor, artworks in artwork_data["by_vendor"].items():
        vendor_stats[vendor] = len(artworks)
    
    for vendor, count in vendor_stats.most_common(8):
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "Native Instruments": "🎵",
            "EastWest": "🎭",
            "Spectrasonics": "🎹",
            "Output": "⚡"
        }.get(vendor, "🎨")
        print(f"{vendor_emoji} {vendor}: {count} artwork files")
    
    print(f"\n🎨 YOUR ENTIRE VISUAL ASSET COLLECTION HAS BEEN MAPPED!")
    print(f"🖼️  From library covers to high-res artwork - everything found!")
    
    return artwork_data

def create_artwork_gallery_html(artwork_data):
    """Create an HTML gallery of found artwork"""
    output_dir = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/ARTWORK_HUNTER_RESULTS")
    gallery_file = output_dir / "ARTWORK_GALLERY.html"
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎨 NOIZYGENIE ARTWORK GALLERY</title>
        <style>
            body { font-family: Arial, sans-serif; background: #1a1a1a; color: #fff; }
            .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 20px; }
            .artwork-item { background: #2a2a2a; border-radius: 10px; padding: 15px; }
            .artwork-item img { max-width: 100%; height: auto; border-radius: 5px; }
            .artwork-info { margin-top: 10px; }
            .vendor { color: #4CAF50; font-weight: bold; }
            .priority { border: 2px solid #FFD700; }
            h1 { text-align: center; color: #4CAF50; }
        </style>
    </head>
    <body>
        <h1>🎨 NOIZYGENIE ARTWORK GALLERY 🖼️</h1>
        <div class="gallery">
    """
    
    # Add priority artwork first
    for artwork in artwork_data["priority_artwork"][:50]:  # Limit to 50 for performance
        vendor_emoji = {
            "Spitfire Audio": "🎼",
            "LA Scoring Strings": "🎻", 
            "Genesis Children's Choir": "👶",
            "Native Instruments": "🎵"
        }.get(artwork["vendor"], "🎨")
        
        html_content += f"""
            <div class="artwork-item priority">
                <img src="file://{artwork['path']}" alt="{artwork['name']}" onerror="this.style.display='none'">
                <div class="artwork-info">
                    <div class="vendor">{vendor_emoji} {artwork['vendor']}</div>
                    <div>{artwork['name']}</div>
                    <div>{artwork['image_info']['dimensions']} - {artwork['size_formatted']}</div>
                </div>
            </div>
        """
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    with open(gallery_file, 'w') as f:
        f.write(html_content)
    
    print(f"🖼️  HTML Gallery Created: {gallery_file}")
    return gallery_file

def main():
    """Execute Artwork Hunter scan"""
    artwork_data = artwork_hunter_scan()
    
    # Create HTML gallery
    gallery_file = create_artwork_gallery_html(artwork_data)
    
    print(f"\n🎨 ARTWORK HUNTING COMPLETE!")
    print(f"🖼️  Open {gallery_file} in your browser to view the gallery!")
    
    return artwork_data

if __name__ == "__main__":
    main()