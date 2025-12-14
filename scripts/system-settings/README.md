# System Settings Scripts

macOS system configuration, optimization, and automation scripts for the NOIZYLAB platform.

## Overview

This directory contains scripts for configuring and optimizing macOS system settings, particularly for professional audio production workflows.

## Scripts

### System Configuration

**Purpose:** Automate macOS system preferences and settings for optimal audio production performance.

**Includes:**
- Network optimization (MTU, TCP/UDP tuning)
- iCloud sync configuration
- Spotlight indexing management
- Audio interface settings
- Performance tuning

## Usage

### Prerequisites
- macOS 12+ (Monterey or later)
- Administrator access
- Backup of current settings

### Running Scripts

```bash
# Make scripts executable
chmod +x *.sh

# Run configuration
./configure-system.sh

# Apply specific settings
./network-optimization.sh
./audio-settings.sh
```

## Configuration Areas

### Network Optimization

**Features:**
- MTU size adjustment (Jumbo Frames support)
- TCP/UDP stack tuning
- DNS cache management
- SMB optimization

**Example:**
```bash
# Enable Jumbo Frames (MTU 9000)
./network-optimization.sh --mtu 9000

# Optimize SMB
./network-optimization.sh --smb
```

### iCloud Settings

**Manages:**
- iCloud Drive sync
- iCloud Photos
- Screen Time settings
- System Settings access

**Example:**
```bash
# Configure iCloud sync
./icloud-settings.sh --enable-sync

# Fix greyed-out panels
./icloud-settings.sh --unlock-settings
```

### Audio Interface Configuration

**Optimizes:**
- Sample rate settings
- Buffer size
- Bit depth
- Aggregate devices
- MIDI configuration

**Example:**
```bash
# Set audio defaults
./audio-settings.sh --sample-rate 48000 --buffer-size 256
```

### Spotlight Management

**Controls:**
- Indexing settings
- Search domains
- Privacy exclusions
- Performance impact

**Example:**
```bash
# Exclude directories from indexing
./spotlight-settings.sh --exclude /path/to/audio/cache
```

## System Optimization

### Performance Tuning

Scripts optimize macOS for:
- Low-latency audio processing
- Large file operations
- Network throughput
- Resource management

### Settings Applied

```bash
# Audio production optimizations
- Disable system animations
- Reduce visual effects
- Prioritize audio processes
- Optimize memory management
- Configure swap behavior
```

## Configuration Files

### Settings Storage

System settings are stored in:
```
~/Library/Preferences/com.noizylab.system/
├── network-config.plist
├── audio-config.plist
├── icloud-config.plist
└── system-config.plist
```

### Backup & Restore

```bash
# Backup current settings
./backup-settings.sh --output ~/Desktop/settings-backup

# Restore settings
./restore-settings.sh --input ~/Desktop/settings-backup
```

## Safety Features

### Automatic Backups
- Settings backed up before changes
- Rollback capability
- Version tracking

### Validation
- Verify settings before apply
- Check for conflicts
- Confirm critical changes

### Logging
- All changes logged
- Timestamp tracking
- Success/failure reporting

## Common Tasks

### Initial Setup
```bash
# Complete system configuration for NOIZYLAB
./setup-noizylab-system.sh
```

### Network Optimization
```bash
# Optimize for audio streaming
./network-optimization.sh --audio-streaming

# Optimize for large file transfers
./network-optimization.sh --file-transfers
```

### Troubleshooting
```bash
# Reset to defaults
./reset-settings.sh

# Verify configuration
./verify-settings.sh

# Generate diagnostic report
./system-diagnostics.sh
```

## Environment Variables

```bash
# Configuration directory
export NOIZYLAB_CONFIG_DIR="$HOME/.noizylab"

# Backup directory
export NOIZYLAB_BACKUP_DIR="$HOME/.noizylab/backups"

# Log level
export NOIZYLAB_LOG_LEVEL="INFO"
```

## Compatibility

### Supported macOS Versions
- macOS 14 (Sonoma) - Fully supported
- macOS 13 (Ventura) - Fully supported
- macOS 12 (Monterey) - Supported
- macOS 11 (Big Sur) - Limited support

### Architecture
- Apple Silicon (M1/M2/M3) - Optimized
- Intel - Supported

## Security Considerations

1. **Requires admin privileges** for system changes
2. **Backs up settings** before modifications
3. **Validates inputs** to prevent misconfigurations
4. **Logs all changes** for audit trail
5. **No remote access** - all changes local

## Best Practices

1. **Test in safe mode** before applying to production
2. **Backup settings** before making changes
3. **Review logs** after configuration
4. **Document changes** in your setup notes
5. **Version control** your custom configurations

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
# Run with sudo
sudo ./configure-system.sh
```

**Settings Not Applied**
```bash
# Restart affected services
sudo killall -HUP mDNSResponder
```

**iCloud Settings Greyed Out**
```bash
# Unlock Screen Time
./icloud-settings.sh --unlock-screentime
```

## Integration

### With SystemGuardian
```bash
# Monitor system health after changes
../SystemGuardian/guardian_core.sh
```

### With Audio Processing
```bash
# Configure system, then process audio
./configure-system.sh && ../audio-processing/rr.sh process audio.wav
```

## Related Documentation

- [Scripts Overview](../README.md)
- [SystemGuardian](../../SystemGuardian/README.md)
- [System Documentation](../../docs/NOIZYLAB-SYSTEM-COMPLETE.md)
- [Network Optimization Guide](../../docs/deployment/)

## Support

For system configuration questions:
- Check system logs: `Console.app`
- Review script logs in `~/.noizylab/logs`
- Test in safe mode
- Open an issue on GitHub

---

**NOIZYLAB System Settings** | macOS Optimization for Audio Production
