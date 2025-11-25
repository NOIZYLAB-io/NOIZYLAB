#!/usr/bin/env python3
# ==============================================================================
# THE LIBRARIAN - INGEST TOOL
# ==============================================================================
# Add items to the catalog from CSV or command line
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

import yaml
import csv
import os
import sys
from pathlib import Path
from datetime import datetime

# ==============================================================================
# CONFIGURATION
# ==============================================================================

REGISTRY_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = REGISTRY_ROOT / "data"
CATALOG_FILE = DATA_DIR / "catalog.yaml"

# ==============================================================================
# COLORS
# ==============================================================================

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
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

def save_catalog(catalog):
    """Save the catalog YAML file."""
    with open(CATALOG_FILE, 'w') as f:
        yaml.dump(catalog, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    print(f"{Colors.GREEN}Catalog saved: {CATALOG_FILE}{Colors.END}")

def generate_item_id(items, item_type):
    """Generate a unique item ID."""
    prefix_map = {
        "daw": "daw",
        "plugin": "plug",
        "instrument": "inst",
        "ai_model": "ai"
    }
    prefix = prefix_map.get(item_type, "item")

    existing_nums = []
    for item in items:
        item_id = item.get("itemId", "")
        if item_id.startswith(prefix + "-"):
            try:
                num = int(item_id.split("-")[1])
                existing_nums.append(num)
            except (IndexError, ValueError):
                pass

    next_num = max(existing_nums, default=0) + 1
    return f"{prefix}-{next_num:03d}"

def add_item(catalog, item_data):
    """Add a single item to the catalog."""
    items = catalog.get("items", [])

    # Generate ID if not provided
    if "itemId" not in item_data:
        item_data["itemId"] = generate_item_id(items, item_data.get("type", "item"))

    # Set default status
    if "status" not in item_data:
        item_data["status"] = "active"

    # Add to catalog
    items.append(item_data)
    catalog["items"] = items

    print(f"{Colors.GREEN}[ADDED] {item_data['name']} ({item_data['itemId']}){Colors.END}")
    return item_data["itemId"]

def import_csv(catalog, csv_file):
    """Import items from CSV file."""
    if not os.path.exists(csv_file):
        print(f"{Colors.RED}[ERROR] CSV file not found: {csv_file}{Colors.END}")
        return 0

    count = 0
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse list fields
            item = {
                "name": row.get("name"),
                "type": row.get("type"),
                "category": row.get("category"),
                "developer": row.get("developer"),
            }

            # Optional fields
            if row.get("format"):
                item["format"] = [f.strip() for f in row["format"].split(",")]
            if row.get("os"):
                item["os"] = [o.strip() for o in row["os"].split(",")]
            if row.get("releaseYear"):
                item["releaseYear"] = int(row["releaseYear"])
            if row.get("tags"):
                item["tags"] = [t.strip() for t in row["tags"].split(",")]
            if row.get("status"):
                item["status"] = row["status"]
            if row.get("url"):
                item["urls"] = {"home": row["url"]}
            if row.get("notes"):
                item["notes"] = row["notes"]

            add_item(catalog, item)
            count += 1

    print(f"\n{Colors.GREEN}Imported {count} items from {csv_file}{Colors.END}")
    return count

def interactive_add(catalog):
    """Interactive mode to add items."""
    print(f"\n{Colors.BOLD}Add New Item{Colors.END}")
    print("-" * 40)

    name = input("Name: ").strip()
    if not name:
        print(f"{Colors.RED}Name is required{Colors.END}")
        return

    print("\nTypes: daw, plugin, instrument, ai_model")
    item_type = input("Type: ").strip().lower()

    print("\nCategories: daw, synth, sampler, drum, orchestral, eq, compressor,")
    print("            reverb, delay, saturation, pitch, spectral, utility, etc.")
    category = input("Category: ").strip().lower()

    developer = input("Developer: ").strip()

    print("\nFormats (comma-separated): VST3, AU, AAX, CLAP, Standalone")
    formats_str = input("Formats: ").strip()
    formats = [f.strip() for f in formats_str.split(",")] if formats_str else None

    print("\nOS (comma-separated): macOS, Windows, Linux")
    os_str = input("OS: ").strip()
    os_list = [o.strip() for o in os_str.split(",")] if os_str else None

    year_str = input("Release Year: ").strip()
    year = int(year_str) if year_str else None

    tags_str = input("Tags (comma-separated): ").strip()
    tags = [t.strip() for t in tags_str.split(",")] if tags_str else None

    url = input("URL: ").strip()
    notes = input("Notes: ").strip()

    item_data = {
        "name": name,
        "type": item_type,
        "category": category,
        "developer": developer,
    }

    if formats:
        item_data["format"] = formats
    if os_list:
        item_data["os"] = os_list
    if year:
        item_data["releaseYear"] = year
    if tags:
        item_data["tags"] = tags
    if url:
        item_data["urls"] = {"home": url}
    if notes:
        item_data["notes"] = notes

    add_item(catalog, item_data)
    save_catalog(catalog)

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add items to the Audio Canon catalog")
    parser.add_argument("--csv", "-c", type=str, help="Import from CSV file")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")

    # Direct add flags
    parser.add_argument("--name", type=str, help="Item name")
    parser.add_argument("--type", type=str, help="Item type")
    parser.add_argument("--category", type=str, help="Item category")
    parser.add_argument("--developer", type=str, help="Developer name")
    parser.add_argument("--format", type=str, nargs="+", help="Formats")
    parser.add_argument("--os", type=str, nargs="+", help="Operating systems")
    parser.add_argument("--year", type=int, help="Release year")
    parser.add_argument("--tags", type=str, nargs="+", help="Tags")
    parser.add_argument("--url", type=str, help="Home URL")
    parser.add_argument("--notes", type=str, help="Notes")

    args = parser.parse_args()

    catalog = load_catalog()
    if not catalog:
        sys.exit(1)

    if args.csv:
        import_csv(catalog, args.csv)
        save_catalog(catalog)
    elif args.interactive:
        interactive_add(catalog)
    elif args.name:
        item_data = {
            "name": args.name,
            "type": args.type,
            "category": args.category,
            "developer": args.developer,
        }
        if args.format:
            item_data["format"] = args.format
        if args.os:
            item_data["os"] = args.os
        if args.year:
            item_data["releaseYear"] = args.year
        if args.tags:
            item_data["tags"] = args.tags
        if args.url:
            item_data["urls"] = {"home": args.url}
        if args.notes:
            item_data["notes"] = args.notes

        add_item(catalog, item_data)
        save_catalog(catalog)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
