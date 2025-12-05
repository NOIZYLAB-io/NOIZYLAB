"""
NoizyOS Ultra — NoizyGrid Controller
====================================
Central brain for distributed compute cluster.
Discovers nodes, routes tasks, manages load balancing.
"""

import httpx
from typing import List, Dict, Any, Optional
from datetime import datetime

# Node registry - configure your machines here
NODES = [
    {"ip": "192.168.1.20", "port": 8899, "name": "M2-Ultra", "role": "primary"},
    {"ip": "192.168.1.21", "port": 8899, "name": "Mac-Pro", "role": "secondary"},
    {"ip": "192.168.1.40", "port": 8899, "name": "HP-Omen", "role": "windows"},
]

# Task type to node specialization mapping
NODE_TYPES = {
    "ai_heavy": ["mac"],           # AI tasks go to Mac
    "ai_inference": ["mac"],       # AI inference on Mac
    "windows_diagnostics": ["windows"],  # Windows tasks to Omen
    "windows_repair": ["windows"],
    "game_testing": ["windows"],
    "video_encoding": ["mac"],
    "audio_processing": ["mac"],
    "general": ["mac", "windows"],  # Any node
}

# Cache for node status
node_cache: Dict[str, Dict] = {}
cache_timestamp: Optional[datetime] = None
CACHE_TTL_SECONDS = 5


async def discover_nodes() -> List[Dict[str, Any]]:
    """
    Discover all available nodes in the cluster.
    Returns list of node info dicts.
    """
    global node_cache, cache_timestamp
    
    # Check cache
    if cache_timestamp and (datetime.now() - cache_timestamp).seconds < CACHE_TTL_SECONDS:
        return list(node_cache.values())
    
    available = []
    
    async with httpx.AsyncClient(timeout=2.0) as client:
        for node in NODES:
            ip = node["ip"]
            port = node["port"]
            url = f"http://{ip}:{port}/info"
            
            try:
                r = await client.get(url)
                info = r.json()
                info["ip"] = ip
                info["port"] = port
                info["name"] = node.get("name", "Unknown")
                info["role"] = node.get("role", "general")
                info["status"] = "online"
                info["last_seen"] = datetime.now().isoformat()
                
                available.append(info)
                node_cache[ip] = info
                
            except httpx.ConnectError:
                # Node offline
                node_cache[ip] = {
                    "ip": ip,
                    "port": port,
                    "name": node.get("name", "Unknown"),
                    "status": "offline",
                    "last_seen": node_cache.get(ip, {}).get("last_seen")
                }
            except httpx.TimeoutException:
                node_cache[ip] = {
                    "ip": ip,
                    "port": port,
                    "name": node.get("name", "Unknown"),
                    "status": "timeout",
                    "last_seen": node_cache.get(ip, {}).get("last_seen")
                }
            except Exception as e:
                node_cache[ip] = {
                    "ip": ip,
                    "port": port,
                    "name": node.get("name", "Unknown"),
                    "status": "error",
                    "error": str(e)
                }
    
    cache_timestamp = datetime.now()
    return available


async def get_node_info(ip: str, port: int = 8899) -> Optional[Dict]:
    """Get info from a specific node."""
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            r = await client.get(f"http://{ip}:{port}/info")
            return r.json()
    except:
        return None


async def run_on_node(ip: str, task: str, payload: Optional[Dict] = None, port: int = 8899) -> Dict:
    """
    Execute a task on a specific node.
    
    Args:
        ip: Node IP address
        task: Task name/type
        payload: Optional task payload
        port: Node port (default 8899)
    
    Returns:
        Task result dict
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(
                f"http://{ip}:{port}/run",
                json={"task": task, "payload": payload or {}}
            )
            result = r.json()
            result["executed_on"] = ip
            return result
    except httpx.TimeoutException:
        return {"ok": False, "error": "Task timeout", "node": ip}
    except httpx.ConnectError:
        return {"ok": False, "error": "Node unreachable", "node": ip}
    except Exception as e:
        return {"ok": False, "error": str(e), "node": ip}


async def get_best_node_for_task(task: str) -> Optional[Dict]:
    """
    Find the best available node for a given task type.
    Uses NODE_TYPES mapping and current load.
    
    Args:
        task: Task type (e.g., "ai_heavy", "windows_diagnostics")
    
    Returns:
        Best node info dict, or None if no suitable node
    """
    nodes = await discover_nodes()
    
    if not nodes:
        return None
    
    # Get preferred OS types for this task
    preferred_types = NODE_TYPES.get(task, NODE_TYPES["general"])
    
    # Filter nodes by type and online status
    suitable = []
    for node in nodes:
        if node.get("status") != "online":
            continue
        
        node_type = node.get("type", "unknown").lower()
        if any(pref in node_type for pref in preferred_types):
            suitable.append(node)
    
    if not suitable:
        # Fallback to any online node
        suitable = [n for n in nodes if n.get("status") == "online"]
    
    if not suitable:
        return None
    
    # Sort by load (lowest CPU + RAM usage first)
    suitable.sort(key=lambda n: (n.get("cpu", 100) + n.get("ram", 100)))
    
    return suitable[0]


async def health_check_all() -> Dict[str, Any]:
    """
    Run health check on all nodes.
    Returns cluster health summary.
    """
    nodes = await discover_nodes()
    
    online = [n for n in nodes if n.get("status") == "online"]
    offline = [n for n in nodes if n.get("status") != "online"]
    
    # Calculate cluster load
    if online:
        avg_cpu = sum(n.get("cpu", 0) for n in online) / len(online)
        avg_ram = sum(n.get("ram", 0) for n in online) / len(online)
    else:
        avg_cpu = 0
        avg_ram = 0
    
    return {
        "total_nodes": len(NODES),
        "online": len(online),
        "offline": len(offline),
        "avg_cpu": round(avg_cpu, 1),
        "avg_ram": round(avg_ram, 1),
        "nodes": nodes,
        "healthy": len(online) > 0,
        "timestamp": datetime.now().isoformat()
    }


def add_node(ip: str, port: int = 8899, name: str = None, role: str = "general") -> bool:
    """Add a new node to the cluster."""
    for node in NODES:
        if node["ip"] == ip:
            return False  # Already exists
    
    NODES.append({
        "ip": ip,
        "port": port,
        "name": name or f"Node-{ip}",
        "role": role
    })
    return True


def remove_node(ip: str) -> bool:
    """Remove a node from the cluster."""
    global NODES
    original_len = len(NODES)
    NODES = [n for n in NODES if n["ip"] != ip]
    return len(NODES) < original_len

