import json, os
from datetime import datetime

agents = ["Strategist", "Healer", "Archivist", "Visionary"]
capsule = {
    "timestamp": datetime.now().isoformat(),
    "agents": agents,
    "rituals": ["overlay_launch", "capsule_build", "slab_scan"],
    "sequoia_logic": "Vertical agent orchestration + capsule economy"
}

with open(os.path.expanduser("~/NoizyFish/Legacy/sequoia_infusion_log.json"), "w") as f:
    json.dump(capsule, f, indent=4)

print("🧞 Sequoia infusion complete. Agents are glowing.")
