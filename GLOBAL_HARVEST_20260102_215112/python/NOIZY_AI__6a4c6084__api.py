#!/usr/bin/env python3
"""
GABRIEL Dashboard - FastAPI Backend
REST API server for file intelligence dashboard
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import sqlite3
import os
from pathlib import Path

app = FastAPI(
    title="GABRIEL File Suite Dashboard",
    description="REST API for intelligent file management",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database path from environment or default
DB_PATH = os.getenv('GABRIEL_DB_PATH', '/Volumes/GABRIEL/gabriel.db')


class ScanRequest(BaseModel):
    volume_path: str
    workers: int = 8


class ClassifyRequest(BaseModel):
    batch_size: int = 100
    use_ai: bool = False


class OrganizeRequest(BaseModel):
    output_path: str
    mode: str = "symlink"
    dry_run: bool = True


@app.get("/")
async def root():
    return {
        "service": "GABRIEL File Suite API",
        "version": "1.0.0",
        "status": "online"
    }


@app.get("/api/stats")
async def get_stats():
    """Get overall database statistics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Overall stats
        cursor.execute('SELECT COUNT(*), SUM(size) FROM files')
        total_files, total_size = cursor.fetchone()
        
        # Category stats
        cursor.execute('''
            SELECT ai_category, COUNT(*), SUM(size)
            FROM files
            WHERE ai_category IS NOT NULL
            GROUP BY ai_category
        ''')
        categories = [
            {'category': cat, 'count': cnt, 'size_gb': round(sz / (1024**3), 2)}
            for cat, cnt, sz in cursor.fetchall()
        ]
        
        # Extension stats
        cursor.execute('''
            SELECT extension, COUNT(*)
            FROM files
            GROUP BY extension
            ORDER BY COUNT(*) DESC
            LIMIT 10
        ''')
        extensions = [
            {'extension': ext or 'none', 'count': cnt}
            for ext, cnt in cursor.fetchall()
        ]
        
        conn.close()
        
        return {
            'total_files': total_files or 0,
            'total_size_gb': round((total_size or 0) / (1024**3), 2),
            'categories': categories,
            'top_extensions': extensions
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/duplicates")
async def get_duplicates():
    """Get duplicate file groups"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT hash_sha256, COUNT(*) as count, SUM(size) as total_size
            FROM files
            WHERE hash_sha256 IS NOT NULL
            GROUP BY hash_sha256
            HAVING count > 1
            ORDER BY total_size DESC
            LIMIT 100
        ''')
        
        duplicates = []
        total_wasted = 0
        
        for hash_val, count, total_size in cursor.fetchall():
            # Get file paths
            cursor.execute('''
                SELECT path, filename, size
                FROM files
                WHERE hash_sha256 = ?
            ''', (hash_val,))
            
            files = [
                {'path': p, 'filename': f, 'size': s}
                for p, f, s in cursor.fetchall()
            ]
            
            wasted = total_size * (count - 1)
            total_wasted += wasted
            
            duplicates.append({
                'hash': hash_val[:16],
                'count': count,
                'wasted_space_mb': round(wasted / (1024**2), 2),
                'files': files
            })
        
        conn.close()
        
        return {
            'duplicate_groups': len(duplicates),
            'total_wasted_gb': round(total_wasted / (1024**3), 2),
            'duplicates': duplicates
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/categories")
async def get_categories():
    """Get all categories with file counts"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT ai_category, COUNT(*), SUM(size), AVG(ai_confidence)
            FROM files
            WHERE ai_category IS NOT NULL
            GROUP BY ai_category
            ORDER BY COUNT(*) DESC
        ''')
        
        categories = []
        for cat, count, size, confidence in cursor.fetchall():
            categories.append({
                'category': cat,
                'count': count,
                'size_gb': round(size / (1024**3), 2),
                'avg_confidence': round(confidence, 2) if confidence else 0
            })
        
        conn.close()
        return {'categories': categories}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/search")
async def search_files(
    query: str,
    category: Optional[str] = None,
    extension: Optional[str] = None,
    limit: int = 100
):
    """Search files by filename, category, or extension"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        sql = 'SELECT path, filename, ai_category, extension, size FROM files WHERE 1=1'
        params = []
        
        if query:
            sql += ' AND filename LIKE ?'
            params.append(f'%{query}%')
        
        if category:
            sql += ' AND ai_category = ?'
            params.append(category)
        
        if extension:
            sql += ' AND extension = ?'
            params.append(extension)
        
        sql += ' LIMIT ?'
        params.append(limit)
        
        cursor.execute(sql, params)
        
        results = [
            {
                'path': path,
                'filename': filename,
                'category': cat,
                'extension': ext,
                'size_mb': round(size / (1024**2), 2)
            }
            for path, filename, cat, ext, size in cursor.fetchall()
        ]
        
        conn.close()
        return {'results': results, 'count': len(results)}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    db_exists = os.path.exists(DB_PATH)
    
    return {
        'status': 'healthy' if db_exists else 'degraded',
        'database': DB_PATH,
        'database_exists': db_exists
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
