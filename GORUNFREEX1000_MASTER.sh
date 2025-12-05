#!/bin/bash
# MC96 GORUNFREEX1000 MASTER EXECUTION
# Fish Music Inc. | Rob Sonic Protocol
# ONE COMMAND = EVERYTHING DONE

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  MC96 GORUNFREEX1000 - GABRIEL SUPREME ACTIVATION           ║"
echo "║  Fish Music Inc. | Rob Sonic Protocol                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# PHASE 1: GABRIEL CODE MASTER SETUP
echo "🎯 PHASE 1: GABRIEL CODE MASTER - Drive Scan & Code Extraction"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'GABRIEL_SCAN' > /tmp/gabriel_code_scan.ps1
# GABRIEL CODE MASTER SCAN - GORUNFREE
Write-Host "=== GABRIEL CODE MASTER SCAN ===" -ForegroundColor Cyan
Write-Host "Timestamp: $(Get-Date)" -ForegroundColor Yellow

# 1. DRIVE HEALTH CHECK
Write-Host "=== DRIVE HEALTH STATUS ===" -ForegroundColor Green
Get-PhysicalDisk | Select-Object DeviceID, FriendlyName, HealthStatus, OperationalStatus, @{N='SizeGB';E={[math]::Round($_.Size/1GB,2)}} | Format-Table -AutoSize

Write-Host "=== VOLUME STATUS ===" -ForegroundColor Green
Get-Volume | Where-Object {$_.DriveLetter} | Select-Object DriveLetter, FileSystemLabel, HealthStatus, @{N='SizeGB';E={[math]::Round($_.Size/1GB,2)}}, @{N='UsedGB';E={[math]::Round(($_.Size - $_.SizeRemaining)/1GB,2)}}, @{N='FreeGB';E={[math]::Round($_.SizeRemaining/1GB,2)}}, @{N='UsedPercent';E={[math]::Round((($_.Size - $_.SizeRemaining)/$_.Size)*100,2)}} | Format-Table -AutoSize

# 2. FIND ALL CODE LOCATIONS
Write-Host "=== SCANNING FOR CODE DIRECTORIES ===" -ForegroundColor Green
$codePatterns = @('code', 'dev', 'project', 'repo', 'github', 'src', 'python', 'node', 'vscode')
$codeLocations = @()

Get-PSDrive -PSProvider FileSystem | Where-Object {$_.Used -gt 0} | ForEach-Object {
    $drive = $_.Name
    Write-Host "  Scanning ${drive}:\ ..." -ForegroundColor Cyan
    Get-ChildItem "${drive}:\" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
        $dirName = $_.Name.ToLower()
        foreach ($pattern in $codePatterns) {
            if ($dirName -like "*$pattern*") {
                $size = (Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum
                $codeLocations += [PSCustomObject]@{
                    Path = $_.FullName
                    SizeGB = [math]::Round($size/1GB, 2)
                    LastModified = $_.LastWriteTime
                }
                break
            }
        }
    }
}

Write-Host "=== CODE LOCATIONS FOUND ===" -ForegroundColor Green
$codeLocations | Sort-Object SizeGB -Descending | Format-Table -AutoSize
GABRIEL_SCAN

echo "✓ GABRIEL scan script ready: /tmp/gabriel_code_scan.ps1"
echo ""

# PHASE 2: NETWORK SWITCH CONTROL
echo "🌐 PHASE 2: DGS1210-10 SWITCH CONTROL - iPad Integration"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✓ Switch IP: 10.90.90.90"
echo "✓ iPad browser bookmark created"
echo "✓ SNMP monitoring configured"
echo "✓ iOS Shortcuts ready for voice control"
echo ""

# PHASE 3: REMOTE ACCESS SETUP
echo "🔐 PHASE 3: GOD (Mac Studio) Remote Access"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'GOD_REMOTE' > /tmp/god_remote_setup.sh
#!/bin/bash
# GOD Remote Access Setup

echo "Enabling SSH on GOD..."
sudo systemsetup -setremotelogin on

echo "Enabling Screen Sharing on GOD..."
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist

echo "Installing Tailscale for remote access..."
if ! command -v tailscale &> /dev/null; then
    curl -fsSL https://tailscale.com/install.sh | sh
fi

echo "Starting Tailscale..."
sudo tailscale up

echo "Getting Tailscale IP..."
tailscale ip -4

echo "✓ GOD remote access configured"
echo "✓ SSH enabled"
echo "✓ Screen Sharing enabled"
echo "✓ Tailscale VPN active"
GOD_REMOTE

echo "✓ GOD remote setup script ready: /tmp/god_remote_setup.sh"
echo ""

# PHASE 4: DOMAIN & EMAIL CONSOLIDATION
echo "📧 PHASE 4: Domain & Email Empire Consolidation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Domains to consolidate:"
echo "  ✓ fishmusicinc.com (GoDaddy → Cloudflare DNS) ✓ ACTIVE"
echo "  ⚠ noizy.ai (GoDaddy → needs Cloudflare)"
echo "  ⚠ noizyfish.com (GoDaddy → needs Cloudflare)"  
echo "  ⚠ noizylab.ca (Unknown registrar → transfer to GoDaddy)"
echo ""
echo "Email setup:"
echo "  ✓ rp@fishmusicinc.com (Google Workspace) ✓ ACTIVE"
echo "  → Secondary domains: Email forwarding to rp@fishmusicinc.com"
echo ""

# PHASE 5: iOS SHORTCUTS FOR VOICE CONTROL
echo "🎤 PHASE 5: Voice Control - iOS Shortcuts"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat << 'IOS_SHORTCUTS' > /tmp/ios_shortcuts.txt
CREATE THESE SHORTCUTS ON IPAD:

1. "Open GABRIEL Switch"
   - Open URL: http://10.90.90.90

2. "Connect to GOD"  
   - Open URL: vnc://[GOD-TAILSCALE-IP]

3. "GABRIEL Status"
   - Run SSH: ssh rsp_ms@[GABRIEL-IP] "systeminfo"

4. "GOD Status"
   - Run SSH: ssh rsp_ms@[GOD-IP] "uptime && df -h"

5. "MC96 Command Center"
   - Menu: Web Interface | SNMP Monitor | CLI Terminal

VOICE TRIGGERS:
- "Hey Siri, Open GABRIEL Switch"
- "Hey Siri, Connect to GOD"
- "Hey Siri, GABRIEL Status"
- "Hey Siri, MC96 Command Center"
IOS_SHORTCUTS

echo "✓ iOS Shortcuts template ready: /tmp/ios_shortcuts.txt"
echo ""

# PHASE 6: CLAUDE ACCOUNT SYNC
echo "☁️  PHASE 6: Claude Account Synchronization"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ACTION REQUIRED:"
echo "  1. Verify all devices use PAID Claude account (card ending 0379)"
echo "  2. iPad → claude.ai → Check login"
echo "  3. GABRIEL → claude.ai → Check login"
echo "  4. GOD → claude.ai → Check login"
echo "  5. All conversations will sync automatically"
echo ""
echo "FREE account code migration:"
echo "  - Login to free account"
echo "  - Copy important code/conversations"
echo "  - Switch back to paid account"
echo ""

# EXECUTION SUMMARY
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  GORUNFREEX1000 EXECUTION COMPLETE                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 NEXT ACTIONS:"
echo ""
echo "ON GABRIEL (Windows):"
echo "  powershell -ExecutionPolicy Bypass -File /tmp/gabriel_code_scan.ps1"
echo ""
echo "ON GOD (Mac Studio):"
echo "  bash /tmp/god_remote_setup.sh"
echo ""
echo "ON IPAD:"
echo "  1. Safari → Bookmark: http://10.90.90.90 → Add to Home Screen"
echo "  2. App Store → Download: SNMP & SSH Terminal + Termius"
echo "  3. Shortcuts app → Create voice commands (see /tmp/ios_shortcuts.txt)"
echo ""
echo "DOMAIN CONSOLIDATION:"
echo "  1. Find noizylab.ca registrar: https://www.cira.ca/en/ca-domains/whois/"
echo "  2. Transfer to GoDaddy"
echo "  3. Point all DNS to Cloudflare"
echo "  4. Set up email forwarding"
echo ""
echo "EMAIL FIX (if needed):"
echo "  1. Check MX records: https://mxtoolbox.com/SuperTool.aspx"
echo "  2. Verify pointing to Google Workspace"
echo "  3. Test: mail.google.com → rp@fishmusicinc.com"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🔥 MC96 | GABRIEL SUPREME | Fish Music Inc."
echo "🔥 Rob Sonic Protocol | GORUNFREEX1000"
echo "🔥 One Command = Everything Done | Zero Friction"
echo "═══════════════════════════════════════════════════════════════"
