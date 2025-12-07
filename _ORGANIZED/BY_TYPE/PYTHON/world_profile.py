import json
import time
from typing import Dict, List, Optional

WORLD_PROFILES = {}


class WorldProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self._load()

    def _load(self):
        if self.user_id in WORLD_PROFILES:
            self.data = WORLD_PROFILES[self.user_id]
        else:
            self.data = {
                "user_id": self.user_id,
                "created": time.time(),
                "devices": [],
                "cities": [],
                "accessibility": {},
                "preferences": {},
                "repair_history": [],
                "ai_memory": {}
            }
            WORLD_PROFILES[self.user_id] = self.data

    def add_device(self, device_id: str, device_type: str) -> Dict:
        self.data["devices"].append({
            "id": device_id,
            "type": device_type,
            "added": time.time()
        })
        return {"added": True}

    def add_city(self, city_id: str) -> Dict:
        if city_id not in self.data["cities"]:
            self.data["cities"].append(city_id)
        return {"cities": self.data["cities"]}

    def set_accessibility(self, settings: Dict) -> Dict:
        self.data["accessibility"] = {**self.data["accessibility"], **settings}
        return self.data["accessibility"]

    def add_repair(self, repair_data: Dict) -> Dict:
        repair_data["timestamp"] = time.time()
        self.data["repair_history"].append(repair_data)
        return {"logged": True}

    def set_ai_memory(self, key: str, value: any) -> Dict:
        self.data["ai_memory"][key] = value
        return {"stored": True}

    def get_ai_memory(self, key: str) -> Optional[any]:
        return self.data["ai_memory"].get(key)

    def export(self) -> Dict:
        return self.data


def get_profile(user_id: str) -> WorldProfile:
    return WorldProfile(user_id)

