"""
NoizyBrain & SuperBrain Automation Assistant

Modular Python automation for audio/media (NoizyBrain) and general workflows (SuperBrain).

Onboarding & Extension:
- Create and activate a Python 3 virtual environment, install requirements, and launch the assistant.
- Choose your workflow (Audio/Media Automation or General Automation).
- Extend by adding new handler functions and registering them in the menu.
- For advanced features, add new menu actions and handlers.
- For NGR integration, add handler functions for routing, approval, and feedback, and register NGR-specific actions and workflows.
- For market adaptation, create new menu functions and register them. Handlers can be reused or customized per market.

Voice-Activated Automation:
Install speech_recognition for hands-free control:
    pip install SpeechRecognition
Add a microphone and say commands like "move files" or "scan media" to trigger actions.

Example NGR Extension:
Register a menu with register_module('NGR', ngr_menu()).
Add handler functions for NGR actions and feedback.
"""

import subprocess
import os

# --- Handler Functions ---
def handle_speak_clipboard():
    """Speak clipboard text aloud"""
    print("Speak clipboard text aloud (feature not implemented yet).")

def handle_move_files(ext):
    """Move files by extension"""
    print(f"Move files with extension {ext} (feature not implemented yet).")

def handle_scan_media():
    """Scan for media files"""
    scan_dir = choose_directory("/")
    print(f"[scan] Scanning media files in {scan_dir}")

def handle_extract_metadata():
    """Extract media metadata"""
    file_path = input("Enter full path to media file: ").strip()
    print(f"[metadata] {file_path}")

def handle_run_shell():
    """Run any shell command"""
    cmd = input("Enter shell command to run: ").strip()
    print(f"[shell] {cmd}")

def handle_view_log():
    """View logs"""
    print("\n--- VS Buddy Log ---\n")
    print("No log file found.")

def handle_quick_search():
    """Quick search for files"""
    print("Choose directory to search:")
    search_dir = choose_directory("/")
    query = input("Enter filename or extension to search for (e.g. .wav or piano): ").strip()
    results = [f"dummy_file_{i}.{query.strip('.')}" for i in range(1, 4)]
    show_search_results(results)

def show_search_results(results):
    if not results:
        print("No files found.")
        return
    print(f"Found {len(results)} files:")
    for i, f in enumerate(results, 1):
        print(f"  {i}. {f}")
    batch = input("Select files to batch move/copy/delete (comma-separated numbers, or Enter to skip): ").strip()
    if not batch:
        return
    indices = [int(x)-1 for x in batch.split(',') if x.strip().isdigit() and 0 <= int(x)-1 < len(results)]
    selected = [results[i] for i in indices]
    print("Selected files:")
    for f in selected:
        print(f"  {f}")
    handle_batch_action(selected)

def handle_batch_action(selected):
    action = input("Choose action: [m]ove, [c]opy, [d]elete, [x]cancel: ").strip().lower()
    if action == 'm':
        dest = choose_directory("/")
        for f in selected:
            print(f"Move {f} to {dest}")
    elif action == 'c':
        dest = choose_directory("/")
        for f in selected:
            print(f"Copy {f} to {dest}")
    elif action == 'd':
        for f in selected:
            print(f"Delete {f}")
    else:
        print("Batch action cancelled.")

def help_menu():
    """Help & exit"""
    print("""
VS Buddy Help:
  1. Speak clipboard text aloud
  2. Move files by extension
  3. Scan for media files
  4. Extract media metadata
  5. Run any shell command
  6. View logs
  7. Quick search for files
  8. Help & exit
""")

def choose_directory(start_path):
    # Dummy implementation for now
    return start_path

# --- Menu Registration ---
MODULES = {}

def register_module(name, menu):
    MODULES[name] = menu

def noizybrain_menu():
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
    return {
        '1': handle_speak_clipboard,
        '2': handle_run_shell,
        '3': handle_view_log,
        '4': help_menu
    }

def register_menus():
    register_module('NoizyBrain', noizybrain_menu())
    register_module('SuperBrain', superbrain_menu())

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

def set_default_voice():
    """Set default macOS system voice to British Siri"""
    voice_name = "Siri (United Kingdom)"
    try:
        subprocess.run([
            "defaults", "write", "com.apple.speech.voice.prefs", "SelectedVoiceName", voice_name
        ], check=True)
        subprocess.run([
            "killall", "-u", os.getlogin(), "cfprefsd"
        ], check=True)
        print(f"Default system voice set to: {voice_name}")
        subprocess.run([
            "say", "-v", voice_name, "Hello Rob, I am now your British Siri voice."
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting voice: {e}")

if __name__ == "__main__":
    register_menus()
    workflow = select_workflow()
    if workflow:
        run_menu(workflow)
