"""NoizyGrid: GPU Sharding"""
from datetime import datetime

GPU_STATUS = {"m2_ultra": {"vram_total": 192, "vram_used": 24, "utilization": 0.15},
              "hp_omen": {"vram_total": 12, "vram_used": 4, "utilization": 0.3}}

SHARDS = []

def shard_task(task, shard_count=2):
    """Shard a GPU task across nodes"""
    available_gpus = [n for n, s in GPU_STATUS.items() if s["utilization"] < 0.8]
    if len(available_gpus) < shard_count: shard_count = len(available_gpus)
    if shard_count == 0: return {"error": "No GPU capacity"}
    
    shards = []
    for i, gpu in enumerate(available_gpus[:shard_count]):
        shard = {"task_id": task.get("id"), "shard_index": i, "node": gpu, "created_at": datetime.now().isoformat()}
        shards.append(shard)
        SHARDS.append(shard)
    return {"task": task, "shards": shards}

def get_gpu_status():
    return GPU_STATUS

def update_gpu_status(node, vram_used=None, utilization=None):
    if node in GPU_STATUS:
        if vram_used is not None: GPU_STATUS[node]["vram_used"] = vram_used
        if utilization is not None: GPU_STATUS[node]["utilization"] = utilization

def get_available_vram():
    return {n: s["vram_total"] - s["vram_used"] for n, s in GPU_STATUS.items()}

