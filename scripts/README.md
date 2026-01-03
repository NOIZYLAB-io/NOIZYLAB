# Scripts

Utility scripts for NOIZYLAB operations, maintenance, and deployment.

## Core Scripts

### Operational Scripts

- **`autorun.sh`** - Automated startup and initialization
- **`supersonic.sh`** - Fast system checks and health monitoring
- **`ultimate.sh`** - Comprehensive system operations
- **`ultimate.ps1`** - Windows PowerShell version of ultimate operations

### Setup & Maintenance

- **`GORUNFREE-DNS-FIX.sh`** - DNS configuration fixes
- **`deep_system_scan.sh`** - Comprehensive system scanning
- **`import_all_projects.sh`** - Batch import projects
- **`mass_import.sh`** - Mass import operations
- **`pull_all_downloads_final.sh`** - Download synchronization

### System Management

- **`backup.sh`** - System backup operations
- **`rollback.sh`** - System rollback functionality
- **`setup_aliases.sh`** - Command alias configuration
- **`switch_finalize.sh`** - Finalize system switches

### Performance & Health

- **`heal_optimize_run.sh`** - System healing and optimization
- **`health_alerts.sh`** - Health monitoring and alerts
- **`performance_tuner.sh`** - Performance optimization
- **`upgrade_macos.sh`** - macOS upgrade utilities
- **`reset_system_settings.sh`** - Reset system configurations

### Voice & AI

- **`voice_pipeline.py`** - Voice processing pipeline

### Quick Commands

- **`QUICK_COMMANDS.sh`** - Quick command reference and shortcuts

## Usage

Most scripts support `--help` or `-h` flags for usage information:

```bash
./scripts/script_name.sh --help
```

## Environment Variables

Scripts may require environment variables from `.env`:
- `PRIMARY_HOST` - Primary host for operations
- `BACKUP_HOST` - Backup host configuration
- `PROJECTS_PATH` - Path to projects directory

## Requirements

- Bash 4.0+ or Zsh
- Python 3.12+ (for Python scripts)
- Standard Unix utilities (curl, ssh, etc.)

## Safety

- Most scripts include dry-run modes
- Backups are created before destructive operations
- Check script contents before running on production systems
