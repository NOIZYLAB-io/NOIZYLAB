from pathlib import Path

workspace = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
for path in workspace.rglob("*"):
    print(path)