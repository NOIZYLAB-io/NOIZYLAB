---
description: Deploy the locally organized Audio Universe to Google Drive (gdrive:MC96UNIVERSE)
---

This workflow syncs your pristine `Staging_Area` to the Cloud.

1.  **Authentication (First Time Only)**
    You need to link your Google Drive. Run this in the terminal:
    ```bash
    rclone config
    ```
    -   Press `n` (New Remote).
    -   Name it: `gdrive`
    -   Select `Google Drive` (Type the number, usually around 18).
    -   Press `Enter` through defaults until it gives you a link to login.
    -   Login with your Google Account.

2.  **Deploy to the Universe**
    Once authenticated, run the deployment script:
    
    ```bash
    python3 Audio_Unitor/Scripts/deploy_to_universe.py
    ```
    
    This will:
    -   Scan your local `Audio_Unitor/Staging_Area`.
    -   Sync everything to a folder named `MC96UNIVERSE` on your Drive.
    -   It is "Like New" (Perfect Mirror).
