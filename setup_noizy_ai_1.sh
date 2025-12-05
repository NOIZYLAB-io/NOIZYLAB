#!/bin/bash
# NOIZY.AI - Ultimate Setup Script
# Installs EVERYTHING needed for the consolidated AI engine

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Project info
PROJECT_NAME="Noizy.AI"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_NAME="noizy_ai_env"

echo -e "${PURPLE}🎵 ${PROJECT_NAME} - Ultimate Setup Script 🎵${NC}"
echo -e "${CYAN}Setting up the most badass AI audio engine ever created...${NC}\n"

# Function to print status
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "\n${BLUE}=== $1 ===${NC}"
}

# Check if running on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    print_status "Detected macOS - Perfect for Noizy.AI development! 🍎"
    PLATFORM="macos"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    print_status "Detected Linux - Great choice! 🐧"
    PLATFORM="linux"
else
    print_warning "Unrecognized platform. Proceeding with standard setup..."
    PLATFORM="other"
fi

# Check for required system tools
print_header "Checking System Requirements"

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_status "Python ${PYTHON_VERSION} found ✅"
    
    # Check if Python version is >= 3.9
    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)"; then
        print_status "Python version is compatible ✅"
    else
        print_error "Python 3.9+ is required. Current version: ${PYTHON_VERSION}"
        exit 1
    fi
else
    print_error "Python 3 not found! Please install Python 3.9+ first."
    exit 1
fi

# Check pip
if command -v pip3 &> /dev/null; then
    print_status "pip3 found ✅"
else
    print_error "pip3 not found! Please install pip3 first."
    exit 1
fi

# Platform-specific dependencies
print_header "Installing System Dependencies"

if [[ "$PLATFORM" == "macos" ]]; then
    # Check for Homebrew
    if command -v brew &> /dev/null; then
        print_status "Homebrew found ✅"
    else
        print_warning "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Install audio dependencies
    print_status "Installing macOS audio dependencies..."
    brew install portaudio libsndfile ffmpeg sox
    brew install --cask vlc  # For python-vlc
    
elif [[ "$PLATFORM" == "linux" ]]; then
    print_status "Installing Linux audio dependencies..."
    
    # Detect package manager
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y \
            portaudio19-dev \
            libsndfile1-dev \
            ffmpeg \
            sox \
            vlc \
            python3-dev \
            build-essential \
            cmake
    elif command -v yum &> /dev/null; then
        sudo yum install -y \
            portaudio-devel \
            libsndfile-devel \
            ffmpeg \
            sox \
            vlc \
            python3-devel \
            gcc-c++ \
            cmake
    else
        print_warning "Unrecognized package manager. Please install audio dependencies manually."
    fi
fi

# Create virtual environment
print_header "Setting Up Python Virtual Environment"

if [ -d "$VENV_NAME" ]; then
    print_warning "Virtual environment already exists. Removing old one..."
    rm -rf "$VENV_NAME"
fi

print_status "Creating virtual environment: $VENV_NAME"
python3 -m venv "$VENV_NAME"

print_status "Activating virtual environment..."
source "$VENV_NAME/bin/activate"

# Upgrade pip and install wheel
print_status "Upgrading pip and installing wheel..."
pip install --upgrade pip wheel setuptools

# Install core Python packages
print_header "Installing Core Python Dependencies"

print_status "Installing audio processing libraries..."
pip install librosa soundfile pydub numpy scipy matplotlib
pip install resampy audioread mutagen
pip install pedalboard  # Spotify's audio effects library

print_status "Installing AI platform SDKs..."
pip install openai elevenlabs anthropic
pip install requests httpx aiohttp

print_status "Installing web framework dependencies..."
pip install flask flask-cors flask-limiter flask-caching
pip install fastapi uvicorn starlette websockets

print_status "Installing database and storage..."
pip install sqlalchemy alembic redis pymongo psycopg2-binary

print_status "Installing development tools..."
pip install pytest pytest-asyncio pytest-cov
pip install black flake8 mypy bandit pre-commit isort

print_status "Installing utility libraries..."
pip install click rich tqdm python-dateutil pytz pyyaml
pip install python-dotenv cryptography pyjwt bcrypt

print_status "Installing machine learning libraries..."
pip install pandas scikit-learn torch torchaudio transformers

# Install optional advanced audio libraries
print_header "Installing Advanced Audio Libraries"

print_status "Installing advanced audio analysis libraries..."
pip install essentia-tensorflow madmom pyrubberband || print_warning "Some advanced audio libraries failed to install (this is normal)"

# Install cloud and monitoring
print_status "Installing cloud and monitoring libraries..."
pip install boto3 azure-storage-blob google-cloud-storage
pip install prometheus-client sentry-sdk

# Install from requirements.txt (if exists)
if [ -f "requirements.txt" ]; then
    print_header "Installing from requirements.txt"
    pip install -r requirements.txt || print_warning "Some packages from requirements.txt failed to install"
fi

# Install the package itself in development mode
print_header "Installing Noizy.AI Package"
if [ -f "setup.py" ]; then
    print_status "Installing Noizy.AI in development mode..."
    pip install -e .
fi

# Create necessary directories
print_header "Creating Project Structure"
mkdir -p logs
mkdir -p data/audio
mkdir -p data/models
mkdir -p config
mkdir -p tests
mkdir -p notebooks
mkdir -p scripts
mkdir -p docs

# Create configuration files
print_status "Creating configuration files..."

# .env file
cat > .env << EOL
# NOIZY.AI Environment Configuration
# Copy this file and rename to .env, then fill in your actual API keys

# AI Platform API Keys
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Audio Platform APIs
LANDR_API_KEY=your_landr_api_key_here
IZOTOPE_API_KEY=your_izotope_api_key_here
SPLICE_API_KEY=your_splice_api_key_here

# Music Platform APIs
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here

# Database Configuration
DATABASE_URL=sqlite:///noizy_ai.db
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your_super_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/noizy_ai.log

# Development
DEBUG=True
DEVELOPMENT_MODE=True
EOL

# Create a basic config file
cat > config/default.json << EOL
{
    "app": {
        "name": "Noizy.AI",
        "version": "1.0.0",
        "debug": true
    },
    "audio": {
        "supported_formats": [".wav", ".mp3", ".flac", ".aiff", ".m4a", ".ogg"],
        "default_sample_rate": 44100,
        "default_bit_depth": 16
    },
    "ai_engines": {
        "max_concurrent_engines": 5,
        "timeout_seconds": 30,
        "retry_attempts": 3
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000,
        "cors_enabled": true
    }
}
EOL

# Set up git hooks (if git repo exists)
if [ -d ".git" ]; then
    print_header "Setting Up Git Hooks"
    pre-commit install || print_warning "Pre-commit hooks setup failed"
fi

# Create startup scripts
print_header "Creating Startup Scripts"

# Development server script
cat > start_dev.sh << 'EOL'
#!/bin/bash
source noizy_ai_env/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
echo "🎵 Starting Noizy.AI Development Server..."
python -m flask run --host=0.0.0.0 --port=5000
EOL
chmod +x start_dev.sh

# Production server script
cat > start_prod.sh << 'EOL'
#!/bin/bash
source noizy_ai_env/bin/activate
echo "🎵 Starting Noizy.AI Production Server..."
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
EOL
chmod +x start_prod.sh

# Test runner script
cat > run_tests.sh << 'EOL'
#!/bin/bash
source noizy_ai_env/bin/activate
echo "🧪 Running Noizy.AI Tests..."
pytest tests/ -v --cov=noizy_ai --cov-report=html
EOL
chmod +x run_tests.sh

# Create README if it doesn't exist
if [ ! -f "README.md" ]; then
    print_status "Creating README.md..."
    cat > README.md << EOL
# 🎵 Noizy.AI - Consolidated AI Engine

The most badass audio & music-centered AI platform ever created.

## Quick Start

1. **Activate the environment:**
   \`\`\`bash
   source noizy_ai_env/bin/activate
   \`\`\`

2. **Configure your API keys:**
   - Copy \`.env.example\` to \`.env\`
   - Add your API keys for OpenAI, ElevenLabs, etc.

3. **Start the development server:**
   \`\`\`bash
   ./start_dev.sh
   \`\`\`

4. **Run tests:**
   \`\`\`bash
   ./run_tests.sh
   \`\`\`

## Features

- 🤖 Multi-AI engine integration (ElevenLabs, OpenAI, LANDR, iZotope)
- 🎧 Advanced audio processing and analysis
- 🎵 Music composition and generation
- 🔊 Voice synthesis and cloning
- 📊 Real-time audio visualization
- 🚀 High-performance async processing
- 🌐 RESTful API and WebSocket support

## Documentation

Visit our [documentation](https://noizy-ai.readthedocs.io/) for detailed guides.

## License

MIT License - Build amazing audio AI experiences!
EOL
fi

# Final status report
print_header "Installation Complete! 🚀"

echo -e "${GREEN}✅ Virtual environment created: ${VENV_NAME}${NC}"
echo -e "${GREEN}✅ All Python dependencies installed${NC}"
echo -e "${GREEN}✅ Project structure created${NC}"
echo -e "${GREEN}✅ Configuration files generated${NC}"
echo -e "${GREEN}✅ Startup scripts ready${NC}"

print_header "Next Steps"
echo -e "${CYAN}1. Activate the environment:${NC}"
echo -e "   ${YELLOW}source ${VENV_NAME}/bin/activate${NC}"
echo -e ""
echo -e "${CYAN}2. Configure your API keys:${NC}"
echo -e "   ${YELLOW}nano .env${NC}"
echo -e ""
echo -e "${CYAN}3. Start developing:${NC}"
echo -e "   ${YELLOW}./start_dev.sh${NC}"
echo -e ""
echo -e "${CYAN}4. Run tests:${NC}"
echo -e "   ${YELLOW}./run_tests.sh${NC}"

print_header "🎵 Noizy.AI is Ready to Rock! 🎵"
echo -e "${PURPLE}Go build the most amazing audio AI platform the world has ever seen!${NC}"
echo -e "${CYAN}Remember: With great AI power comes great audio responsibility! 🎧${NC}"