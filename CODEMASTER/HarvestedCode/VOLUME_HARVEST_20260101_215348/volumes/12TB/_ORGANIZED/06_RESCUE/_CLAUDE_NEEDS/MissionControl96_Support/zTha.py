import requests
import time

def speak_with_sarah(text, voice_id="Sarah", api_key="your-elevenlabs-api-key"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.85
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    with open("/Users/rob/Desktop/NoizyFish/utilities/sarah_output.mp3", "wb") as f:
        f.write(response.content)
    print("Sarah has spoken.")

"editor.accessibilitySignalTimeout": 3000,

"workbench.colorCustomizations": {
  "activityBar.background": "#3B2F2F",
  "sideBar.background": "#2E1F1F",
  "editor.background": "#1F1414",
  "statusBar.background": "#3B2F2F",
  "titleBar.activeBackground": "#3B2F2F",
  "titleBar.activeForeground": "#D8CFC4",
  "tab.activeBackground": "#2E1F1F",
  "tab.inactiveBackground": "#1F1414",
  "tab.border": "#3B2F2F"
}

def run_alias_creation():
    summary = []
    actions = 0
    for vol in VOLUMES.iterdir():
        if vol.name.startswith('.') or not vol.is_dir() or vol.name in SKIP_VOLUMES:
            continue
        alias_path = SUBFOLDER / vol.name
        if alias_path.exists():
            if alias_path.is_symlink() and os.readlink(str(alias_path)) == str(vol):
                msg = f"Alias already exists and is correct: {alias_path}"
            else:
                msg = f"Alias already exists but may be incorrect: {alias_path}"
            print(msg)
            summary.append(f"• {msg}")
            continue
        try:
            os.symlink(str(vol), str(alias_path))
            msg = f"Created alias for {vol} -> {alias_path}"
            print(msg)
            summary.append(f"• {msg}")
            actions += 1
        except PermissionError:
            msg = f"Permission denied: Failed to create alias for {vol}"
            print(msg)
            summary.append(f"• {msg}")
        except Exception as e:
            msg = f"Failed to create alias for {vol}: {e}"
            print(msg)
            summary.append(f"• {msg}")
    return actions, summary

if __name__ == "__main__":
    while True:
        actions, summary = run_alias_creation()
        print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")
        print("\nSummary:")
        for line in summary[-2:]:
            print(line)
        if summary:
            speak_with_sarah("\n".join(summary[-2:]), api_key="your-elevenlabs-api-key")
        if actions == 0:
            print("No new actions. All aliases are up to date and clear.")
            break
        time.sleep(2)  # Optional: wait before retrying