"""NoizyGrid++ GPU/CPU Sharding"""
SHARDS = {}

def shard_workload(job_id, workload, nodes):
    shard_size = len(workload) // len(nodes) if nodes else len(workload)
    for i, node in enumerate(nodes):
        start = i * shard_size
        end = start + shard_size if i < len(nodes) - 1 else len(workload)
        SHARDS[f"{job_id}_{node}"] = {"node": node, "data": workload[start:end]}
    return list(SHARDS.keys())

def get_shard_status(shard_id=None):
    if shard_id:
        return SHARDS.get(shard_id)
    return SHARDS

