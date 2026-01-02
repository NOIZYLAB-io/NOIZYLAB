"""
NoizyBrain & SuperBrain Automation Assistant

Modular Python automation for audio/media (NoizyBrain) and general workflows (SuperBrain).


Extension Points: To extend for NGR or other markets, create new menu functions and handlers, then register them with register_module(). For advanced features such as previews, undo, or multi-pane navigation, add new menu actions and handlers. For NGR integration, add new handler functions for routing, approval, and feedback, and register NGR-specific actions and workflows in the modular menu system. To adapt for new markets, create new menu functions (e.g., finance_menu, health_menu) and register them with register_module(). Handlers can be reused or customized per market. If you see missing package errors, run the pip install command above in your active virtual environment. To add new features, copy the pattern of the handler functions and register them in the appropriate menu. See the onboarding section above for setup and troubleshooting.
    register_module('NGR', ngr_menu())

    def handle_ng_voice():
        "Handle NGR voice command."
        # Implement NGR voice logic here
        pass

    def handle_ng_batch():
        "Handle NGR batch routing."
        # Implement NGR batch logic here
        pass

See the onboarding section above for setup and troubleshooting.
"""

#!/usr/bin/env python3
"""
NoizyBrain & SuperBrain Automation Assistant

Modular Python automation for audio/media (NoizyBrain) and general workflows (SuperBrain).

Features:
- Dynamic script runner
- Clipboard-to-speech
- Batch file operations
- Media metadata extraction
- Logging & notifications
- Approval workflow
- Interactive menu & navigation
- Colorized output
- Fuzzy search & batch actions



6. For advanced features (previews, undo, multi-pane navigation), add new menu actions and handlers.

7. For NGR integration, see extension points and modular handler structure.

Advanced Onboarding & Extension Points
======================================

NGR Integration:
- To integrate with NGR (Next Generation Routing), add new handler functions for routing, approval, and feedback.
- Use the modular menu system to register NGR-specific actions and workflows.
- Example: Add a handler for NGR voice commands, batch routing, or approval workflows.

Market Adaptation:
- To adapt for new markets, create new menu functions (e.g., finance_menu, health_menu) and register them with register_module().
- Handlers can be reused or customized per market.
- Example: For finance, add batch transaction handlers, reporting, or compliance checks.

See the onboarding section above for setup and troubleshooting.
"""




# Requirements: pip install prompt_toolkit rich pyperclip ffmpeg-python
import subprocess
import pyperclip
import time

# Add missing imports
from pathlib import Path
from rich import print as rprint
from prompt_toolkit.shortcuts import radiolist_dialog

# Import handler dependencies (assuming these are defined elsewhere in the file or in modules)
from vsbuddy_handlers import speak_clipboard, batch_move_files, scan_media_files, extract_metadata, run_shell

# Define LOG_FILE for logging
LOG_FILE = Path("vsbuddy.log")


def help_menu():
    print("""
VS Buddy Help:
  1. Speak clipboard text aloud
  2. Move files by extension
  3. Scan for media files
  4. Extract media metadata
  5. Run any shell command
  6. View logs
  7. Help & exit
""")

def list_directories(path):
    path = Path(path)
    dirs = [d for d in path.iterdir() if d.is_dir()]
    for i, d in enumerate(dirs, 1):
        print(f"  {i}. {d.name}")
    return dirs

def choose_directory(start_path):
    current = Path(start_path)
    while True:
        rprint(f"\n[bold cyan]Current directory:[/] [yellow]{str(current)}[/]")
        items = list(current.iterdir())
        dirs = [d for d in items if d.is_dir()]
        files = [f for f in items if f.is_file()]
        choices = [(f"[bold blue]{d.name}/[/]", str(d)) for d in dirs] + [(f"[white]{f.name}[/]", str(f)) for f in files]
        choices.insert(0, ("[magenta].. (Go up one level)[/]", str(current.parent) if current.parent != current else str(current)))
        choices.append(("[green]Select this directory[/]", str(current)))
        result = radiolist_dialog(
            title="Directory Navigator",
            text=f"Choose a directory or file in [yellow]{str(current)}[/]",
            values=choices
        ).run()
        if result is None:
            rprint("[red]Cancelled selection.[/]")
            return str(current)
        elif result == str(current):
            return str(current)
        elif result in [str(d) for d in dirs]:
            current = Path(result)
        elif result == str(current.parent):
            current = current.parent
        else:
            rprint("[red]Invalid choice.[/]")

# Handler functions for menu actions
def handle_speak_clipboard():
    """Speak clipboard text aloud."""
    speak_clipboard()

def handle_move_files(ext):
    """Move files by extension from source to destination."""
    print(f"Choose source directory for {ext} files:")
    src = choose_directory("/")
    print(f"Choose destination directory for {ext} files:")
    dest = choose_directory("/")
    batch_move_files(src, dest, ext)

def handle_scan_media():
    """Scan for media files in a chosen directory."""
    print("Choose directory to scan for media files:")
    scan_dir = choose_directory("/")
    scan_media_files(scan_dir, ['.mp4', '.mov', '.wav', '.mp3', '.aiff', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'])

def handle_extract_metadata():
    """Extract metadata from a file."""
    file_path = input("Enter full path to media file: ").strip()
    extract_metadata(file_path)

def handle_run_shell():
    """Run a shell command."""
    cmd = input("Enter shell command to run: ").strip()
    run_shell(cmd)

def handle_view_log():
    """View VS Buddy log file."""
    print("\n--- VS Buddy Log ---\n")
    if LOG_FILE.exists():
        print(LOG_FILE.read_text())
    else:
        print("No log file found.")

def handle_quick_search():
    """Quick Search for files with fuzzy matching and batch actions."""
    print("Choose directory to search:")
    search_dir = choose_directory("/")
    query = input("Enter filename or extension to search for (e.g. .wav or piano): ").strip()
    results = [f for f in Path(search_dir).rglob('*') if query.lower() in f.name.lower()]
    show_search_results(results)

def show_search_results(results):
    if not results:
        rprint("[red]No files found.[/]")
        return
    rprint(f"[bold green]Found {len(results)} files:[/]")
    for i, f in enumerate(results, 1):
        rprint(f"[yellow]{i}. {f}[/]")
    batch = input("Select files to batch move/copy/delete (comma-separated numbers, or Enter to skip): ").strip()
    if not batch:
        return
    indices = [int(x)-1 for x in batch.split(',') if x.strip().isdigit() and 0 <= int(x)-1 < len(results)]
    selected = [results[i] for i in indices]
    rprint("[cyan]Selected files:[/]")
    for f in selected:
        rprint(f"[magenta]{f}")
    handle_batch_action(selected)

def handle_batch_action(selected):
    action = input("Choose action: [m]ove, [c]opy, [d]elete, [x]cancel: ").strip().lower()
    if action == 'm':
        dest = choose_directory("/")
        for f in selected:
            run_shell(f'mv "{f}" "{Path(dest)/f.name}"', label=f"Move {f.name}")
    elif action == 'c':
        dest = choose_directory("/")
        for f in selected:
            run_shell(f'cp "{f}" "{Path(dest)/f.name}"', label=f"Copy {f.name}")
    elif action == 'd':
        for f in selected:
            run_shell(f'rm "{f}"', label=f"Delete {f.name}")
    else:
        rprint("[red]Batch action cancelled.[/]")

# Modular menu registry
MODULES = {}
def register_module(name, menu):
    MODULES[name] = menu

def noizybrain_menu():
    """NoizyBrain: Audio/Media Automation Menu"""
    return {
        '1': handle_speak_clipboard,
        '2': lambda: handle_move_files('.mp4'),
        '3': lambda: handle_move_files('.mov'),
        '4': handle_scan_media,
        '5': handle_extract_metadata,
        '6': handle_run_shell,
        '7': handle_view_log,
        '8': handle_quick_search,
        '9': help_menu
    }

def superbrain_menu():
    """SuperBrain: General Automation Menu (customize for other markets)"""
    return {
        '1': handle_speak_clipboard,
        '2': handle_run_shell,
        '3': handle_view_log,
        '4': help_menu
    }

def main():
    """Entry point: Choose NoizyBrain (audio/media) or SuperBrain (general)"""
    register_module('NoizyBrain', noizybrain_menu())
    register_module('SuperBrain', superbrain_menu())
    print("\nWelcome to NoizyBrain & SuperBrain Automation Assistant!")
    print("Choose your workflow:")
    print("  1. Audio/Media Automation (NoizyBrain)")
    print("  2. General Automation (SuperBrain)")
    choice = input("Select workflow number: ").strip()
    if choice == '1':
        run_menu('NoizyBrain')
    elif choice == '2':
        run_menu('SuperBrain')
    else:
        print("Invalid choice. Exiting.")

def run_menu(module_name):
    menu = MODULES.get(module_name)
    if menu is None:
        print(f"No menu found for {module_name}.")
        return
    while True:
        print(f"\n{module_name} Menu:")
        for k, v in menu.items():
            label = v.__doc__.splitlines()[0] if v.__doc__ else ""
            print(f"  {k}. {label}")
        choice = input("Select action number: ").strip()
        if choice in menu:
            menu[choice]()
            if menu[choice].__name__ == 'help_menu':
                break
        else:
            print("Invalid choice.")
