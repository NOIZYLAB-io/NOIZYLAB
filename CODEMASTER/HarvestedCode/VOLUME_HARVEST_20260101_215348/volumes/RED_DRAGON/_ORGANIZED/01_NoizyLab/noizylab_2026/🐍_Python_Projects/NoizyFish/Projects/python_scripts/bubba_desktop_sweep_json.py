{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;}
{\colortbl;\red255\green255\blue255;\red14\green14\blue14;}
{\*\expandedcolortbl;;\cssrgb\c6700\c6700\c6700;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\fs28 \cf2 #!/usr/bin/env python3\
"""\
Manage macOS Voice Control custom commands plist.\
Export, import, or delete the file safely.\
"""\
\
import shutil\
from pathlib import Path\
\
plist_path = Path.home() / "Library/Preferences/com.apple.speech.recognition.AppleSpeechRecognitionCustomCommands.plist"\
backup_path = Path.home() / "Documents/VoiceControl_Backup.plist"\
\
def export_commands():\
    if plist_path.exists():\
        shutil.copy2(plist_path, backup_path)\
        print(f"\uc0\u9989  Exported commands to \{backup_path\}")\
    else:\
        print("\uc0\u9888 \u65039  No commands plist found to export.")\
\
def import_commands():\
    if backup_path.exists():\
        shutil.copy2(backup_path, plist_path)\
        print(f"\uc0\u9989  Restored commands from \{backup_path\}")\
        print("You may need to restart Voice Control for changes to apply.")\
    else:\
        print("\uc0\u9888 \u65039  No backup found to import.")\
\
def delete_commands():\
    if plist_path.exists():\
        plist_path.unlink()\
        print("\uc0\u55357 \u56785  Deleted custom commands plist. Voice Control will reset.")\
    else:\
        print("\uc0\u9888 \u65039  Nothing to delete, plist not found.")\
\
if __name__ == "__main__":\
    print("Voice Control Command Manager")\
    print("1) Export")\
    print("2) Import")\
    print("3) Delete All")\
    choice = input("Choose an option: ").strip()\
    if choice == "1":\
        export_commands()\
    elif choice == "2":\
        import_commands()\
    elif choice == "3":\
        delete_commands()\
    else:\
        print("No action taken.")}