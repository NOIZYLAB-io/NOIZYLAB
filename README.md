# NOIZYLAB

## Complete Infrastructure Build

### One-Command Full Setup
Run the complete end-to-end Tailscale infrastructure deployment:

```bash
./scripts/build-complete-infrastructure.sh
```

This master orchestration script will:
1. Install Tailscale for your platform
2. Wait for authentication
3. Configure advanced features (interactive)
4. Run comprehensive health checks
5. Provide ACL setup instructions

All steps are logged and verified automatically.

## Quick Setup

### Tailscale Network Setup
Automated setup scripts for installing Tailscale:

```bash
# macOS
./scripts/setup-tailscale-macos.sh

# Linux
./scripts/setup-tailscale-linux.sh

# Windows (PowerShell as Administrator)
.\scripts\setup-tailscale-windows.ps1
```

After installation, configure and verify:

```bash
# Configure advanced options (MagicDNS, subnet routing, SSH, etc.)
./scripts/configure-tailscale.sh

# Run health check
./scripts/healthcheck-tailscale.sh

# Set up continuous monitoring
./scripts/monitor-tailscale.sh
```

See [Setup Scripts Documentation](./scripts/README.md) for details.

## Docker Deployment

### Quick Start with Docker

```bash
# Build and run
docker-compose up -d

# Or using Docker directly
docker build -t noizylab-tailscale .
docker run -d --name noizylab-ts \
  --cap-add=NET_ADMIN \
  -e TAILSCALE_AUTH_KEY=your-auth-key \
  noizylab-tailscale
```

### Environment Configuration

Copy and customize environment variables:

```bash
cp .env.example .env
# Edit .env with your Tailscale auth key and configuration
```

See [Dockerfile](./Dockerfile) and [docker-compose.yml](./docker-compose.yml) for details.

## Monitoring & Alerting

### Continuous Monitoring

Set up automated health monitoring:

```bash
# Manual monitoring check
./scripts/monitor-tailscale.sh

# With email alerts
ALERT_EMAIL="admin@noizylab.com" ./scripts/monitor-tailscale.sh

# Automated via cron (check every 5 minutes)
*/5 * * * * /path/to/scripts/monitor-tailscale.sh
```

See [Monitoring Documentation](./docs/MONITORING.md) for details.

## Configuration

### ACL Templates
Pre-configured Access Control Lists for NOIZYLAB infrastructure:

```bash
# View and customize the ACL template
cat config/tailscale-acl-template.json
```

Apply at: https://login.tailscale.com/admin/acls

See [Configuration Documentation](./config/README.md) for details.

## CI/CD Integration

Automated testing and deployment with GitHub Actions:

- **Script Validation**: ShellCheck linting
- **JSON Validation**: ACL template verification
- **Docker Build**: Multi-platform container builds
- **Security Scanning**: Trivy vulnerability scanning
- **Automated Deployment**: Container registry publishing

See [.github/workflows/tailscale-ci.yml](./.github/workflows/tailscale-ci.yml) for details.

## Documentation

- [Email System Setup](./CODE_MASTER/NOIZYLAB_EMAIL_SYSTEM_COMPLETE.md)
- [Tailscale Network Setup](./CODE_MASTER/TAILSCALE_SETUP.md) - Comprehensive guide
- [Tailscale Setup Scripts](./scripts/README.md) - Automated installation
- [Tailscale Configuration](./config/README.md) - ACL templates and policies
- [Monitoring & Alerting](./docs/MONITORING.md) - Health monitoring setup

## Architecture

```
NOIZYLAB Tailscale Infrastructure
├── Installation (setup-tailscale-*.sh)
├── Configuration (configure-tailscale.sh)
├── Health Monitoring (healthcheck-tailscale.sh, monitor-tailscale.sh)
├── Docker Deployment (Dockerfile, docker-compose.yml)
├── CI/CD Pipeline (.github/workflows/tailscale-ci.yml)
├── ACL Templates (config/tailscale-acl-template.json)
└── Complete Orchestration (build-complete-infrastructure.sh)
```

## Quick Reference

| Task | Command |
|------|---------|
| Complete Setup | `./scripts/build-complete-infrastructure.sh` |
| Install | `./scripts/setup-tailscale-{macos\|linux}.sh` |
| Configure | `./scripts/configure-tailscale.sh` |
| Health Check | `./scripts/healthcheck-tailscale.sh` |
| Monitor | `./scripts/monitor-tailscale.sh` |
| Docker Run | `docker-compose up -d` |
| View Status | `tailscale status` |
| View IP | `tailscale ip` |