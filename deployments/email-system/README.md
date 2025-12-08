# 📧 Email System - Email Management & Automation

## Overview
Comprehensive email management, automation, and routing system.

## Tech Stack
- **Language**: Python, Shell scripts
- **Services**: SMTP, IMAP
- **Deployment**: Server/Cron

## Project Structure
```
email-system/
├── src/              # Source code
│   ├── automation/   # Email automation scripts
│   ├── routing/      # Email routing logic
│   └── testing/      # Email testing tools
├── config/           # Configuration files
│   ├── routing.json  # Routing rules
│   └── templates.json # Email templates
├── docs/             # Documentation
├── tests/            # Test suite
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- SMTP server access
- Email accounts configured

### Installation
```bash
pip install -r requirements.txt
python setup.py install
```

### Configuration
1. Copy `config/email_master_config.json.example` to `config/email_master_config.json`
2. Configure your email accounts
3. Set up routing rules

### Running
```bash
# Start email automation
python src/email_automation.py

# Test email setup
python src/test_email.py
```

## Features
- ✅ Multi-account email management
- ✅ Automated email routing
- ✅ Email templates
- ✅ Queue system
- ✅ Testing dashboard
- ✅ iCloud, Gmail, domain email support

## Email Accounts Supported
- rsplowman@icloud.com (Apple)
- rsplowman@gmail.com (Gmail)
- rp@fishmusicinc.com (Domain)
- rsp@noizylab.ca (Domain)
- And more...

## Documentation
- `docs/SETUP.md` - Setup guide
- `docs/ROUTING.md` - Routing configuration
- `docs/TEMPLATES.md` - Email templates

## Testing
```bash
python -m pytest tests/
```

## Support
Contact: rsplowman@icloud.com

## License
MIT
