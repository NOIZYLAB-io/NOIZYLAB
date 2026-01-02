#!/usr/bin/env python3
"""
Bucket Switcher: Unified Research Script
- Bucket 1: NoizyFish (music/audio distribution APIs, instruments, hardware)
- Bucket 2: From a Seed Interiors (interior designers market analysis)
"""

import os
import sys
import subprocess
from pathlib import Path
import datetime

# ---------- Config ----------
BASE_DIR = Path.home() / "Documents" / "Bucket_Workspaces"
NOIZY_DIR = BASE_DIR / "Noizyfish_Aquarium" / "Noizy_Workspace"
INTERIORS_DIR = BASE_DIR / "From_a_Seed_Interiors" / "Interiors_Workspace"

SAVE_DIR_NAME = "Saved_Notes"

# Prompts
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

# ---------- Helpers ----------
def ensure_workspace(path: Path):
    """Make sure workspace + Saved_Notes exist."""
    path.mkdir(parents=True, exist_ok=True)
    (path / SAVE_DIR_NAME).mkdir(parents=True, exist_ok=True)
    return path / SAVE_DIR_NAME

def run_super_brain(prompt: str, workspace: Path, prefix: str):
    """Call super_brain.py with a given prompt and save output in bucket workspace."""
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

def menu():
    print("\n=== Bucket Switcher ===")
    print("1. Run NoizyFish API/SDK Research")
    print("2. Run From a Seed Interiors Market Analysis")
    print("3. Exit")
    return input("Choose a bucket (1-3): ").strip()

# ---------- Main ----------
def main():
    # CLI argument support for direct superbrain prompt
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.lower().startswith("superbrain"):
            # Extract prompt after 'superbrain'
            prompt = arg[len("superbrain"):].strip()
            if not prompt:
                print("⚠️ Please provide a prompt after 'superbrain'.")
                sys.exit(2)
            run_super_brain(prompt, NOIZY_DIR, "superbrain_custom")
            return
    # Interactive menu fallback
    while True:
        choice = menu()
        if choice == "1":
            run_super_brain(NOIZY_PROMPT, NOIZY_DIR, "noizyfish_research")
        elif choice == "2":
            run_super_brain(INTERIORS_PROMPT, INTERIORS_DIR, "interiors_research")
        elif choice == "3":
            print("👋 Exiting Bucket Switcher.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
