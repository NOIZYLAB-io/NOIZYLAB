# ---------- Agent Stubs ----------
def super_brain(arg=None):
    return f"[Super Brain] {arg}"

def cleanup_system():
    return "[Bubba] Desktop cleaned"

def clean_big_house(copy_mode=True):
    return f"[Bubba] Big house cleaned (copy_mode={copy_mode})"

def audit_workspace():
    return "[Bubba] Workspace audited"

def run_diagnostics():
    return "[Bubba] Diagnostics run"

def list_projects():
    return "[Bubba] Projects listed"

def parallels_status():
    return "[Bubba] Parallels status checked"

def launch_parallels():
    return "[Bubba] Parallels launched"

def prep_app_store(vendor):
    return f"[Bubba] App Store prepped for {vendor.title()}"

def set_mute_state(state):
    return f"Mute set to {state}"

def speak(msg):
    print(f"[Speak] {msg}")

def menu():
    print("[Menu] Interactive mode not implemented in stub.")
#!/usr/bin/env python3
"""
bucket_switcher.py
Cha-Cha routes commands to Bubba, Super Brain, Noizy Brain, etc.
Features:
 - Default fallback bucket (Bubba).
 - Synonym mapping for more natural commands.
"""



import subprocess, sys
import difflib
from pathlib import Path
# ---------- Synonym Map ----------
# Maps alternate phrases to canonical bucket commands
CLEANUP_CMD = "cleanup big house"
SYNONYMS = {
    "tidy big house": CLEANUP_CMD,
    "sort drives": CLEANUP_CMD,
    "organize volumes": CLEANUP_CMD,
    "parallels start": "launch parallels",
    "parallels boot": "launch parallels",
    "prep store": "prep appstore",
    "app store": "prep appstore",
    "checklist": "write checklist",
}


# ---------- Command Handler with Fuzzy + Chaining ----------
COMMANDS = {
    "super brain": lambda arg=None: super_brain(arg or "Hello from Bubba"),
    "cleanup desktop": lambda arg=None: cleanup_system(),
    "cleanup big house": lambda arg=None: clean_big_house(copy_mode=True),
    "audit workspace": lambda arg=None: audit_workspace(),
    "diagnostics": lambda arg=None: run_diagnostics(),
    "list projects": lambda arg=None: list_projects(),
    "parallels status": lambda arg=None: parallels_status(),
    "launch parallels": lambda arg=None: launch_parallels(),
    "prep app store apple": lambda arg=None: prep_app_store("apple"),
    "prep app store microsoft": lambda arg=None: prep_app_store("microsoft"),
    "mute": lambda arg=None: (set_mute_state(True), "🔇 Cha-Cha muted.")[1],
    "unmute": lambda arg=None: (set_mute_state(False), "🔊 Cha-Cha unmuted.")[1],
}

def match_command(user_input: str):
    """Fuzzy match user input to known commands."""
    best = difflib.get_close_matches(user_input, COMMANDS.keys(), n=1, cutoff=0.5)
    return best[0] if best else None

def handle_input(command_str: str):
    """Split into subcommands, match fuzzily, and run them all."""
    results = []
    parts = [p.strip() for p in command_str.replace("then", "and").split("and")]
    for part in parts:
        key = match_command(part)
        if key:
            out = COMMANDS[key]()
            results.append(f"[{key}] {out}")
        else:
            results.append(f"Unknown command: {part}")
    result = "\n".join(results)
    print(result)
    speak(result)
    return result

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"

BUCKETS = {
    "bubba": WORKSPACE / "bubba_hand_of_god.py",
    "superbrain": WORKSPACE / "super_brain.py",
    "noizybrain": WORKSPACE / "noizy_brain.py",
}

DEFAULT_BUCKET = "bubba"


CLEANUP_CMD = "cleanup big house"
SYNONYMS = {
    "tidy big house": CLEANUP_CMD,
    "sort drives": CLEANUP_CMD,
    "organize volumes": CLEANUP_CMD,
    "parallels start": "launch parallels",
    "parallels boot": "launch parallels",
    "prep store": "prep appstore",
    "app store": "prep appstore",
    "checklist": "write checklist",
}

def normalize_command(cmd_str: str) -> str:
    """Normalize synonyms to canonical form."""
    cmd = cmd_str.lower().strip()
    for alt, canonical in SYNONYMS.items():
        if alt in cmd:
            return canonical
    return cmd

def run_bucket(bucket_name: str, cmd_str: str):
    if bucket_name not in BUCKETS:
        print(f"❓ Unknown bucket: {bucket_name}. Falling back to {DEFAULT_BUCKET}.")
        bucket_name = DEFAULT_BUCKET
    target = BUCKETS[bucket_name]
    if not target.exists():
        print(f"⚠️ Bucket {bucket_name} file not found at {target}")
        return
    try:
        subprocess.run(["python3", str(target), cmd_str], check=False)
    except subprocess.SubprocessError as e:
        print(f"⚠️ Error running {bucket_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command_str = " ".join(sys.argv[1:]).lower()
        handle_input(command_str)
    else:
        menu()
