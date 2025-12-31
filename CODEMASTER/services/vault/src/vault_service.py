#!/usr/bin/env python3
"""
🔐 VAULT SERVICE - The Truth Storage System
============================================
Append-only storage with automatic routing, deduplication, and sidecars.

Storage Contract (GABRIEL, immutable rules):
GABRIEL:/NOIZY_AI/
├── vault/raw/           (append-only originals)
├── vault/derived/       (processed outputs)
├── vault/index/         (search indexes)
├── vault/staging/       (quarantine, needs_fixing, dedupe)
├── evidence_packs/      (immutable output artifacts)
├── mission_control/queues/
└── logs/{audit,errors,ingest,mc96,portal}
"""

import os
import json
import hashlib
import shutil
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import queue

# ═══════════════════════════════════════════════════════════════
# 🔧 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", "/Users/m2ultra/NOIZYLAB/GABRIEL/NOIZY_AI"))
INGEST_WATCH = Path(os.environ.get("INGEST_WATCH", "/Users/m2ultra/NOIZYLAB/GABRIEL/INGEST"))

# Vault directories
DIRS = {
    "raw": VAULT_ROOT / "vault" / "raw",
    "derived": VAULT_ROOT / "vault" / "derived",
    "index": VAULT_ROOT / "vault" / "index",
    "staging": VAULT_ROOT / "vault" / "staging",
    "quarantine": VAULT_ROOT / "vault" / "staging" / "quarantine",
    "needs_fixing": VAULT_ROOT / "vault" / "staging" / "needs_fixing",
    "dedupe": VAULT_ROOT / "vault" / "staging" / "dedupe",
    "evidence": VAULT_ROOT / "evidence_packs",
    "queues": VAULT_ROOT / "mission_control" / "queues",
    "logs": VAULT_ROOT / "logs",
}

# File routing rules (extension -> category)
ROUTING_RULES = {
    # Code
    ".py": "code/python",
    ".js": "code/javascript",
    ".ts": "code/typescript",
    ".sh": "code/shell",
    ".sql": "code/sql",
    # Documents
    ".md": "docs/markdown",
    ".txt": "docs/text",
    ".pdf": "docs/pdf",
    ".docx": "docs/word",
    # Data
    ".json": "data/json",
    ".yaml": "data/yaml",
    ".yml": "data/yaml",
    ".csv": "data/csv",
    ".xml": "data/xml",
    # Media
    ".mp3": "media/audio",
    ".wav": "media/audio",
    ".mp4": "media/video",
    ".mov": "media/video",
    ".jpg": "media/image",
    ".jpeg": "media/image",
    ".png": "media/image",
    ".gif": "media/image",
    # Config
    ".env": "config/env",
    ".ini": "config/ini",
    ".conf": "config/conf",
    # Archives
    ".zip": "archives/zip",
    ".tar": "archives/tar",
    ".gz": "archives/gz",
}

# ═══════════════════════════════════════════════════════════════
# 📦 DATA MODELS
# ═══════════════════════════════════════════════════════════════

@dataclass
class VaultAsset:
    """Represents a stored asset in the vault"""
    id: str
    filename: str
    original_path: str
    vault_path: str
    category: str
    content_hash: str
    size_bytes: int
    mime_type: str
    ingested_at: str
    source: str
    tags: List[str]
    metadata: Dict[str, Any]

@dataclass
class Sidecar:
    """Metadata sidecar (.noizy.json)"""
    asset_id: str
    original_filename: str
    content_hash: str
    ingested_at: str
    source: str
    category: str
    routing_rule: str
    tags: List[str]
    derived_from: Optional[str] = None
    evidence_refs: List[str] = None

# ═══════════════════════════════════════════════════════════════
# 🔒 VAULT CORE
# ═══════════════════════════════════════════════════════════════

class VaultService:
    """The Vault - Append-only truth storage"""
    
    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or (VAULT_ROOT / "vault.db")
        self.job_queue = queue.Queue()
        self._init_dirs()
        self._init_db()
        
    def _init_dirs(self):
        """Create all vault directories"""
        for name, path in DIRS.items():
            path.mkdir(parents=True, exist_ok=True)
        # Create log subdirs
        for log_type in ["audit", "errors", "ingest", "mc96", "portal"]:
            (DIRS["logs"] / log_type).mkdir(exist_ok=True)
    
    def _init_db(self):
        """Initialize SQLite catalog"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                original_path TEXT,
                vault_path TEXT NOT NULL,
                category TEXT,
                content_hash TEXT NOT NULL,
                size_bytes INTEGER,
                mime_type TEXT,
                ingested_at TEXT NOT NULL,
                source TEXT,
                tags TEXT,
                metadata TEXT
            )
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_hash ON assets(content_hash)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_category ON assets(category)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_filename ON assets(filename)
        """)
        
        conn.commit()
        conn.close()
    
    def compute_hash(self, filepath: Path) -> str:
        """Compute SHA-256 hash of file"""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def generate_id(self, content_hash: str, filename: str) -> str:
        """Generate unique asset ID"""
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}_{content_hash[:12]}_{filename[:20]}"
    
    def route_file(self, filepath: Path) -> str:
        """Determine category based on routing rules"""
        ext = filepath.suffix.lower()
        return ROUTING_RULES.get(ext, "uncategorized")
    
    def check_duplicate(self, content_hash: str) -> Optional[VaultAsset]:
        """Check if file already exists in vault"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assets WHERE content_hash = ?", (content_hash,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return VaultAsset(
                id=row[0], filename=row[1], original_path=row[2],
                vault_path=row[3], category=row[4], content_hash=row[5],
                size_bytes=row[6], mime_type=row[7], ingested_at=row[8],
                source=row[9], tags=json.loads(row[10] or "[]"),
                metadata=json.loads(row[11] or "{}")
            )
        return None
    
    def ingest(self, filepath: Path, source: str = "manual", tags: List[str] = None) -> VaultAsset:
        """
        Ingest a file into the vault.
        
        1. Compute hash
        2. Check for duplicates
        3. Route to correct category
        4. Copy to vault/raw/
        5. Create sidecar
        6. Update catalog
        """
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        tags = tags or []
        
        # Step 1: Compute hash
        content_hash = self.compute_hash(filepath)
        
        # Step 2: Check duplicates
        existing = self.check_duplicate(content_hash)
        if existing:
            self._log("ingest", f"DUPLICATE: {filepath.name} matches {existing.id}")
            # Copy to dedupe staging for review
            dedupe_path = DIRS["dedupe"] / filepath.name
            shutil.copy2(filepath, dedupe_path)
            return existing
        
        # Step 3: Route file
        category = self.route_file(filepath)
        
        # Step 4: Create vault path and copy
        timestamp = datetime.utcnow()
        date_path = timestamp.strftime("%Y/%m/%d")
        vault_dir = DIRS["raw"] / category / date_path
        vault_dir.mkdir(parents=True, exist_ok=True)
        
        asset_id = self.generate_id(content_hash, filepath.name)
        vault_path = vault_dir / f"{asset_id}{filepath.suffix}"
        
        shutil.copy2(filepath, vault_path)
        
        # Step 5: Create sidecar
        sidecar = Sidecar(
            asset_id=asset_id,
            original_filename=filepath.name,
            content_hash=content_hash,
            ingested_at=timestamp.isoformat(),
            source=source,
            category=category,
            routing_rule=filepath.suffix.lower(),
            tags=tags,
            evidence_refs=[]
        )
        
        sidecar_path = vault_path.with_suffix(vault_path.suffix + ".noizy.json")
        with open(sidecar_path, 'w') as f:
            json.dump(asdict(sidecar), f, indent=2)
        
        # Step 6: Update catalog
        asset = VaultAsset(
            id=asset_id,
            filename=filepath.name,
            original_path=str(filepath),
            vault_path=str(vault_path),
            category=category,
            content_hash=content_hash,
            size_bytes=filepath.stat().st_size,
            mime_type=self._get_mime_type(filepath),
            ingested_at=timestamp.isoformat(),
            source=source,
            tags=tags,
            metadata={}
        )
        
        self._save_asset(asset)
        self._log("ingest", f"INGESTED: {filepath.name} -> {vault_path}")
        
        return asset
    
    def _save_asset(self, asset: VaultAsset):
        """Save asset to catalog"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO assets 
            (id, filename, original_path, vault_path, category, content_hash,
             size_bytes, mime_type, ingested_at, source, tags, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            asset.id, asset.filename, asset.original_path, asset.vault_path,
            asset.category, asset.content_hash, asset.size_bytes, asset.mime_type,
            asset.ingested_at, asset.source, json.dumps(asset.tags),
            json.dumps(asset.metadata)
        ))
        conn.commit()
        conn.close()
    
    def find(self, query: str, category: str = None, limit: int = 50) -> List[VaultAsset]:
        """Search the vault catalog"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        sql = "SELECT * FROM assets WHERE (filename LIKE ? OR tags LIKE ?)"
        params = [f"%{query}%", f"%{query}%"]
        
        if category:
            sql += " AND category LIKE ?"
            params.append(f"%{category}%")
        
        sql += f" ORDER BY ingested_at DESC LIMIT {limit}"
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        conn.close()
        
        return [VaultAsset(
            id=r[0], filename=r[1], original_path=r[2], vault_path=r[3],
            category=r[4], content_hash=r[5], size_bytes=r[6], mime_type=r[7],
            ingested_at=r[8], source=r[9], tags=json.loads(r[10] or "[]"),
            metadata=json.loads(r[11] or "{}")
        ) for r in rows]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get vault statistics"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*), SUM(size_bytes) FROM assets")
        total_count, total_size = cursor.fetchone()
        
        cursor.execute("SELECT category, COUNT(*) FROM assets GROUP BY category")
        by_category = dict(cursor.fetchall())
        
        conn.close()
        
        return {
            "total_assets": total_count or 0,
            "total_size_bytes": total_size or 0,
            "total_size_gb": round((total_size or 0) / (1024**3), 2),
            "by_category": by_category
        }
    
    def _get_mime_type(self, filepath: Path) -> str:
        """Get MIME type for file"""
        import mimetypes
        mime, _ = mimetypes.guess_type(str(filepath))
        return mime or "application/octet-stream"
    
    def _log(self, log_type: str, message: str):
        """Write to audit log"""
        log_file = DIRS["logs"] / log_type / f"{datetime.utcnow().strftime('%Y-%m-%d')}.log"
        timestamp = datetime.utcnow().isoformat()
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

# ═══════════════════════════════════════════════════════════════
# 👁️ INGEST WATCHER
# ═══════════════════════════════════════════════════════════════

class IngestWatcher(FileSystemEventHandler):
    """Watch for new files and auto-ingest"""
    
    def __init__(self, vault: VaultService):
        self.vault = vault
        
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = Path(event.src_path)
        # Skip hidden files and sidecars
        if filepath.name.startswith('.') or filepath.suffix == '.noizy.json':
            return
        try:
            self.vault.ingest(filepath, source="auto_watch")
        except Exception as e:
            self.vault._log("errors", f"INGEST FAILED: {filepath} - {e}")

def start_watcher(vault: VaultService, watch_path: Path = None):
    """Start the ingest watcher"""
    watch_path = watch_path or INGEST_WATCH
    watch_path.mkdir(parents=True, exist_ok=True)
    
    observer = Observer()
    handler = IngestWatcher(vault)
    observer.schedule(handler, str(watch_path), recursive=True)
    observer.start()
    return observer

# ═══════════════════════════════════════════════════════════════
# 🚀 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="🔐 VAULT SERVICE")
    parser.add_argument("command", choices=["ingest", "find", "stats", "watch"])
    parser.add_argument("args", nargs="*")
    parser.add_argument("--source", default="cli")
    parser.add_argument("--tags", default="")
    
    args = parser.parse_args()
    vault = VaultService()
    
    if args.command == "ingest":
        if not args.args:
            print("Usage: vault_service.py ingest <file>")
            return
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        asset = vault.ingest(Path(args.args[0]), source=args.source, tags=tags)
        print(f"✅ Ingested: {asset.id}")
        print(f"   Path: {asset.vault_path}")
        print(f"   Category: {asset.category}")
    
    elif args.command == "find":
        query = args.args[0] if args.args else ""
        results = vault.find(query)
        print(f"🔍 Found {len(results)} assets:")
        for r in results[:20]:
            print(f"  [{r.category}] {r.filename} ({r.id})")
    
    elif args.command == "stats":
        stats = vault.get_stats()
        print(f"📊 VAULT STATISTICS")
        print(f"   Total Assets: {stats['total_assets']}")
        print(f"   Total Size: {stats['total_size_gb']} GB")
        print(f"   Categories:")
        for cat, count in stats.get('by_category', {}).items():
            print(f"      {cat}: {count}")
    
    elif args.command == "watch":
        print(f"👁️ Starting ingest watcher on {INGEST_WATCH}")
        observer = start_watcher(vault)
        try:
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    main()
