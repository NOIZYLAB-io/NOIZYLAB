#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║  GABRIEL MCP SERVER - Model Context Protocol for Claude Desktop               ║
║  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // INFINITE ENERGY ⚡                  ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent, Resource
except ImportError:
    print("MCP package not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# ════════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

GABRIEL_ROOT = Path(__file__).parent.parent.parent.resolve()
VERSION = "3.0.0"

# ════════════════════════════════════════════════════════════════════════════════
# MCP SERVER
# ════════════════════════════════════════════════════════════════════════════════

server = Server("gabriel-mcp")

@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available GABRIEL tools."""
    return [
        Tool(
            name="gabriel_status",
            description="Get GABRIEL system status including services, code inventory, and health",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="gabriel_search",
            description="Search across GABRIEL codebase and documentation",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "file_type": {
                        "type": "string",
                        "description": "File type filter (py, js, sh, md)",
                        "enum": ["py", "js", "sh", "md", "all"]
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="gabriel_list_code",
            description="List code files in GABRIEL directories",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory to list (CODE, scripts, workers, CODEMASTER)"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "File pattern filter (e.g., *.py)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="gabriel_run_command",
            description="Run a GABRIEL command (status, deploy, sync, doctor)",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Command to run",
                        "enum": ["status", "doctor", "sync", "clean"]
                    }
                },
                "required": ["command"]
            }
        ),
        Tool(
            name="codemaster_scan",
            description="Scan and analyze code organization",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {
                        "type": "string",
                        "description": "Directory to scan"
                    }
                },
                "required": []
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Execute a GABRIEL tool."""
    
    if name == "gabriel_status":
        return await get_status()
    
    elif name == "gabriel_search":
        query = arguments.get("query", "")
        file_type = arguments.get("file_type", "all")
        return await search_code(query, file_type)
    
    elif name == "gabriel_list_code":
        directory = arguments.get("directory", "")
        pattern = arguments.get("pattern", "*")
        return await list_code(directory, pattern)
    
    elif name == "gabriel_run_command":
        command = arguments.get("command", "status")
        return await run_command(command)
    
    elif name == "codemaster_scan":
        target = arguments.get("target", str(GABRIEL_ROOT))
        return await codemaster_scan(target)
    
    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def get_status() -> List[TextContent]:
    """Get GABRIEL system status."""
    import socket
    
    def check_port(port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    status = {
        "gabriel_root": str(GABRIEL_ROOT),
        "version": VERSION,
        "timestamp": datetime.now().isoformat(),
        "services": {
            "MCP Server": {"port": 8080, "running": check_port(8080)},
            "API Gateway": {"port": 3000, "running": check_port(3000)},
        },
        "directories": {}
    }
    
    # Count code files
    for dir_name in ["CODE", "scripts", "workers", "CODEMASTER"]:
        dir_path = GABRIEL_ROOT / dir_name
        if dir_path.exists():
            py_count = len(list(dir_path.rglob("*.py"))) if dir_name != "CODEMASTER" else "large"
            status["directories"][dir_name] = {
                "exists": True,
                "python_files": py_count
            }
    
    return [TextContent(type="text", text=json.dumps(status, indent=2))]


async def search_code(query: str, file_type: str = "all") -> List[TextContent]:
    """Search across GABRIEL codebase."""
    import subprocess
    
    ext_map = {
        "py": "*.py",
        "js": "*.js", 
        "sh": "*.sh",
        "md": "*.md",
        "all": "*"
    }
    
    pattern = ext_map.get(file_type, "*")
    
    try:
        result = subprocess.run(
            ["grep", "-r", "-l", "-i", query, "--include", pattern, str(GABRIEL_ROOT)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        files = result.stdout.strip().split("\n") if result.stdout.strip() else []
        
        # Limit and clean results
        files = [f.replace(str(GABRIEL_ROOT) + "/", "") for f in files[:20]]
        
        return [TextContent(type="text", text=json.dumps({
            "query": query,
            "file_type": file_type,
            "matches": files,
            "count": len(files)
        }, indent=2))]
        
    except Exception as e:
        return [TextContent(type="text", text=f"Search error: {str(e)}")]


async def list_code(directory: str, pattern: str) -> List[TextContent]:
    """List code files in a directory."""
    
    if directory:
        target = GABRIEL_ROOT / directory
    else:
        target = GABRIEL_ROOT
    
    if not target.exists():
        return [TextContent(type="text", text=f"Directory not found: {directory}")]
    
    files = []
    for f in target.rglob(pattern):
        if f.is_file() and not any(p in str(f) for p in ["__pycache__", "node_modules", ".git"]):
            files.append(str(f.relative_to(GABRIEL_ROOT)))
    
    return [TextContent(type="text", text=json.dumps({
        "directory": directory or "root",
        "pattern": pattern,
        "files": files[:50],
        "total": len(files)
    }, indent=2))]


async def run_command(command: str) -> List[TextContent]:
    """Run a GABRIEL command."""
    import subprocess
    
    cmd_map = {
        "status": ["python3", str(GABRIEL_ROOT / "gabriel.py"), "status"],
        "doctor": ["python3", str(GABRIEL_ROOT / "gabriel.py"), "doctor"],
        "sync": ["bash", str(GABRIEL_ROOT / "gorunfree"), "sync"],
        "clean": ["bash", str(GABRIEL_ROOT / "gorunfree"), "clean"]
    }
    
    if command not in cmd_map:
        return [TextContent(type="text", text=f"Unknown command: {command}")]
    
    try:
        result = subprocess.run(
            cmd_map[command],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=GABRIEL_ROOT
        )
        
        output = result.stdout + result.stderr
        return [TextContent(type="text", text=output[:4000])]
        
    except Exception as e:
        return [TextContent(type="text", text=f"Command error: {str(e)}")]


async def codemaster_scan(target: str) -> List[TextContent]:
    """Run CODEMASTER scan."""
    import subprocess
    
    try:
        result = subprocess.run(
            ["python3", str(GABRIEL_ROOT / "codemaster.py"), "status"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=GABRIEL_ROOT
        )
        
        return [TextContent(type="text", text=result.stdout + result.stderr)]
        
    except Exception as e:
        return [TextContent(type="text", text=f"CODEMASTER error: {str(e)}")]


@server.list_resources()
async def list_resources() -> List[Resource]:
    """List GABRIEL resources."""
    return [
        Resource(
            uri=f"gabriel://readme",
            name="GABRIEL README",
            description="Main README documentation",
            mimeType="text/markdown"
        ),
        Resource(
            uri=f"gabriel://status",
            name="System Status",
            description="Current system status",
            mimeType="application/json"
        )
    ]


@server.read_resource()
async def read_resource(uri: str) -> str:
    """Read a GABRIEL resource."""
    
    if uri == "gabriel://readme":
        readme = GABRIEL_ROOT / "README.md"
        if readme.exists():
            return readme.read_text()
        return "README not found"
    
    elif uri == "gabriel://status":
        result = await get_status()
        return result[0].text
    
    return f"Unknown resource: {uri}"


# ════════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════════

async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
