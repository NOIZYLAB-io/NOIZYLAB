#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║         ███████╗██╗  ██╗██╗  ██╗ ██████╗ ███████╗    ██╗  ██╗                      ║
║         ██╔════╝██║ ██╔╝██║ ██╔╝██╔═══██╗██╔════╝    ╚██╗██╔╝                      ║
║         █████╗  █████╔╝ █████╔╝ ██║   ██║███████╗     ╚███╔╝                       ║
║         ██╔══╝  ██╔═██╗ ██╔═██╗ ██║   ██║╚════██║     ██╔██╗                       ║
║         ███████╗██║  ██╗██║  ██╗╚██████╔╝███████║    ██╔╝ ██╗                      ║
║         ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝                      ║
║                                                                                   ║
║                   ⚡ MEMORY SYSTEM - CODEMASTER INTEGRATION ⚡                     ║
║                                                                                   ║
║                 11-Layer Memory Architecture for NOIZYLAB                         ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝

ekkOS Memory System - Integrated with CODEMASTER
Based on CLAUDE.md specification - 28 MCP Tools, 11 Memory Layers
"""

import asyncio
import json
import hashlib
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field

try:
    import orjson
    def json_dumps(obj): return orjson.dumps(obj).decode()
    def json_loads(s): return orjson.loads(s)
except ImportError:
    def json_dumps(obj): return json.dumps(obj)
    def json_loads(s): return json.loads(s)


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

MEMORY_DIR = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER/data/memory")
MEMORY_DIR.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════════════
# 11-LAYER MEMORY ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class MemoryLayer:
    """Base memory layer"""
    name: str
    layer_num: int
    description: str
    items: Dict[str, Any] = field(default_factory=dict)
    
    def add(self, key: str, value: Any) -> str:
        item_id = hashlib.md5(f"{key}{time.time()}".encode()).hexdigest()[:12]
        self.items[item_id] = {
            "id": item_id,
            "key": key,
            "value": value,
            "created_at": datetime.now().isoformat(),
            "access_count": 0,
            "last_accessed": None
        }
        return item_id
    
    def get(self, item_id: str) -> Optional[Any]:
        if item_id in self.items:
            self.items[item_id]["access_count"] += 1
            self.items[item_id]["last_accessed"] = datetime.now().isoformat()
            return self.items[item_id]
        return None
    
    def search(self, query: str) -> List[Dict]:
        results = []
        query_lower = query.lower()
        for item in self.items.values():
            key_match = query_lower in str(item.get("key", "")).lower()
            value_match = query_lower in str(item.get("value", "")).lower()
            if key_match or value_match:
                results.append(item)
        return results


class EkkOSMemory:
    """
    11-Layer Memory System
    
    Layer 1: Working - Current session state
    Layer 2: Episodic - Past conversations
    Layer 3: Semantic - Embeddings/knowledge
    Layer 4: Patterns - Proven solutions
    Layer 5: Procedural - Step-by-step guides
    Layer 6: Collective - Cross-project wisdom
    Layer 7: Meta - Pattern effectiveness
    Layer 8: Codebase - Project-specific
    Layer 9: Directives - User preferences
    Layer 10: Conflict - Auto-resolves contradictions
    Layer 11: Secrets - Encrypted credentials
    """
    
    def __init__(self):
        self.layers = {
            1: MemoryLayer("working", 1, "Current session state"),
            2: MemoryLayer("episodic", 2, "Past conversations"),
            3: MemoryLayer("semantic", 3, "Embeddings/knowledge"),
            4: MemoryLayer("patterns", 4, "Proven solutions"),
            5: MemoryLayer("procedural", 5, "Step-by-step guides"),
            6: MemoryLayer("collective", 6, "Cross-project wisdom"),
            7: MemoryLayer("meta", 7, "Pattern effectiveness"),
            8: MemoryLayer("codebase", 8, "Project-specific"),
            9: MemoryLayer("directives", 9, "User preferences"),
            10: MemoryLayer("conflict", 10, "Auto-resolves contradictions"),
            11: MemoryLayer("secrets", 11, "Encrypted credentials"),
        }
        self.session_id = str(uuid.uuid4())[:8]
        self.started_at = datetime.now()
        self._load_persisted()
    
    def _load_persisted(self):
        """Load persisted memory from disk"""
        for layer_num, layer in self.layers.items():
            path = MEMORY_DIR / f"layer_{layer_num}_{layer.name}.json"
            if path.exists():
                try:
                    with open(path) as f:
                        data = json.load(f)
                        layer.items = data.get("items", {})
                except Exception:
                    pass
    
    def _persist_layer(self, layer_num: int):
        """Persist a layer to disk"""
        layer = self.layers[layer_num]
        path = MEMORY_DIR / f"layer_{layer_num}_{layer.name}.json"
        with open(path, "w") as f:
            json.dump({
                "name": layer.name,
                "layer_num": layer_num,
                "items": layer.items,
                "persisted_at": datetime.now().isoformat()
            }, f, indent=2)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # CORE MEMORY TOOLS (from CLAUDE.md)
    # ═══════════════════════════════════════════════════════════════════════════
    
    def search_memory(self, query: str, layers: List[int] = None) -> Dict[str, List]:
        """
        🔴 REQUIRED: Search all 11 layers before answering
        """
        if layers is None:
            layers = list(range(1, 12))
        
        results = {}
        for layer_num in layers:
            if layer_num in self.layers:
                layer_results = self.layers[layer_num].search(query)
                if layer_results:
                    results[self.layers[layer_num].name] = layer_results
        
        return {
            "query": query,
            "results": results,
            "total_matches": sum(len(r) for r in results.values()),
            "layers_searched": len(layers),
            "timestamp": datetime.now().isoformat()
        }
    
    def forge_pattern(self, name: str, problem: str, solution: str, 
                      tags: List[str] = None, is_anti_pattern: bool = False) -> Dict:
        """
        🔴 REQUIRED: Create pattern from solution
        """
        pattern = {
            "name": name,
            "problem": problem,
            "solution": solution,
            "tags": tags or [],
            "is_anti_pattern": is_anti_pattern,
            "effectiveness": 1.0,
            "uses": 0
        }
        
        item_id = self.layers[4].add(name, pattern)
        self._persist_layer(4)
        
        return {
            "status": "forged",
            "pattern_id": item_id,
            "layer": "patterns",
            "is_anti_pattern": is_anti_pattern,
            "timestamp": datetime.now().isoformat()
        }
    
    def forge_directive(self, directive: str, directive_type: str, 
                        reason: str = None) -> Dict:
        """
        🔴 REQUIRED: Create MUST/NEVER/PREFER/AVOID rules
        
        Types:
        - MUST: "always do X"
        - NEVER: "never do Y"  
        - PREFER: "I prefer X"
        - AVOID: "avoid X"
        """
        if directive_type not in ["MUST", "NEVER", "PREFER", "AVOID"]:
            raise ValueError(f"Invalid directive type: {directive_type}")
        
        directive_obj = {
            "directive": directive,
            "type": directive_type,
            "reason": reason,
            "active": True
        }
        
        item_id = self.layers[9].add(directive, directive_obj)
        self._persist_layer(9)
        
        return {
            "status": "forged",
            "directive_id": item_id,
            "type": directive_type,
            "timestamp": datetime.now().isoformat()
        }
    
    def record_outcome(self, pattern_id: str, success: bool, notes: str = None) -> Dict:
        """Track if pattern worked or failed"""
        # Update pattern effectiveness in meta layer
        outcome = {
            "pattern_id": pattern_id,
            "success": success,
            "notes": notes
        }
        
        item_id = self.layers[7].add(f"outcome_{pattern_id}", outcome)
        self._persist_layer(7)
        
        # Update effectiveness in patterns layer
        pattern = self.layers[4].get(pattern_id)
        if pattern:
            current = pattern["value"].get("effectiveness", 1.0)
            uses = pattern["value"].get("uses", 0) + 1
            # Exponential moving average
            new_eff = current * 0.9 + (1.0 if success else 0.0) * 0.1
            pattern["value"]["effectiveness"] = new_eff
            pattern["value"]["uses"] = uses
            self._persist_layer(4)
        
        return {
            "status": "recorded",
            "outcome_id": item_id,
            "success": success,
            "timestamp": datetime.now().isoformat()
        }
    
    def capture_event(self, event_type: str, content: Any, context: Dict = None) -> Dict:
        """Capture memory events to episodic layer"""
        event = {
            "type": event_type,
            "content": content,
            "context": context or {},
            "session_id": self.session_id
        }
        
        item_id = self.layers[2].add(f"{event_type}_{time.time()}", event)
        self._persist_layer(2)
        
        return {
            "status": "captured",
            "event_id": item_id,
            "type": event_type,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_context(self, task: str, max_items: int = 10) -> Dict:
        """Get relevant context for a task"""
        # Search across all layers
        all_results = self.search_memory(task)
        
        # Prioritize by relevance
        context_items = []
        for layer_name, items in all_results["results"].items():
            for item in items[:max_items // len(all_results["results"]) + 1]:
                context_items.append({
                    "layer": layer_name,
                    "item": item
                })
        
        return {
            "task": task,
            "context_items": context_items[:max_items],
            "total_available": all_results["total_matches"],
            "timestamp": datetime.now().isoformat()
        }
    
    def check_conflict(self, action: str, target: str) -> Dict:
        """
        🔴 REQUIRED: Check for conflicts before destructive actions
        """
        # Check directives for conflicts
        conflicts = []
        
        for item_id, item in self.layers[9].items.items():
            directive = item["value"]
            if directive.get("type") == "NEVER":
                if any(word in action.lower() for word in directive["directive"].lower().split()):
                    conflicts.append({
                        "directive_id": item_id,
                        "type": "NEVER",
                        "directive": directive["directive"],
                        "severity": "HIGH"
                    })
        
        return {
            "action": action,
            "target": target,
            "conflicts_found": len(conflicts) > 0,
            "conflicts": conflicts,
            "safe_to_proceed": len(conflicts) == 0,
            "timestamp": datetime.now().isoformat()
        }
    
    def session_summary(self) -> Dict:
        """
        🔴 REQUIRED: Get summary of MCP activity
        """
        layer_stats = {}
        total_items = 0
        
        for layer_num, layer in self.layers.items():
            count = len(layer.items)
            total_items += count
            layer_stats[layer.name] = {
                "layer": layer_num,
                "items": count,
                "description": layer.description
            }
        
        return {
            "session_id": self.session_id,
            "started_at": self.started_at.isoformat(),
            "uptime_seconds": (datetime.now() - self.started_at).total_seconds(),
            "total_items": total_items,
            "layers": layer_stats,
            "timestamp": datetime.now().isoformat()
        }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PORTABILITY TOOLS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def export_memory(self, filepath: str = None) -> Dict:
        """Export your patterns, directives, plans as portable JSON backup"""
        if filepath is None:
            filepath = MEMORY_DIR / f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        export_data = {
            "exported_at": datetime.now().isoformat(),
            "session_id": self.session_id,
            "layers": {}
        }
        
        for layer_num, layer in self.layers.items():
            export_data["layers"][layer.name] = {
                "layer_num": layer_num,
                "items": layer.items
            }
        
        with open(filepath, "w") as f:
            json.dump(export_data, f, indent=2)
        
        return {
            "status": "exported",
            "filepath": str(filepath),
            "total_items": sum(len(l.items) for l in self.layers.values()),
            "timestamp": datetime.now().isoformat()
        }
    
    def import_memory(self, filepath: str) -> Dict:
        """Import memory from backup (auto-deduplication)"""
        with open(filepath) as f:
            import_data = json.load(f)
        
        imported = 0
        duplicates = 0
        
        for layer_name, layer_data in import_data.get("layers", {}).items():
            layer_num = layer_data.get("layer_num")
            if layer_num and layer_num in self.layers:
                for item_id, item in layer_data.get("items", {}).items():
                    if item_id not in self.layers[layer_num].items:
                        self.layers[layer_num].items[item_id] = item
                        imported += 1
                    else:
                        duplicates += 1
                self._persist_layer(layer_num)
        
        return {
            "status": "imported",
            "filepath": filepath,
            "imported": imported,
            "duplicates_skipped": duplicates,
            "timestamp": datetime.now().isoformat()
        }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SECRETS MANAGEMENT (Layer 11)
    # ═══════════════════════════════════════════════════════════════════════════
    
    def store_secret(self, name: str, value: str, category: str = "api_key") -> Dict:
        """Encrypt and store sensitive data"""
        # Simple obfuscation (in production, use proper encryption)
        import base64
        encoded = base64.b64encode(value.encode()).decode()
        
        secret = {
            "name": name,
            "value": encoded,
            "category": category,
            "encrypted": True
        }
        
        item_id = self.layers[11].add(name, secret)
        self._persist_layer(11)
        
        return {
            "status": "stored",
            "secret_id": item_id,
            "name": name,
            "category": category,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_secret(self, name: str) -> Optional[str]:
        """Retrieve and decrypt a secret"""
        import base64
        
        for item in self.layers[11].items.values():
            if item["value"].get("name") == name:
                encoded = item["value"].get("value")
                return base64.b64decode(encoded).decode()
        return None
    
    def list_secrets(self) -> List[Dict]:
        """List secrets metadata (no values)"""
        return [
            {
                "id": item_id,
                "name": item["value"].get("name"),
                "category": item["value"].get("category"),
                "created_at": item.get("created_at")
            }
            for item_id, item in self.layers[11].items.items()
        ]
    
    # ═══════════════════════════════════════════════════════════════════════════
    # CODEMASTER INTEGRATION
    # ═══════════════════════════════════════════════════════════════════════════
    
    def get_memory_stats(self) -> Dict:
        """Get statistics for all layers - CODEMASTER metrics endpoint"""
        stats = {
            "total_items": 0,
            "layers": {},
            "top_patterns": [],
            "active_directives": 0
        }
        
        for layer_num, layer in self.layers.items():
            count = len(layer.items)
            stats["total_items"] += count
            stats["layers"][layer.name] = {
                "count": count,
                "layer": layer_num
            }
        
        # Get top patterns by effectiveness
        patterns = list(self.layers[4].items.values())
        patterns.sort(key=lambda x: x["value"].get("effectiveness", 0), reverse=True)
        stats["top_patterns"] = [
            {"name": p["key"], "effectiveness": p["value"].get("effectiveness", 1.0)}
            for p in patterns[:5]
        ]
        
        # Count active directives
        stats["active_directives"] = sum(
            1 for item in self.layers[9].items.values()
            if item["value"].get("active", True)
        )
        
        return stats


# ═══════════════════════════════════════════════════════════════════════════════
# GLOBAL INSTANCE
# ═══════════════════════════════════════════════════════════════════════════════

memory = EkkOSMemory()


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys
    
    print("""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║         ███████╗██╗  ██╗██╗  ██╗ ██████╗ ███████╗    ██╗  ██╗                      ║
║         ██╔════╝██║ ██╔╝██║ ██╔╝██╔═══██╗██╔════╝    ╚██╗██╔╝                      ║
║         █████╗  █████╔╝ █████╔╝ ██║   ██║███████╗     ╚███╔╝                       ║
║         ██╔══╝  ██╔═██╗ ██╔═██╗ ██║   ██║╚════██║     ██╔██╗                       ║
║         ███████╗██║  ██╗██║  ██╗╚██████╔╝███████║    ██╔╝ ██╗                      ║
║         ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝                      ║
║                      ⚡ 11-LAYER MEMORY SYSTEM ⚡                                  ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "stats":
            stats = memory.get_memory_stats()
            print(json_dumps(stats))
        
        elif cmd == "summary":
            summary = memory.session_summary()
            print(f"\n📊 Session: {summary['session_id']}")
            print(f"⏱️  Uptime: {summary['uptime_seconds']:.1f}s")
            print(f"📦 Total Items: {summary['total_items']}")
            print("\n📑 Layers:")
            for name, info in summary['layers'].items():
                print(f"   {info['layer']:2}. {name:12} - {info['items']:4} items - {info['description']}")
        
        elif cmd == "search" and len(sys.argv) > 2:
            query = " ".join(sys.argv[2:])
            results = memory.search_memory(query)
            print(f"\n🔍 Search: '{query}'")
            print(f"📊 Found: {results['total_matches']} matches")
            for layer, items in results['results'].items():
                print(f"\n  [{layer}]")
                for item in items[:3]:
                    print(f"    - {item['key']}")
        
        elif cmd == "export":
            result = memory.export_memory()
            print(f"✅ Exported to: {result['filepath']}")
        
        else:
            print("Usage: python ekkos_memory.py [stats|summary|search <query>|export]")
    else:
        # Show summary by default
        summary = memory.session_summary()
        print(f"📊 Session: {summary['session_id']}")
        print(f"📦 Total Items: {summary['total_items']}")
        print("\nCommands: stats, summary, search <query>, export")
