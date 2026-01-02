import os
import json

# Define paths
desktop_path = os.path.expanduser("~/Desktop/NoizyFish/utilities")
os.makedirs(desktop_path, exist_ok=True)
settings_path = os.path.join(desktop_path, "settings.json")

# Define your custom theme and layout
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
            {
                "scope": "comment",
                "settings": {"foreground": "#A89F91"}
            },
            {
                "scope": "keyword",
                "settings": {"foreground": "#D8CFC4"}
            },
            {
                "scope": "string",
                "settings": {"foreground": "#CBBEAA"}
            }
        ]
    },
    "editor.fontFamily": "Fira Code, Menlo, Monaco, 'Courier New', monospace",
    "editor.fontSize": 16,
    "editor.lineHeight": 24,
    "terminal.integrated.fontFamily": "Fira Code",
    "terminal.integrated.fontSize": 14,
    "window.zoomLevel": 1,
    "workbench.startupEditor": "newUntitledFile",
    "workbench.editor.enablePreview": False,
    "workbench.editor.showTabs": True,
    "workbench.editor.tabSizing": "shrink"
}

# Save the settings file
with open(settings_path, "w") as f:
    json.dump(settings, f, indent=4)

print(f"VS Code profile settings saved to: {settings_path}")
