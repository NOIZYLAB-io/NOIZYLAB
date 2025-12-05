#!/bin/zsh
rm -rf ~/Downloads/* ~/Library/Caches/*

<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.rspms.backup</string>
  <key>ProgramArguments</key>
  <array>
    <string>/Users/rsp_ms/auto_backup.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>2</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>

class HealthHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Change detected: {event.src_path}")
        with open("/Users/rsp_ms/watchdog.log", "a") as log:
            log.write(f"{time.ctime()}: Change detected: {event.src_path}\n")
        # Autoheal: restart a service or run a repair script
        os.system("~/cleanup.sh")
        os.system("~/auto_backup.sh")
        # Add more as needed

C:\MissionControl96\Scripts\
  ├─ VSCode\
  ├─ Backup\
  ├─ GraphAPI\
  ├─ Cleanup\
  ├─ Monitoring\
  └─ README.md

"files.autoSave": "afterDelay"

API_KEY = 'your_godaddy_api_key'

import os
print(os.getenv("GD_KEY"))
print(os.getenv("GD_SECRET"))
