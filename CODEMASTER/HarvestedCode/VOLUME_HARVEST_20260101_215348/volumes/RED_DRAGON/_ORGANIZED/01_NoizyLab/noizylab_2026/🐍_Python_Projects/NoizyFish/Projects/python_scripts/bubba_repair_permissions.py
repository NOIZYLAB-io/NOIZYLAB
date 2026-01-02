{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/usr/bin/env python3\
"""\
Bubba Repair Permissions\
Safely reset/fix file ownership and permissions on Mission Control drive.\
"""\
\
import subprocess, getpass\
from pathlib import Path\
from datetime import datetime\
\
VOLUME = "/Volumes/Mission Control"\
LOGS = Path.home() / "Documents/Noizyfish_Aquarium/Noizy_Workspace/Bubba's Bitz/Logs"\
LOGS.mkdir(parents=True, exist_ok=True)\
\
def run(cmd):\
    try:\
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)\
        return out.strip()\
    except subprocess.CalledProcessError as e:\
        return f"ERROR: \{e.output.strip()\}"\
\
def repair_permissions():\
    log = []\
    user = getpass.getuser()\
    log.append(f"=== Bubba Repair Permissions \{datetime.now()\} ===")\
    log.append(f"Target volume: \{VOLUME\}")\
    log.append(f"User: \{user\}")\
\
    # Step 1: First Aid check\
    log.append("Running diskutil verifyVolume...")\
    log.append(run(["diskutil", "verifyVolume", VOLUME]))\
\
    # Step 2: Reset ownership\
    log.append("Resetting ownership...")\
    log.append(run(["sudo", "chown", "-R", f"\{user\}:staff", VOLUME]))\
\
    # Step 3: Reset permissions\
    log.append("Resetting permissions...")\
    log.append(run(["sudo", "chmod", "-R", "u+rwX,go+rX", VOLUME]))\
\
    # Save log\
    logfile = LOGS / f"repair_permissions_\{datetime.now().strftime('%Y%m%d_%H%M%S')\}.log"\
    logfile.write_text("\\n".join(log), encoding="utf-8")\
    return logfile\
\
if __name__ == "__main__":\
    print("\uc0\u55357 \u56615  Bubba is repairing Mission Control permissions...")\
    logfile = repair_permissions()\
    print(f"\uc0\u9989  Done. Full log saved to \{logfile\}")}