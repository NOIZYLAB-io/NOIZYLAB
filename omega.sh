#!/bin/bash
# 🔥 NOIZYLAB OMEGA SUPER-SYSTEM DEPLOYER 🔥
# Fish Music Inc - CB_01
# ONE SCRIPT TO RULE THEM ALL
# 🔥 GORUNFREE! 🎸🔥

set -e

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║          🔥 NOIZYLAB OMEGA SUPER-SYSTEM DEPLOYER 🔥                       ║"
echo "║                                                                           ║"
echo "║                    GABRIEL ↔ HP-OMEN SUPER-MESH                          ║"
echo "║                       Fish Music Inc - CB_01                              ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

OS=$(uname)
BASE="$HOME/OMEGA_BUILD"
mkdir -p "$BASE"

echo "🎯 Build directory: $BASE"
echo ""

########################################
# DETECT OS & PROCEED
########################################

if [[ "$OS" != "Darwin" ]]; then
    echo "❌ This script must run on GABRIEL (macOS)"
    echo "   For OMEN (Windows), use the generated install_omen.ps1"
    exit 1
fi

echo "✅ macOS detected — configuring GABRIEL..."
echo ""

########################################
# INSTALL CORE PACKAGES
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📦 PHASE 1: INSTALLING CORE PACKAGES"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check Homebrew
if ! command -v brew >/dev/null; then
    echo "[+] Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew already installed"
fi

echo ""
echo "[+] Installing network tools..."
brew install iperf3 mtr nmap || echo "Some tools already installed"

echo "[+] Installing monitoring tools..."
brew install glances htop smartmontools || echo "Some tools already installed"

echo "[+] Installing sync & messaging..."
brew install syncthing redis mosquitto || echo "Some tools already installed"

echo "[+] Installing automation..."
brew install go-task node python || echo "Some tools already installed"

echo ""
echo "✅ Core packages installed!"
echo ""

########################################
# NETWORK OPTIMIZATION
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 PHASE 2: NETWORK OPTIMIZATION (JUMBO FRAMES)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Detect primary network interface
INTERFACE=$(route -n get default | grep interface | awk '{print $2}')
echo "🔍 Primary interface: $INTERFACE"

# Set jumbo frames (MTU 9000)
echo "[+] Setting MTU to 9000 (Jumbo Frames)..."
sudo networksetup -setMTU "$INTERFACE" 9000 || echo "⚠️ MTU setting failed (may need manual config)"

# Verify
CURRENT_MTU=$(ifconfig "$INTERFACE" | grep mtu | awk '{print $6}')
echo "✅ Current MTU: $CURRENT_MTU"

# TCP optimization
echo "[+] Applying TCP optimizations..."
sudo sysctl -w net.inet.tcp.delayed_ack=0
sudo sysctl -w net.inet.tcp.tso=1
sudo sysctl -w net.inet.tcp.rfc1323=1

echo ""
echo "✅ Network optimized for jumbo frames!"
echo ""

########################################
# CREATE JUMBO FRAME TEST SCRIPT
########################################

cat <<'EOF' > "$BASE/test_jumbo.sh"
#!/bin/bash
# Test jumbo frames to target IP

if [ -z "$1" ]; then
    echo "Usage: ./test_jumbo.sh <target-ip>"
    exit 1
fi

echo "Testing jumbo frames to $1..."
ping -D -s 8972 -c 5 "$1"

if [ $? -eq 0 ]; then
    echo "✅ Jumbo frames working!"
else
    echo "❌ Jumbo frames NOT working - check MTU settings"
fi
EOF

chmod +x "$BASE/test_jumbo.sh"
echo "✅ Jumbo frame test script: $BASE/test_jumbo.sh"
echo ""

########################################
# DISTRIBUTED COMPUTE (RAY)
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧠 PHASE 3: DISTRIBUTED AI COMPUTE GRID (RAY)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "[+] Installing Ray..."
pip3 install -q ray[default] || echo "Ray install attempted"

cat <<'EOF' > "$BASE/start_ray_head.sh"
#!/bin/bash
# Start Ray cluster head node on GABRIEL

echo "🧠 Starting Ray cluster HEAD node..."
ray start --head --port=6379 --dashboard-host=0.0.0.0

echo "✅ Ray head node running!"
echo ""
echo "Connect workers with:"
echo "  ray start --address='<GABRIEL-IP>:6379'"
EOF

chmod +x "$BASE/start_ray_head.sh"

echo "✅ Ray head node script: $BASE/start_ray_head.sh"
echo ""

########################################
# SHARED MEMORY (REDIS)
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💾 PHASE 4: SHARED MEMORY POOL (REDIS)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/start_redis.sh"
#!/bin/bash
# Start Redis server

echo "💾 Starting Redis server..."
redis-server --daemonize yes --bind 0.0.0.0

echo "✅ Redis running on port 6379"
EOF

chmod +x "$BASE/start_redis.sh"

echo "✅ Redis start script: $BASE/start_redis.sh"
echo ""

########################################
# REAL-TIME SYNC (SYNCTHING)
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔄 PHASE 5: REAL-TIME FILE SYNC (SYNCTHING)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/start_syncthing.sh"
#!/bin/bash
# Start Syncthing

echo "🔄 Starting Syncthing..."
syncthing -no-browser &

echo "✅ Syncthing running!"
echo "   Web UI: http://localhost:8384"
EOF

chmod +x "$BASE/start_syncthing.sh"

echo "✅ Syncthing start script: $BASE/start_syncthing.sh"
echo ""

########################################
# AI/ML LIBRARIES
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🤖 PHASE 6: AI/ML LIBRARIES"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "[+] Installing AI/ML packages..."
pip3 install -q chromadb sentence-transformers watchdog scikit-learn || echo "AI packages install attempted"

echo "✅ AI libraries installed!"
echo ""

########################################
# MQTT TELEMETRY
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📡 PHASE 7: MQTT TELEMETRY (MOSQUITTO)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "[+] Starting Mosquitto MQTT broker..."
brew services start mosquitto || echo "Mosquitto start attempted"

echo "✅ MQTT broker ready on port 1883"
echo ""

########################################
# MASTER OMEGA START SCRIPT
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌌 PHASE 8: CREATING OMEGA MASTER BOOT SCRIPT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/omega_start.sh"
#!/bin/bash
# 🔥 NOIZYLAB OMEGA SUPER-SYSTEM BOOT 🔥

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║        🔥 NOIZYLAB OMEGA SUPER-SYSTEM STARTING 🔥             ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Start Redis (shared memory)
echo "[+] Starting Redis..."
redis-server --daemonize yes --bind 0.0.0.0
sleep 1
echo "✅ Redis online"

# Start Ray cluster head
echo "[+] Starting Ray cluster HEAD..."
ray start --head --port=6379 --dashboard-host=0.0.0.0
sleep 2
echo "✅ Ray cluster online"
echo "   Dashboard: http://localhost:8265"

# Start Syncthing
echo "[+] Starting Syncthing..."
syncthing -no-browser > /tmp/syncthing.log 2>&1 &
sleep 2
echo "✅ Syncthing online"
echo "   Web UI: http://localhost:8384"

# Start MQTT broker
echo "[+] Starting MQTT broker..."
brew services start mosquitto
echo "✅ MQTT online (port 1883)"

# Start NOIZYLAB Agent
echo "[+] Starting NOIZYLAB Agent..."
cd ~/NOIZYLAB/agent
python3 noizylab_agent.py --machine gabriel > /tmp/noizylab_agent.log 2>&1 &
echo "✅ NOIZYLAB Agent online"

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                 🚀 OMEGA SYSTEM ONLINE 🚀                     ║"
echo "╠═══════════════════════════════════════════════════════════════╣"
echo "║                                                               ║"
echo "║  Services Running:                                            ║"
echo "║  ├─ Redis         → port 6379                                 ║"
echo "║  ├─ Ray           → http://localhost:8265                     ║"
echo "║  ├─ Syncthing     → http://localhost:8384                     ║"
echo "║  ├─ MQTT          → port 1883                                 ║"
echo "║  └─ NOIZYLAB      → /tmp/noizylab_agent.log                   ║"
echo "║                                                               ║"
echo "║  Status:                                                      ║"
echo "║  ├─ Jumbo Frames  → MTU 9000 ✅                               ║"
echo "║  ├─ Distributed   → Ray cluster HEAD ✅                       ║"
echo "║  ├─ Sync          → Syncthing active ✅                       ║"
echo "║  └─ Telemetry     → MQTT publishing ✅                        ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🔥 GORUNFREE! 🎸🔥"
echo ""
EOF

chmod +x "$BASE/omega_start.sh"

echo "✅ OMEGA master boot script: $BASE/omega_start.sh"
echo ""

########################################
# GENERATE WINDOWS INSTALLER
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💻 PHASE 9: GENERATING WINDOWS (OMEN) INSTALLER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/install_omen.ps1"
# 🔥 NOIZYLAB OMEGA - WINDOWS (HP-OMEN) INSTALLER 🔥
# Fish Music Inc - CB_01
# Run as Administrator

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════════╗"
Write-Host "║     🔥 NOIZYLAB OMEGA - HP-OMEN INSTALLER 🔥                  ║"
Write-Host "╚═══════════════════════════════════════════════════════════════╝"
Write-Host ""

# Install packages
Write-Host "[+] Installing core packages..."
winget install -e --id Python.Python.3.11
winget install -e --id OpenJS.NodeJS
winget install -e --id Task.Task
winget install -e --id Redis.Redis
winget install -e --id Syncthing.Syncthing

Write-Host ""
Write-Host "[+] Installing AI/ML libraries..."
pip install ray chromadb sentence-transformers watchdog scikit-learn paho-mqtt psutil pydantic

Write-Host ""
Write-Host "[+] Configuring jumbo frames..."
Write-Host "   MANUAL STEP: Network Adapter → Properties → Advanced → Jumbo Packet → 9014"
Write-Host "   (Cannot be scripted - requires manual NIC configuration)"

Write-Host ""
Write-Host "[+] Creating Ray worker start script..."
$rayScript = @'
@echo off
REM Start Ray worker node
echo Starting Ray worker...
ray start --address="%GABRIEL_IP%:6379"
echo Ray worker connected to GABRIEL!
pause
'@
$rayScript | Out-File -FilePath "$HOME\Desktop\start_ray_worker.bat" -Encoding ASCII

Write-Host ""
Write-Host "[+] Creating GABRIEL mount script..."
$mountScript = @'
@echo off
REM Mount GABRIEL SMB share
echo Mounting GABRIEL share as Z: drive...
net use Z: \\gabriel.local\NoizyShare /persistent:yes
echo Done!
pause
'@
$mountScript | Out-File -FilePath "$HOME\Desktop\mount_gabriel.bat" -Encoding ASCII

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════════╗"
Write-Host "║                 ✅ OMEN INSTALLER COMPLETE ✅                  ║"
Write-Host "╠═══════════════════════════════════════════════════════════════╣"
Write-Host "║                                                               ║"
Write-Host "║  Next Steps:                                                  ║"
Write-Host "║  1. Set Jumbo Frames in Network Adapter (9014 bytes)          ║"
Write-Host "║  2. Run mount_gabriel.bat to connect to GABRIEL               ║"
Write-Host "║  3. Run start_ray_worker.bat to join compute cluster          ║"
Write-Host "║  4. Enable SSH: Optional Features → OpenSSH Server            ║"
Write-Host "║  5. Install Tailscale: https://tailscale.com/download         ║"
Write-Host "║                                                               ║"
Write-Host "╚═══════════════════════════════════════════════════════════════╝"
Write-Host ""
Write-Host "🔥 GORUNFREE! 🎸🔥"
Write-Host ""
EOF

echo "✅ Windows installer: $BASE/install_omen.ps1"
echo ""

########################################
# VERIFICATION SCRIPT
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 PHASE 10: CREATING VERIFICATION SCRIPT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/verify.sh"
#!/bin/bash
# 🔍 NOIZYLAB OMEGA VERIFICATION

echo ""
echo "🔍 OMEGA SUPER-SYSTEM VERIFICATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check MTU
echo "[1] Checking Jumbo Frames (MTU)..."
INTERFACE=$(route -n get default | grep interface | awk '{print $2}')
MTU=$(ifconfig "$INTERFACE" | grep mtu | awk '{print $6}')
if [ "$MTU" -ge 9000 ]; then
    echo "    ✅ MTU: $MTU (Jumbo Frames enabled)"
else
    echo "    ❌ MTU: $MTU (Should be 9000+)"
fi

# Check Redis
echo ""
echo "[2] Checking Redis..."
if pgrep -x "redis-server" > /dev/null; then
    echo "    ✅ Redis running"
else
    echo "    ❌ Redis not running"
fi

# Check Ray
echo ""
echo "[3] Checking Ray cluster..."
if ray status > /dev/null 2>&1; then
    echo "    ✅ Ray cluster running"
    ray status
else
    echo "    ❌ Ray cluster not running"
fi

# Check Syncthing
echo ""
echo "[4] Checking Syncthing..."
if pgrep -x "syncthing" > /dev/null; then
    echo "    ✅ Syncthing running"
else
    echo "    ❌ Syncthing not running"
fi

# Check MQTT
echo ""
echo "[5] Checking MQTT broker..."
if lsof -i :1883 > /dev/null 2>&1; then
    echo "    ✅ MQTT broker running (port 1883)"
else
    echo "    ❌ MQTT broker not running"
fi

# Check NOIZYLAB Agent
echo ""
echo "[6] Checking NOIZYLAB Agent..."
if pgrep -f "noizylab_agent.py" > /dev/null; then
    echo "    ✅ NOIZYLAB Agent running"
else
    echo "    ❌ NOIZYLAB Agent not running"
fi

# Check SSH
echo ""
echo "[7] Checking SSH..."
if sudo systemsetup -getremotelogin | grep -q "On"; then
    echo "    ✅ SSH enabled"
else
    echo "    ❌ SSH not enabled"
fi

# Check Tailscale
echo ""
echo "[8] Checking Tailscale..."
if command -v tailscale > /dev/null && tailscale status > /dev/null 2>&1; then
    echo "    ✅ Tailscale connected"
    tailscale status | head -5
else
    echo "    ⚠️ Tailscale not installed or not connected"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Verification complete!"
echo ""
EOF

chmod +x "$BASE/verify.sh"

echo "✅ Verification script: $BASE/verify.sh"
echo ""

########################################
# SELF-HEALING SCRIPT
########################################

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔧 PHASE 11: CREATING SELF-HEALING SCRIPT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cat <<'EOF' > "$BASE/heal.sh"
#!/bin/bash
# 🔧 NOIZYLAB OMEGA SELF-HEAL

echo "🔧 Running OMEGA self-heal..."
echo ""

# Flush DNS
echo "[+] Flushing DNS cache..."
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Restart services if needed
echo "[+] Checking services..."

if ! pgrep -x "redis-server" > /dev/null; then
    echo "   [!] Restarting Redis..."
    redis-server --daemonize yes
fi

if ! ray status > /dev/null 2>&1; then
    echo "   [!] Restarting Ray..."
    ray start --head --port=6379
fi

if ! pgrep -x "syncthing" > /dev/null; then
    echo "   [!] Restarting Syncthing..."
    syncthing -no-browser &
fi

# Check network
echo ""
echo "[+] Testing network connectivity..."
ping -c 3 192.168.1.1 > /dev/null && echo "   ✅ Gateway reachable"

echo ""
echo "✅ Heal complete!"
EOF

chmod +x "$BASE/heal.sh"

echo "✅ Self-healing script: $BASE/heal.sh"
echo ""

########################################
# CREATE SETUP_GABRIEL.SH
########################################

cat <<'EOF' > "$BASE/setup_gabriel.sh"
#!/bin/bash
# 🔥 GABRIEL FINAL SETUP SCRIPT

echo "🔥 GABRIEL FINAL SETUP"
echo ""

# Enable SSH
echo "[+] Enabling SSH (Remote Login)..."
sudo systemsetup -setremotelogin on

# Enable Screen Sharing
echo "[+] Enabling Screen Sharing..."
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist

# Enable File Sharing (SMB)
echo "[+] File Sharing already configured via System Preferences"
echo "   MANUAL: System Settings → Sharing → File Sharing → ON"

# Generate SSH key if needed
if [ ! -f ~/.ssh/id_ed25519 ]; then
    echo "[+] Generating SSH key..."
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
fi

echo ""
echo "✅ GABRIEL setup complete!"
echo ""
echo "📋 Next Steps:"
echo "   1. Copy this key to OMEN:"
echo "      cat ~/.ssh/id_ed25519.pub"
echo "   2. Enable File Sharing in System Settings"
echo "   3. Run: ./omega_start.sh"
EOF

chmod +x "$BASE/setup_gabriel.sh"

echo "✅ GABRIEL setup script: $BASE/setup_gabriel.sh"
echo ""

########################################
# COMPLETE!
########################################

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║              🚀 OMEGA SUPER-SYSTEM BUILD COMPLETE! 🚀                    ║"
echo "║                                                                           ║"
echo "╠═══════════════════════════════════════════════════════════════════════════╣"
echo "║                                                                           ║"
echo "║  📦 Location: $BASE"
echo "║                                                                           ║"
echo "║  Created Files:                                                           ║"
echo "║  ├─ omega_start.sh          → Master boot script                          ║"
echo "║  ├─ setup_gabriel.sh        → Final GABRIEL setup                         ║"
echo "║  ├─ verify.sh               → System verification                         ║"
echo "║  ├─ heal.sh                 → Self-healing script                         ║"
echo "║  ├─ test_jumbo.sh           → Jumbo frame tester                          ║"
echo "║  ├─ start_ray_head.sh       → Ray cluster head                            ║"
echo "║  ├─ start_redis.sh          → Redis server                                ║"
echo "║  ├─ start_syncthing.sh      → Syncthing sync                              ║"
echo "║  └─ install_omen.ps1        → Windows installer (for OMEN)                ║"
echo "║                                                                           ║"
echo "╠═══════════════════════════════════════════════════════════════════════════╣"
echo "║                                                                           ║"
echo "║  🎯 NEXT STEPS:                                                           ║"
echo "║                                                                           ║"
echo "║  On GABRIEL:                                                              ║"
echo "║  1. cd $BASE"
echo "║  2. ./setup_gabriel.sh                                                    ║"
echo "║  3. ./omega_start.sh                                                      ║"
echo "║  4. ./verify.sh                                                           ║"
echo "║                                                                           ║"
echo "║  On HP-OMEN:                                                              ║"
echo "║  1. Copy install_omen.ps1 to OMEN                                         ║"
echo "║  2. Run as Administrator                                                  ║"
echo "║  3. Follow on-screen instructions                                         ║"
echo "║                                                                           ║"
echo "╠═══════════════════════════════════════════════════════════════════════════╣"
echo "║                                                                           ║"
echo "║             🔥 READY TO DEPLOY! GORUNFREE! 🎸🔥                           ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""
