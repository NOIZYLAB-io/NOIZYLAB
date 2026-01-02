#!/usr/bin/env python3
"""
Superscript: Voice-First Creative Cockpit
Author: R.S Plowman
Purpose: Unified voice loop with ElevenLabs (Sarah), VS Code task triggers,
         and safe auto-save/backup hooks.
"""

import os, subprocess, tempfile, requests, argparse, asyncio
import speech_recognition as sr
from playsound import playsound

# --- CONFIG ---
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
VOICE_ID = "your_sarah_voice_id"  # Replace with your ElevenLabs Sarah voice ID

# --- MASTER LIST (shortened for brevity, expand with your 100+ items) ---
VS_CODE_TREATS = """
1. Voice dictation everywhere
2. Copilot Voice Chat
3. Cursorless + Talon integration
4. Serenade AI
5. Accessibility Help menu
6. Error Lens
7. Code Spell Checker
...
100. Voice-driven multi-modal AI
"""

# --- CORE FUNCTIONS ---

def list_all():
    print(VS_CODE_TREATS)

def search(keyword: str):
    results = [line for line in VS_CODE_TREATS.splitlines() if keyword.lower() in line.lower()]
    print("\n".join(results) if results else f"No matches for '{keyword}'")

def speak(text: str):
    """Send text to ElevenLabs and play Sarah's voice"""
    if not ELEVEN_API_KEY:
        print("No ELEVEN_API_KEY set")
        return
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    data = {"text": text}
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print("TTS error:", e)
        return
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        f.write(resp.content)
        path = f.name
    playsound(path)
    os.remove(path)

def listen():
    """Capture voice input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except Exception:
        return None

def run_task(task: str):
    """Trigger VS Code tasks or scripts by voice"""
    t = task.lower()
    if "save superscript" in t:
        subprocess.run([
            "osascript", "-e",
            'tell application "Visual Studio Code" to save front document'
        ])
        return "Superscript saved."
    if "checklist" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "checklist"])
        return "Checklist run."
    if "status" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "status"])
        return "Status displayed."
    if "open godaddy" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "open", "godaddy"])
        return "GoDaddy security opened."
    if "open facebook" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "open", "social"])
        return "Facebook security opened."
    if "open microsoft" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "open", "microsoft"])
        return "Microsoft 365 admin opened."
    if "store facebook code" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "vault", "add", "Facebook unlock code: E0aImbc6k6"])
        return "Facebook unlock code stored in vault."
    if "read vault" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "vault", "read"])
        return "Vault contents displayed."
    # Add more for Instagram, LinkedIn, etc.
    return f"No mapped task for: {task}"

# --- MAIN LOOP ---
async def interactive_loop():
    while True:
        cmd = listen()
        if not cmd:
            continue
        print("Heard:", cmd)
        if "search" in cmd.lower():
            keyword = cmd.split("search",1)[1].strip()
            results = [line for line in VS_CODE_TREATS.splitlines() if keyword.lower() in line.lower()]
            response = "\n".join(results) if results else f"No matches for {keyword}"
        else:
            response = run_task(cmd)
        print("AI:", response)
        speak(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", "-s", help="Search the treats list")
    parser.add_argument("--list", "-l", action="store_true", help="List all treats")
    parser.add_argument("--loop", action="store_true", help="Start interactive voice loop")
    args = parser.parse_args()

    if args.list:
        list_all()
    elif args.search:
        search(args.search)
    elif args.loop:
        asyncio.run(interactive_loop())
    else:
        parser.print_help()

# Initialize git repository and commit
subprocess.run(["git", "init"], cwd=os.path.expanduser("~/Projects/voice-cockpit"))
subprocess.run(["git", "add", "."], cwd=os.path.expanduser("~/Projects/voice-cockpit"))
subprocess.run(["git", "commit", "-m", "Initial superscript"], cwd=os.path.expanduser("~/Projects/voice-cockpit"))
subprocess.run(["git", "add", "superscript.py"], cwd=os.path.expanduser("~/Projects/voice-cockpit"))
subprocess.run(["git", "commit", "-m", "Voice update"], cwd=os.path.expanduser("~/Projects/voice-cockpit"))

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
 <dict>
   <key>Label</key>
   <string>com.plowman.superscript</string>
   <key>ProgramArguments</key>
   <array>
     <string>/usr/bin/python3</string>
     <string>/Users/rob/Projects/voice-cockpit/superscript.py</string>
     <string>--loop</string>
   </array>
   <key>RunAtLoad</key>
   <true/>
   <key>KeepAlive</key>
   <true/>
   <key>StandardOutPath</key>
   <string>/tmp/superscript.log</string>
   <key>StandardErrorPath</key>
   <string>/tmp/superscript.err</string>
 </dict>
</plist>

launchctl load ~/Library/LaunchAgents/com.plowman.superscript.plist
launchctl list | grep superscript
tail -f /tmp/superscript.log
tail -f /tmp/superscript.err