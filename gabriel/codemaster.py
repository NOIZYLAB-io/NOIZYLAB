#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║  ✨ CODEMASTER v3.0 - ULTIMATE CODE ORGANIZATION SYSTEM ✨                     ║
║                                                                                ║
║  GABRIEL's Neural Core for Code Organization & Intelligence                    ║
║                                                                                ║
║  Commands:                                                                     ║
║    init        - Initialize CODEMASTER folder structure                        ║
║    scan        - Deep scan and fingerprint all code                           ║
║    plan        - Create organization plan (dry-run)                            ║
║    apply       - Execute the plan                                              ║
║    status      - Show organization dashboard                                   ║
║    dedupe      - Find and report duplicate files                              ║
║    harvest     - Collect valuable code from all sources                        ║
║    validate    - Check structure integrity                                     ║
║    rollback    - Undo last operation                                           ║
║    search      - Search across all code                                        ║
║                                                                                ║
║  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // INFINITE ENERGY ⚡                  ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import time
import threading
import signal
from abc import ABC, abstractmethod
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum, auto
from functools import lru_cache
from pathlib import Path
from typing import (
    Any, Callable, Dict, Iterable, Iterator, List, 
    Optional, Set, Tuple, TypeVar, Union
)

# ════════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

VERSION = "3.0.0"
PROGRAM_NAME = "codemaster"
SIGNATURE = "MC96DIGIUNIVERSE AI LIFELUV INFINITE ENERGY ⚡"

# Default root
DEFAULT_ROOT = Path(__file__).parent.resolve()


class Folders:
    """Canonical folder names for CODEMASTER structure."""
    CONTROL_PLANE = "00_CONTROL_PLANE"
    INTAKE = "01_INTAKE"
    DEDUP = "02_DEDUP"
    CORE = "10_CORE"
    AGENTS = "11_AGENTS"
    MCP = "12_MCP"
    PROJECTS = "20_PROJECTS"
    LIBRARIES = "30_LIBRARIES"
    AUTOMATIONS = "40_AUTOMATIONS"
    TEMPLATES = "50_TEMPLATES"
    ARCHIVE = "90_ARCHIVE"
    
    # Subfolders
    MANIFEST = "manifest"
    LOGS = "logs"
    ROLLBACK = "rollback"
    
    INTAKE_UNSORTED = "A_UNSORTED"
    INTAKE_QUARANTINE = "B_QUARANTINE"
    INTAKE_READY = "C_READY"
    
    LOOSE = "_LOOSE"


RESERVED_TOPLEVEL: Set[str] = {
    ".git", ".vscode", ".github", ".idea", ".claude",
    Folders.CONTROL_PLANE, Folders.INTAKE, Folders.DEDUP,
    Folders.CORE, Folders.AGENTS, Folders.MCP,
    Folders.PROJECTS, Folders.LIBRARIES, Folders.AUTOMATIONS,
    Folders.TEMPLATES, Folders.ARCHIVE,
    "node_modules", "__pycache__", ".venv", "venv",
}

IGNORE_DIRS: Set[str] = {
    "node_modules", "__pycache__", ".venv", "venv", "env",
    ".mypy_cache", ".pytest_cache", ".tox", ".nox",
    "dist", "build", "out", "target", "bin", "obj",
    ".next", ".nuxt", ".cache", ".parcel-cache",
    ".gradle", ".maven", ".ivy2",
    ".idea", ".vs", "coverage", ".nyc_output",
    "eggs", ".eggs", "bower_components",
    ".terraform", ".serverless",
}

IGNORE_FILES: Set[str] = {
    ".DS_Store", "Thumbs.db", "desktop.ini",
    ".gitkeep", ".npmignore", ".dockerignore",
}


# ════════════════════════════════════════════════════════════════════════════════
# LANGUAGE DETECTION
# ════════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class Language:
    name: str
    display: str
    extensions: Tuple[str, ...]
    markers: Tuple[str, ...] = ()
    priority: int = 50


LANGUAGES: Tuple[Language, ...] = (
    # High priority - specific markers
    Language("rust", "Rust", (".rs",), ("Cargo.toml",), 90),
    Language("go", "Go", (".go",), ("go.mod",), 90),
    Language("elixir", "Elixir", (".ex", ".exs"), ("mix.exs",), 90),
    Language("swift", "Swift", (".swift",), ("Package.swift",), 85),
    Language("kotlin", "Kotlin", (".kt", ".kts"), ("build.gradle.kts",), 80),
    
    # Medium-high priority
    Language("typescript", "TypeScript", (".ts", ".tsx", ".mts", ".cts"), ("tsconfig.json",), 80),
    Language("python", "Python", (".py", ".pyi", ".pyx"), ("pyproject.toml", "setup.py", "requirements.txt"), 75),
    
    # Medium priority
    Language("java", "Java", (".java",), ("pom.xml", "build.gradle"), 70),
    Language("csharp", "C#", (".cs", ".csx"), (), 70),
    Language("cpp", "C++", (".cpp", ".cc", ".cxx", ".hpp", ".hxx"), ("CMakeLists.txt",), 65),
    Language("c", "C", (".c", ".h"), ("Makefile",), 60),
    
    # Web/scripting
    Language("javascript", "JavaScript", (".js", ".jsx", ".mjs", ".cjs"), ("package.json",), 55),
    Language("vue", "Vue", (".vue",), ("vue.config.js",), 70),
    Language("svelte", "Svelte", (".svelte",), ("svelte.config.js",), 70),
    Language("php", "PHP", (".php",), ("composer.json",), 55),
    Language("ruby", "Ruby", (".rb", ".rake"), ("Gemfile",), 55),
    
    # Shell/scripting
    Language("shell", "Shell", (".sh", ".bash", ".zsh", ".fish"), (), 40),
    Language("powershell", "PowerShell", (".ps1", ".psm1"), (), 40),
    Language("lua", "Lua", (".lua",), (), 45),
    
    # Data/config
    Language("sql", "SQL", (".sql",), (), 30),
    Language("yaml", "YAML", (".yaml", ".yml"), (), 20),
    Language("json", "JSON", (".json",), (), 15),
    Language("markdown", "Markdown", (".md", ".mdx"), (), 10),
    Language("html", "HTML", (".html", ".htm"), (), 25),
    Language("css", "CSS", (".css", ".scss", ".sass", ".less"), (), 25),
)

# Build lookup tables
EXT_TO_LANGUAGE: Dict[str, Language] = {}
for lang in LANGUAGES:
    for ext in lang.extensions:
        if ext not in EXT_TO_LANGUAGE or lang.priority > EXT_TO_LANGUAGE[ext].priority:
            EXT_TO_LANGUAGE[ext] = lang

MARKER_TO_LANGUAGE: Dict[str, Language] = {}
for lang in LANGUAGES:
    for marker in lang.markers:
        MARKER_TO_LANGUAGE[marker] = lang


PROJECT_MARKERS: Tuple[str, ...] = (
    ".git", "package.json", "pyproject.toml", "requirements.txt", "setup.py",
    "Cargo.toml", "go.mod", "pom.xml", "build.gradle", "CMakeLists.txt",
    "composer.json", "Gemfile", "tsconfig.json", "mix.exs",
)


# ════════════════════════════════════════════════════════════════════════════════
# CONSOLE OUTPUT
# ════════════════════════════════════════════════════════════════════════════════

class Style(Enum):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_CYAN = "\033[96m"


class Console:
    """Rich console output without external dependencies."""
    
    _instance: Optional['Console'] = None
    
    def __new__(cls) -> 'Console':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance
    
    def _init(self) -> None:
        self.use_color = sys.stdout.isatty()
        self.verbose = False
        self.quiet = False
        self._spinner_active = False
    
    def _style(self, text: str, *styles: Style) -> str:
        if not self.use_color:
            return text
        prefix = "".join(s.value for s in styles)
        return f"{prefix}{text}{Style.RESET.value}"
    
    def print(self, msg: str = "", **kwargs: Any) -> None:
        if not self.quiet:
            print(msg, **kwargs)
    
    def banner(self) -> None:
        self.print()
        self.print(self._style("╔════════════════════════════════════════════════════════════════════╗", Style.CYAN, Style.BOLD))
        self.print(self._style("║", Style.CYAN, Style.BOLD) + self._style("  ✨ CODEMASTER v3.0 - GABRIEL CODE INTELLIGENCE ✨                 ", Style.BRIGHT_GREEN, Style.BOLD) + self._style("║", Style.CYAN, Style.BOLD))
        self.print(self._style("║", Style.CYAN, Style.BOLD) + self._style("  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // INFINITE ENERGY ⚡      ", Style.WHITE) + self._style("║", Style.CYAN, Style.BOLD))
        self.print(self._style("╚════════════════════════════════════════════════════════════════════╝", Style.CYAN, Style.BOLD))
        self.print()
    
    def header(self, text: str) -> None:
        width = 68
        border = "═" * width
        self.print()
        self.print(self._style(f"╔{border}╗", Style.CYAN, Style.BOLD))
        self.print(self._style(f"║{text.center(width)}║", Style.CYAN, Style.BOLD))
        self.print(self._style(f"╚{border}╝", Style.CYAN, Style.BOLD))
        self.print()
    
    def section(self, text: str) -> None:
        self.print()
        self.print(self._style(f"┌─ {text} ", Style.BLUE, Style.BOLD) + 
                   self._style("─" * (60 - len(text)), Style.DIM))
    
    def success(self, msg: str) -> None:
        self.print(self._style("  ✓ ", Style.GREEN, Style.BOLD) + msg)
    
    def error(self, msg: str) -> None:
        self.print(self._style("  ✗ ", Style.RED, Style.BOLD) + msg)
    
    def warning(self, msg: str) -> None:
        self.print(self._style("  ⚠ ", Style.YELLOW, Style.BOLD) + msg)
    
    def info(self, msg: str) -> None:
        self.print(self._style("  ℹ ", Style.BLUE) + msg)
    
    def debug(self, msg: str) -> None:
        if self.verbose:
            self.print(self._style("  · ", Style.DIM) + self._style(msg, Style.DIM))
    
    def item(self, msg: str, indent: int = 2) -> None:
        self.print(" " * indent + self._style("→ ", Style.CYAN) + msg)
    
    def key_value(self, key: str, value: str, indent: int = 4) -> None:
        self.print(" " * indent + self._style(f"{key}: ", Style.DIM) + str(value))
    
    def table(self, headers: List[str], rows: List[List[str]], indent: int = 2) -> None:
        if not rows:
            return
        
        widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(widths):
                    widths[i] = max(widths[i], len(str(cell)))
        
        prefix = " " * indent
        header_line = " │ ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
        self.print(prefix + self._style(header_line, Style.BOLD))
        self.print(prefix + "─" * (sum(widths) + 3 * (len(headers) - 1)))
        
        for row in rows:
            cells = [str(row[i]).ljust(widths[i]) if i < len(row) else " " * widths[i] 
                     for i in range(len(headers))]
            self.print(prefix + " │ ".join(cells))
    
    def progress_bar(self, current: int, total: int, width: int = 40, 
                     prefix: str = "", suffix: str = "") -> None:
        if total == 0:
            pct = 100
        else:
            pct = int(100 * current / total)
        filled = int(width * current / total) if total > 0 else width
        bar = "█" * filled + "░" * (width - filled)
        line = f"\r  {prefix}[{bar}] {pct:3d}% {suffix}"
        self.print(line, end="", flush=True)
        if current >= total:
            self.print()


console = Console()


# ════════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ════════════════════════════════════════════════════════════════════════════════

class MoveKind(Enum):
    PROJECT = "project"
    LOOSE = "loose"
    CORE = "core"
    AGENT = "agent"
    MCP = "mcp"


@dataclass
class MoveItem:
    src: Path
    dst: Path
    kind: MoveKind
    reason: str
    language: str = "unknown"
    size_bytes: int = 0
    file_count: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "src": str(self.src),
            "dst": str(self.dst),
            "kind": self.kind.value,
            "reason": self.reason,
            "language": self.language,
            "size_bytes": self.size_bytes,
            "file_count": self.file_count,
        }
    
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'MoveItem':
        return cls(
            src=Path(d["src"]),
            dst=Path(d["dst"]),
            kind=MoveKind(d["kind"]),
            reason=d["reason"],
            language=d.get("language", "unknown"),
            size_bytes=d.get("size_bytes", 0),
            file_count=d.get("file_count", 0),
        )


@dataclass
class FileFingerprint:
    path: Path
    sha256: str
    size: int
    mtime: float
    language: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": str(self.path),
            "sha256": self.sha256,
            "size": self.size,
            "mtime": self.mtime,
            "language": self.language,
        }


@dataclass
class MovePlan:
    version: str
    created_at: datetime
    root: Path
    moves: List[MoveItem]
    stats: Dict[str, int] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "root": str(self.root),
            "moves": [m.to_dict() for m in self.moves],
            "stats": self.stats,
        }
    
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'MovePlan':
        return cls(
            version=d["version"],
            created_at=datetime.fromisoformat(d["created_at"]),
            root=Path(d["root"]),
            moves=[MoveItem.from_dict(m) for m in d["moves"]],
            stats=d.get("stats", {}),
        )
    
    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
    
    @classmethod
    def load(cls, path: Path) -> 'MovePlan':
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls.from_dict(data)


@dataclass
class RollbackInfo:
    id: str
    created_at: datetime
    moves_applied: List[Tuple[str, str]]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "moves_applied": self.moves_applied,
        }
    
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'RollbackInfo':
        return cls(
            id=d["id"],
            created_at=datetime.fromisoformat(d["created_at"]),
            moves_applied=[tuple(m) for m in d["moves_applied"]],
        )


# ════════════════════════════════════════════════════════════════════════════════
# PATH UTILITIES
# ════════════════════════════════════════════════════════════════════════════════

class PathManager:
    def __init__(self, root: Path):
        self.root = root.resolve()
    
    @property
    def control_plane(self) -> Path:
        return self.root / Folders.CONTROL_PLANE
    
    @property
    def manifest_dir(self) -> Path:
        return self.control_plane / Folders.MANIFEST
    
    @property
    def logs_dir(self) -> Path:
        return self.control_plane / Folders.LOGS
    
    @property
    def rollback_dir(self) -> Path:
        return self.control_plane / Folders.ROLLBACK
    
    @property
    def intake(self) -> Path:
        return self.root / Folders.INTAKE
    
    @property
    def dedup(self) -> Path:
        return self.root / Folders.DEDUP
    
    @property
    def core(self) -> Path:
        return self.root / Folders.CORE
    
    @property
    def agents(self) -> Path:
        return self.root / Folders.AGENTS
    
    @property
    def mcp(self) -> Path:
        return self.root / Folders.MCP
    
    @property
    def projects(self) -> Path:
        return self.root / Folders.PROJECTS
    
    @property
    def libraries(self) -> Path:
        return self.root / Folders.LIBRARIES
    
    @property
    def automations(self) -> Path:
        return self.root / Folders.AUTOMATIONS
    
    @property
    def templates(self) -> Path:
        return self.root / Folders.TEMPLATES
    
    @property
    def archive(self) -> Path:
        return self.root / Folders.ARCHIVE
    
    @property
    def loose_code(self) -> Path:
        return self.libraries / Folders.LOOSE
    
    def all_managed_dirs(self) -> List[Path]:
        return [
            self.control_plane,
            self.manifest_dir,
            self.logs_dir,
            self.rollback_dir,
            self.intake,
            self.dedup,
            self.core,
            self.agents,
            self.mcp,
            self.projects,
            self.libraries,
            self.automations,
            self.templates,
            self.archive,
        ]
    
    def move_plan_path(self) -> Path:
        return self.manifest_dir / "move_plan.json"
    
    def fingerprints_path(self) -> Path:
        return self.manifest_dir / "fingerprints.json"
    
    def latest_rollback_path(self) -> Path:
        return self.rollback_dir / "latest.json"


def is_subpath(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def sanitize_name(name: str) -> str:
    name = name.strip().replace(" ", "-")
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)
    name = re.sub(r"-{2,}", "-", name).strip("-")
    return name or "UNNAMED"


def unique_path(base_dir: Path, name: str, is_file: bool = False) -> Path:
    name = sanitize_name(name)
    
    if is_file:
        stem = Path(name).stem
        suffix = Path(name).suffix
        candidate = base_dir / name
        if not candidate.exists():
            return candidate
        for i in range(2, 10000):
            candidate = base_dir / f"{stem}-{i}{suffix}"
            if not candidate.exists():
                return candidate
    else:
        candidate = base_dir / name
        if not candidate.exists():
            return candidate
        for i in range(2, 10000):
            candidate = base_dir / f"{name}-{i}"
            if not candidate.exists():
                return candidate
    
    raise RuntimeError(f"Cannot find unique path for {name}")


def should_ignore_dir(path: Path) -> bool:
    return path.name in IGNORE_DIRS or path.name.startswith(".")


def should_ignore_file(path: Path) -> bool:
    return path.name in IGNORE_FILES or path.name.startswith(".")


# ════════════════════════════════════════════════════════════════════════════════
# FILE UTILITIES
# ════════════════════════════════════════════════════════════════════════════════

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def get_dir_stats(path: Path) -> Tuple[int, int]:
    file_count = 0
    total_size = 0
    
    for item in path.rglob("*"):
        if item.is_file() and not should_ignore_file(item):
            if any(p.name in IGNORE_DIRS for p in item.parents):
                continue
            file_count += 1
            try:
                total_size += item.stat().st_size
            except OSError:
                pass
    
    return file_count, total_size


def format_size(size_bytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


# ════════════════════════════════════════════════════════════════════════════════
# PROJECT DETECTION
# ════════════════════════════════════════════════════════════════════════════════

class ProjectDetector:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def find_markers(self, directory: Path) -> List[str]:
        found = []
        for marker in PROJECT_MARKERS:
            if (directory / marker).exists():
                found.append(marker)
        return found
    
    def detect_language(self, project_root: Path) -> str:
        for marker in PROJECT_MARKERS:
            if (project_root / marker).exists() and marker in MARKER_TO_LANGUAGE:
                return MARKER_TO_LANGUAGE[marker].name
        
        ext_counts: Dict[str, int] = defaultdict(int)
        for path in project_root.rglob("*"):
            if path.is_file() and not should_ignore_file(path):
                if any(should_ignore_dir(p) for p in path.parents):
                    continue
                ext = path.suffix.lower()
                if ext in EXT_TO_LANGUAGE:
                    lang = EXT_TO_LANGUAGE[ext]
                    ext_counts[lang.name] += lang.priority
        
        if ext_counts:
            return max(ext_counts.items(), key=lambda x: x[1])[0]
        
        return "unknown"
    
    def is_gabriel_file(self, path: Path) -> bool:
        """Check if file is a GABRIEL core file."""
        name = path.name.lower()
        return "gabriel" in name or "gorunfree" in name or "mc96" in name
    
    def is_mcp_file(self, path: Path) -> bool:
        """Check if file is an MCP server."""
        name = path.name.lower()
        content_check = False
        if path.suffix == ".py":
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")[:1000]
                content_check = "mcp" in content.lower() and ("server" in content.lower() or "Server" in content)
            except:
                pass
        return "mcp" in name or content_check
    
    def is_agent_file(self, path: Path) -> bool:
        """Check if file is an AI agent."""
        name = path.name.lower()
        return "agent" in name or "brain" in name


# ════════════════════════════════════════════════════════════════════════════════
# HARVESTER - COLLECT VALUABLE CODE
# ════════════════════════════════════════════════════════════════════════════════

class CodeHarvester:
    """Harvest valuable code from across the repository."""
    
    def __init__(self, paths: PathManager):
        self.paths = paths
        self.detector = ProjectDetector(paths)
    
    def harvest(self, dry_run: bool = True) -> List[MoveItem]:
        """Find and collect all valuable code."""
        console.section("Harvesting Valuable Code")
        
        moves: List[MoveItem] = []
        
        # Scan all directories
        for item in self.paths.root.rglob("*"):
            if not item.is_file():
                continue
            if should_ignore_file(item):
                continue
            if any(should_ignore_dir(p) for p in item.parents):
                continue
            
            # Skip already organized
            if any(is_subpath(item, d) for d in [
                self.paths.core, self.paths.agents, self.paths.mcp,
                self.paths.projects, self.paths.libraries
            ]):
                continue
            
            ext = item.suffix.lower()
            if ext not in EXT_TO_LANGUAGE:
                continue
            
            # Categorize the file
            if self.detector.is_gabriel_file(item):
                dst = unique_path(self.paths.core / "gabriel", item.name, is_file=True)
                moves.append(MoveItem(
                    src=item, dst=dst,
                    kind=MoveKind.CORE,
                    reason="GABRIEL core file",
                    language=EXT_TO_LANGUAGE.get(ext, Language("unknown", "Unknown", ())).name,
                ))
            elif self.detector.is_mcp_file(item):
                dst = unique_path(self.paths.mcp / "servers", item.name, is_file=True)
                moves.append(MoveItem(
                    src=item, dst=dst,
                    kind=MoveKind.MCP,
                    reason="MCP server",
                    language="python",
                ))
            elif self.detector.is_agent_file(item):
                dst = unique_path(self.paths.agents, item.name, is_file=True)
                moves.append(MoveItem(
                    src=item, dst=dst,
                    kind=MoveKind.AGENT,
                    reason="AI agent file",
                    language=EXT_TO_LANGUAGE.get(ext, Language("unknown", "Unknown", ())).name,
                ))
        
        console.success(f"Found {len(moves)} files to harvest")
        
        # Show summary
        by_kind = defaultdict(int)
        for m in moves:
            by_kind[m.kind.value] += 1
        
        for kind, count in by_kind.items():
            console.item(f"{kind}: {count} files")
        
        return moves


# ════════════════════════════════════════════════════════════════════════════════
# INITIALIZER
# ════════════════════════════════════════════════════════════════════════════════

class Initializer:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def initialize(self) -> None:
        console.section("Initializing CODEMASTER Structure")
        
        for path in self.paths.all_managed_dirs():
            path.mkdir(parents=True, exist_ok=True)
            console.debug(f"Created: {path.relative_to(self.paths.root)}")
        
        # Create special subdirectories
        (self.paths.core / "gabriel").mkdir(parents=True, exist_ok=True)
        (self.paths.mcp / "servers").mkdir(parents=True, exist_ok=True)
        (self.paths.intake / Folders.INTAKE_UNSORTED).mkdir(parents=True, exist_ok=True)
        (self.paths.intake / Folders.INTAKE_QUARANTINE).mkdir(parents=True, exist_ok=True)
        (self.paths.intake / Folders.INTAKE_READY).mkdir(parents=True, exist_ok=True)
        
        self._create_readme()
        console.success("Structure initialized!")
    
    def _create_readme(self) -> None:
        readme_path = self.paths.control_plane / "README.md"
        if readme_path.exists():
            return
        
        content = f"""# CODEMASTER Control Plane

> GABRIEL Code Intelligence System v{VERSION}
> {SIGNATURE}

## Structure

```
{Folders.CONTROL_PLANE}/   - Manifests, logs, policies
{Folders.INTAKE}/          - Incoming files staging
{Folders.DEDUP}/           - Duplicate detection
{Folders.CORE}/            - GABRIEL core systems
{Folders.AGENTS}/          - AI agents
{Folders.MCP}/             - MCP servers
{Folders.PROJECTS}/        - Organized projects
{Folders.LIBRARIES}/       - Libraries & loose code
{Folders.AUTOMATIONS}/     - Scripts & automation
{Folders.TEMPLATES}/       - Project templates
{Folders.ARCHIVE}/         - Archived items
```

## Commands

```bash
python codemaster.py init      # Initialize structure
python codemaster.py scan      # Scan and fingerprint
python codemaster.py harvest   # Collect valuable code
python codemaster.py plan      # Create move plan
python codemaster.py apply     # Execute plan
python codemaster.py status    # Show dashboard
python codemaster.py dedupe    # Find duplicates
python codemaster.py search    # Search code
```

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        readme_path.write_text(content, encoding="utf-8")


# ════════════════════════════════════════════════════════════════════════════════
# STATUS REPORTER
# ════════════════════════════════════════════════════════════════════════════════

class StatusReporter:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def report(self) -> Dict[str, Any]:
        console.banner()
        
        sections = [
            ("Core", self.paths.core),
            ("Agents", self.paths.agents),
            ("MCP", self.paths.mcp),
            ("Projects", self.paths.projects),
            ("Libraries", self.paths.libraries),
            ("Automations", self.paths.automations),
            ("Templates", self.paths.templates),
            ("Archive", self.paths.archive),
            ("Intake", self.paths.intake),
        ]
        
        rows = []
        for name, path in sections:
            if path.exists():
                file_count, size = get_dir_stats(path)
                subdirs = len([d for d in path.iterdir() if d.is_dir()])
                rows.append([name, str(subdirs), str(file_count), format_size(size)])
            else:
                rows.append([name, "-", "-", "-"])
        
        console.table(["Section", "Units", "Files", "Size"], rows)
        
        # Check for pending plan
        plan_path = self.paths.move_plan_path()
        if plan_path.exists():
            plan = MovePlan.load(plan_path)
            console.section("Pending Plan")
            console.info(f"Created: {plan.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            console.info(f"Moves: {len(plan.moves)}")
        
        return {}


# ════════════════════════════════════════════════════════════════════════════════
# FINGERPRINT & DEDUPE
# ════════════════════════════════════════════════════════════════════════════════

class FingerprintScanner:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def scan(self) -> List[FileFingerprint]:
        console.section("Scanning Files for Fingerprints")
        
        files_to_scan: List[Path] = []
        
        for path in self.paths.root.rglob("*"):
            if path.is_file() and not should_ignore_file(path):
                if not any(should_ignore_dir(p) for p in path.parents):
                    if path.suffix.lower() in EXT_TO_LANGUAGE:
                        files_to_scan.append(path)
        
        console.info(f"Found {len(files_to_scan)} code files to scan")
        
        fingerprints: List[FileFingerprint] = []
        
        for i, path in enumerate(files_to_scan):
            if i % 500 == 0:
                console.progress_bar(i, len(files_to_scan), prefix="Scanning: ")
            
            try:
                stat = path.stat()
                ext = path.suffix.lower()
                lang = EXT_TO_LANGUAGE.get(ext, Language("unknown", "Unknown", ())).name
                
                fingerprints.append(FileFingerprint(
                    path=path.relative_to(self.paths.root),
                    sha256=sha256_file(path),
                    size=stat.st_size,
                    mtime=stat.st_mtime,
                    language=lang,
                ))
            except Exception as e:
                console.debug(f"Error scanning {path}: {e}")
        
        console.progress_bar(len(files_to_scan), len(files_to_scan), prefix="Scanning: ")
        
        # Save fingerprints
        self._save_fingerprints(fingerprints)
        console.success(f"Generated {len(fingerprints)} fingerprints")
        
        return fingerprints
    
    def _save_fingerprints(self, fingerprints: List[FileFingerprint]) -> None:
        self.paths.manifest_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.fingerprints_path()
        data = {
            "generated_at": datetime.now().isoformat(),
            "count": len(fingerprints),
            "fingerprints": [fp.to_dict() for fp in fingerprints],
        }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")


class DuplicateDetector:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def find_duplicates(self) -> Dict[str, List[Path]]:
        console.section("Detecting Duplicates")
        
        fp_path = self.paths.fingerprints_path()
        if not fp_path.exists():
            console.warning("No fingerprints found. Run 'scan' first.")
            return {}
        
        data = json.loads(fp_path.read_text(encoding="utf-8"))
        
        hash_groups: Dict[str, List[Path]] = defaultdict(list)
        for fp in data["fingerprints"]:
            hash_groups[fp["sha256"]].append(Path(fp["path"]))
        
        duplicates = {k: v for k, v in hash_groups.items() if len(v) > 1}
        
        console.success(f"Found {len(duplicates)} duplicate groups")
        
        if duplicates:
            console.section("Duplicate Report (Top 10)")
            for i, (sha, paths) in enumerate(list(duplicates.items())[:10]):
                console.item(f"{sha[:12]}... ({len(paths)} copies)")
                for p in paths[:3]:
                    console.key_value("", str(p), indent=6)
        
        return duplicates


# ════════════════════════════════════════════════════════════════════════════════
# SEARCH
# ════════════════════════════════════════════════════════════════════════════════

class CodeSearcher:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def search(self, query: str, max_results: int = 50) -> List[Dict[str, Any]]:
        console.section(f"Searching for: {query}")
        
        results = []
        query_lower = query.lower()
        
        for path in self.paths.root.rglob("*"):
            if not path.is_file():
                continue
            if should_ignore_file(path):
                continue
            if any(should_ignore_dir(p) for p in path.parents):
                continue
            
            ext = path.suffix.lower()
            if ext not in EXT_TO_LANGUAGE:
                continue
            
            # Check filename
            if query_lower in path.name.lower():
                results.append({
                    "path": str(path.relative_to(self.paths.root)),
                    "match_type": "filename",
                    "language": EXT_TO_LANGUAGE.get(ext, Language("unknown", "Unknown", ())).name,
                })
                continue
            
            # Check content (first 10KB)
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")[:10000]
                if query_lower in content.lower():
                    results.append({
                        "path": str(path.relative_to(self.paths.root)),
                        "match_type": "content",
                        "language": EXT_TO_LANGUAGE.get(ext, Language("unknown", "Unknown", ())).name,
                    })
            except:
                pass
            
            if len(results) >= max_results:
                break
        
        console.success(f"Found {len(results)} matches")
        
        for r in results[:20]:
            console.item(f"[{r['match_type']}] {r['path']}")
        
        if len(results) > 20:
            console.info(f"... and {len(results) - 20} more")
        
        return results


# ════════════════════════════════════════════════════════════════════════════════
# MOVE EXECUTOR
# ════════════════════════════════════════════════════════════════════════════════

class MoveExecutor:
    def __init__(self, paths: PathManager):
        self.paths = paths
    
    def apply(self, moves: List[MoveItem], dry_run: bool = False) -> RollbackInfo:
        rollback_id = datetime.now().strftime("%Y%m%d-%H%M%S")
        applied_moves: List[Tuple[str, str]] = []
        
        console.section("Applying Moves")
        console.info(f"Total moves: {len(moves)}")
        
        if dry_run:
            console.warning("DRY RUN - No files will be moved")
        
        for i, move in enumerate(moves):
            console.progress_bar(i, len(moves), prefix="Progress: ")
            
            if not move.src.exists():
                console.warning(f"Source missing: {move.src}")
                continue
            
            move.dst.parent.mkdir(parents=True, exist_ok=True)
            
            dst = move.dst
            if dst.exists():
                dst = unique_path(dst.parent, dst.name, is_file=move.src.is_file())
            
            if not dry_run:
                try:
                    shutil.move(str(move.src), str(dst))
                    applied_moves.append((str(move.src), str(dst)))
                except Exception as e:
                    console.error(f"Failed to move {move.src}: {e}")
            else:
                console.debug(f"Would move: {move.src} -> {dst}")
                applied_moves.append((str(move.src), str(dst)))
        
        console.progress_bar(len(moves), len(moves), prefix="Progress: ")
        
        rollback_info = RollbackInfo(
            id=rollback_id,
            created_at=datetime.now(),
            moves_applied=applied_moves,
        )
        
        if not dry_run and applied_moves:
            self._save_rollback(rollback_info)
            console.success(f"Applied {len(applied_moves)} moves")
        
        return rollback_info
    
    def rollback(self) -> int:
        rollback_path = self.paths.latest_rollback_path()
        if not rollback_path.exists():
            console.error("No rollback information found")
            return 0
        
        data = json.loads(rollback_path.read_text(encoding="utf-8"))
        info = RollbackInfo.from_dict(data)
        
        console.section("Rolling Back Changes")
        
        undone = 0
        for dst, src in reversed(info.moves_applied):
            src_path = Path(src)
            dst_path = Path(dst)
            
            if not src_path.exists():
                continue
            
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            
            try:
                shutil.move(str(src_path), str(dst_path))
                undone += 1
            except Exception as e:
                console.error(f"Failed to restore {dst}: {e}")
        
        console.success(f"Rolled back {undone} moves")
        return undone
    
    def _save_rollback(self, info: RollbackInfo) -> None:
        self.paths.rollback_dir.mkdir(parents=True, exist_ok=True)
        path = self.paths.latest_rollback_path()
        path.write_text(json.dumps(info.to_dict(), indent=2), encoding="utf-8")


# ════════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════════

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description="CODEMASTER - GABRIEL Code Intelligence System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s init                    Initialize structure
  %(prog)s scan                    Scan and fingerprint all code
  %(prog)s harvest                 Find and collect valuable code
  %(prog)s harvest --apply         Collect and move valuable code
  %(prog)s status                  Show organization dashboard
  %(prog)s search "gabriel"        Search for code
  %(prog)s dedupe                  Find duplicate files
  %(prog)s rollback                Undo last operation

{SIGNATURE}
        """
    )
    
    parser.add_argument("--version", "-V", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--root", "-r", type=Path, default=DEFAULT_ROOT, help="Root directory")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet output")
    parser.add_argument("--no-color", action="store_true", help="Disable colors")
    
    subparsers = parser.add_subparsers(dest="command", help="Command")
    
    # Commands
    subparsers.add_parser("init", help="Initialize folder structure")
    subparsers.add_parser("scan", help="Scan and fingerprint code")
    subparsers.add_parser("status", help="Show status dashboard")
    subparsers.add_parser("dedupe", help="Find duplicate files")
    subparsers.add_parser("rollback", help="Undo last operation")
    
    harvest_parser = subparsers.add_parser("harvest", help="Harvest valuable code")
    harvest_parser.add_argument("--apply", action="store_true", help="Actually move files")
    
    search_parser = subparsers.add_parser("search", help="Search code")
    search_parser.add_argument("query", help="Search query")
    
    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()
    
    if args.no_color:
        console.use_color = False
    if args.verbose:
        console.verbose = True
    if args.quiet:
        console.quiet = True
    
    if not args.command:
        console.banner()
        parser.print_help()
        return 0
    
    root = args.root.resolve()
    paths = PathManager(root)
    
    try:
        if args.command == "init":
            console.banner()
            Initializer(paths).initialize()
            return 0
        
        elif args.command == "scan":
            console.banner()
            FingerprintScanner(paths).scan()
            return 0
        
        elif args.command == "status":
            StatusReporter(paths).report()
            return 0
        
        elif args.command == "dedupe":
            console.banner()
            DuplicateDetector(paths).find_duplicates()
            return 0
        
        elif args.command == "harvest":
            console.banner()
            harvester = CodeHarvester(paths)
            moves = harvester.harvest(dry_run=not args.apply)
            
            if args.apply and moves:
                executor = MoveExecutor(paths)
                executor.apply(moves, dry_run=False)
            elif moves:
                console.info("Run with --apply to move files")
            return 0
        
        elif args.command == "search":
            console.banner()
            CodeSearcher(paths).search(args.query)
            return 0
        
        elif args.command == "rollback":
            console.banner()
            MoveExecutor(paths).rollback()
            return 0
        
        else:
            parser.print_help()
            return 1
    
    except KeyboardInterrupt:
        console.print()
        console.warning("Interrupted")
        return 130
    
    except Exception as e:
        console.error(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
