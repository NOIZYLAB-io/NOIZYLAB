#!/bin/zsh

# VM name
VM_NAME="NOIZYWIND"

# Paths to your ISOs (download from Microsoft)
ISO_64="$HOME/Downloads/Win10_64.iso"
ISO_32="$HOME/Downloads/Win10_32.iso"

# Ask user which build to use
echo "Which Windows 10 version do you want to install?"
echo "1) Windows 10 64-bit (modern, best performance)"
echo "2) Windows 10 32-bit (legacy software support)"
read "CHOICE?Choose [1 or 2]: "

if [ "$CHOICE" = "1" ]; then
  ISO_PATH="$ISO_64"
  ARCH="x64"
elif [ "$CHOICE" = "2" ]; then
  ISO_PATH="$ISO_32"
  ARCH="x86"
else
  echo "❌ Invalid choice. Exiting."
  exit 1
fi

echo "⚠️ Removing any old NOIZYWIND VM..."
prlctl stop "$VM_NAME" --kill 2>/dev/null
prlctl unregister "$VM_NAME" 2>/dev/null
rm -rf "$HOME/Parallels/$VM_NAME.pvm"

echo "🛠 Creating new NOIZYWIND VM for Windows 10 $ARCH..."
prlctl create "$VM_NAME" --distribution win-10 --location "$HOME/Parallels"

echo "📀 Attaching chosen ISO ($ISO_PATH)..."
prlctl set "$VM_NAME" --device-set cdrom0 --connect --image "$ISO_PATH"

echo "⚙️ Configuring hardware..."
prlctl set "$VM_NAME" --cpus 2
prlctl set "$VM_NAME" --memsize 8192
prlctl set "$VM_NAME" --3d-accelerate on
prlctl set "$VM_NAME" --resolution 1280x800
prlctl set "$VM_NAME" --on-window-close keep-running

echo "🚀 Booting installer..."
prlctl start "$VM_NAME"

echo "✅ Windows 10 $ARCH setup launched! Use 'Custom (Advanced)' and let it format NTFS."

~/Desktop/NoizyFish/scripts/setup_noizywind.sh