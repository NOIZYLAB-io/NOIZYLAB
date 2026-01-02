
#!/usr/bin/env python3
"""
vsbuddy.py
Advanced Python automation assistant for VS Code workflows.
Features: dynamic script runner, clipboard-to-speech, batch file ops, media metadata, logging, notifications, approval workflow, help menu, and error handling.
"""
import subprocess
import pyperclip
import time
from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog
from rich import print as rprint


LOG_FILE = Path.home() / "vsbuddy.log"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

def notify(msg):
    try:
        subprocess.run(["osascript", "-e", f'display notification "{msg}" with title "VS Buddy"'], check=True)
    except subprocess.CalledProcessError:
        print(f"[NOTIFY] {msg}")

def prompt_approval(action):
    resp = input(f"Approve and run '{action}'? [y/N]: ").strip().lower()
    return resp == 'y'

def run_shell(command, label=None):
    print(f"\n=== {label or command} ===")
    log(f"Running: {command}")
    if prompt_approval(label or command):
        try:
            subprocess.run(command, shell=True, check=True)
            notify(f"Completed: {label or command}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            log(f"Error: {e}")
            notify(f"Error: {label or command}")
    else:
        print(f"Skipped: {label or command}")
        log(f"Skipped: {label or command}")

def speak_clipboard():
    text = pyperclip.paste()
    if not text.strip():
        print("Clipboard is empty.")
        return
    # Remove code blocks
    import re
    clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL).strip()
    run_shell(f'say "{clean}"', label="Speak Clipboard")

def batch_move_files(src_dir, dest_dir, ext):
    src = Path(src_dir)
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    files = list(src.rglob(f'*{ext}'))
    for f in files:
        target = dest / f.name
        run_shell(f'mv "{f}" "{target}"', label=f"Move {f.name}")
    print(f"Moved {len(files)} {ext} files.")
    log(f"Moved {len(files)} {ext} files from {src} to {dest}")


def scan_media_files(root, exts):
    root = Path(root)
    found = []
    for ext in exts:
        found.extend(root.rglob(f'*{ext}'))
    for f in found:
        print(f)
    log(f"Scanned {len(found)} media files in {root}")

def extract_metadata(file_path):
    try:
        import ffmpeg
    except ImportError:
        print("ffmpeg-python is not installed. Run 'pip install ffmpeg-python' to use metadata extraction.")
        return
    try:
        probe = ffmpeg.probe(str(file_path))
        print(probe)
        log(f"Metadata for {file_path}: {probe}")
    except Exception as e:
        print(f"Metadata error: {e}")
        log(f"Metadata error for {file_path}: {e}")

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

def main():
    while True:
        print("\nVS Buddy Advanced Menu:")
        print("  1. Speak clipboard text")
        print("  2. Move all .mp4 files from a chosen source to a chosen destination")
        print("  3. Move all .mov files from a chosen source to a chosen destination")
        print("  4. Scan for media files in a chosen directory")
        print("  5. Extract metadata from a file")
        print("  6. Run a shell command")
        print("  7. View log file")
        print("  8. Quick Search for files")
        print("  9. Help & exit")
        choice = input("Select action number: ").strip()
        if choice == '1':
            speak_clipboard()
        elif choice == '2':
            print("Choose source directory for .mp4 files:")
            src = choose_directory("/")
            print("Choose destination directory for .mp4 files:")
            dest = choose_directory("/")
            batch_move_files(src, dest, ".mp4")
        elif choice == '3':
            print("Choose source directory for .mov files:")
            src = choose_directory("/")
            print("Choose destination directory for .mov files:")
            dest = choose_directory("/")
            batch_move_files(src, dest, ".mov")
        elif choice == '4':
            print("Choose directory to scan for media files:")
            scan_dir = choose_directory("/")
            scan_media_files(scan_dir, ['.mp4', '.mov', '.wav', '.mp3', '.aiff', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'])
        elif choice == '5':
            file_path = input("Enter full path to media file: ").strip()
            extract_metadata(file_path)
        elif choice == '6':
            cmd = input("Enter shell command to run: ").strip()
            run_shell(cmd)
        elif choice == '7':
            print("\n--- VS Buddy Log ---\n")
            if LOG_FILE.exists():
                print(LOG_FILE.read_text())
            else:
                print("No log file found.")
        elif choice == '8':
            print("Choose directory to search:")
            search_dir = choose_directory("/")
            query = input("Enter filename or extension to search for (e.g. .wav or piano): ").strip()
            try:
                from rich import print as rprint
            except ImportError:
                def rprint(x): print(x)
            # Fuzzy search: match if query is in filename (case-insensitive)
            results = [f for f in Path(search_dir).rglob('*') if query.lower() in f.name.lower()]
            if results:
                rprint(f"[bold green]Found {len(results)} files:[/]")
                for i, f in enumerate(results, 1):
                    rprint(f"[yellow]{i}. {f}[/]")
                batch = input("Select files to batch move/copy/delete (comma-separated numbers, or Enter to skip): ").strip()
                if batch:
                    indices = [int(x)-1 for x in batch.split(',') if x.strip().isdigit() and 0 <= int(x)-1 < len(results)]
                    selected = [results[i] for i in indices]
                    rprint(f"[cyan]Selected files:[/]")
                    for f in selected:
                        rprint(f"[magenta]{f}[/]")
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
            else:
                rprint("[red]No files found.[/]")
        elif choice == '9':
            help_menu()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
