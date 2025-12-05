#!/bin/zsh
# Noizy Full Setup — macOS side
# Runs top-to-tail: Parallels config + Windows bootstrap delivery + optional auto-run

set -euo pipefail

# ====== EDIT THESE IF NEEDED ======
VM_NAME="Windows 11"                 # Your target VM name (quotes needed if spaces)
ISO_PATH="$HOME/Downloads/Win11_ARM64.iso"  # Optional; Parallels can download via GUI if missing
CPUS=8
RAM_MB=16384
VRAM_MB=1024
AUTOSTART="on"
STARTUP_VIEW="fullscreen"
# Optional: set these ONLY if you want the script to auto-run bootstrap inside Windows.
WIN_USER=""     # e.g. "rob"
WIN_PASS=""     # e.g. "YourStrongPassword!"
# ==================================

say_done() { echo "✅ $1"; }
say_step() { echo "\n=== $1 ==="; }

say_step "Checking Parallels Desktop / prlctl"
[ -d "/Applications/Parallels Desktop.app" ] || { echo "❌ Parallels not installed."; exit 1; }
command -v prlctl >/dev/null || { echo "❌ prlctl not found (restart Parallels)."; exit 1; }
prlctl --version || true
say_done "Parallels CLI ready"

say_step "Verifying VM exists: $VM_NAME"
if ! prlctl list --all | awk '{print substr($0,index($0,$4)) }' | grep -Fx "$VM_NAME" >/dev/null; then
  echo "❌ VM '$VM_NAME' not found. Use Parallels GUI (File → New) to create Windows 11, or rename VM_NAME."
  exit 1
fi
say_done "VM found"

say_step "Stopping VM (if running)"
prlctl stop "$VM_NAME" --kill >/dev/null 2>&1 || true
say_done "Stopped"

say_step "Configuring hardware"
prlctl set "$VM_NAME" --cpus $CPUS
prlctl set "$VM_NAME" --memsize $RAM_MB
prlctl set "$VM_NAME" --vram $VRAM_MB
prlctl set "$VM_NAME" --autostart $AUTOSTART
prlctl set "$VM_NAME" --startup-view $STARTUP_VIEW
say_done "CPU/RAM/VRAM/autostart/startup-view applied"

say_step "Attaching Windows ISO (if present)"
if [ -f "$ISO_PATH" ]; then
  prlctl set "$VM_NAME" --device-del cdrom >/dev/null 2>&1 || true
  prlctl set "$VM_NAME" --device-add cdrom --image "$ISO_PATH"
  say_done "ISO attached"
else
  echo "⚠️ ISO not found at $ISO_PATH — ok if Windows already installed. Parallels GUI can fetch it."
fi

say_step "Setting up shared folders"
# Ensure predictable host directories
BOOTSTRAP_HOST="$HOME/NoizyBootstrap"
mkdir -p "$BOOTSTRAP_HOST"
mkdir -p "$HOME/Desktop" "$HOME/Documents" "$HOME/Music"
# Add shares (idempotent)
prlctl set "$VM_NAME" --shf-host-add Desktop   --path "$HOME/Desktop"   >/dev/null 2>&1 || true
prlctl set "$VM_NAME" --shf-host-add Documents --path "$HOME/Documents" >/dev/null 2>&1 || true
prlctl set "$VM_NAME" --shf-host-add Music     --path "$HOME/Music"     >/dev/null 2>&1 || true
prlctl set "$VM_NAME" --shf-host-add Bootstrap --path "$BOOTSTRAP_HOST" >/dev/null 2>&1 || true
say_done "Shared folders ready"

say_step "Installing Parallels Tools (if needed)"
# Tools install requires the VM running; we’ll start, request tools, and wait a bit.
prlctl start "$VM_NAME" >/dev/null 2>&1 || true
# Try to detect if tools already present by a lightweight command
if prlctl exec "$VM_NAME" "cmd /c ver" >/dev/null 2>&1; then
  say_done "Parallels Tools already active"
else
  prlctl installtools "$VM_NAME" || true
  echo "⏳ Waiting 30s for Tools mount/prompt..."
  sleep 30
fi

say_step "Powering off to finalize host-side config"
prlctl stop "$VM_NAME" --kill >/dev/null 2>&1 || true
say_done "Stopped"

say_step "Drop Windows bootstrap into shared folder"
BOOT_PS="$BOOTSTRAP_HOST/bootstrap.ps1"
cat > "$BOOT_PS" <<'EOF'
# Noizy Windows Bootstrap — run in elevated PowerShell (Run as Administrator)
# Sets power plan, UX prefs, enables features, installs apps via winget, then reboots.

$ErrorActionPreference = "Stop"

Write-Host "=== Noizy Bootstrap starting ==="

# 1) Make sure winget is available (Windows 11 should have it)
try {
  winget --version | Out-Null
} catch {
  Write-Host "winget missing. Install App Installer from Microsoft Store, then re-run."
  exit 1
}

# 2) Power plan: High performance (or Ultimate if available)
Write-Host "Setting High Performance power plan..."
powercfg -setactive SCHEME_MIN

# 3) Show file extensions & hidden items
Write-Host "Showing file extensions and hidden items..."
New-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name HideFileExt -Value 0
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name Hidden -Value 1
Stop-Process -Name explorer -Force

# 4) Enable long paths
Write-Host "Enabling long file paths..."
New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Force | Out-Null
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -Value 1

# 5) Optional: Disable hibernation (saves disk, can help VMs)
Write-Host "Disabling hibernation..."
powercfg -h off

# 6) Install core apps via winget (quiet)
$apps = @(
  "Microsoft.Edge",
  "Google.Chrome",
  "Mozilla.Firefox",
  "Microsoft.PowerToys",
  "Git.Git",
  "GitHub.GitHubDesktop",
  "Microsoft.VisualStudioCode",
  "7zip.7zip",
  "VideoLAN.VLC",
  "Microsoft.WindowsTerminal",
  "Python.Python.3.12",
  "OpenJS.NodeJS.LTS",
  "Microsoft.DotNet.SDK.8",
  "Gyan.FFmpeg",
  "Cockos.REAPER",
  "Microsoft.VisualStudio.2022.BuildTools"
)

Write-Host "Installing core apps..."
foreach ($pkg in $apps) {
  try {
    winget install --id $pkg -e --silent --accept-package-agreements --accept-source-agreements
  } catch {
    Write-Host "⚠️ Failed to install $pkg — continuing."
  }
}

# 7) Enable .NET features and WSL (optional)
Write-Host "Enabling .NET Framework and WSL optional features..."
dism /online /enable-feature /featurename:NetFx3 /all /norestart | Out-Null
dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart | Out-Null

# 8) Audio & latency basics: set High performance policy (done), disable system sounds (optional)
Write-Host "Disabling Windows system sounds..."
reg add "HKCU\AppEvents\Schemes" /v Default /t REG_SZ /d ".None" /f | Out-Null

# 9) Create C:\Noizy\bin and add to PATH
Write-Host "Creating C:\\Noizy\\bin..."
New-Item -ItemType Directory -Path "C:\Noizy\bin" -Force | Out-Null
$envPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($envPath -notlike "*C:\Noizy\bin*") {
  [Environment]::SetEnvironmentVariable("Path", $envPath + ";C:\Noizy\bin", "Machine")
}

# 10) Final tidy + reboot prompt
Write-Host "Bootstrap complete. A reboot is recommended."
EOF

chmod 644 "$BOOT_PS"
say_done "bootstrap.ps1 written to $BOOT_PS"

say_step "Start the VM"
prlctl start "$VM_NAME"
say_done "VM started"

# Try to execute bootstrap automatically if creds + tools are ready
if [ -n "$WIN_USER" ] && [ -n "$WIN_PASS" ]; then
  echo "⏳ Attempting in-guest bootstrap execution (requires Parallels Tools & user account)..."
  # Typical Parallels mapping: \\Mac\Home\NoizyBootstrap\bootstrap.ps1
  # We call PowerShell to bypass policy and run it elevated via scheduled task trick.
  BOOT_NET="\\\\Mac\\Home\\NoizyBootstrap\\bootstrap.ps1"
  RUN_CMD="powershell -ExecutionPolicy Bypass -Command \"Start-Process PowerShell -Verb RunAs -ArgumentList '-ExecutionPolicy Bypass -File `\"$BOOT_NET`\"'\""
  prlctl exec "$VM_NAME" --user "$WIN_USER" --passwd "$WIN_PASS" "$RUN_CMD" || echo "⚠️ Auto-run failed. Run bootstrap manually inside Windows."
fi

echo "\n=== Final steps ===
1) If Windows is still installing, finish OOBE.
2) In Windows, open File Explorer → \\\\Mac\\Home\\NoizyBootstrap → Right-click **bootstrap.ps1** → **Run with PowerShell (as Administrator)**.
3) After it completes, reboot Windows.
4) Back on macOS, you can snapshot:
   prlctl snapshot \"$VM_NAME\" --name \"Noizy-FreshSetup\"
"
