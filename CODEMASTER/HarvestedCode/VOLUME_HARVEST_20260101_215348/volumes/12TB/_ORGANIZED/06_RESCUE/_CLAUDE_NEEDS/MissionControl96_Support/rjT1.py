#!/usr/bin/env python3
import json
from pathlib import Path

# VS Code workspace settings
VSCODE_SETTINGS = {
    "editor.fontFamily": "JetBrains Mono, Fira Mono, Menlo, Monaco, 'Courier New', monospace",
    "editor.fontSize": 14,
    "workbench.colorTheme": "Default Dark+"
}

# Tkinter GUI defaults
TKINTER_DEFAULTS = '''\
import tkinter as tk
root = tk.Tk()
root.option_add("*Font", "JetBrains Mono 14")
root.configure(bg="#222222")
# ...rest of your GUI code...
'''

# Write VS Code settings.json
vscode_dir = Path.home() / "Desktop" / "NoizyFish" / ".vscode"
vscode_dir.mkdir(parents=True, exist_ok=True)
settings_path = vscode_dir / "settings.json"
with open(settings_path, "w") as f:
    json.dump(VSCODE_SETTINGS, f, indent=2)
print(f"VS Code settings written to {settings_path}")

# Write Tkinter defaults example
example_path = Path.home() / "Desktop" / "NoizyFish" / "tkinter_defaults_example.py"
with open(example_path, "w") as f:
    f.write(TKINTER_DEFAULTS)
print(f"Tkinter GUI defaults example written to {example_path}")

print("Universal font and theme settings applied for VS Code and Python GUIs.")
