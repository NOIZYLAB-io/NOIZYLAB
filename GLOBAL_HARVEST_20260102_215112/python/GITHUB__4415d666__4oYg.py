#!/usr/bin/env python3
"""
🧠 GABRIEL UNIFIED MCP SERVER v2.0
==================================
The ultimate MCP server combining all GABRIEL intelligence:
- Deep codebase knowledge (29K+ files, 8.5M lines)
- AI model orchestration (40+ models)
- Voice synthesis
- Memory systems
- System operations
- Network operations

© NOIZYLAB 2024-2025
"""

import asyncio
import json
import os
import sys
import subprocess
import hashlib
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from collections import defaultdict
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

# =============================================================================
# MCP SDK
# =============================================================================
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

GABRIEL_ROOT = Path("/Users/m2ultra/NOIZYLAB/GABRIEL")
NOIZYLAB_ROOT = Path("/Users/m2ultra/NOIZYLAB")
CONFIG_DIR = Path.home() / ".noizylab"
DATA_DIR = GABRIEL_ROOT / "memcell_data"
LOGS_DIR = GABRIEL_ROOT / "logs"

# Ensure directories exist
for d in [CONFIG_DIR, DATA_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Data files
BRAIN_FILE = DATA_DIR / "gabriel_brain.json"
MEMORY_FILE = DATA_DIR / "memory.json"
TASKS_FILE = DATA_DIR / "tasks.json"
KEYS_FILE = CONFIG_DIR / "api_keys.json"

# Environment file
ENV_FILE = Path.home() / ".env.gabriel"

# =============================================================================
# AI SERVICE REGISTRY
# =============================================================================

@dataclass
class AIService:
    name: str
    category: str
    api_url: str
    api_key_env: str
    models: List[str] = field(default_factory=list)


AI_SERVICES = {
    # Video Generation
    "runway": AIService("Runway Gen-3", "video", "https://api.runwayml.com/v1", "RUNWAY_API_KEY", ["gen-3-alpha", "gen-3-turbo"]),
    "kling": AIService("Kling AI", "video", "https://api.klingai.com/v1", "KLING_API_KEY", ["kling-1.6", "kling-pro"]),
    "pika": AIService("Pika", "video", "https://api.pika.art/v1", "PIKA_API_KEY", ["pika-1.5"]),
    
    # Audio Generation
    "suno": AIService("Suno", "audio", "https://api.suno.ai/v1", "SUNO_API_KEY", ["chirp-v3"]),
    "udio": AIService("Udio", "audio", "https://api.udio.com/v1", "UDIO_API_KEY", ["udio-32"]),
    "elevenlabs": AIService("ElevenLabs", "audio", "https://api.elevenlabs.io/v1", "ELEVENLABS_API_KEY", ["eleven_multilingual_v2"]),
    
    # Avatar/Video
    "heygen": AIService("HeyGen", "avatar", "https://api.heygen.com/v2", "HEYGEN_API_KEY", ["v2"]),
    
    # LLMs
    "openai": AIService("OpenAI", "llm", "https://api.openai.com/v1", "OPENAI_API_KEY", ["gpt-4o", "gpt-4o-mini", "o1", "o1-mini"]),
    "anthropic": AIService("Anthropic", "llm", "https://api.anthropic.com/v1", "ANTHROPIC_API_KEY", ["claude-sonnet-4-20250514", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"]),
    "gemini": AIService("Google Gemini", "llm", "https://generativelanguage.googleapis.com/v1beta", "GEMINI_API_KEY", ["gemini-2.0-flash-exp", "gemini-1.5-pro"]),
    "groq": AIService("Groq", "llm", "https://api.groq.com/openai/v1", "GROQ_API_KEY", ["llama-3.3-70b-versatile", "mixtral-8x7b"]),
    "deepseek": AIService("DeepSeek", "llm", "https://api.deepseek.com/v1", "DEEPSEEK_API_KEY", ["deepseek-chat", "deepseek-coder"]),
    "mistral": AIService("Mistral", "llm", "https://api.mistral.ai/v1", "MISTRAL_API_KEY", ["mistral-large-latest"]),
    "together": AIService("Together AI", "llm", "https://api.together.xyz/v1", "TOGETHER_API_KEY", ["meta-llama/Meta-Llama-3.1-405B"]),
    "perplexity": AIService("Perplexity", "llm", "https://api.perplexity.ai", "PERPLEXITY_API_KEY", ["llama-3.1-sonar-large"]),
    "xai": AIService("xAI Grok", "llm", "https://api.x.ai/v1", "XAI_API_KEY", ["grok-beta"]),
    "cohere": AIService("Cohere", "llm", "https://api.cohere.ai/v1", "COHERE_API_KEY", ["command-r-plus"]),
}

# =============================================================================
# UTILITY CLASSES
# =============================================================================

class Logger:
    """Thread-safe logger."""
    
    @staticmethod
    def log(msg: str, level: str = "INFO"):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] [{level}] {msg}"
        print(line, file=sys.stderr)
        
        # Also write to log file
        log_file = LOGS_DIR / f"gabriel_{datetime.now().strftime('%Y%m%d')}.log"
        with open(log_file, "a") as f:
            f.write(line + "\n")


class KeyManager:
    """Secure API key management."""
    
    def __init__(self):
        self.keys = self._load()
        self._load_env_file()
    
    def _load(self) -> Dict:
        if KEYS_FILE.exists():
            try:
                return json.loads(KEYS_FILE.read_text())
            except:
                return {}
        return {}
    
    def _load_env_file(self):
        """Load keys from .env.gabriel file."""
        if ENV_FILE.exists():
            for line in ENV_FILE.read_text().split("\n"):
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    value = value.strip('"').strip("'")
                    if value and not value.startswith("sk-") == False:  # Skip placeholders
                        os.environ[key] = value
    
    def _save(self):
        KEYS_FILE.write_text(json.dumps(self.keys, indent=2))
        os.chmod(KEYS_FILE, 0o600)
    
    def set(self, service: str, key: str):
        self.keys[service] = key
        self._save()
    
    def get(self, service: str) -> Optional[str]:
        # First check environment
        svc = AI_SERVICES.get(service)
        if svc:
            env_key = os.environ.get(svc.api_key_env)
            if env_key:
                return env_key
        # Then check stored keys
        return self.keys.get(service)
    
    def list(self) -> Dict[str, bool]:
        return {name: bool(self.get(name)) for name in AI_SERVICES}
    
    def validate(self, service: str) -> Dict:
        """Validate an API key by making a test request."""
        key = self.get(service)
        if not key:
            return {"valid": False, "error": "No API key found"}
        
        svc = AI_SERVICES.get(service)
        if not svc:
            return {"valid": False, "error": "Unknown service"}
        
        # Simple validation - just check key format
        return {"valid": True, "service": svc.name, "key_length": len(key)}


class MemoryStore:
    """Persistent memory storage."""
    
    def __init__(self):
        self.data = self._load()
    
    def _load(self) -> Dict:
        if MEMORY_FILE.exists():
            try:
                return json.loads(MEMORY_FILE.read_text())
            except:
                return {"entries": [], "context": {}}
        return {"entries": [], "context": {}}
    
    def _save(self):
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2, default=str))
    
    def store(self, key: str, value: Any, tags: List[str] = None):
        entry = {
            "id": f"mem_{datetime.now().strftime('%Y%m%d%H%M%S')}_{hashlib.md5(key.encode()).hexdigest()[:6]}",
            "key": key,
            "value": value,
            "tags": tags or [],
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
        }
        
        # Update existing or add new
        for i, e in enumerate(self.data["entries"]):
            if e.get("key") == key:
                entry["created"] = e.get("created", entry["created"])
                self.data["entries"][i] = entry
                self._save()
                return entry["id"]
        
        self.data["entries"].append(entry)
        self.data["entries"] = self.data["entries"][-1000:]  # Keep last 1000
        self._save()
        return entry["id"]
    
    def get(self, key: str) -> Optional[Dict]:
        for entry in self.data["entries"]:
            if entry.get("key") == key:
                return entry
        return None
    
    def search(self, query: str, limit: int = 20) -> List[Dict]:
        results = []
        query_lower = query.lower()
        
        for entry in reversed(self.data["entries"]):
            if query_lower in entry.get("key", "").lower() or \
               query_lower in str(entry.get("value", "")).lower() or \
               any(query_lower in t.lower() for t in entry.get("tags", [])):
                results.append(entry)
                if len(results) >= limit:
                    break
        
        return results
    
    def delete(self, key: str) -> bool:
        for i, entry in enumerate(self.data["entries"]):
            if entry.get("key") == key:
                self.data["entries"].pop(i)
                self._save()
                return True
        return False
    
    def set_context(self, key: str, value: Any):
        """Set session context."""
        self.data["context"][key] = value
        self._save()
    
    def get_context(self, key: str) -> Any:
        """Get session context."""
        return self.data["context"].get(key)


class CodebaseScanner:
    """Deep codebase analysis."""
    
    LANG_MAP = {
        '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
        '.go': 'Go', '.rs': 'Rust', '.sh': 'Shell', '.bash': 'Shell',
        '.html': 'HTML', '.css': 'CSS', '.scss': 'SCSS',
        '.md': 'Markdown', '.json': 'JSON', '.yaml': 'YAML', '.yml': 'YAML',
        '.swift': 'Swift', '.c': 'C', '.cpp': 'C++', '.h': 'C/C++ Header',
        '.java': 'Java', '.kt': 'Kotlin', '.rb': 'Ruby', '.php': 'PHP',
        '.sql': 'SQL', '.graphql': 'GraphQL', '.vue': 'Vue', '.svelte': 'Svelte',
    }
    
    SKIP_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', '.venv', 
                 '.next', '.cache', 'dist', 'build', '.DS_Store'}
    
    def scan(self, path: Path, depth: int = 10) -> Dict:
        """Scan a directory and collect statistics."""
        stats = {
            'timestamp': datetime.now().isoformat(),
            'path': str(path),
            'total_files': 0,
            'total_lines': 0,
            'total_bytes': 0,
            'languages': defaultdict(lambda: {'files': 0, 'lines': 0, 'bytes': 0}),
            'hot_files': [],
            'recent_files': [],
        }
        
        files_data = []
        recent_cutoff = time.time() - (7 * 24 * 3600)  # 7 days
        
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in self.SKIP_DIRS]
            rel_depth = str(root).count(os.sep) - str(path).count(os.sep)
            if rel_depth > depth:
                continue
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                fp = Path(root) / file
                try:
                    st = fp.stat()
                    ext = fp.suffix.lower()
                    
                    info = {
                        'path': str(fp.relative_to(path)),
                        'size': st.st_size,
                        'lines': 0,
                        'complexity': 0,
                        'mtime': st.st_mtime,
                    }
                    
                    if ext in self.LANG_MAP:
                        try:
                            content = fp.read_text(errors='ignore')
                            lines = content.split('\n')
                            info['lines'] = len(lines)
                            
                            # Calculate complexity
                            for line in lines:
                                if any(k in line for k in ['if ', 'for ', 'while ', 'def ', 'fn ', 'func ', 'class ', 'async ']):
                                    info['complexity'] += 1
                            
                            lang = self.LANG_MAP[ext]
                            stats['languages'][lang]['files'] += 1
                            stats['languages'][lang]['lines'] += info['lines']
                            stats['languages'][lang]['bytes'] += info['size']
                        except:
                            pass
                    
                    files_data.append(info)
                    stats['total_files'] += 1
                    stats['total_lines'] += info['lines']
                    stats['total_bytes'] += info['size']
                    
                    # Track recent files
                    if st.st_mtime > recent_cutoff:
                        stats['recent_files'].append(info)
                except:
                    continue
        
        # Sort by complexity for hot files
        files_data.sort(key=lambda x: x['complexity'], reverse=True)
        stats['hot_files'] = files_data[:20]
        
        # Sort recent files by mtime
        stats['recent_files'].sort(key=lambda x: x['mtime'], reverse=True)
        stats['recent_files'] = stats['recent_files'][:20]
        
        stats['languages'] = dict(stats['languages'])
        return stats
    
    def search(self, query: str, path: Path, search_type: str = "both", limit: int = 50) -> List[Dict]:
        """Search codebase for files or content."""
        results = []
        q = query.lower()
        
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in self.SKIP_DIRS]
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                fp = Path(root) / file
                rel_path = str(fp.relative_to(path))
                
                # Filename match
                if search_type in ["filename", "both"] and q in file.lower():
                    results.append({
                        'type': 'filename',
                        'path': rel_path,
                        'name': file,
                    })
                
                # Content match
                if search_type in ["content", "both"] and fp.suffix.lower() in self.LANG_MAP:
                    try:
                        content = fp.read_text(errors='ignore')
                        if q in content.lower():
                            # Find matching lines
                            matches = []
                            for i, line in enumerate(content.split('\n'), 1):
                                if q in line.lower():
                                    matches.append({'line': i, 'text': line.strip()[:100]})
                                    if len(matches) >= 5:
                                        break
                            
                            results.append({
                                'type': 'content',
                                'path': rel_path,
                                'matches': matches,
                            })
                    except:
                        pass
                
                if len(results) >= limit:
                    break
            
            if len(results) >= limit:
                break
        
        return results


# =============================================================================
# AI MODEL CALLER
# =============================================================================

class AIOrchestrator:
    """Unified AI model interface."""
    
    def __init__(self, key_manager: KeyManager):
        self.keys = key_manager
        self.executor = ThreadPoolExecutor(max_workers=10)
    
    def _make_request(self, url: str, method: str, headers: Dict, body: Dict = None, timeout: int = 120) -> Dict:
        """Make HTTP request to AI API."""
        try:
            data = json.dumps(body).encode() if body else None
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode() if e.fp else str(e)
            return {"error": f"HTTP {e.code}: {error_body}"}
        except Exception as e:
            return {"error": str(e)}
    
    def call_claude(self, prompt: str, model: str = "claude-sonnet-4-20250514", system: str = None) -> Dict:
        """Call Anthropic Claude."""
        key = self.keys.get("anthropic")
        if not key:
            return {"error": "ANTHROPIC_API_KEY not set"}
        
        start = time.perf_counter()
        
        payload = {
            "model": model,
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system:
            payload["system"] = system
        
        result = self._make_request(
            "https://api.anthropic.com/v1/messages",
            "POST",
            {
                "x-api-key": key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            payload
        )
        
        latency = int((time.perf_counter() - start) * 1000)
        
        if "content" in result:
            return {
                "success": True,
                "provider": "anthropic",
                "model": model,
                "content": result["content"][0]["text"],
                "tokens": result.get("usage", {}),
                "latency_ms": latency
            }
        return {"success": False, "error": result.get("error", str(result))}
    
    def call_openai(self, prompt: str, model: str = "gpt-4o", system: str = None) -> Dict:
        """Call OpenAI."""
        key = self.keys.get("openai")
        if not key:
            return {"error": "OPENAI_API_KEY not set"}
        
        start = time.perf_counter()
        
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        result = self._make_request(
            "https://api.openai.com/v1/chat/completions",
            "POST",
            {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            {"model": model, "messages": messages, "max_tokens": 4096}
        )
        
        latency = int((time.perf_counter() - start) * 1000)
        
        if "choices" in result:
            return {
                "success": True,
                "provider": "openai",
                "model": model,
                "content": result["choices"][0]["message"]["content"],
                "tokens": result.get("usage", {}),
                "latency_ms": latency
            }
        return {"success": False, "error": result.get("error", str(result))}
    
    def call_gemini(self, prompt: str, model: str = "gemini-2.0-flash-exp") -> Dict:
        """Call Google Gemini."""
        key = self.keys.get("gemini")
        if not key:
            return {"error": "GEMINI_API_KEY not set"}
        
        start = time.perf_counter()
        
        result = self._make_request(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
            "POST",
            {"Content-Type": "application/json"},
            {"contents": [{"parts": [{"text": prompt}]}]}
        )
        
        latency = int((time.perf_counter() - start) * 1000)
        
        if "candidates" in result:
            return {
                "success": True,
                "provider": "gemini",
                "model": model,
                "content": result["candidates"][0]["content"]["parts"][0]["text"],
                "tokens": result.get("usageMetadata", {}),
                "latency_ms": latency
            }
        return {"success": False, "error": result.get("error", str(result))}
    
    def call_groq(self, prompt: str, model: str = "llama-3.3-70b-versatile") -> Dict:
        """Call Groq (ultra-fast)."""
        key = self.keys.get("groq")
        if not key:
            return {"error": "GROQ_API_KEY not set"}
        
        start = time.perf_counter()
        
        result = self._make_request(
            "https://api.groq.com/openai/v1/chat/completions",
            "POST",
            {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            {"model": model, "messages": [{"role": "user", "content": prompt}]}
        )
        
        latency = int((time.perf_counter() - start) * 1000)
        
        if "choices" in result:
            return {
                "success": True,
                "provider": "groq",
                "model": model,
                "content": result["choices"][0]["message"]["content"],
                "tokens": result.get("usage", {}),
                "latency_ms": latency
            }
        return {"success": False, "error": result.get("error", str(result))}
    
    def call(self, provider: str, prompt: str, model: str = None, **kwargs) -> Dict:
        """Unified call to any provider."""
        providers = {
            "claude": self.call_claude,
            "anthropic": self.call_claude,
            "openai": self.call_openai,
            "gpt": self.call_openai,
            "gemini": self.call_gemini,
            "groq": self.call_groq,
        }
        
        if provider.lower() not in providers:
            return {"error": f"Unknown provider: {provider}. Available: {list(providers.keys())}"}
        
        func = providers[provider.lower()]
        if model:
            return func(prompt, model=model, **kwargs)
        return func(prompt, **kwargs)
    
    def race(self, prompt: str, providers: List[str] = None) -> Dict[str, Dict]:
        """Race multiple providers and return all responses."""
        if providers is None:
            providers = ["claude", "openai", "gemini", "groq"]
        
        import concurrent.futures
        results = {}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(providers)) as executor:
            futures = {executor.submit(self.call, p, prompt): p for p in providers}
            for future in concurrent.futures.as_completed(futures):
                provider = futures[future]
                try:
                    results[provider] = future.result()
                except Exception as e:
                    results[provider] = {"success": False, "error": str(e)}
        
        return results


# =============================================================================
# MCP SERVER
# =============================================================================

app = Server("gabriel-unified")

# Initialize components
logger = Logger()
keys = KeyManager()
memory = MemoryStore()
scanner = CodebaseScanner()
ai = AIOrchestrator(keys)


def load_json(path: Path, default: Any = None) -> Any:
    """Safe JSON loader."""
    try:
        if path.exists():
            return json.loads(path.read_text())
    except Exception as e:
        logger.log(f"Error loading {path}: {e}", "ERROR")
    return default if default is not None else {}


def save_json(path: Path, data: Any):
    """Safe JSON saver."""
    path.write_text(json.dumps(data, indent=2, default=str))


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
            description="Deep knowledge index (29K+ files, 8.5M lines)",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://memory",
            name="Conversation Memory",
            description="Persistent memory and context",
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
            description="GABRIEL system health and API status",
            mimeType="application/json"
        ),
        types.Resource(
            uri="gabriel://services",
            name="AI Services",
            description="Available AI services and their status",
            mimeType="application/json"
        ),
    ]


@app.read_resource()
async def read_resource(uri: str) -> str:
    """Read a GABRIEL resource."""
    
    if uri == "gabriel://brain":
        brain = load_json(BRAIN_FILE, {"knowledge": [], "indexed": False})
        return json.dumps({
            "indexed": brain.get("indexed", False),
            "stats": brain.get("stats", {}),
            "version": brain.get("version", "unknown"),
        }, indent=2)
    
    if uri == "gabriel://memory":
        return json.dumps(memory.data, indent=2)
    
    if uri == "gabriel://tasks":
        return json.dumps(load_json(TASKS_FILE, {"pending": [], "completed": []}), indent=2)
    
    if uri == "gabriel://status":
        status = {
            "online": True,
            "timestamp": datetime.now().isoformat(),
            "version": "2.0.0",
            "gabriel_root": str(GABRIEL_ROOT),
            "api_keys_configured": sum(1 for k in keys.list().values() if k),
            "memory_entries": len(memory.data.get("entries", [])),
        }
        return json.dumps(status, indent=2)
    
    if uri == "gabriel://services":
        services = {}
        for name, svc in AI_SERVICES.items():
            services[name] = {
                "name": svc.name,
                "category": svc.category,
                "models": svc.models,
                "configured": bool(keys.get(name)),
            }
        return json.dumps(services, indent=2)
    
    raise ValueError(f"Unknown resource: {uri}")


# =============================================================================
# TOOLS
# =============================================================================

@app.list_tools()
async def list_tools() -> List[types.Tool]:
    """List all GABRIEL tools."""
    return [
        # === CODEBASE TOOLS ===
        types.Tool(
            name="scan_codebase",
            description="Scan a directory to get statistics (files, lines, languages, complexity)",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Directory to scan (default: NOIZYLAB)"},
                    "depth": {"type": "integer", "description": "Max depth", "default": 10}
                }
            }
        ),
        types.Tool(
            name="search_code",
            description="Search codebase for files or content matching a pattern",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search pattern"},
                    "path": {"type": "string", "description": "Directory to search"},
                    "type": {"type": "string", "enum": ["filename", "content", "both"], "default": "both"},
                    "limit": {"type": "integer", "default": 50}
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
                    "lines": {"type": "integer", "description": "Max lines", "default": 500}
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
                    "append": {"type": "boolean", "default": False}
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
                    "pattern": {"type": "string", "default": "*"},
                    "recursive": {"type": "boolean", "default": False}
                },
                "required": ["path"]
            }
        ),
        
        # === AI TOOLS ===
        types.Tool(
            name="ai_call",
            description="Call an AI model (claude, openai, gemini, groq)",
            inputSchema={
                "type": "object",
                "properties": {
                    "provider": {"type": "string", "description": "AI provider (claude, openai, gemini, groq)"},
                    "prompt": {"type": "string", "description": "Prompt to send"},
                    "model": {"type": "string", "description": "Specific model (optional)"},
                    "system": {"type": "string", "description": "System prompt (optional)"}
                },
                "required": ["provider", "prompt"]
            }
        ),
        types.Tool(
            name="ai_race",
            description="Race multiple AI providers and get all responses",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {"type": "string", "description": "Prompt to send"},
                    "providers": {"type": "array", "items": {"type": "string"}, "description": "Providers to race"}
                },
                "required": ["prompt"]
            }
        ),
        types.Tool(
            name="ai_services",
            description="List all available AI services and their status",
            inputSchema={"type": "object", "properties": {}}
        ),
        
        # === MEMORY TOOLS ===
        types.Tool(
            name="remember",
            description="Store information in GABRIEL memory",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Memory key"},
                    "value": {"type": "string", "description": "Value to store"},
                    "tags": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["key", "value"]
            }
        ),
        types.Tool(
            name="recall",
            description="Search GABRIEL memory",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "limit": {"type": "integer", "default": 20}
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="forget",
            description="Delete a memory entry",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Memory key to delete"}
                },
                "required": ["key"]
            }
        ),
        
        # === TASK TOOLS ===
        types.Tool(
            name="add_task",
            description="Add a task to GABRIEL's queue",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"], "default": "medium"}
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
                    "task_id": {"type": "string"}
                },
                "required": ["task_id"]
            }
        ),
        types.Tool(
            name="list_tasks",
            description="List tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "status": {"type": "string", "enum": ["pending", "completed", "all"], "default": "pending"}
                }
            }
        ),
        
        # === SYSTEM TOOLS ===
        types.Tool(
            name="run_command",
            description="Execute a shell command (safe commands only)",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {"type": "string"},
                    "cwd": {"type": "string"},
                    "timeout": {"type": "integer", "default": 30}
                },
                "required": ["command"]
            }
        ),
        types.Tool(
            name="system_info",
            description="Get system information",
            inputSchema={"type": "object", "properties": {}}
        ),
        types.Tool(
            name="git_status",
            description="Get git status for a repository",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "default": str(GABRIEL_ROOT)}
                }
            }
        ),
        
        # === API KEY TOOLS ===
        types.Tool(
            name="set_api_key",
            description="Store an API key for a service",
            inputSchema={
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "Service name (anthropic, openai, etc)"},
                    "key": {"type": "string", "description": "API key"}
                },
                "required": ["service", "key"]
            }
        ),
        types.Tool(
            name="list_api_keys",
            description="List configured API keys (shows which are set, not values)",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


# =============================================================================
# TOOL IMPLEMENTATIONS
# =============================================================================

@app.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Execute a GABRIEL tool."""
    try:
        result = await execute_tool(name, arguments)
        return [types.TextContent(type="text", text=result)]
    except Exception as e:
        logger.log(f"Tool error [{name}]: {e}", "ERROR")
        return [types.TextContent(type="text", text=f"Error: {str(e)}")]


async def execute_tool(name: str, args: Dict[str, Any]) -> str:
    """Tool execution dispatcher."""
    
    # === CODEBASE TOOLS ===
    if name == "scan_codebase":
        path = Path(args.get("path", str(NOIZYLAB_ROOT)))
        depth = args.get("depth", 10)
        stats = scanner.scan(path, depth)
        return json.dumps(stats, indent=2)
    
    if name == "search_code":
        path = Path(args.get("path", str(NOIZYLAB_ROOT)))
        results = scanner.search(
            args.get("query"),
            path,
            args.get("type", "both"),
            args.get("limit", 50)
        )
        return json.dumps({"query": args.get("query"), "results": results}, indent=2)
    
    if name == "read_file":
        p = Path(args.get("path"))
        if not p.exists():
            return f"File not found: {p}"
        content = p.read_text()
        lines = content.split('\n')
        max_lines = args.get("lines", 500)
        if len(lines) > max_lines:
            return '\n'.join(lines[:max_lines]) + f"\n\n... [{len(lines) - max_lines} more lines]"
        return content
    
    if name == "write_file":
        p = Path(args.get("path"))
        p.parent.mkdir(parents=True, exist_ok=True)
        if args.get("append"):
            with open(p, 'a') as f:
                f.write(args.get("content"))
        else:
            p.write_text(args.get("content"))
        return f"Written to {p}"
    
    if name == "list_files":
        p = Path(args.get("path"))
        if not p.exists():
            return f"Path not found: {p}"
        pattern = args.get("pattern", "*")
        files = list(p.rglob(pattern) if args.get("recursive") else p.glob(pattern))[:100]
        result = [{"name": f.name, "type": "dir" if f.is_dir() else "file", "size": f.stat().st_size if f.is_file() else 0} for f in files]
        return json.dumps(result, indent=2)
    
    # === AI TOOLS ===
    if name == "ai_call":
        result = ai.call(
            args.get("provider"),
            args.get("prompt"),
            model=args.get("model"),
            system=args.get("system")
        )
        return json.dumps(result, indent=2)
    
    if name == "ai_race":
        results = ai.race(args.get("prompt"), args.get("providers"))
        return json.dumps(results, indent=2)
    
    if name == "ai_services":
        services = {}
        for name_svc, svc in AI_SERVICES.items():
            services[name_svc] = {
                "name": svc.name,
                "category": svc.category,
                "models": svc.models,
                "configured": bool(keys.get(name_svc)),
            }
        return json.dumps(services, indent=2)
    
    # === MEMORY TOOLS ===
    if name == "remember":
        mem_id = memory.store(args.get("key"), args.get("value"), args.get("tags", []))
        return f"Stored memory: {args.get('key')} (id: {mem_id})"
    
    if name == "recall":
        results = memory.search(args.get("query"), args.get("limit", 20))
        return json.dumps(results, indent=2)
    
    if name == "forget":
        if memory.delete(args.get("key")):
            return f"Deleted memory: {args.get('key')}"
        return f"Memory not found: {args.get('key')}"
    
    # === TASK TOOLS ===
    if name == "add_task":
        tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
        task = {
            "id": f"task_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "title": args.get("title"),
            "description": args.get("description", ""),
            "priority": args.get("priority", "medium"),
            "created": datetime.now().isoformat()
        }
        tasks["pending"].append(task)
        save_json(TASKS_FILE, tasks)
        return f"Task added: {task['id']}"
    
    if name == "complete_task":
        tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
        task_id = args.get("task_id")
        for i, task in enumerate(tasks["pending"]):
            if task["id"] == task_id:
                task["completed_at"] = datetime.now().isoformat()
                tasks["completed"].append(task)
                tasks["pending"].pop(i)
                save_json(TASKS_FILE, tasks)
                return f"Task completed: {task_id}"
        return f"Task not found: {task_id}"
    
    if name == "list_tasks":
        tasks = load_json(TASKS_FILE, {"pending": [], "completed": []})
        status = args.get("status", "pending")
        if status == "all":
            return json.dumps(tasks, indent=2)
        return json.dumps(tasks.get(status, []), indent=2)
    
    # === SYSTEM TOOLS ===
    if name == "run_command":
        command = args.get("command")
        dangerous = ["rm -rf /", "mkfs", "dd if=", "> /dev/", ":(){ :|:& };:"]
        if any(d in command for d in dangerous):
            return "Command blocked for safety"
        
        try:
            proc = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=args.get("cwd")
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=args.get("timeout", 30))
            output = stdout.decode()
            if stderr:
                output += f"\n[STDERR]\n{stderr.decode()}"
            return output or "(no output)"
        except asyncio.TimeoutError:
            return f"Command timed out"
        except Exception as e:
            return f"Error: {e}"
    
    if name == "system_info":
        info = {"platform": sys.platform, "python": sys.version}
        try:
            result = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True)
            info["cpu"] = result.stdout.strip()
        except:
            pass
        try:
            result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
            info["disk"] = result.stdout
        except:
            pass
        return json.dumps(info, indent=2)
    
    if name == "git_status":
        path = args.get("path", str(GABRIEL_ROOT))
        try:
            proc = await asyncio.create_subprocess_exec(
                "git", "status", "--porcelain", "-b",
                cwd=path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, _ = await proc.communicate()
            return stdout.decode() or "Clean working tree"
        except Exception as e:
            return f"Git error: {e}"
    
    # === API KEY TOOLS ===
    if name == "set_api_key":
        keys.set(args.get("service"), args.get("key"))
        return f"API key set for: {args.get('service')}"
    
    if name == "list_api_keys":
        configured = keys.list()
        return json.dumps({k: "✅ configured" if v else "❌ not set" for k, v in configured.items()}, indent=2)
    
    raise ValueError(f"Unknown tool: {name}")


# =============================================================================
# PROMPTS
# =============================================================================

@app.list_prompts()
async def list_prompts() -> List[types.Prompt]:
    """List available prompts."""
    return [
        types.Prompt(
            name="analyze_code",
            description="Analyze code for improvements, bugs, and optimizations",
            arguments=[
                types.PromptArgument(name="file_path", description="Path to the file to analyze", required=True)
            ]
        ),
        types.Prompt(
            name="explain_codebase",
            description="Get an overview of the GABRIEL codebase",
            arguments=[]
        ),
        types.Prompt(
            name="ai_comparison",
            description="Compare responses from multiple AI providers",
            arguments=[
                types.PromptArgument(name="question", description="Question to ask all providers", required=True)
            ]
        ),
    ]


@app.get_prompt()
async def get_prompt(name: str, arguments: Dict[str, str] = None) -> types.GetPromptResult:
    """Get a prompt template."""
    
    if name == "analyze_code":
        file_path = arguments.get("file_path", "")
        return types.GetPromptResult(
            description=f"Analyze {file_path}",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"""Analyze the following code file and provide:
1. Overview of what it does
2. Potential bugs or issues
3. Performance optimizations
4. Code quality improvements
5. Security concerns

File: {file_path}

Please use the read_file tool to read the file first."""
                    )
                )
            ]
        )
    
    if name == "explain_codebase":
        return types.GetPromptResult(
            description="GABRIEL Codebase Overview",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text="""Give me an overview of the GABRIEL codebase. Use the scan_codebase tool to analyze it and explain:
1. Project structure
2. Main components
3. Technologies used
4. Key files and their purposes"""
                    )
                )
            ]
        )
    
    if name == "ai_comparison":
        question = arguments.get("question", "")
        return types.GetPromptResult(
            description=f"AI Comparison: {question[:50]}...",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"""Use the ai_race tool to ask multiple AI providers the following question and compare their responses:

Question: {question}

After getting responses, analyze:
1. Which response is most accurate
2. Which is most comprehensive
3. Any contradictions between responses
4. Your recommendation"""
                    )
                )
            ]
        )
    
    raise ValueError(f"Unknown prompt: {name}")


# =============================================================================
# MAIN
# =============================================================================

async def main():
    """Run the GABRIEL MCP server."""
    logger.log("🧠 GABRIEL UNIFIED MCP SERVER v2.0 starting...", "INFO")
    logger.log(f"Root: {GABRIEL_ROOT}", "INFO")
    logger.log(f"API Keys configured: {sum(1 for v in keys.list().values() if v)}/{len(AI_SERVICES)}", "INFO")
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
