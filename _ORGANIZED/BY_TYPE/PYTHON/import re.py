import re
import json

input_file = "logic_pro_x_editing_control.txt"  # Your raw text file
output_file = "logic_pro_x_commands.json"

commands = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # Skip section headers and empty lines
        if not line or line.startswith("-") or line.startswith("Command") or line.startswith("Key") or line.startswith("Touch Bar"):
            continue
        # Match: Command [tab] Key [tab] Touch Bar
        parts = re.split(r"\t+", line)
        if len(parts) == 1:
            command = parts[0]
            key = ""
            touchbar = ""
        elif len(parts) == 2:
            command, key = parts
            touchbar = ""
        elif len(parts) == 3:
            command, key, touchbar = parts
        else:
            continue
        commands.append({
            "command": command.strip(),
            "key": key.strip(),
            "touchbar": touchbar.strip()
        })

with open(output_file, "w", encoding="utf-8") as out:
    json.dump(commands, out, indent=2, ensure_ascii=False)

print(f"Extracted {len(commands)} Logic Pro X commands to {output_file}")