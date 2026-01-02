import subprocess
import time

# --- Sarah TTS function ---
def sarah_speak(text):
    # Use 'Sarah' voice if available, otherwise fallback to 'Samantha'
    try:
        subprocess.run(['say', '-v', 'Sarah', text])
    except Exception:
        subprocess.run(['say', '-v', 'Samantha', text])

# --- Important bullet points for VS Code feedback ---
important_points = [
    "You have 158 settings configured in your VS Code profile.",
    "Your terminal font is set to SL Mono, size 14 for legibility.",
    "The terminal and chat backgrounds use a sandy cream color for comfort.",
    "Accessibility and AI features are enabled for your workspace.",
    "Auto-save and code formatting are active for all files.",
    "Cloud sync and collaboration features are available.",
    "Security and audit logging are enabled for your projects."
]

# --- Speak each bullet point with Sarah ---
for point in important_points:
    sarah_speak(point)
    time.sleep(1.5)  # Pause between points for clarity
