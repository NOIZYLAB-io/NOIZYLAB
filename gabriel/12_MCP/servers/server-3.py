#!/usr/bin/env python3
"""
🧠 GABRIEL MCP SERVER
=====================
Model Context Protocol server for GABRIEL AI system.

Features:
- Codebase intelligence & search
- Voice synthesis control
- System monitoring
- Task orchestration
- Memory management
"""

import asyncio
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# MCP imports
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    import mcp.types as types
except ImportError:
    print("Installing MCP SDK...", file=sys.stderr)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mcp"])
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    import mcp.types as types

# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_GABRIEL_ROOT = Path("/Users/m2ultra/NOIZYLAB/GABRIEL")

GABRIEL_ROOT = Path(os.environ.get("GABRIEL_ROOT", DEFAULT_GABRIEL_ROOT)).expanduser().resolve()
NOIZYLAB_ROOT = Path(os.environ.get("NOIZYLAB_ROOT", GABRIEL_ROOT.parent)).expanduser().resolve()
DATA_DIR = Path(os.environ.get("GABRIEL_DATA_DIR", GABRIEL_ROOT / "memcell_data")).expanduser().resolve()
LOGS_DIR = Path(os.environ.get("GABRIEL_LOGS_DIR", GABRIEL_ROOT / "logs")).expanduser().resolve()

ALLOWED_ROOTS = [GABRIEL_ROOT, NOIZYLAB_ROOT]

MAX_LOG_LINES = 200
MAX_FILE_PREVIEW_BYTES = 512 * 1024  # 512KB to keep responses snappy
MAX_WRITE_BYTES = 2 * 1024 * 1024    # 2MB safeguard for writes
MAX_SEARCH_RESULTS = 50
MAX_LISTING = 200
MAX_SEARCH_TRAVERSAL = 20000         # cap filesystem walks
SEARCH_TIMEOUT_SECONDS = 20

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Memory files
BRAIN_FILE = DATA_DIR / "gabriel_brain.json"  # Deep knowledge index
BRAIN_QUICK_FILE = DATA_DIR / "gabriel_brain_quick.json"
PROMPTS_INDEX_FILE = DATA_DIR / "prompts_index.json"
FUNCTIONS_INDEX_FILE = DATA_DIR / "functions_index.json"
MEMORY_FILE = DATA_DIR / "memory.json"
TASKS_FILE = DATA_DIR / "tasks.json"

# =============================================================================
# SERVER INITIALIZATION
# =============================================================================

app = Server("gabriel-mcp")

def log(msg: str):
    """Log with timestamp."""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", file=sys.stderr)

def load_json(path: Path, default: Any = None) -> Any:
    """Safe JSON loader."""
    try:
        if path.exists():
            return json.loads(path.read_text())
    except Exception as e:
        log(f"Error loading {path}: {e}")
    return default if default is not None else {}

def save_json(path: Path, data: Any):
    """Safe JSON saver."""
    path.write_text(json.dumps(data, indent=2, default=str))


def _resolve_under_roots(path_str: str) -> Path:
    """Resolve a path and ensure it stays within allowed roots."""
    if not path_str:
        raise ValueError("Path is required")

    candidate = Path(path_str).expanduser().resolve()
    for root in [*ALLOWED_ROOTS, DATA_DIR, LOGS_DIR]:
        try:
            candidate.relative_to(root)
            return candidate
        except ValueError:
            continue
    raise ValueError(f"Path not allowed: {path_str}")


def _read_text_with_limit(path: Path, limit_bytes: int = MAX_FILE_PREVIEW_BYTES) -> str:
    """Read text from a file with a size cap to avoid huge responses."""
    size = path.stat().st_size
    with open(path, "rb") as f:
        data = f.read(limit_bytes)

    text = data.decode("utf-8", errors="replace")
    if size > limit_bytes:
        remainder = size - limit_bytes
        return f"{text}\n\n...[truncated {remainder:,} bytes]"
    return text


def _tail_file(path: Path, max_lines: int = MAX_LOG_LINES) -> str:
    """Return the tail of a file without loading it entirely."""
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        end = f.tell()
        f.seek(max(0, end - MAX_FILE_PREVIEW_BYTES), os.SEEK_SET)
        data = f.read()

    text = data.decode("utf-8", errors="replace")
    lines = text.splitlines()[-max_lines:]
    return "\n".join(lines)

# =============================================================================
# RESOURCES
# =============================================================================

@app.list_resources()
async def list_resources() -> List[types.Resource]:
    """List available GABRIEL resources."""
    return [
        types.Resource(
            uri="gabriel://brain",
            name="GABRIEL Brain State",
            description="Current knowledge and context",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://memory",
            name="Conversation Memory",
            description="Recent interactions and context",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://tasks",
            name="Task Queue",
            description="Pending and completed tasks",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://status",
            name="System Status",
            description="GABRIEL system health and metrics",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://logs",
            name="Server Logs",
            description="Recent GABRIEL activity logs",
            mimeType="text/plain"
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    """Read a GABRIEL resource."""
    
    if uri == "gabriel://brain":
        return json.dumps(load_json(BRAIN_FILE, {"knowledge": [], "context": {}}), indent=2)
    
    if uri == "gabriel://memory":
        return json.dumps(load_json(MEMORY_FILE, {"conversations": [], "insights": []}), indent=2)
    
    if uri == "gabriel://tasks":
        return json.dumps(load_json(TASKS_FILE, {"pending": [], "completed": []}), indent=2)
    
    if uri == "gabriel://status":
        status = {
            "online": True,
            "timestamp": datetime.now().isoformat(),
            "version": "2.0.0",
            "components": {
                "mcp_server": "running",
                "voice_engine": check_process("gabriel_voice"),
                "file_watcher": check_process("file_watcher")
            }
        }
        return json.dumps(status, indent=2)
    
    if uri == "gabriel://logs":
        log_file = LOGS_DIR / "gabriel.log"
        if log_file.exists():
            return _tail_file(log_file, max_lines=MAX_LOG_LINES)
        return "No logs available."
    
    raise ValueError(f"Unknown resource: {uri}")

def check_process(name: str) -> str:
    """Check if a process is running."""
    try:
        result = subprocess.run(["pgrep", "-f", name], capture_output=True, text=True)
        return "running" if result.returncode == 0 else "stopped"
    except:
        return "unknown"

# =============================================================================
# TOOLS
# =============================================================================

@app.list_tools()
async def list_tools() -> List[types.Tool]:
    """List all GABRIEL tools."""
    return [
        # --- CODEBASE TOOLS ---
        types.Tool(
            name="search_code",
            description="Search codebase for files or content matching a pattern",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search pattern (filename or content)"},
                    "path": {"type": "string", "description": "Directory to search (default: NOIZYLAB)"},
                    "type": {"type": "string", "enum": ["filename", "content", "both"], "default": "both"}
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="read_file",
            description="Read contents of a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path"},
                    "lines": {"type": "integer", "description": "Max lines to return", "default": 500}
                },
                "required": ["path"]
            }
        ),
        types.Tool(
            name="write_file",
            description="Write content to a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path"},
                    "content": {"type": "string", "description": "Content to write"},
                    "append": {"type": "boolean", "description": "Append instead of overwrite", "default": False}
                },
                "required": ["path", "content"]
            }
        ),
        types.Tool(
            name="list_files",
            description="List files in a directory",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Directory path"},
                    "pattern": {"type": "string", "description": "Glob pattern", "default": "*"},
                    "recursive": {"type": "boolean", "default": False}
                },
                "required": ["path"]
            }
        ),
        
        # --- VOICE TOOLS ---
        types.Tool(
            name="speak",
            description="Generate speech using GABRIEL voice engine",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to speak"},
                    "voice": {"type": "string", "description": "Voice preset", "default": "gabriel"},
                    "save_path": {"type": "string", "description": "Optional: save to file instead of playing"}
                },
                "required": ["text"]
            }
        ),
        
        # --- MEMORY TOOLS ---
        types.Tool(
            name="remember",
            description="Store information in GABRIEL memory",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Memory key/topic"},
                    "value": {"type": "string", "description": "Information to remember"},
                    "tags": {"type": "array", "items": {"type": "string"}, "description": "Tags for categorization"}
                },
                "required": ["key", "value"]
            }
        ),
        types.Tool(
            name="recall",
            description="Retrieve information from GABRIEL memory",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query for memory"},
                    "limit": {"type": "integer", "description": "Max results", "default": 10}
                },
                "required": ["query"]
            }
        ),
        
        # --- TASK TOOLS ---
        types.Tool(
            name="add_task",
            description="Add a task to GABRIEL's queue",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Task title"},
                    "description": {"type": "string", "description": "Task details"},
                    "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"], "default": "medium"},
                    "due": {"type": "string", "description": "Due date (ISO format)"}
                },
                "required": ["title"]
            }
        ),
        types.Tool(
            name="complete_task",
            description="Mark a task as completed",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "string", "description": "Task ID to complete"}
                },
                "required": ["task_id"]
            }
        ),
        types.Tool(
            name="list_tasks",
            description="List pending tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "status": {"type": "string", "enum": ["pending", "completed", "all"], "default": "pending"}
                }
            }
        ),
        
        # --- SYSTEM TOOLS ---
        types.Tool(
            name="run_command",
            description="Execute a shell command (safe commands only)",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Command to run"},
                    "cwd": {"type": "string", "description": "Working directory"},
                    "timeout": {"type": "integer", "description": "Timeout in seconds", "default": 30}
                },
                "required": ["command"]
            }
        ),
        types.Tool(
            name="system_info",
            description="Get system information (CPU, memory, disk)",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        
        # --- PROJECT TOOLS ---
        types.Tool(
            name="scan_project",
            description="Scan a project directory and return structure + stats",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Project root path"},
                    "depth": {"type": "integer", "description": "Max depth to scan", "default": 3}
                },
                "required": ["path"]
            }
        ),
        types.Tool(
            name="git_status",
            description="Get git status for a repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Repository path", "default": str(NOIZYLAB_ROOT)}
                }
            }
        ),
        
        # --- DEEP KNOWLEDGE TOOLS ---
        types.Tool(
            name="knowledge_stats",
            description="Get statistics about GABRIEL's indexed knowledge (29K+ files, 8.5M lines)",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="search_knowledge",
            description="Search GABRIEL's deep knowledge index for prompts, functions, code, docs",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term"},
                    "type": {"type": "string", "enum": ["all", "prompts", "functions", "classes", "knowledge", "files"], "default": "all"},
                    "limit": {"type": "integer", "description": "Max results", "default": 20}
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="get_prompts",
            description="Get indexed prompts and agent definitions (98 prompts indexed)",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Filter prompts by name/content"},
                    "limit": {"type": "integer", "default": 20}
                }
            }
        ),
        types.Tool(
            name="get_functions",
            description="Search 30K+ indexed functions across all code",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Function name to search"},
                    "file_pattern": {"type": "string", "description": "Filter by file path pattern"},
                    "limit": {"type": "integer", "default": 50}
                },
                "required": ["name"]
            }
        ),
        types.Tool(
            name="get_knowledge_base",
            description="Search 1200+ knowledge base entries (markdown docs)",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Topic to search"},
                    "limit": {"type": "integer", "default": 20}
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="get_imports",
            description="Get list of 3300+ unique imports/dependencies used across codebase",
            inputSchema={
                "type": "object",
                "properties": {
                    "filter": {"type": "string", "description": "Filter import names"}
                }
            }
        ),
        types.Tool(
            name="get_todos",
            description="Get 1700+ TODOs found across the codebase",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {"type": "integer", "default": 50}
                }
            }
        ),
        types.Tool(
            name="explore_category",
            description="Explore files by category (voice, ai_ml, prompts, api, database, cloud, network, automation, ui, config, docs)",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {"type": "string", "enum": ["voice", "ai_ml", "prompts", "api", "database", "cloud", "network", "automation", "ui", "config", "docs"]},
                    "limit": {"type": "integer", "default": 30}
                },
                "required": ["category"]
            }
        ),
        types.Tool(
            name="reindex_knowledge",
            description="Re-run the deep knowledge indexer to update GABRIEL's brain",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

# =============================================================================
# TOOL IMPLEMENTATIONS
# =============================================================================

@app.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Execute a GABRIEL tool."""
    
    try:
        result = await _execute_tool(name, arguments)
        return [types.TextContent(type="text", text=result)]
    except Exception as e:
        return [types.TextContent(type="text", text=f"Error: {str(e)}")]

async def _execute_tool(name: str, args: Dict[str, Any]) -> str:
    """Tool execution dispatcher."""
    
    # --- CODEBASE TOOLS ---
    if name == "search_code":
        return await search_code(args.get("query"), args.get("path"), args.get("type", "both"))
    
    if name == "read_file":
        return await read_file_content(args.get("path"), args.get("lines", 500))
    
    if name == "write_file":
        return await write_file_content(args.get("path"), args.get("content"), args.get("append", False))
    
    if name == "list_files":
        return await list_directory(args.get("path"), args.get("pattern", "*"), args.get("recursive", False))
    
    # --- VOICE TOOLS ---
    if name == "speak":
        return await speak_text(args.get("text"), args.get("voice", "gabriel"), args.get("save_path"))
    
    # --- MEMORY TOOLS ---
    if name == "remember":
        return await store_memory(args.get("key"), args.get("value"), args.get("tags", []))
    
    if name == "recall":
        return await search_memory(args.get("query"), args.get("limit", 10))
    
    # --- TASK TOOLS ---
    if name == "add_task":
        return await add_task(args.get("title"), args.get("description", ""), args.get("priority", "medium"), args.get("due"))
    
    if name == "complete_task":
        return await complete_task(args.get("task_id"))
    
    if name == "list_tasks":
        return await get_tasks(args.get("status", "pending"))
    
    # --- SYSTEM TOOLS ---
    if name == "run_command":
        return await run_shell_command(args.get("command"), args.get("cwd"), args.get("timeout", 30))
    
    if name == "system_info":
        return await get_system_info()
    
    # --- PROJECT TOOLS ---
    if name == "scan_project":
        return await scan_project_structure(args.get("path"), args.get("depth", 3))
    
    if name == "git_status":
        return await get_git_status(args.get("path", str(NOIZYLAB_ROOT)))
    
    # --- DEEP KNOWLEDGE TOOLS ---
    if name == "knowledge_stats":
        return await get_knowledge_stats()
    
    if name == "search_knowledge":
        return await search_knowledge(args.get("query"), args.get("type", "all"), args.get("limit", 20))
    
    if name == "get_prompts":
        return await get_prompts_list(args.get("query"), args.get("limit", 20))
    
    if name == "get_functions":
        return await get_functions_list(args.get("name"), args.get("file_pattern"), args.get("limit", 50))
    
    if name == "get_knowledge_base":
        return await get_knowledge_entries(args.get("query"), args.get("limit", 20))
    
    if name == "get_imports":
        return await get_imports_list(args.get("filter"))
    
    if name == "get_todos":
        return await get_todos_list(args.get("limit", 50))
    
    if name == "explore_category":
        return await explore_category(args.get("category"), args.get("limit", 30))
    
    if name == "reindex_knowledge":
        return await reindex_knowledge()
    
    raise ValueError(f"Unknown tool: {name}")

# =============================================================================
# TOOL FUNCTIONS
# =============================================================================

async def search_code(query: str, path: str = None, search_type: str = "both") -> str:
    """Search codebase for files or content."""
    if not query:
        return "Query is required"

    try:
        search_path = _resolve_under_roots(path or str(NOIZYLAB_ROOT))
    except ValueError as exc:
        return str(exc)

    if not search_path.exists():
        return f"Search path not found: {search_path}"

    results: Dict[str, Any] = {
        "query": query,
        "path": str(search_path),
        "files": [],
        "matches": [],
    }

    query_lower = query.lower()
    visited = 0

    if search_type in ["filename", "both"]:
        for p in search_path.rglob("*"):
            visited += 1
            if visited > MAX_SEARCH_TRAVERSAL:
                results["truncated"] = True
                break

            if p.is_file() and query_lower in p.name.lower():
                results["files"].append(str(p))
                if len(results["files"]) >= MAX_SEARCH_RESULTS:
                    break

    if search_type in ["content", "both"] and len(results["matches"]) < MAX_SEARCH_RESULTS:
        results["matches"] = await _run_content_search(query, search_path)

    results["scanned"] = visited
    return json.dumps(results, indent=2)


async def _run_content_search(query: str, search_path: Path) -> List[str]:
    """Search file contents using ripgrep if available, otherwise grep."""
    if shutil.which("rg"):
        cmd = [
            "rg",
            "--no-config",
            "--color",
            "never",
            "--files-with-matches",
            "--max-count",
            "1",
            "--iglob",
            "*.py",
            "--iglob",
            "*.ts",
            "--iglob",
            "*.js",
            "--iglob",
            "*.md",
            query,
            str(search_path),
        ]
    else:
        cmd = [
            "grep",
            "-r",
            "-l",
            "-i",
            "--include=*.py",
            "--include=*.ts",
            "--include=*.js",
            "--include=*.md",
            query,
            str(search_path),
        ]

    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=SEARCH_TIMEOUT_SECONDS)
    except asyncio.TimeoutError:
        return [f"Content search timed out after {SEARCH_TIMEOUT_SECONDS}s"]

    matches = [line for line in stdout.decode().splitlines() if line][:MAX_SEARCH_RESULTS]
    if stderr and not matches:
        err = stderr.decode().strip()
        if err:
            matches.append(f"stderr: {err}")
    return matches

async def read_file_content(path: str, max_lines: int = 500) -> str:
    """Read file contents."""
    try:
        p = _resolve_under_roots(path)
    except ValueError as exc:
        return str(exc)

    if not p.exists():
        return f"File not found: {p}"
    if not p.is_file():
        return f"Not a file: {p}"

    # Guard against huge payloads
    if p.stat().st_size > MAX_FILE_PREVIEW_BYTES:
        preview = _read_text_with_limit(p, MAX_FILE_PREVIEW_BYTES)
        return f"{preview}\n\n...[file truncated at {MAX_FILE_PREVIEW_BYTES // 1024}KB]"

    content = p.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()
    if len(lines) > max_lines:
        remainder = len(lines) - max_lines
        return "\n".join(lines[:max_lines]) + f"\n\n...[{remainder} more lines]"
    return content

async def write_file_content(path: str, content: str, append: bool = False) -> str:
    """Write content to file."""
    if content is None:
        return "Content is required"

    encoded_length = len(content.encode("utf-8"))
    if encoded_length > MAX_WRITE_BYTES:
        return f"Content too large ({encoded_length} bytes). Limit is {MAX_WRITE_BYTES} bytes."

    try:
        p = _resolve_under_roots(path)
    except ValueError as exc:
        return str(exc)

    p.parent.mkdir(parents=True, exist_ok=True)

    if append:
        with open(p, "a", encoding="utf-8") as f:
            f.write(content)
    else:
        p.write_text(content, encoding="utf-8")
    
    return f"Written to {p}"

async def list_directory(path: str, pattern: str = "*", recursive: bool = False) -> str:
    """List directory contents."""
    try:
        p = _resolve_under_roots(path)
    except ValueError as exc:
        return str(exc)

    if not p.exists():
        return f"Path not found: {p}"
    if not p.is_dir():
        return f"Not a directory: {p}"

    iterator = p.rglob(pattern) if recursive else p.glob(pattern)

    entries = []
    truncated = False
    for entry in iterator:
        entries.append(
            {
                "name": entry.name,
                "type": "dir" if entry.is_dir() else "file",
                "size": entry.stat().st_size if entry.is_file() else 0,
                "path": str(entry),
            }
        )
        if len(entries) >= MAX_LISTING:
            truncated = True
            break

    result = {"path": str(p), "count": len(entries), "truncated": truncated, "entries": entries}
    return json.dumps(result, indent=2)

async def speak_text(text: str, voice: str = "gabriel", save_path: str = None) -> str:
    """Generate speech."""
    if not text:
        return "Text is required"

    # Check for voice engine
    voice_script = GABRIEL_ROOT / "gabriel_voice.py"
    if not voice_script.exists():
        return "Voice engine not available. Install with: pip install TTS"

    output_path: Optional[Path] = None
    if save_path:
        try:
            output_path = _resolve_under_roots(save_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
        except ValueError as exc:
            return str(exc)
    
    cmd = [sys.executable, str(voice_script), "--text", text, "--voice", voice]
    if save_path:
        cmd.extend(["--output", str(output_path)])
    
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    
    if proc.returncode == 0:
        return f"Speech generated: {output_path or 'played'}"
    return f"Speech failed: {stderr.decode()}"

async def store_memory(key: str, value: str, tags: List[str] = []) -> str:
    """Store in memory."""
    if not key or value is None:
        return "Key and value are required"

    memory = load_json(MEMORY_FILE, {"entries": []})
    
    entry = {
        "id": f"mem_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "key": key,
        "value": value,
        "tags": tags,
        "timestamp": datetime.now().isoformat()
    }
    
    memory["entries"].append(entry)
    memory["entries"] = memory["entries"][-1000:]  # Keep last 1000
    save_json(MEMORY_FILE, memory)
    
    return f"Stored memory: {key}"

async def search_memory(query: str, limit: int = 10) -> str:
    """Search memory."""
    if not query:
        return "Query is required"

    memory = load_json(MEMORY_FILE, {"entries": []})
    query_lower = query.lower()
    
    matches = []
    for entry in reversed(memory["entries"]):
        if query_lower in entry.get("key", "").lower() or query_lower in entry.get("value", "").lower() or any(query_lower in t.lower() for t in entry.get("tags", [])):
            matches.append(entry)
            if len(matches) >= limit:
                break
    
    return json.dumps(matches, indent=2)

async def add_task(title: str, description: str = "", priority: str = "medium", due: str = None) -> str:
    """Add a task."""
    if not title:
        return "Title is required"

    tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
    
    task = {
        "id": f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "title": title,
        "description": description,
        "priority": priority,
        "due": due,
        "created": datetime.now().isoformat()
    }
    
    tasks["pending"].append(task)
    save_json(TASKS_FILE, tasks)
    
    return f"Task added: {task['id']}"

async def complete_task(task_id: str) -> str:
    """Complete a task."""
    if not task_id:
        return "Task ID is required"

    tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
    
    for i, task in enumerate(tasks["pending"]):
        if task["id"] == task_id:
            task["completed_at"] = datetime.now().isoformat()
            tasks["completed"].append(task)
            tasks["pending"].pop(i)
            save_json(TASKS_FILE, tasks)
            return f"Task completed: {task_id}"
    
    return f"Task not found: {task_id}"

async def get_tasks(status: str = "pending") -> str:
    """Get tasks."""
    tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
    
    if status == "all":
        return json.dumps(tasks, indent=2)
    return json.dumps(tasks.get(status, []), indent=2)

async def run_shell_command(command: str, cwd: str = None, timeout: int = 30) -> str:
    """Run a shell command (with safety checks)."""
    if not command or not command.strip():
        return "Command is required"

    command = command.strip()

    try:
        resolved_cwd = _resolve_under_roots(cwd) if cwd else None
    except ValueError as exc:
        return str(exc)

    # Block dangerous commands
    dangerous = ["rm -rf /", "mkfs", "dd if=", "> /dev/", ":(){ :|:& };:"]
    if any(d in command for d in dangerous):
        return "Command blocked for safety"
    
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(resolved_cwd) if resolved_cwd else None
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        
        output = stdout.decode()
        if stderr:
            output += f"\n[STDERR]\n{stderr.decode()}"
        return output or "(no output)"
    except asyncio.TimeoutError:
        return f"Command timed out after {timeout}s"
    except Exception as e:
        return f"Error: {e}"

async def get_system_info() -> str:
    """Get system information."""
    info = {}
    
    # CPU
    try:
        result = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True)
        info["cpu"] = result.stdout.strip()
    except:
        info["cpu"] = "unknown"
    
    # Memory
    try:
        result = subprocess.run(["vm_stat"], capture_output=True, text=True)
        info["memory_raw"] = result.stdout[:500]
    except:
        pass
    
    # Disk
    try:
        result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
        info["disk"] = result.stdout
    except:
        pass
    
    return json.dumps(info, indent=2)

async def scan_project_structure(path: str, depth: int = 3) -> str:
    """Scan project structure."""
    try:
        p = _resolve_under_roots(path)
    except ValueError as exc:
        return str(exc)

    if not p.exists():
        return f"Path not found: {p}"
    
    structure: Dict[str, Any] = {"root": str(p), "files": 0, "dirs": 0, "by_type": {}, "tree": [], "truncated": False}
    nodes_scanned = 0

    def scan(current: Path, current_depth: int):
        nonlocal nodes_scanned
        if current_depth > depth or structure["truncated"]:
            return
        
        for item in sorted(current.iterdir()):
            if item.name.startswith('.'):
                continue
            nodes_scanned += 1
            if nodes_scanned >= MAX_SEARCH_TRAVERSAL:
                structure["truncated"] = True
                break

            if item.is_dir():
                structure["dirs"] += 1
                if current_depth < depth:
                    scan(item, current_depth + 1)
            else:
                structure["files"] += 1
                ext = item.suffix or "no_ext"
                structure["by_type"][ext] = structure["by_type"].get(ext, 0) + 1
    
    scan(p, 0)
    structure["scanned"] = nodes_scanned
    return json.dumps(structure, indent=2)

async def get_git_status(path: str) -> str:
    """Get git status."""
    try:
        repo_path = _resolve_under_roots(path)
    except ValueError as exc:
        return str(exc)

    try:
        proc = await asyncio.create_subprocess_exec(
            "git", "status", "--porcelain", "-b",
            cwd=str(repo_path),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        return stdout.decode() or "Clean working tree"
    except Exception as e:
        return f"Git error: {e}"

# =============================================================================
# DEEP KNOWLEDGE TOOLS IMPLEMENTATION
# =============================================================================

async def get_knowledge_stats() -> str:
    """Get brain statistics."""
    brain = load_json(BRAIN_FILE, {})
    stats = brain.get("stats", {})
    
    result = {
        "indexed": True,
        "version": brain.get("version", "unknown"),
        "created": brain.get("created", "unknown"),
        "stats": stats,
        "brain_file": str(BRAIN_FILE),
        "message": f"🧠 GABRIEL knows {stats.get('total_files', 0):,} files with {stats.get('total_lines', 0):,} lines of code!"
    }
    return json.dumps(result, indent=2)

async def search_knowledge(query: str, search_type: str = "all", limit: int = 20) -> str:
    """Search the deep knowledge index."""
    if not query:
        return "Query is required"

    brain = load_json(BRAIN_FILE, {})
    query_lower = query.lower()
    results = {"query": query, "type": search_type, "results": []}
    
    # Search prompts
    if search_type in ["all", "prompts"]:
        for p in brain.get("prompts", []):
            if query_lower in p.get("path", "").lower() or query_lower in p.get("name", "").lower():
                results["results"].append({"type": "prompt", **p})
                if len(results["results"]) >= limit:
                    break
    
    # Search functions
    if search_type in ["all", "functions"] and len(results["results"]) < limit:
        for f in brain.get("functions", []):
            if query_lower in f.get("name", "").lower():
                results["results"].append({"type": "function", **f})
                if len(results["results"]) >= limit:
                    break
    
    # Search classes
    if search_type in ["all", "classes"] and len(results["results"]) < limit:
        for c in brain.get("classes", []):
            if query_lower in c.get("name", "").lower():
                results["results"].append({"type": "class", **c})
                if len(results["results"]) >= limit:
                    break
    
    # Search knowledge base
    if search_type in ["all", "knowledge"] and len(results["results"]) < limit:
        for k in brain.get("knowledge_base", []):
            if query_lower in k.get("title", "").lower() or query_lower in str(k.get("headers", [])).lower():
                results["results"].append({"type": "knowledge", "path": k["path"], "title": k["title"]})
                if len(results["results"]) >= limit:
                    break
    
    # Search files
    if search_type in ["all", "files"] and len(results["results"]) < limit:
        for f in brain.get("files", []):
            if query_lower in f.get("path", "").lower() or query_lower in f.get("name", "").lower():
                results["results"].append({"type": "file", **f})
                if len(results["results"]) >= limit:
                    break
    
    results["count"] = len(results["results"])
    return json.dumps(results, indent=2)

async def get_prompts_list(query: str = None, limit: int = 20) -> str:
    """Get indexed prompts."""
    brain = load_json(BRAIN_FILE, {})
    prompts = brain.get("prompts", [])
    
    if query:
        query_lower = query.lower()
        prompts = [p for p in prompts if query_lower in p.get("path", "").lower() or query_lower in p.get("name", "").lower()]
    
    return json.dumps({
        "total": len(brain.get("prompts", [])),
        "filtered": len(prompts[:limit]),
        "prompts": prompts[:limit]
    }, indent=2)

async def get_functions_list(name: str, file_pattern: str = None, limit: int = 50) -> str:
    """Search functions."""
    if not name:
        return "Function name is required"

    brain = load_json(BRAIN_FILE, {})
    functions = brain.get("functions", [])
    name_lower = name.lower()
    
    matches = []
    for f in functions:
        if name_lower in f.get("name", "").lower():
            if file_pattern and file_pattern.lower() not in f.get("file", "").lower():
                continue
            matches.append(f)
            if len(matches) >= limit:
                break
    
    return json.dumps({
        "total_indexed": len(functions),
        "matches": len(matches),
        "functions": matches
    }, indent=2)

async def get_knowledge_entries(query: str, limit: int = 20) -> str:
    """Search knowledge base."""
    if not query:
        return "Query is required"

    brain = load_json(BRAIN_FILE, {})
    kb = brain.get("knowledge_base", [])
    query_lower = query.lower()
    
    matches = []
    for k in kb:
        if query_lower in k.get("title", "").lower() or query_lower in str(k.get("headers", [])).lower() or query_lower in k.get("preview", "").lower():
            matches.append(k)
            if len(matches) >= limit:
                break
    
    return json.dumps({
        "total_indexed": len(kb),
        "matches": len(matches),
        "entries": matches
    }, indent=2)

async def get_imports_list(filter_str: str = None) -> str:
    """Get imports."""
    brain = load_json(BRAIN_FILE, {})
    imports = brain.get("imports", [])
    
    if filter_str:
        imports = [i for i in imports if filter_str.lower() in i.lower()]
    
    return json.dumps({
        "total": len(brain.get("imports", [])),
        "filtered": len(imports),
        "imports": sorted(imports)
    }, indent=2)

async def get_todos_list(limit: int = 50) -> str:
    """Get TODOs."""
    brain = load_json(BRAIN_FILE, {})
    todos = brain.get("todos", [])[:limit]
    
    return json.dumps({
        "total": len(brain.get("todos", [])),
        "showing": len(todos),
        "todos": todos
    }, indent=2)

async def explore_category(category: str, limit: int = 30) -> str:
    """Explore files by category."""
    if not category:
        return "Category is required"

    brain = load_json(BRAIN_FILE, {})
    by_category = brain.get("by_category", {})
    
    files = by_category.get(category, [])[:limit]
    
    return json.dumps({
        "category": category,
        "total": len(by_category.get(category, [])),
        "showing": len(files),
        "files": files
    }, indent=2)

async def reindex_knowledge() -> str:
    """Re-run the indexer."""
    indexer_path = GABRIEL_ROOT / "tools" / "deep_knowledge_indexer.py"
    
    if not indexer_path.exists():
        return "Indexer not found!"
    
    proc = await asyncio.create_subprocess_exec(
        sys.executable, str(indexer_path),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    
    return f"Reindex complete:\n{stdout.decode()}"

# =============================================================================
# MAIN
# =============================================================================

async def main():
    """Run the GABRIEL MCP server."""
    log("🧠 GABRIEL MCP Server starting...")
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
