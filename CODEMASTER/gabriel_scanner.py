#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║        ██████╗  █████╗ ██████╗ ██████╗ ██╗███████╗██╗                             ║
║       ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║                             ║
║       ██║  ███╗███████║██████╔╝██████╔╝██║█████╗  ██║                             ║
║       ██║   ██║██╔══██║██╔══██╗██╔══██╗██║██╔══╝  ██║                             ║
║       ╚██████╔╝██║  ██║██████╔╝██║  ██║██║███████╗███████╗                        ║
║        ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝                        ║
║                                                                                   ║
║                    ⚡ CODE SCANNER & INDEXER ⚡                                    ║
║                                                                                   ║
║              Scan, Index, and Catalog all GABRIEL Code                            ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import ast
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import orjson
    def json_dumps(obj): return orjson.dumps(obj).decode()
    def json_loads(s): return orjson.loads(s)
    ORJSON = True
except ImportError:
    def json_dumps(obj): return json.dumps(obj)
    def json_loads(s): return json.loads(s)
    ORJSON = False


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

GABRIEL_ROOT = Path("/Users/m2ultra/NOIZYLAB/GABRIEL")
INDEX_FILE = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER/data/gabriel_index.json")
INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)

# Directories to scan (core GABRIEL code)
SCAN_DIRS = [
    GABRIEL_ROOT / "CODE",
    GABRIEL_ROOT / "10_CORE",
    GABRIEL_ROOT / "11_AGENTS",
    GABRIEL_ROOT / "12_MCP",
    GABRIEL_ROOT / "automation",
    GABRIEL_ROOT / "mcp_servers",
]

# Patterns to exclude
EXCLUDE_PATTERNS = [
    "__pycache__",
    ".venv",
    "venv",
    "site-packages",
    "node_modules",
    ".git",
    "archive-harvest",  # Large legacy files
]


# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class FunctionInfo:
    name: str
    lineno: int
    args: List[str]
    decorators: List[str]
    docstring: Optional[str]
    is_async: bool
    complexity: int = 0

@dataclass
class ClassInfo:
    name: str
    lineno: int
    bases: List[str]
    methods: List[str]
    docstring: Optional[str]

@dataclass 
class FileInfo:
    path: str
    size: int
    lines: int
    functions: List[FunctionInfo]
    classes: List[ClassInfo]
    imports: List[str]
    docstring: Optional[str]
    hash: str
    scanned_at: str
    tags: List[str] = field(default_factory=list)


# ═══════════════════════════════════════════════════════════════════════════════
# AST ANALYZER
# ═══════════════════════════════════════════════════════════════════════════════

class PythonAnalyzer:
    """Analyze Python files using AST"""
    
    @staticmethod
    def analyze_file(filepath: Path) -> Optional[FileInfo]:
        """Analyze a single Python file"""
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            lines = len(content.splitlines())
            
            try:
                tree = ast.parse(content)
            except SyntaxError:
                return None
            
            # Extract module docstring
            docstring = ast.get_docstring(tree)
            
            # Extract imports
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            
            # Extract functions
            functions = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_info = FunctionInfo(
                        name=node.name,
                        lineno=node.lineno,
                        args=[arg.arg for arg in node.args.args],
                        decorators=[PythonAnalyzer._get_decorator_name(d) for d in node.decorator_list],
                        docstring=ast.get_docstring(node),
                        is_async=isinstance(node, ast.AsyncFunctionDef),
                        complexity=PythonAnalyzer._calculate_complexity(node)
                    )
                    functions.append(func_info)
            
            # Extract classes
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                    bases = [PythonAnalyzer._get_base_name(b) for b in node.bases]
                    class_info = ClassInfo(
                        name=node.name,
                        lineno=node.lineno,
                        bases=bases,
                        methods=methods,
                        docstring=ast.get_docstring(node)
                    )
                    classes.append(class_info)
            
            # Generate tags based on content
            tags = PythonAnalyzer._generate_tags(filepath, imports, functions, classes)
            
            # File hash
            file_hash = hashlib.md5(content.encode()).hexdigest()[:12]
            
            return FileInfo(
                path=str(filepath),
                size=filepath.stat().st_size,
                lines=lines,
                functions=functions,
                classes=classes,
                imports=imports,
                docstring=docstring,
                hash=file_hash,
                scanned_at=datetime.now().isoformat(),
                tags=tags
            )
            
        except Exception as e:
            return None
    
    @staticmethod
    def _get_decorator_name(node) -> str:
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return node.attr
        elif isinstance(node, ast.Call):
            return PythonAnalyzer._get_decorator_name(node.func)
        return "unknown"
    
    @staticmethod
    def _get_base_name(node) -> str:
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return node.attr
        return "unknown"
    
    @staticmethod
    def _calculate_complexity(node) -> int:
        """Simple cyclomatic complexity estimation"""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler, 
                                  ast.With, ast.Assert, ast.comprehension)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity
    
    @staticmethod
    def _generate_tags(filepath: Path, imports: List[str], 
                       functions: List[FunctionInfo], classes: List[ClassInfo]) -> List[str]:
        """Generate tags based on file content"""
        tags = []
        
        # Check imports for framework detection
        import_str = " ".join(imports).lower()
        if "fastapi" in import_str:
            tags.append("fastapi")
        if "asyncio" in import_str:
            tags.append("async")
        if "httpx" in import_str or "aiohttp" in import_str:
            tags.append("http")
        if "mcp" in import_str:
            tags.append("mcp")
        if "cloudflare" in import_str:
            tags.append("cloudflare")
        if "openai" in import_str or "anthropic" in import_str:
            tags.append("ai")
        if "torch" in import_str or "tensorflow" in import_str:
            tags.append("ml")
        
        # Check filename
        name = filepath.stem.lower()
        if "turbo" in name:
            tags.append("turbo")
        if "gabriel" in name:
            tags.append("gabriel")
        if "mc96" in name:
            tags.append("mc96")
        if "agent" in name:
            tags.append("agent")
        if "server" in name:
            tags.append("server")
        if "test" in name:
            tags.append("test")
        
        # Check for async functions
        if any(f.is_async for f in functions):
            tags.append("async")
        
        return list(set(tags))


# ═══════════════════════════════════════════════════════════════════════════════
# SCANNER
# ═══════════════════════════════════════════════════════════════════════════════

class GabrielScanner:
    """Scan and index all GABRIEL code"""
    
    def __init__(self):
        self.index: Dict[str, Any] = {
            "version": "2.0",
            "scanned_at": None,
            "stats": {},
            "files": {},
            "functions": {},
            "classes": {},
            "tags": {},
        }
        self.analyzer = PythonAnalyzer()
    
    def should_exclude(self, path: Path) -> bool:
        """Check if path should be excluded"""
        path_str = str(path)
        return any(pattern in path_str for pattern in EXCLUDE_PATTERNS)
    
    def find_python_files(self) -> List[Path]:
        """Find all Python files to scan"""
        files = []
        for scan_dir in SCAN_DIRS:
            if scan_dir.exists():
                for py_file in scan_dir.rglob("*.py"):
                    if not self.should_exclude(py_file):
                        files.append(py_file)
        return files
    
    def scan_file(self, filepath: Path) -> Optional[FileInfo]:
        """Scan a single file"""
        return self.analyzer.analyze_file(filepath)
    
    def scan_all(self, max_workers: int = 24) -> Dict[str, Any]:
        """Scan all Python files"""
        print(f"\n🔍 Finding Python files in GABRIEL...")
        files = self.find_python_files()
        print(f"📂 Found {len(files)} files to scan")
        
        start_time = time.time()
        scanned = 0
        failed = 0
        total_lines = 0
        total_functions = 0
        total_classes = 0
        
        # Scan files in parallel
        print(f"⚡ Scanning with {max_workers} workers...")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.scan_file, files))
        
        # Process results
        for result in results:
            if result:
                scanned += 1
                total_lines += result.lines
                total_functions += len(result.functions)
                total_classes += len(result.classes)
                
                # Store file info
                rel_path = str(Path(result.path).relative_to(GABRIEL_ROOT))
                self.index["files"][rel_path] = {
                    "path": result.path,
                    "size": result.size,
                    "lines": result.lines,
                    "functions": len(result.functions),
                    "classes": len(result.classes),
                    "imports": result.imports[:20],  # Limit imports
                    "docstring": result.docstring[:500] if result.docstring else None,
                    "hash": result.hash,
                    "tags": result.tags,
                    "scanned_at": result.scanned_at
                }
                
                # Index functions
                for func in result.functions:
                    func_key = f"{rel_path}::{func.name}"
                    self.index["functions"][func_key] = {
                        "file": rel_path,
                        "name": func.name,
                        "lineno": func.lineno,
                        "args": func.args,
                        "is_async": func.is_async,
                        "complexity": func.complexity,
                        "decorators": func.decorators,
                        "docstring": func.docstring[:200] if func.docstring else None
                    }
                
                # Index classes
                for cls in result.classes:
                    cls_key = f"{rel_path}::{cls.name}"
                    self.index["classes"][cls_key] = {
                        "file": rel_path,
                        "name": cls.name,
                        "lineno": cls.lineno,
                        "bases": cls.bases,
                        "methods": cls.methods,
                        "docstring": cls.docstring[:200] if cls.docstring else None
                    }
                
                # Index by tags
                for tag in result.tags:
                    if tag not in self.index["tags"]:
                        self.index["tags"][tag] = []
                    self.index["tags"][tag].append(rel_path)
            else:
                failed += 1
        
        elapsed = time.time() - start_time
        
        # Update stats
        self.index["scanned_at"] = datetime.now().isoformat()
        self.index["stats"] = {
            "files_scanned": scanned,
            "files_failed": failed,
            "total_lines": total_lines,
            "total_functions": total_functions,
            "total_classes": total_classes,
            "scan_time_seconds": round(elapsed, 2),
            "files_per_second": round(scanned / elapsed, 1) if elapsed > 0 else 0
        }
        
        return self.index
    
    def save_index(self):
        """Save index to disk"""
        with open(INDEX_FILE, "w") as f:
            json.dump(self.index, f, indent=2)
        print(f"💾 Index saved to {INDEX_FILE}")
    
    def load_index(self) -> bool:
        """Load existing index"""
        if INDEX_FILE.exists():
            with open(INDEX_FILE) as f:
                self.index = json.load(f)
            return True
        return False
    
    def search(self, query: str, search_type: str = "all") -> Dict[str, List]:
        """Search the index"""
        query_lower = query.lower()
        results = {"files": [], "functions": [], "classes": []}
        
        if search_type in ["all", "files"]:
            for path, info in self.index.get("files", {}).items():
                if query_lower in path.lower():
                    results["files"].append({"path": path, **info})
                elif info.get("docstring") and query_lower in info["docstring"].lower():
                    results["files"].append({"path": path, **info})
        
        if search_type in ["all", "functions"]:
            for key, info in self.index.get("functions", {}).items():
                if query_lower in info["name"].lower():
                    results["functions"].append(info)
                elif info.get("docstring") and query_lower in info["docstring"].lower():
                    results["functions"].append(info)
        
        if search_type in ["all", "classes"]:
            for key, info in self.index.get("classes", {}).items():
                if query_lower in info["name"].lower():
                    results["classes"].append(info)
        
        return results
    
    def get_by_tag(self, tag: str) -> List[str]:
        """Get files by tag"""
        return self.index.get("tags", {}).get(tag, [])


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║        ██████╗  █████╗ ██████╗ ██████╗ ██╗███████╗██╗                             ║
║       ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║                             ║
║       ██║  ███╗███████║██████╔╝██████╔╝██║█████╗  ██║                             ║
║       ██║   ██║██╔══██║██╔══██╗██╔══██╗██║██╔══╝  ██║                             ║
║       ╚██████╔╝██║  ██║██████╔╝██║  ██║██║███████╗███████╗                        ║
║        ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝                        ║
║                    ⚡ CODE SCANNER & INDEXER ⚡                                    ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    """)


def main():
    print_banner()
    
    scanner = GabrielScanner()
    
    if len(sys.argv) < 2:
        print("Usage: python gabriel_scanner.py [scan|search|stats|tags]")
        print("\nCommands:")
        print("  scan              - Scan all GABRIEL code")
        print("  search <query>    - Search the index")
        print("  stats             - Show index statistics")
        print("  tags              - List all tags")
        print("  tag <tagname>     - Get files by tag")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "scan":
        index = scanner.scan_all()
        scanner.save_index()
        
        stats = index["stats"]
        print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                            📊 SCAN COMPLETE                                       ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  📂 Files Scanned:    {stats['files_scanned']:>6}                                              ║
║  ❌ Files Failed:     {stats['files_failed']:>6}                                              ║
║  📝 Total Lines:      {stats['total_lines']:>6}                                              ║
║  🔧 Functions:        {stats['total_functions']:>6}                                              ║
║  📦 Classes:          {stats['total_classes']:>6}                                              ║
║  ⏱️  Scan Time:        {stats['scan_time_seconds']:>6.1f}s                                             ║
║  ⚡ Speed:            {stats['files_per_second']:>6.1f} files/sec                                     ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
        """)
    
    elif cmd == "search" and len(sys.argv) > 2:
        if not scanner.load_index():
            print("❌ No index found. Run 'scan' first.")
            return
        
        query = " ".join(sys.argv[2:])
        results = scanner.search(query)
        
        print(f"\n🔍 Search: '{query}'")
        print(f"📂 Files: {len(results['files'])}")
        for f in results['files'][:10]:
            print(f"   - {f['path']} ({f['lines']} lines)")
        
        print(f"\n🔧 Functions: {len(results['functions'])}")
        for f in results['functions'][:10]:
            async_mark = "async " if f['is_async'] else ""
            print(f"   - {async_mark}{f['name']}() in {f['file']}:{f['lineno']}")
        
        print(f"\n📦 Classes: {len(results['classes'])}")
        for c in results['classes'][:10]:
            print(f"   - {c['name']} in {c['file']}:{c['lineno']}")
    
    elif cmd == "stats":
        if not scanner.load_index():
            print("❌ No index found. Run 'scan' first.")
            return
        
        stats = scanner.index.get("stats", {})
        print(f"""
📊 Index Statistics:
  Files: {stats.get('files_scanned', 0)}
  Lines: {stats.get('total_lines', 0)}
  Functions: {stats.get('total_functions', 0)}
  Classes: {stats.get('total_classes', 0)}
  Scanned: {scanner.index.get('scanned_at', 'Unknown')}
        """)
    
    elif cmd == "tags":
        if not scanner.load_index():
            print("❌ No index found. Run 'scan' first.")
            return
        
        tags = scanner.index.get("tags", {})
        print("\n🏷️  Tags:")
        for tag, files in sorted(tags.items(), key=lambda x: -len(x[1])):
            print(f"   {tag}: {len(files)} files")
    
    elif cmd == "tag" and len(sys.argv) > 2:
        if not scanner.load_index():
            print("❌ No index found. Run 'scan' first.")
            return
        
        tag = sys.argv[2]
        files = scanner.get_by_tag(tag)
        print(f"\n🏷️  Tag '{tag}': {len(files)} files")
        for f in files[:20]:
            print(f"   - {f}")
    
    else:
        print("Unknown command. Use: scan, search, stats, tags, tag")


if __name__ == "__main__":
    main()
