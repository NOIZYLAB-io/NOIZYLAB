import subprocess
import mido  # pip install mido python-rtmidi
import time

def detect_usb_keyboards():
    cmd = 'ioreg -p IOUSB -l -w 0'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.splitlines()
    keyboards = []
    for line in lines:
        if '"USB Product Name"' in line and any(k in line.lower() for k in ['keyboard', 'novation', 'midi', 'synth']):
            keyboards.append(line)
    return keyboards

def list_midi_ports():
    return mido.get_input_names(), mido.get_output_names()

def midi_bridge(input_port, output_port):
    inport = mido.open_input(input_port)
    outport = mido.open_output(output_port)
    print(f"Bridging {input_port} → {output_port}")
    for msg in inport:
        print(f"Forwarding: {msg}")
        outport.send(msg)

def ai_midi_control():
    # Placeholder for AI-driven MIDI mapping/control
    print("AI MIDI Control: Listening for commands...")
    # You could integrate with an LLM or custom AI agent here

if __name__ == "__main__":
    print("🎹 NoizyFish Lifeboat Rescue Agent Starting...")
    keyboards = detect_usb_keyboards()
    if keyboards:
        print("Detected USB/MIDI Keyboards/Synths:")
        for kb in keyboards:
            print(kb)
    else:
        print("No USB/MIDI keyboards detected.")

    ins, outs = list_midi_ports()
    print("Available MIDI Inputs:", ins)
    print("Available MIDI Outputs:", outs)

    # Example: Bridge first input to first output (customize as needed)
    if ins and outs:
        midi_bridge(ins[0], outs[0])
    else:
        print("No MIDI ports available for bridging.")

    # Start AI MIDI control (expand as needed)
    ai_midi_control()

python lifeboat.py