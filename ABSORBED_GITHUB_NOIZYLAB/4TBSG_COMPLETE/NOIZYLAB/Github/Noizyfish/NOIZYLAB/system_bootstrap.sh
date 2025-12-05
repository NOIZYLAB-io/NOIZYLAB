#!/bin/zsh
echo "🚀 Starting Mac Studio Bootstrap — Finder, Terminal, Utilities, Cleanup"

# 1. Create Utilities Folder Structure
UTIL=~/Documents/_The_Aquarium/_utilities
mkdir -p $UTIL/{scripts,_documents,logs}
echo "📁 Utilities folder ready at $UTIL"

# 2. Convert stray RTF/TextEdit files into usable .py scripts
for f in ~/Documents/_The_Aquarium/_shell_scripts/*.rtf; do
  [ -f "$f" ] || continue
  base=$(basename "$f" .rtf)
  textutil -convert txt "$f" -output "$UTIL/scripts/$base.py"
  cp "$UTIL/scripts/$base.py" "$UTIL/_documents/$base.py.txt"
  echo "📝 Converted $f → $base.py"
done

# 3. Drop in Desktop Cleaner utility
cat > $UTIL/scripts/clean_desktop.py <<'EOF'
import os, shutil, datetime
desktop = os.path.expanduser("~/Desktop")
aquarium = os.path.expanduser("~/Documents/_The_Aquarium")
folders_dest = os.path.join(aquarium, "_folders")
unassigned = os.path.join(aquarium, "_unassigned")
log_dir = os.path.join(aquarium, "_utilities/logs")
os.makedirs(folders_dest, exist_ok=True)
os.makedirs(unassigned, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "desktop_cleanup_log.txt")
def log(msg):
    with open(log_file, "a") as logf:
        logf.write(f"[{datetime.datetime.now()}] {msg}\n")
for item in os.listdir(desktop):
    path = os.path.join(desktop, item)
    if os.path.isdir(path):
        if not os.listdir(path):
            os.rmdir(path); log(f"Deleted empty folder: {item}")
        else:
            dest = os.path.join(folders_dest, item)
            if os.path.exists(dest):
                dest = os.path.join(folders_dest, f"{item}_{int(datetime.datetime.now().timestamp())}")
            shutil.move(path, dest); log(f"Moved folder {item} -> {dest}")
    elif os.path.isfile(path):
        dest = os.path.join(unassigned, item)
        if os.path.exists(dest):
            base, ext = os.path.splitext(item)
            dest = os.path.join(unassigned, f"{base}_{int(datetime.datetime.now().timestamp())}{ext}")
        shutil.move(path, dest); log(f"Moved file {item} -> {dest}")
print("✅ Desktop cleaned. Check _The_Aquarium/_folders and _The_Aquarium/_unassigned.")
EOF
cp $UTIL/scripts/clean_desktop.py $UTIL/_documents/clean_desktop.py.txt
echo "🧹 Desktop cleaner installed"

# 4. Finder defaults (column view + window size)
osascript <<'EOF'
tell application "Finder"
    activate
    set current view of Finder window 1 to column view
    set bounds of Finder window 1 to {100, 100, 1200, 800}
end tell
EOF
echo "📐 Finder window defaults set (Column view, 100x100→1200x800)"

# 5. Terminal defaults (rows/columns)
osascript <<'EOF'
tell application "Terminal"
    set default settings to settings set "Basic"
    set number of columns of default settings to 100
    set number of rows of default settings to 35
end tell
EOF
echo "🖥️ Terminal defaults applied (100 cols × 35 rows)"

# 6. Terminal Position AppleScript
cat > $UTIL/scripts/terminal_position.scpt <<'APPLESCRIPT'
tell application "Terminal"
    activate
    if (count of windows) is 0 then
        do script ""
    end if
    set bounds of front window to {100, 100, 1200, 800}
end tell
APPLESCRIPT
echo "📌 Terminal positioning script ready"

# 7. Run desktop cleanup immediately
python3 $UTIL/scripts/clean_desktop.py

echo "🎉 Bootstrap complete! Utilities ready, Finder/Terminal set, Desktop cleaned."
