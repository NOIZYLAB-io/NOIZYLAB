# Tailscale Infrastructure Monitoring

This directory contains monitoring and alerting tools for NOIZYLAB Tailscale infrastructure.

## Monitoring Script

**Script**: `monitor-tailscale.sh`

Automated monitoring script that checks Tailscale health and sends alerts on issues.

### Features

- **Health Checks**:
  - Installation verification
  - Service status monitoring
  - Network connectivity
  - Peer connection tracking
  - Network diagnostics

- **Alerting**:
  - Email notifications
  - Webhook integration
  - Severity levels (CRITICAL, WARNING, INFO)

- **Metrics Collection**:
  - Connection status
  - IP addresses
  - Peer count
  - Version information
  - Timestamps

### Usage

#### Manual Run

```bash
./scripts/monitor-tailscale.sh
```

#### Verbose Output

```bash
VERBOSE=1 ./scripts/monitor-tailscale.sh
```

#### With Email Alerts

```bash
ALERT_EMAIL="admin@noizylab.com" ./scripts/monitor-tailscale.sh
```

#### With Webhook Alerts

```bash
ALERT_WEBHOOK="https://hooks.slack.com/services/YOUR/WEBHOOK/URL" \
./scripts/monitor-tailscale.sh
```

### Automated Monitoring (Cron)

Add to crontab for continuous monitoring:

```bash
# Check every 5 minutes
*/5 * * * * /path/to/scripts/monitor-tailscale.sh

# Check every hour with email alerts
0 * * * * ALERT_EMAIL="admin@noizylab.com" /path/to/scripts/monitor-tailscale.sh

# Daily verbose report
0 9 * * * VERBOSE=1 ALERT_EMAIL="admin@noizylab.com" /path/to/scripts/monitor-tailscale.sh
```

### References

- [Complete Setup Guide](../CODE_MASTER/TAILSCALE_SETUP.md)
- [Health Check Script](../scripts/healthcheck-tailscale.sh)
- [Configuration Script](../scripts/configure-tailscale.sh)
