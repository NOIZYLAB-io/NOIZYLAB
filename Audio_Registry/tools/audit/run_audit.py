#!/usr/bin/env python3
# ==============================================================================
# THE LIBRARIAN - AUDIT TOOL
# ==============================================================================
# Catalog audit and health check script
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

import yaml
import json
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

REQUIRED_FIELDS = ["name", "type", "category", "developer"]
RECOMMENDED_FIELDS = ["format", "os", "releaseYear", "status", "urls"]

# ==============================================================================
# COLORS
# ==============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ==============================================================================
# AUDIT FUNCTIONS
# ==============================================================================

def load_catalog():
    """Load the catalog YAML file."""
    if not CATALOG_FILE.exists():
        print(f"{Colors.RED}[ERROR] Catalog not found: {CATALOG_FILE}{Colors.END}")
        return None

    with open(CATALOG_FILE, 'r') as f:
        return yaml.safe_load(f)

def audit_completeness(items):
    """Check for missing required and recommended fields."""
    issues = {
        "missing_required": [],
        "missing_recommended": [],
        "empty_values": []
    }

    for item in items:
        item_id = item.get("itemId", "UNKNOWN")
        name = item.get("name", "UNKNOWN")

        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in item or not item[field]:
                issues["missing_required"].append({
                    "itemId": item_id,
                    "name": name,
                    "field": field
                })

        # Check recommended fields
        for field in RECOMMENDED_FIELDS:
            if field not in item or not item[field]:
                issues["missing_recommended"].append({
                    "itemId": item_id,
                    "name": name,
                    "field": field
                })

    return issues

def count_by_field(items, field):
    """Count items by a specific field."""
    counts = defaultdict(int)
    for item in items:
        value = item.get(field)
        if isinstance(value, list):
            for v in value:
                counts[v] += 1
        elif value:
            counts[value] += 1
        else:
            counts["UNKNOWN"] += 1
    return dict(sorted(counts.items(), key=lambda x: -x[1]))

def decade_distribution(items):
    """Count items by decade."""
    decades = defaultdict(int)
    for item in items:
        year = item.get("releaseYear")
        if year:
            decade = f"{(year // 10) * 10}s"
            decades[decade] += 1
    return dict(sorted(decades.items()))

def health_check(items):
    """Perform health checks on the catalog."""
    health = {
        "total_items": len(items),
        "active": 0,
        "legacy": 0,
        "discontinued": 0,
        "os_coverage": {"macOS": 0, "Windows": 0, "Linux": 0},
        "format_coverage": defaultdict(int),
        "has_url": 0,
        "has_year": 0,
        "health_score": 0
    }

    for item in items:
        status = item.get("status", "unknown")
        if status == "active":
            health["active"] += 1
        elif status == "legacy":
            health["legacy"] += 1
        elif status == "discontinued":
            health["discontinued"] += 1

        for os_name in item.get("os", []):
            if os_name in health["os_coverage"]:
                health["os_coverage"][os_name] += 1

        for fmt in item.get("format", []):
            health["format_coverage"][fmt] += 1

        if item.get("urls"):
            health["has_url"] += 1

        if item.get("releaseYear"):
            health["has_year"] += 1

    # Calculate health score (0-100)
    total = health["total_items"]
    if total > 0:
        url_pct = (health["has_url"] / total) * 25
        year_pct = (health["has_year"] / total) * 25
        active_pct = (health["active"] / total) * 30
        os_pct = min(health["os_coverage"]["macOS"], health["os_coverage"]["Windows"]) / total * 20
        health["health_score"] = int(url_pct + year_pct + active_pct + os_pct)

    return health

def print_report(catalog):
    """Print the audit report."""
    items = catalog.get("items", [])

    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}  THE LIBRARIAN - CATALOG AUDIT REPORT{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}  Generated: {datetime.now().isoformat()}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")

    # Summary
    print(f"{Colors.BOLD}SUMMARY{Colors.END}")
    print(f"{'─'*40}")
    print(f"  Total Items: {Colors.BOLD}{len(items)}{Colors.END}")

    # By Type
    print(f"\n{Colors.BOLD}BY TYPE{Colors.END}")
    print(f"{'─'*40}")
    type_counts = count_by_field(items, "type")
    for t, c in type_counts.items():
        print(f"  {t:20} {c:5}")

    # By Category
    print(f"\n{Colors.BOLD}BY CATEGORY{Colors.END}")
    print(f"{'─'*40}")
    cat_counts = count_by_field(items, "category")
    for cat, c in list(cat_counts.items())[:15]:
        print(f"  {cat:20} {c:5}")

    # By Developer (Top 15)
    print(f"\n{Colors.BOLD}TOP DEVELOPERS{Colors.END}")
    print(f"{'─'*40}")
    dev_counts = count_by_field(items, "developer")
    for dev, c in list(dev_counts.items())[:15]:
        print(f"  {dev:30} {c:5}")

    # By Decade
    print(f"\n{Colors.BOLD}BY DECADE{Colors.END}")
    print(f"{'─'*40}")
    decades = decade_distribution(items)
    for decade, c in decades.items():
        bar = '█' * (c // 2)
        print(f"  {decade:10} {c:5} {Colors.CYAN}{bar}{Colors.END}")

    # Health Check
    health = health_check(items)
    print(f"\n{Colors.BOLD}HEALTH CHECK{Colors.END}")
    print(f"{'─'*40}")

    score = health["health_score"]
    if score >= 80:
        score_color = Colors.GREEN
    elif score >= 60:
        score_color = Colors.YELLOW
    else:
        score_color = Colors.RED

    print(f"  Health Score: {score_color}{score}/100{Colors.END}")
    print(f"  Active Items: {health['active']}")
    print(f"  Legacy Items: {health['legacy']}")
    print(f"  Discontinued: {health['discontinued']}")
    print(f"  Items with URLs: {health['has_url']}")
    print(f"  Items with Year: {health['has_year']}")

    print(f"\n{Colors.BOLD}OS COVERAGE{Colors.END}")
    print(f"{'─'*40}")
    for os_name, c in health["os_coverage"].items():
        pct = (c / len(items) * 100) if items else 0
        print(f"  {os_name:15} {c:5} ({pct:.1f}%)")

    print(f"\n{Colors.BOLD}FORMAT COVERAGE{Colors.END}")
    print(f"{'─'*40}")
    for fmt, c in sorted(health["format_coverage"].items(), key=lambda x: -x[1]):
        print(f"  {fmt:15} {c:5}")

    # Completeness Issues
    issues = audit_completeness(items)

    if issues["missing_required"]:
        print(f"\n{Colors.RED}{Colors.BOLD}MISSING REQUIRED FIELDS{Colors.END}")
        print(f"{'─'*40}")
        for issue in issues["missing_required"][:10]:
            print(f"  [{issue['itemId']}] {issue['name']}: missing '{issue['field']}'")
        if len(issues["missing_required"]) > 10:
            print(f"  ... and {len(issues['missing_required']) - 10} more")

    if len(issues["missing_recommended"]) > 0:
        missing_rec_count = len(issues["missing_recommended"])
        print(f"\n{Colors.YELLOW}{Colors.BOLD}MISSING RECOMMENDED FIELDS: {missing_rec_count}{Colors.END}")

    print(f"\n{Colors.GREEN}Audit complete!{Colors.END}\n")

    return health

def export_audit_json(catalog, output_path):
    """Export audit results to JSON."""
    items = catalog.get("items", [])

    audit_data = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "total_items": len(items),
            "by_type": count_by_field(items, "type"),
            "by_category": count_by_field(items, "category"),
            "by_developer": count_by_field(items, "developer"),
            "by_decade": decade_distribution(items)
        },
        "health": health_check(items),
        "issues": audit_completeness(items)
    }

    with open(output_path, 'w') as f:
        json.dump(audit_data, f, indent=2)

    print(f"{Colors.GREEN}Audit exported to: {output_path}{Colors.END}")

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Audit the Audio Canon catalog")
    parser.add_argument("--json", "-j", type=str, help="Export audit to JSON file")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only show summary")

    args = parser.parse_args()

    catalog = load_catalog()
    if not catalog:
        sys.exit(1)

    if args.json:
        export_audit_json(catalog, args.json)
    else:
        print_report(catalog)

if __name__ == "__main__":
    main()
