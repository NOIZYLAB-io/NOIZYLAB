# Tailscale Setup Scripts

Automated setup scripts for installing and configuring Tailscale on different platforms for NOIZYLAB infrastructure.

## Available Scripts

### macOS
**Script**: `setup-tailscale-macos.sh`

Automatically installs Tailscale using Homebrew and launches the application.

```bash
./scripts/setup-tailscale-macos.sh
```

**What it does:**
- Checks/installs Homebrew if needed
- Installs Tailscale via Homebrew
- Launches the Tailscale app
- Provides next steps for authentication

### Linux
**Script**: `setup-tailscale-linux.sh`

Automatically detects your Linux distribution and installs Tailscale using the appropriate package manager.

```bash
./scripts/setup-tailscale-linux.sh
```

**Supported distributions:**
- Ubuntu/Debian
- Fedora/RHEL/CentOS
- Arch Linux/Manjaro
- Other distributions (downloads installer for manual review)

**What it does:**
- Detects your Linux distribution
- Adds Tailscale repository
- Installs Tailscale
- Enables and starts the Tailscale service
- Connects to your Tailscale network
- Shows connection status

### Windows
**Script**: `setup-tailscale-windows.ps1`

Automatically installs Tailscale using winget, Chocolatey, or direct download.

```powershell
# Run as Administrator
.\scripts\setup-tailscale-windows.ps1
```

**What it does:**
- Checks for Administrator privileges
- Tries installation via winget first
- Falls back to Chocolatey if available
- Downloads installer directly if needed
- Starts Tailscale service
- Launches the Tailscale GUI
- Provides next steps for authentication

**Parameters:**
- `-Force`: Reinstall even if already installed

## Quick Start

1. **Choose your platform** and run the appropriate script
2. **Follow the on-screen instructions** to complete setup
3. **Authenticate** when prompted (via browser)
4. **Verify connection** by running:
   ```bash
   tailscale status
   ```

## After Installation

Once Tailscale is installed and connected:

1. Check your Tailscale IP:
   ```bash
   # macOS/Linux
   tailscale ip -4
   
   # Windows
   tailscale.exe ip -4
   ```

2. View connected devices:
   ```bash
   # macOS/Linux
   tailscale status
   
   # Windows
   tailscale.exe status
   ```

3. For advanced configuration options, see: [TAILSCALE_SETUP.md](../CODE_MASTER/TAILSCALE_SETUP.md)

## Troubleshooting

### macOS
- If Homebrew installation fails, install manually from App Store
- Link: https://apps.apple.com/ca/app/tailscale/id1475387142?mt=12

### Linux
- Ensure you have `sudo` privileges
- For unsupported distributions, review `/tmp/tailscale-install.sh` before running

### Windows
- Script must be run as Administrator
- If all installation methods fail, download manually from: https://tailscale.com/download/windows

## Security Notes

- All scripts follow security best practices:
  - Linux script avoids piping remote scripts directly to shell
  - Windows script verifies Administrator privileges
  - Downloads are from official Tailscale sources only
- Review scripts before running if you have security concerns
- See [TAILSCALE_SETUP.md](../CODE_MASTER/TAILSCALE_SETUP.md) for additional security recommendations

## Manual Installation

If automated scripts don't work for your environment, see [TAILSCALE_SETUP.md](../CODE_MASTER/TAILSCALE_SETUP.md) for manual installation instructions.

## Support

For issues with these scripts:
1. Check script output for error messages
2. Verify system requirements (sudo access, internet connectivity)
3. Try manual installation from official sources
4. Contact NOIZYLAB DevOps team

For Tailscale-specific issues:
- [Tailscale Documentation](https://tailscale.com/kb/)
- [Tailscale Support](https://tailscale.com/contact/support/)
