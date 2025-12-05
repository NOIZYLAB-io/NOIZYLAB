import time
from typing import Dict, List, Optional

GLOBAL_NODES = {}
GLOBAL_CITIES = {}


class GlobalRegistry:
    def __init__(self):
        self.nodes = GLOBAL_NODES
        self.cities = GLOBAL_CITIES

    def register_node(self, node_id: str, node_type: str, city: str) -> Dict:
        """Register a NoizyOS node in the global network"""
        self.nodes[node_id] = {
            "type": node_type,  # consumer, business, enterprise, government
            "city": city,
            "registered": time.time(),
            "status": "online",
            "last_heartbeat": time.time()
        }
        return {"registered": True, "node_id": node_id}

    def register_city(self, city_id: str, country: str, config: Dict) -> Dict:
        """Register a city in the NoizyGrid"""
        self.cities[city_id] = {
            "country": country,
            "config": config,
            "activated": time.time(),
            "nodes": 0,
            "status": "active"
        }
        return {"registered": True, "city_id": city_id}

    def heartbeat(self, node_id: str) -> Dict:
        """Node heartbeat to maintain online status"""
        if node_id in self.nodes:
            self.nodes[node_id]["last_heartbeat"] = time.time()
            self.nodes[node_id]["status"] = "online"
            return {"ack": True}
        return {"ack": False, "error": "node_not_found"}

    def get_city_nodes(self, city: str) -> List[str]:
        """Get all nodes in a city"""
        return [nid for nid, data in self.nodes.items() if data["city"] == city]

    def get_online_nodes(self) -> List[str]:
        """Get all online nodes globally"""
        now = time.time()
        return [nid for nid, data in self.nodes.items() 
                if now - data["last_heartbeat"] < 300]  # 5 min timeout


registry = GlobalRegistry()

