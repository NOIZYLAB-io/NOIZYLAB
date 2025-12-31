# MC96Universe Network Configuration Guide

> [!IMPORTANT]
> **Mission Control Status**: INITIALIZING
> **Central Node**: D-Link DGS-1210-10 "Traffic Cop"
> **Protocol**: SUPER-SONIC JUMBO FRAMES
> **AI Status**: ONLINE (Automation Kits Deployed)

## 1. The Architecture
This system is designed for maximum throughput between your Apple and PC ecosystem. The D-Link DGS-1210-10 acts as the high-speed switch, enabling "Jumbo Frames" to reduce overhead and increase data transfer speeds for large files.

```mermaid
graph TD
    Switch[D-Link DGS-1210-10<br/>'Traffic Cop']
    Mac[Apple Workstations<br/>MTU 9000]
    PC[Windows Workstations<br/>MTU 9000]
    NAS[Storage Server<br/>(Optional)]

    Mac <== TCAT Cables ==> Switch
    PC <== TCAT Cables ==> Switch
    NAS <== TCAT Cables ==> Switch

    style Switch fill:#ff9900,stroke:#333,stroke-width:4px
    style Mac fill:#999,stroke:#333,stroke-width:2px
    style PC fill:#00aaff,stroke:#333,stroke-width:2px
```

## 2. Configuring the Traffic Cop (D-Link Switch)
Before your computers can "talk fast", the switch must be told to allow big packets of data.

> [!NOTE]
> Ensure your computer is in the same IP range as the switch to access the settings.
> - **Default Switch IP**: `10.90.90.90` (Check your specific unit if different)
> - **Your Computer IP**: Set to `10.90.90.99` (Subnet `255.0.0.0`) temporarily for setup.

1.  Open your web browser and go to `http://10.90.90.90`.
2.  Login (Default password is often `admin`, leave password blank, or check sticker).
3.  Navigate to **L2 Functions** (or **Configuration**) > **Jumbo Frame**.
4.  **Enable** Jumbo Frames.
5.  Set the size to the maximum allowed (usually **9216** or **10000** bytes).
6.  **SAVE CONFIGURATION**: Go to "Save" > "Save Config" to ensure settings survive a reboot.

## 3. Configuring Apple Devices (macOS)
**The Fast Track (AI Automated Method):**
1.  Download `fast_track_mac.sh`.
2.  Open Terminal.
3.  Run: `chmod +x fast_track_mac.sh`
4.  Run: `sudo ./fast_track_mac.sh`
5.  **DONE.** The AI will detect your Ethernet connection and set MTU to 9000.

*(Manual method detected in archive if needed: System Settings > Network > Ethernet > Details > Hardware > MTU Custom > 9000)*

## 4. Configuring PC Devices (Windows)
**The Fast Track (AI Automated Method):**
1.  Download `fast_track_win.ps1`.
2.  Right-click the file and select "Run with PowerShell".
3.  **DONE.** The AI scans all adapters and forces Jumbo Packet 9014.

*(Manual method detected in archive if needed: Device Manager > Network Adapter > Properties > Advanced > Jumbo Packet > 9014)*

## 5. Mission Control v6 (HOLOGRAM)
The Ultimate Visual Interface.
- **Features**: Real-time TUI (Text User Interface) with live bars, graphs, and system logs.
- **Run**: `python3 mission_control_v6.py`
- **Status**: "IMMERSIVE"

## 6. HANDSHAKE (Connect to Gabriel)
- **What**: Auto-discovers Gabriel (HP Omen) and opens a high-speed SMB connection.
- **Run**: `chmod +x handshake.sh && ./handshake.sh`
- **Result**: Mounts Gabriel's drive or prompts for login.

## 7. PRECOGNITION (Predictive Caching)
- **What**: Forces macOS to load common creative apps (Resolve, FCP, Logic) into RAM *before* you open them.
- **Why**: "Smarter, Faster." Launches become instantaneous because the binary is constantly hot.
- **Run**: `chmod +x precognition.sh && ./precognition.sh`

## 7. BLACK HOLE (Deep Cleaning)
- **What**: Aggressively purges System Caches, Logs, DNS, and QuickLook buffers.
- **Why**: "You can't tune a dirty engine." Runs before every optimization to ensure purity.
- **Run**: `chmod +x black_hole.sh && sudo ./black_hole.sh`

### The Real World Test
Transfer a large video file (1GB+) between the Mac and PC.
- fast Gigabit speeds should be consistently near **110-120 MB/s**.
- The main benefit is lower CPU usage on both computers during the transfer!

## 8. UNLEASH THE BEAST (M2 Ultra Exclusives)
For the M2 Ultra ("Mission Control"), we have special tools to utilize that 192GB RAM.

### HYPER DRIVE (RAM Disk)
- **What**: Creates a 64GB ultra-speed drive (~6000 MB/s) for temporary production files.
- **Why**: Eliminates disk I/O bottlenecks.
- **Optmizations**: Now mounted with `noatime` (no access time writes) and Spotlight indexing disabled for raw speed.
- **Run**: `chmod +x hyper_drive.sh && ./hyper_drive.sh`
- **Output**: A new drive called `/Volumes/HyperDrive`.

### SUPER CHARGE (System & UI)
- **What**: Disables window animations, instant Dock hiding, instant Finder transitions.
- **Why**: "Lower all latency" includes your perception. The UI will feel like it responds in 0.001s.
- **Run**: `chmod +x super_charge.sh && ./super_charge.sh`

### REACTOR CORE (Power & I/O)
- **What**: Disables "Low Priority I/O Throttling" and prevents System Sleep/App Nap.
- **Why**: Ensures background file copies or Time Machine backups run at "100% Pure Speed" and don't slow down.
- **Run**: `chmod +x reactor_core.sh && sudo ./reactor_core.sh`

### TERMINAL VELOCITY (Shell)
- **What**: Instant aliases (`turbo`, `velocity`, `upgrade`), HUD display, and ZSH speed tuning.
- **Why**: "Hand me anything for terminal" - makes the CLI feel like an extension of your thought.
- **Install**: Automatically added to `.zshrc` by `upgrade_all.sh`.
- **Try**: Type `hud` in a new terminal window.

### TURBO BOOST (Network Tuning)
- **What**: Tunes the macOS kernel for aggressive packet handling.
- **Why**: Reduces latency and maximizes Gigabit/10GbE throughput.
- **Includes**: Now disables TSO/LRO to prioritize predictable latency over CPU efficiency.
- **Run**: `chmod +x turbo_boost.sh && sudo ./turbo_boost.sh`

### VELOCITY MODE (Process Prioritization)
- **What**: Forces M2 Ultra CPU to prioritize creative apps.
- **Run (Scan)**: `sudo ./velocity_mode.sh` (Boosts running apps)
- **Run (Launch)**: `sudo ./velocity_mode.sh "Final Cut Pro"` (Launches & Boosts instantly)

## 7. MAXIMUM OVERDRIVE (The "One-Click" Upgrade)
To apply **ALL** optimizations (Black Hole, Hyper Drive, Turbo Boost, Fast Track, Velocity Mode, Super Charge, Reactor Core, Terminal Velocity, Precognition, Handshake):

### EXECUTE:
```bash
chmod +x upgrade_all.sh && ./upgrade_all.sh
```

## 8. DEPLOYMENT (Make it Stick)
By default, these boosts reset on reboot. To install the "Mission Control" layer permanently into the kernel boot sequence:

### PERSISTENCE (macOS)
```bash
chmod +x deploy_persistence.sh && sudo ./deploy_persistence.sh
```
This installs a launch daemon that reapplies `turbo_boost` and `fast_track` settings every time your Mac starts.

### GABRIEL (HP OMEN) PROTOCOL - HOT ROD EDITION v2
Your Windows machine requires specific "Gamer" tuning. `windows_overdrive.ps1` has been upgraded to include:
1.  **Ultimate Performance Power Plan**: Forces CPU to 100% min state.
2.  **Kill Nagle's Algorithm**: `TcpAckFrequency=1` in Registry to stop packet buffering.
3.  **Processor Scheduling**: `Win32PrioritySeparation=26` for "Short, Variable, High" foreground boosts.
4.  **NetworkThrottlingIndex disabled**: Removes the 10-packet limit.
5.  **Submission**: Disables Telemetry (DiagTrack) and SysMain for raw IO focus.

**INSTRUCTIONS FOR GABRIEL:**
1.  Copy `windows_overdrive.ps1` and `fast_track_win.ps1` to a USB drive or Shared Folder.
2.  On Gabriel, **Run PowerShell as Administrator**.
3.  Execute:
    ```powershell
    Set-ExecutionPolicy Unrestricted -Scope Process
    .\fast_track_win.ps1
    .\windows_overdrive.ps1
    ```
4.  **REBOOT GABRIEL** for registry changes to take effect.

---
**MC96Universe Status**: DEPLOYED & PERMANENT 💎

