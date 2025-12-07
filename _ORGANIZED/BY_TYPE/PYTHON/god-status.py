#!/usr/bin/env python3
"""
GOD Performance Status Monitor
CB_01 - Fish Music Inc
Real-time system performance tracking for Mac Studio M2 Ultra 192GB
GORUNFREE! 🎸🔥
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Colors for terminal output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    BOLD = '\033[1m'
    NC = '\033[0m'  # No Color

def clear_screen():
    """Clear terminal screen"""
    subprocess.run(['clear'])

def run_command(cmd: str) -> str:
    """Run shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Command timeout"
    except Exception as e:
        return f"Error: {e}"

def get_cpu_info() -> dict:
    """Get CPU information"""
    logical_cpus = run_command("sysctl -n hw.logicalcpu")
    physical_cpus = run_command("sysctl -n hw.physicalcpu")
    cpu_brand = run_command("sysctl -n machdep.cpu.brand_string")

    # Get CPU load averages
    load_avg = run_command("sysctl -n vm.loadavg").replace("{ ", "").replace(" }", "")

    return {
        'logical': logical_cpus,
        'physical': physical_cpus,
        'brand': cpu_brand,
        'load_avg': load_avg
    }

def get_memory_info() -> dict:
    """Get memory information"""
    # Total memory
    total_bytes = int(run_command("sysctl -n hw.memsize"))
    total_gb = total_bytes / (1024**3)

    # Memory pressure
    mem_pressure = run_command("memory_pressure 2>&1 | head -5")

    # vm_stat for detailed memory info
    vm_output = run_command("vm_stat")

    # Parse vm_stat for pages
    free_pages = 0
    active_pages = 0
    inactive_pages = 0
    wired_pages = 0

    for line in vm_output.split('\n'):
        if 'Pages free' in line:
            free_pages = int(line.split(':')[1].strip().replace('.', ''))
        elif 'Pages active' in line:
            active_pages = int(line.split(':')[1].strip().replace('.', ''))
        elif 'Pages inactive' in line:
            inactive_pages = int(line.split(':')[1].strip().replace('.', ''))
        elif 'Pages wired down' in line:
            wired_pages = int(line.split(':')[1].strip().replace('.', ''))

    # Calculate memory usage (pages * 4KB)
    page_size = 4096
    free_gb = (free_pages * page_size) / (1024**3)
    used_gb = total_gb - free_gb
    used_percent = (used_gb / total_gb) * 100 if total_gb > 0 else 0

    return {
        'total_gb': total_gb,
        'used_gb': used_gb,
        'free_gb': free_gb,
        'used_percent': used_percent,
        'pressure': mem_pressure
    }

def get_disk_info() -> dict:
    """Get disk usage information"""
    df_output = run_command("df -h / | tail -1")
    parts = df_output.split()

    if len(parts) >= 5:
        return {
            'total': parts[1],
            'used': parts[2],
            'available': parts[3],
            'percent': parts[4],
            'mount': parts[8] if len(parts) > 8 else '/'
        }
    return {}

def get_network_info() -> dict:
    """Get network information"""
    # Try both Wi-Fi and Ethernet
    dns_wifi = run_command("networksetup -getdnsservers Wi-Fi 2>/dev/null")
    dns_ethernet = run_command("networksetup -getdnsservers Ethernet 2>/dev/null")

    dns = dns_wifi if dns_wifi and "not" not in dns_wifi.lower() else dns_ethernet

    # Check if Cloudflare DNS is active
    cloudflare_active = "1.1.1.1" in dns

    return {
        'dns': dns,
        'cloudflare_active': cloudflare_active
    }

def get_uptime() -> str:
    """Get system uptime"""
    return run_command("uptime")

def get_top_processes() -> list:
    """Get top CPU-consuming processes"""
    output = run_command("top -l 1 -o cpu -n 5 | tail -6")
    return output.split('\n')[1:]  # Skip header

def display_status(continuous: bool = False):
    """Display comprehensive system status"""

    while True:
        clear_screen()

        # Header
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.NC}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}  🔥 GOD PERFORMANCE STATUS - Mac Studio M2 Ultra{Colors.NC}")
        print(f"{Colors.BOLD}{Colors.CYAN}  Fish Music Inc - CB_01{Colors.NC}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.NC}\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{Colors.CYAN}Snapshot: {Colors.BOLD}{timestamp}{Colors.NC}\n")

        # CPU Information
        print(f"{Colors.BOLD}{Colors.BLUE}⚡ CPU STATUS:{Colors.NC}")
        cpu = get_cpu_info()
        print(f"  Chip: {Colors.GREEN}{cpu['brand']}{Colors.NC}")
        print(f"  Cores: {Colors.GREEN}{cpu['logical']} logical, {cpu['physical']} physical{Colors.NC}")
        print(f"  Load Average: {Colors.YELLOW}{cpu['load_avg']}{Colors.NC}")
        print()

        # Memory Information
        print(f"{Colors.BOLD}{Colors.BLUE}💾 MEMORY STATUS:{Colors.NC}")
        mem = get_memory_info()

        # Color code based on usage
        mem_color = Colors.GREEN
        if mem['used_percent'] > 80:
            mem_color = Colors.RED
        elif mem['used_percent'] > 60:
            mem_color = Colors.YELLOW

        print(f"  Total: {Colors.GREEN}{mem['total_gb']:.1f} GB{Colors.NC}")
        print(f"  Used: {mem_color}{mem['used_gb']:.1f} GB ({mem['used_percent']:.1f}%){Colors.NC}")
        print(f"  Free: {Colors.GREEN}{mem['free_gb']:.1f} GB{Colors.NC}")
        print()

        # Disk Information
        print(f"{Colors.BOLD}{Colors.BLUE}💽 DISK STATUS:{Colors.NC}")
        disk = get_disk_info()
        if disk:
            disk_percent = int(disk['percent'].replace('%', ''))
            disk_color = Colors.GREEN
            if disk_percent > 90:
                disk_color = Colors.RED
            elif disk_percent > 80:
                disk_color = Colors.YELLOW

            print(f"  Total: {Colors.GREEN}{disk['total']}{Colors.NC}")
            print(f"  Used: {disk_color}{disk['used']} ({disk['percent']}){Colors.NC}")
            print(f"  Available: {Colors.GREEN}{disk['available']}{Colors.NC}")
        print()

        # Network Information
        print(f"{Colors.BOLD}{Colors.BLUE}🌐 NETWORK STATUS:{Colors.NC}")
        network = get_network_info()
        if network['cloudflare_active']:
            print(f"  DNS: {Colors.GREEN}✓ Cloudflare Optimized (1.1.1.1){Colors.NC}")
        else:
            dns_display = network['dns'].split('\n')[0] if network['dns'] else "Unknown"
            print(f"  DNS: {Colors.YELLOW}{dns_display}{Colors.NC}")
        print()

        # Top Processes
        print(f"{Colors.BOLD}{Colors.BLUE}🔝 TOP CPU PROCESSES:{Colors.NC}")
        processes = get_top_processes()
        for proc in processes[:5]:
            if proc.strip():
                print(f"  {Colors.CYAN}{proc.strip()}{Colors.NC}")
        print()

        # System Uptime
        print(f"{Colors.BOLD}{Colors.BLUE}⏱️  UPTIME:{Colors.NC}")
        print(f"  {Colors.GREEN}{get_uptime()}{Colors.NC}")
        print()

        # Performance Assessment
        print(f"{Colors.BOLD}{Colors.BLUE}📊 PERFORMANCE ASSESSMENT:{Colors.NC}")

        issues = []
        if mem['used_percent'] > 80:
            issues.append(f"{Colors.YELLOW}⚠️  Memory usage high (>80%){Colors.NC}")
        if disk and disk_percent > 90:
            issues.append(f"{Colors.YELLOW}⚠️  Disk space critical (>90%){Colors.NC}")
        if not network['cloudflare_active']:
            issues.append(f"{Colors.YELLOW}ℹ️  DNS not optimized (run god-hotrod.sh){Colors.NC}")

        if not issues:
            print(f"  {Colors.GREEN}✅ All systems optimal - GOD singing like a lark 🎵{Colors.NC}")
        else:
            for issue in issues:
                print(f"  {issue}")

        print()

        # Footer
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.NC}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}GORUNFREE! 🎸🔥{Colors.NC}")

        if continuous:
            print(f"\n{Colors.YELLOW}Refreshing in 5 seconds... (Ctrl+C to exit){Colors.NC}")
            time.sleep(5)
        else:
            break

def save_baseline():
    """Save performance baseline for comparison"""
    baseline_dir = Path.home() / ".god-performance"
    baseline_dir.mkdir(exist_ok=True)

    baseline_file = baseline_dir / f"baseline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(baseline_file, 'w') as f:
        f.write(f"GOD Performance Baseline - {datetime.now()}\n")
        f.write("=" * 70 + "\n\n")

        cpu = get_cpu_info()
        f.write(f"CPU:\n")
        f.write(f"  Cores: {cpu['logical']} logical, {cpu['physical']} physical\n")
        f.write(f"  Load: {cpu['load_avg']}\n\n")

        mem = get_memory_info()
        f.write(f"Memory:\n")
        f.write(f"  Total: {mem['total_gb']:.1f} GB\n")
        f.write(f"  Used: {mem['used_gb']:.1f} GB ({mem['used_percent']:.1f}%)\n\n")

        disk = get_disk_info()
        if disk:
            f.write(f"Disk:\n")
            f.write(f"  Total: {disk['total']}\n")
            f.write(f"  Used: {disk['used']} ({disk['percent']})\n\n")

        network = get_network_info()
        f.write(f"Network:\n")
        f.write(f"  Cloudflare DNS: {network['cloudflare_active']}\n\n")

        f.write(f"Uptime:\n")
        f.write(f"  {get_uptime()}\n")

    print(f"{Colors.GREEN}✅ Baseline saved: {baseline_file}{Colors.NC}")
    print(f"{Colors.CYAN}Use this for before/after optimization comparison{Colors.NC}")

def main():
    """Main execution"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--continuous" or sys.argv[1] == "-c":
            display_status(continuous=True)
        elif sys.argv[1] == "--baseline" or sys.argv[1] == "-b":
            save_baseline()
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(f"{Colors.BOLD}GOD Performance Status Monitor{Colors.NC}")
            print(f"\nUsage:")
            print(f"  {Colors.CYAN}python god-status.py{Colors.NC}              # Single snapshot")
            print(f"  {Colors.CYAN}python god-status.py -c{Colors.NC}           # Continuous monitoring")
            print(f"  {Colors.CYAN}python god-status.py -b{Colors.NC}           # Save baseline")
            print(f"  {Colors.CYAN}python god-status.py -h{Colors.NC}           # Show help")
            print(f"\n{Colors.BOLD}GORUNFREE! 🎸🔥{Colors.NC}")
        else:
            print(f"{Colors.RED}Unknown option: {sys.argv[1]}{Colors.NC}")
            print(f"Use --help for usage information")
    else:
        display_status(continuous=False)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Monitoring stopped{Colors.NC}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}GORUNFREE! 🎸🔥{Colors.NC}\n")
        sys.exit(0)
