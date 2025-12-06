# 🎯 NoizyLab Slack & Network Integration - Complete System

## 🌟 What You Now Have

A fully integrated, enterprise-grade system that:

### 1. **Slack Integration** 💬
- Real-time notifications for all NoizyLab events
- Interactive slash commands
- Rich message formatting with Block Kit
- Full API for custom integrations
- Beautiful management dashboard
- Complete audit trail in SQLite database

### 2. **DGS1210 Network Agent** 🌐
- Real-time port monitoring via SNMP
- Automatic device detection when plugged in
- Multiple handshake protocols (MC96, HTTP, SSH, Ping)
- MC96-specific auto-handshake on designated ports
- Slack notifications for all network events
- RESTful API for integration
- Complete device database

### 3. **Master Dashboard** 🎛️
- Unified control panel for everything
- Real-time service status
- Network port visualization
- MC96 device management
- Slack integration status
- One-click access to all services

### 4. **Automatic Device Handshake** 🤝
When you plug a device into your DGS1210-10 switch:
1. **Instant Detection** (< 1 second)
2. **Device Discovery** (2-3 seconds)
3. **Automatic Handshake** (3-5 seconds)
4. **Slack Notification** (instant)
5. **Device Ready** (total: ~5-10 seconds)

---

## 📁 What Was Created

### Slack Integration
```
/Users/m2ultra/NOIZYLAB/integrations/slack/
├── slack_core.py                 # Core Slack client library
├── slack_api_server.py           # FastAPI server for webhooks
├── slack_dashboard.py            # Streamlit management UI
├── slack_notifier.py             # Easy integration module
├── slack_data.db                 # SQLite database
├── requirements.txt              # Python dependencies
├── start_slack_services.sh       # Startup script
├── __init__.py                   # Package init
└── README.md                     # Full documentation
```

### Network Agent
```
/Users/m2ultra/NOIZYLAB/network/
├── dgs1210_network_agent.py      # Main agent with auto-handshake
├── network_agent_service.py      # FastAPI service wrapper
├── network_devices.db            # SQLite database
├── requirements.txt              # Python dependencies
├── start_network_agent.sh        # Startup script
├── __init__.py                   # Package init
└── README.md                     # Full documentation
```

### Documentation
```
/Users/m2ultra/NOIZYLAB/
├── NOIZYLAB_SLACK_QUICKSTART.md  # 5-minute quick start
├── SLACK_NETWORK_COMPLETE_GUIDE.md  # This file
├── LAUNCH_NOIZYLAB_COMPLETE.sh   # Master launcher
└── master-dashboard/
    └── master-dashboard.py       # Updated with Slack & Network
```

---

## 🚀 Launch Everything

### Single Command Launch
```bash
cd /Users/m2ultra/NOIZYLAB
./LAUNCH_NOIZYLAB_COMPLETE.sh
```

This starts:
- ✅ Master Dashboard (port 8501)
- ✅ Slack API Server (port 8003)
- ✅ Slack Dashboard (port 8506)
- ✅ Network Agent (port 8005)
- ✅ All monitoring and notifications

### Manual Launch (Individual Services)

```bash
# Terminal 1: Slack Integration
cd /Users/m2ultra/NOIZYLAB/integrations/slack
./start_slack_services.sh

# Terminal 2: Network Agent
cd /Users/m2ultra/NOIZYLAB/network
./start_network_agent.sh

# Terminal 3: Master Dashboard
cd /Users/m2ultra/NOIZYLAB/master-dashboard
streamlit run master-dashboard.py
```

---

## 🎯 MC96 Auto-Handshake Setup

### Configure MC96 Ports

```bash
# Set which ports are for MC96 devices
export MC96_PORTS="1,2,3"

# Or edit in agent_config.json
```

### What Happens When MC96 Connects

**You:** Plug MC96 device into port 1 and turn it on

**System:**
```
[00:00] 🔌 Link detected on port 1
        → Slack: "Device connected to port 1"

[00:02] 🔍 Scanning for device...
        → Found MAC: 00:1a:2b:3c:4d:5e
        → Resolved IP: 192.168.1.100
        → Hostname: MC96-Device-1

[00:03] 🤝 Starting MC96 handshake...
        → Step 1: Ping test ✅
        → Step 2: HTTP check ✅
        → Step 3: API status ✅
        → Step 4: Send init command ✅

[00:05] ✅ Handshake complete!
        → Device registered
        → Configuration stored
        → Slack: Full success notification

[00:06] 🎉 MC96 Device Ready!
```

**Slack receives:**
```
🤝 Network Event: Handshake
Device: MC96-Device-1
━━━━━━━━━━━━━━━━━━━━
Port: 1
Device: MC96-Device-1
MAC: 00:1a:2b:3c:4d:5e
IP: 192.168.1.100
Type: mc96
Response Time: 2.34s
Status: ✅ Success
━━━━━━━━━━━━━━━━━━━━
🕐 2024-11-26 14:32:15
```

---

## 💡 Usage Examples

### Send Slack Alert from Anywhere

```python
import sys
sys.path.append('/Users/m2ultra/NOIZYLAB/integrations/slack')
from slack_notifier import alert

alert("Deployment started", "info")
alert("Warning: High CPU usage", "warning")
alert("Error: Service crashed!", "error")
alert("Success: All tests passed", "success")
```

### Send Network Event

```python
from slack_notifier import network_event

network_event("connected", "MacBook Pro", {
    "Port": "5",
    "IP": "192.168.1.50",
    "MAC": "a1:b2:c3:d4:e5:f6",
    "Status": "Handshake complete"
})
```

### Send System Status

```python
from slack_notifier import system_status

system_status({
    "Email API": "running",
    "Database": "healthy",
    "CPU": "45%",
    "Memory": "62%",
    "Disk": "78%"
})
```

### Check Network Devices via API

```bash
# Get all ports
curl http://localhost:8005/ports | jq

# Get specific port
curl http://localhost:8005/ports/1 | jq

# Get all devices
curl http://localhost:8005/devices | jq

# Get MC96 devices only
curl http://localhost:8005/mc96/devices | jq

# Force handshake on port 1
curl -X POST http://localhost:8005/handshake \
  -H "Content-Type: application/json" \
  -d '{"port": 1}'

# Get statistics
curl http://localhost:8005/statistics | jq
```

---

## 📊 Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **Master Dashboard** | http://localhost:8501 | Main control center |
| **Slack Dashboard** | http://localhost:8506 | Manage Slack integration |
| **Slack API** | http://localhost:8003 | Slack webhooks & API |
| **Network Agent** | http://localhost:8005 | Network monitoring API |
| **API Docs (Slack)** | http://localhost:8003/docs | Interactive API docs |
| **API Docs (Network)** | http://localhost:8005/docs | Interactive API docs |

---

## ⚙️ Configuration

### Environment Variables

Add to `~/.zshrc` or `~/.bashrc`:

```bash
# Slack Configuration (Required)
export SLACK_BOT_TOKEN="xoxb-your-token-here"
export SLACK_SIGNING_SECRET="your-signing-secret-here"

# Slack Channels (Optional)
export SLACK_ALERTS_CHANNEL="#noizylab-alerts"
export SLACK_MONITORING_CHANNEL="#noizylab-monitor"
export SLACK_EMAIL_CHANNEL="#noizylab-email"
export SLACK_NETWORK_CHANNEL="#noizylab-network"

# Network Agent Configuration (Optional)
export DGS1210_IP="192.168.1.1"
export SNMP_COMMUNITY="public"
export MC96_PORTS="1,2,3"
```

Then reload:
```bash
source ~/.zshrc
```

### Database Locations

```bash
# Slack database
/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db

# Network database
/Users/m2ultra/NOIZYLAB/network/network_devices.db
```

### Query Databases

```bash
# View recent Slack notifications
sqlite3 integrations/slack/slack_data.db \
  "SELECT * FROM slack_notifications ORDER BY sent_at DESC LIMIT 10"

# View network devices
sqlite3 network/network_devices.db \
  "SELECT * FROM network_devices"

# View handshake log
sqlite3 network/network_devices.db \
  "SELECT * FROM handshake_log ORDER BY timestamp DESC LIMIT 10"

# View MC96 devices
sqlite3 network/network_devices.db \
  "SELECT * FROM mc96_devices"
```

---

## 🔧 Customization

### Add Custom Handshake Protocol

```python
# In your code
from network.dgs1210_network_agent import DGS1210Agent

agent = DGS1210Agent()

def my_custom_handshake(device):
    # Your custom logic here
    success = do_something(device.ip_address)
    details = {"custom_field": "value"}
    return success, details

# Register custom handler
agent.handshake_handlers["custom"] = my_custom_handshake
```

### Add Custom Slack Notification

```python
from integrations.slack.slack_core import SlackClient, SlackBlockBuilder

client = SlackClient()

# Build custom blocks
blocks = [
    SlackBlockBuilder.header("🎨 Custom Notification"),
    SlackBlockBuilder.section("Your custom content here"),
    SlackBlockBuilder.divider(),
    SlackBlockBuilder.actions([
        SlackBlockBuilder.button("Click Me", "action_id", "value")
    ])
]

# Send
client.send_rich_notification("#general", blocks)
```

### Integrate into Your Services

```python
# At top of any NoizyLab service
import sys
sys.path.append('/Users/m2ultra/NOIZYLAB/integrations/slack')

from slack_notifier import alert, network_event, email_event

# Use throughout your code
alert("Service started", "success")
network_event("device_connected", "MyDevice", {"details": "..."})
email_event("received", {"from": "user@example.com", "subject": "..."})
```

---

## 📱 Slack Slash Commands

Configure these in your Slack App settings:

### Command Setup

1. Go to your Slack App → **Slash Commands**
2. Add these commands:

| Command | Request URL | Description |
|---------|-------------|-------------|
| `/noizylab-status` | `http://your-domain:8003/commands/status` | System status |
| `/noizylab-services` | `http://your-domain:8003/commands/services` | Manage services |
| `/noizylab-notify` | `http://your-domain:8003/commands/notify` | Send alert |
| `/noizylab-logs` | `http://your-domain:8003/commands/logs` | View logs |
| `/noizylab-deploy` | `http://your-domain:8003/commands/deploy` | Deploy |

### Usage

```
# In Slack
/noizylab-status
/noizylab-services
/noizylab-notify System is running smoothly
/noizylab-logs email
/noizylab-deploy frontend
```

---

## 🐛 Troubleshooting

### Slack Not Working

```bash
# Check environment
echo $SLACK_BOT_TOKEN

# Test connection
curl http://localhost:8003/health

# Send test notification
curl -X POST http://localhost:8003/notify/system-alert \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","message":"Hello","level":"info"}'
```

### Network Agent Not Detecting

```bash
# Check agent health
curl http://localhost:8005/health

# Verify switch reachable
ping $DGS1210_IP

# Test SNMP
snmpwalk -v2c -c public $DGS1210_IP

# Check port status
curl http://localhost:8005/ports | jq
```

### Services Not Starting

```bash
# Check PIDs
cat /Users/m2ultra/NOIZYLAB/.noizylab_pids

# Check ports
lsof -i :8001,8003,8005,8501,8506

# Kill stuck processes
kill $(cat /Users/m2ultra/NOIZYLAB/.noizylab_pids)
```

---

## 📚 Full Documentation

- **Slack Integration:** [integrations/slack/README.md](integrations/slack/README.md)
- **Network Agent:** [network/README.md](network/README.md)
- **Quick Start:** [NOIZYLAB_SLACK_QUICKSTART.md](NOIZYLAB_SLACK_QUICKSTART.md)

### API Documentation

- Slack API Docs: http://localhost:8003/docs
- Network API Docs: http://localhost:8005/docs

---

## 🎓 Learning Path

### Day 1: Setup & Testing
1. Configure Slack app and tokens
2. Launch all services
3. Send test notifications
4. Monitor Master Dashboard

### Day 2: Network Monitoring
1. Configure MC96 ports
2. Plug in test device
3. Watch auto-handshake
4. Check Slack notifications

### Day 3: Integration
1. Add alerts to your code
2. Create custom notifications
3. Build custom handshakes
4. Set up slash commands

### Day 4: Production
1. Set up systemd/launchd services
2. Configure monitoring
3. Set up logging
4. Create dashboards

---

## ✨ Key Features Summary

### ✅ Completed & Ready
- [x] Slack core library with full API
- [x] Slack API server with webhooks
- [x] Slack dashboard UI
- [x] Network agent with SNMP monitoring
- [x] Auto device detection
- [x] MC96 auto-handshake protocol
- [x] Multiple handshake protocols
- [x] Real-time Slack notifications
- [x] Complete database logging
- [x] RESTful APIs
- [x] Master dashboard integration
- [x] Comprehensive documentation
- [x] Startup scripts
- [x] Quick start guide

### 🔥 Advanced Features
- Multiple handshake protocols
- Vendor detection from MAC
- Hostname resolution
- Port event logging
- Handshake history
- Statistics and analytics
- Interactive Slack components
- Rich message formatting
- Database audit trails
- Health monitoring
- API documentation

---

## 🎉 You're All Set!

Your NoizyLab Portal now has enterprise-grade:
- ✅ Slack integration with real-time notifications
- ✅ DGS1210 network monitoring
- ✅ Automatic device detection and handshake
- ✅ MC96-specific auto-configuration
- ✅ Unified dashboard and control
- ✅ Complete API access
- ✅ Full documentation

**Just plug in a device and watch the magic! 🪄**

---

## 📞 Quick Reference

```bash
# Launch everything
./LAUNCH_NOIZYLAB_COMPLETE.sh

# Send Slack alert
curl -X POST localhost:8003/notify/system-alert \
  -H "Content-Type: application/json" \
  -d '{"title":"Alert","message":"Hello","level":"info"}'

# Check network
curl localhost:8005/ports | jq

# View MC96 devices
curl localhost:8005/mc96/devices | jq

# Access dashboards
open http://localhost:8501  # Master
open http://localhost:8506  # Slack
```

---

**Built with ❤️ for NoizyLab Portal**

*Now go plug something into your DGS1210 and watch the notifications fly!* 🚀

