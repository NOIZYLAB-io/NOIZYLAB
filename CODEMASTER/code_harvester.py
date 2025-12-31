#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║   ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███████╗   ║
║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║  ██║██╔══██╗██╔══██╗██║   ██║██╔════╝   ║
║  ██║     ██║   ██║██║  ██║█████╗      ███████║███████║██████╔╝██║   ██║█████╗     ║
║  ██║     ██║   ██║██║  ██║██╔══╝      ██╔══██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝     ║
║  ╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗   ║
║   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝   ║
║                                                                                   ║
║                    ⚡ HARVEST ALL CODE INTO CODEMASTER ⚡                          ║
║                                                                                   ║
║                         🚀 OPTIMIZED FOR M2 ULTRA 🚀                              ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝

Scans directories for code files, extracts metadata, indexes into CODEMASTER Vault & Catalog.
"""

import asyncio
import ast
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import aiofiles
    AIOFILES = True
except ImportError:
    AIOFILES = False

try:
    import httpx
    HTTPX = True
except ImportError:
    HTTPX = False

try:
    import orjson
    def json_dumps(obj):
        return orjson.dumps(obj).decode()
    def json_loads(s):
        return orjson.loads(s)
    ORJSON = True
except ImportError:
    def json_dumps(obj):
        return json.dumps(obj)
    def json_loads(s):
        return json.loads(s)
    ORJSON = False

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    UVLOOP = True
except ImportError:
    UVLOOP = False


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class HarvesterConfig:
    """Harvester configuration optimized for M2 Ultra"""
    # Paths to scan
    scan_paths: List[str] = field(default_factory=lambda: [
        "/Users/m2ultra/NOIZYLAB/NOIZYLAB/gabriel",
        "/Users/m2ultra/NOIZYLAB/GABRIEL",
        "/Users/m2ultra/NOIZYLAB/CODEMASTER",
    ])
    
    # File extensions to harvest
    extensions: Set[str] = field(default_factory=lambda: {
        '.py', '.js', '.ts', '.jsx', '.tsx', '.swift', '.rs', '.go',
        '.java', '.kt', '.c', '.cpp', '.h', '.hpp', '.rb', '.php',
        '.sh', '.bash', '.zsh', '.sql', '.yaml', '.yml', '.json',
        '.md', '.html', '.css', '.scss', '.vue', '.svelte'
    })
    
    # CODEMASTER API
    codemaster_url: str = "http://localhost:8000"
    
    # Performance settings (M2 Ultra optimized)
    max_workers: int = 24
    batch_size: int = 100
    max_file_size: int = 1024 * 1024  # 1MB max
    
    # Output
    output_dir: Path = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER/data/harvest")


# ═══════════════════════════════════════════════════════════════════════════════
# CODE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class CodeFile:
    """Represents a harvested code file"""
    path: str
    name: str
    extension: str
    language: str
    size: int
    lines: int
    hash: str
    created: str
    modified: str
    
    # Extracted metadata
    imports: List[str] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)
    functions: List[str] = field(default_factory=list)
    docstring: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    
    # Analysis
    complexity: int = 0
    todos: List[str] = field(default_factory=list)


LANGUAGE_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.jsx': 'javascript-react',
    '.tsx': 'typescript-react',
    '.swift': 'swift',
    '.rs': 'rust',
    '.go': 'go',
    '.java': 'java',
    '.kt': 'kotlin',
    '.c': 'c',
    '.cpp': 'cpp',
    '.h': 'c-header',
    '.hpp': 'cpp-header',
    '.rb': 'ruby',
    '.php': 'php',
    '.sh': 'bash',
    '.bash': 'bash',
    '.zsh': 'zsh',
    '.sql': 'sql',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.json': 'json',
    '.md': 'markdown',
    '.html': 'html',
    '.css': 'css',
    '.scss': 'scss',
    '.vue': 'vue',
    '.svelte': 'svelte',
}


def analyze_python_file(content: str, file_path: str) -> Dict[str, Any]:
    """Deep analysis of Python files using AST"""
    result = {
        'imports': [],
        'classes': [],
        'functions': [],
        'docstring': None,
        'complexity': 0,
        'todos': [],
        'decorators': [],
        'async_functions': [],
    }
    
    try:
        tree = ast.parse(content)
        
        # Module docstring
        if (tree.body and isinstance(tree.body[0], ast.Expr) and 
            isinstance(tree.body[0].value, ast.Constant) and 
            isinstance(tree.body[0].value.value, str)):
            result['docstring'] = tree.body[0].value.value[:500]
        
        for node in ast.walk(tree):
            # Imports
            if isinstance(node, ast.Import):
                for alias in node.names:
                    result['imports'].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    result['imports'].append(node.module)
            
            # Classes
            elif isinstance(node, ast.ClassDef):
                result['classes'].append(node.name)
                result['complexity'] += 2
            
            # Functions
            elif isinstance(node, ast.FunctionDef):
                result['functions'].append(node.name)
                result['complexity'] += 1
            elif isinstance(node, ast.AsyncFunctionDef):
                result['async_functions'].append(node.name)
                result['functions'].append(f"async:{node.name}")
                result['complexity'] += 1
            
            # Complexity indicators
            elif isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
                result['complexity'] += 1
            elif isinstance(node, ast.comprehension):
                result['complexity'] += 1
                
    except SyntaxError:
        pass
    except Exception:
        pass
    
    # Find TODOs and FIXMEs
    todo_pattern = re.compile(r'#\s*(TODO|FIXME|XXX|HACK|NOTE):\s*(.+)', re.IGNORECASE)
    for match in todo_pattern.finditer(content):
        result['todos'].append(f"{match.group(1)}: {match.group(2)[:100]}")
    
    return result


def analyze_file(file_path: Path, content: str) -> CodeFile:
    """Analyze a code file and extract metadata"""
    ext = file_path.suffix.lower()
    language = LANGUAGE_MAP.get(ext, 'unknown')
    
    stat = file_path.stat()
    lines = content.count('\n') + 1
    
    code_file = CodeFile(
        path=str(file_path),
        name=file_path.name,
        extension=ext,
        language=language,
        size=stat.st_size,
        lines=lines,
        hash=hashlib.md5(content.encode()).hexdigest()[:16],
        created=datetime.fromtimestamp(stat.st_ctime).isoformat(),
        modified=datetime.fromtimestamp(stat.st_mtime).isoformat(),
    )
    
    # Python-specific analysis
    if ext == '.py':
        analysis = analyze_python_file(content, str(file_path))
        code_file.imports = analysis['imports'][:50]  # Limit
        code_file.classes = analysis['classes'][:50]
        code_file.functions = analysis['functions'][:100]
        code_file.docstring = analysis['docstring']
        code_file.complexity = analysis['complexity']
        code_file.todos = analysis['todos'][:20]
    
    # Generate tags
    tags = [language]
    if 'test' in file_path.name.lower():
        tags.append('test')
    if 'config' in file_path.name.lower():
        tags.append('config')
    if 'util' in file_path.name.lower() or 'helper' in file_path.name.lower():
        tags.append('utility')
    if code_file.classes:
        tags.append('has-classes')
    if 'async:' in str(code_file.functions):
        tags.append('async')
    if code_file.complexity > 20:
        tags.append('complex')
    
    code_file.tags = tags
    
    return code_file


# ═══════════════════════════════════════════════════════════════════════════════
# HARVESTER ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class CodeHarvester:
    """High-performance code harvester for M2 Ultra"""
    
    def __init__(self, config: HarvesterConfig = None):
        self.config = config or HarvesterConfig()
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.files_found: List[Path] = []
        self.files_harvested: List[CodeFile] = []
        self.errors: List[str] = []
        
        self.stats = {
            'total_files': 0,
            'total_lines': 0,
            'total_size': 0,
            'by_language': {},
            'start_time': None,
            'end_time': None,
        }
    
    def discover_files(self) -> List[Path]:
        """Discover all code files in scan paths"""
        print("\n🔍 Discovering files...")
        files = []
        
        for scan_path in self.config.scan_paths:
            path = Path(scan_path)
            if not path.exists():
                print(f"  ⚠️  Path not found: {scan_path}")
                continue
            
            print(f"  📁 Scanning: {scan_path}")
            
            for file_path in path.rglob('*'):
                if not file_path.is_file():
                    continue
                
                # Skip hidden and cache directories
                if any(part.startswith('.') or part in ('__pycache__', 'node_modules', 'venv', '.git')
                       for part in file_path.parts):
                    continue
                
                # Check extension
                if file_path.suffix.lower() in self.config.extensions:
                    # Check size
                    if file_path.stat().st_size <= self.config.max_file_size:
                        files.append(file_path)
        
        print(f"  ✅ Found {len(files)} files")
        self.files_found = files
        return files
    
    def harvest_file(self, file_path: Path) -> Optional[CodeFile]:
        """Harvest a single file"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            return analyze_file(file_path, content)
        except Exception as e:
            self.errors.append(f"{file_path}: {str(e)}")
            return None
    
    def harvest_all(self) -> List[CodeFile]:
        """Harvest all discovered files using parallel processing"""
        if not self.files_found:
            self.discover_files()
        
        self.stats['start_time'] = datetime.now()
        print(f"\n⚡ Harvesting {len(self.files_found)} files with {self.config.max_workers} workers...")
        
        harvested = []
        
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            results = list(executor.map(self.harvest_file, self.files_found))
        
        for result in results:
            if result:
                harvested.append(result)
                self.stats['total_lines'] += result.lines
                self.stats['total_size'] += result.size
                
                lang = result.language
                if lang not in self.stats['by_language']:
                    self.stats['by_language'][lang] = {'files': 0, 'lines': 0}
                self.stats['by_language'][lang]['files'] += 1
                self.stats['by_language'][lang]['lines'] += result.lines
        
        self.stats['total_files'] = len(harvested)
        self.stats['end_time'] = datetime.now()
        self.files_harvested = harvested
        
        print(f"  ✅ Harvested {len(harvested)} files")
        return harvested
    
    def save_harvest(self) -> Path:
        """Save harvest results to JSON"""
        output_file = self.config.output_dir / f"harvest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = {
            'stats': {
                **self.stats,
                'start_time': self.stats['start_time'].isoformat() if self.stats['start_time'] else None,
                'end_time': self.stats['end_time'].isoformat() if self.stats['end_time'] else None,
                'duration_seconds': (self.stats['end_time'] - self.stats['start_time']).total_seconds() if self.stats['end_time'] else 0,
            },
            'files': [
                {
                    'path': f.path,
                    'name': f.name,
                    'language': f.language,
                    'lines': f.lines,
                    'size': f.size,
                    'hash': f.hash,
                    'classes': f.classes,
                    'functions': f.functions[:30],  # Limit for JSON
                    'imports': f.imports[:20],
                    'tags': f.tags,
                    'complexity': f.complexity,
                    'docstring': f.docstring[:200] if f.docstring else None,
                }
                for f in self.files_harvested
            ],
            'errors': self.errors[:100],
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n💾 Saved to: {output_file}")
        return output_file
    
    async def upload_to_codemaster(self) -> Dict[str, int]:
        """Upload harvested files to CODEMASTER Vault"""
        if not HTTPX:
            print("❌ httpx not installed, cannot upload")
            return {'uploaded': 0, 'failed': 0}
        
        print(f"\n📤 Uploading to CODEMASTER ({self.config.codemaster_url})...")
        
        uploaded = 0
        failed = 0
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Check if CODEMASTER is running
            try:
                resp = await client.get(f"{self.config.codemaster_url}/health")
                if resp.status_code != 200:
                    print("❌ CODEMASTER not responding")
                    return {'uploaded': 0, 'failed': 0}
            except Exception:
                print("❌ Cannot connect to CODEMASTER")
                return {'uploaded': 0, 'failed': 0}
            
            # Upload in batches
            for i, code_file in enumerate(self.files_harvested):
                try:
                    # Create vault entry
                    vault_item = {
                        'name': code_file.name,
                        'content': f"Path: {code_file.path}\nLines: {code_file.lines}\nClasses: {', '.join(code_file.classes[:10])}\nFunctions: {', '.join(code_file.functions[:20])}",
                        'language': code_file.language,
                        'tags': code_file.tags,
                    }
                    
                    resp = await client.post(
                        f"{self.config.codemaster_url}/vault/",
                        json=vault_item
                    )
                    
                    if resp.status_code == 200:
                        uploaded += 1
                    else:
                        failed += 1
                        
                except Exception as e:
                    failed += 1
                
                # Progress
                if (i + 1) % 100 == 0:
                    print(f"  📤 Progress: {i + 1}/{len(self.files_harvested)} ({uploaded} uploaded)")
        
        print(f"  ✅ Uploaded: {uploaded}, Failed: {failed}")
        return {'uploaded': uploaded, 'failed': failed}
    
    def print_report(self):
        """Print harvest report"""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds() if self.stats['end_time'] else 0
        
        print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                          🌾 HARVEST REPORT 🌾                                     ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  📁 Total Files:     {self.stats['total_files']:>10,}                                            ║
║  📝 Total Lines:     {self.stats['total_lines']:>10,}                                            ║
║  💾 Total Size:      {self.stats['total_size'] / 1024 / 1024:>10.2f} MB                                       ║
║  ⏱️  Duration:        {duration:>10.2f} seconds                                     ║
║  ⚡ Speed:           {self.stats['total_files'] / duration if duration else 0:>10.1f} files/sec                                  ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                          📊 BY LANGUAGE                                           ║
╠═══════════════════════════════════════════════════════════════════════════════════╣""")
        
        for lang, data in sorted(self.stats['by_language'].items(), key=lambda x: -x[1]['lines']):
            print(f"║  {lang:15} {data['files']:>6,} files   {data['lines']:>10,} lines                       ║")
        
        print(f"""╠═══════════════════════════════════════════════════════════════════════════════════╣
║  UVLOOP: {'✅' if UVLOOP else '❌':4} | ORJSON: {'✅' if ORJSON else '❌':4} | AIOFILES: {'✅' if AIOFILES else '❌':4} | HTTPX: {'✅' if HTTPX else '❌':4}        ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

async def main():
    print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║   ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███████╗   ║
║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║  ██║██╔══██╗██╔══██╗██║   ██║██╔════╝   ║
║  ██║     ██║   ██║██║  ██║█████╗      ███████║███████║██████╔╝██║   ██║█████╗     ║
║  ██║     ██║   ██║██║  ██║██╔══╝      ██╔══██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝     ║
║  ╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗   ║
║   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝   ║
║                                                                                   ║
║                    ⚡ HARVEST ALL CODE INTO CODEMASTER ⚡                          ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    harvester = CodeHarvester()
    
    # Discover and harvest
    harvester.discover_files()
    harvester.harvest_all()
    
    # Save results
    harvester.save_harvest()
    
    # Print report
    harvester.print_report()
    
    # Upload to CODEMASTER if running
    if '--upload' in sys.argv:
        await harvester.upload_to_codemaster()
    else:
        print("💡 Tip: Run with --upload to send to CODEMASTER Vault")


if __name__ == "__main__":
    asyncio.run(main())
