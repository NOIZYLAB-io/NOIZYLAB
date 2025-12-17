# Audio Unitor Project

Welcome to **Audio Unitor**, your mission control for pristine audio organization and virtual instrument knowledge.

## 1. "Like New" Audio Organization
We treat your files with respect. No more "Untitled_01" or cluttered Downloads folders.

### How to use:
1.  Place your raw audio packs or messy folders into a source folder (e.g. `Downloads/Inbox`).
2.  Open `Scripts/organize_audio.py` and set your `SOURCE_DIR`.
3.  Run the script:
    ```bash
    python3 Audio_Unitor/Scripts/organize_audio.py
    ```
4.  The script will **simulate** a reorganization into `Audio_Unitor/Staging_Area`.
    -   Files are sorted into cleaned, Title-Cased folder names.
    -   Junk files are ignored.
5.  Uncomment the `shutil.move` line in the script to apply changes for real.

## 2. Google Drive Sync
Once your Staging Area is perfect, beam it up to the cloud.

We use **rclone** for reliable, fast syncing.
Check out the workflow guide:
`/.agent/workflows/google_drive_sync.md`
(Or just ask me to "Run the drive sync workflow" once you have rclone installed).

## 3. The Unitor Brain (Virtual Instrument Database)
We are building the ultimate index of every VI release.
See `Audio_Unitor/Database/vi_db.json`.

Current Status: **Seed**
-   Contains structure (ID, Developer, Type, Release Date).
-   Ready for expansion.

**Tonight's Mission:**
-   Expand the database?
-   Organize your local files?
-   Sync to Drive?

## 4. ANTI-PARALYSIS PROTOCOL (Turbo Mode)
If you are feeling stuck or overwhelmed, use the **Turbo Modes**.

### Option A: Manual Turbo
1.  Drag files to `~/Downloads/Audio_Inbox`.
2.  Run: `/clean_audio_turbo`

### Option B: 🚀 HYPER-DRIVE (Always On)
0% Latency. Continuous Processing.

1.  Run this in your terminal:
    ```bash
    python3 Audio_Unitor/Scripts/hyper_drive_watcher.py
    ```
2.  Leave that terminal window open.
3.  Any file you drop into `~/Downloads/Audio_Inbox` will be **INSTANTLY** teleported, cleaned, and sorted into your Staging Area.
4.  No commands. No questions. Just speed.

You decide, Commander.
