#!/usr/bin/env python3

import subprocess

# 🧞 Slab Input Mapping
PLANAR_INPUTS = {
    "StudioSlab": "HDMI1",
    "PowerSlab": "HDMI2"
}

# 🧠 Ritual Command (example using cec-client or smart dock API)
def switch_input(slab_name):
    input_port = PLANAR_INPUTS.get(slab_name)
    if not input_port:
        print(f"❌ Unknown slab: {slab_name}")
        return

    # Replace with actual command for your switcher
    command = f"echo 'tx 10:82:{input_port}' | cec-client"
    subprocess.run(command, shell=True)
    print(f"🧞 Planar slab now channeling {slab_name} via {input_port}")

# 🧬 Example Usage
switch_input("PowerSlab")  # Possess Planar with Mac Pro
