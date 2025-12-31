#!/usr/bin/env python3
"""
🔥 CODEMASTER VAULT SERVICE 🔥
================================
The immutable truth layer. Every file gets:
- Routed to correct vault path
- Tagged with .noizy.json sidecar
- Indexed in catalog
- SHA256 verified

Storage Contract (GABRIEL):
  /NOIZY_AI/vault/raw/          (append-only source)
  /NOIZY_AI/vault/derived/      (previews, proxies)
  /NOIZY_AI/vault/index/        (search indexes)
  /NOIZY_AI/vault/staging/      (quarantine, needs_fixing, dedupe)
  /NOIZY_AI/evidence_packs/     (immutable output artifacts)
"""

import os
import json
import hashlib
import shutil
import mimetypes
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import queue
import time

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", "/Users/m2ultra/NOIZY_AI"))
WATCH_PATHS = [
    Path.home() / "Desktop",
    Path.home() / "Downloads",
    Path.home() / "Documents",
]

class AssetType(Enum):
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"
    DOCUMENT = "document"
    CODE = "code"
    DATA = "data"
    ARCHIVE = "archive"
    UNKNOWN = "unknown"

class SessionMode(Enum):
    PLAY = "play"
    RECORD = "record"
    EDIT = "edit"
    MIX = "mix"
    SHIP = "ship"
    RECOVER = "recover"

# File extension mappings
TYPE_MAPPINGS = {
    AssetType.AUDIO: {'.wav', '.mp3', '.flac', '.aiff', '.ogg', '.m4a', '.aac', '.opus'},
    AssetType.VIDEO: {'.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.prores'},
    AssetType.IMAGE: {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.raw'},
    AssetType.DOCUMENT: {'.pdf', '.doc', '.docx', '.txt', '.md', '.rtf', '.odt', '.pages'},
    AssetType.CODE: {'.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.json', '.yaml', '.sh'},
    AssetType.DATA: {'.csv', '.xlsx', '.xls', '.db', '.sqlite', '.parquet', '.json'},
    AssetType.ARCHIVE: {'.zip', '.tar', '.gz', '.7z', '.rar', '.dmg'},
}

# ═══════════════════════════════════════════════════════════════
# 📄 ASSET SIDECAR (the truth about every file)
# ═══════════════════════════════════════════════════════════════

@dataclass
class AssetSidecar:
    """The .noizy.json sidecar - truth about every asset"""
    asset_id: str
    captured_at: str
    source_path: str
    vault_path: str
    asset_type: str
    sha256: str
    size_bytes: int
    
    # Optional metadata
    project: Optional[str] = None
    tags: List[str] = None
    session_mode: Optional[str] = None
    
    # Media-specific
    duration_seconds: Optional[float] = None
    codec: Optional[str] = None
    sample_rate: Optional[int] = None
    fps: Optional[float] = None
    channels: Optional[int] = None
    resolution: Optional[str] = None
    
    # Relations
    parent_asset_id: Optional[str] = None
    related_assets: List[str] = None
    
    # Unknowns (things we couldn't determine)
    unknowns: List[str] = None
    confidence: float = 1.0
    
    def __post_init__(self):
        self.tags = self.tags or []
        self.related_assets = self.related_assets or []
        self.unknowns = self.unknowns or []
    
    def to_dict(self) -> Dict:
        return {k: v for k, v in asdict(self).items() if v is not None}
    
    def save(self, path: Path):
        """Save sidecar next to asset"""
        sidecar_path = path.with_suffix(path.suffix + '.noizy.json')
        with open(sidecar_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        return sidecar_path

# ═══════════════════════════════════════════════════════════════
# 🔐 VAULT CORE
# ═══════════════════════════════════════════════════════════════

class VaultService:
    """The immutable truth layer"""
    
    def __init__(self, root: Path = VAULT_ROOT):
        self.root = root
        self.raw = root / "vault" / "raw"
        self.derived = root / "vault" / "derived"
        self.index = root / "vault" / "index"
        self.staging = root / "vault" / "staging"
        self.evidence = root / "evidence_packs"
        self.logs = root / "logs"
        
        # Ensure directories exist
        for d in [self.raw, self.derived, self.index, 
                  self.staging / "quarantine",
                  self.staging / "needs_fixing",
                  self.staging / "dedupe",
                  self.evidence, self.logs / "ingest"]:
            d.mkdir(parents=True, exist_ok=True)
        
        # Ingest queue
        self.ingest_queue = queue.Queue()
        self._running = False
    
    @staticmethod
    def compute_sha256(filepath: Path) -> str:
        """Compute SHA256 hash of file"""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    @staticmethod
    def detect_type(filepath: Path) -> AssetType:
        """Detect asset type from extension"""
        ext = filepath.suffix.lower()
        for asset_type, extensions in TYPE_MAPPINGS.items():
            if ext in extensions:
                return asset_type
        return AssetType.UNKNOWN
    
    def route_path(self, asset_type: AssetType, project: Optional[str] = None) -> Path:
        """Determine vault destination based on type and project"""
        today = datetime.now().strftime("%Y/%m/%d")
        
        if project:
            return self.raw / "projects" / project / asset_type.value / today
        else:
            return self.raw / asset_type.value / today
    
    def ingest(self, source: Path, project: Optional[str] = None, 
               tags: List[str] = None, mode: SessionMode = None,
               move: bool = False) -> AssetSidecar:
        """
        Ingest a file into the vault.
        
        Args:
            source: Path to source file
            project: Optional project name
            tags: Optional list of tags
            mode: Session mode (Play/Record/Edit/Mix/Ship/Recover)
            move: If True, move file instead of copy
        
        Returns:
            AssetSidecar with all metadata
        """
        source = Path(source)
        if not source.exists():
            raise FileNotFoundError(f"Source not found: {source}")
        
        # Generate asset ID
        asset_id = str(uuid.uuid4())[:12]
        
        # Compute hash
        sha256 = self.compute_sha256(source)
        
        # Check for duplicates
        existing = self._find_by_hash(sha256)
        if existing:
            self._log_ingest("DEDUPE", source, f"Already exists: {existing}")
            # Move to dedupe staging
            dedupe_path = self.staging / "dedupe" / source.name
            if move:
                shutil.move(str(source), str(dedupe_path))
            return self._load_sidecar(existing)
        
        # Detect type and route
        asset_type = self.detect_type(source)
        dest_dir = self.route_path(asset_type, project)
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Destination filename (add asset_id prefix for uniqueness)
        dest_name = f"{asset_id}_{source.name}"
        dest_path = dest_dir / dest_name
        
        # Copy or move
        if move:
            shutil.move(str(source), str(dest_path))
        else:
            shutil.copy2(str(source), str(dest_path))
        
        # Create sidecar
        sidecar = AssetSidecar(
            asset_id=asset_id,
            captured_at=datetime.now().isoformat(),
            source_path=str(source),
            vault_path=str(dest_path.relative_to(self.root)),
            asset_type=asset_type.value,
            sha256=sha256,
            size_bytes=dest_path.stat().st_size,
            project=project,
            tags=tags or [],
            session_mode=mode.value if mode else None,
        )
        
        # Extract media metadata if applicable
        sidecar = self._extract_media_metadata(dest_path, sidecar)
        
        # Save sidecar
        sidecar.save(dest_path)
        
        # Log
        self._log_ingest("INGEST", source, f"→ {dest_path}")
        
        # Index in catalog
        self._index_asset(sidecar)
        
        return sidecar
    
    def _extract_media_metadata(self, path: Path, sidecar: AssetSidecar) -> AssetSidecar:
        """Extract media-specific metadata (best effort)"""
        try:
            import subprocess
            result = subprocess.run(
                ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', str(path)],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                fmt = data.get('format', {})
                streams = data.get('streams', [])
                
                sidecar.duration_seconds = float(fmt.get('duration', 0)) or None
                
                for stream in streams:
                    if stream.get('codec_type') == 'video':
                        sidecar.codec = stream.get('codec_name')
                        sidecar.fps = eval(stream.get('r_frame_rate', '0/1')) if '/' in stream.get('r_frame_rate', '') else None
                        sidecar.resolution = f"{stream.get('width')}x{stream.get('height')}"
                    elif stream.get('codec_type') == 'audio':
                        if not sidecar.codec:
                            sidecar.codec = stream.get('codec_name')
                        sidecar.sample_rate = int(stream.get('sample_rate', 0)) or None
                        sidecar.channels = stream.get('channels')
        except Exception as e:
            sidecar.unknowns.append(f"media_metadata: {e}")
        
        return sidecar
    
    def _find_by_hash(self, sha256: str) -> Optional[Path]:
        """Check if file already exists by hash"""
        # Search index for hash
        hash_index = self.index / "hashes" / sha256[:2] / f"{sha256}.json"
        if hash_index.exists():
            with open(hash_index) as f:
                return Path(json.load(f).get('vault_path'))
        return None
    
    def _index_asset(self, sidecar: AssetSidecar):
        """Index asset for fast lookup"""
        # Hash index
        hash_dir = self.index / "hashes" / sidecar.sha256[:2]
        hash_dir.mkdir(parents=True, exist_ok=True)
        with open(hash_dir / f"{sidecar.sha256}.json", 'w') as f:
            json.dump({'asset_id': sidecar.asset_id, 'vault_path': sidecar.vault_path}, f)
        
        # ID index
        id_dir = self.index / "ids"
        id_dir.mkdir(parents=True, exist_ok=True)
        with open(id_dir / f"{sidecar.asset_id}.json", 'w') as f:
            json.dump(sidecar.to_dict(), f, indent=2)
    
    def _load_sidecar(self, path: Path) -> AssetSidecar:
        """Load sidecar from path"""
        sidecar_path = Path(str(path) + '.noizy.json')
        if sidecar_path.exists():
            with open(sidecar_path) as f:
                data = json.load(f)
                return AssetSidecar(**data)
        return None
    
    def _log_ingest(self, action: str, source: Path, message: str):
        """Log ingest action"""
        log_file = self.logs / "ingest" / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} [{action}] {source} - {message}\n")
    
    def find(self, query: str = None, asset_type: AssetType = None,
             project: str = None, tags: List[str] = None,
             date_from: str = None, date_to: str = None,
             limit: int = 100) -> List[AssetSidecar]:
        """
        Search the vault.
        
        Args:
            query: Text search in filename/path
            asset_type: Filter by type
            project: Filter by project
            tags: Filter by tags (any match)
            date_from: ISO date string
            date_to: ISO date string
            limit: Max results
        
        Returns:
            List of matching AssetSidecars
        """
        results = []
        id_dir = self.index / "ids"
        
        if not id_dir.exists():
            return results
        
        for sidecar_file in id_dir.glob("*.json"):
            if len(results) >= limit:
                break
            
            with open(sidecar_file) as f:
                data = json.load(f)
            
            # Apply filters
            if query and query.lower() not in data.get('vault_path', '').lower():
                continue
            if asset_type and data.get('asset_type') != asset_type.value:
                continue
            if project and data.get('project') != project:
                continue
            if tags and not any(t in data.get('tags', []) for t in tags):
                continue
            if date_from and data.get('captured_at', '') < date_from:
                continue
            if date_to and data.get('captured_at', '') > date_to:
                continue
            
            results.append(AssetSidecar(**data))
        
        return results
    
    def get(self, asset_id: str) -> Optional[AssetSidecar]:
        """Get asset by ID"""
        id_file = self.index / "ids" / f"{asset_id}.json"
        if id_file.exists():
            with open(id_file) as f:
                return AssetSidecar(**json.load(f))
        return None
    
    def stats(self) -> Dict:
        """Get vault statistics"""
        id_dir = self.index / "ids"
        total = len(list(id_dir.glob("*.json"))) if id_dir.exists() else 0
        
        # Count by type
        by_type = {}
        if id_dir.exists():
            for f in id_dir.glob("*.json"):
                with open(f) as fp:
                    data = json.load(fp)
                    t = data.get('asset_type', 'unknown')
                    by_type[t] = by_type.get(t, 0) + 1
        
        # Disk usage
        def dir_size(path: Path) -> int:
            return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
        
        return {
            'total_assets': total,
            'by_type': by_type,
            'raw_size_gb': round(dir_size(self.raw) / (1024**3), 2) if self.raw.exists() else 0,
            'derived_size_gb': round(dir_size(self.derived) / (1024**3), 2) if self.derived.exists() else 0,
        }

# ═══════════════════════════════════════════════════════════════
# 👁️ INGEST WATCHER
# ═══════════════════════════════════════════════════════════════

class IngestWatcher(FileSystemEventHandler):
    """Watch directories for new files to ingest"""
    
    def __init__(self, vault: VaultService, auto_project: str = None):
        self.vault = vault
        self.auto_project = auto_project
        self.pending = set()
        self.lock = threading.Lock()
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        path = Path(event.src_path)
        
        # Skip hidden files and sidecars
        if path.name.startswith('.') or path.suffix == '.noizy.json':
            return
        
        # Debounce - wait for file to finish writing
        with self.lock:
            if str(path) in self.pending:
                return
            self.pending.add(str(path))
        
        # Wait then ingest
        threading.Timer(2.0, self._ingest_file, args=[path]).start()
    
    def _ingest_file(self, path: Path):
        try:
            if path.exists():
                self.vault.ingest(path, project=self.auto_project, move=True)
        except Exception as e:
            print(f"⚠️ Ingest failed: {path} - {e}")
        finally:
            with self.lock:
                self.pending.discard(str(path))

def start_watcher(vault: VaultService, watch_paths: List[Path] = WATCH_PATHS):
    """Start the ingest watcher"""
    observer = Observer()
    handler = IngestWatcher(vault)
    
    for path in watch_paths:
        if path.exists():
            observer.schedule(handler, str(path), recursive=False)
            print(f"👁️ Watching: {path}")
    
    observer.start()
    return observer

# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🔥 CODEMASTER Vault Service')
    parser.add_argument('command', choices=['ingest', 'find', 'get', 'stats', 'watch'])
    parser.add_argument('args', nargs='*')
    parser.add_argument('--project', '-p', help='Project name')
    parser.add_argument('--tags', '-t', help='Comma-separated tags')
    parser.add_argument('--type', help='Asset type filter')
    parser.add_argument('--move', action='store_true', help='Move instead of copy')
    
    args = parser.parse_args()
    vault = VaultService()
    
    if args.command == 'ingest':
        if not args.args:
            print("Usage: vault_service.py ingest <file> [--project X] [--tags a,b,c]")
            return
        
        tags = args.tags.split(',') if args.tags else None
        for path in args.args:
            try:
                sidecar = vault.ingest(Path(path), project=args.project, tags=tags, move=args.move)
                print(f"✅ Ingested: {sidecar.asset_id} → {sidecar.vault_path}")
            except Exception as e:
                print(f"❌ Failed: {path} - {e}")
    
    elif args.command == 'find':
        query = args.args[0] if args.args else None
        asset_type = AssetType(args.type) if args.type else None
        results = vault.find(query=query, asset_type=asset_type, project=args.project)
        
        print(f"\n🔍 Found {len(results)} assets:\n")
        for r in results[:20]:
            print(f"  [{r.asset_type}] {r.asset_id} - {Path(r.vault_path).name}")
            if r.project:
                print(f"      Project: {r.project}")
            if r.tags:
                print(f"      Tags: {', '.join(r.tags)}")
    
    elif args.command == 'get':
        if not args.args:
            print("Usage: vault_service.py get <asset_id>")
            return
        
        sidecar = vault.get(args.args[0])
        if sidecar:
            print(json.dumps(sidecar.to_dict(), indent=2))
        else:
            print(f"❌ Not found: {args.args[0]}")
    
    elif args.command == 'stats':
        stats = vault.stats()
        print("\n📊 VAULT STATISTICS\n")
        print(f"  Total Assets: {stats['total_assets']}")
        print(f"  Raw Storage:  {stats['raw_size_gb']} GB")
        print(f"  Derived:      {stats['derived_size_gb']} GB")
        print("\n  By Type:")
        for t, count in stats['by_type'].items():
            print(f"    {t}: {count}")
    
    elif args.command == 'watch':
        print("👁️ Starting ingest watcher...")
        observer = start_watcher(vault)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    main()
