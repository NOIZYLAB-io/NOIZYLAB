#!/bin/zsh
# fast_fix.sh
# Turbo cleanup + performance tuning for macOS

echo "🚀 Starting Fast Fix…"

### 1. Update Xcode tools & accept license
if ! xcode-select -p >/dev/null 2>&1; then
  echo "📦 Installing Xcode Command Line Tools..."
  xcode-select --install
fi
sudo xcodebuild -license accept 2>/dev/null

### 2. Homebrew health
if command -v brew >/dev/null 2>&1; then
  echo "🍺 Cleaning & optimizing Homebrew…"
  brew update
  brew upgrade
  brew cleanup -s
  brew autoremove
else
  echo "⚠️ Homebrew not installed — skipping."
fi

### 3. Clear caches & logs
echo "🧹 Clearing caches & logs…"
rm -rf ~/Library/Caches/* ~/Library/Logs/* 2>/dev/null
sudo rm -rf /Library/Caches/* /System/Library/Caches/* 2>/dev/null

### 4. Handle unexpected headers/libs
for path in /usr/local/include/unexpected_backup /usr/local/lib/unexpected_backup; do
  if [ -d "$path" ]; then
    echo "📦 Moving unexpected items from $path …"
    sudo mv "$path" ~/Homebrew_Backups_$(date +%Y%m%d%H%M%S)
  fi
done

### 5. Clean shell configs (remove direnv hooks etc.)
echo "🧩 Cleaning shell configs…"
sed -i.bak '/direnv/d' ~/.zshrc ~/.zprofile 2>/dev/null

### 6. Rebuild zsh completions
rm -f ~/.zcompdump
autoload -Uz compinit && compinit

### 7. Run Apple’s maintenance scripts
echo "🛠 Running periodic maintenance…"
sudo periodic daily weekly monthly

### 8. Free RAM cache
echo "💾 Flushing inactive memory…"
sudo purge

### 9. Rebuild Spotlight index (optional heavy step)
echo "🔍 Rebuilding Spotlight index…"
sudo mdutil -E /

### 10. Verify disk & enable TRIM (for SSD)
echo "💽 Verifying disk volume…"
diskutil verifyVolume /
sudo trimforce enable

### 11. Final brew doctor
if command -v brew >/dev/null 2>&1; then
  echo "🔎 Final brew doctor check:"
  brew doctor
fi

echo "✅ Fast Fix complete. macOS should feel cleaner & quicker."
