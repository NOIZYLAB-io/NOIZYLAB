# MC96ECOUNIVERSE REMOTE ACCESS
## SCANNED • FIXED • OPTIMIZED
---

# STEP 1: INITIAL SETUP (Run Once Per Machine)

---

## GOD (Mac Studio M2 Ultra)

```bash
cd ~ && rm -f vscode_cli.tar.gz code 2>/dev/null && curl -fSL 'https://code.visualstudio.com/sha/download?build=stable&os=cli-darwin-arm64' -o vscode_cli.tar.gz && tar -xzf vscode_cli.tar.gz && rm vscode_cli.tar.gz && chmod +x ./code && ./code tunnel --name GOD --accept-server-license-terms
```

---

## GABRIEL (Windows - Run PowerShell as Admin)

```powershell
Set-Location $env:USERPROFILE; Remove-Item -Force vscode_cli.zip,code.exe -ErrorAction SilentlyContinue; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://code.visualstudio.com/sha/download?build=stable&os=cli-win32-x64' -OutFile vscode_cli.zip; Expand-Archive vscode_cli.zip -DestinationPath . -Force; Remove-Item vscode_cli.zip; .\code.exe tunnel --name GABRIEL --accept-server-license-terms
```

---

## DaFixer (MacBook Pro 13" Intel)

```bash
cd ~ && rm -f vscode_cli.tar.gz code 2>/dev/null && curl -fSL 'https://code.visualstudio.com/sha/download?build=stable&os=cli-darwin-x64' -o vscode_cli.tar.gz && tar -xzf vscode_cli.tar.gz && rm vscode_cli.tar.gz && chmod +x ./code && ./code tunnel --name DaFixer --accept-server-license-terms
```

---

# STEP 2: AUTHENTICATE

When you run the command above, you'll see:

```
To grant access to the server, please log into https://github.com/login/device and use code XXXX-XXXX
```

1. Go to **github.com/login/device** (from any device)
2. Enter the code shown
3. Click Authorize
4. Done - tunnel is live

---

# STEP 3: MAKE PERSISTENT (Survives Reboot)

Run AFTER Step 1 succeeds.

---

## GOD - Auto-Start

```bash
mkdir -p ~/Library/LaunchAgents && cat > ~/Library/LaunchAgents/com.vscode.tunnel.GOD.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.vscode.tunnel.GOD</string>
    <key>ProgramArguments</key>
    <array>
        <string>sh</string>
        <string>-c</string>
        <string>$HOME/code tunnel --name GOD --accept-server-license-terms</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>NetworkState</key>
        <true/>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/vscode-tunnel-GOD.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/vscode-tunnel-GOD.err</string>
</dict>
</plist>
PLIST
launchctl bootout gui/$(id -u)/com.vscode.tunnel.GOD 2>/dev/null; launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.vscode.tunnel.GOD.plist && echo "✅ GOD tunnel will auto-start on boot"
```

---

## GABRIEL - Auto-Start

```powershell
$task = Get-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL" -ErrorAction SilentlyContinue; if ($task) { Unregister-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL" -Confirm:$false }
$action = New-ScheduledTaskAction -Execute "$env:USERPROFILE\code.exe" -Argument "tunnel --name GABRIEL --accept-server-license-terms"
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL" -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest -Force
Write-Host "✅ GABRIEL tunnel will auto-start on login" -ForegroundColor Green
```

---

## DaFixer - Auto-Start

```bash
mkdir -p ~/Library/LaunchAgents && cat > ~/Library/LaunchAgents/com.vscode.tunnel.DaFixer.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.vscode.tunnel.DaFixer</string>
    <key>ProgramArguments</key>
    <array>
        <string>sh</string>
        <string>-c</string>
        <string>$HOME/code tunnel --name DaFixer --accept-server-license-terms</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>NetworkState</key>
        <true/>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/vscode-tunnel-DaFixer.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/vscode-tunnel-DaFixer.err</string>
</dict>
</plist>
PLIST
launchctl bootout gui/$(id -u)/com.vscode.tunnel.DaFixer 2>/dev/null; launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.vscode.tunnel.DaFixer.plist && echo "✅ DaFixer tunnel will auto-start on boot"
```

---

# ACCESS FROM iPAD

Open Safari and go to:

| Machine | URL |
|---------|-----|
| GOD | `vscode.dev/tunnel/GOD` |
| GABRIEL | `vscode.dev/tunnel/GABRIEL` |
| DaFixer | `vscode.dev/tunnel/DaFixer` |

Sign in with same GitHub account. Full VS Code in browser.

---

# MANAGEMENT COMMANDS

## Check Status

**Mac:**
```bash
launchctl list | grep vscode && echo "---" && cat /tmp/vscode-tunnel-*.log 2>/dev/null | tail -5
```

**Windows:**
```powershell
Get-ScheduledTask -TaskName "VSCodeTunnel*" | Select-Object TaskName,State
```

## Stop Tunnel

**Mac (GOD):**
```bash
launchctl bootout gui/$(id -u)/com.vscode.tunnel.GOD
```

**Mac (DaFixer):**
```bash
launchctl bootout gui/$(id -u)/com.vscode.tunnel.DaFixer
```

**Windows:**
```powershell
Stop-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL"
```

## Restart Tunnel

**Mac (GOD):**
```bash
launchctl kickstart -k gui/$(id -u)/com.vscode.tunnel.GOD
```

**Windows:**
```powershell
Start-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL"
```

## Remove Everything

**Mac:**
```bash
launchctl bootout gui/$(id -u)/com.vscode.tunnel.GOD 2>/dev/null; launchctl bootout gui/$(id -u)/com.vscode.tunnel.DaFixer 2>/dev/null; rm -f ~/Library/LaunchAgents/com.vscode.tunnel.*.plist ~/code ~/vscode_cli.tar.gz
```

**Windows:**
```powershell
Unregister-ScheduledTask -TaskName "VSCodeTunnel_GABRIEL" -Confirm:$false; Remove-Item "$env:USERPROFILE\code.exe","$env:USERPROFILE\vscode_cli.zip" -Force -ErrorAction SilentlyContinue
```

## Revoke All GitHub Access
Visit: **github.com/settings/sessions** → Remove VS Code tunnels

---

# FIXES APPLIED

| Issue | Fix |
|-------|-----|
| curl silent fail | Added `-f` flag to fail on HTTP errors |
| Stale files | Added cleanup of old downloads before fresh install |
| Missing execute permission | Added `chmod +x` |
| Hardcoded username in plist | Changed to `$HOME` via shell wrapper |
| Old launchctl syntax | Updated to `bootout`/`bootstrap` (modern macOS) |
| No network awareness | Added `KeepAlive.NetworkState` - waits for network |
| No logging | Added stdout/stderr to `/tmp/` for debugging |
| Windows TLS issues | Force TLS 1.2 for download |
| Task conflicts | Remove existing task before creating new |
| No restart on failure | Windows task retries 3x on failure |

---

# SECURITY

- Only YOUR GitHub account can connect
- All traffic end-to-end encrypted  
- Revoke anytime at github.com/settings/sessions
- No ports opened on your router
- No SSH keys to manage
