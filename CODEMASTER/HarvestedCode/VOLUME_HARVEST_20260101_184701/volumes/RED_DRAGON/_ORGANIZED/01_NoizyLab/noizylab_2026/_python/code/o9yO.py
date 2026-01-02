# Handler functions for menu actions
"""
NoizyBrain & SuperBrain Automation Assistant

Modular Python automation for audio/media (NoizyBrain) and general workflows (SuperBrain).

VS Buddy Help:
  1. Speak clipboard text aloud
  2. Move files by extension
  3. Scan for media files
  4. Extract media metadata
  5. Run any shell command
  6. View logs
  7. Help & exit
"""

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
