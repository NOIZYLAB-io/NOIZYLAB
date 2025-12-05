from typing import Dict, List, Callable

GENIUS_REGISTRY = {}


class NoizyGenius:
    def __init__(self, genius_id: int, name: str, domain: str):
        self.genius_id = genius_id
        self.name = name
        self.domain = domain
        self.weight = 1.0
        self.active = True

    def think(self, context: Dict) -> Dict:
        """Override in subclasses"""
        return {"genius": self.name, "thought": "base thinking"}

    def can_handle(self, intent: str) -> float:
        """Return confidence 0-1 for handling this intent"""
        return 0.0


# The 25 NoizyGeniuses
GENIUSES = [
    {"id": 1, "name": "NetworkGenius", "domain": "network"},
    {"id": 2, "name": "OSInternalsGenius", "domain": "os"},
    {"id": 3, "name": "AccessibilityGenius", "domain": "accessibility"},
    {"id": 4, "name": "VoiceGenius", "domain": "voice"},
    {"id": 5, "name": "PsychologyGenius", "domain": "psychology"},
    {"id": 6, "name": "ComfortGenius", "domain": "comfort"},
    {"id": 7, "name": "PCHardwareGenius", "domain": "pc_hardware"},
    {"id": 8, "name": "macOSGenius", "domain": "macos"},
    {"id": 9, "name": "ElectronicsGenius", "domain": "electronics"},
    {"id": 10, "name": "SecurityGenius", "domain": "security"},
    {"id": 11, "name": "StorageGenius", "domain": "storage"},
    {"id": 12, "name": "PerformanceGenius", "domain": "performance"},
    {"id": 13, "name": "MobileGenius", "domain": "mobile"},
    {"id": 14, "name": "CloudGenius", "domain": "cloud"},
    {"id": 15, "name": "PrinterGenius", "domain": "printers"},
    {"id": 16, "name": "AudioGenius", "domain": "audio"},
    {"id": 17, "name": "VideoGenius", "domain": "video"},
    {"id": 18, "name": "GamingGenius", "domain": "gaming"},
    {"id": 19, "name": "BusinessGenius", "domain": "business"},
    {"id": 20, "name": "HomeAutomationGenius", "domain": "smart_home"},
    {"id": 21, "name": "DataRecoveryGenius", "domain": "data_recovery"},
    {"id": 22, "name": "VirusRemovalGenius", "domain": "malware"},
    {"id": 23, "name": "SetupGenius", "domain": "setup"},
    {"id": 24, "name": "TrainingGenius", "domain": "training"},
    {"id": 25, "name": "CivicGenius", "domain": "civic"},
]


def get_genius(genius_id: int) -> Dict:
    for g in GENIUSES:
        if g["id"] == genius_id:
            return g
    return None


def get_geniuses_for_domain(domain: str) -> List[Dict]:
    return [g for g in GENIUSES if g["domain"] == domain]


def list_all_geniuses() -> List[Dict]:
    return GENIUSES

