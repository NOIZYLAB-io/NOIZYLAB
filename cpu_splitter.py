"""NoizyGrid: CPU Task Splitter"""
from datetime import datetime

CPU_STATUS = {"m2_ultra": {"cores": 24, "load": 0.2}, "hp_omen": {"cores": 16, "load": 0.4}, "mac_studio": {"cores": 12, "load": 0.1}}
SPLITS = []

def split_task(task, parts=None):
    """Split CPU task across nodes"""
    if parts is None: parts = len([n for n, s in CPU_STATUS.items() if s["load"] < 0.7])
    if parts == 0: return {"error": "All CPUs overloaded"}
    
    available = sorted([(n, s) for n, s in CPU_STATUS.items() if s["load"] < 0.7], key=lambda x: x[1]["load"])
    splits = []
    for i, (node, status) in enumerate(available[:parts]):
        split = {"task_id": task.get("id"), "part": i, "node": node, "cores_assigned": status["cores"] // parts, "created_at": datetime.now().isoformat()}
        splits.append(split)
        SPLITS.append(split)
    return {"task": task, "splits": splits}

def get_cpu_status():
    return CPU_STATUS

def update_cpu_load(node, load):
    if node in CPU_STATUS: CPU_STATUS[node]["load"] = load

def get_total_cores():
    return sum(s["cores"] for s in CPU_STATUS.values())

def get_available_cores():
    return sum(int(s["cores"] * (1 - s["load"])) for s in CPU_STATUS.values())

