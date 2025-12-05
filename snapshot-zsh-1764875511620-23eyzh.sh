# Snapshot file
# Unset all aliases to avoid conflicts with functions
unalias -a 2>/dev/null || true
# Functions
# Shell Options
setopt nohashdirs
setopt login
# Aliases
alias -- cb01='cd $CB01_KNOWLEDGE && ls -la'
alias -- cf='god cf'
alias -- code='cd $CODE_MASTER && ls -la'
alias -- damaged='find . -name "*[?<>]*" | head -20'
alias -- dash='mc96 dash'
alias -- dns='god net dns'
alias -- dragon='cd "$RED_DRAGON" && ls -la'
alias -- drives='df -h | grep -E "Volumes|disk"'
alias -- email='god email'
alias -- fbig='cd "$FISH_BIG" && ls -la'
alias -- fblue='cd "$FISH_BLUE" && ls -la'
alias -- fish='cd "$FISH_MAIN" && ls -la'
alias -- fsg='cd "$FISH_SG" && ls -la'
alias -- ga='git add -A'
alias -- gall=$'git add -A && git commit -m "ð\M-\C-_\M-\C-Z\M-\C-@ SUPER-SONIC UPDATE" && git push'
alias -- gc='git commit -m'
alias -- gl='git log --oneline -10'
alias -- gp='git push'
alias -- gs='git status'
alias -- heal='find . -type f -size 0 | head -20'
alias -- inbox='god email inbox'
alias -- mail='god email'
alias -- mc96='cd $MC96 && ls -la'
alias -- net='god net'
alias -- nl='cd $NOIZYLAB && ls -la'
alias -- noizy='god noizy'
alias -- nz='python3 ~/NOIZYLAB/email-intelligence/main.py'
alias -- rsp='cd "$RSP" && ls -la'
alias -- run-help=man
alias -- s4='cd "$SAMPLES_4TBSG" && ls -la'
alias -- s6='cd "$SAMPLES_6TB" && ls -la'
alias -- sew='cd "$SAMPLES_EW" && ls -la'
alias -- smag='cd "$SAMPLES_MAG" && ls -la'
alias -- smaster='cd "$SAMPLES_MASTER" && ls -la'
alias -- status=$'echo "ð\M-\C-_\M-\C-Z\M-\C-@ NOIZYLAB STATUS:" && du -sh $NOIZYLAB && git -C $NOIZYLAB status --short | head -10'
alias -- superaudio='find . -type f \( -name "*.wav" -o -name "*.aif*" -o -name "*.mp3" -o -name "*.ncw" \) | wc -l'
alias -- supercode='find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.sh" \) | wc -l'
alias -- superscan='find . -type f | wc -l && du -sh .'
alias -- supersonic='mc96 supersonic'
alias -- support='god email support'
alias -- t12='cd "$ARCHIVE_12TB" && ls -la'
alias -- which-command=whence
# Check for rg availability
if ! command -v rg >/dev/null 2>&1; then
  alias rg=''\''/Users/m2ultra/Library/Application Support/Claude/claude-code/2.0.53/claude'\'' --ripgrep'
fi
export PATH=/usr/bin\:/bin\:/usr/sbin\:/sbin
