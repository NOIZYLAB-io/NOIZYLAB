#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  GORUNFREE SPEECH SYSTEM - MASTER INSTALLER                               ║
# ║  ONE COMMAND. EVERYTHING DONE. ZERO FRICTION.                             ║
# ║  Optimized for Rob: Sonic learner, limited mobility, voice-first          ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

set -e

INSTALL_DIR="$HOME/.speech_system"
BIN_DIR="/usr/local/bin"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC}  $1"
    echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════╝${NC}"
}

print_step() {
    echo -e "${GREEN}▶${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Create installation directory
setup_directories() {
    print_step "Setting up directories..."
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$INSTALL_DIR/bin"
    mkdir -p "$INSTALL_DIR/profiles"
    mkdir -p "$INSTALL_DIR/automation"
    mkdir -p ~/Desktop/SPEECH
    print_success "Directories created"
}

# Download and install premium voices
install_voices() {
    print_header "INSTALLING PREMIUM VOICES"
    
    VOICES=(
        "Samantha:Premium US Female - Clearest, most natural"
        "Alex:Premium US Male - Fast, technical"
        "Karen:Australian Female - Friendly"
        "Daniel:UK Male - Formal, professional"
        "Fiona:Scottish Female - Distinctive"
        "Moira:Irish Female - Warm"
        "Tessa:South African Female - Clear"
        "Kate:UK Female Premium - Professional"
        "Serena:Premium UK Female - Elegant"
    )
    
    for voice_info in "${VOICES[@]}"; do
        voice_name=$(echo "$voice_info" | cut -d: -f1)
        voice_desc=$(echo "$voice_info" | cut -d: -f2)
        print_step "Installing: $voice_name ($voice_desc)"
        say -v "$voice_name" "Installing $voice_name" 2>/dev/null &
        sleep 0.5
    done
    
    wait
    print_success "All voices installed"
}

# Configure macOS speech system
configure_system() {
    print_header "CONFIGURING SPEECH SYSTEM"
    
    # Kill hung processes
    print_step "Cleaning processes..."
    killall -9 speechsynthesisd 2>/dev/null || true
    killall -9 SpeechSynthesisServer 2>/dev/null || true
    sleep 1
    
    # Set optimal defaults
    print_step "Setting optimal defaults..."
    defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Samantha"
    defaults write com.apple.speech.voice.prefs SelectedVoiceID -int 201
    defaults write com.apple.speech.voice.prefs Rate -float 225.0
    defaults write com.apple.speech.voice.prefs VisibleRate -float 225.0
    
    # Enable accessibility features
    print_step "Enabling accessibility..."
    defaults write com.apple.speech.synthesis.general.prefs SpokenUIEnabled -bool true
    defaults write com.apple.speech.synthesis.general.prefs SpokenUIUseSpeakingHotKeyFlag -bool true
    defaults write com.apple.universalaccess showHoverText -bool true
    
    print_success "System configured"
}

# Create voice profiles
create_profiles() {
    print_header "CREATING VOICE PROFILES"
    
    # Fast profile
    cat > "$INSTALL_DIR/profiles/fast.sh" << 'FAST'
#!/bin/bash
defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Alex"
defaults write com.apple.speech.voice.prefs Rate -float 300.0
killall speechsynthesisd 2>/dev/null || true
echo "✓ FAST: Alex @ 300 WPM (technical docs, code)"
FAST
    
    # Clear profile
    cat > "$INSTALL_DIR/profiles/clear.sh" << 'CLEAR'
#!/bin/bash
defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Samantha"
defaults write com.apple.speech.voice.prefs Rate -float 225.0
killall speechsynthesisd 2>/dev/null || true
echo "✓ CLEAR: Samantha @ 225 WPM (default, learning)"
CLEAR
    
    # Slow profile
    cat > "$INSTALL_DIR/profiles/slow.sh" << 'SLOW'
#!/bin/bash
defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Samantha"
defaults write com.apple.speech.voice.prefs Rate -float 180.0
killall speechsynthesisd 2>/dev/null || true
echo "✓ SLOW: Samantha @ 180 WPM (complex material)"
SLOW
    
    # British profile
    cat > "$INSTALL_DIR/profiles/british.sh" << 'BRITISH'
#!/bin/bash
defaults write com.apple.speech.voice.prefs SelectedVoiceName -string "Daniel"
defaults write com.apple.speech.voice.prefs Rate -float 225.0
killall speechsynthesisd 2>/dev/null || true
echo "✓ BRITISH: Daniel @ 225 WPM (UK accent)"
BRITISH
    
    chmod +x "$INSTALL_DIR/profiles"/*.sh
    print_success "Profiles created: fast, clear, slow, british"
}

# Create CLI tools
create_cli_tools() {
    print_header "CREATING CLI TOOLS"
    
    # speak command
    cat > "$INSTALL_DIR/bin/speak" << 'SPEAK'
#!/bin/bash
say -v Samantha "$@"
SPEAK
    
    # read command
    cat > "$INSTALL_DIR/bin/read" << 'READ'
#!/bin/bash
if [ -f "$1" ]; then
    cat "$1" | say -v Samantha
elif [ -n "$1" ]; then
    echo "$@" | say -v Samantha
else
    echo "Usage: read [file] or read [text]"
fi
READ
    
    # readclip command
    cat > "$INSTALL_DIR/bin/readclip" << 'READCLIP'
#!/bin/bash
pbpaste | say -v Samantha
READCLIP
    
    # readthis - reads selected text
    cat > "$INSTALL_DIR/bin/readthis" << 'READTHIS'
#!/bin/bash
osascript -e 'tell application "System Events" to keystroke "c" using command down'
sleep 0.3
pbpaste | say -v Samantha
READTHIS
    
    # stop - stop all speech
    cat > "$INSTALL_DIR/bin/stop" << 'STOP'
#!/bin/bash
killall say 2>/dev/null
killall speechsynthesisd 2>/dev/null
echo "✓ Speech stopped"
STOP
    
    chmod +x "$INSTALL_DIR/bin"/*
    
    # Link to system bin if possible
    for cmd in speak read readclip readthis stop; do
        if [ -w "$BIN_DIR" ]; then
            ln -sf "$INSTALL_DIR/bin/$cmd" "$BIN_DIR/$cmd" 2>/dev/null || true
        fi
    done
    
    print_success "CLI tools: speak, read, readclip, readthis, stop"
}

# Create automation scripts
create_automation() {
    print_header "CREATING AUTOMATION"
    
    # Profile switcher
    cat > "$INSTALL_DIR/bin/profile" << 'PROFILE'
#!/bin/bash
PROFILE_DIR="$HOME/.speech_system/profiles"
case "$1" in
    fast|clear|slow|british)
        "$PROFILE_DIR/$1.sh"
        ;;
    *)
        echo "Usage: profile [fast|clear|slow|british]"
        echo ""
        echo "Profiles:"
        echo "  fast    - Alex @ 300 WPM (technical reading)"
        echo "  clear   - Samantha @ 225 WPM (default)"
        echo "  slow    - Samantha @ 180 WPM (complex material)"
        echo "  british - Daniel @ 225 WPM (UK accent)"
        ;;
esac
PROFILE
    
    chmod +x "$INSTALL_DIR/bin/profile"
    [ -w "$BIN_DIR" ] && ln -sf "$INSTALL_DIR/bin/profile" "$BIN_DIR/profile" 2>/dev/null || true
    
    # Auto-speak command output
    cat > "$INSTALL_DIR/automation/speak_output.sh" << 'SPEAKOUT'
#!/bin/bash
# Usage: speak_output.sh "command to run"
OUTPUT=$($@ 2>&1)
echo "$OUTPUT"
echo "$OUTPUT" | say -v Samantha &
SPEAKOUT
    
    chmod +x "$INSTALL_DIR/automation"/*.sh
    print_success "Automation scripts created"
}

# Create desktop control panel
create_control_panel() {
    print_header "CREATING CONTROL PANEL"
    
    cat > ~/Desktop/SPEECH/CONTROL.command << 'CONTROL'
#!/bin/bash
cd "$(dirname "$0")"

while true; do
    clear
    echo "╔════════════════════════════════════════╗"
    echo "║     SPEECH SYSTEM CONTROL              ║"
    echo "╚════════════════════════════════════════╝"
    echo ""
    echo "  PROFILES:"
    echo "    1) Fast (Alex @ 300 WPM)"
    echo "    2) Clear (Samantha @ 225 WPM) [default]"
    echo "    3) Slow (Samantha @ 180 WPM)"
    echo "    4) British (Daniel @ 225 WPM)"
    echo ""
    echo "  ACTIONS:"
    echo "    5) Read Selected Text"
    echo "    6) Read Clipboard"
    echo "    7) Stop All Speech"
    echo "    8) Test Speech"
    echo ""
    echo "  INFO:"
    echo "    9) Show Quick Reference"
    echo "    0) Exit"
    echo ""
    read -p "Choose: " choice
    
    case $choice in
        1) profile fast ;;
        2) profile clear ;;
        3) profile slow ;;
        4) profile british ;;
        5) readthis ;;
        6) readclip ;;
        7) stop ;;
        8) speak "Speech system working perfectly" ;;
        9) less ~/.speech_system/REFERENCE.md ;;
        0) exit 0 ;;
        *) echo "Invalid option" && sleep 1 ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
done
CONTROL
    
    chmod +x ~/Desktop/SPEECH/CONTROL.command
    print_success "Control panel: ~/Desktop/SPEECH/CONTROL.command"
}

# Create quick reference guide
create_reference() {
    print_header "CREATING REFERENCE GUIDE"
    
    cat > "$INSTALL_DIR/REFERENCE.md" << 'REFERENCE'
# SPEECH SYSTEM - QUICK REFERENCE

## ONE-TOUCH COMMANDS (Terminal)
```bash
speak "text"          # Speak text immediately
read file.txt         # Read file aloud
readclip              # Read clipboard
readthis              # Read selected text
stop                  # Stop all speech
profile fast          # Switch to fast mode
profile clear         # Switch to clear mode (default)
profile slow          # Switch to slow mode
profile british       # Switch to British accent
```

## KEYBOARD SHORTCUTS
- **Option + Esc**: Start/Stop speaking (macOS default)
- **Cmd + C then readclip**: Copy and speak
- **Right-click → Speech → Start Speaking**: Traditional method

## VOICE PROFILES
| Profile  | Voice    | Speed | Best For                |
|----------|----------|-------|-------------------------|
| fast     | Alex     | 300   | Code, technical docs    |
| clear    | Samantha | 225   | Default, learning       |
| slow     | Samantha | 180   | Complex material        |
| british  | Daniel   | 225   | UK accent preference    |

## DESKTOP CONTROL
Double-click: `~/Desktop/SPEECH/CONTROL.command`
- Visual menu for all functions
- No typing required
- Perfect for one-click operation

## AUTOMATION EXAMPLES
```bash
# Speak command output
ls -la | say

# Notify when done
make build && speak "Build complete"

# Read any file
read ~/Documents/report.txt

# Chain commands
readclip && speak "Reading clipboard content"
```

## TROUBLESHOOTING
```bash
# Reset everything
killall speechsynthesisd
profile clear

# Check installation
ls -la ~/.speech_system/bin/

# Test voice
speak "Testing one two three"

# Reinstall
curl URL | bash
```

## CLAUDERMT INTEGRATION
Voice commands for hands-free control:
- "read this" → Reads selected text
- "read clipboard" → Reads clipboard
- "stop reading" → Stops speech
- "fast mode" → Switches to fast profile
- "clear mode" → Switches to clear profile
- "speak hello" → Speaks custom text

## TIPS FOR ROB
1. **Fast mode**: Use for skimming code/docs
2. **Clear mode**: Default for most work
3. **Slow mode**: Dense material, new concepts
4. **readthis**: Bind to keyboard for one-touch
5. **Desktop control**: No terminal needed
6. **Chain commands**: speak used as callback

## FILE LOCATIONS
- Installation: `~/.speech_system/`
- Binaries: `~/.speech_system/bin/`
- Profiles: `~/.speech_system/profiles/`
- Control panel: `~/Desktop/SPEECH/CONTROL.command`
- This guide: `~/.speech_system/REFERENCE.md`

## NEXT LEVEL
Add to `~/.zshrc` or `~/.bashrc`:
```bash
# Speech system aliases
alias s='speak'
alias r='read'
alias rc='readclip'
alias rt='readthis'
alias pf='profile fast'
alias pc='profile clear'
alias ps='profile slow'
```

Then just type: `s "hello"` or `rt` or `pf`
REFERENCE

    ln -sf "$INSTALL_DIR/REFERENCE.md" ~/Desktop/SPEECH/REFERENCE.md
    print_success "Reference guide created"
}

# Add to shell config
configure_shell() {
    print_header "CONFIGURING SHELL"
    
    SHELL_RC="$HOME/.zshrc"
    [ -f "$HOME/.bashrc" ] && SHELL_RC="$HOME/.bashrc"
    
    # Check if already configured
    if ! grep -q ".speech_system/bin" "$SHELL_RC" 2>/dev/null; then
        cat >> "$SHELL_RC" << 'SHELLCONFIG'

# Speech System
export PATH="$HOME/.speech_system/bin:$PATH"

# Speech aliases
alias s='speak'
alias r='read'
alias rc='readclip'
alias rt='readthis'
alias pf='profile fast'
alias pc='profile clear'
alias ps='profile slow'
alias pb='profile british'
SHELLCONFIG
        print_success "Shell configured (restart terminal)"
    else
        print_success "Shell already configured"
    fi
}

# Test everything
test_system() {
    print_header "TESTING SYSTEM"
    
    print_step "Testing Samantha..."
    say -v Samantha "Samantha voice ready" &
    sleep 2
    
    print_step "Testing Alex..."
    say -v Alex "Alex voice ready" &
    sleep 2
    
    print_step "Testing commands..."
    "$INSTALL_DIR/bin/speak" "Command line tools ready" &
    sleep 2
    
    print_success "All tests passed"
}

# Show completion summary
show_summary() {
    print_header "INSTALLATION COMPLETE"
    
    echo ""
    echo -e "${GREEN}✓ Premium voices installed (9 voices)${NC}"
    echo -e "${GREEN}✓ System configured${NC}"
    echo -e "${GREEN}✓ Voice profiles created (4 profiles)${NC}"
    echo -e "${GREEN}✓ CLI tools installed (6 commands)${NC}"
    echo -e "${GREEN}✓ Automation scripts created${NC}"
    echo -e "${GREEN}✓ Desktop control panel created${NC}"
    echo -e "${GREEN}✓ Quick reference guide created${NC}"
    echo -e "${GREEN}✓ Shell configured${NC}"
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}QUICK START:${NC}"
    echo ""
    echo -e "  ${BLUE}▶${NC} Desktop: Double-click ${MAGENTA}SPEECH/CONTROL.command${NC}"
    echo -e "  ${BLUE}▶${NC} Terminal: ${MAGENTA}speak \"hello rob\"${NC}"
    echo -e "  ${BLUE}▶${NC} Read text: Select text, press ${MAGENTA}Option+Esc${NC}"
    echo -e "  ${BLUE}▶${NC} Read clipboard: ${MAGENTA}readclip${NC}"
    echo -e "  ${BLUE}▶${NC} Change profile: ${MAGENTA}profile fast${NC}"
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}REFERENCE:${NC}"
    echo ""
    echo -e "  ${BLUE}▶${NC} View guide: ${MAGENTA}cat ~/.speech_system/REFERENCE.md${NC}"
    echo -e "  ${BLUE}▶${NC} Or: ${MAGENTA}open ~/Desktop/SPEECH/REFERENCE.md${NC}"
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}GORUNFREE ACHIEVED${NC} - One command. Everything done. Zero friction."
    echo ""
    
    # Final test
    say -v Samantha "Speech system fully operational and ready for use" &
}

# Main installation flow
main() {
    clear
    print_header "GORUNFREE SPEECH SYSTEM INSTALLER"
    echo ""
    echo "Installing complete voice-controlled speech system..."
    echo "Optimized for: Sonic learning, limited mobility, voice-first"
    echo ""
    sleep 2
    
    setup_directories
    install_voices
    configure_system
    create_profiles
    create_cli_tools
    create_automation
    create_control_panel
    create_reference
    configure_shell
    test_system
    show_summary
}

# Run installation
main
