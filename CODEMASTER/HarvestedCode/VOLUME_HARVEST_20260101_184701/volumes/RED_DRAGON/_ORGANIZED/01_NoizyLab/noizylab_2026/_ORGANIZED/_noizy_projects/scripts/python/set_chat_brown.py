import json
import os

# Path to VS Code user settings.json
settings_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")

# Load existing settings
if os.path.exists(settings_path):
    with open(settings_path, "r") as f:
        try:
            settings = json.load(f)
        except Exception:
            settings = {}
else:
    settings = {}

# Set chat background to loud brown
color_customizations = settings.get("workbench.colorCustomizations", {})
color_customizations["chat.background"] = "#4B2E19"
settings["workbench.colorCustomizations"] = color_customizations

# Save updated settings
with open(settings_path, "w") as f:
    json.dump(settings, f, indent=4)

print("Loud brown chat background applied to VS Code settings!")
