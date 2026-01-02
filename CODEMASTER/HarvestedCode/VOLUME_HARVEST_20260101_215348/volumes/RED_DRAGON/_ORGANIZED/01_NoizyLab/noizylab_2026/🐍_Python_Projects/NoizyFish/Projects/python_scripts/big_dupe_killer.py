Last login: Tue Sep 23 03:13:11 on ttys021
rsp_ms@RSPMS ~ % sudo chown -R "$USER":staff "/Volumes/Noizy Wind"
Password:
chown: /Volumes/Noizy Wind: No such file or directory
rsp_ms@RSPMS ~ % mkdir -p "/Volumes/NoizyWind/NoizyWorkspace"
rsp_ms@RSPMS ~ % ls -ld "/Volumes/NoizyWind/NoizyWorkspace"
drwx------  1 rsp_ms  staff  131072 Sep 23 03:17 /Volumes/NoizyWind/NoizyWorkspace
rsp_ms@RSPMS ~ % ls -ld "/Volumes/NoizyWind/NoizyWorkspace"
drwx------  1 rsp_ms  staff  131072 Sep 23 03:17 /Volumes/NoizyWind/NoizyWorkspace
rsp_ms@RSPMS ~ % ~/Documents/_The_Aquarium/_projects/big_dupe_killer/big_dupe_killer.py
zsh: no such file or directory: /Users/rsp_ms/Documents/_The_Aquarium/_projects/big_dupe_killer/big_dupe_killer.py
rsp_ms@RSPMS ~ % mkdir -p ~/Documents/_The_Aquarium/_projects/big_dupe_killer

cat > ~/Documents/_The_Aquarium/_projects/big_dupe_killer/big_dupe_killer.py <<'EOF'
#!/usr/bin/env python3
import os, hashlib, shutil

# Folders to scan for dupes — start small (Desktop + NoizyWorkspace)
targets = [
    os.path.expanduser("~/Desktop"),
    "/Volumes/NoizyWind/NoizyWorkspace"
]

# Where to stash dupes (keeps originals safe)
dupe_dir = os.path.expanduser("~/Documents/_The_Aquarium/_projects/big_dupe_killer/dupes")
os.makedirs(dupe_dir, exist_ok=True)

def filehash(path, blocksize=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(blocksize), b""):
            h.update(chunk)
    return h.hexdigest()

seen = {}
for folder in targets:
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                h = filehash(path)
            except Exception as e:
                print(f"⚠️ Skipped {path}: {e}")
                continue

            if h in seen:
                base = os.path.basename(path)
                dest = os.path.join(dupe_dir, base)
                counter = 1
                while os.path.exists(dest):
                    base_name, ext = os.path.splitext(base)
                    dest = os.path.join(dupe_dir, f"{base_name}_{counter}{ext}")
                    counter += 1
                shutil.move(path, dest)
                print(f"🗑️ Duplicate moved: {path} → {dest}")
            else:
                seen[h] = path

print("✅ Big Dupe Killer finished. Check 'dupes' folder in the project.")
EOF

chmod +x ~/Documents/_The_Aquarium/_projects/big_dupe_killer/big_dupe_killer.py
