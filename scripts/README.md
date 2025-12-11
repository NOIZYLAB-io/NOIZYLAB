# Scripts

Automation scripts and utilities for the NOIZYLAB platform. This directory contains various tools for audio processing, system configuration, and mail management.

## Directory Structure

### `/audio-processing`
Audio repair, restoration, and dataset curation pipelines.

**Key Scripts:**
- `rr.sh` - Main audio repair pipeline
- Audio processing utilities
- Dataset management tools

**Usage:**
```bash
cd audio-processing
./rr.sh setup
./rr.sh process [audio-file]
```

See [audio-processing/README.md](audio-processing/README.md) for detailed documentation.

### `/mail_manager_pro`
Full-featured mail backup and management suite.

**Features:**
- Complete mail backup system
- Folder organization
- Archive management
- Search and indexing

**Quick Start:**
```bash
cd mail_manager_pro
# See docs/QUICK_START.md
```

See [mail_manager_pro/README.md](mail_manager_pro/README.md) for complete guide.

### `/system-settings`
macOS system configuration and optimization scripts.

**Includes:**
- System preferences automation
- iCloud sync configuration
- Network optimization
- Performance tuning

See [system-settings/README.md](system-settings/README.md) for details.

## General Usage

### Prerequisites
- macOS 12+ (Monterey or later)
- Bash 4.0+
- Python 3.9+ (for Python scripts)
- Homebrew (for installing dependencies)

### Making Scripts Executable
```bash
chmod +x script-name.sh
./script-name.sh
```

### Common Patterns

**Audio Processing:**
```bash
./audio-processing/rr.sh setup
./audio-processing/rr.sh process input.wav
```

**Mail Management:**
```bash
cd mail_manager_pro
python mail_backup.py --help
```

**System Settings:**
```bash
./system-settings/configure-system.sh
```

## Script Development Guidelines

### Writing New Scripts

1. **Use proper shebang**: `#!/bin/bash` or `#!/usr/bin/env python3`
2. **Add usage/help**: Include `--help` flag
3. **Error handling**: Check return codes, use `set -e`
4. **Documentation**: Add header comments
5. **Testing**: Test on clean system when possible

### Script Template (Bash)
```bash
#!/bin/bash
# Script Name: example.sh
# Description: Brief description
# Author: NOIZYLAB
# Usage: ./example.sh [options]

set -e  # Exit on error
set -u  # Exit on undefined variable

# Function to display usage
usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help     Show this help message"
    exit 1
}

# Main script logic
main() {
    # Your code here
    echo "Script running..."
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
    shift
done

# Run main function
main "$@"
```

### Script Template (Python)
```python
#!/usr/bin/env python3
"""
Script Name: example.py
Description: Brief description
Author: NOIZYLAB
"""

import sys
import argparse

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('--option', help='Option description')
    args = parser.parse_args()
    
    # Your code here
    print("Script running...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```

## Testing Scripts

### Manual Testing
```bash
# Test script syntax
bash -n script.sh

# Test with shellcheck
shellcheck script.sh

# Test Python syntax
python3 -m py_compile script.py
```

### Integration Testing
- Test with sample data in `/tmp`
- Verify outputs
- Check error conditions
- Test edge cases

## Security Considerations

1. **Never hardcode credentials** - Use environment variables
2. **Validate inputs** - Sanitize all user inputs
3. **Use absolute paths** - Avoid relative path vulnerabilities
4. **Check permissions** - Verify file/directory permissions
5. **Log securely** - Don't log sensitive information

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
chmod +x script.sh
```

**Command Not Found**
```bash
# Check PATH
echo $PATH

# Use full path
/usr/local/bin/command
```

**Python Module Not Found**
```bash
pip3 install -r requirements.txt
```

## Best Practices

1. **Document scripts** - Include comments and usage info
2. **Use version control** - Commit scripts regularly
3. **Test thoroughly** - Test on clean systems
4. **Handle errors** - Proper error handling and logging
5. **Follow conventions** - Consistent naming and style
6. **Keep it simple** - One script, one purpose
7. **Make backups** - Before running destructive operations

## Related Documentation

- [Main README](../README.md)
- [Audio Processing Guide](audio-processing/README.md)
- [Mail Manager Pro Guide](mail_manager_pro/README.md)
- [System Guardian](../SystemGuardian/README.md)
- [Contributing Guidelines](../CONTRIBUTING.md)

## Support

For script-related questions:
- Check script documentation
- Review error logs
- Open an issue on GitHub
- Contact: rsplowman@icloud.com

---

**NOIZYLAB** | Professional Music Production & Audio Engineering Platform
