#!/usr/bin/env python3
"""
🔍 SEMANTIC FILE SYSTEM - AI-POWERED FILE INDEXING
Fish Music Inc - CB_01
🔥 GORUNFREE! 🎸🔥
"""

import os
import json
from pathlib import Path
from datetime import datetime

class SemanticFileIndexer:
    """Index files with AI-powered semantic search"""
    
    def __init__(self, root_path: str = "/Users/m2ultra"):
        self.root = Path(root_path)
        self.index_path = Path.home() / "NoizyIndex"
        self.index_path.mkdir(exist_ok=True)
        
    def index_directory(self, path: Path, max_depth: int = 3):
        """Index directory structure"""
        print(f"📁 Indexing: {path}")
        
        index = {
            "indexed_at": datetime.now().isoformat(),
            "root_path": str(path),
            "files": [],
            "directories": [],
        }
        
        try:
            for item in path.rglob("*"):
                # Skip hidden files
                if item.name.startswith('.'):
                    continue
                
                # Calculate depth
                depth = len(item.relative_to(path).parts)
                if depth > max_depth:
                    continue
                
                if item.is_file():
                    index["files"].append({
                        "path": str(item),
                        "name": item.name,
                        "size": item.stat().st_size,
                        "modified": datetime.fromtimestamp(item.stat().st_mtime).isoformat(),
                        "type": item.suffix,
                    })
                elif item.is_dir():
                    index["directories"].append({
                        "path": str(item),
                        "name": item.name,
                    })
        except PermissionError:
            print(f"   ⚠️  Permission denied")
        
        # Save index
        index_file = self.index_path / f"index_{path.name}.json"
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)
        
        print(f"   ✅ Indexed {len(index['files'])} files, {len(index['directories'])} directories")
        print(f"   💾 Saved to: {index_file}")
        
        return index
    
    def search(self, query: str):
        """Search indexed files"""
        results = []
        
        for index_file in self.index_path.glob("index_*.json"):
            with open(index_file) as f:
                index = json.load(f)
                
            for file in index["files"]:
                if query.lower() in file["name"].lower():
                    results.append(file)
        
        return results

if __name__ == "__main__":
    indexer = SemanticFileIndexer()
    
    # Index key directories
    print("🔍 SEMANTIC FILE INDEXER")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")
    
    paths_to_index = [
        Path.home() / "NOIZYLAB",
        Path.home() / "Projects",
        Path.home() / "Desktop",
    ]
    
    for path in paths_to_index:
        if path.exists():
            indexer.index_directory(path, max_depth=2)
            print("")
    
    print("✅ Indexing complete!")
    print(f"   Index location: {indexer.index_path}")
    print("")
    print("🔥 GORUNFREE! 🎸🔥")
