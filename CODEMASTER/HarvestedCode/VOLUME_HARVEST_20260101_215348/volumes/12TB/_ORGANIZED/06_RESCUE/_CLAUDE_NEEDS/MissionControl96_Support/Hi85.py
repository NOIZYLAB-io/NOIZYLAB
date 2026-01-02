import os
import subprocess
from pathlib import Path

# === CONFIGURATION ===
VM_NAME = "NOIZYWIN-FORGE"
ISO_PATH = Path.home() / "Downloads" / "Win10_ARM.iso"
NOIZYWIN_FOLDER = Path.home() / "NOIZYWIN"
MEMORY_MB = "8192"
CPU_COUNT = "4"

def run(cmd):
    print(f"🔧 Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

# === STEP 1: Create VM ===
def create_vm():
    run(["prlctl", "create", VM_NAME, "--distribution", "win-10-arm", "--vmtype", "vm"])
    run(["prlctl", "set", VM_NAME, "--mem", MEMORY_MB, "--cpus", CPU_COUNT, "--cpu-hotplug", "on"])

# === STEP 2: Mount ISO ===
def mount_iso():
    run(["prlctl", "set", VM_NAME, "--device-add", "cdrom", "--image", str(ISO_PATH)])

# === STEP 3: Mount Shared Folder ===
def mount_shared_folder():
    run(["prlctl", "set", VM_NAME, "--shf-host-add", str(NOIZYWIN_FOLDER), "--shf-host-name", "NOIZYWIN"])

# === STEP 4: Start VM ===
def start_vm():
    run(["prlctl", "start", VM_NAME])

# === STEP 5: Inject Ritual Scripts ===
def inject_assets():
    NOIZYWIN_FOLDER.mkdir(exist_ok=True)
    (NOIZYWIN_FOLDER / "hotrod.ps1").write_text("""# NOIZYWIN Hotrod Ritual
Write-Host "🔥 Starting NOIZYWIN branding ritual..."

# Debloat
Get-AppxPackage -AllUsers | Remove-AppxPackage
Get-AppxProvisionedPackage -Online | Remove-AppxProvisionedPackage -Online

# Branding
Set-ItemProperty -Path 'HKCU:\\Control Panel\\Desktop' -Name Wallpaper -Value "C:\\NOIZYWIN\\wallpaper.jpg"
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

# Healing
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File C:\\NOIZYWIN\\ethernet-healer.ps1"

# Snapshot
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File C:\\NOIZYWIN\\snapshot.ps1"
""")

    (NOIZYWIN_FOLDER / "ethernet-healer.ps1").write_text("""$eth = Get-NetAdapter | Where-Object {$_.Status -eq "Up" -and $_.Name -like "*Ethernet*"}
If ($eth) {
  Set-NetIPInterface -InterfaceAlias $eth.Name -Dhcp Enabled
}""")

    (NOIZYWIN_FOLDER / "snapshot.ps1").write_text("""Checkpoint-Computer -Description "NOIZYWIN Ritual Snapshot" -RestorePointType "APPLICATION_INSTALL"
Write-Host "🧙 Snapshot created."""")

    print("✅ NOIZYWIN assets injected.")

# === MAIN RITUAL ===
def main():
    inject_assets()
    create_vm()
    mount_iso()
    mount_shared_folder()
    start_vm()
    print("🎉 NOIZYWIN VM is forged and ready to install.")

if __name__ == "__main__":
    main()
