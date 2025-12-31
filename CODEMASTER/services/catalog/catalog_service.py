#!/usr/bin/env python3
"""
🗃️ CODEMASTER CATALOG SERVICE 🗃️
===================================
SQLite-based asset catalog with:
- Full-text search
- Tag management
- Project organization
- Fingerprint matching
- Derived asset tracking

v0.1: SQLite → v0.2: PostgreSQL migration path
"""

import os
import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from contextlib import contextmanager
from dataclasses import dataclass

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

CATALOG_PATH = Path(os.environ.get("CATALOG_PATH", "/Users/m2ultra/NOIZY_AI/vault/index/catalog.db"))

# ═══════════════════════════════════════════════════════════════
# 🗄️ DATABASE SCHEMA
# ═══════════════════════════════════════════════════════════════

SCHEMA = """
-- Assets table (core)
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id TEXT UNIQUE NOT NULL,
    captured_at TEXT NOT NULL,
    source_path TEXT,
    vault_path TEXT NOT NULL,
    asset_type TEXT NOT NULL,
    sha256 TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    project_id INTEGER,
    session_mode TEXT,
    duration_seconds REAL,
    codec TEXT,
    sample_rate INTEGER,
    fps REAL,
    channels INTEGER,
    resolution TEXT,
    parent_asset_id TEXT,
    confidence REAL DEFAULT 1.0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Tags table
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    color TEXT DEFAULT '#808080',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Asset-Tag junction
CREATE TABLE IF NOT EXISTS asset_tags (
    asset_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (asset_id, tag_id),
    FOREIGN KEY (asset_id) REFERENCES assets(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- Asset relations
CREATE TABLE IF NOT EXISTS relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_asset_id INTEGER NOT NULL,
    target_asset_id INTEGER NOT NULL,
    relation_type TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_asset_id) REFERENCES assets(id),
    FOREIGN KEY (target_asset_id) REFERENCES assets(id)
);

-- Fingerprints (for audio/video matching)
CREATE TABLE IF NOT EXISTS fingerprints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER NOT NULL,
    fingerprint_type TEXT NOT NULL,
    fingerprint_data BLOB NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (asset_id) REFERENCES assets(id)
);

-- Derived assets (previews, proxies, waveforms)
CREATE TABLE IF NOT EXISTS derived (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_asset_id INTEGER NOT NULL,
    derived_type TEXT NOT NULL,
    vault_path TEXT NOT NULL,
    format TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_asset_id) REFERENCES assets(id)
);

-- Full-text search
CREATE VIRTUAL TABLE IF NOT EXISTS assets_fts USING fts5(
    asset_id,
    vault_path,
    asset_type,
    project_name,
    tags,
    content='assets'
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_assets_sha256 ON assets(sha256);
CREATE INDEX IF NOT EXISTS idx_assets_type ON assets(asset_type);
CREATE INDEX IF NOT EXISTS idx_assets_project ON assets(project_id);
CREATE INDEX IF NOT EXISTS idx_assets_captured ON assets(captured_at);
CREATE INDEX IF NOT EXISTS idx_tags_name ON tags(name);
"""

# ═══════════════════════════════════════════════════════════════
# 🔗 DATABASE CONNECTION
# ═══════════════════════════════════════════════════════════════

class CatalogService:
    """SQLite-based asset catalog"""
    
    def __init__(self, db_path: Path = CATALOG_PATH):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()
    
    def _init_db(self):
        """Initialize database schema"""
        with self._connect() as conn:
            conn.executescript(SCHEMA)
    
    @contextmanager
    def _connect(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    
    # ═══════════════════════════════════════════════════════════
    # 📁 ASSET OPERATIONS
    # ═══════════════════════════════════════════════════════════
    
    def index_asset(self, sidecar: Dict) -> int:
        """Index an asset from its sidecar data"""
        with self._connect() as conn:
            # Get or create project
            project_id = None
            if sidecar.get('project'):
                project_id = self._get_or_create_project(conn, sidecar['project'])
            
            # Insert asset
            cursor = conn.execute("""
                INSERT OR REPLACE INTO assets (
                    asset_id, captured_at, source_path, vault_path, asset_type,
                    sha256, size_bytes, project_id, session_mode, duration_seconds,
                    codec, sample_rate, fps, channels, resolution, parent_asset_id, confidence
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                sidecar['asset_id'],
                sidecar['captured_at'],
                sidecar.get('source_path'),
                sidecar['vault_path'],
                sidecar['asset_type'],
                sidecar['sha256'],
                sidecar['size_bytes'],
                project_id,
                sidecar.get('session_mode'),
                sidecar.get('duration_seconds'),
                sidecar.get('codec'),
                sidecar.get('sample_rate'),
                sidecar.get('fps'),
                sidecar.get('channels'),
                sidecar.get('resolution'),
                sidecar.get('parent_asset_id'),
                sidecar.get('confidence', 1.0),
            ))
            
            asset_db_id = cursor.lastrowid
            
            # Add tags
            if sidecar.get('tags'):
                for tag in sidecar['tags']:
                    tag_id = self._get_or_create_tag(conn, tag)
                    conn.execute(
                        "INSERT OR IGNORE INTO asset_tags (asset_id, tag_id) VALUES (?, ?)",
                        (asset_db_id, tag_id)
                    )
            
            # Update FTS index
            project_name = sidecar.get('project', '')
            tags_str = ' '.join(sidecar.get('tags', []))
            conn.execute("""
                INSERT INTO assets_fts (asset_id, vault_path, asset_type, project_name, tags)
                VALUES (?, ?, ?, ?, ?)
            """, (sidecar['asset_id'], sidecar['vault_path'], sidecar['asset_type'], project_name, tags_str))
            
            return asset_db_id
    
    def _get_or_create_project(self, conn, name: str) -> int:
        """Get or create a project"""
        row = conn.execute("SELECT id FROM projects WHERE name = ?", (name,)).fetchone()
        if row:
            return row['id']
        cursor = conn.execute("INSERT INTO projects (name) VALUES (?)", (name,))
        return cursor.lastrowid
    
    def _get_or_create_tag(self, conn, name: str) -> int:
        """Get or create a tag"""
        row = conn.execute("SELECT id FROM tags WHERE name = ?", (name,)).fetchone()
        if row:
            return row['id']
        cursor = conn.execute("INSERT INTO tags (name) VALUES (?)", (name,))
        return cursor.lastrowid
    
    def get_asset(self, asset_id: str) -> Optional[Dict]:
        """Get asset by ID"""
        with self._connect() as conn:
            row = conn.execute("""
                SELECT a.*, p.name as project_name
                FROM assets a
                LEFT JOIN projects p ON a.project_id = p.id
                WHERE a.asset_id = ?
            """, (asset_id,)).fetchone()
            
            if not row:
                return None
            
            result = dict(row)
            
            # Get tags
            tags = conn.execute("""
                SELECT t.name FROM tags t
                JOIN asset_tags at ON t.id = at.tag_id
                JOIN assets a ON at.asset_id = a.id
                WHERE a.asset_id = ?
            """, (asset_id,)).fetchall()
            result['tags'] = [t['name'] for t in tags]
            
            return result
    
    def search(self, query: str = None, asset_type: str = None,
               project: str = None, tags: List[str] = None,
               date_from: str = None, date_to: str = None,
               limit: int = 100, offset: int = 0) -> List[Dict]:
        """
        Search assets with filters.
        
        Args:
            query: Full-text search query
            asset_type: Filter by type
            project: Filter by project name
            tags: Filter by tags (any match)
            date_from: ISO date string
            date_to: ISO date string
            limit: Max results
            offset: Pagination offset
        
        Returns:
            List of matching assets
        """
        with self._connect() as conn:
            conditions = []
            params = []
            
            # Full-text search
            if query:
                conditions.append("a.asset_id IN (SELECT asset_id FROM assets_fts WHERE assets_fts MATCH ?)")
                params.append(query)
            
            if asset_type:
                conditions.append("a.asset_type = ?")
                params.append(asset_type)
            
            if project:
                conditions.append("p.name = ?")
                params.append(project)
            
            if date_from:
                conditions.append("a.captured_at >= ?")
                params.append(date_from)
            
            if date_to:
                conditions.append("a.captured_at <= ?")
                params.append(date_to)
            
            where_clause = " AND ".join(conditions) if conditions else "1=1"
            
            sql = f"""
                SELECT DISTINCT a.*, p.name as project_name
                FROM assets a
                LEFT JOIN projects p ON a.project_id = p.id
                LEFT JOIN asset_tags at ON a.id = at.asset_id
                LEFT JOIN tags t ON at.tag_id = t.id
                WHERE {where_clause}
            """
            
            if tags:
                tag_placeholders = ','.join('?' * len(tags))
                sql += f" AND t.name IN ({tag_placeholders})"
                params.extend(tags)
            
            sql += f" ORDER BY a.captured_at DESC LIMIT ? OFFSET ?"
            params.extend([limit, offset])
            
            rows = conn.execute(sql, params).fetchall()
            
            results = []
            for row in rows:
                result = dict(row)
                # Get tags for each result
                asset_tags = conn.execute("""
                    SELECT t.name FROM tags t
                    JOIN asset_tags at ON t.id = at.tag_id
                    WHERE at.asset_id = ?
                """, (row['id'],)).fetchall()
                result['tags'] = [t['name'] for t in asset_tags]
                results.append(result)
            
            return results
    
    def get_by_hash(self, sha256: str) -> Optional[Dict]:
        """Find asset by SHA256 hash"""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT asset_id FROM assets WHERE sha256 = ?", (sha256,)
            ).fetchone()
            return self.get_asset(row['asset_id']) if row else None
    
    # ═══════════════════════════════════════════════════════════
    # 🏷️ TAG OPERATIONS
    # ═══════════════════════════════════════════════════════════
    
    def add_tag(self, asset_id: str, tag: str):
        """Add a tag to an asset"""
        with self._connect() as conn:
            asset = conn.execute("SELECT id FROM assets WHERE asset_id = ?", (asset_id,)).fetchone()
            if not asset:
                raise ValueError(f"Asset not found: {asset_id}")
            
            tag_id = self._get_or_create_tag(conn, tag)
            conn.execute(
                "INSERT OR IGNORE INTO asset_tags (asset_id, tag_id) VALUES (?, ?)",
                (asset['id'], tag_id)
            )
    
    def remove_tag(self, asset_id: str, tag: str):
        """Remove a tag from an asset"""
        with self._connect() as conn:
            conn.execute("""
                DELETE FROM asset_tags
                WHERE asset_id = (SELECT id FROM assets WHERE asset_id = ?)
                AND tag_id = (SELECT id FROM tags WHERE name = ?)
            """, (asset_id, tag))
    
    def list_tags(self) -> List[Dict]:
        """List all tags with counts"""
        with self._connect() as conn:
            rows = conn.execute("""
                SELECT t.name, t.color, COUNT(at.asset_id) as count
                FROM tags t
                LEFT JOIN asset_tags at ON t.id = at.tag_id
                GROUP BY t.id
                ORDER BY count DESC
            """).fetchall()
            return [dict(r) for r in rows]
    
    # ═══════════════════════════════════════════════════════════
    # 📁 PROJECT OPERATIONS
    # ═══════════════════════════════════════════════════════════
    
    def list_projects(self) -> List[Dict]:
        """List all projects with counts"""
        with self._connect() as conn:
            rows = conn.execute("""
                SELECT p.name, p.description, COUNT(a.id) as asset_count
                FROM projects p
                LEFT JOIN assets a ON p.id = a.project_id
                GROUP BY p.id
                ORDER BY asset_count DESC
            """).fetchall()
            return [dict(r) for r in rows]
    
    def create_project(self, name: str, description: str = None) -> int:
        """Create a new project"""
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO projects (name, description) VALUES (?, ?)",
                (name, description)
            )
            return cursor.lastrowid
    
    # ═══════════════════════════════════════════════════════════
    # 📊 STATISTICS
    # ═══════════════════════════════════════════════════════════
    
    def stats(self) -> Dict:
        """Get catalog statistics"""
        with self._connect() as conn:
            total = conn.execute("SELECT COUNT(*) FROM assets").fetchone()[0]
            
            by_type = {}
            for row in conn.execute(
                "SELECT asset_type, COUNT(*) as count FROM assets GROUP BY asset_type"
            ).fetchall():
                by_type[row['asset_type']] = row['count']
            
            projects = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
            tags = conn.execute("SELECT COUNT(*) FROM tags").fetchone()[0]
            
            total_size = conn.execute("SELECT SUM(size_bytes) FROM assets").fetchone()[0] or 0
            
            return {
                'total_assets': total,
                'by_type': by_type,
                'projects': projects,
                'tags': tags,
                'total_size_gb': round(total_size / (1024**3), 2),
            }

# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🗃️ CODEMASTER Catalog Service')
    parser.add_argument('command', choices=['search', 'get', 'stats', 'tags', 'projects'])
    parser.add_argument('args', nargs='*')
    parser.add_argument('--type', help='Asset type filter')
    parser.add_argument('--project', '-p', help='Project filter')
    parser.add_argument('--tags', '-t', help='Comma-separated tags')
    parser.add_argument('--limit', '-l', type=int, default=20, help='Result limit')
    
    args = parser.parse_args()
    catalog = CatalogService()
    
    if args.command == 'search':
        query = args.args[0] if args.args else None
        tags = args.tags.split(',') if args.tags else None
        results = catalog.search(
            query=query,
            asset_type=args.type,
            project=args.project,
            tags=tags,
            limit=args.limit
        )
        
        print(f"\n🔍 Found {len(results)} assets:\n")
        for r in results:
            print(f"  [{r['asset_type']}] {r['asset_id']} - {Path(r['vault_path']).name}")
            if r.get('project_name'):
                print(f"      Project: {r['project_name']}")
            if r.get('tags'):
                print(f"      Tags: {', '.join(r['tags'])}")
    
    elif args.command == 'get':
        if not args.args:
            print("Usage: catalog_service.py get <asset_id>")
            return
        asset = catalog.get_asset(args.args[0])
        if asset:
            print(json.dumps(asset, indent=2, default=str))
        else:
            print(f"❌ Not found: {args.args[0]}")
    
    elif args.command == 'stats':
        stats = catalog.stats()
        print("\n📊 CATALOG STATISTICS\n")
        print(f"  Total Assets:  {stats['total_assets']}")
        print(f"  Total Size:    {stats['total_size_gb']} GB")
        print(f"  Projects:      {stats['projects']}")
        print(f"  Tags:          {stats['tags']}")
        print("\n  By Type:")
        for t, count in stats['by_type'].items():
            print(f"    {t}: {count}")
    
    elif args.command == 'tags':
        tags = catalog.list_tags()
        print("\n🏷️ TAGS:\n")
        for t in tags:
            print(f"  {t['name']}: {t['count']} assets")
    
    elif args.command == 'projects':
        projects = catalog.list_projects()
        print("\n📁 PROJECTS:\n")
        for p in projects:
            print(f"  {p['name']}: {p['asset_count']} assets")
            if p.get('description'):
                print(f"    {p['description']}")

if __name__ == "__main__":
    main()
