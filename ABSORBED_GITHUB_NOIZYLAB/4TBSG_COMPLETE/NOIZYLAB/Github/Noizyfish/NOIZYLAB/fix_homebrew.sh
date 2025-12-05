#!/bin/zsh
set -e

echo "🔍 Checking for existing Homebrew installation..."

if command -v brew &>/dev/null; then
    echo "🍺 Homebrew is installed. Running brew doctor to check health..."
    if brew doctor; then
        echo "✅ Homebrew seems healthy. Updating..."
        brew update
        brew upgrade
        brew cleanup
        echo "🎉 Homebrew updated successfully."
        exit 0
    else
        echo "⚠️ Homebrew appears broken. Removing it..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
    fi
else
    echo "🚫 No working Homebrew found. Proceeding with fresh install..."
fi

echo "⬇️ Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
if [[ -d /opt/homebrew/bin ]]; then
    echo "export PATH=\"/opt/homebrew/bin:\$PATH\"" >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -d /usr/local/bin ]]; then
    echo "export PATH=\"/usr/local/bin:\$PATH\"" >> ~/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
fi

echo "🔁 Running brew doctor for verification..."
brew doctor || true

echo "🎉 Homebrew setup complete!"
brew --version
