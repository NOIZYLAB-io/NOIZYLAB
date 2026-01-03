#!/usr/bin/env python3
"""
Bucket Switcher: Unified Research Controller for Super Brain

Buckets included:
1. NoizyFish (music/audio APIs, instruments, hardware)
2. From a Seed Interiors (Canadian designers market analysis)

This script:
- Creates project + workspace folders automatically
- Auto-generates super_brain.py into each workspace
- Routes prompts into the correct workspace
- Saves results into Saved_Notes with timestamps
"""

import os
import sys
import subprocess
from pathlib import Path
import datetime
import textwrap
import json

# ---------- Config ----------
BASE_DIR = Path.home() / "Documents" / "Bucket_Switcher_Project"
NOIZY_DIR = BASE_DIR / "Noizyfish_Aquarium" / "Noizy_Workspace"
INTERIORS_DIR = BASE_DIR / "From_a_Seed_Interiors" / "Interiors_Workspace"

SAVE_DIR_NAME = "Saved_Notes"

# Prompts for each bucket
NOIZY_PROMPT = """
Give me the top 10 social distribution networks for music, audio, and sound.
For each, provide SDK or API documentation links, plus what developers can do.
Expand this to cover musical instruments, digital music instruments, and hardware
APIs that matter for distribution and integration. Organize into an 'API Bucket'.
"""

INTERIORS_PROMPT = """
List the top 50 interior designers in Canada. For each, show their finest
work in a PowerPoint-style layout (slide by slide summary). Include
Seed Interiors and Carolyn Arnold, then compare her firm to the market.
Provide a market analysis and positioning map.
"""

# ---------- Templates ----------
SUPER_BRAIN_TEMPLATE = textwrap.dedent("""
#!/usr/bin/env python3
'''Super Brain: Workspace Orchestrator'''

import os, sys, datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python super_brain.py '<your prompt here>'")
        sys.exit(1)

    prompt = sys.argv[1]
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    save_dir = "Saved_Notes"
    os.makedirs(save_dir, exist_ok=True)
    outfile = os.path.join(save_dir, f"{ts}_superbrain.txt")

    # Placeholder: replace this with OpenAI API calls if available
    fake_answer = f'''Super Brain received prompt:\n{prompt}\n\n[Simulated AI response here]'''
    print(fake_answer)

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(fake_answer)

    print(f"\n💾 Saved to {outfile}")

if __name__ == "__main__":
    main()
""")

# ---------- Helpers ----------
def ensure_workspace(path: Path):
    """Make sure workspace + Saved_Notes + super_brain.py exist."""
    path.mkdir(parents=True, exist_ok=True)
    (path / SAVE_DIR_NAME).mkdir(parents=True, exist_ok=True)

    sb_path = path / "super_brain.py"
    if not sb_path.exists():
        sb_path.write_text(SUPER_BRAIN_TEMPLATE)
        os.chmod(sb_path, 0o755)
        print(f"✅ Generated {sb_path}")

    return path / SAVE_DIR_NAME

def run_super_brain(prompt: str, workspace: Path, prefix: str):
    """Run super_brain.py inside workspace with a given prompt."""
    save_dir = ensure_workspace(workspace)
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    outfile = save_dir / f"{ts}_{prefix}.txt"

    print(f"\n🧠 Running Super Brain in: {workspace}")
    print(f"   Saving results to: {outfile}\n")

    try:
        result = subprocess.check_output(
            ["python3", "super_brain.py", prompt],
            cwd=workspace,
            text=True
        )
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ Output saved to {outfile}")
    except subprocess.CalledProcessError as e:
        print("❌ Error running Super Brain:", e)
        sys.exit(1)

def is_muted():
    mute_file = WORKSPACE / "mute_state.json"
    if mute_file.exists():
        try:
            return json.loads(mute_file.read_text()).get("mute", False)
        except Exception:
            return False
    return False

def speak(msg):
    if is_muted():
        return
    subprocess.run(["say", "-v", "Serena", msg])

def speak_siri(text, voice="Siri Voice 1"):
    subprocess.run(["say", "-v", voice, text], check=True)

def menu():
    print("\n=== Bucket Switcher ===")
    print("1. Run NoizyFish API/SDK Research")
    print("10) Talk to Cha-Cha (voice or text)")
    print("11) Cha-Cha read clipboard")
    print("12) Cha-Cha read current page")
    print("2. Exit")
    return input("Choose an option (1, 2, 10-12): ").strip()

def receive_clipboard():
    text = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout
    if not text.strip():
        return "Clipboard empty."
    fname = SAVED / f"buddy_clip_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    fname.write_text(text, encoding="utf-8")
    return f"Saved clipboard to {fname}"

def log(tag, note):
    SAVED = WORKSPACE / "Saved_Notes"
    SAVED.mkdir(parents=True, exist_ok=True)
    f = SAVED / f"{tag}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    f.write_text(note)

def handle_hotrod(lowered):
    if "hot rod" in lowered or "hot-rod" in lowered or "boost mac" in lowered:
        hog = NOIZY_DIR / "cha_cha_hotrod.py"
        if hog.exists():
            speak_siri("Hot-rodding your Mac, my dear.", voice="Siri Voice 3")
            try:
                out = subprocess.check_output(["python3", str(hog)], text=True)
                log("hotrod_run", out)
                speak_siri("Your Mac is hot-rodded, my dear.", voice="Siri Voice 3")
                return out
            except subprocess.CalledProcessError as e:
                speak_siri("The hot rod sputtered, my dear.", voice="Siri Voice 3")
                log("hotrod_err", str(e))
                return str(e)
        else:
            speak_siri("Hot rod script not found, my dear.", voice="Siri Voice 3")
            return "missing_hotrod"

def handle_overdrive(lowered):
    if "overdrive" in lowered or "keep it cooking" in lowered:
        speak_siri("Engaging Overdrive, my dear.", voice="Siri Voice 3")
        return overdrive()

def overdrive():
    notes = []
    # 1. Prioritize Logic & VS Code
    for app in ["Logic Pro X", "Visual Studio Code"]:
        try:
            subprocess.run([
                "osascript", "-e",
                f'tell application "System Events" to set frontmost of process "{app}" to true'
            ], check=True)
            notes.append(f"Prioritized {app}")
        except Exception as e:
            notes.append(f"Failed to prioritize {app}: {e}")

    # 2. Kill known background hogs (safe list)
    hogs = ["PhotoAnalysisd", "mds", "backupd"]
    for h in hogs:
        subprocess.run(["killall", "-9", h], stderr=subprocess.DEVNULL)
    notes.append("Background hogs trimmed.")

    # 3. Faster Cha-Cha speech
    subprocess.run(["defaults", "write", "com.apple.speech.synthesis.general.prefs", "Rate", "250"], check=True)
    notes.append("Cha-Cha speech sped up.")

    log("overdrive", "\n".join(notes))
    speak_siri("Overdrive engaged, my dear.", voice="Siri Voice 3")
    return "\n".join(notes)

# ---------- Main ----------
def main():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    speak_siri("Good evening, my dear.", voice="Siri Voice 3")
    while True:
        choice = menu()
        if choice == "1":
            run_super_brain(NOIZY_PROMPT, NOIZY_DIR, "noizyfish_research")
        elif choice == "10":
            subprocess.run([
                "python3",
                str(NOIZY_DIR / "noizyfish_command_center.py")
            ], check=True)
        elif choice == "11":
            subprocess.run([
                "python3",
                str(NOIZY_DIR / "noizyfish_command_center.py")
            ], input="11\n", text=True, check=True)
        elif choice == "12":
            subprocess.run([
                "python3",
                str(NOIZY_DIR / "noizyfish_command_center.py")
            ], input="12\n", text=True, check=True)
        elif choice == "2":
            print("👋 Exiting Bucket Switcher.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    print(subprocess.getoutput("system_profiler SPAudioDataType"))
    main()

    if "receive clipboard" in lowered or "clipboard in" in lowered:
        out = receive_clipboard()

    handle_hotrod(lowered)

import subprocess
subprocess.run(["sudo", "pkill", "-9", "coreaudiod"])