# 🐳 Docker Deployment Guide - NoizyLab

## **One-Command Deployment with Docker!**

---

## 🚀 **Quick Start (30 seconds)**

```bash
# 1. Set environment variables
cp .env.example .env
# Edit .env with your settings

# 2. Start everything
docker-compose up -d

# 3. Check status
docker-compose ps

# Done! 🎉
```

---

## 📦 **What Gets Deployed**

### **Services**:
1. **Master Dashboard** (port 8501) - Main UI
2. **Slack API** (port 8003) - Slack integration
3. **Network Agent** (port 8005) - DGS1210 monitoring
4. **Intelligent Monitor** - Background monitoring
5. **Prometheus** (port 9090) - Metrics collection
6. **Grafana** (port 3000) - Beautiful visualizations
7. **Webhook Manager** (port 8006) - Webhook routing

### **Volumes** (Persistent Data):
- `slack-data` - Slack integration data
- `network-data` - Network monitoring data
- `monitoring-data` - System metrics
- `prometheus-data` - Prometheus time-series data
- `grafana-data` - Grafana dashboards & config
- `webhook-data` - Webhook logs

---

## ⚙️ **Configuration**

### **1. Environment Variables** (`.env` file):

```bash
# Slack (Required for Slack features)
SLACK_BOT_TOKEN=xoxb-your-token
SLACK_SIGNING_SECRET=your-secret
SLACK_ALERTS_CHANNEL=#noizylab-alerts
SLACK_NETWORK_CHANNEL=#noizylab-network

# Network
DGS1210_IP=192.168.1.1
SNMP_COMMUNITY=public
MC96_PORTS=1,2,3

# Monitoring
MONITOR_INTERVAL=60

# AI (Optional but recommended)
OPENAI_API_KEY=sk-your-key

# Grafana
GRAFANA_PASSWORD=admin
```

### **2. Custom Configuration** (`config.yaml`):

Edit thresholds, intervals, and features in `config.yaml`.

---

## 🎯 **Commands**

### **Start Services**:
```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d slack-api

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f network-agent
```

### **Stop Services**:
```bash
# Stop all
docker-compose down

# Stop and remove volumes (CAREFUL!)
docker-compose down -v
```

### **Restart Services**:
```bash
# Restart all
docker-compose restart

# Restart specific
docker-compose restart slack-api
```

### **Update & Rebuild**:
```bash
# Rebuild after code changes
docker-compose build

# Rebuild and restart
docker-compose up -d --build

# Rebuild specific service
docker-compose build slack-api
docker-compose up -d slack-api
```

---

## 📊 **Access Points**

| Service | URL | Description |
|---------|-----|-------------|
| Master Dashboard | http://localhost:8501 | Main control panel |
| Slack API | http://localhost:8003 | Slack integration API |
| Network Agent | http://localhost:8005 | Network monitoring |
| Prometheus | http://localhost:9090 | Metrics & alerts |
| Grafana | http://localhost:3000 | Dashboards |
| Webhook Manager | http://localhost:8006 | Webhook routing |

---

## 🔍 **Monitoring & Logs**

### **View Logs**:
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f slack-api

# Last 100 lines
docker-compose logs --tail=100 network-agent

# Since timestamp
docker-compose logs --since 2024-01-01T00:00:00
```

### **Check Health**:
```bash
# Service status
docker-compose ps

# Detailed stats
docker stats

# Inspect service
docker-compose exec slack-api sh
```

---

## 💾 **Backup & Restore**

### **Backup Volumes**:
```bash
# Backup all volumes
docker run --rm \
  -v noizylab_slack-data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/slack-data-$(date +%Y%m%d).tar.gz -C /data .

# Backup script provided
./backup_docker_volumes.sh
```

### **Restore Volume**:
```bash
# Stop services first
docker-compose down

# Restore
docker run --rm \
  -v noizylab_slack-data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar xzf /backup/slack-data-YYYYMMDD.tar.gz -C /data

# Restart
docker-compose up -d
```

---

## 🔧 **Troubleshooting**

### **Service Won't Start**:
```bash
# Check logs
docker-compose logs SERVICE_NAME

# Check if port is in use
lsof -i :8003

# Remove and recreate
docker-compose rm -f SERVICE_NAME
docker-compose up -d SERVICE_NAME
```

### **Network Issues**:
```bash
# Check networks
docker network ls
docker network inspect noizylab_noizylab

# Recreate network
docker-compose down
docker network prune
docker-compose up -d
```

### **Permission Issues**:
```bash
# Fix volume permissions
docker-compose exec SERVICE_NAME chown -R app:app /app/data
```

### **Out of Disk Space**:
```bash
# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Clean everything
docker system prune -a --volumes
```

---

## 🎯 **Production Deployment**

### **1. Use Production Compose File**:

Create `docker-compose.prod.yml`:
```yaml
version: '3.8'
services:
  master-dashboard:
    restart: always
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
  # ... rest of services
```

### **2. Deploy**:
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### **3. Set up Monitoring**:
- Configure Prometheus alerts
- Set up Grafana dashboards
- Configure Slack notifications

### **4. Automated Backups**:
```bash
# Add to crontab
0 2 * * * cd /path/to/noizylab && ./backup_docker_volumes.sh
```

---

## 🔒 **Security**

### **Best Practices**:

1. **Use secrets**:
```bash
# Store secrets in Docker secrets
echo "xoxb-token" | docker secret create slack_token -
```

2. **Limit network exposure**:
```yaml
# Only expose necessary ports
ports:
  - "127.0.0.1:8003:8003"  # Only localhost
```

3. **Run as non-root**:
```dockerfile
USER nobody
```

4. **Keep images updated**:
```bash
docker-compose pull
docker-compose up -d
```

---

## 📈 **Scaling**

### **Scale Services**:
```bash
# Run multiple instances
docker-compose up -d --scale slack-api=3

# With load balancer
# Add nginx/traefik in front
```

---

## 🎓 **Tips & Tricks**

### **Development Mode**:
```bash
# Mount code as volume for live reload
docker-compose -f docker-compose.dev.yml up
```

### **Execute Commands**:
```bash
# Run command in container
docker-compose exec slack-api python3 -c "print('hello')"

# Open shell
docker-compose exec slack-api sh

# Run one-off command
docker-compose run --rm slack-api python3 script.py
```

### **Resource Limits**:
```yaml
services:
  slack-api:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

---

## 🚀 **Quick Deploy Script**

Save as `deploy.sh`:
```bash
#!/bin/bash
set -e

echo "🚀 Deploying NoizyLab..."

# Pull latest
git pull

# Rebuild
docker-compose build

# Stop old
docker-compose down

# Start new
docker-compose up -d

# Health check
sleep 10
docker-compose ps

echo "✅ Deployment complete!"
```

---

## 📚 **Resources**

- **Docker Compose Docs**: https://docs.docker.com/compose/
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000

---

## 🎉 **Done!**

Your entire NoizyLab system is now containerized and production-ready!

```bash
# Start everything
docker-compose up -d

# Access dashboards
open http://localhost:8501  # Master
open http://localhost:3000  # Grafana
```

**Enterprise deployment in 30 seconds!** 🚀

