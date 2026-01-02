\
#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shutil, sys
from pathlib import Path
from typing import List, Dict
from engine.dupeshark.engine import scan
from engine.dupeshark.heuristics import pick_keepers

def parse_size(s: str) -> int:
    # Accepts "1024", "1KB", "5MB", "1GB"
    s = s.strip().upper()
    multipliers = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}
    for suf, mul in multipliers.items():
        if s.endswith(suf):
            return int(float(s[:-len(suf)]) * mul)
    return int(s)

def main():
    ap = argparse.ArgumentParser(description="DupeShark CLI - find and handle duplicate files.")
    ap.add_argument("--path", required=True, help="Path to scan")
    ap.add_argument("--min-size", default="1KB", help="Minimum file size to consider (e.g., 1KB, 5MB)")
    ap.add_argument("--report-json", help="Write full report JSON to this path")
    ap.add_argument("--move-dupes-to", help="Directory to move duplicates (keepers stay put)")
    ap.add_argument("--dry-run", action="store_true", help="Show actions without executing")
    args = ap.parse_args()

    root = Path(args.path).expanduser()
    min_size = parse_size(args.min_size)

    groups = scan(root, min_size=min_size)
    # convert to dict for JSON
    as_dict = [ {"size": g.size, "files": [vars(f) for f in g.files]} for g in groups ]

    # write report if requested
    if args.report_json:
        out = Path(args.report_json).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(as_dict, indent=2))
        print(f"[report] wrote {out}")

    # optional move
    if args.move_dupes_to:
        decisions = pick_keepers(groups)
        dest_root = Path(args.move_dupes_to).expanduser()
        dest_root.mkdir(parents=True, exist_ok=True)
        for keeper, dupes in decisions:
            for d in dupes:
                src = Path(d.path)
                rel = src.name
                dst = dest_root / rel
                if args.dry_run:
                    print(f"(dry-run) move {src} -> {dst}")
                else:
                    try:
                        shutil.move(str(src), str(dst))
                        print(f"moved {src} -> {dst}")
                    except Exception as e:
                        print(f"[warn] failed to move {src}: {e}", file=sys.stderr)

    # summary to stdout (for GUI)
    print(json.dumps({"groups": len(groups), "files": sum(len(g.files) for g in groups)}))

if __name__ == "__main__":
    main()
