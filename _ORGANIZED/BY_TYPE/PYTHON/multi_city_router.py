from typing import Dict, Optional
from .global_registry import registry

CITY_CONFIGS = {
    "ottawa": {
        "country": "CA",
        "timezone": "America/Toronto",
        "language": ["en", "fr"],
        "emergency": "911",
        "accessibility_hotline": "211"
    },
    "toronto": {
        "country": "CA",
        "timezone": "America/Toronto",
        "language": ["en"],
        "emergency": "911",
        "accessibility_hotline": "211"
    },
    "vancouver": {
        "country": "CA",
        "timezone": "America/Vancouver",
        "language": ["en"],
        "emergency": "911",
        "accessibility_hotline": "211"
    },
    "nyc": {
        "country": "US",
        "timezone": "America/New_York",
        "language": ["en", "es"],
        "emergency": "911",
        "accessibility_hotline": "311"
    },
    "london": {
        "country": "UK",
        "timezone": "Europe/London",
        "language": ["en"],
        "emergency": "999",
        "accessibility_hotline": "116123"
    }
}


class MultiCityRouter:
    def __init__(self):
        self.cities = CITY_CONFIGS

    def route_request(self, city_id: str, request_type: str) -> Dict:
        """Route a request to the appropriate city handler"""
        if city_id not in self.cities:
            return {"error": "city_not_found", "available": list(self.cities.keys())}

        config = self.cities[city_id]
        return {
            "city": city_id,
            "config": config,
            "request_type": request_type,
            "routed": True
        }

    def get_city_config(self, city_id: str) -> Optional[Dict]:
        return self.cities.get(city_id)

    def get_emergency_number(self, city_id: str) -> str:
        config = self.cities.get(city_id, {})
        return config.get("emergency", "911")

    def get_accessibility_line(self, city_id: str) -> str:
        config = self.cities.get(city_id, {})
        return config.get("accessibility_hotline", "211")

    def list_cities(self) -> Dict:
        return {
            "cities": list(self.cities.keys()),
            "count": len(self.cities)
        }

    def add_city(self, city_id: str, config: Dict) -> Dict:
        self.cities[city_id] = config
        registry.register_city(city_id, config.get("country", "XX"), config)
        return {"added": True, "city_id": city_id}


router = MultiCityRouter()

