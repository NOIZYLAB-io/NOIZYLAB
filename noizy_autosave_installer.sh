#!/usr/bin/env bash
set -euo pipefail

# --- Configuration ---
USER_HOME="$HOME"
LOG_ROOT="${USER_HOME}/noizy_autosave"
TRACER_DIR="/usr/local/bin"
TRACER_SH="${TRACER_DIR}/say-tracer"
SHIM_DIR="${USER_HOME}/.noizy_shim"
SHIM_SAY="${SHIM_DIR}/say"
PATH_AGENT_PLIST="${USER_HOME}/Library/LaunchAgents/com.noizy.pathfix.plist"
TRACER_AGENT_PLIST="${USER_HOME}/Library/LaunchAgents/com.noizy.tracer.plist"
ROTATE_AGENT_PLIST="${USER_HOME}/Library/LaunchAgents/com.noizy.logrotate.plist"
INV_LOG="${LOG_ROOT}/invocations.log"
DIAG_LOG="${LOG_ROOT}/diag.log"
ROTATED_DIR="${LOG_ROOT}/archive"
RETENTION_DAYS=14
TRACER_INTERVAL=0   # 0 means tracer runs on demand via shim; agent keeps PATH set on login
ROTATE_HOUR=3       # daily rotation hour (24h)

mkdir -p "${LOG_ROOT}" "${ROTATED_DIR}" "${SHIM_DIR}" 2>/dev/null || true

timestamp(){ date -u +"%Y-%m-%dT%H:%M:%SZ"; }

echo "$(timestamp) Installing NOIZY AutoSave & AutoRun (logs: ${LOG_ROOT})" >> "${DIAG_LOG}"

# --- 1) Install non-destructive tracer binary in /usr/local/bin ---
sudo mkdir -p "${TRACER_DIR}" 2>/dev/null || true

sudo tee "${TRACER_SH}" > /dev/null <<'EOF'
#!/usr/bin/env bash
LOG="${HOME}/noizy_autosave/invocations.log"
DIAG="${HOME}/noizy_autosave/diag_each.log"
T="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
CALLER=${PPID:-0}
CHAIN=""
pid=$CALLER
while [ "$pid" -gt 1 ]; do
  comm=$(ps -p "$pid" -o comm= 2>/dev/null | tr -d '\n' || echo "unknown")
  CHAIN="${CHAIN}${pid}:${comm}|"
  pid=$(ps -p "$pid" -o ppid= 2>/dev/null | tr -d ' ' || echo 1)
  if [ -z "$pid" ]; then pid=1; fi
done
echo "${T} CALLER:${CALLER} CHAIN:${CHAIN} ARGS:${*}" >> "${LOG}"
echo "${T} detailed: CALLER:${CALLER} CHAIN:${CHAIN} ARGS:${*}" >> "${DIAG}"
# attempt to call system say in background so tracer is non-blocking
if [ -x "/usr/bin/say" ]; then
  /usr/bin/say "$@" &
fi
EOF

sudo chmod 755 "${TRACER_SH}"
echo "$(timestamp) Tracer installed at ${TRACER_SH}" >> "${DIAG_LOG}"

# --- 2) Create shim in user's home and ensure GUI session PATH points to shim ---
ln -sf "${TRACER_SH}" "${SHIM_SAY}"
chmod 755 "${SHIM_SAY}"
echo "$(timestamp) Shim created at ${SHIM_SAY}" >> "${DIAG_LOG}"

cat > "${PATH_AGENT_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.noizy.pathfix</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>-lc</string>
      <string>/bin/launchctl setenv PATH "${SHIM_DIR}:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"; echo "$(timestamp) PATH set by noizy pathfix" >> ${DIAG_LOG}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
  </dict>
</plist>
PLIST

chmod 644 "${PATH_AGENT_PLIST}"
launchctl bootstrap gui/$(id -u) "${PATH_AGENT_PLIST}" 2>/dev/null || launchctl kickstart -k "gui/$(id -u)/com.noizy.pathfix" 2>/dev/null || true
echo "$(timestamp) PATH fix agent installed: ${PATH_AGENT_PLIST}" >> "${DIAG_LOG}"

# --- 3) Install daily log-rotate autorun agent (archives and prunes logs) ---
cat > "${ROTATE_AGENT_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.noizy.logrotate</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>-lc</string>
      <string>mkdir -p ${ROTATED_DIR}; ts=\$(date -u +%Y%m%dT%H%M%SZ); if [ -f ${INV_LOG} ]; then mv ${INV_LOG} ${ROTATED_DIR}/invocations-\$ts.log; fi; if [ -f ${DIAG_LOG} ]; then mv ${DIAG_LOG} ${ROTATED_DIR}/diag-\$ts.log; fi; find ${ROTATED_DIR} -type f -mtime +${RETENTION_DAYS} -delete; echo "\$(date -u) rotated logs" >> ${LOG_ROOT}/rotate.log</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
      <key>Hour</key>
      <integer>${ROTATE_HOUR}</integer>
      <key>Minute</key>
      <integer>5</integer>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${LOG_ROOT}/rotate.out.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_ROOT}/rotate.err.log</string>
  </dict>
</plist>
PLIST

chmod 644 "${ROTATE_AGENT_PLIST}"
launchctl bootstrap gui/$(id -u) "${ROTATE_AGENT_PLIST}" 2>/dev/null || launchctl kickstart -k "gui/$(id -u)/com.noizy.logrotate" 2>/dev/null || true
echo "$(timestamp) Log-rotate agent installed: ${ROTATE_AGENT_PLIST}" >> "${DIAG_LOG}"

# --- 4) (Optional) Install a light tracer agent to tail and snapshot invocations (keeps small footprint) ---
cat > "${TRACER_AGENT_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.noizy.tracer</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>-lc</string>
      <string>mkdir -p ${LOG_ROOT}; tail -n 200 ${INV_LOG} 2>/dev/null | tail -n 200 > ${LOG_ROOT}/last_invocations.tmp || true; echo "\$(date -u) tracer agent run" >> ${DIAG_LOG}</string>
    </array>
    <key>StartInterval</key>
    <integer>30</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${LOG_ROOT}/tracer.out.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_ROOT}/tracer.err.log</string>
  </dict>
</plist>
PLIST

chmod 644 "${TRACER_AGENT_PLIST}"
launchctl bootstrap gui/$(id -u) "${TRACER_AGENT_PLIST}" 2>/dev/null || launchctl kickstart -k "gui/$(id -u)/com.noizy.tracer" 2>/dev/null || true
echo "$(timestamp) Tracer agent installed: ${TRACER_AGENT_PLIST}" >> "${DIAG_LOG}"

# --- 5) Quick immediate mute and kill to stop current voices while installer finishes ---
osascript -e "set volume output muted true" 2>/dev/null || true
pkill -f '\bsay\b' 2>/dev/null || true
pkill -f -i 'voiceover' 2>/dev/null || true
pkill -f -i 'speech' 2>/dev/null || true
pkill -f -i 'avspeech' 2>/dev/null || true
pkill -f -i 'siri' 2>/dev/null || true

echo "$(timestamp) Immediate silence applied" >> "${DIAG_LOG}"

# --- 6) Uninstall helper ---
UNINSTALL="${LOG_ROOT}/uninstall_noizy_autosave.sh"
cat > "${UNINSTALL}" <<UNINST
#!/usr/bin/env bash
set -euo pipefail
USER_HOME="${USER_HOME}"
LOG_ROOT="${LOG_ROOT}"
TRACER_SH="${TRACER_SH}"
SHIM_DIR="${SHIM_DIR}"
LAUNCH_PLISTS=("${PATH_AGENT_PLIST}" "${ROTATE_AGENT_PLIST}" "${TRACER_AGENT_PLIST}")

echo "Stopping and removing LaunchAgents..."
for p in "\${LAUNCH_PLISTS[@]}"; do
  if [ -f "\$p" ]; then
    launchctl bootout gui/\$(id -u) "\$p" 2>/dev/null || true
    rm -f "\$p"
  fi
done

echo "Removing shim and tracer binary..."
rm -f "${SHIM_SAY}"
sudo rm -f "${TRACER_SH}" 2>/dev/null || true

echo "Removing PATH env if present..."
/bin/launchctl unsetenv PATH 2>/dev/null || true

echo "Uninstall complete. Logs preserved at \${LOG_ROOT}"
UNINST
chmod +x "${UNINSTALL}"

echo "$(timestamp) Installation complete.
- Tracer shim: ${SHIM_SAY}
- Tracer binary: ${TRACER_SH}
- PATH agent: ${PATH_AGENT_PLIST}
- Tracer agent: ${TRACER_AGENT_PLIST}
- Log rotate agent: ${ROTATE_AGENT_PLIST}
- Logs: ${LOG_ROOT}
- Uninstall helper: ${UNINSTALL}" >> "${DIAG_LOG}"

cat <<SUMMARY

NOIZY AutoSave & AutoRun installed.

What it does
- Ensures GUI session PATH contains a shim so GUI-launched processes prefer the tracer shim
- Captures every future TTS invocation to: ${INV_LOG}
- Autosaves and archives logs daily to: ${ROTATED_DIR} and keeps ${RETENTION_DAYS} days
- Autoruns on login via LaunchAgents; tracer agent snapshots invocations every 30s

To inspect now:
- Tail live invocations: tail -n 200 ${INV_LOG}
- See diagnostics: tail -n 200 ${DIAG_LOG}
- View archived logs: ls -1 ${ROTATED_DIR}

To uninstall:
bash "${UNINSTALL}"

SUMMARY
