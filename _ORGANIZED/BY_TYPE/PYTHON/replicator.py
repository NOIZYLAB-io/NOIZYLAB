"""NoizySync++ State Replicator - CRDT-style conflict-free sync"""
import time
from datetime import datetime

NODES = {}
STATE_VECTOR = {}

def register_node(node_id, endpoint):
    NODES[node_id] = {"endpoint": endpoint, "last_seen": datetime.now().isoformat(), "state": {}}

def replicate_state(node_id, state):
    STATE_VECTOR[node_id] = {"state": state, "timestamp": time.time()}
    return merge_states()

def merge_states():
    merged = {}
    for node_id, data in STATE_VECTOR.items():
        for k, v in data["state"].items():
            if k not in merged or data["timestamp"] > merged[k]["ts"]:
                merged[k] = {"value": v, "ts": data["timestamp"], "source": node_id}
    return {k: v["value"] for k, v in merged.items()}

def sync_all_nodes():
    return merge_states()

def get_node_status():
    return {nid: {"endpoint": n["endpoint"], "last_seen": n["last_seen"]} for nid, n in NODES.items()}

