#!/usr/bin/env python3
"""
MC96 Dedupe Analyzer v2.0
=========================
Analyzes truth scanner TSV files to find duplicates and generate fix queue.

Usage:
    python3 mc96_dedupe.py <tsv_file> [--output-dir DIR] [--json] [--quarantine-script]
"""

import csv
import sys
import os
import json
import hashlib
from collections import defaultdict
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# === CONFIGURATION ===
JUNK_PATTERNS = {
    '.DS_Store',
    'Thumbs.db',
    'desktop.ini',
    '._.DS_Store',
    '__MACOSX',
    '.Spotlight-V100',
    '.Trashes',
    '.fseventsd',
}

JUNK_EXTENSIONS = {
    '.tmp', '.temp', '.swp', '.swo', '.bak', '.orig',
}

# Priority paths - files here are preferred as "canonical"
PRIORITY_PATHS = [
    '/Users/m2ultra/NOIZYLAB/',
    '/Users/m2ultra/Documents/',
    '/Users/m2ultra/Desktop/',
]

class DedupeAnalyzer:
    def __init__(self, tsv_path: str, output_dir: Optional[str] = None):
        self.tsv_path = Path(tsv_path)
        self.output_dir = Path(output_dir) if output_dir else self.tsv_path.parent
        self.by_hash: Dict[str, List[dict]] = defaultdict(list)
        self.junk_files: List[dict] = []
        self.permission_anomalies: List[dict] = []
        self.stats = {
            'total_files': 0,
            'unique_hashes': 0,
            'duplicate_groups': 0,
            'duplicate_files': 0,
            'wasted_space': 0,
            'junk_files': 0,
            'junk_size': 0,
        }

    def load_tsv(self) -> None:
        """Load and parse the TSV file."""
        print(f"📂 Loading: {self.tsv_path}")

        with open(self.tsv_path, newline='') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                self.stats['total_files'] += 1
                h = row.get('sha256', '').strip()
                path = row.get('path', '')
                size = int(row.get('size', 0))
                mode = row.get('mode', '')

                # Check for junk files
                filename = os.path.basename(path)
                ext = os.path.splitext(filename)[1].lower()

                if filename in JUNK_PATTERNS or ext in JUNK_EXTENSIONS:
                    self.junk_files.append(row)
                    self.stats['junk_files'] += 1
                    self.stats['junk_size'] += size
                    continue

                # Check for permission anomalies (world-writable, etc.)
                if mode and len(mode) >= 4:
                    # Check if world-writable (mode ends in 7, 6, 3, 2)
                    last_digit = mode[-1]
                    if last_digit in '2367':
                        self.permission_anomalies.append(row)

                if h:
                    self.by_hash[h].append(row)

        self.stats['unique_hashes'] = len(self.by_hash)
        print(f"✅ Loaded {self.stats['total_files']} files, {self.stats['unique_hashes']} unique hashes")

    def find_duplicates(self) -> List[Tuple[str, List[dict]]]:
        """Find all duplicate groups."""
        dupes = []
        for h, rows in self.by_hash.items():
            if len(rows) > 1:
                dupes.append((h, rows))
                self.stats['duplicate_groups'] += 1
                self.stats['duplicate_files'] += len(rows) - 1  # -1 for canonical
                # Wasted space = size * (count - 1)
                self.stats['wasted_space'] += int(rows[0].get('size', 0)) * (len(rows) - 1)

        # Sort by number of duplicates (most first)
        dupes.sort(key=lambda x: len(x[1]), reverse=True)
        return dupes

    def select_canonical(self, files: List[dict]) -> Tuple[dict, List[dict]]:
        """Select the canonical file to keep from a duplicate group."""
        def score(f: dict) -> int:
            path = f.get('path', '')
            s = 0
            # Prefer priority paths
            for i, pp in enumerate(PRIORITY_PATHS):
                if path.startswith(pp):
                    s += (len(PRIORITY_PATHS) - i) * 100
                    break
            # Prefer shorter paths
            s -= len(path)
            # Prefer newer mtime
            try:
                mtime = datetime.strptime(f.get('mtime', ''), '%Y-%m-%d %H:%M:%S')
                s += mtime.timestamp() / 1000000  # Small boost for newer
            except:
                pass
            return s

        sorted_files = sorted(files, key=score, reverse=True)
        return sorted_files[0], sorted_files[1:]

    def generate_report(self, limit: int = 50) -> str:
        """Generate a human-readable report."""
        dupes = self.find_duplicates()

        lines = [
            "=" * 70,
            "MC96 DEDUPE ANALYSIS REPORT",
            "=" * 70,
            f"Source: {self.tsv_path.name}",
            f"Generated: {datetime.now().isoformat()}",
            "",
            "STATISTICS",
            "-" * 70,
            f"Total files scanned:     {self.stats['total_files']:,}",
            f"Unique file hashes:      {self.stats['unique_hashes']:,}",
            f"Duplicate groups:        {self.stats['duplicate_groups']:,}",
            f"Duplicate files:         {self.stats['duplicate_files']:,}",
            f"Wasted space:            {self.stats['wasted_space'] / 1024 / 1024:.2f} MB",
            f"Junk files found:        {self.stats['junk_files']:,}",
            f"Junk size:               {self.stats['junk_size'] / 1024 / 1024:.2f} MB",
            f"Permission anomalies:    {len(self.permission_anomalies):,}",
            "",
        ]

        if dupes:
            lines.extend([
                f"TOP {min(limit, len(dupes))} DUPLICATE GROUPS",
                "-" * 70,
            ])

            for h, rows in dupes[:limit]:
                canonical, extras = self.select_canonical(rows)
                size_mb = int(rows[0].get('size', 0)) / 1024 / 1024

                lines.append(f"\nSHA256: {h}")
                lines.append(f"Count: {len(rows)} | Size each: {size_mb:.2f} MB | Wasted: {size_mb * len(extras):.2f} MB")
                lines.append(f"  ✅ KEEP: {canonical.get('path', '')}")
                for ex in extras:
                    lines.append(f"  ❌ DUPE: {ex.get('path', '')}")

        if self.junk_files:
            lines.extend([
                "",
                f"JUNK FILES ({len(self.junk_files)} found)",
                "-" * 70,
            ])
            for jf in self.junk_files[:20]:
                lines.append(f"  🗑️  {jf.get('path', '')}")
            if len(self.junk_files) > 20:
                lines.append(f"  ... and {len(self.junk_files) - 20} more")

        if self.permission_anomalies:
            lines.extend([
                "",
                f"PERMISSION ANOMALIES ({len(self.permission_anomalies)} found)",
                "-" * 70,
            ])
            for pa in self.permission_anomalies[:10]:
                lines.append(f"  ⚠️  {pa.get('mode', '')} {pa.get('path', '')}")
            if len(self.permission_anomalies) > 10:
                lines.append(f"  ... and {len(self.permission_anomalies) - 10} more")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    def generate_quarantine_script(self) -> str:
        """Generate a safe quarantine script."""
        dupes = self.find_duplicates()
        quarantine_dir = "$HOME/MC96_Quarantine"
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')

        lines = [
            "#!/usr/bin/env bash",
            "# MC96 QUARANTINE SCRIPT",
            f"# Generated: {datetime.now().isoformat()}",
            "# This script MOVES (not deletes) duplicate files to quarantine",
            "",
            "set -euo pipefail",
            "",
            f'QUARANTINE="{quarantine_dir}/{ts}"',
            'mkdir -p "$QUARANTINE"',
            "",
            'echo "🗃️  Quarantine directory: $QUARANTINE"',
            'echo ""',
            "",
            "# === DUPLICATES ===",
        ]

        batch_count = 0
        for h, rows in dupes:
            canonical, extras = self.select_canonical(rows)
            if extras:
                lines.append(f"# Hash: {h[:16]}... ({len(extras)} dupes)")
                for ex in extras:
                    path = ex.get('path', '')
                    if path:
                        safe_path = path.replace("'", "'\"'\"'")
                        lines.append(f"mv -v '{safe_path}' \"$QUARANTINE/\" 2>/dev/null || true")
                        batch_count += 1
                lines.append("")

        lines.extend([
            "",
            "# === JUNK FILES ===",
        ])

        for jf in self.junk_files:
            path = jf.get('path', '')
            if path:
                safe_path = path.replace("'", "'\"'\"'")
                lines.append(f"mv -v '{safe_path}' \"$QUARANTINE/\" 2>/dev/null || true")

        lines.extend([
            "",
            f'echo ""',
            f'echo "✅ Quarantined files to: $QUARANTINE"',
            f'echo "📊 Review before permanent deletion"',
        ])

        return "\n".join(lines)

    def generate_json(self) -> dict:
        """Generate JSON report for programmatic use."""
        dupes = self.find_duplicates()

        dupe_groups = []
        for h, rows in dupes:
            canonical, extras = self.select_canonical(rows)
            dupe_groups.append({
                'hash': h,
                'count': len(rows),
                'size': int(rows[0].get('size', 0)),
                'wasted': int(rows[0].get('size', 0)) * len(extras),
                'canonical': canonical,
                'duplicates': extras,
            })

        return {
            'source': str(self.tsv_path),
            'generated': datetime.now().isoformat(),
            'stats': self.stats,
            'duplicate_groups': dupe_groups,
            'junk_files': self.junk_files,
            'permission_anomalies': self.permission_anomalies,
        }

    def run(self, output_json: bool = False, output_script: bool = False) -> None:
        """Run the full analysis."""
        self.load_tsv()

        # Generate report
        report = self.generate_report()
        report_path = self.output_dir / f"{self.tsv_path.stem}_dedupe_report.txt"
        with open(report_path, 'w') as f:
            f.write(report)
        print(f"📄 Report: {report_path}")
        print(report)

        # Generate JSON if requested
        if output_json:
            json_data = self.generate_json()
            json_path = self.output_dir / f"{self.tsv_path.stem}_dedupe.json"
            with open(json_path, 'w') as f:
                json.dump(json_data, f, indent=2, default=str)
            print(f"📊 JSON: {json_path}")

        # Generate quarantine script if requested
        if output_script:
            script = self.generate_quarantine_script()
            script_path = self.output_dir / f"{self.tsv_path.stem}_quarantine.sh"
            with open(script_path, 'w') as f:
                f.write(script)
            os.chmod(script_path, 0o755)
            print(f"🔧 Quarantine script: {script_path}")
            print("   ⚠️  Review before running!")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='MC96 Dedupe Analyzer - Find and manage duplicate files'
    )
    parser.add_argument('tsv_file', help='Path to truth scanner TSV file')
    parser.add_argument('--output-dir', '-o', help='Output directory for reports')
    parser.add_argument('--json', action='store_true', help='Generate JSON report')
    parser.add_argument('--quarantine-script', action='store_true',
                        help='Generate quarantine bash script')

    args = parser.parse_args()

    if not os.path.exists(args.tsv_file):
        print(f"❌ File not found: {args.tsv_file}")
        sys.exit(1)

    analyzer = DedupeAnalyzer(args.tsv_file, args.output_dir)
    analyzer.run(output_json=args.json, output_script=args.quarantine_script)


if __name__ == '__main__':
    main()
