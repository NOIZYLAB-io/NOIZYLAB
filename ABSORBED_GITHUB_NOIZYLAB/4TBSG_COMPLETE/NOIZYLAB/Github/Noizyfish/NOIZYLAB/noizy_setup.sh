#!/bin/zsh
# Clean Windows 11 VM setup for Parallels
# Targets: "Windows 11"

VM_NAME="Windows 11"
ISO_PATH=~/Downloads/Win11_ARM64.iso   # adjust if needed

echo "=== Noizy Setup for $VM_NAME ==="

# Make sure VM is off
echo "⚙️ Stopping VM (if running)..."
prlctl stop "$VM_NAME" --kill 2>/dev/null

# Configure hardware for a Mac Studio balance
echo "🔧 Setting performance profile..."
prlctl set "$VM_NAME" --cpus 8
prlctl set "$VM_NAME" --memsize 16384
prlctl set "$VM_NAME" --vram 1024
prlctl set "$VM_NAME" --autostart on
prlctl set "$VM_NAME" --startup-view fullscreen

# Attach ISO if available
if [ -f "$ISO_PATH" ]; then
  echo "📀 Attaching Windows 11 ISO..."
  prlctl set "$VM_NAME" --device-del cdrom 2>/dev/null
  prlctl set "$VM_NAME" --device-add cdrom --image "$ISO_PATH"
else
  echo "⚠️ Windows ISO not found at $ISO_PATH"
  echo "Parallels GUI can auto-download it (File → New → Get Windows 11)."
fi

# Shared folders
echo "📂 Setting up shared folders..."
prlctl set "$VM_NAME" --shf-host-add Desktop --path ~/Desktop
prlctl set "$VM_NAME" --shf-host-add Documents --path ~/Documents
prlctl set "$VM_NAME" --shf-host-add Music --path ~/Music
prlctl set "$VM_NAME" --shf-host-add Projects --path ~/Documents/projects 2>/dev/null

# Boot VM
echo "🚀 Starting VM..."
prlctl start "$VM_NAME"

# Take a snapshot for rollback
echo "📸 Creating baseline snapshot..."
prlctl snapshot "$VM_NAME" --name "Noizy-FreshSetup"

echo "=== ✅ Windows 11 VM is ready. Run the installer if prompted, then install Parallels Tools inside Windows. ==="
