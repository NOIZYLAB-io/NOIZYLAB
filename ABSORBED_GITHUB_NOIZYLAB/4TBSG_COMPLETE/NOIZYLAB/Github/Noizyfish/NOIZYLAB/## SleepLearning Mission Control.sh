## SleepLearning Mission Control

### Quickstart

1. Install dependencies:
   ```sh
   pip install fastapi uvicorn pydantic requests elevenlabs
   ```
2. Set up your ElevenLabs API key (with voices_read and text-to-speech permissions).  
   - Store your API key securely in macOS Keychain.  
   - Make sure the environment variable or keychain entry is accessible to `mcp_server.py`.
3. Run:
   ```sh
   python3 mcp_server.py
   ```
4. Use endpoints:
   - POST `/speak` with `{ "text": "..." }` for text-to-speech
   - GET `/diagnostics` for healthcheck
   - POST `/generate_playlist` to create playlist

### Troubleshooting

- If you are experiencing multiple (e.g., 10) Sleep Mission Control spoken prompts:
  1. Open the Mission Control application/service and review all notification and speech settings. Disable any options related to spoken prompts.
  2. Check for multiple automation scripts, scheduled tasks, or integrations in Mission Control that may be triggering speech repeatedly.
  3. Look for duplicate custom workflows, plugins, or extensions in Mission Control that could be causing multiple spoken notifications.
  4. Use Activity Monitor to see if there are multiple Mission Control or related processes running. Quit all of them.
  5. Review the **Login Items** in System Settings for duplicate entries of Mission Control or related scripts.
  6. Inspect Automator workflows, Calendar alerts, and custom scripts in your user folder for repeated triggers.
  7. Remove or disable any duplicate or unnecessary scripts, tasks, or processes.
  8. Restart your Mac to ensure all changes are applied.
- If the spoken prompts are coming from ElevenLabs TTS:
  - Check the configuration in `mcp_server.py` to ensure ElevenLabs is only called when needed.
  - Review your automation scripts or API calls to avoid repeated or unintended requests to the ElevenLabs service.
  - Inspect logs or output from `mcp_server.py` for excessive ElevenLabs TTS activity.
  - If necessary, temporarily remove your ElevenLabs API key or disable the ElevenLabs integration in your code to stop all ElevenLabs speech.
  - Restart your Mac and the Mission Control service after making changes.
- To immediately mute all system audio output, run this command in Terminal:
  ```sh
  osascript -e "set volume output muted true"
  ```
  This will silence all sounds, including spoken prompts, until you unmute.
- To immediately stop all speech-related processes, run these commands in Terminal:
  ```sh
  pkill -9 -f 'com.apple.speech.synthesis'
  pkill -9 -f 'say'
  pkill -9 -f 'VoiceOver'
  ```
  This will force quit any running speech synthesis, say, or VoiceOver processes.
- To force quit a specific process by its exact name, run this command in Terminal:
  ```sh
  sudo pkill -9 -f 'exact_process_name'
  ```
  Replace `'exact_process_name'` with the actual name of the process you want to stop.
- To fully disable VoiceOver and related spoken services on macOS, you can run:
  ```sh
  osascript -e 'tell application "System Events" to set voiceOverEnabled to false'
  launchctl bootout gui/$(id -u) /System/Library/LaunchAgents/com.apple.VoiceOver.plist 2>/dev/null
  launchctl disable user/$(id -u)/com.apple.VoiceOver
  ```
  This will turn off VoiceOver and prevent it from launching for your user.
- To disable VoiceOver and speech synthesis system-wide, run these commands in Terminal:
  ```sh
  sudo launchctl disable system/com.apple.VoiceOver
  sudo launchctl disable user/$(id -u)/com.apple.speech.synthesis
  ```
  This will prevent VoiceOver and speech synthesis services from launching for all users and at the system level.
- To disable spoken notifications and VoiceOver/spoken feedback system-wide, run these commands in Terminal:
  ```sh
  # Disable spoken notifications
  defaults write com.apple.speech.synthesis.general.prefs SpokenNotificationsEnabled -bool false

  # Disable VoiceOver and spoken feedback
  defaults write com.apple.Accessibility VoiceOverEnabled -bool false
  defaults write com.apple.Accessibility SpokenFeedbackEnabled -bool false
  defaults write com.apple.Accessibility SpeechEnabled -bool false
  ```
  Then restart your Mac to ensure all changes take effect.
- To permanently stop and find all Sleep Mission Control notifications and spoken prompts:
  1. Uninstall or delete the Mission Control application/service from your Applications folder or Launchpad.
  2. In **System Settings > Accessibility > Spoken Content**, turn off all speech-related options ("Speak selection", "System Voice", "Speak announcements", etc.).
  3. Search for and remove any related automation scripts, scheduled tasks (Automator, Calendar, crontab), or background processes that may trigger speech.
  4. Use Activity Monitor to locate and quit any running processes related to Sleep Mission Control.
  5. If you want to find the source of spoken prompts, check the **Login Items** in System Settings, Automator workflows, Calendar alerts, and any custom scripts in your user folder.
  6. Restart your Mac to ensure all changes are applied.
- If ElevenLabs TTS fails, fallback to Siri Kate/Daniel is automatic.
- The fallback system voice is triggered when ElevenLabs TTS is unavailable or fails.  
  This causes macOS to use the voice set in **System Settings > Accessibility > Spoken Content > System Voice** for spoken output.
- To locate and manage the system voice, open **System Settings > Accessibility > Spoken Content > System Voice**.  
  Here you can see which voice is active, select a different one, or turn off "Speak selection" and "System Voice" to stop voice prompts.
- If port is in use, change the port in `mcp_server.py`.
- If your ElevenLabs API key is missing or invalid, check your macOS Keychain or environment variable setup.
- Ensure API key is stored securely in macOS Keychain.
- iCloud sync and playlist require iCloud Drive enabled.

### Features

- Flexible voice selection for automation
- Robust fallback logic
- Secure API key management
- Automated diagnostics and playlist generation

- Note: The commands and troubleshooting steps above are for you to manually scan, identify, and stop speech-related processes, agents, and daemons on your MacStudio.  
  SleepLearning Mission Control does not automatically scan your system; you must run these commands and checks yourself.

- To list all non-Apple launch services currently running, use this command in Terminal:
  ```sh
  launchctl list | grep -v apple
  ```
  This will show all user and system launch agents/daemons except those from Apple.  
  Review the output for any third-party or custom services that may be responsible for spoken prompts.
- When you run `launchctl list | grep -v apple`, the output columns are:
  - **PID**: The process ID of the running service (if active).
  - **Status**: The exit status of the service (0 means running, other values indicate stopped or error).
  - **Label**: The unique identifier for the launch agent or daemon.
  Review these columns to identify and manage any non-Apple services that may be responsible for spoken prompts.
- To list all Launch Agents and Daemons on your system, run these commands in Terminal:
  ```sh
  ls ~/Library/LaunchAgents
  ls /Library/LaunchAgents
  ls /Library/LaunchDaemons
  ```
  Review the output for any files related to speech, voice, Siri, assistant, or SleepLearning Mission Control.  
  You can then investigate, disable, or remove any agents or daemons responsible for spoken prompts.
- To search for Launch Agents or Daemons that may trigger speech or voice services, run this command in Terminal:
  ```sh
  grep -Eil 'say|speech|voice|announce|siri|assistant|spoken' \
    ~/Library/LaunchAgents/*.plist \
    /Library/LaunchAgents/*.plist \
    /Library/LaunchDaemons/*.plist 2>/dev/null
  ```
  This will list any `.plist` files related to speech, voice, Siri, or assistant services in user and system locations.  
  You can review and disable or remove these if they are responsible for spoken prompts.
- To unload and disable a specific user Launch Agent, run these commands in Terminal:
  ```sh
  launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.example.offender.plist
  launchctl disable user/$(id -u)/com.example.offender
  ```
  Replace `com.example.offender` with the actual identifier of the offending Launch Agent you want to stop.
- To unload and disable a specific system Launch Daemon, run these commands in Terminal:
  ```sh
  sudo launchctl bootout system /Library/LaunchDaemons/com.example.offender.plist
  sudo launchctl disable system/com.example.offender
  ```
  Replace `com.example.offender` with the actual identifier of the offending Launch Daemon you want to stop.
- To immediately and permanently stop all spoken prompts:
  1. Uninstall or quit the Mission Control application/service.
  2. Remove or disable any related Launch Agents or Daemons:
     ```sh
     launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.example.offender.plist
     launchctl disable user/$(id -u)/com.example.offender
     sudo launchctl bootout system /Library/LaunchDaemons/com.example.offender.plist
     sudo launchctl disable system/com.example.offender
     ```
     Replace `com.example.offender` with the actual identifier.
  3. Turn off all speech-related options in **System Settings > Accessibility > Spoken Content**.
  4. Run these commands to kill speech processes:
     ```sh
     pkill -9 -f 'say'
     pkill -9 -f 'speech'
     pkill -9 -f 'voiceover'
     pkill -9 -f 'announce'
     pkill -9 -f 'siri'
     pkill -9 -f 'assistant'
     pkill -9 -f 'spoken'
     sudo pkill -9 -f 'com.apple.speech.synthesis'
     sudo pkill -9 -f 'VoiceOver'
     ```
  5. Disable spoken notifications and VoiceOver/spoken feedback:
     ```sh
     defaults write com.apple.speech.synthesis.general.prefs SpokenNotificationsEnabled -bool false
     defaults write com.apple.Accessibility VoiceOverEnabled -bool false
     defaults write com.apple.Accessibility SpokenFeedbackEnabled -bool false
     defaults write com.apple.Accessibility SpeechEnabled -bool false
     ```
  6. Remove any Automator workflows, Calendar alerts, or custom scripts that trigger speech.
  7. Restart your Mac to ensure all changes are applied.

- If you have followed all these steps and speech persists, create a new user account to test, or contact Apple Support for advanced troubleshooting.

- To automate killing all speech and voice processes, you can use a master script like the following:
  - Mutes system audio
  - Kills common TTS and voice processes (`say`, `voiceover`, `speech`, `avspeech`, `siri`)
  - Installs a wrapper for `say` to log invocations
  - Sets up a LaunchAgent to periodically kill speech processes
  - Provides an uninstall helper

- Example master script (run in Terminal, requires admin rights for some steps):

  ```bash
  #!/usr/bin/env bash
  set -euo pipefail

  # --- Configuration ---
  AGENT_LABEL="com.noizyf.killer"
  AGENT_PLIST="$HOME/Library/LaunchAgents/${AGENT_LABEL}.plist"
  WRAPPER_DIR="/usr/local/bin"
  WRAPPER_REAL="/usr/bin/say"
  WRAPPER_LINK="${WRAPPER_DIR}/say"
  LOGDIR="$HOME/noizy_logs"
  INVOCATION_LOG="$LOGDIR/say_invocations.log"
  DIAG_LOG="$LOGDIR/diagnostics.log"
  START_INTERVAL=10

  mkdir -p "$LOGDIR"

  # --- 5) Quick immediate mute and kill to stop current voices while installer finishes ---
  osascript -e "set volume output muted true" 2>/dev/null || true
  pkill -f '\bsay\b' 2>/dev/null || true
  pkill -f -i 'voiceover' 2>/dev/null || true
  pkill -f -i 'speech' 2>/dev/null || true
  pkill -f -i 'avspeech' 2>/dev/null || true
  pkill -f -i 'siri' 2>/dev/null || true

  # Install say wrapper
  if [ ! -d "$WRAPPER_DIR" ]; then
    sudo mkdir -p "$WRAPPER_DIR"
    sudo chown root:wheel "$WRAPPER_DIR"
  fi
  if [ -w "$WRAPPER_DIR" ] || sudo -n true 2>/dev/null; then
    if [ ! -f "${WRAPPER_DIR}/say.real" ]; then
      if [ -f "$WRAPPER_REAL" ]; then
        sudo cp -a "$WRAPPER_REAL" "${WRAPPER_DIR}/say.real" 2>/dev/null || true
      fi
    fi
    sudo tee "${WRAPPER_DIR}/say" > /dev/null <<'EOF'
#!/usr/bin/env bash
LOGFILE="$HOME/noizy_logs/say_invocations.log"
echo "$(date -u) SAY invoked by PID:$PPID USER:$USER ARGS:$*" >> "$LOGFILE"
if [ -x "/usr/local/bin/say.real" ]; then
  exec /usr/local/bin/say.real "$@"
elif [ -x "/usr/bin/say" ]; then
  exec /usr/bin/say "$@"
else
  exit 0
fi
EOF
    sudo chmod 755 "${WRAPPER_DIR}/say"