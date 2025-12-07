from typing import Dict, List
import time

FLEET_REGISTRY = {}


class FleetManager:
    """Manage hundreds of corporate devices"""

    def __init__(self, org_id: str):
        self.org_id = org_id
        if org_id not in FLEET_REGISTRY:
            FLEET_REGISTRY[org_id] = {
                "devices": {},
                "policies": {},
                "created": time.time()
            }
        self.fleet = FLEET_REGISTRY[org_id]

    def register_device(self, device_id: str, device_info: Dict) -> Dict:
        """Register a device in the fleet"""
        self.fleet["devices"][device_id] = {
            **device_info,
            "registered": time.time(),
            "status": "active",
            "health_score": 100,
            "last_seen": time.time()
        }
        return {"registered": True, "device_id": device_id}

    def get_device(self, device_id: str) -> Dict:
        return self.fleet["devices"].get(device_id, {})

    def list_devices(self) -> List[Dict]:
        return list(self.fleet["devices"].values())

    def update_health(self, device_id: str, score: int) -> Dict:
        if device_id in self.fleet["devices"]:
            self.fleet["devices"][device_id]["health_score"] = score
            self.fleet["devices"][device_id]["last_seen"] = time.time()
            return {"updated": True}
        return {"error": "device_not_found"}

    def get_unhealthy_devices(self, threshold: int = 70) -> List[Dict]:
        """Get devices below health threshold"""
        return [
            d for d in self.fleet["devices"].values()
            if d.get("health_score", 100) < threshold
        ]

    def fleet_stats(self) -> Dict:
        devices = list(self.fleet["devices"].values())
        return {
            "total_devices": len(devices),
            "healthy": len([d for d in devices if d.get("health_score", 100) >= 80]),
            "warning": len([d for d in devices if 50 <= d.get("health_score", 100) < 80]),
            "critical": len([d for d in devices if d.get("health_score", 100) < 50])
        }


def get_fleet(org_id: str) -> FleetManager:
    return FleetManager(org_id)

