#!/usr/bin/env python3
# Handler functions for menu actions
def handle_speak_clipboard():
    print("[clipboard] Speaking clipboard text...")

def handle_move_files(ext):
    print(f"Choose source directory for {ext} files:")
    src = choose_directory("/")
    print(f"Choose destination directory for {ext} files:")
    dest = choose_directory("/")
    print(f"[move] Moving {ext} files from {src} to {dest}")

def handle_scan_media():
    print("Choose directory to scan for media files:")
    scan_dir = choose_directory("/")
    print(f"[scan] Scanning media files in {scan_dir}")

def handle_extract_metadata():
    file_path = input("Enter full path to media file: ").strip()
    extract_metadata(file_path)

def handle_run_shell():
    cmd = input("Enter shell command to run: ").strip()
    run_shell(cmd)

def handle_view_log():
    print("\n--- VS Buddy Log ---\n")
    if LOG_FILE.exists():
        print(LOG_FILE.read_text())
    else:
        print("No log file found.")

def handle_quick_search():
    print("Choose directory to search:")
    search_dir = choose_directory("/")
    query = input("Enter filename or extension to search for (e.g. .wav or piano): ").strip()
    results = [f for f in Path(search_dir).rglob('*') if query.lower() in f.name.lower()]
    show_search_results(results)

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

def choose_directory(start_path):
    current = Path(start_path)
    # Dummy implementation for now
    return start_path

from pathlib import Path
from rich import print as rprint
from prompt_toolkit.shortcuts import radiolist_dialog

# Dummy implementations for missing helpers (replace with actual logic as needed)
def run_shell(cmd, label=None):
    print(f"[shell] {label or ''}: {cmd}")

def extract_metadata(file_path):
    print(f"[metadata] {file_path}")

# LOG_FILE for logging
LOG_FILE = Path("vsbuddy.log")

#!/usr/bin/env python3
"""
NoizyBrain & SuperBrain Automation Assistant

Modular Python automation for audio/media (NoizyBrain) and general workflows (SuperBrain).
"""

    # ...existing code...
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
    register_menus()
    workflow = select_workflow()
    if workflow:
        run_menu(workflow)

def register_menus():
    register_module('NoizyBrain', noizybrain_menu())
    register_module('SuperBrain', superbrain_menu())

    """Register all available menus."""
    register_module('NoizyBrain', noizybrain_menu())
    register_module('SuperBrain', superbrain_menu())

    """Prompt user to select workflow."""
    print("\nWelcome to NoizyBrain & SuperBrain Automation Assistant!")
    print("Choose your workflow:")
    print("  1. Audio/Media Automation (NoizyBrain)")
    print("  2. General Automation (SuperBrain)")
    choice = input("Select workflow number: ").strip()
    if choice == '1':
        return 'NoizyBrain'
    elif choice == '2':
        return 'SuperBrain'
    else:
        print("Invalid choice. Exiting.")
        return None

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

# Register all available menus
def register_menus():
    register_module('NoizyBrain', noizybrain_menu())
    register_module('SuperBrain', superbrain_menu())

# Prompt user to select workflow
def select_workflow():
    print("\nWelcome to NoizyBrain & SuperBrain Automation Assistant!")
    print("Choose your workflow:")
    print("  1. Audio/Media Automation (NoizyBrain)")
    print("  2. General Automation (SuperBrain)")
    choice = input("Select workflow number: ").strip()
    if choice == '1':
        return 'NoizyBrain'
    elif choice == '2':
        return 'SuperBrain'
    else:
        print("Invalid choice. Exiting.")
        return None
