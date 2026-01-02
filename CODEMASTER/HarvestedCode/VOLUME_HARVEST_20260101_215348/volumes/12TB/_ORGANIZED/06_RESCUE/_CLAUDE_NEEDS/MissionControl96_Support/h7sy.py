def write_vscode_files():
    vscode_dir = ROOT / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    tasks_path = vscode_dir / "tasks.json"
    keybindings_path = vscode_dir / "keybindings.json"

    ua_tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "UA Orchestrator: Hygiene",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/ua_orchestrator.py", "hygiene"],
                "isBackground": False,
                "problemMatcher": []
            },
            {
                "label": "UA Orchestrator: List Scenes",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/ua_orchestrator.py", "list"],
                "isBackground": False,
                "problemMatcher": []
            },
            {
                "label": "UA Orchestrator: Apply Tracking Vocal",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/ua_orchestrator.py", "apply", "tracking_vocal"],
                "isBackground": False,
                "problemMatcher": []
            },
            {
                "label": "UA Orchestrator: Apply Guitar Unison",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/ua_orchestrator.py", "apply", "guitar_unison"],
                "isBackground": False,
                "problemMatcher": []
            },
            {
                "label": "UA Orchestrator: Apply Mixdown Lowlat",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/ua_orchestrator.py", "apply", "mixdown_lowlat"],
                "isBackground": False,
                "problemMatcher": []
            },
            {
                "label": "Extract Logic Commands",
                "type": "shell",
                "command": "python3",
                "args": [f"{ROOT}/extract_logic_commands.py"],
                "isBackground": False,
                "problemMatcher": []
            }
        ]
    }

    ua_keybindings = [
        { "key": "ctrl+alt+f", "command": "workbench.action.tasks.runTask", "args": "UA Orchestrator: Hygiene" },
        { "key": "ctrl+alt+1", "command": "workbench.action.tasks.runTask", "args": "UA Orchestrator: Apply Tracking Vocal" },
        { "key": "ctrl+alt+2", "command": "workbench.action.tasks.runTask", "args": "UA Orchestrator: Apply Guitar Unison" },
        { "key": "ctrl+alt+3", "command": "workbench.action.tasks.runTask", "args": "UA Orchestrator: Apply Mixdown Lowlat" }
    ]

    tasks_path.write_text(json.dumps(ua_tasks, indent=2))
    keybindings_path.write_text(json.dumps(ua_keybindings, indent=2))
    console.print(f"[green]Wrote UA tasks:[/green] {tasks_path}")
    console.print(f"[green]Wrote UA keybindings:[/green] {keybindings_path}")
    speak("UA VS Code automation files written.")