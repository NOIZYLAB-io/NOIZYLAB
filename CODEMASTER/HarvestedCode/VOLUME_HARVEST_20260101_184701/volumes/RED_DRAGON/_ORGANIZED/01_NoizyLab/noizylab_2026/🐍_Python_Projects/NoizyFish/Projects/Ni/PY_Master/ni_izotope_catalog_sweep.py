#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NI + iZotope Catalog & Document Sweep
Author: R.S Plowman (Fish Music Inc.)

- Scans Native Instruments + iZotope installs, libraries, plugins, presets
- Indexes PDFs (manuals/invoices) with basic metadata
- Deduplicates by checksum, exports CSV + YAML
"""

import os, csv, yaml, json, hashlib, re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.table import Table

console = Console()

# Configure roots (adjust to your environment)
SCAN_ROOTS = [
    "/Users/Shared/Native Instruments",
    "/Library/Application Support/Native Instruments",
    "~/Documents/Native Instruments",
    "~/Documents/iZotope",
    "/Library/Application Support/iZotope",
    "/Library/Audio/Plug-Ins/Components",
    "/Library/Audio/Plug-Ins/VST",
    "/Library/Audio/Plug-Ins/VST3",
    "/Library/Application Support/Avid/Audio/Plug-Ins",
    "/Libraries",
    "~/Music",
    "/Volumes/Archive1",
    "/Volumes/Archive2"
]

# File categories and extensions
LIB_EXTS = {".wav",".aiff",".aif",".flac",".ncw",".nki",".nkm",".nkc",".nkr",".preset",".bank",".bundle",".nks",".nis"}
PLUGIN_EXTS = {".component",".vst",".vst3",".aaxplugin"}
DOC_EXTS = {".pdf"}

CSV_OUT = "ni_izotope_catalog.csv"
YAML_OUT = "ni_izotope_catalog.yaml"
DOC_CSV = "ni_izotope_docs.csv"
DOC_YAML = "ni_izotope_docs.yaml"

MANIFEST = "fishnet_vendors.yaml"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def safe_read_pdf_meta(path: Path) -> Dict[str, Any]:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(str(path))
        info = reader.metadata or {}
        pages = len(reader.pages)
        title = getattr(info, "title", None) or ""
        author = getattr(info, "author", None) or ""
        subject = getattr(info, "subject", None) or ""
        return {"pages": pages, "title": str(title), "author": str(author), "subject": str(subject)}
    except Exception:
        return {"pages": None, "title": "", "author": "", "subject": ""}

def load_manifest() -> Dict[str, Any]:
    if not Path(MANIFEST).exists():
        console.print(f"[yellow]Manifest not found: {MANIFEST}. Using empty vendors.[/yellow]")
        return {"vendors": []}
    return yaml.safe_load(Path(MANIFEST).read_text())

def walk_paths(roots: List[str]) -> List[Path]:
    found = []
    for r in roots:
        root = Path(r).expanduser().resolve()
        if not root.exists():
            console.print(f"[yellow]Missing path:[/yellow] {root}")
            continue
        for p in root.rglob("*"):
            if p.is_file():
                found.append(p)
    return found

def classify_file(p: Path) -> str:
    ext = p.suffix.lower()
    if ext in DOC_EXTS:
        return "doc"
    if ext in PLUGIN_EXTS:
        return "plugin"
    if ext in LIB_EXTS:
        return "library"
    return "other"

def infer_vendor_product(p: Path, manifest: Dict[str, Any]) -> Dict[str, Optional[str]]:
    path_str = str(p)
    vendor_match = None
    product_match = None

    # Heuristics from path segments
    parts = [s.lower() for s in p.parts]
    if any("native instruments" in s for s in parts) or "ni" in parts:
        vendor_match = "Native Instruments"
    if any("izotope" in s for s in parts):
        vendor_match = "iZotope"

    # Manifest-based path association
    for v in manifest.get("vendors", []):
        for prod in v.get("products", []):
            for lp in prod.get("library_paths", []):
                base = Path(lp).expanduser().resolve()
                try:
                    if path_str.startswith(str(base)):
                        vendor_match = v["name"]
                        product_match = prod["title"]
                        break
                except Exception:
                    pass

    # Plugin name heuristics
    name = p.name.lower()
    if vendor_match == "iZotope" and not product_match:
        for prod in ["ozone","rx","neutron","nectar","insight","tonal balance","trash"]:
            if prod in name:
                product_match = prod.title()
                break
    if vendor_match == "Native Instruments" and not product_match:
        for prod in ["kontakt","komplete","massive","replika","fm8","absynth","reaktor","guitar rig","supercharger"]:
            if prod in name:
                product_match = prod.title()
                break

    return {"vendor": vendor_match, "product": product_match}

def build_catalog(files: List[Path], manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    for p in files:
        kind = classify_file(p)
        if kind not in {"library","plugin"}:
            continue
        meta = infer_vendor_product(p, manifest)
        try:
            cs = sha256_file(p)
        except Exception:
            cs = None
        rows.append({
            "kind": kind,
            "vendor": meta["vendor"] or "",
            "product": meta["product"] or "",
            "path": str(p),
            "name": p.name,
            "ext": p.suffix.lower(),
            "size_bytes": p.stat().st_size,
            "checksum": cs
        })
    # Deduplicate by checksum (prefer plugin over library if conflict)
    uniq: Dict[str, Dict[str, Any]] = {}
    for r in rows:
        key = r["checksum"] or f"{r['path']}"
        prev = uniq.get(key)
        if not prev or (r["kind"] == "plugin" and prev["kind"] != "plugin"):
            uniq[key] = r
    return list(uniq.values())

def build_doc_index(files: List[Path], manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    docs = []
    for p in files:
        if classify_file(p) != "doc":
            continue
        meta = infer_vendor_product(p, manifest)
        pdf = safe_read_pdf_meta(p)
        try:
            cs = sha256_file(p)
        except Exception:
            cs = None
        docs.append({
            "vendor": meta["vendor"] or "",
            "product": meta["product"] or "",
            "path": str(p),
            "name": p.name,
            "ext": p.suffix.lower(),
            "size_bytes": p.stat().st_size,
            "checksum": cs,
            "pages": pdf["pages"],
            "title": pdf["title"],
            "author": pdf["author"],
            "subject": pdf["subject"]
        })
    # Deduplicate by checksum
    uniq: Dict[str, Dict[str, Any]] = {}
    for d in docs:
        key = d["checksum"] or f"{d['path']}"
        uniq.setdefault(key, d)
    return list(uniq.values())

def export_catalog(rows: List[Dict[str, Any]], csv_out: str, yaml_out: str):
    if not rows:
        console.print("[yellow]No catalog rows to export.[/yellow]")
        return
    headers = ["kind","vendor","product","path","name","ext","size_bytes","checksum"]
    with open(csv_out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in headers})
    Path(yaml_out).write_text(yaml.safe_dump({"generated": datetime.utcnow().isoformat(), "items": rows}, sort_keys=False))
    console.print(f"[green]Catalog exported:[/green] {csv_out} / {yaml_out}")

def export_docs(rows: List[Dict[str, Any]], csv_out: str, yaml_out: str):
    if not rows:
        console.print("[yellow]No documents to export.[/yellow]")
        return
    headers = ["vendor","product","path","name","ext","size_bytes","checksum","pages","title","author","subject"]
    with open(csv_out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in headers})
    Path(yaml_out).write_text(yaml.safe_dump({"generated": datetime.utcnow().isoformat(), "docs": rows}, sort_keys=False))
    console.print(f"[green]Docs exported:[/green] {csv_out} / {yaml_out}")

def main():
    manifest = load_manifest()
    files = walk_paths(SCAN_ROOTS)
    cat = build_catalog(files, manifest)
    docs = build_doc_index(files, manifest)

    # Pretty summary
    table = Table(title="NI + iZotope Catalog Summary")
    table.add_column("Kind"); table.add_column("Vendor"); table.add_column("Product"); table.add_column("Count")
    def count_by(kind, vendor):
        return sum(1 for r in cat if r["kind"] == kind and r["vendor"] == vendor)
    for vendor in ["Native Instruments","iZotope",""]:
        for kind in ["plugin","library"]:
            c = count_by(kind, vendor)
            if c:
                table.add_row(kind, vendor or "(unknown)", "", str(c))
    console.print(table)

    export_catalog(cat, CSV_OUT, YAML_OUT)
    export_docs(docs, DOC_CSV, DOC_YAML)

if __name__ == "__main__":
    main()