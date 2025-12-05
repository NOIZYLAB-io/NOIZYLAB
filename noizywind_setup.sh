#!/bin/zsh
# noizywind_setup.sh
# One-shot setup for Parallels VM "NoizyWind" with Parallels Tools

VM_NAME="NoizyWind"
ISO_PATH="/Applications/Parallels Desktop.app/Contents/Resources/Tools/prl-tools-win.iso"

echo "🚀 Preparing $VM_NAME ..."

# 1. Make sure the VM exists
prlctl list --all | grep "$VM_NAME" || {
  echo "⚠️ VM $VM_NAME not found. Create it first with Parallels Desktop GUI or prlctl."
  exit 1
}

# 2. Stop the VM if it's running
echo "🛑 Stopping $VM_NAME if running..."
prlctl stop "$VM_NAME" --kill || true

# 3. Configure startup
echo "⚙️ Setting startup config..."
prlctl set "$VM_NAME" --startup-view window
prlctl set "$VM_NAME" --startup-auto off

# 4. Start the VM
echo "▶️ Starting $VM_NAME ..."
prlctl start "$VM_NAME"

# Wait for Windows to boot
sleep 30

# 5. Mount Parallels Tools ISO
echo "💿 Mounting Parallels Tools..."
prlctl set "$VM_NAME" --device-add cdrom --image "$ISO_PATH" || true

# 6. Run installer inside Windows
echo "⚙️ Installing Parallels Tools inside VM..."
prlctl exec "$VM_NAME" powershell -command "Start-Process 'D:\Setup.exe' -Verb runAs"

# 7. Done
echo "✅ Parallels Tools install triggered. Complete the install in Windows if prompted."
