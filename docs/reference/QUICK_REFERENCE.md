# 🚀 NoizyLab Quick Reference

## **ONE-PAGE CHEAT SHEET**

---

## ⚡ **Quick Commands**

### **Start/Stop**
```bash
make start              # Start everything
make stop               # Stop everything
make restart            # Restart everything
make status             # Check status
```

### **Docker**
```bash
make docker-up          # Start with Docker
make docker-down        # Stop Docker
docker-compose up -d    # Start services
docker-compose logs -f  # View logs
```

### **CLI**
```bash
python3 noizylab_cli.py status           # Service status
python3 noizylab_cli.py health           # Health check
python3 noizylab_cli.py doctor           # Diagnostics
python3 noizylab_cli.py slack send "Hi"  # Send to Slack
python3 noizylab_cli.py network ports    # Port status
python3 noizylab_cli.py ai chat          # AI chat
```

---

## 🔗 **Access Points**

| Service | URL |
|---------|-----|
| Master Dashboard | http://localhost:8501 |
| Slack Dashboard | http://localhost:8506 |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Slack API | http://localhost:8003 |
| Network Agent | http://localhost:8005 |

---

## 🤖 **AI Commands**

```bash
# Chat with AI
python3 ai/ai_chat_interface.py

# Ask question
python3 noizylab_cli.py ai ask "Why is CPU high?"

# Analyze logs
python3 noizylab_cli.py ai analyze-logs /path/to/log

# Capacity planning
python3 noizylab_cli.py ai capacity
```

---

## 📊 **Monitoring**

```bash
# System metrics
python3 -c "import psutil; print(f'CPU: {psutil.cpu_percent()}%')"

# Service health
curl http://localhost:8005/health | jq

# Port status
curl http://localhost:8005/ports | jq

# MC96 devices
curl http://localhost:8005/mc96/devices | jq
```

---

## 💬 **Slack Integration**

```python
# Send alert
from integrations.slack.slack_notifier import alert
alert("Message", "success")  # success, warning, error, info

# Network event
from integrations.slack.slack_notifier import network_event
network_event("connected", "Device", {"Port": "1"})

# System status
from integrations.slack.slack_notifier import system_status
system_status({"Service": "running"})
```

---

## 🌐 **Network Monitoring**

```bash
# View ports
python3 noizylab_cli.py network ports

# View devices
python3 noizylab_cli.py network devices

# MC96 devices
python3 noizylab_cli.py network mc96

# Force handshake
curl -X POST localhost:8005/handshake -d '{"port":1}'
```

---

## 🔧 **Automation**

```bash
# Optimize
python3 automation/auto_optimizer.py

# Self-heal
python3 automation/self_healing.py

# Backup
python3 automation/backup_manager.py create --type full

# Daily health
./scripts/daily_health_check.sh
```

---

## 🧪 **Testing**

```bash
# Run all tests
make test

# Individual tests
python3 tests/test_slack_integration.py
python3 tests/test_network_agent.py
python3 tests/test_ai_features.py
```

---

## 📦 **Backup & Restore**

```bash
# Create backup
make backup

# List backups
python3 automation/backup_manager.py list

# Restore
python3 automation/backup_manager.py restore --name BACKUP_NAME
```

---

## 🔐 **Environment Variables**

```bash
# Required for Slack
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_SIGNING_SECRET="..."

# Optional for Network
export DGS1210_IP="192.168.1.1"
export MC96_PORTS="1,2,3"

# Optional for AI
export OPENAI_API_KEY="sk-..."
```

---

## 🆘 **Troubleshooting**

```bash
# Check services
make status

# Run diagnostics
make doctor

# View logs
make logs

# Check specific service
curl http://localhost:PORT/health
```

---

## 📚 **Documentation**

- Main: `README.md`
- Quick Start: `NOIZYLAB_SLACK_QUICKSTART.md`
- AI Guide: `AI_INTEGRATION_COMPLETE.md`
- Docker: `DOCKER_GUIDE.md`
- Complete: `COMPLETE_SYSTEM_FINAL.md`

---

## 🎯 **Common Tasks**

### **Setup New Installation**
```bash
./scripts/setup_wizard.sh
```

### **Send Slack Test**
```bash
curl -X POST localhost:8003/notify/system-alert \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","message":"Hi","level":"info"}'
```

### **Check Network Port**
```bash
curl localhost:8005/ports/1 | jq
```

### **Run AI Chat**
```bash
python3 ai/ai_chat_interface.py
```

### **Get System Health**
```bash
python3 noizylab_cli.py health
```

---

## 💡 **Tips**

- Use `make help` for all commands
- Check logs in `logs/` directory
- Databases are in each module's directory
- Set OPENAI_API_KEY for 10X better AI
- Run `make daily` for daily health check

---

**Keep this page bookmarked!** 📑

