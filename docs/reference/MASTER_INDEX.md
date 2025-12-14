# 📚 NoizyLab Portal - Master Index

## **Complete System Documentation Index**

---

## 🚀 **Getting Started** (Start Here!)

1. **[README.md](README.md)** - Main documentation & overview
2. **[NOIZYLAB_SLACK_QUICKSTART.md](NOIZYLAB_SLACK_QUICKSTART.md)** - 5-minute quick start
3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - One-page cheat sheet
4. **Setup Wizard** - Run: `./scripts/setup_wizard.sh`

---

## 📖 **Complete Guides**

### **System Guides**
- **[SLACK_NETWORK_COMPLETE_GUIDE.md](SLACK_NETWORK_COMPLETE_GUIDE.md)** - Complete Slack & Network guide
- **[COMPLETE_SYSTEM_FINAL.md](COMPLETE_SYSTEM_FINAL.md)** - Final complete system guide
- **[SYSTEM_SUMMARY.md](SYSTEM_SUMMARY.md)** - System overview & summary

### **Feature-Specific**
- **[AI_INTEGRATION_COMPLETE.md](AI_INTEGRATION_COMPLETE.md)** - AI features guide
- **[AI_FEATURES_DEMO.md](AI_FEATURES_DEMO.md)** - Live AI demos
- **[ai/README_AI.md](ai/README_AI.md)** - AI API documentation
- **[DOCKER_GUIDE.md](DOCKER_GUIDE.md)** - Docker deployment guide

### **Component Docs**
- **[integrations/slack/README.md](integrations/slack/README.md)** - Slack integration
- **[network/README.md](network/README.md)** - Network monitoring
- **[FINAL_COMPLETE_SUMMARY.md](FINAL_COMPLETE_SUMMARY.md)** - Final summary

---

## 💻 **Code Examples**

### **Slack Integration**
- **[examples/slack_integration_example.py](examples/slack_integration_example.py)** - Slack examples
- 7 complete examples showing all Slack features

### **AI Integration**
- **[examples/ai_integration_example.py](examples/ai_integration_example.py)** - AI examples
- 6 examples showing AI capabilities

### **Complete Workflow**
- **[examples/complete_workflow_example.py](examples/complete_workflow_example.py)** - End-to-end workflow
- Real production simulation

---

## 🔧 **Setup & Configuration**

### **Installation**
- **[install_dependencies.sh](install_dependencies.sh)** - Install all dependencies
- **[requirements.txt](requirements.txt)** - Python packages
- **[scripts/setup_wizard.sh](scripts/setup_wizard.sh)** - Interactive setup

### **Configuration**
- **[config.yaml](config.yaml)** - Main configuration file
- **[.env.example](.env.example)** - Environment variables template

### **Deployment**
- **[LAUNCH_NOIZYLAB_COMPLETE.sh](LAUNCH_NOIZYLAB_COMPLETE.sh)** - Master launcher
- **[docker-compose.yml](docker-compose.yml)** - Docker deployment
- **[Makefile](Makefile)** - Make commands

---

## 📊 **Components**

### **Slack Integration** (`integrations/slack/`)
- `slack_core.py` - Core client
- `slack_api_server.py` - API server
- `slack_dashboard.py` - UI dashboard
- `slack_notifier.py` - Easy integration
- `slack_analytics.py` - Analytics engine

### **Network Monitoring** (`network/`)
- `dgs1210_network_agent.py` - Main agent
- `network_agent_service.py` - API service
- `device_fingerprinting.py` - Device classification

### **AI Systems** (`ai/`)
- `ai_operations_agent.py` - Operations AI
- `intelligent_log_analyzer.py` - Log analysis
- `predictive_capacity_planner.py` - Capacity planning
- `ai_chat_interface.py` - Chat interface

### **Monitoring** (`monitoring/`)
- `intelligent_monitor.py` - System monitoring

### **Automation** (`automation/`)
- `auto_optimizer.py` - Auto-optimization
- `self_healing.py` - Self-healing
- `backup_manager.py` - Backup system

### **Analytics** (`analytics/`)
- `performance_profiler.py` - Performance profiling
- `alert_correlation.py` - Alert correlation

### **Security** (`security/`)
- `api_security.py` - API authentication

### **Other**
- `integrations/webhook_manager.py` - Webhook routing
- `integrations/email_notifier.py` - Email notifications
- `integrations/prometheus_exporter.py` - Prometheus metrics

---

## 💻 **CLI Commands**

### **Service Management**
```bash
noizylab_cli.py start/stop/restart
noizylab_cli.py status
noizylab_cli.py health
noizylab_cli.py doctor
```

### **Slack**
```bash
noizylab_cli.py slack send "message"
noizylab_cli.py slack channels
noizylab_cli.py slack stats
```

### **Network**
```bash
noizylab_cli.py network ports
noizylab_cli.py network devices
noizylab_cli.py network mc96
noizylab_cli.py network handshake PORT
```

### **AI**
```bash
noizylab_cli.py ai chat
noizylab_cli.py ai ask "question"
noizylab_cli.py ai analyze-logs FILE
noizylab_cli.py ai capacity
```

---

## 🐳 **Docker**

### **Files**
- `docker-compose.yml` - Main compose file
- `Dockerfile` - Base image
- `Dockerfile.slack` - Slack service
- `Dockerfile.network` - Network agent
- `Dockerfile.monitor` - Monitor service
- `Dockerfile.webhooks` - Webhook manager
- `.dockerignore` - Docker ignore file

### **Commands**
```bash
docker-compose up -d        # Start
docker-compose down         # Stop
docker-compose logs -f      # Logs
docker-compose ps           # Status
```

---

## 🧪 **Testing**

### **Test Files**
- `tests/test_slack_integration.py`
- `tests/test_network_agent.py`
- `tests/test_ai_features.py`
- `tests/run_all_tests.sh`

### **Run Tests**
```bash
make test                   # All tests
python3 tests/test_*.py     # Individual
```

---

## 🔄 **Automation Scripts**

### **Daily Tasks**
- `scripts/daily_health_check.sh` - Daily health check
- Add to cron: `0 9 * * * ~/NOIZYLAB/scripts/daily_health_check.sh`

### **Service Management**
- `scripts/install_as_service.sh` - Install as macOS service
- `scripts/setup_wizard.sh` - Interactive setup

### **Startup Scripts**
- `integrations/slack/start_slack_services.sh`
- `network/start_network_agent.sh`

---

## 📈 **Monitoring & Metrics**

### **Prometheus**
- Config: `prometheus/prometheus.yml`
- Alerts: `prometheus/alerts.yml`
- URL: http://localhost:9090

### **Grafana**
- Dashboards: `grafana/dashboards/`
- Datasources: `grafana/datasources/`
- URL: http://localhost:3000

### **Custom Metrics**
- `integrations/prometheus_exporter.py` - Export custom metrics

---

## 💾 **Databases**

| Database | Location | Purpose |
|----------|----------|---------|
| slack_data.db | integrations/slack/ | Slack data |
| network_devices.db | network/ | Network monitoring |
| monitoring.db | monitoring/ | System metrics |
| ai_operations.db | ai/ | AI analyses |
| optimizer.db | automation/ | Optimization history |
| self_healing.db | automation/ | Healing logs |
| performance.db | analytics/ | Performance data |
| correlation.db | analytics/ | Alert correlation |

---

## 🔑 **Environment Variables**

```bash
# Slack (Required for Slack features)
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
SLACK_ALERTS_CHANNEL=#noizylab-alerts
SLACK_NETWORK_CHANNEL=#noizylab-network

# Network (Optional)
DGS1210_IP=192.168.1.1
SNMP_COMMUNITY=public
MC96_PORTS=1,2,3

# AI (Optional, ~$2/month)
OPENAI_API_KEY=sk-...

# Email (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_USER=your@email.com
SMTP_PASSWORD=yourpassword
```

---

## 🚨 **Common Issues**

### **Services Won't Start**
```bash
make doctor                 # Run diagnostics
make clean                  # Clean temp files
kill $(cat .noizylab_pids)  # Kill stuck processes
```

### **Slack Not Working**
```bash
echo $SLACK_BOT_TOKEN       # Verify token set
curl localhost:8003/health  # Check API
# Invite bot to channels in Slack
```

### **Network Not Detecting**
```bash
ping $DGS1210_IP            # Check switch reachable
snmpwalk -v2c -c public $DGS1210_IP  # Test SNMP
curl localhost:8005/health  # Check agent
```

---

## 📊 **System Overview**

```
Master Dashboard (8501)
    ├── Slack Integration (8003, 8506)
    ├── Network Agent (8005)
    ├── Monitoring System
    ├── AI Systems
    └── Automation
```

---

## 🎯 **Quick Tasks**

| Task | Command |
|------|---------|
| Start system | `make start` |
| Check status | `make status` |
| Send Slack message | `make slack-send` |
| View network ports | `make network-ports` |
| Run AI chat | `make ai-chat` |
| Optimize system | `make optimize` |
| Create backup | `make backup` |
| Run tests | `make test` |
| Open dashboard | `make dashboard` |

---

## 💡 **Pro Tips**

1. **Use Makefile** - `make help` shows all commands
2. **Set OpenAI Key** - 10X better AI for $2/month
3. **Run Daily Health** - Add to cron
4. **Use Docker** - Easy deployment
5. **Check Logs** - `make logs` or `logs/` directory
6. **Try AI Chat** - Most fun way to manage system
7. **Enable Auto-healing** - Set it and forget it

---

## 📞 **Get Help**

```bash
make help                   # Makefile commands
python3 noizylab_cli.py --help  # CLI help
python3 noizylab_cli.py doctor  # System diagnostics
```

---

## 🎓 **Learning Path**

1. **Day 1**: Setup → `./scripts/setup_wizard.sh`
2. **Day 2**: Try examples → `examples/`
3. **Day 3**: Configure Slack → See Slack README
4. **Day 4**: Add AI → Set OpenAI key
5. **Day 5**: Production → Docker deploy

---

**Bookmark this page!** 📑

**Everything you need on one page!** ⚡

