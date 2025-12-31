#!/usr/bin/env python3
"""
📚 CATALOG SERVICE - The Index
==============================
SQLite-based catalog with migration path to PostgreSQL.
Full-text search, tag indexing, relationship mapping.
"""

import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass, asdict
from contextlib import contextmanager

# ═══════════════════════════════════════════════════════════════
# 🔧 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

CATALOG_DB = Path(os.environ.get("CATALOG_DB", "/Users/m2ultra/NOIZYLAB/GABRIEL/NOIZY_AI/catalog.db"))

# ═══════════════════════════════════════════════════════════════
# 📦 DATA MODELS
# ═══════════════════════════════════════════════════════════════

@dataclass
class CatalogEntry:
    """A searchable catalog entry"""
    id: str
    asset_id: str
    title: str
    description: str
    category: str
    tags: List[str]
    content_preview: str
    file_path: str
    created_at: str
    updated_at: str
    metadata: Dict[str, Any]
    search_vector: str  # Combined searchable text

@dataclass
class SearchResult:
    """Search result with relevance"""
    entry: CatalogEntry
    score: float
    highlights: List[str]

# ═══════════════════════════════════════════════════════════════
# 📚 CATALOG CORE
# ═══════════════════════════════════════════════════════════════

class CatalogService:
    """The Catalog - Searchable index of all vault assets"""
    
    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or CATALOG_DB
        self._init_db()
    
    @contextmanager
    def _get_conn(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    def _init_db(self):
        """Initialize the catalog database"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        with self._get_conn() as conn:
            cursor = conn.cursor()
            
            # Main catalog table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS catalog (
                    id TEXT PRIMARY KEY,
                    asset_id TEXT UNIQUE NOT NULL,
                    title TEXT,
                    description TEXT,
                    category TEXT,
                    tags TEXT,
                    content_preview TEXT,
                    file_path TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    metadata TEXT,
                    search_vector TEXT
                )
            """)
            
            # Full-text search virtual table
            cursor.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS catalog_fts USING fts5(
                    asset_id,
                    title,
                    description,
                    tags,
                    content_preview,
                    search_vector,
                    content='catalog',
                    content_rowid='rowid'
                )
            """)
            
            # Triggers to keep FTS in sync
            cursor.execute("""
                CREATE TRIGGER IF NOT EXISTS catalog_ai AFTER INSERT ON catalog BEGIN
                    INSERT INTO catalog_fts(rowid, asset_id, title, description, tags, content_preview, search_vector)
                    VALUES (new.rowid, new.asset_id, new.title, new.description, new.tags, new.content_preview, new.search_vector);
                END
            """)
            
            cursor.execute("""
                CREATE TRIGGER IF NOT EXISTS catalog_ad AFTER DELETE ON catalog BEGIN
                    INSERT INTO catalog_fts(catalog_fts, rowid, asset_id, title, description, tags, content_preview, search_vector)
                    VALUES ('delete', old.rowid, old.asset_id, old.title, old.description, old.tags, old.content_preview, old.search_vector);
                END
            """)
            
            cursor.execute("""
                CREATE TRIGGER IF NOT EXISTS catalog_au AFTER UPDATE ON catalog BEGIN
                    INSERT INTO catalog_fts(catalog_fts, rowid, asset_id, title, description, tags, content_preview, search_vector)
                    VALUES ('delete', old.rowid, old.asset_id, old.title, old.description, old.tags, old.content_preview, old.search_vector);
                    INSERT INTO catalog_fts(rowid, asset_id, title, description, tags, content_preview, search_vector)
                    VALUES (new.rowid, new.asset_id, new.title, new.description, new.tags, new.content_preview, new.search_vector);
                END
            """)
            
            # Tags table for faceted search
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    count INTEGER DEFAULT 1
                )
            """)
            
            # Asset-tag relationships
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS asset_tags (
                    asset_id TEXT NOT NULL,
                    tag_id INTEGER NOT NULL,
                    PRIMARY KEY (asset_id, tag_id),
                    FOREIGN KEY (tag_id) REFERENCES tags(id)
                )
            """)
            
            # Relationships between assets
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS relationships (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    relationship_type TEXT NOT NULL,
                    metadata TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            
            # Indexes
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_catalog_category ON catalog(category)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_catalog_created ON catalog(created_at)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_tags_name ON tags(name)")
            
            conn.commit()
    
    def index(self, asset_id: str, title: str, description: str = "", 
              category: str = "", tags: List[str] = None, 
              content_preview: str = "", file_path: str = "",
              metadata: Dict[str, Any] = None) -> CatalogEntry:
        """Index an asset in the catalog"""
        tags = tags or []
        metadata = metadata or {}
        now = datetime.utcnow().isoformat()
        
        # Build search vector
        search_vector = " ".join([
            title, description, " ".join(tags), content_preview, category
        ]).lower()
        
        entry_id = f"cat_{asset_id}"
        
        entry = CatalogEntry(
            id=entry_id,
            asset_id=asset_id,
            title=title,
            description=description,
            category=category,
            tags=tags,
            content_preview=content_preview[:1000],
            file_path=file_path,
            created_at=now,
            updated_at=now,
            metadata=metadata,
            search_vector=search_vector
        )
        
        with self._get_conn() as conn:
            cursor = conn.cursor()
            
            # Upsert catalog entry
            cursor.execute("""
                INSERT OR REPLACE INTO catalog 
                (id, asset_id, title, description, category, tags, content_preview,
                 file_path, created_at, updated_at, metadata, search_vector)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entry.id, entry.asset_id, entry.title, entry.description,
                entry.category, json.dumps(entry.tags), entry.content_preview,
                entry.file_path, entry.created_at, entry.updated_at,
                json.dumps(entry.metadata), entry.search_vector
            ))
            
            # Update tags
            for tag in tags:
                cursor.execute("""
                    INSERT OR IGNORE INTO tags (name, count) VALUES (?, 0)
                """, (tag.lower(),))
                cursor.execute("""
                    UPDATE tags SET count = count + 1 WHERE name = ?
                """, (tag.lower(),))
                
                cursor.execute("SELECT id FROM tags WHERE name = ?", (tag.lower(),))
                tag_id = cursor.fetchone()[0]
                
                cursor.execute("""
                    INSERT OR IGNORE INTO asset_tags (asset_id, tag_id) VALUES (?, ?)
                """, (asset_id, tag_id))
            
            conn.commit()
        
        return entry
    
    def search(self, query: str, category: str = None, 
               tags: List[str] = None, limit: int = 50) -> List[SearchResult]:
        """Full-text search across the catalog"""
        results = []
        
        with self._get_conn() as conn:
            cursor = conn.cursor()
            
            # Build FTS query
            fts_query = query.replace('"', '""')
            
            sql = """
                SELECT c.*, bm25(catalog_fts) as score
                FROM catalog c
                JOIN catalog_fts ON c.rowid = catalog_fts.rowid
                WHERE catalog_fts MATCH ?
            """
            params = [fts_query]
            
            if category:
                sql += " AND c.category LIKE ?"
                params.append(f"%{category}%")
            
            sql += " ORDER BY score LIMIT ?"
            params.append(limit)
            
            cursor.execute(sql, params)
            rows = cursor.fetchall()
            
            for row in rows:
                entry = CatalogEntry(
                    id=row['id'],
                    asset_id=row['asset_id'],
                    title=row['title'],
                    description=row['description'],
                    category=row['category'],
                    tags=json.loads(row['tags'] or '[]'),
                    content_preview=row['content_preview'],
                    file_path=row['file_path'],
                    created_at=row['created_at'],
                    updated_at=row['updated_at'],
                    metadata=json.loads(row['metadata'] or '{}'),
                    search_vector=row['search_vector']
                )
                results.append(SearchResult(
                    entry=entry,
                    score=abs(row['score']),
                    highlights=self._extract_highlights(query, entry)
                ))
        
        # Filter by tags if provided
        if tags:
            results = [r for r in results if any(t.lower() in [x.lower() for x in r.entry.tags] for t in tags)]
        
        return results
    
    def _extract_highlights(self, query: str, entry: CatalogEntry) -> List[str]:
        """Extract text snippets containing the query"""
        highlights = []
        query_lower = query.lower()
        
        for text in [entry.title, entry.description, entry.content_preview]:
            if query_lower in text.lower():
                idx = text.lower().find(query_lower)
                start = max(0, idx - 50)
                end = min(len(text), idx + len(query) + 50)
                snippet = "..." + text[start:end] + "..."
                highlights.append(snippet)
        
        return highlights[:3]
    
    def get_by_asset_id(self, asset_id: str) -> Optional[CatalogEntry]:
        """Get catalog entry by asset ID"""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM catalog WHERE asset_id = ?", (asset_id,))
            row = cursor.fetchone()
            
            if row:
                return CatalogEntry(
                    id=row['id'],
                    asset_id=row['asset_id'],
                    title=row['title'],
                    description=row['description'],
                    category=row['category'],
                    tags=json.loads(row['tags'] or '[]'),
                    content_preview=row['content_preview'],
                    file_path=row['file_path'],
                    created_at=row['created_at'],
                    updated_at=row['updated_at'],
                    metadata=json.loads(row['metadata'] or '{}'),
                    search_vector=row['search_vector']
                )
        return None
    
    def list_tags(self, limit: int = 100) -> List[Tuple[str, int]]:
        """List all tags with counts"""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, count FROM tags 
                ORDER BY count DESC LIMIT ?
            """, (limit,))
            return cursor.fetchall()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get catalog statistics"""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM catalog")
            total_entries = cursor.fetchone()[0]
            
            cursor.execute("SELECT category, COUNT(*) FROM catalog GROUP BY category")
            by_category = dict(cursor.fetchall())
            
            cursor.execute("SELECT COUNT(*) FROM tags")
            total_tags = cursor.fetchone()[0]
            
            return {
                "total_entries": total_entries,
                "by_category": by_category,
                "total_tags": total_tags
            }

# ═══════════════════════════════════════════════════════════════
# 🚀 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="📚 CATALOG SERVICE")
    parser.add_argument("command", choices=["search", "index", "tags", "stats"])
    parser.add_argument("args", nargs="*")
    
    args = parser.parse_args()
    catalog = CatalogService()
    
    if args.command == "search":
        query = " ".join(args.args) if args.args else ""
        results = catalog.search(query)
        print(f"🔍 Found {len(results)} results for '{query}':")
        for r in results[:20]:
            print(f"  [{r.entry.category}] {r.entry.title} (score: {r.score:.2f})")
            if r.highlights:
                print(f"    → {r.highlights[0][:80]}...")
    
    elif args.command == "tags":
        tags = catalog.list_tags()
        print(f"🏷️ Top tags:")
        for name, count in tags[:30]:
            print(f"  {name}: {count}")
    
    elif args.command == "stats":
        stats = catalog.get_stats()
        print(f"📊 CATALOG STATISTICS")
        print(f"   Total Entries: {stats['total_entries']}")
        print(f"   Total Tags: {stats['total_tags']}")
        print(f"   Categories:")
        for cat, count in stats.get('by_category', {}).items():
            print(f"      {cat}: {count}")

if __name__ == "__main__":
    main()
