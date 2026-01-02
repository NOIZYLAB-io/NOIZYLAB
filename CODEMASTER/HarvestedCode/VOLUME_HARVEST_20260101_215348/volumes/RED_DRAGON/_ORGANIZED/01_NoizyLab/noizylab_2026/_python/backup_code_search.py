#!/usr/bin/env python3
"""
backup_code_search.py

Searches a set of directories for potential Facebook 2FA backup codes and related files.
Default targets: $HOME, /Users/Shared, /Volumes (if present)

What it looks for:
 - Lines that are exactly 8 digits (common Facebook backup code format)
 - 6-digit codes (common SMS / TOTP codes) in file contents
 - Filenames containing keywords: facebook, fb, backup, codes, 2fa, two-factor, twofactor
 - Files with names similar to "Mission Control" (case-insensitive)
 - Basic heuristics for images containing "backup code" in filename (will list but not OCR)

Usage:
  python3 backup_code_search.py --root /Users/rob --include-volumes --max-files 200000

Notes/permissions:
 - For macOS, grant Terminal Full Disk Access to let the script read protected locations.
 - Scanning root '/' is possible but may be extremely slow and will hit permission errors.
 - This script is non-destructive and only reads files. It will skip binary files larger than a threshold
   unless they have a text-like extension (.txt, .md, .log, .eml, .pdf not parsed).

Output:
 - backup_code_search_out/backup_search.json
 - backup_code_search_out/backup_search_report.txt
"""
from pathlib import Path
import re, json, argparse, sys, os, time

KW_FILENAMES = re.compile(r'(facebook|fb|backup|codes|two[\s\-]?factor|2fa|twofactor)', re.I)
MISSION_CTRL = re.compile(r'mission\s*control', re.I)
EIGHT_DIGIT_LINE = re.compile(r'^\s*(\d{8})\s*$', re.M)
SIX_DIGIT = re.compile(r'(?<!\d)(\d{6})(?!\d)')

TEXT_EXT_WHITELIST = {
    ".txt", ".md", ".log", ".csv", ".json", ".eml", ".html", ".htm", ".py", ".rtf", ".tex", ".cfg", ".ini", ".plist"
}

MAX_READ_BYTES = 200000  # read up to 200KB to scan a file (adjustable)
MAX_FILE_SIZE = 50 * 1024 * 1024  # skip files larger than 50MB by default (unless extension is whitelisted)

OUTDIR = Path.cwd() / "backup_code_search_out"
OUTDIR.mkdir(exist_ok=True)

def scan_file(path: Path, results: dict):
    try:
        size = path.stat().st_size
    except Exception as e:
        results.setdefault("errors", []).append({"path": str(path), "error": f"stat: {e}"})
        return
    # quick filename checks
    name = path.name
    name_hits = []
    if KW_FILENAMES.search(name):
        name_hits.append("filename_keyword")
    if MISSION_CTRL.search(name):
        name_hits.append("mission_control_name")

    # if filename matched strongly, try to read small files even if ext not whitelisted
    ext = path.suffix.lower()
    is_text_ext = ext in TEXT_EXT_WHITELIST
    try_read = False
    if is_text_ext:
        try_read = True
    else:
        # also allow reading small files with matching names
        if size <= MAX_READ_BYTES and name_hits:
            try_read = True

    if size > MAX_FILE_SIZE and not is_text_ext:
        # skip large binaries
        if name_hits:
            results.setdefault("candidates", []).append({
                "path": str(path),
                "size": size,
                "reason": "large_binary_but_name_match"
            })
        return

    if not try_read:
        return

    try:
        with open(path, "rb") as f:
            raw = f.read(MAX_READ_BYTES)
        try:
            text = raw.decode("utf-8", errors="ignore")
        except Exception:
            text = ""
    except Exception as e:
        results.setdefault("errors", []).append({"path": str(path), "error": f"read: {e}"})
        return

    eight = EIGHT_DIGIT_LINE.findall(text)
    six = SIX_DIGIT.findall(text)
    snippets = []
    if eight:
        snippets.append({"type": "8digit_lines", "matches": list(set(eight))})
    if six:
        snippets.append({"type": "6digit", "matches": list(set(six)[:10])})

    if name_hits or snippets:
        entry = {
            "path": str(path),
            "size": size,
            "name_hits": name_hits,
            "snippets": snippets,
        }
        results.setdefault("found", []).append(entry)

def walk_and_scan(roots, max_files):
    results = {"scanned": 0, "found": [], "errors": []}
    files_seen = 0
    start = time.time()
    for root in roots:
        p = Path(root)
        if not p.exists():
            continue
        for path in p.rglob("*"):
            if files_seen >= max_files:
                return results
            if path.is_dir():
                continue
            files_seen += 1
            results["scanned"] += 1
            # skip obvious system dirs that will choke permission-wise unless user wants them
            try:
                rel = path.relative_to(Path.home()) if path.exists() else path
            except Exception:
                rel = path
            scan_file(path, results)
    duration = time.time() - start
    results["duration_secs"] = duration
    results["files_seen"] = files_seen
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", help="Single path to scan (defaults to $HOME and /Users/Shared and /Volumes)", default=None)
    ap.add_argument("--include-volumes", action="store_true", help="Include /Volumes in scan")
    ap.add_argument("--max-files", type=int, default=200000, help="Max files to inspect (safety cap)")
    ap.add_argument("--max-depth", type=int, default=0, help="Unused (kept for compatibility)")
    args = ap.parse_args()

    roots = []
    if args.root:
        roots = [args.root]
    else:
        roots = [str(Path.home()), "/Users/Shared"]
        if args.include_volumes:
            roots += [str(p) for p in Path("/Volumes").glob("*") if p.exists()]
    roots = [r for r in roots if Path(r).exists()]

    print("Scanning roots:", roots)
    res = walk_and_scan(roots, args.max_files)
    out_json = OUTDIR / "backup_search.json"
    out_txt = OUTDIR / "backup_search_report.txt"
    out_json.write_text(json.dumps(res, indent=2))
    # human report
    lines = []
    lines.append(f"Backup search report - {time.ctime()}")
    lines.append("Scanned files: %d" % res.get("scanned", 0))
    lines.append("Duration (s): %.1f" % res.get("duration_secs", 0.0))
    lines.append("Found candidates: %d" % len(res.get("found", [])))
    lines.append("")
    for f in res.get("found", [])[:200]:
        lines.append(f"{f['path']}  ({f['size']} bytes)  name_hits={f.get('name_hits', [])}")
        for s in f.get("snippets", []):
            lines.append("  - %s: %s" % (s.get("type"), ", ".join(s.get("matches", [])[:10])))
        lines.append("")
    if res.get("errors"):
        lines.append("Errors:")
        for e in res.get("errors")[:200]:
            lines.append(str(e))

    out_txt.write_text("\n".join(lines))
    print("Wrote:", out_json, out_txt)

if __name__ == "__main__":
    main()
