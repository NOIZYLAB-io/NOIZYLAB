import subprocess
import os
import openai

VM_NAME = "Windows10"
ISO_PATH = "/Users/yourname/Downloads/Win10.iso"  # Change this to your actual ISO path

openai.api_key = "your-api-key"  # Replace with your actual API key

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}\n{e.stderr}")
        return None

def prlctl_exists():
    return run_cmd(['which', 'prlctl']) is not None

def iso_exists():
    return os.path.isfile(ISO_PATH)

def vm_exists():
    vms = run_cmd(['prlctl', 'list', '--all'])
    return VM_NAME in vms if vms else False

def vm_status():
    vms = run_cmd(['prlctl', 'list', '--all'])
    for line in vms.splitlines():
        if VM_NAME in line:
            return line.split()[2]  # status column
    return None

def create_vm():
    print("Creating VM...")
    run_cmd(['prlctl', 'create', VM_NAME, '--distribution', 'win-10'])

def attach_iso():
    print("Attaching ISO...")
    run_cmd(['prlctl', 'set', VM_NAME, '--device-set', 'cdrom0', '--image', ISO_PATH])

def start_vm():
    print("Starting VM...")
    run_cmd(['prlctl', 'start', VM_NAME])

def transcribe_audio(file_path):
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=open(file_path, "rb")
    )
    return response['text']

def main():
    print("=== Parallels Desktop Windows 10 VM Automation ===")
    if not prlctl_exists():
        print("❌ Parallels CLI (prlctl) not found. Please install Parallels Desktop.")
        return
    if not iso_exists():
        print(f"❌ Windows 10 ISO not found at {ISO_PATH}")
        print("Download it from https://www.microsoft.com/software-download/windows10ISO")
        return
    if not vm_exists():
        create_vm()
        attach_iso()
    else:
        print(f"VM '{VM_NAME}' already exists.")
        attach_iso()
    status = vm_status()
    if status == "running":
        print(f"VM '{VM_NAME}' is already running.")
    else:
        start_vm()
    print("\n✅ VM setup automated. Complete Windows installation inside the Parallels window.")

if __name__ == "__main__":
    main()
    os.system('python3 transcribe_audio.py')
    os.system('pip install openai')