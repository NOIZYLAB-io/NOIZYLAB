#!/usr/bin/env python3
# ==============================================================================
# THE LIBRARIAN - EXPORT TOOL
# ==============================================================================
# Export catalog to JSON/CSV for MissionControl96 dashboards
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

import yaml
import json
import csv
import hashlib
import os
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ==============================================================================
# CONFIGURATION
# ==============================================================================

REGISTRY_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = REGISTRY_ROOT / "data"
CATALOG_FILE = DATA_DIR / "catalog.yaml"
INDEX_FILE = DATA_DIR / "index.json"
CHECKSUMS_DIR = REGISTRY_ROOT / "checksums"

# ==============================================================================
# COLORS
# ==============================================================================

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def load_catalog():
    """Load the catalog YAML file."""
    if not CATALOG_FILE.exists():
        print(f"{Colors.RED}[ERROR] Catalog not found: {CATALOG_FILE}{Colors.END}")
        return None

    with open(CATALOG_FILE, 'r') as f:
        return yaml.safe_load(f)

def compute_stats(items):
    """Compute statistics for the catalog."""
    stats = {
        "byType": defaultdict(int),
        "byCategory": defaultdict(int),
        "byStatus": defaultdict(int),
        "byOS": {"macOS": 0, "Windows": 0, "Linux": 0},
        "byFormat": defaultdict(int),
        "byDeveloper": defaultdict(int),
        "byDecade": defaultdict(int)
    }

    for item in items:
        stats["byType"][item.get("type", "unknown")] += 1
        stats["byCategory"][item.get("category", "unknown")] += 1
        stats["byStatus"][item.get("status", "unknown")] += 1

        for os_name in item.get("os", []):
            if os_name in stats["byOS"]:
                stats["byOS"][os_name] += 1

        for fmt in item.get("format", []):
            stats["byFormat"][fmt] += 1

        stats["byDeveloper"][item.get("developer", "unknown")] += 1

        year = item.get("releaseYear")
        if year:
            decade = f"{(year // 10) * 10}s"
            stats["byDecade"][decade] += 1

    # Convert defaultdicts to regular dicts and sort
    return {
        "byType": dict(stats["byType"]),
        "byCategory": dict(sorted(stats["byCategory"].items(), key=lambda x: -x[1])),
        "byStatus": dict(stats["byStatus"]),
        "byOS": stats["byOS"],
        "byFormat": dict(sorted(stats["byFormat"].items(), key=lambda x: -x[1])),
        "byDeveloper": dict(sorted(stats["byDeveloper"].items(), key=lambda x: -x[1])[:20]),
        "byDecade": dict(sorted(stats["byDecade"].items()))
    }

def export_json(catalog, output_path):
    """Export catalog to JSON format for dashboards."""
    items = catalog.get("items", [])
    meta = catalog.get("meta", {})

    # Build compact index
    index = {
        "meta": {
            "catalogName": meta.get("catalogName", "Audio Canon"),
            "version": meta.get("version", "1.0.0"),
            "generatedAt": datetime.now().isoformat(),
            "owner": meta.get("owner", "NOIZYLAB"),
            "itemCount": len(items),
            "lastExport": datetime.now().strftime("%Y-%m-%d")
        },
        "stats": compute_stats(items),
        "items": [],
        "filterOptions": {
            "types": list(set(i.get("type") for i in items if i.get("type"))),
            "categories": list(set(i.get("category") for i in items if i.get("category"))),
            "status": ["active", "legacy", "discontinued"],
            "os": ["macOS", "Windows", "Linux"],
            "formats": list(set(f for i in items for f in i.get("format", [])))
        }
    }

    # Add compact items
    for item in items:
        compact_item = {
            "id": item.get("itemId"),
            "name": item.get("name"),
            "type": item.get("type"),
            "category": item.get("category"),
            "developer": item.get("developer"),
            "status": item.get("status", "active")
        }

        if item.get("releaseYear"):
            compact_item["year"] = item["releaseYear"]
        if item.get("tags"):
            compact_item["tags"] = item["tags"]
        if item.get("urls", {}).get("home"):
            compact_item["url"] = item["urls"]["home"]

        index["items"].append(compact_item)

    # Write JSON
    with open(output_path, 'w') as f:
        json.dump(index, f, indent=2)

    print(f"{Colors.GREEN}[EXPORTED] JSON: {output_path}{Colors.END}")

    # Generate checksum
    generate_checksum(output_path)

    return output_path

def export_csv(catalog, output_path):
    """Export catalog to CSV format."""
    items = catalog.get("items", [])

    fieldnames = [
        "itemId", "name", "type", "category", "developer",
        "format", "os", "releaseYear", "status", "tags", "url", "notes"
    ]

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in items:
            row = {
                "itemId": item.get("itemId"),
                "name": item.get("name"),
                "type": item.get("type"),
                "category": item.get("category"),
                "developer": item.get("developer"),
                "format": ",".join(item.get("format", [])),
                "os": ",".join(item.get("os", [])),
                "releaseYear": item.get("releaseYear", ""),
                "status": item.get("status", ""),
                "tags": ",".join(item.get("tags", [])),
                "url": item.get("urls", {}).get("home", ""),
                "notes": item.get("notes", "")
            }
            writer.writerow(row)

    print(f"{Colors.GREEN}[EXPORTED] CSV: {output_path}{Colors.END}")
    return output_path

def export_developers(catalog, output_path):
    """Export developer constellation data."""
    items = catalog.get("items", [])

    developers = defaultdict(lambda: {
        "items": [],
        "types": set(),
        "categories": set()
    })

    for item in items:
        dev = item.get("developer", "Unknown")
        developers[dev]["items"].append({
            "id": item.get("itemId"),
            "name": item.get("name"),
            "type": item.get("type"),
            "category": item.get("category")
        })
        developers[dev]["types"].add(item.get("type"))
        developers[dev]["categories"].add(item.get("category"))

    # Convert to serializable format
    dev_data = {}
    for dev, data in developers.items():
        dev_data[dev] = {
            "itemCount": len(data["items"]),
            "types": list(data["types"]),
            "categories": list(data["categories"]),
            "items": data["items"]
        }

    with open(output_path, 'w') as f:
        json.dump(dev_data, f, indent=2)

    print(f"{Colors.GREEN}[EXPORTED] Developers: {output_path}{Colors.END}")
    return output_path

def generate_checksum(file_path):
    """Generate MD5 checksum for a file."""
    CHECKSUMS_DIR.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'rb') as f:
        md5_hash = hashlib.md5(f.read()).hexdigest()

    checksum_file = CHECKSUMS_DIR / f"{Path(file_path).name}.md5"
    with open(checksum_file, 'w') as f:
        f.write(f"{md5_hash}  {Path(file_path).name}\n")

    print(f"{Colors.CYAN}[CHECKSUM] {md5_hash}{Colors.END}")
    return md5_hash

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Export Audio Canon catalog")
    parser.add_argument("--format", "-f", choices=["json", "csv", "developers", "all"],
                       default="json", help="Export format")
    parser.add_argument("--output", "-o", type=str, help="Output file path")

    args = parser.parse_args()

    catalog = load_catalog()
    if not catalog:
        sys.exit(1)

    if args.format == "json" or args.format == "all":
        output = args.output or INDEX_FILE
        export_json(catalog, output)

    if args.format == "csv" or args.format == "all":
        output = args.output or (DATA_DIR / "catalog.csv")
        export_csv(catalog, output)

    if args.format == "developers" or args.format == "all":
        output = args.output or (DATA_DIR / "developers.json")
        export_developers(catalog, output)

if __name__ == "__main__":
    main()
