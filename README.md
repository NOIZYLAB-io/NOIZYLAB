# NOIZYLAB

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
```

See [Setup Scripts Documentation](./scripts/README.md) for details.

## Configuration

### ACL Templates
Pre-configured Access Control Lists for NOIZYLAB infrastructure:

```bash
# View and customize the ACL template
cat config/tailscale-acl-template.json
```

Apply at: https://login.tailscale.com/admin/acls

See [Configuration Documentation](./config/README.md) for details.

## Documentation

- [Email System Setup](./CODE_MASTER/NOIZYLAB_EMAIL_SYSTEM_COMPLETE.md)
- [Tailscale Network Setup](./CODE_MASTER/TAILSCALE_SETUP.md) - Comprehensive guide
- [Tailscale Setup Scripts](./scripts/README.md) - Automated installation
- [Tailscale Configuration](./config/README.md) - ACL templates and policies