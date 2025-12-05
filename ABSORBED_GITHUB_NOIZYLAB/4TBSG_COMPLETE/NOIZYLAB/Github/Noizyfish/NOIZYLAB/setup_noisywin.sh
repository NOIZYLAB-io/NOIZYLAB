#!/bin/zsh
# Check & Setup Parallels Desktop with Windows 11 ARM
# VM name: NoizyWind / NoisyWin (handles both)

echo "=== Checking Parallels Desktop installation ==="

# 1. Confirm app exists
if [ -d "/Applications/Parallels Desktop.app" ]; then
    echo "✅ Parallels Desktop is installed."
else
    echo "❌ Parallels Desktop not found in /Applications."
    echo "Please install it from https://www.parallels.com/products/desktop/"
    exit 1
fi

# 2. Check version
if command -v prlctl >/dev/null 2>&1; then
    echo "Parallels CLI is available."
    prlctl --version
else
    echo "❌ prlctl CLI not found. Try restarting or reinstalling Parallels."
    exit 1
fi

# 3. List VMs
echo "=== Current Virtual Machines ==="
prlctl list --all

# 4. Decide on VM name
VM_NAME=""
if prlctl list --all | grep -q "NoizyWind"; then
    VM_NAME="NoizyWind"
elif prlctl list --all | grep -q "NoisyWin"; then
    VM_NAME="NoisyWin"
else
    VM_NAME="NoizyWind"
fi

echo "Using VM name: $VM_NAME"

# 5. If VM exists, start it; if not, create new
if prlctl list --all | grep -q "$VM_NAME"; then
    echo "✅ VM '$VM_NAME' already exists."
    echo "Starting VM..."
    prlctl start "$VM_NAME"
else
    echo "⚙️  VM '$VM_NAME' not found. Creating new Windows 11 VM..."

    prlctl create "$VM_NAME" --ostype win-11 --distribution win11

    # Configure hardware
    prlctl set "$VM_NAME" --cpus 8
    prlctl set "$VM_NAME" --memsize 16384
    prlctl set "$VM_NAME" --vram 1024
    prlctl set "$VM_NAME" --autostart on

    echo "🚀 Starting Windows 11 setup on '$VM_NAME'..."
    prlctl start "$VM_NAME"
    echo "Follow the Windows 11 setup wizard in the Parallels window."
fi

echo "=== Done. '$VM_NAME' should now be running or ready to finish setup. ==="
