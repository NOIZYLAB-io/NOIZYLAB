#!/usr/bin/env python3
"""
███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗      ██████╗ ██████╗ 
████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝      ██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ █████╗██████╔╝██████╔╝
██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ╚════╝██╔══██╗██╔══██╗
██║ ╚████║╚██████╔╝██║███████╗   ██║         ██║  ██║██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝

NOIZY-RR (REPAIR ROB) - Voice-Powered Repair Assistant
=========================================================

"Yo, what's broken?" → Diagnose → Fix → Done.

Voice Commands:
  "RR, what's wrong with my Mac?"
  "RR, fix my wifi"
  "RR, speed up this thing"
  "RR, check disk space"
  "RR, why is it slow?"
  "RR, help"

CIRCLE OF 8 MEMBER: The Fixer
"""

import os
import sys
import subprocess
import json
import re
import platform
from datetime import datetime
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════

HOME = Path.home()
RR_HOME = HOME / ".noizy_rr"
LOG_PATH = RR_HOME / "repairs.log"
VOICE_ENABLED = True

# Personality
RR_NAME = "Repair Rob"
RR_VOICE = "Daniel"  # macOS voice: Daniel, Alex, Samantha, etc.
RR_PHRASES = {
    "greeting": ["Yo, what's broken?", "RR here. What needs fixing?", "Repair Rob online. Hit me."],
    "thinking": ["Let me check that...", "Scanning...", "On it..."],
    "success": ["Boom. Fixed.", "Done deal.", "That's handled.", "Easy money."],
    "fail": ["Hmm, that's weird.", "Gonna need to dig deeper.", "That one's tricky."],
    "goodbye": ["Stay noizy.", "RR out.", "Call me if it breaks again."]
}

# ═══════════════════════════════════════════════════════════════════════════════
# VOICE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def speak(text, wait=True):
    """Text-to-speech using macOS say command"""
    if not VOICE_ENABLED:
        print(f"🔊 {text}")
        return
    try:
        cmd = ["say", "-v", RR_VOICE, text]
        if wait:
            subprocess.run(cmd, capture_output=True)
        else:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"🔊 {text}")
    except:
        print(f"🔊 {text}")

def listen(prompt="", timeout=10):
    """Listen for voice input using macOS speech recognition"""
    # For now, fall back to text input
    # TODO: Integrate with macOS Dictation API or whisper.cpp
    if prompt:
        speak(prompt, wait=True)
    try:
        return input("🎤 You: ").strip()
    except (KeyboardInterrupt, EOFError):
        return "quit"

def random_phrase(category):
    """Get random phrase from category"""
    import random
    phrases = RR_PHRASES.get(category, ["..."])
    return random.choice(phrases)

# ═══════════════════════════════════════════════════════════════════════════════
# DIAGNOSTIC ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def run_cmd(cmd, timeout=30):
    """Run shell command and return output"""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip() + r.stderr.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"

def diagnose_system():
    """Full system diagnostic"""
    speak(random_phrase("thinking"))
    results = []
    
    # CPU
    cpu = run_cmd("sysctl -n machdep.cpu.brand_string")
    load = run_cmd("uptime | awk -F'load averages:' '{print $2}'")
    results.append(f"🖥️  CPU: {cpu}")
    results.append(f"📊 Load:{load}")
    
    # Memory
    mem = run_cmd("vm_stat | head -5")
    results.append(f"🧠 Memory OK" if "Pages free" in mem else "⚠️ Memory pressure")
    
    # Disk
    disk = run_cmd("df -h / | tail -1 | awk '{print $5}'")
    pct = int(disk.replace('%', '')) if disk.replace('%', '').isdigit() else 0
    emoji = "✅" if pct < 80 else "⚠️" if pct < 90 else "🔴"
    results.append(f"{emoji} Disk: {disk} used")
    
    # Network
    ping = run_cmd("ping -c 1 -t 2 8.8.8.8 2>&1")
    results.append("🌐 Network: Connected" if "1 packets received" in ping else "🔴 Network: Issues")
    
    # Battery (if laptop)
    batt = run_cmd("pmset -g batt 2>/dev/null | grep -o '[0-9]*%'")
    if batt:
        results.append(f"🔋 Battery: {batt}")
    
    return results

def diagnose_network():
    """Network diagnostic"""
    speak("Checking network...")
    results = ["🌐 NETWORK DIAGNOSTIC", "═" * 40]
    
    # WiFi status
    wifi = run_cmd("networksetup -getairportnetwork en0 2>/dev/null")
    results.append(f"📶 {wifi}" if "Current" in wifi else "📶 WiFi: Not connected")
    
    # IP
    ip = run_cmd("ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null")
    results.append(f"🏠 Local IP: {ip}" if ip else "🏠 No IP address")
    
    # External IP
    ext_ip = run_cmd("curl -s ifconfig.me --max-time 5")
    results.append(f"🌍 External: {ext_ip}" if ext_ip and not ext_ip.startswith("ERROR") else "🌍 Can't reach internet")
    
    # DNS
    dns = run_cmd("scutil --dns | grep nameserver | head -2")
    results.append(f"🔍 DNS:\n{dns}" if dns else "🔍 No DNS configured")
    
    # Speed test (quick)
    results.append("\n⚡ Testing speed...")
    dl = run_cmd("curl -s -w '%{speed_download}' -o /dev/null http://speedtest.tele2.net/1MB.zip --max-time 10")
    if dl and dl.replace('.', '').isdigit():
        mbps = float(dl) / 125000  # bytes/s to Mbps
        results.append(f"⬇️  Download: {mbps:.1f} Mbps")
    
    return results

def diagnose_disk():
    """Disk diagnostic"""
    speak("Checking storage...")
    results = ["💾 DISK DIAGNOSTIC", "═" * 40]
    
    # Disk usage
    df = run_cmd("df -h / /Volumes/* 2>/dev/null | grep -v 'Filesystem'")
    for line in df.split('\n')[:5]:
        if line.strip():
            results.append(f"📁 {line}")
    
    # Large files
    results.append("\n🐘 Largest directories in ~:")
    large = run_cmd("du -sh ~/Downloads ~/Library/Caches ~/Desktop 2>/dev/null | sort -hr | head -5")
    results.append(large)
    
    # Trash size
    trash = run_cmd("du -sh ~/.Trash 2>/dev/null | awk '{print $1}'")
    results.append(f"\n🗑️  Trash: {trash}" if trash else "🗑️  Trash: Empty")
    
    return results

def diagnose_performance():
    """Why is it slow?"""
    speak("Let me see what's eating resources...")
    results = ["🐌 PERFORMANCE CHECK", "═" * 40]
    
    # Top CPU processes
    results.append("🔥 Top CPU hogs:")
    cpu_procs = run_cmd("ps aux | sort -nrk 3 | head -5 | awk '{print $3\"% \"$11}'")
    results.append(cpu_procs)
    
    # Top memory processes
    results.append("\n🧠 Top memory hogs:")
    mem_procs = run_cmd("ps aux | sort -nrk 4 | head -5 | awk '{print $4\"% \"$11}'")
    results.append(mem_procs)
    
    # Uptime
    uptime = run_cmd("uptime")
    results.append(f"\n⏱️  {uptime}")
    
    # Suggest restart if uptime > 7 days
    days = run_cmd("uptime | grep -oE '[0-9]+ days?' | grep -oE '[0-9]+'")
    if days and int(days) > 7:
        results.append("💡 Been running {days} days. Restart might help.")
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# FIX ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def fix_wifi():
    """Reset WiFi"""
    speak("Resetting WiFi...")
    run_cmd("networksetup -setairportpower en0 off")
    import time; time.sleep(2)
    run_cmd("networksetup -setairportpower en0 on")
    speak(random_phrase("success"))
    return ["✅ WiFi reset", "Give it a few seconds to reconnect"]

def fix_dns():
    """Flush DNS cache"""
    speak("Flushing DNS...")
    run_cmd("sudo dscacheutil -flushcache 2>/dev/null")
    run_cmd("sudo killall -HUP mDNSResponder 2>/dev/null")
    speak(random_phrase("success"))
    return ["✅ DNS cache flushed"]

def fix_memory():
    """Free up memory"""
    speak("Clearing memory pressure...")
    run_cmd("sudo purge 2>/dev/null")
    speak(random_phrase("success"))
    return ["✅ Memory purged", "Inactive memory freed up"]

def fix_disk():
    """Clean up disk space"""
    speak("Cleaning up disk space...")
    results = ["🧹 CLEANUP", "═" * 40]
    
    # Clear caches
    cache_before = run_cmd("du -sh ~/Library/Caches 2>/dev/null | awk '{print $1}'")
    run_cmd("rm -rf ~/Library/Caches/* 2>/dev/null")
    results.append(f"✅ Cleared ~/Library/Caches (was {cache_before})")
    
    # Clear logs
    run_cmd("sudo rm -rf /private/var/log/asl/*.asl 2>/dev/null")
    results.append("✅ Cleared system logs")
    
    # Suggest emptying trash
    trash = run_cmd("du -sh ~/.Trash 2>/dev/null | awk '{print $1}'")
    if trash and trash != "0B":
        results.append(f"💡 Trash has {trash}. Empty it: rm -rf ~/.Trash/*")
    
    speak(random_phrase("success"))
    return results

def fix_slow():
    """Speed up Mac"""
    speak("Let me speed this up...")
    results = ["⚡ SPEEDUP", "═" * 40]
    
    # Kill heavy processes (user can choose)
    results.append("Heavy processes:")
    heavy = run_cmd("ps aux | sort -nrk 3 | head -3 | awk '{print $2\" \"$11\" (\"$3\"%)\"}'")
    results.append(heavy)
    results.append("\n💡 Kill a process: kill -9 <PID>")
    
    # Reindex Spotlight (common slowdown cause)
    results.append("\n🔍 Rebuilding Spotlight index...")
    run_cmd("sudo mdutil -E / 2>/dev/null &")
    results.append("✅ Spotlight reindexing in background")
    
    speak(random_phrase("success"))
    return results

def fix_permissions():
    """Fix permissions"""
    speak("Fixing permissions...")
    run_cmd("diskutil resetUserPermissions / $(id -u) 2>/dev/null")
    speak(random_phrase("success"))
    return ["✅ User permissions reset"]

# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND PARSER
# ═══════════════════════════════════════════════════════════════════════════════

def parse_command(text):
    """Parse natural language into commands"""
    text = text.lower().strip()
    
    # Exit commands
    if text in ["quit", "exit", "bye", "q"]:
        return "quit", None
    
    # Help
    if "help" in text:
        return "help", None
    
    # Diagnostics
    if any(w in text for w in ["what's wrong", "diagnose", "check", "scan", "status"]):
        if "network" in text or "wifi" in text or "internet" in text:
            return "diagnose", "network"
        if "disk" in text or "storage" in text or "space" in text:
            return "diagnose", "disk"
        if "slow" in text or "performance" in text or "speed" in text:
            return "diagnose", "performance"
        return "diagnose", "system"
    
    # Why questions
    if "why" in text:
        if "slow" in text:
            return "diagnose", "performance"
        return "diagnose", "system"
    
    # Fix commands
    if any(w in text for w in ["fix", "repair", "reset", "clear", "clean"]):
        if "wifi" in text or "network" in text:
            return "fix", "wifi"
        if "dns" in text:
            return "fix", "dns"
        if "memory" in text or "ram" in text:
            return "fix", "memory"
        if "disk" in text or "storage" in text or "space" in text:
            return "fix", "disk"
        if "slow" in text or "speed" in text:
            return "fix", "slow"
        if "permission" in text:
            return "fix", "permissions"
        return "help", None
    
    # Speed up
    if "speed" in text and "up" in text:
        return "fix", "slow"
    
    return "unknown", text

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN LOOP
# ═══════════════════════════════════════════════════════════════════════════════

def show_help():
    return """
🔧 NOIZY-RR (Repair Rob) Commands:
══════════════════════════════════════

DIAGNOSE:
  "What's wrong with my Mac?"
  "Check my network"
  "Check disk space"
  "Why is it slow?"

FIX:
  "Fix my wifi"
  "Fix DNS"
  "Clear memory"
  "Clean disk space"
  "Speed up my Mac"
  "Fix permissions"

OTHER:
  "help" - This menu
  "quit" - Exit

Just talk naturally. RR understands.
"""

def log_action(action, result):
    """Log repair actions"""
    RR_HOME.mkdir(exist_ok=True)
    with open(LOG_PATH, 'a') as f:
        f.write(f"{datetime.now().isoformat()} | {action} | {result[:100]}\n")

def main():
    RR_HOME.mkdir(exist_ok=True)
    
    # CLI mode
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        action, target = parse_command(text)
    else:
        # Interactive mode
        print("""
███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗      ██████╗ ██████╗ 
████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝      ██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ █████╗██████╔╝██████╔╝
██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ╚════╝██╔══██╗██╔══██╗
██║ ╚████║╚██████╔╝██║███████╗   ██║         ██║  ██║██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝
        """)
        speak(random_phrase("greeting"))
        
        while True:
            text = listen()
            if not text:
                continue
            
            action, target = parse_command(text)
            
            if action == "quit":
                speak(random_phrase("goodbye"))
                break
            
            if action == "help":
                print(show_help())
                continue
            
            if action == "diagnose":
                if target == "network":
                    results = diagnose_network()
                elif target == "disk":
                    results = diagnose_disk()
                elif target == "performance":
                    results = diagnose_performance()
                else:
                    results = diagnose_system()
                print('\n'.join(results))
                log_action(f"diagnose_{target}", "completed")
                continue
            
            if action == "fix":
                if target == "wifi":
                    results = fix_wifi()
                elif target == "dns":
                    results = fix_dns()
                elif target == "memory":
                    results = fix_memory()
                elif target == "disk":
                    results = fix_disk()
                elif target == "slow":
                    results = fix_slow()
                elif target == "permissions":
                    results = fix_permissions()
                else:
                    print("❓ What should I fix? (wifi/dns/memory/disk/slow)")
                    continue
                print('\n'.join(results))
                log_action(f"fix_{target}", "completed")
                continue
            
            # Unknown
            speak(f"Not sure what you mean by '{text}'. Say 'help' for options.")
        
        return
    
    # Single command mode
    if action == "help":
        print(show_help())
    elif action == "diagnose":
        if target == "network":
            print('\n'.join(diagnose_network()))
        elif target == "disk":
            print('\n'.join(diagnose_disk()))
        elif target == "performance":
            print('\n'.join(diagnose_performance()))
        else:
            print('\n'.join(diagnose_system()))
    elif action == "fix":
        fixes = {"wifi": fix_wifi, "dns": fix_dns, "memory": fix_memory, 
                 "disk": fix_disk, "slow": fix_slow, "permissions": fix_permissions}
        if target in fixes:
            print('\n'.join(fixes[target]()))
        else:
            print(show_help())
    else:
        print(f"❓ Unknown: {text}")
        print(show_help())

if __name__ == "__main__":
    main()
