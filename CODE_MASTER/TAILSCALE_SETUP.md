# Tailscale Setup for NOIZYLAB

## Overview
Tailscale is a secure network solution that creates a private mesh network for the NOIZYLAB infrastructure. This document provides complete setup and configuration instructions for integrating Tailscale with NOIZYLAB.

## What is Tailscale?
Tailscale is a zero-config VPN built on WireGuard that creates a secure network between your devices. It provides:
- **Secure connectivity** across different networks
- **Easy device management** with centralized control
- **No complex configuration** required
- **End-to-end encryption** for all traffic

## Installation

### macOS Installation
1. **Download from App Store**: [Tailscale for macOS](https://apps.apple.com/ca/app/tailscale/id1475387142?mt=12)
2. **Alternative via Homebrew**:
   ```bash
   brew install --cask tailscale
   ```

### Linux Installation
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### Windows Installation
Download the installer from [Tailscale Downloads](https://tailscale.com/download)

## Initial Setup

### 1. Start Tailscale
After installation, launch the Tailscale app and sign in with your account.

**macOS/Windows**: Click the Tailscale icon in the system tray
**Linux**: Run `sudo tailscale up`

### 2. Authenticate
Follow the browser prompt to authenticate with:
- Google
- Microsoft
- GitHub
- Email

### 3. Connect to Network
Once authenticated, your device will automatically join your Tailscale network (tailnet).

## Configuration for NOIZYLAB

### Network Access
Ensure your Tailscale network has the following devices connected:
- Development machines
- Production servers
- Testing environments

### Access Control Lists (ACLs)
Configure ACLs in the Tailscale admin console to control access:

```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["tag:noizylab-servers:*"]
    }
  ]
}
```

### Subnet Routing
To access NOIZYLAB internal networks:

```bash
sudo tailscale up --advertise-routes=10.0.0.0/24
```

Approve the subnet routes in the Tailscale admin console.

## Using Tailscale with NOIZYLAB Services

### SSH Access
Connect to NOIZYLAB servers using Tailscale IPs:
```bash
ssh user@100.x.y.z
```

### Service Access
Access internal services securely:
- **Email System**: `http://noizylab-email.tailnet-name.ts.net`
- **API Endpoints**: `https://api.noizylab.tailnet-name.ts.net`
- **Database**: Connect using Tailscale IP for secure access

### Environment Variables
Update your NOIZYLAB configuration to use Tailscale networking:
```bash
export NOIZYLAB_HOST=100.x.y.z
export SECURE_NETWORK=tailscale
```

## Security Best Practices

1. **Enable MFA**: Always enable multi-factor authentication for your Tailscale account
2. **Regular Audits**: Review connected devices regularly
3. **Key Expiry**: Set appropriate key expiry times for devices
4. **ACL Reviews**: Regularly review and update access control lists
5. **Audit Logs**: Monitor Tailscale audit logs for suspicious activity

## Troubleshooting

### Connection Issues
```bash
# Check Tailscale status
tailscale status

# View connection details
tailscale netcheck

# Restart Tailscale
sudo tailscale down
sudo tailscale up
```

### DNS Resolution
If you experience DNS issues:
```bash
tailscale up --accept-dns=false
```

### Firewall Configuration
Ensure the following ports are allowed:
- UDP 41641 (Tailscale default)
- TCP 443 (for HTTPS connectivity)

## Advanced Features

### MagicDNS
Enable MagicDNS for easy device access by hostname:
1. Go to Tailscale admin console
2. Enable MagicDNS in DNS settings
3. Access devices: `ssh noizylab-server`

### Exit Nodes
Use a device as an exit node for routing all traffic:
```bash
# Advertise as exit node
sudo tailscale up --advertise-exit-node

# Use an exit node
sudo tailscale up --exit-node=100.x.y.z
```

### Taildrop
Share files between Tailscale devices:
```bash
tailscale file cp myfile.txt 100.x.y.z:
```

## Integration with NOIZYLAB Email System

For secure email relay through Tailscale:

1. Configure SMTP to use Tailscale IP:
   ```javascript
   let transporter = nodemailer.createTransport({
       host: '100.x.y.z',  // Tailscale IP of mail server
       port: 587,
       secure: false,
       auth: {
           user: 'user@noizylab.com',
           pass: process.env.EMAIL_PASSWORD
       }
   });
   ```

2. Update DNS records to include Tailscale endpoints
3. Configure firewall rules to accept connections from Tailscale subnet

## Monitoring and Maintenance

### Health Checks
Regularly verify Tailscale connectivity:
```bash
tailscale ping 100.x.y.z
```

### Updates
Keep Tailscale updated:
- **macOS**: Updates via App Store
- **Linux**: `sudo apt update && sudo apt upgrade tailscale`
- **Homebrew**: `brew upgrade tailscale`

### Backup Configuration
Export your Tailscale ACL configuration regularly from the admin console.

## Resources

- [Tailscale Documentation](https://tailscale.com/kb/)
- [Tailscale Admin Console](https://login.tailscale.com/admin)
- [Tailscale GitHub](https://github.com/tailscale)
- [Community Forum](https://forum.tailscale.com)

## Support

For NOIZYLAB-specific Tailscale issues:
1. Check Tailscale status: `tailscale status`
2. Review logs: `tailscale debug logs`
3. Contact NOIZYLAB DevOps team
4. Submit issue to Tailscale support if needed

## Conclusion

Tailscale provides secure, seamless networking for NOIZYLAB infrastructure. Follow the above guidelines to ensure proper setup and maintenance of your Tailscale network.
