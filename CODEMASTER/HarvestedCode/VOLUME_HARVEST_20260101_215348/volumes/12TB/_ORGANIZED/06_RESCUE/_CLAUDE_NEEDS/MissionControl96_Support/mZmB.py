#!/usr/bin/env python3
"""
Superscript: Voice-First Creative Cockpit
Author: R.S Plowman
Purpose: Unified voice loop with ElevenLabs (Sarah), VS Code task triggers,
         browser opens, vault actions, git automation, and transfer workflow.
"""

import os, subprocess, tempfile, requests, argparse, asyncio, webbrowser
import speech_recognition as sr
from playsound import playsound

# --- CONFIG ---
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
VOICE_ID = "your_sarah_voice_id"  # Replace with your ElevenLabs Sarah voice ID
PROJECT_DIR = os.path.expanduser("~/Projects/voice-cockpit")
PLIST_PATH = os.path.expanduser("~/Library/LaunchAgents/com.plowman.superscript.plist")

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
    """Trigger VS Code tasks, scripts, browser, vault, and transfer actions by voice"""
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
    if "service backup codes" in t:
        subprocess.run(["python", "authenticator_orchestrator.py", "vault", "add", "Service backup codes: XXXXX"])
        return "Service backup codes stored in vault."
    if "read vault" in t:
        subprocess.run(["python", "forward1_all_in_one.py", "vault", "read"])
        return "Vault contents displayed."
    if "open webador dns" in t:
        webbrowser.open("https://www.webador.com/v2/website/6949172/dns/noizyfish.com")
        return "Webador DNS for noizyfish.com opened."
    if "transfer noizyfish" in t:
        webbrowser.open("https://www.webador.com/v2/website/6949172/dns/noizyfish.com")
        print("Unlock at Webador and request EPP/Auth code.")
        webbrowser.open("https://account.godaddy.com/domains/transfer")
        print("Paste EPP code and complete transfer at GoDaddy.")
        subprocess.run(["python", "forward1_all_in_one.py", "cfg", "set-domain-status", "noizyfish.com", "transfer_in_progress"])
        return "Transfer initiated and status updated."
    if "m365" in t:
        subprocess.run(["python", "authenticator_orchestrator.py", "flow", "m365"])
        return "Microsoft 365 flow executed."
    if "godaddy" in t:
        subprocess.run(["python", "authenticator_orchestrator.py", "flow", "godaddy"])
        return "GoDaddy flow executed."
    if "facebook" in t:
        subprocess.run(["python", "authenticator_orchestrator.py", "flow", "facebook"])
        return "Facebook flow executed."
    return f"No mapped task for: {task}"

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

def git_init_and_commit():
    subprocess.run(["git", "init"], cwd=PROJECT_DIR)
    subprocess.run(["git", "add", "."], cwd=PROJECT_DIR)
    subprocess.run(["git", "commit", "-m", "Initial superscript"], cwd=PROJECT_DIR)
    subprocess.run(["git", "add", "superscript.py"], cwd=PROJECT_DIR)
    subprocess.run(["git", "commit", "-m", "Voice update"], cwd=PROJECT_DIR)

def create_plist():
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
 <dict>
   <key>Label</key>
   <string>com.plowman.superscript</string>
   <key>ProgramArguments</key>
   <array>
     <string>/usr/bin/python3</string>
     <string>{PROJECT_DIR}/superscript.py</string>
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
"""
    with open(PLIST_PATH, "w") as f:
        f.write(plist_content)
    print(f"LaunchAgent plist created at {PLIST_PATH}")
    print("To load it, run:")
    print(f"launchctl load {PLIST_PATH}")
    print("To monitor logs:")
    print("tail -f /tmp/superscript.log")
    print("tail -f /tmp/superscript.err")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", "-s", help="Search the treats list")
    parser.add_argument("--list", "-l", action="store_true", help="List all treats")
    parser.add_argument("--loop", action="store_true", help="Start interactive voice loop")
    parser.add_argument("--git", action="store_true", help="Initialize and commit git repo")
    parser.add_argument("--plist", action="store_true", help="Create LaunchAgent plist")
    args = parser.parse_args()

    if args.list:
        list_all()
    elif args.search:
        search(args.search)
    elif args.loop:
        asyncio.run(interactive_loop())
    elif args.git:
        git_init_and_commit()
    elif args.plist:
        create_plist()
    else:
        parser.print_help()

subprocess.run(["pip", "install", "click", "rich", "pyyaml", "cryptography", "requests"])