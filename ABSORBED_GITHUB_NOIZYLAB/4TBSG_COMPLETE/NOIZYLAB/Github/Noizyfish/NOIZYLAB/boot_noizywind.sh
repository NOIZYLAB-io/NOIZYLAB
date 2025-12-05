#!/bin/zsh
# Auto-detect and boot Windows 11 VM with installer

ISO_PATH=~/Downloads/Win11_ARM64.iso   # <--- change if ISO is elsewhere

echo "=== Checking available Parallels VMs ==="
VM_NAME=$(prlctl list --all | awk '{print $3}' | grep -E "NoizyWind|Windows" | head -n1)

if [ -z "$VM_NAME" ]; then
  echo "❌ No VM found named NoizyWind or Windows 11. Create one first."
  exit 1
fi

echo "✅ Using VM: $VM_NAME"

# Stop if running
echo "⚙️ Ensuring VM is stopped..."
prlctl stop "$VM_NAME" --kill 2>/dev/null

# Attach ISO
if [ -f "$ISO_PATH" ]; then
  echo "📀 Attaching Windows 11 ARM ISO..."
  prlctl set "$VM_NAME" --device-del cdrom 2>/dev/null
  prlctl set "$VM_NAME" --device-add cdrom --image "$ISO_PATH"
else
  echo "❌ ISO not found at $ISO_PATH"
  echo "Download Windows 11 ARM64 ISO first, then rerun."
  exit 1
fi

# Start VM
echo "🚀 Booting into Windows installer..."
prlctl start "$VM_NAME"

echo "=== All set! Follow the on-screen Windows setup ==="
