#!/bin/zsh
set -e

echo "🔧 Checking Xcode Command Line Tools..."
if ! xcode-select -p &>/dev/null; then
    echo "📦 Installing Xcode Command Line Tools..."
    xcode-select --install || true
fi

echo "📜 Accepting Xcode license..."
sudo xcodebuild -license accept || true

echo "🔍 Checking for existing Homebrew installation..."
if command -v brew &>/dev/null; then
    echo "🍺 Homebrew found. Running brew doctor..."
    if brew doctor; then
        echo "✅ Homebrew healthy. Updating..."
        brew update
        brew upgrade
        brew cleanup
        echo "🎉 Homebrew updated successfully."
        brew --version
        exit 0
    else
        echo "⚠️ Homebrew appears broken. Removing..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
    fi
else
    echo "🚫 No Homebrew found. Installing fresh..."
fi

echo "⬇️ Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH depending on chip
if [[ -d /opt/homebrew/bin ]]; then
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -d /usr/local/bin ]]; then
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
fi

echo "🔁 Running brew doctor for verification..."
brew doctor || true

echo "🎉 Homebrew installation complete!"
brew --version
