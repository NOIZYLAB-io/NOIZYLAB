"""
NoizyOS Ultra — NoizyGrid API Routes
====================================
REST endpoints for distributed cluster management.
"""

from fastapi import APIRouter
from ..noizygrid.grid_controller import (
    discover_nodes, run_on_node, get_node_info,
    get_best_node_for_task, health_check_all,
    add_node, remove_node, NODES
)

router = APIRouter()


@router.get("/nodes")
async def list_nodes():
    """Get all nodes in the cluster with current status."""
    nodes = await discover_nodes()
    return {"nodes": nodes, "count": len(nodes)}


@router.get("/health")
async def cluster_health():
    """Get cluster health summary."""
    return await health_check_all()


@router.get("/node/{ip}")
async def get_single_node(ip: str):
    """Get info for a specific node."""
    info = await get_node_info(ip)
    if info:
        return {"node": info}
    return {"error": "Node not found or offline"}


@router.post("/run")
async def run_task(payload: dict):
    """
    Run a task on the cluster.
    
    Payload:
        task: Task type (required)
        target: Target node IP (optional - auto-selects if not provided)
        payload: Task-specific data (optional)
    """
    task = payload.get("task")
    target_ip = payload.get("target")
    task_payload = payload.get("payload", {})
    
    if not task:
        return {"ok": False, "error": "Task required"}
    
    # Auto-select best node if no target specified
    if not target_ip:
        best_node = await get_best_node_for_task(task)
        if not best_node:
            return {"ok": False, "error": "No suitable node available"}
        target_ip = best_node["ip"]
        target_port = best_node.get("port", 8899)
    else:
        target_port = 8899
    
    # Execute task
    result = await run_on_node(target_ip, task, task_payload, target_port)
    result["routed_to"] = target_ip
    
    return result


@router.post("/run/{ip}")
async def run_on_specific_node(ip: str, payload: dict):
    """Run a task on a specific node by IP."""
    task = payload.get("task")
    task_payload = payload.get("payload", {})
    port = payload.get("port", 8899)
    
    if not task:
        return {"ok": False, "error": "Task required"}
    
    return await run_on_node(ip, task, task_payload, port)


@router.post("/broadcast")
async def broadcast_task(payload: dict):
    """Run a task on ALL online nodes."""
    task = payload.get("task")
    task_payload = payload.get("payload", {})
    
    if not task:
        return {"ok": False, "error": "Task required"}
    
    nodes = await discover_nodes()
    online_nodes = [n for n in nodes if n.get("status") == "online"]
    
    results = []
    for node in online_nodes:
        result = await run_on_node(node["ip"], task, task_payload, node.get("port", 8899))
        results.append(result)
    
    return {
        "ok": True,
        "task": task,
        "node_count": len(online_nodes),
        "results": results
    }


@router.get("/best/{task}")
async def find_best_node(task: str):
    """Find the best node for a given task type."""
    node = await get_best_node_for_task(task)
    if node:
        return {"node": node}
    return {"error": "No suitable node found"}


@router.post("/add")
def add_new_node(payload: dict):
    """Add a new node to the cluster."""
    ip = payload.get("ip")
    port = payload.get("port", 8899)
    name = payload.get("name")
    role = payload.get("role", "general")
    
    if not ip:
        return {"ok": False, "error": "IP required"}
    
    success = add_node(ip, port, name, role)
    return {"ok": success, "message": "Added" if success else "Already exists"}


@router.delete("/remove/{ip}")
def remove_existing_node(ip: str):
    """Remove a node from the cluster."""
    success = remove_node(ip)
    return {"ok": success, "message": "Removed" if success else "Not found"}


@router.get("/config")
def get_cluster_config():
    """Get current cluster configuration."""
    return {
        "nodes": NODES,
        "count": len(NODES)
    }

