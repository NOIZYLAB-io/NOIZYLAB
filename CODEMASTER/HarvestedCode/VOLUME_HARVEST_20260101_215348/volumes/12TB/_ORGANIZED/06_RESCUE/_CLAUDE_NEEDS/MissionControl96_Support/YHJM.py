"editor.accessibilitySignalTimeout": 3000,

summary = []
for vol in VOLUMES.iterdir():
    # Skip hidden/system volumes, non-directories, or volumes in SKIP_VOLUMES
    if vol.name.startswith('.') or not vol.is_dir() or vol.name in SKIP_VOLUMES:
        continue
    alias_path = SUBFOLDER / vol.name
    if alias_path.exists():
        if alias_path.is_symlink() and os.readlink(str(alias_path)) == str(vol):
            msg = f"Alias already exists and is correct: {alias_path}"
        else:
            msg = f"Alias already exists but may be incorrect: {alias_path}"
        print(msg)
        summary.append(f"• {msg}")
        continue
    try:
        os.symlink(str(vol), str(alias_path))
        msg = f"Created alias for {vol} -> {alias_path}"
        print(msg)
        summary.append(f"• {msg}")
    except PermissionError:
        msg = f"Permission denied: Failed to create alias for {vol}"
        print(msg)
        summary.append(f"• {msg}")
    except Exception as e:
        msg = f"Failed to create alias for {vol}: {e}"
        print(msg)
        summary.append(f"• {msg}")

print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")
print("\nSummary:")
for line in summary[-2:]:
    print(line)