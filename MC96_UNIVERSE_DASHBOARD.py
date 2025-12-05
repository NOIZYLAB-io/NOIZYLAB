#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
███╗   ███╗ ██████╗ █████╗  ██████╗     ██╗   ██╗███╗   ██╗██╗██╗   ██╗███████╗██████╗ ███████╗███████╗
████╗ ████║██╔════╝██╔══██╗██╔════╝     ██║   ██║████╗  ██║██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝
██╔████╔██║██║     ╚██████║███████╗     ██║   ██║██╔██╗ ██║██║██║   ██║█████╗  ██████╔╝███████╗█████╗  
██║╚██╔╝██║██║      ╚═══██║██╔═══██╗    ██║   ██║██║╚██╗██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  
██║ ╚═╝ ██║╚██████╗ █████╔╝╚██████╔╝    ╚██████╔╝██║ ╚████║██║ ╚████╔╝ ███████╗██║  ██║███████║███████╗
╚═╝     ╚═╝ ╚═════╝ ╚════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
                            ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗  █████╗ ██████╗ ██████╗   
                            ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗  
                            ██║  ██║███████║███████╗███████║██████╔╝██║   ██║███████║██████╔╝██║  ██║  
                            ██║  ██║██╔══██║╚════██║██╔══██║██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║  
                            ██████╔╝██║  ██║███████║██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝  
                            ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝   
═══════════════════════════════════════════════════════════════════════════════
MC96ECOUNIVERSE REAL-TIME DASHBOARD - 1000% SPEED MONITORING
GOD (M2 Ultra) + GABRIEL (HP-OMEN) = UNIFIED THROUGH GITHUB
═══════════════════════════════════════════════════════════════════════════════
"""

import subprocess
import os
import time
import json
from datetime import datetime
from pathlib import Path

# Colors
class C:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def run_cmd(cmd):
    """Run command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except:
        return ""

def get_mtu():
    """Get current MTU"""
    output = run_cmd("ifconfig en0 | grep mtu | awk '{print $NF}'")
    return output if output else "Unknown"

def get_dns():
    """Get DNS servers"""
    output = run_cmd("scutil --dns | grep 'nameserver' | head -1 | awk '{print $3}'")
    return output if output else "Unknown"

def get_volumes():
    """Get all mounted volumes with sizes"""
    volumes = []
    output = run_cmd("df -h | grep -E '^/dev|Volumes'")
    for line in output.split('\n'):
        if line:
            parts = line.split()
            if len(parts) >= 6:
                volumes.append({
                    'device': parts[0][:30],
                    'size': parts[1],
                    'used': parts[2],
                    'free': parts[3],
                    'percent': parts[4],
                    'mount': parts[-1]
                })
    return volumes

def get_network_speed():
    """Get network interface speed"""
    output = run_cmd("ifconfig en0 | grep 'media:' | head -1")
    if "1000" in output or "Gigabit" in output:
        return "1 Gbps"
    elif "10G" in output:
        return "10 Gbps"
    elif "100" in output:
        return "100 Mbps"
    return "Unknown"

def get_tcp_settings():
    """Get TCP buffer settings"""
    send = run_cmd("sysctl -n net.inet.tcp.sendspace 2>/dev/null")
    recv = run_cmd("sysctl -n net.inet.tcp.recvspace 2>/dev/null")
    return {
        'send': f"{int(send)//1024}KB" if send.isdigit() else "Unknown",
        'recv': f"{int(recv)//1024}KB" if recv.isdigit() else "Unknown"
    }

def get_memory():
    """Get memory usage"""
    output = run_cmd("vm_stat | head -10")
    # Parse vm_stat output
    total = run_cmd("sysctl -n hw.memsize 2>/dev/null")
    if total:
        total_gb = int(total) / (1024**3)
        return f"{total_gb:.0f} GB"
    return "Unknown"

def get_cpu():
    """Get CPU info"""
    output = run_cmd("sysctl -n machdep.cpu.brand_string 2>/dev/null")
    return output if output else "Apple Silicon"

def get_git_status():
    """Get git repo status for NOIZYLAB"""
    noizylab_path = "/Users/m2ultra/NOIZYLAB"
    if os.path.exists(f"{noizylab_path}/.git"):
        branch = run_cmd(f"cd {noizylab_path} && git branch --show-current")
        status = run_cmd(f"cd {noizylab_path} && git status --porcelain | wc -l").strip()
        last_commit = run_cmd(f"cd {noizylab_path} && git log -1 --format='%h %s' 2>/dev/null")
        return {
            'branch': branch,
            'changes': status,
            'last_commit': last_commit[:60] if last_commit else "None"
        }
    return None

def get_sample_library_stats():
    """Get Sample_Libraries folder stats"""
    path = "/Volumes/6TB/Sample_Libraries"
    if os.path.exists(path):
        # Count files by type
        stats = {
            'aiff': run_cmd(f"find '{path}' -name '*.aif' -o -name '*.aiff' 2>/dev/null | wc -l").strip(),
            'wav': run_cmd(f"find '{path}' -name '*.wav' 2>/dev/null | wc -l").strip(),
            'rx2': run_cmd(f"find '{path}' -name '*.rx2' 2>/dev/null | wc -l").strip(),
            'mid': run_cmd(f"find '{path}' -name '*.mid' 2>/dev/null | wc -l").strip(),
        }
        return stats
    return None

def calculate_supersonic_score():
    """Calculate overall SUPERSONIC score"""
    score = 0
    max_score = 100
    
    # MTU check (20 points)
    mtu = get_mtu()
    if mtu == "9000":
        score += 20
    
    # DNS check (15 points)
    dns = get_dns()
    if "1.1.1.1" in dns:
        score += 15
    
    # TCP buffers (20 points)
    tcp = get_tcp_settings()
    if "2048KB" in tcp['send'] or "2097" in str(run_cmd("sysctl -n net.inet.tcp.sendspace")):
        score += 20
    elif int(run_cmd("sysctl -n net.inet.tcp.sendspace 2>/dev/null") or 0) > 131072:
        score += 10
    
    # Network speed (15 points)
    speed = get_network_speed()
    if "1 Gbps" in speed or "10 Gbps" in speed:
        score += 15
    
    # Volumes mounted (15 points)
    volumes = get_volumes()
    if len(volumes) >= 5:
        score += 15
    elif len(volumes) >= 3:
        score += 10
    
    # Git configured (15 points)
    git = get_git_status()
    if git:
        score += 15
    
    return min(score, max_score)

def print_dashboard():
    """Print the full dashboard"""
    os.system('clear')
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{C.PURPLE}{'═' * 80}{C.END}")
    print(f"{C.WHITE}{C.BOLD}  🚀 MC96ECOUNIVERSE DASHBOARD - REAL-TIME MONITORING{C.END}")
    print(f"{C.PURPLE}{'═' * 80}{C.END}")
    print(f"  {C.CYAN}Updated: {now}{C.END}")
    print()
    
    # SUPERSONIC SCORE
    score = calculate_supersonic_score()
    score_color = C.GREEN if score >= 80 else C.YELLOW if score >= 50 else C.RED
    score_bar = "█" * (score // 5) + "░" * (20 - score // 5)
    print(f"  {C.WHITE}{C.BOLD}SUPERSONIC SCORE:{C.END} {score_color}[{score_bar}] {score}%{C.END}")
    print()
    
    # NETWORK STATUS
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.WHITE}{C.BOLD}⚡ NETWORK STATUS{C.END}")
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    
    mtu = get_mtu()
    mtu_status = f"{C.GREEN}✅ JUMBO FRAMES ACTIVE{C.END}" if mtu == "9000" else f"{C.RED}❌ STANDARD{C.END}"
    print(f"  MTU:           {mtu} {mtu_status}")
    
    dns = get_dns()
    dns_status = f"{C.GREEN}✅ CLOUDFLARE{C.END}" if "1.1.1.1" in dns else f"{C.YELLOW}⚠️ NOT CLOUDFLARE{C.END}"
    print(f"  DNS:           {dns} {dns_status}")
    
    speed = get_network_speed()
    print(f"  Link Speed:    {speed}")
    
    tcp = get_tcp_settings()
    print(f"  TCP Buffers:   Send: {tcp['send']} | Recv: {tcp['recv']}")
    print()
    
    # SYSTEM STATUS
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.WHITE}{C.BOLD}💻 SYSTEM STATUS (GOD - M2 Ultra){C.END}")
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    
    cpu = get_cpu()
    memory = get_memory()
    print(f"  CPU:           {cpu}")
    print(f"  Memory:        {memory}")
    print()
    
    # VOLUMES
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.WHITE}{C.BOLD}💾 MC96ECOUNIVERSE STORAGE{C.END}")
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    
    volumes = get_volumes()
    local_total = 0
    network_total = 0
    
    print(f"  {'VOLUME':<25} {'SIZE':>8} {'USED':>8} {'FREE':>8} {'USE%':>6}")
    print(f"  {'─' * 60}")
    
    for vol in volumes[:12]:  # Limit to 12 volumes
        mount = vol['mount']
        name = os.path.basename(mount) if mount != "/" else "SYSTEM"
        if len(name) > 24:
            name = name[:21] + "..."
        
        # Color based on usage
        try:
            pct = int(vol['percent'].replace('%', ''))
        except:
            pct = 0
        pct_color = C.RED if pct >= 90 else C.YELLOW if pct >= 75 else C.GREEN
        
        print(f"  {name:<25} {vol['size']:>8} {vol['used']:>8} {vol['free']:>8} {pct_color}{vol['percent']:>6}{C.END}")
    
    print()
    
    # GIT STATUS
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.WHITE}{C.BOLD}📦 GIT STATUS (NOIZYLAB){C.END}")
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    
    git = get_git_status()
    if git:
        changes_color = C.YELLOW if int(git['changes']) > 0 else C.GREEN
        print(f"  Branch:        {git['branch']}")
        print(f"  Changes:       {changes_color}{git['changes']} files{C.END}")
        print(f"  Last Commit:   {git['last_commit']}")
    else:
        print(f"  {C.YELLOW}⚠️ Git not configured{C.END}")
    
    print()
    
    # QUICK COMMANDS
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.WHITE}{C.BOLD}🔧 QUICK COMMANDS{C.END}")
    print(f"  {C.CYAN}{'─' * 76}{C.END}")
    print(f"  {C.GREEN}sudo ./MC96_SUPERSONIC.sh{C.END}     Activate SUPERSONIC mode")
    print(f"  {C.GREEN}git flow \"message\"{C.END}          Add + Commit + Push")
    print(f"  {C.GREEN}git morning{C.END}                  Sync from GitHub")
    print(f"  {C.GREEN}git night{C.END}                    Push nightly backup")
    print()
    
    print(f"{C.PURPLE}{'═' * 80}{C.END}")
    print(f"  {C.WHITE}GORUNFREE!!! 🔥 NO LIMITS OF ANY KIND IN THE UNIVERSE{C.END}")
    print(f"{C.PURPLE}{'═' * 80}{C.END}")

def main():
    """Main function"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        # Watch mode - refresh every 5 seconds
        try:
            while True:
                print_dashboard()
                time.sleep(5)
        except KeyboardInterrupt:
            print(f"\n{C.CYAN}Dashboard stopped. GORUNFREE!!! 🔥{C.END}\n")
    else:
        # Single run
        print_dashboard()

if __name__ == "__main__":
    main()

