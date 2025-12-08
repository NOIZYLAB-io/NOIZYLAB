# 🎯 AI Cockpit - AI Engine Aggregator

## Overview
Multi-engine AI query dashboard with side-by-side comparison and response blending.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: JavaScript, HTML/CSS
- **Deployment**: Docker, Web Server

## Project Structure
```
ai-cockpit/
├── src/              # Source code
│   ├── app.py        # Main Flask app
│   ├── templates/    # HTML templates
│   └── static/       # CSS/JS assets
├── config/           # Configuration files
├── docs/             # Documentation
├── tests/            # Test suite
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker configuration
└── README.md         # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- Docker (optional)

### Installation
```bash
pip install -r requirements.txt
```

### Development
```bash
python src/app.py
```
Access at: http://localhost:5000

### Docker Deployment
```bash
docker build -t ai-cockpit:latest .
docker run -p 5000:5000 ai-cockpit:latest
```

## Configuration
Create `config/config.json` with API keys for:
- OpenAI (ChatGPT)
- Anthropic (Claude)
- Google (Gemini)
- And more...

## Features
- ✅ Multi-engine simultaneous queries
- ✅ Side-by-side response comparison
- ✅ Response blending tool
- ✅ Export functionality (JSON, Markdown)
- ✅ Query history tracking
- ✅ Subscription management

## API Documentation
See `docs/API.md` for detailed API documentation.

## Testing
```bash
python -m pytest tests/
```

## Support
Contact: rsplowman@icloud.com

## License
MIT
