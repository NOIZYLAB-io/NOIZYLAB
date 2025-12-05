"""Decision Engine: Agent Router - Routes to 25 NoizyGeniuses"""
from datetime import datetime

AGENTS = {
    "logic": {"id": "genius_logic", "specialty": "reasoning", "active": True},
    "vision": {"id": "genius_vision", "specialty": "visual_analysis", "active": True},
    "voice": {"id": "genius_voice", "specialty": "speech", "active": True},
    "compute": {"id": "genius_compute", "specialty": "processing", "active": True},
    "shield": {"id": "genius_shield", "specialty": "security", "active": True},
    "flow": {"id": "genius_flow", "specialty": "automation", "active": True},
    "calm": {"id": "genius_calm", "specialty": "wellness", "active": True},
    "design": {"id": "genius_design", "specialty": "creative", "active": True},
    "memory": {"id": "genius_memory", "specialty": "recall", "active": True},
    "time": {"id": "genius_time", "specialty": "scheduling", "active": True},
    "task": {"id": "genius_task", "specialty": "management", "active": True},
    "chat": {"id": "genius_chat", "specialty": "conversation", "active": True},
    "home": {"id": "genius_home", "specialty": "environment", "active": True},
    "drive": {"id": "genius_drive", "specialty": "storage", "active": True},
    "repair": {"id": "genius_repair", "specialty": "diagnostics", "active": True},
    "economy": {"id": "genius_economy", "specialty": "business", "active": True},
    "desk": {"id": "genius_desk", "specialty": "reception", "active": True},
    "grid": {"id": "genius_grid", "specialty": "cluster", "active": True},
    "assist": {"id": "genius_assist", "specialty": "accessibility", "active": True},
    "improve": {"id": "genius_improve", "specialty": "optimization", "active": True},
}

ROUTING_LOG = []

def route_to_agent(task_type):
    """Route task to appropriate agent"""
    routing = {
        "repair": "repair", "diagnostic": "repair", "security": "shield", "threat": "shield",
        "schedule": "time", "calendar": "time", "task": "task", "todo": "task",
        "chat": "chat", "message": "chat", "file": "drive", "storage": "drive",
        "compute": "compute", "gpu": "compute", "stress": "calm", "relax": "calm",
        "business": "economy", "invoice": "economy", "client": "desk", "booking": "desk",
        "cluster": "grid", "voice": "assist", "click": "assist", "memory": "memory",
    }
    
    agent_key = routing.get(task_type.lower(), "logic")
    agent = AGENTS.get(agent_key, AGENTS["logic"])
    
    ROUTING_LOG.append({"task": task_type, "agent": agent["id"], "timestamp": datetime.now().isoformat()})
    return agent

def get_agents():
    return AGENTS

def get_agent(name):
    return AGENTS.get(name)

def get_routing_log():
    return ROUTING_LOG[-50:]

