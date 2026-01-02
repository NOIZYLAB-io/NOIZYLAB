import os
from datetime import datetime

target_path = "/Volumes/YourDriveName"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"/Users/rsp_ms/Desktop/library_index_{timestamp}.txt"

with open(output_file, "w") as f:
    for root, dirs, files in os.walk(target_path):
        for name in files:
            f.write(os.path.join(root, name) + "\n")

print("Scan complete. Output saved to", output_file)
