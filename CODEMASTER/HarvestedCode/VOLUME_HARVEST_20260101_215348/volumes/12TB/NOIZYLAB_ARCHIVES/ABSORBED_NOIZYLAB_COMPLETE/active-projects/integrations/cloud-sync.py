#!/usr/bin/env python3
"""
Cloud Sync - Sync data across devices via iCloud/Google Drive
==============================================================
"""

import shutil
import json
from pathlib import Path
from datetime import datetime

class CloudSync:
    def __init__(self):
        self.icloud_path = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/NoizyLab"
        self.sync_config = {
            "email_intelligence": "email-intelligence/email_intelligence.db",
            "blocklist": "universal-blocker/blocklist.txt",
            "spam_patterns": "imessage-spam-filter/patterns.json"
        }
    
    def sync_to_cloud(self):
        """Sync all data to iCloud"""
        self.icloud_path.mkdir(parents=True, exist_ok=True)
        
        for name, path in self.sync_config.items():
            source = Path(f"/Users/m2ultra/NOIZYLAB/{path}")
            dest = self.icloud_path / Path(path).name
            
            if source.exists():
                shutil.copy2(source, dest)
                print(f"✅ Synced {name}")
    
    def sync_from_cloud(self):
        """Sync data from iCloud"""
        for name, path in self.sync_config.items():
            source = self.icloud_path / Path(path).name
            dest = Path(f"/Users/m2ultra/NOIZYLAB/{path}")
            
            if source.exists():
                shutil.copy2(source, dest)
                print(f"✅ Restored {name}")

if __name__ == "__main__":
    sync = CloudSync()
    sync.sync_to_cloud()

