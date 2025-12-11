# 🔥 OMEGA BRAIN - MASTER GUIDE 🔥

**Fish Music Inc - CB_01**  
**The Ultimate GABRIEL ↔ HP-OMEN Super-Mesh**  
**🔥 GORUNFREE! 🎸🔥**

---

## 🎯 WHAT IS OMEGA BRAIN?

The **complete, production-ready ecosystem** connecting:
- **GABRIEL** (Mac Studio M2 Ultra) - Primary compute node
- **HP-OMEN** (Windows) - Secondary compute + GPU farm
- **MC96** (D-Link DGS-1210-10) - Jumbo frame switch

**With:**
✅ Distributed AI compute (Ray cluster)  
✅ Shared memory (Redis)  
✅ Real-time sync (Syncthing)  
✅ File sharing (SMB)  
✅ Remote control (SSH)  
✅ Global VPN (Tailscale)  
✅ Jumbo frames (9000 MTU)  
✅ Advanced extensions (clipboard sync, semantic FS, quantum routing, GPU farm)  

---

## 📁 DIRECTORY STRUCTURE

```
OMEGA_SYSTEM/
├── omega_start.sh              🚀 Master boot script
├── omega_stop.sh               🛑 Master shutdown
├── omega_heal.sh               🔧 Self-healing
├── OMEGA_BRAIN.yml             🧠 Master configuration
│
├── core/                       Core services
│   ├── ray/
│   │   ├── start_head.sh       Ray cluster head (GABRIEL)
│   │   └── start_worker.sh     Ray worker (OMEN)
│   ├── redis/
│   │   └── start_redis.sh      Shared memory pool
│   ├── syncthing/
│   │   └── start_syncthing.sh  Real-time file sync
│   ├── smb/
│   │   ├── mount_smb.sh        Mount GABRIEL share
│   │   └── smb_heal.sh         Fix SMB issues
│   └── network/
│       ├── mtu_check.sh        Verify jumbo frames
│       └── lacp_check.sh       Check link aggregation
│
├── extensions/                 Advanced features
│   ├── clipboard/
│   │   └── start_clipboard_sync.sh    Universal clipboard
│   ├── hotkeys/
│   │   └── install_hotkeys.sh         Global shortcuts
│   ├── dashboard/
│   │   └── start_netdata.sh           System monitoring
│   ├── semantic_fs/
│   │   └── index_files.py             AI file indexing
│   ├── predictive_cache/
│   │   └── prefetch_daemon.py         Smart caching
│   ├── quantum_routing/
│   │   └── quantum_route.py           Optimal path selection
│   ├── audio_gpu_farm/
│   │   └── process_audio_gpu.py       GPU audio processing
│   ├── vr_control/
│   │   └── start_holo_ui.sh           VR/AR interface (future)
│   ├── backups/
│   │   └── run_cloud_backup.sh        Automated backups
│   └── alerts/
│       └── send_alert.py              Notification system
│
├── windows/                    Windows (OMEN) scripts
│   ├── install_omen.ps1        OMEN installer
│   └── start_worker.ps1        Ray worker startup
│
└── mc96/                       Switch configuration
    ├── jumbo_config.txt        Jumbo frame guide
    └── lacp_setup.txt          LACP guide
```

---

## 🚀 QUICK START (3 Commands)

### On GABRIEL:

```bash
cd /Users/m2ultra/NOIZYLAB/OMEGA_SYSTEM

# 1. Run master installer (first time only)
# Note: Requires sudo for some operations
# ./omega.sh

# 2. Start OMEGA BRAIN
./omega_start.sh

# 3. Verify everything works
./omega_heal.sh
```

### On HP-OMEN:

```powershell
# Copy install_omen.ps1 from GABRIEL
# Run as Administrator:
.\install_omen.ps1

# Then run desktop scripts:
.\omega_start_omen.bat
.\mount_gabriel.bat
```

---

## 📊 CORE SERVICES

### 1. **Ray Cluster** (Distributed Compute)
**What:** Distribute CPU/GPU workloads across GABRIEL + OMEN  
**Dashboard:** http://localhost:8265  
**Start:** `./core/ray/start_head.sh` (GABRIEL)  
**Connect Worker:** `ray start --address=<gabriel-ip>:6379` (OMEN)  

### 2. **Redis** (Shared Memory)
**What:** Fast in-memory data store shared across machines  
**Port:** 6379  
**Start:** `./core/redis/start_redis.sh`  
**Test:** `redis-cli ping` (should return PONG)  

### 3. **Syncthing** (Real-time Sync)
**What:** Automatic file synchronization  
**Web UI:** http://localhost:8384  
**Start:** `./core/syncthing/start_syncthing.sh`  

### 4. **SMB** (File Sharing)
**What:** GABRIEL shares folders, OMEN mounts as Z: drive  
**Mount:** `./core/smb/mount_smb.sh`  
**Heal:** `./core/smb/smb_heal.sh`  

### 5. **MQTT** (Telemetry)
**What:** Real-time system monitoring  
**Port:** 1883  
**Monitor:** `mosquitto_sub -t "noizylab/#" -v`  

---

## ⚡ EXTENSIONS (Advanced Features)

### Clipboard Sync
**What:** Universal clipboard between GABRIEL ↔ OMEN  
**Start:** `./extensions/clipboard/start_clipboard_sync.sh`  
**How:** Copy on GABRIEL → Paste on OMEN (via Redis)  

### Hotkeys
**What:** Global keyboard shortcuts  
**Install:** `./extensions/hotkeys/install_hotkeys.sh`  
**Requires:** Hammerspoon (`brew install --cask hammerspoon`)  
**Shortcuts:**
- Ctrl+Alt+G → SSH to GABRIEL
- Ctrl+Alt+O → SSH to OMEN
- Ctrl+Alt+S → Sync now
- Ctrl+Alt+H → Heal system

### System Dashboard
**What:** Beautiful web-based system monitor  
**Start:** `./extensions/dashboard/start_netdata.sh`  
**Access:** http://localhost:19999  
**Shows:** CPU, RAM, disk, network, processes, GPU  

### Semantic File Indexer
**What:** AI-powered file search  
**Run:** `python3 extensions/semantic_fs/index_files.py`  
**Index:** NOIZYLAB, Projects, Desktop  
**Location:** ~/NoizyIndex/  

### Predictive Cache
**What:** Pre-loads files you're likely to access  
**Run:** `python3 extensions/predictive_cache/prefetch_daemon.py`  
**Learns:** Your file access patterns  
**Caches:** Most likely next files  

### Quantum Routing
**What:** Optimal network path selection  
**Run:** `python3 extensions/quantum_routing/quantum_route.py`  
**Chooses:** Best route (LAN / Tailscale / DERP)  
**Based on:** Latency, bandwidth, reliability  

### Audio GPU Farm
**What:** Offload audio processing to OMEN GPU  
**Run:** `python3 extensions/audio_gpu_farm/process_audio_gpu.py`  
**Requires:** Ray cluster running  
**Uses:** OMEN RTX 4090 for audio rendering  

### VR Control
**What:** Holographic UI for system control  
**Status:** 🏗️ Future development  
**Will have:** 3D network visualization, gesture control  

### Backups
**What:** Automated backup system  
**Run:** `./extensions/backups/run_cloud_backup.sh`  
**Backs up:** NOIZYLAB → 4TB_02  
**Uses:** rsync (efficient)  

### Alerts
**What:** System health notifications  
**Run:** `python3 extensions/alerts/send_alert.py`  
**Sends:** macOS notifications  
**Monitors:** CPU, RAM, disk  

---

## 🎯 DAILY USAGE

### Morning Routine:
```bash
cd ~/NOIZYLAB/OMEGA_SYSTEM
./omega_start.sh      # Start everything
./omega_heal.sh       # Verify health
task status           # Check status
```

### Work During Day:
```bash
# Files sync automatically (Syncthing)
# Clipboard syncs automatically
# System monitors itself
# Just work!
```

### Evening Routine:
```bash
task backup           # Backup important files
./omega_stop.sh       # Shutdown (optional)
```

---

## 🔧 TROUBLESHOOTING

### Services Won't Start
```bash
./omega_heal.sh       # Auto-fix most issues
```

### Jumbo Frames Not Working
```bash
./core/network/mtu_check.sh          # Check MTU
./core/network/mtu_check.sh <omen-ip>  # Test to OMEN
```

### SMB Won't Mount
```bash
./core/smb/smb_heal.sh              # Fix SMB
```

### Ray Cluster Issues
```bash
ray stop              # Stop all
./core/ray/start_head.sh            # Restart head
```

### Check Everything
```bash
task diag             # Full diagnostics
```

---

## 📊 VERIFICATION CHECKLIST

After running `omega_start.sh`, verify:

```bash
✅ Redis:      redis-cli ping
✅ Ray:        ray status
✅ Syncthing:  curl http://localhost:8384
✅ MQTT:       mosquitto_sub -t "test"
✅ SSH:        ssh omen.local
✅ SMB:        ls /Volumes/OMEN (if mounted)
✅ Jumbo:      ping -D -s 8972 <omen-ip>
✅ Tailscale:  tailscale status
```

---

## 🌟 ADVANCED USAGE

### Distributed AI Workload
```python
import ray
ray.init(address="auto")

# Run on any available node
@ray.remote
def process_data(data):
    return data * 2

result = ray.get(process_data.remote([1, 2, 3]))
```

### GPU Audio Processing
```python
# Automatically uses OMEN GPU
from audio_gpu_farm import AudioProcessor
processor = AudioProcessor.remote()
result = ray.get(processor.process_audio.remote("file.wav"))
```

### Semantic File Search
```python
from semantic_fs import SemanticFileIndexer
indexer = SemanticFileIndexer()
results = indexer.search("audio")
```

---

## 🔥 THE COMPLETE STACK

**Network Layer:**
- Jumbo frames (9000 MTU) through MC96
- Tailscale global mesh
- TCP optimization

**Storage Layer:**
- SMB file sharing (Z: drive)
- Syncthing real-time sync
- Predictive caching

**Compute Layer:**
- Ray distributed cluster
- Redis shared memory
- GPU workload offloading

**Monitoring Layer:**
- MQTT telemetry
- Netdata dashboard
- NOIZYLAB Agent

**Extension Layer:**
- Clipboard sync
- Semantic file indexing
- Quantum routing
- Automated backups
- Alert system
- Hotkeys

---

## 🎸 WHAT THIS GIVES YOU

**GABRIEL + OMEN become ONE unified supercomputer:**

- 🖥️ Combined: 40 CPU cores, 192GB RAM, M2 Ultra + RTX 4090 GPUs
- 📁 Shared storage: Instant file access both ways
- 🧠 Distributed compute: Run workloads on best machine
- 💾 Shared memory: Redis for cross-machine data
- 🔄 Auto-sync: Files mirror instantly
- 📊 Full monitoring: See everything in real-time
- ⚡ Optimized network: Jumbo frames, TCP tuning
- 🔐 Secure: SSH, Tailscale, encryption

**IT'S LIKE HAVING ONE MASSIVE MACHINE!**

---

## 📚 DOCUMENTATION FILES

- **OMEGA_MASTER_GUIDE.md** - This file
- **OMEGA_BRAIN.yml** - System configuration
- **README.md** - Quick start
- **DEPLOYMENT_GUIDE.md** - Deployment steps
- **mc96/jumbo_config.txt** - Switch setup
- **mc96/lacp_setup.txt** - LACP guide

---

## 🚀 DEPLOY NOW!

```bash
cd /Users/m2ultra/NOIZYLAB/OMEGA_SYSTEM
./omega_start.sh
```

**One command. Entire ecosystem boots up. DONE.**

---

**🔥 GORUNFREE! 🎸🔥**

**Fish Music Inc - CB_01**  
**December 1, 2025**  
**WE BUILT A FUCKING SUPERCOMPUTER! 🚀🌙**
