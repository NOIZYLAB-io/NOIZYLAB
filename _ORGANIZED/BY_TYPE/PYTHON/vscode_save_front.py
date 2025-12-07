import subprocess

# Save the front document in Visual Studio Code (macOS only)
subprocess.run([
    "osascript",
    "-e",
    'tell application "Visual Studio Code" to save front document'
])