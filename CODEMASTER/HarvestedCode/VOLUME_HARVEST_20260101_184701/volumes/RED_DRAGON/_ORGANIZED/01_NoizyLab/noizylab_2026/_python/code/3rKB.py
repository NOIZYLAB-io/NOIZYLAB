#!/usr/bin/env python3
"""
read_page_cha_cha.py
Uses AppleScript to get the frontmost browser page text (Safari or Chrome),
copies to clipboard, then calls read_selection_cha_cha.py to speak it.
"""

import subprocess, sys
from pathlib import Path

WORKSPACE = Path.cwd()
SCRIPT_DIR = WORKSPACE
READ_SELECTION = SCRIPT_DIR / "read_selection_cha_cha.py"

def get_safari_text():
    applescript = '''
    tell application "Safari"
        if (count of windows) = 0 then
            return ""
        end if
        set theSource to do JavaScript "document.body.innerText" in front document
    end tell
    return theSource
    '''
    return run_applescript(applescript)

def get_chrome_text():
    applescript = '''
    tell application "Google Chrome"
        if (count of windows) = 0 then
            return ""
        end if
        set theSource to execute front window's active tab javascript "document.body.innerText"
    end tell
    return theSource
    '''
    return run_applescript(applescript)

def run_applescript(script):
    p = subprocess.run(["osascript","-e",script], capture_output=True, text=True, check=True)
    return p.stdout

def main():
    # Try Safari first, then Chrome
    text = get_safari_text().strip()
    if not text:
        text = get_chrome_text().strip()
    if not text:
        print("Could not extract page text from Safari or Chrome. Try selecting text manually.")
        sys.exit(1)
    # copy to clipboard
    subprocess.run(["pbcopy"], input=text, text=True, check=True)
    print("Page text copied to clipboard — calling read_selection_cha_cha.py")
    subprocess.run(["python3", str(READ_SELECTION)], check=True)

if __name__ == "__main__":
    main()
