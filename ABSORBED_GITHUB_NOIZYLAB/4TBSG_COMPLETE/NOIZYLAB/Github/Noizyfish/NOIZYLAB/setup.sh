#!/bin/bash

# AI Aggregator Setup Script
# This script sets up the AI Aggregator application

set -e

echo "🚀 AI Aggregator Setup Script"
echo "=============================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.8+
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Error: Python 3.8 or higher is required"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo ""
echo "Creating directories..."
mkdir -p static/css static/js templates
echo "✅ Directories created"

# Create config.json if it doesn't exist
if [ ! -f "config.json" ]; then
    echo ""
    echo "Creating config.json..."
    cat > config.json << 'EOF'
{
  "openai": {
    "api_key": "",
    "enabled": true,
    "display_name": "ChatGPT (GPT-4)"
  },
  "anthropic": {
    "api_key": "",
    "enabled": true,
    "display_name": "Claude (Anthropic)"
  },
  "google": {
    "api_key": "",
    "enabled": true,
    "display_name": "Gemini (Google)"
  },
  "github_copilot": {
    "api_key": "",
    "enabled": false,
    "display_name": "GitHub Copilot Pro"
  },
  "windsurf": {
    "api_key": "",
    "enabled": false,
    "display_name": "Windsurf AI"
  },
  "vscode_insiders": {
    "api_key": "",
    "enabled": false,
    "display_name": "VS Code Insiders AI"
  },
  "cursor": {
    "api_key": "",
    "enabled": false,
    "display_name": "Cursor AI (Auto)"
  },
  "mistral": {
    "api_key": "",
    "enabled": false,
    "display_name": "Mistral AI"
  },
  "perplexity": {
    "api_key": "",
    "enabled": false,
    "display_name": "Perplexity"
  },
  "cohere": {
    "api_key": "",
    "enabled": false,
    "display_name": "Cohere"
  },
  "xai": {
    "api_key": "",
    "enabled": false,
    "display_name": "Grok (xAI)"
  },
  "openrouter": {
    "api_key": "",
    "enabled": false,
    "display_name": "OpenRouter (Multi-Model)"
  }
}
EOF
    echo "✅ config.json created"
    echo "⚠️  Remember to add your API keys in config.json or use the Settings UI"
else
    echo "✅ config.json already exists"
fi

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo ""
    echo "Creating .gitignore..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Config and data
config.json
*.json
!package.json
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
EOF
    echo "✅ .gitignore created"
fi

echo ""
echo "=============================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Add your API keys to config.json or use the Settings UI"
echo "2. Activate virtual environment: source venv/bin/activate"
echo "3. Run the app: python app.py"
echo "4. Open browser: http://localhost:5000"
echo ""
echo "For more information, see README.md"

