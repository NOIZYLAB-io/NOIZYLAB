#!/usr/bin/env bash
set -euo pipefail

# Configuration
LOGDIR="$HOME/noizy_tracer"
INV_LOG="$LOGDIR/say_invocations.log"
DIAG_LOG="$LOGDIR/diagnostics.log"
WRAPPER_DIR="/usr/local/bin"
WRAPPER_LINK="${WRAPPER_DIR}/say"
REAL_BACKUP="${WRAPPER_DIR}/say.real"
AGENT_LABEL="com.noizy.tracer"
AGENT_PLIST="$HOME/Library/LaunchAgents/${AGENT_LABEL}.plist"
START_INTERVAL=8

mkdir -p "$LOGDIR"

timestamp(){ date -u +"%Y-%m-%dT%H:%M:%SZ"; }

echo "$(timestamp) tracer start" >> "$DIAG_LOG"

# Install wrapper to capture caller PID, parent chain, environment, and launchctl info
sudo mkdir -p "$WRAPPER_DIR" 2>/dev/null || true

if [ -f "$REAL_BACKUP" ]; then
  echo "$(timestamp) wrapper real already present" >> "$DIAG_LOG"
else
  if [ -x "/usr/bin/say" ]; then
    sudo cp -a /usr/bin/say "$REAL_BACKUP" 2>/dev/null || true
    sudo chmod 755 "$REAL_BACKUP" 2>/dev/null || true
  fi
fi

sudo tee "$WRAPPER_LINK" > /dev/null <<'EOF'
#!/usr/bin/env bash
LOG="$HOME/noizy_tracer/say_invocations.log"
DIAG="$HOME/noizy_tracer/diag_each.log"
T="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
CALLER_PID=${PPID:-0}
# collect parent chain
pchain=""
pid=$CALLER_PID
while [ "$pid" -gt 1 ]; do
  comm=$(ps -p "$pid" -o comm= 2>/dev/null | tr -d '\n' || echo "unknown")
  pchain="${pchain}${pid}:${comm}|"
  pid=$(ps -p "$pid" -o ppid= 2>/dev/null | tr -d ' ' || echo 1)
  if [ -z "$pid" ]; then pid=1; fi
done
# capture launchctl list for user and process info
LC=$(launchctl print gui/$(id -u) 2>/dev/null | head -n 30 | tr '\n' ' ' || echo "no-launchctl-info")
echo "$T SAY invoked by PID:$CALLER_PID PCHAIN:$pchain USER:$USER ARGS:$* ENV:$(env | tr '\n' ' ') LAUNCHCTL:$LC" >> "$LOG"
echo "$T SAY invoked by PID:$CALLER_PID PCHAIN:$pchain USER:$USER ARGS:$* ENV:$(env | tr '\n' ' ') LAUNCHCTL:$LC" >> "$DIAG"
if [ -x "/usr/local/bin/say.real" ]; then
  exec /usr/local/bin/say.real "$@"
elif [ -x "/usr/bin/say" ]; then
  exec /usr/bin/say "$@"
else
  exit 0
fi
EOF
sudo chmod 755 "$WRAPPER_LINK"

# Create LaunchAgent plist to periodically kill speech processes
cat > "$AGENT_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>${AGENT_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>-lc</string>
      <string>pkill -f '\bsay\b' || true; pkill -f -i 'voiceover' || true; pkill -f -i 'speech' || true; pkill -f -i 'avspeech' || true; pkill -f -i 'siri' || true; echo "$(timestamp) tracer agent ran" >> ${DIAG_LOG}</string>
    </array>
    <key>StartInterval</key>
    <integer>${START_INTERVAL}</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${LOGDIR}/agent.out.log</string>
    <key>StandardErrorPath</key>
    <string>${LOGDIR}/agent.err.log</string>
  </dict>
</plist>
PLIST

chmod 644 "$AGENT_PLIST"
launchctl bootstrap gui/$(id -u) "$AGENT_PLIST" 2>/dev/null || launchctl unload "$AGENT_PLIST" 2>/dev/null || true
launchctl enable "gui/$(id -u)/${AGENT_LABEL}" 2>/dev/null || true
launchctl kickstart -k "gui/$(id -u)/${AGENT_LABEL}" 2>/dev/null || true

echo "$(timestamp) tracer setup complete" >> "$DIAG_LOG"
