---
description: Automatically organize audio files from Downloads without asking for confirmation for every step.
---

// turbo-all

This workflow will:
1.  Check the Downloads folder for an 'Audio_Inbox' folder.
2.  If it exists, run the organizer script in LIVE mode.
3.  Show the results.

FAIL-SAFE: If `Downloads/Audio_Inbox` doesn't exist, it will just warn you.

1.  Check for source directory
    ```bash
    if [ -d "$HOME/Downloads/Audio_Inbox" ]; then echo "Inbox found."; else echo "Inbox NOT found. Please create $HOME/Downloads/Audio_Inbox and put files there."; fi
    ```

2.  Run the Organizer (Live Mode)
    ```bash
    if [ -d "$HOME/Downloads/Audio_Inbox" ]; then python3 Audio_Unitor/Scripts/organize_audio.py --source "$HOME/Downloads/Audio_Inbox" --live; fi
    ```
