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

def speak(text):
    subprocess.run(["say", "-v", "Serena", text])

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
