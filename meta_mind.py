from typing import Dict, List
from .genius_registry import GENIUSES

# Domain keyword mappings
DOMAIN_KEYWORDS = {
    "network": ["wifi", "internet", "connection", "router", "ethernet", "dns", "ip"],
    "os": ["windows", "macos", "linux", "update", "boot", "crash", "freeze"],
    "accessibility": ["blind", "deaf", "motor", "disability", "accessible", "simple"],
    "voice": ["speak", "voice", "listen", "microphone", "speech"],
    "psychology": ["stressed", "anxious", "worried", "scared", "overwhelmed"],
    "comfort": ["help", "confused", "lost", "don't know"],
    "pc_hardware": ["cpu", "ram", "motherboard", "gpu", "power supply", "fan"],
    "macos": ["mac", "apple", "finder", "spotlight", "time machine"],
    "electronics": ["circuit", "solder", "component", "capacitor", "resistor"],
    "security": ["virus", "hack", "password", "encrypt", "firewall", "malware"],
    "storage": ["ssd", "hdd", "drive", "storage", "backup", "raid"],
    "performance": ["slow", "lag", "speed", "optimize", "fast"],
    "mobile": ["phone", "iphone", "android", "tablet", "app"],
    "cloud": ["sync", "backup", "cloud", "dropbox", "icloud", "onedrive"],
    "printers": ["print", "printer", "scanner", "ink", "paper jam"],
    "audio": ["sound", "speaker", "audio", "music", "headphone"],
    "video": ["display", "monitor", "screen", "resolution", "hdmi"],
    "gaming": ["game", "fps", "graphics", "steam", "controller"],
    "business": ["invoice", "client", "schedule", "productivity"],
    "smart_home": ["alexa", "google home", "smart", "iot", "automation"],
    "data_recovery": ["recover", "deleted", "lost files", "restore"],
    "malware": ["virus", "trojan", "ransomware", "spyware", "infected"],
    "setup": ["install", "setup", "configure", "new device"],
    "training": ["learn", "how to", "teach", "tutorial", "guide"],
    "civic": ["city", "government", "public", "citizen", "community"],
}


class MetaMind:
    def __init__(self):
        self.geniuses = GENIUSES
        self.domain_map = DOMAIN_KEYWORDS

    def analyze_intent(self, text: str) -> Dict[str, float]:
        """Analyze text and return domain confidence scores"""
        text_lower = text.lower()
        scores = {}

        for domain, keywords in self.domain_map.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[domain] = min(score / len(keywords) * 2, 1.0)

        return scores

    def select_geniuses(self, text: str, top_n: int = 3) -> List[Dict]:
        """Select the best geniuses for this input"""
        scores = self.analyze_intent(text)
        
        if not scores:
            # Default to comfort + accessibility
            return [g for g in self.geniuses if g["domain"] in ["comfort", "accessibility"]]

        # Sort by score
        sorted_domains = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_domains = [d[0] for d in sorted_domains[:top_n]]

        return [g for g in self.geniuses if g["domain"] in top_domains]

    def parallel_think(self, text: str) -> List[Dict]:
        """Run parallel thinking across selected geniuses"""
        selected = self.select_geniuses(text)
        thoughts = []

        for genius in selected:
            thoughts.append({
                "genius_id": genius["id"],
                "genius_name": genius["name"],
                "domain": genius["domain"],
                "thought": f"[{genius['name']}] analyzing: {text[:50]}..."
            })

        return thoughts


meta_mind = MetaMind()

