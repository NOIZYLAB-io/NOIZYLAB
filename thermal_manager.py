"""NoizyGrid: Thermal Manager"""
from datetime import datetime

THERMALS = {"m2_ultra": {"cpu_temp": 45, "gpu_temp": 42, "max_safe": 85}, 
            "hp_omen": {"cpu_temp": 55, "gpu_temp": 60, "max_safe": 90},
            "mac_studio": {"cpu_temp": 40, "gpu_temp": 38, "max_safe": 85}}

def get_thermals():
    return THERMALS

def route_by_thermal(task):
    """Route task to coolest node"""
    coolest = min(THERMALS.items(), key=lambda x: x[1]["cpu_temp"])
    return {"node": coolest[0], "temp": coolest[1]["cpu_temp"]}

def is_thermal_safe(node):
    if node not in THERMALS: return False
    t = THERMALS[node]
    return t["cpu_temp"] < t["max_safe"] * 0.8 and t["gpu_temp"] < t["max_safe"] * 0.8

def update_thermal(node, cpu_temp=None, gpu_temp=None):
    if node in THERMALS:
        if cpu_temp: THERMALS[node]["cpu_temp"] = cpu_temp
        if gpu_temp: THERMALS[node]["gpu_temp"] = gpu_temp

def get_thermal_headroom():
    return {n: t["max_safe"] - max(t["cpu_temp"], t["gpu_temp"]) for n, t in THERMALS.items()}

