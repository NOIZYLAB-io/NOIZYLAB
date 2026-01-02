#!/usr/bin/env python3
"""
🧠 GABRIEL DEEP KNOWLEDGE INDEXER
=================================
Scans ALL reachable paths and builds a unified knowledge base.

Targets:
- ~/NOIZYLAB (main repo)
- ~/AI_COMPLETE_BRAIN (prompts, patterns, knowledge)
- ~/GABRIEL_UNIFIED (unified systems)
- ~/Documents/NOIZYLAB_TEXT_VAULT (massive knowledge archive)
- ~/Documents/_ZERO_LATENCY_VAULT (archived code/docs)
- ~/.gabriel_learning_x1000 (learning data)
- All .md, .py, .ts, .js, .json, .yaml, .sql files
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Set
import re

# =============================================================================
# CONFIGURATION
# =============================================================================

HOME = Path.home()
GABRIEL_ROOT = HOME / "NOIZYLAB" / "GABRIEL"
OUTPUT_DIR = GABRIEL_ROOT / "memcell_data"
OUTPUT_DIR.mkdir(exist_ok=True)

# All paths to scan (deep)
SCAN_PATHS = [
    HOME / "NOIZYLAB",
    HOME / "AI_COMPLETE_BRAIN",
    HOME / "GABRIEL_UNIFIED",
    HOME / "Documents" / "NOIZYLAB",
    HOME / "Documents" / "NOIZYLAB_TEXT_VAULT",
    HOME / "Documents" / "_ZERO_LATENCY_VAULT",
    HOME / "Documents" / "GABRIEL",
    HOME / ".gabriel",
    HOME / ".gabriel_learning_x1000",
    HOME / ".noizylab",
    HOME / ".noizyvox",
    HOME / "CODE_MASTER",
    HOME / "CODEBEAST",
    HOME / "bin",
]

# File extensions to index (code & knowledge)
CODE_EXTENSIONS = {'.py', '.ts', '.js', '.jsx', '.tsx', '.go', '.rs', '.sh', '.sql', '.lua'}
DOC_EXTENSIONS = {'.md', '.txt', '.rst', '.json', '.yaml', '.yml', '.toml', '.xml', '.html'}
CONFIG_EXTENSIONS = {'.env', '.cfg', '.ini', '.conf', '.config'}

# Skip patterns
SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv', '.cache',
    'dist', 'build', '.next', '.nuxt', 'coverage', '.pytest_cache',
    'site-packages', '.egg-info', 'htmlcov', '.mypy_cache', '.tox',
    'Library', 'Caches', 'Application Support'
}

SKIP_FILES = {'.DS_Store', 'Thumbs.db', '.gitkeep', 'package-lock.json', 'yarn.lock'}

# =============================================================================
# KNOWLEDGE CATEGORIES
# =============================================================================

CATEGORIES = {
    'prompts': ['prompt', 'system_prompt', 'agent', 'instruction'],
    'api': ['api', 'endpoint', 'route', 'handler', 'controller'],
    'voice': ['voice', 'tts', 'speech', 'audio', 'sound', 'rvc', 'xtts'],
    'ai_ml': ['model', 'train', 'inference', 'neural', 'torch', 'tensor', 'embedding'],
    'database': ['sql', 'query', 'schema', 'migration', 'db', 'postgres', 'sqlite'],
    'cloud': ['cloudflare', 'worker', 'azure', 'aws', 'deploy', 'docker', 'k8s'],
    'network': ['network', 'socket', 'http', 'websocket', 'mqtt', 'nats'],
    'automation': ['script', 'cron', 'task', 'job', 'scheduler', 'workflow'],
    'ui': ['react', 'component', 'ui', 'frontend', 'css', 'style', 'tailwind'],
    'config': ['config', 'settings', 'env', 'options', 'parameters'],
    'docs': ['readme', 'documentation', 'guide', 'tutorial', 'reference'],
}

# =============================================================================
# SCANNER
# =============================================================================

class DeepKnowledgeScanner:
    def __init__(self):
        self.brain = {
            "version": "2.0.0",
            "created": datetime.now().isoformat(),
            "stats": {},
            "files": [],
            "code_files": [],
            "doc_files": [],
            "prompts": [],
            "apis": [],
            "models": [],
            "scripts": [],
            "configs": [],
            "knowledge_base": [],
            "by_category": {k: [] for k in CATEGORIES},
            "by_extension": {},
            "by_directory": {},
            "functions": [],
            "classes": [],
            "imports": [],
            "todos": [],
            "errors": [],
        }
        self.seen_hashes: Set[str] = set()
        self.file_count = 0
        self.total_lines = 0
        self.total_size = 0

    def scan_all(self):
        """Scan all configured paths."""
        print("🔍 GABRIEL DEEP KNOWLEDGE SCAN")
        print("=" * 50)
        
        for scan_path in SCAN_PATHS:
            if scan_path.exists():
                print(f"\n📂 Scanning: {scan_path}")
                self._scan_directory(scan_path, depth=0, max_depth=10)
            else:
                print(f"⏭️  Skip (not found): {scan_path}")
        
        self._compute_stats()
        self._extract_knowledge()
        self._save_brain()
        
        print("\n" + "=" * 50)
        print(f"✅ SCAN COMPLETE!")
        print(f"   Files indexed: {self.file_count}")
        print(f"   Total lines: {self.total_lines:,}")
        print(f"   Total size: {self.total_size / 1024 / 1024:.1f} MB")
        print(f"   Brain saved to: {OUTPUT_DIR / 'gabriel_brain.json'}")

    def _scan_directory(self, path: Path, depth: int, max_depth: int):
        """Recursively scan a directory."""
        if depth > max_depth:
            return
        
        try:
            for item in path.iterdir():
                # Skip hidden and excluded
                if item.name.startswith('.') and item.name not in ['.env', '.gabriel']:
                    continue
                if item.name in SKIP_DIRS or item.name in SKIP_FILES:
                    continue
                
                if item.is_dir():
                    self._scan_directory(item, depth + 1, max_depth)
                elif item.is_file():
                    self._index_file(item)
        except PermissionError:
            pass
        except Exception as e:
            self.brain["errors"].append({"path": str(path), "error": str(e)})

    def _index_file(self, file_path: Path):
        """Index a single file."""
        ext = file_path.suffix.lower()
        
        # Only index relevant files
        all_extensions = CODE_EXTENSIONS | DOC_EXTENSIONS | CONFIG_EXTENSIONS
        if ext not in all_extensions and file_path.name not in ['.env', 'Makefile', 'Dockerfile']:
            return
        
        try:
            stat = file_path.stat()
            size = stat.st_size
            
            # Skip very large files (> 5MB)
            if size > 5 * 1024 * 1024:
                return
            
            # Skip empty files
            if size == 0:
                return
            
            # Read content
            try:
                content = file_path.read_text(errors='ignore')
            except:
                return
            
            # Deduplicate by content hash
            content_hash = hashlib.md5(content.encode()).hexdigest()
            if content_hash in self.seen_hashes:
                return
            self.seen_hashes.add(content_hash)
            
            lines = content.count('\n') + 1
            self.file_count += 1
            self.total_lines += lines
            self.total_size += size
            
            # File entry
            entry = {
                "path": str(file_path),
                "name": file_path.name,
                "ext": ext,
                "size": size,
                "lines": lines,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "hash": content_hash[:8],
            }
            
            self.brain["files"].append(entry)
            
            # Categorize
            if ext in CODE_EXTENSIONS:
                self.brain["code_files"].append(entry)
                self._extract_code_info(file_path, content, entry)
            elif ext in DOC_EXTENSIONS:
                self.brain["doc_files"].append(entry)
                self._extract_doc_info(file_path, content, entry)
            
            # By extension
            if ext not in self.brain["by_extension"]:
                self.brain["by_extension"][ext] = []
            self.brain["by_extension"][ext].append(entry["path"])
            
            # By category
            path_lower = str(file_path).lower()
            name_lower = file_path.name.lower()
            for cat, keywords in CATEGORIES.items():
                if any(kw in path_lower or kw in name_lower for kw in keywords):
                    self.brain["by_category"][cat].append(entry["path"])
                    break
            
            # Progress
            if self.file_count % 500 == 0:
                print(f"   ... {self.file_count} files indexed")
                
        except Exception as e:
            pass

    def _extract_code_info(self, path: Path, content: str, entry: dict):
        """Extract code-specific information."""
        ext = path.suffix
        
        # Python
        if ext == '.py':
            # Functions
            for match in re.finditer(r'^(?:async\s+)?def\s+(\w+)\s*\(', content, re.MULTILINE):
                self.brain["functions"].append({
                    "name": match.group(1),
                    "file": str(path),
                    "line": content[:match.start()].count('\n') + 1
                })
            
            # Classes
            for match in re.finditer(r'^class\s+(\w+)', content, re.MULTILINE):
                self.brain["classes"].append({
                    "name": match.group(1),
                    "file": str(path)
                })
            
            # Imports
            for match in re.finditer(r'^(?:from\s+(\S+)\s+)?import\s+(.+)$', content, re.MULTILINE):
                module = match.group(1) or match.group(2).split(',')[0].strip()
                if module not in ['os', 'sys', 'json', 're', 'typing', 'pathlib']:
                    self.brain["imports"].append(module)
        
        # TypeScript/JavaScript
        elif ext in ['.ts', '.tsx', '.js', '.jsx']:
            # Functions
            for match in re.finditer(r'(?:export\s+)?(?:async\s+)?function\s+(\w+)', content):
                self.brain["functions"].append({
                    "name": match.group(1),
                    "file": str(path)
                })
            
            # Arrow functions
            for match in re.finditer(r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>', content):
                self.brain["functions"].append({
                    "name": match.group(1),
                    "file": str(path)
                })
        
        # TODOs
        for match in re.finditer(r'(?:#|//|/\*)\s*TODO[:\s]+(.+?)(?:\n|\*/)', content, re.IGNORECASE):
            self.brain["todos"].append({
                "text": match.group(1).strip()[:200],
                "file": str(path)
            })

    def _extract_doc_info(self, path: Path, content: str, entry: dict):
        """Extract documentation-specific info."""
        name_lower = path.name.lower()
        
        # Prompts
        if 'prompt' in name_lower or 'agent' in name_lower or 'system' in name_lower:
            self.brain["prompts"].append({
                "path": str(path),
                "name": path.name,
                "preview": content[:500]
            })
        
        # Knowledge base entries (markdown with headers)
        if path.suffix == '.md':
            headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            if headers:
                self.brain["knowledge_base"].append({
                    "path": str(path),
                    "title": headers[0] if headers else path.stem,
                    "headers": headers[:10],
                    "preview": content[:300]
                })

    def _compute_stats(self):
        """Compute final statistics."""
        self.brain["stats"] = {
            "total_files": self.file_count,
            "total_lines": self.total_lines,
            "total_size_mb": round(self.total_size / 1024 / 1024, 2),
            "code_files": len(self.brain["code_files"]),
            "doc_files": len(self.brain["doc_files"]),
            "functions": len(self.brain["functions"]),
            "classes": len(self.brain["classes"]),
            "prompts": len(self.brain["prompts"]),
            "knowledge_entries": len(self.brain["knowledge_base"]),
            "todos": len(self.brain["todos"]),
            "unique_imports": len(set(self.brain["imports"])),
            "by_extension": {k: len(v) for k, v in self.brain["by_extension"].items()},
            "by_category": {k: len(v) for k, v in self.brain["by_category"].items()},
        }
        
        # Dedupe imports
        self.brain["imports"] = list(set(self.brain["imports"]))[:500]

    def _extract_knowledge(self):
        """Build knowledge summaries."""
        # Top directories
        dir_counts: Dict[str, int] = {}
        for f in self.brain["files"]:
            parent = str(Path(f["path"]).parent)
            dir_counts[parent] = dir_counts.get(parent, 0) + 1
        
        self.brain["by_directory"] = dict(sorted(dir_counts.items(), key=lambda x: -x[1])[:100])

    def _save_brain(self):
        """Save the brain to disk."""
        # Main brain file
        brain_path = OUTPUT_DIR / "gabriel_brain.json"
        with open(brain_path, 'w') as f:
            json.dump(self.brain, f, indent=2, default=str)
        
        # Quick reference files
        quick_ref = {
            "version": self.brain["version"],
            "stats": self.brain["stats"],
            "top_directories": list(self.brain["by_directory"].keys())[:20],
            "prompts": [p["path"] for p in self.brain["prompts"][:50]],
            "knowledge_titles": [k["title"] for k in self.brain["knowledge_base"][:50]],
        }
        
        with open(OUTPUT_DIR / "gabriel_brain_quick.json", 'w') as f:
            json.dump(quick_ref, f, indent=2)
        
        # Prompts index
        with open(OUTPUT_DIR / "prompts_index.json", 'w') as f:
            json.dump(self.brain["prompts"], f, indent=2)
        
        # Functions index
        with open(OUTPUT_DIR / "functions_index.json", 'w') as f:
            json.dump(self.brain["functions"][:2000], f, indent=2)

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    scanner = DeepKnowledgeScanner()
    scanner.scan_all()
