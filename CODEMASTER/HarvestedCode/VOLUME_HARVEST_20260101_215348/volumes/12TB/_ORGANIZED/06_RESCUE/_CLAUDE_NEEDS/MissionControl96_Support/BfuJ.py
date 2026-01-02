import os
import json
import subprocess

# === Paths ===
base_path = os.path.expanduser("~/Desktop/NoizyFish/utilities")
os.makedirs(base_path, exist_ok=True)
settings_path = os.path.join(base_path, "settings.json")
workspace_path = os.path.join(base_path, "NoizyCockpit.code-workspace")

# === Visual Theme & Font Customization ===
settings = {
    "workbench.colorCustomizations": {
        "activityBar.background": "#3B2F2F",
        "sideBar.background": "#2E1F1F",
        "editor.background": "#1F1414",
        "statusBar.background": "#3B2F2F",
        "titleBar.activeBackground": "#3B2F2F",
        "titleBar.activeForeground": "#D8CFC4",
        "tab.activeBackground": "#2E1F1F",
        "tab.inactiveBackground": "#1F1414",
        "tab.border": "#3B2F2F"
    },
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {"scope": "comment", "settings": {"foreground": "#A89F91"}},
            {"scope": "keyword", "settings": {"foreground": "#D8CFC4"}},
            {"scope": "string", "settings": {"foreground": "#CBBEAA"}},
            {"scope": "variable", "settings": {"foreground": "#EADDCB"}},
            {"scope": "function", "settings": {"foreground": "#F5EBDD"}}
        ]
    },
    "editor.fontFamily": "Fira Code, Menlo, Monaco, 'Courier New', monospace",
    "editor.fontSize": 16,
    "editor.lineHeight": 24,
    "editor.cursorStyle": "line",
    "editor.cursorBlinking": "phase",
    "terminal.integrated.fontFamily": "Fira Code",
    "terminal.integrated.fontSize": 14,
    "window.zoomLevel": 1.2,
    "workbench.editor.enablePreview": False,
    "workbench.editor.tabSizing": "shrink",
    "workbench.startupEditor": "newUntitledFile",
    "editor.minimap.enabled": False,
    "explorer.compactFolders": False,
    "editor.renderWhitespace": "boundary",
    "editor.wordWrap": "on",
    "editor.smoothScrolling": True,
    "editor.guides.indentation": True,
    "editor.guides.bracketPairs": "active"
}

# === Workspace Layout Preset ===
workspace = {
    "folders": [
        {"path": os.path.expanduser("~/Desktop/NoizyFish/projects")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/scripts")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/assets")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/legacy")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/eco")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/agents")},
        {"path": os.path.expanduser("~/Desktop/NoizyFish/cockpit")}
    ],
    "settings": {
        "files.exclude": {
            "**/__pycache__": True,
            "**/*.tmp": True,
            "**/*.log": True
        },
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.organizeImports": True,
            "source.fixAll": True
        },
        "editor.defaultFormatter": "ms-python.python"
    }
}

# === Save Settings and Workspace ===
with open(settings_path, "w") as f:
    json.dump(settings, f, indent=4)

with open(workspace_path, "w") as f:
    json.dump(workspace, f, indent=4)

# === Optional: Launch VS Code with Workspace ===
try:
    subprocess.run(["code", workspace_path])
    print("🚀 VS Code launched with NoizyCockpit workspace.")
except Exception as e:
    print(f"⚠️ Could not launch VS Code: {e}")

print("✅ VS Code cockpit initialized. Settings and workspace saved.")
