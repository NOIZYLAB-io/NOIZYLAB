#!/usr/bin/env python3
"""
🔥 MC96 HOT ROD TERMINAL 🔥
═══════════════════════════════════════════════════════════════
The Ultimate Supercharged Terminal for NOIZYLAB
Zero Latency • Voice Ready • AI Powered • Cross-Platform

Usage:
    mc96                    # Launch interactive shell
    mc96 status             # System status
    mc96 speak "hello"      # Voice output
    mc96 ask "question"     # AI response
    mc96 run <command>      # Execute with metrics
    mc96 hp <command>       # Run on HP-OMEN
    mc96 cluster start      # Start all services
═══════════════════════════════════════════════════════════════
"""

import os
import sys
import time
import json
import socket
import subprocess
import threading
import readline
import atexit
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List, Callable
from dataclasses import dataclass, field
from enum import Enum
import shutil

# ══════════════════════════════════════════════════════════════
# ANSI COLORS - CYBERPUNK THEME
# ══════════════════════════════════════════════════════════════

class Colors:
    """Cyberpunk terminal colors"""
    # Core colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    BLINK = "\033[5m"
    
    # Neon palette
    NEON_CYAN = "\033[96m"
    NEON_GREEN = "\033[92m"
    NEON_MAGENTA = "\033[95m"
    NEON_YELLOW = "\033[93m"
    NEON_RED = "\033[91m"
    NEON_BLUE = "\033[94m"
    WHITE = "\033[97m"
    
    # Background
    BG_BLACK = "\033[40m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    
    # Semantic
    SUCCESS = NEON_GREEN
    ERROR = NEON_RED
    WARNING = NEON_YELLOW
    INFO = NEON_CYAN
    ACCENT = NEON_MAGENTA
    
    @classmethod
    def gradient(cls, text: str, start: str = "cyan", end: str = "magenta") -> str:
        """Apply gradient effect to text"""
        colors = [cls.NEON_CYAN, cls.NEON_BLUE, cls.NEON_MAGENTA]
        result = []
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result.append(f"{color}{char}")
        return "".join(result) + cls.RESET

C = Colors  # Shorthand

# ══════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════

@dataclass
class MC96Config:
    """Terminal configuration"""
    # Paths
    noizylab_root: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB")
    gabriel_root: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB" / "GABRIEL")
    mc96_root: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB" / "MC96")
    history_file: Path = field(default_factory=lambda: Path.home() / ".mc96_history")
    
    # Network
    mc96_server_port: int = 5174
    grpc_port: int = 50051
    hp_omen_ip: str = "192.168.1.100"  # Update with actual IP
    hp_omen_user: str = "User"
    
    # Features
    voice_enabled: bool = True
    ai_enabled: bool = True
    metrics_enabled: bool = True
    
    # Appearance
    prompt_style: str = "cyberpunk"  # cyberpunk, minimal, classic
    show_latency: bool = True
    show_git_branch: bool = True

CONFIG = MC96Config()

# ══════════════════════════════════════════════════════════════
# SYSTEM METRICS
# ══════════════════════════════════════════════════════════════

@dataclass
class SystemMetrics:
    """Real-time system metrics"""
    cpu_percent: float = 0.0
    memory_percent: float = 0.0
    disk_percent: float = 0.0
    network_latency_ms: float = 0.0
    last_update: datetime = field(default_factory=datetime.now)
    
    def update(self) -> None:
        """Update metrics from system"""
        try:
            # CPU via top (quick sample)
            result = subprocess.run(
                ["ps", "-A", "-o", "%cpu"],
                capture_output=True, text=True, timeout=2
            )
            if result.returncode == 0:
                cpus = [float(x) for x in result.stdout.strip().split('\n')[1:] if x.strip()]
                self.cpu_percent = min(sum(cpus[:10]), 100.0)  # Top 10 processes
            
            # Memory via vm_stat
            result = subprocess.run(
                ["vm_stat"],
                capture_output=True, text=True, timeout=2
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                stats: Dict[str, int] = {}
                for line in lines[1:]:
                    if ':' in line:
                        key, val = line.split(':')
                        val = val.strip().rstrip('.')
                        if val.isdigit():
                            stats[key.strip()] = int(val)
                
                page_size = 16384  # Apple Silicon page size
                free = stats.get('Pages free', 0) * page_size
                active = stats.get('Pages active', 0) * page_size
                inactive = stats.get('Pages inactive', 0) * page_size
                wired = stats.get('Pages wired down', 0) * page_size
                total = free + active + inactive + wired
                if total > 0:
                    self.memory_percent = ((active + wired) / total) * 100
            
            # Disk
            result = subprocess.run(
                ["df", "-h", "/"],
                capture_output=True, text=True, timeout=2
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    parts = lines[1].split()
                    if len(parts) >= 5:
                        self.disk_percent = float(parts[4].rstrip('%'))
            
            # Network latency (ping localhost)
            start = time.perf_counter()
            socket.create_connection(("127.0.0.1", 22), timeout=0.1).close()
            self.network_latency_ms = (time.perf_counter() - start) * 1000
        except Exception:
            self.network_latency_ms = 1.0  # Default
        
        self.last_update = datetime.now()
    
    def format_bar(self, value: float, width: int = 10, color: str = C.NEON_GREEN) -> str:
        """Create a progress bar"""
        filled = int(value / 100 * width)
        empty = width - filled
        if value > 80:
            color = C.NEON_RED
        elif value > 60:
            color = C.NEON_YELLOW
        return f"{color}{'█' * filled}{'░' * empty}{C.RESET}"

METRICS = SystemMetrics()

# ══════════════════════════════════════════════════════════════
# COMMAND REGISTRY
# ══════════════════════════════════════════════════════════════

class CommandRegistry:
    """Registry of all MC96 commands"""
    
    def __init__(self) -> None:
        self.commands: Dict[str, Callable[..., Any]] = {}
        self.aliases: Dict[str, str] = {}
        self.help_texts: Dict[str, str] = {}
    
    def register(
        self, 
        name: str, 
        func: Callable[..., Any], 
        help_text: str = "",
        aliases: Optional[List[str]] = None
    ) -> None:
        """Register a command"""
        self.commands[name] = func
        self.help_texts[name] = help_text
        if aliases:
            for alias in aliases:
                self.aliases[alias] = name
    
    def execute(self, name: str, args: List[str]) -> Any:
        """Execute a command by name"""
        # Check aliases
        if name in self.aliases:
            name = self.aliases[name]
        
        if name in self.commands:
            return self.commands[name](args)
        return None
    
    def get_completions(self, text: str) -> List[str]:
        """Get command completions"""
        all_names = list(self.commands.keys()) + list(self.aliases.keys())
        return [n for n in all_names if n.startswith(text)]

REGISTRY = CommandRegistry()

# ══════════════════════════════════════════════════════════════
# CORE COMMANDS
# ══════════════════════════════════════════════════════════════

def cmd_status(args: List[str]) -> None:
    """Show system status"""
    METRICS.update()
    
    # Header
    print(f"\n{C.NEON_CYAN}{'═' * 60}{C.RESET}")
    print(f"{C.BOLD}{C.NEON_MAGENTA}  🔥 MC96 HOT ROD TERMINAL - SYSTEM STATUS{C.RESET}")
    print(f"{C.NEON_CYAN}{'═' * 60}{C.RESET}\n")
    
    # Machine info
    hostname = socket.gethostname()
    print(f"  {C.NEON_CYAN}MACHINE:{C.RESET}  {hostname}")
    print(f"  {C.NEON_CYAN}TIME:{C.RESET}     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  {C.NEON_CYAN}UPTIME:{C.RESET}   {get_uptime()}")
    print()
    
    # Metrics
    print(f"  {C.NEON_YELLOW}CPU:{C.RESET}      {METRICS.format_bar(METRICS.cpu_percent)} {METRICS.cpu_percent:.1f}%")
    print(f"  {C.NEON_YELLOW}MEMORY:{C.RESET}   {METRICS.format_bar(METRICS.memory_percent)} {METRICS.memory_percent:.1f}%")
    print(f"  {C.NEON_YELLOW}DISK:{C.RESET}     {METRICS.format_bar(METRICS.disk_percent)} {METRICS.disk_percent:.1f}%")
    print(f"  {C.NEON_YELLOW}LATENCY:{C.RESET}  {C.NEON_GREEN}{METRICS.network_latency_ms:.2f}ms{C.RESET}")
    print()
    
    # Services
    print(f"  {C.NEON_MAGENTA}SERVICES:{C.RESET}")
    services = [
        ("MC96 Server", CONFIG.mc96_server_port, check_port(CONFIG.mc96_server_port)),
        ("gRPC Bridge", CONFIG.grpc_port, check_port(CONFIG.grpc_port)),
        ("SSH", 22, check_port(22)),
    ]
    for name, port, status in services:
        icon = f"{C.NEON_GREEN}●{C.RESET}" if status else f"{C.NEON_RED}○{C.RESET}"
        print(f"    {icon} {name:<15} (:{port})")
    
    print(f"\n{C.NEON_CYAN}{'═' * 60}{C.RESET}\n")

def cmd_speak(args: List[str]) -> None:
    """Speak text using TitanHive voice"""
    if not args:
        print(f"{C.ERROR}Usage: speak <text>{C.RESET}")
        return
    
    text = " ".join(args)
    voice_path = CONFIG.gabriel_root / "titanhive" / "voice.py"
    
    if voice_path.exists():
        print(f"{C.INFO}🔊 Speaking: {text}{C.RESET}")
        subprocess.run([sys.executable, str(voice_path), "speak", text])
    else:
        # Fallback to macOS say
        print(f"{C.INFO}🔊 Speaking (macOS): {text}{C.RESET}")
        subprocess.run(["say", "-v", "Samantha", text])

def cmd_ask(args: List[str]) -> None:
    """Ask AI a question"""
    if not args:
        print(f"{C.ERROR}Usage: ask <question>{C.RESET}")
        return
    
    question = " ".join(args)
    print(f"{C.INFO}🤖 Processing: {question}{C.RESET}")
    
    # Try TitanHive AI first
    voice_path = CONFIG.gabriel_root / "titanhive" / "voice.py"
    if voice_path.exists():
        result = subprocess.run(
            [sys.executable, str(voice_path), "ai", question],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"\n{C.NEON_MAGENTA}GABRIEL:{C.RESET} {result.stdout.strip()}")
            return
    
    print(f"{C.WARNING}AI not available. Configure API keys in TitanHive.{C.RESET}")

def cmd_run(args: List[str]) -> None:
    """Run a command with metrics"""
    if not args:
        print(f"{C.ERROR}Usage: run <command>{C.RESET}")
        return
    
    cmd = " ".join(args)
    print(f"{C.DIM}$ {cmd}{C.RESET}")
    
    start = time.perf_counter()
    result = subprocess.run(cmd, shell=True)
    elapsed = time.perf_counter() - start
    
    status_icon = f"{C.SUCCESS}✓{C.RESET}" if result.returncode == 0 else f"{C.ERROR}✗{C.RESET}"
    print(f"\n{status_icon} Exit: {result.returncode} | Time: {elapsed:.3f}s")

def cmd_hp(args: List[str]) -> None:
    """Run command on HP-OMEN via SSH"""
    if not args:
        print(f"{C.ERROR}Usage: hp <command>{C.RESET}")
        return
    
    cmd = " ".join(args)
    print(f"{C.INFO}🖥️  HP-OMEN > {cmd}{C.RESET}")
    
    # Try SSH
    ssh_cmd = f"ssh {CONFIG.hp_omen_user}@{CONFIG.hp_omen_ip} '{cmd}'"
    subprocess.run(ssh_cmd, shell=True)

def cmd_cluster(args: List[str]) -> None:
    """Manage NOIZYLAB cluster"""
    action = args[0] if args else "status"
    
    launcher = CONFIG.noizylab_root / "cluster_launcher.py"
    if launcher.exists():
        subprocess.run([sys.executable, str(launcher), action])
    else:
        print(f"{C.WARNING}Cluster launcher not found at {launcher}{C.RESET}")
        print(f"{C.INFO}Available actions: start, stop, status, logs{C.RESET}")

def cmd_gabriel(args: List[str]) -> None:
    """Launch GABRIEL agent"""
    gabriel_script = CONFIG.gabriel_root / "start_gabriel.sh"
    if gabriel_script.exists():
        print(f"{C.SUCCESS}🚀 Launching GABRIEL...{C.RESET}")
        subprocess.run(["bash", str(gabriel_script)])
    else:
        print(f"{C.WARNING}GABRIEL start script not found{C.RESET}")

def cmd_server(args: List[str]) -> None:
    """Start MC96 server"""
    action = args[0] if args else "start"
    server_path = CONFIG.gabriel_root / "mc96_server.py"
    
    if action == "start":
        print(f"{C.SUCCESS}🔥 Starting MC96 Server on port {CONFIG.mc96_server_port}...{C.RESET}")
        subprocess.Popen(
            [sys.executable, str(server_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(1)
        if check_port(CONFIG.mc96_server_port):
            print(f"{C.SUCCESS}✓ Server running at http://localhost:{CONFIG.mc96_server_port}{C.RESET}")
        else:
            print(f"{C.ERROR}✗ Server failed to start{C.RESET}")
    elif action == "stop":
        subprocess.run(["pkill", "-f", "mc96_server.py"])
        print(f"{C.INFO}Server stopped{C.RESET}")

def cmd_hotrod(args: List[str]) -> None:
    """Show hot rod shortcuts"""
    print(f"""
{C.NEON_CYAN}{'═' * 60}{C.RESET}
{C.BOLD}{C.NEON_MAGENTA}  🔥 HOT ROD SHORTCUTS{C.RESET}
{C.NEON_CYAN}{'═' * 60}{C.RESET}

  {C.NEON_YELLOW}QUICK COMMANDS:{C.RESET}
    {C.NEON_GREEN}s{C.RESET}      → status          System status
    {C.NEON_GREEN}sp{C.RESET}     → speak           Voice output
    {C.NEON_GREEN}a{C.RESET}      → ask             AI query
    {C.NEON_GREEN}r{C.RESET}      → run             Run with metrics
    {C.NEON_GREEN}g{C.RESET}      → gabriel         Launch GABRIEL
    {C.NEON_GREEN}sv{C.RESET}     → server start    Start MC96 server
    {C.NEON_GREEN}c{C.RESET}      → cluster         Cluster management

  {C.NEON_YELLOW}NETWORK:{C.RESET}
    {C.NEON_GREEN}hp{C.RESET}     → hp <cmd>        Run on HP-OMEN
    {C.NEON_GREEN}ping{C.RESET}   → ping            Network test
    {C.NEON_GREEN}ports{C.RESET}  → ports           Show open ports

  {C.NEON_YELLOW}SYSTEM:{C.RESET}
    {C.NEON_GREEN}top{C.RESET}    → htop/top        Process viewer
    {C.NEON_GREEN}df{C.RESET}     → disk            Disk usage
    {C.NEON_GREEN}mem{C.RESET}    → memory          Memory info
    {C.NEON_GREEN}gpu{C.RESET}    → gpu             GPU status

  {C.NEON_YELLOW}DEVELOPMENT:{C.RESET}
    {C.NEON_GREEN}git{C.RESET}    → git status      Git status
    {C.NEON_GREEN}pull{C.RESET}   → git pull        Git pull
    {C.NEON_GREEN}push{C.RESET}   → git push        Git push
    {C.NEON_GREEN}code{C.RESET}   → code .          Open VS Code

{C.NEON_CYAN}{'═' * 60}{C.RESET}
""")

def cmd_ports(args: List[str]) -> None:
    """Show listening ports"""
    print(f"{C.INFO}🔌 Listening ports:{C.RESET}\n")
    subprocess.run(["lsof", "-i", "-P", "-n", "|", "grep", "LISTEN"], shell=True)

def cmd_gpu(args: List[str]) -> None:
    """Show GPU status"""
    print(f"{C.INFO}🎮 GPU Status:{C.RESET}\n")
    # macOS - show Metal devices
    result = subprocess.run(
        ["system_profiler", "SPDisplaysDataType"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        lines = result.stdout.split('\n')
        for line in lines:
            if any(x in line.lower() for x in ['chipset', 'vram', 'metal', 'gpu']):
                print(f"  {line.strip()}")

def cmd_top(args: List[str]) -> None:
    """Open process viewer"""
    if shutil.which("htop"):
        subprocess.run(["htop"])
    else:
        subprocess.run(["top"])

def cmd_disk(args: List[str]) -> None:
    """Show disk usage"""
    print(f"{C.INFO}💾 Disk Usage:{C.RESET}\n")
    subprocess.run(["df", "-h"])

def cmd_mem(args: List[str]) -> None:
    """Show memory info"""
    print(f"{C.INFO}🧠 Memory Info:{C.RESET}\n")
    
    result = subprocess.run(
        ["sysctl", "-n", "hw.memsize"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        total_bytes = int(result.stdout.strip())
        total_gb = total_bytes / (1024**3)
        print(f"  Total RAM: {total_gb:.1f} GB")
    
    METRICS.update()
    print(f"  Used: {METRICS.memory_percent:.1f}%")

def cmd_help(args: List[str]) -> None:
    """Show help"""
    print(f"""
{C.NEON_CYAN}{'═' * 60}{C.RESET}
{C.BOLD}{C.NEON_MAGENTA}  🔥 MC96 HOT ROD TERMINAL - HELP{C.RESET}
{C.NEON_CYAN}{'═' * 60}{C.RESET}

  {C.NEON_YELLOW}COMMANDS:{C.RESET}
    status      System status with metrics
    speak       Text-to-speech output
    ask         Ask AI a question
    run         Execute command with timing
    hp          Execute on HP-OMEN
    cluster     Manage NOIZYLAB cluster
    gabriel     Launch GABRIEL agent
    server      Start/stop MC96 server
    hotrod      Show shortcut reference
    help        This help message
    exit/quit   Exit terminal

  {C.NEON_YELLOW}ALIASES:{C.RESET}
    s=status  sp=speak  a=ask  r=run  g=gabriel
    sv=server  c=cluster  h=help  q=quit

  {C.NEON_YELLOW}PASS-THROUGH:{C.RESET}
    Any unrecognized command is passed to system shell.
    Example: ls -la, git status, python3 script.py

{C.NEON_CYAN}{'═' * 60}{C.RESET}
""")

def cmd_clear(args: List[str]) -> None:
    """Clear screen"""
    os.system('clear')
    show_banner()

def cmd_exit(args: List[str]) -> None:
    """Exit terminal"""
    print(f"\n{C.NEON_MAGENTA}👋 MC96 signing off...{C.RESET}\n")
    sys.exit(0)

def cmd_diag(args: List[str]) -> None:
    """Diagnostic system - find and source problems"""
    # Import diagnostics module
    try:
        script_dir = Path(__file__).parent
        sys.path.insert(0, str(script_dir))
        from mc96_diagnostics import get_engine, cmd_list_reports, cmd_show_report, cmd_test, install_global_handler
        
        if not args:
            print(f"""
{C.NEON_CYAN}{'═' * 60}{C.RESET}
{C.BOLD}{C.NEON_MAGENTA}  🔍 MC96 DIAGNOSTIC ENGINE{C.RESET}
{C.NEON_CYAN}{'═' * 60}{C.RESET}

  {C.NEON_YELLOW}COMMANDS:{C.RESET}
    diag list       List all diagnostic reports
    diag show <id>  Show specific report details
    diag test       Test the diagnostic system
    diag install    Install global exception handler
    diag last       Show most recent report

  {C.NEON_YELLOW}IN PYTHON:{C.RESET}
    from mc96_diagnostics import wtf, diagnose
    
    try:
        risky_code()
    except Exception as e:
        wtf(e)  # Full diagnostic report

{C.NEON_CYAN}{'═' * 60}{C.RESET}
""")
            return
        
        subcmd = args[0]
        subargs = args[1:]
        
        if subcmd == "list":
            cmd_list_reports(subargs)
        elif subcmd == "show":
            cmd_show_report(subargs)
        elif subcmd == "test":
            cmd_test(subargs)
        elif subcmd == "install":
            install_global_handler()
        elif subcmd == "last":
            # Show most recent report
            engine = get_engine()
            reports = sorted(engine.config.report_dir.glob("MC96-*.json"), reverse=True)
            if reports:
                cmd_show_report([reports[0].stem])
            else:
                print(f"{C.WARNING}No diagnostic reports found.{C.RESET}")
        else:
            print(f"{C.ERROR}Unknown diagnostic command: {subcmd}{C.RESET}")
    except ImportError as e:
        print(f"{C.ERROR}Diagnostic module not found: {e}{C.RESET}")
        print(f"{C.INFO}Ensure mc96_diagnostics.py is in the same directory.{C.RESET}")

def cmd_wtf(args: List[str]) -> None:
    """Quick problem diagnosis - run a command and capture any errors"""
    if not args:
        print(f"{C.ERROR}Usage: wtf <command>{C.RESET}")
        print(f"{C.INFO}Example: wtf python3 broken_script.py{C.RESET}")
        return
    
    cmd = " ".join(args)
    print(f"{C.INFO}🔍 Running with diagnostic capture: {cmd}{C.RESET}\n")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            # Problem detected - run diagnostics
            print(f"{C.ERROR}Command failed with exit code {result.returncode}{C.RESET}\n")
            
            if result.stderr:
                print(f"{C.RED}STDERR:{C.RESET}")
                print(result.stderr)
            
            # Try to capture with diagnostics
            try:
                script_dir = Path(__file__).parent
                sys.path.insert(0, str(script_dir))
                from mc96_diagnostics import diagnose, DiagnosticEngine
                
                engine = DiagnosticEngine()
                report = engine.diagnose(
                    title=f"Command Failed: {cmd}",
                    description=f"Exit code: {result.returncode}\nStderr: {result.stderr}"
                )
                report.error_type = "CommandFailure"
                report.error_message = result.stderr[:200] if result.stderr else "Unknown error"
                
                print(engine.format_summary(report))
            except ImportError:
                print(f"{C.WARNING}Diagnostic module not available{C.RESET}")
        else:
            print(f"{C.SUCCESS}✓ Command completed successfully{C.RESET}")
            if result.stdout:
                print(result.stdout)
    except Exception as e:
        print(f"{C.ERROR}Error running command: {e}{C.RESET}")

# ══════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════

def check_port(port: int) -> bool:
    """Check if a port is open"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            return s.connect_ex(('127.0.0.1', port)) == 0
    except Exception:
        return False

def get_uptime() -> str:
    """Get system uptime"""
    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            # Parse uptime output
            output = result.stdout.strip()
            if "up" in output:
                start = output.find("up") + 3
                end = output.find(",", start)
                if end == -1:
                    end = output.find("user") - 2
                return output[start:end].strip()
    except Exception:
        pass
    return "unknown"

def get_git_branch() -> Optional[str]:
    """Get current git branch"""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True,
            cwd=str(CONFIG.gabriel_root)
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None

def show_banner() -> None:
    """Show startup banner"""
    banner = f"""
{C.NEON_CYAN}╔══════════════════════════════════════════════════════════════╗{C.RESET}
{C.NEON_CYAN}║{C.RESET}  {C.BOLD}{Colors.gradient("🔥 MC96 HOT ROD TERMINAL 🔥")}{C.RESET}                           {C.NEON_CYAN}║{C.RESET}
{C.NEON_CYAN}║{C.RESET}  {C.DIM}Zero Latency • Voice Ready • AI Powered{C.RESET}                  {C.NEON_CYAN}║{C.RESET}
{C.NEON_CYAN}╠══════════════════════════════════════════════════════════════╣{C.RESET}
{C.NEON_CYAN}║{C.RESET}  Type {C.NEON_GREEN}help{C.RESET} for commands • {C.NEON_GREEN}hotrod{C.RESET} for shortcuts           {C.NEON_CYAN}║{C.RESET}
{C.NEON_CYAN}╚══════════════════════════════════════════════════════════════╝{C.RESET}
"""
    print(banner)

def get_prompt() -> str:
    """Generate the prompt string"""
    hostname = socket.gethostname().split('.')[0]
    cwd = os.getcwd()
    home = str(Path.home())
    
    # Shorten path
    if cwd.startswith(home):
        cwd = "~" + cwd[len(home):]
    
    # Git branch
    branch = ""
    if CONFIG.show_git_branch:
        b = get_git_branch()
        if b:
            branch = f" {C.NEON_MAGENTA}({b}){C.RESET}"
    
    # Latency indicator
    latency = ""
    if CONFIG.show_latency:
        METRICS.update()
        ms = METRICS.network_latency_ms
        color = C.NEON_GREEN if ms < 5 else C.NEON_YELLOW if ms < 20 else C.NEON_RED
        latency = f" {color}⚡{ms:.0f}ms{C.RESET}"
    
    # Build prompt
    return f"{C.NEON_CYAN}[MC96]{C.RESET} {C.NEON_GREEN}{hostname}{C.RESET}:{C.NEON_YELLOW}{cwd}{C.RESET}{branch}{latency}\n{C.NEON_MAGENTA}❯{C.RESET} "

# ══════════════════════════════════════════════════════════════
# REGISTER COMMANDS
# ══════════════════════════════════════════════════════════════

def register_commands() -> None:
    """Register all commands"""
    REGISTRY.register("status", cmd_status, "System status", ["s"])
    REGISTRY.register("speak", cmd_speak, "Text-to-speech", ["sp", "say"])
    REGISTRY.register("ask", cmd_ask, "Ask AI", ["a", "ai"])
    REGISTRY.register("run", cmd_run, "Run with metrics", ["r"])
    REGISTRY.register("hp", cmd_hp, "Run on HP-OMEN")
    REGISTRY.register("cluster", cmd_cluster, "Cluster management", ["c"])
    REGISTRY.register("gabriel", cmd_gabriel, "Launch GABRIEL", ["g"])
    REGISTRY.register("server", cmd_server, "MC96 server", ["sv"])
    REGISTRY.register("hotrod", cmd_hotrod, "Shortcuts reference", ["hr"])
    REGISTRY.register("ports", cmd_ports, "Show ports")
    REGISTRY.register("gpu", cmd_gpu, "GPU status")
    REGISTRY.register("top", cmd_top, "Process viewer")
    REGISTRY.register("disk", cmd_disk, "Disk usage", ["df"])
    REGISTRY.register("mem", cmd_mem, "Memory info")
    REGISTRY.register("diag", cmd_diag, "Diagnostic system", ["diagnose", "d"])
    REGISTRY.register("wtf", cmd_wtf, "Run with error capture")
    REGISTRY.register("help", cmd_help, "Show help", ["h", "?"])
    REGISTRY.register("clear", cmd_clear, "Clear screen", ["cls"])
    REGISTRY.register("exit", cmd_exit, "Exit terminal", ["quit", "q"])

# ══════════════════════════════════════════════════════════════
# READLINE / TAB COMPLETION
# ══════════════════════════════════════════════════════════════

def setup_readline() -> None:
    """Setup readline with history and completion"""
    # History
    if CONFIG.history_file.exists():
        readline.read_history_file(str(CONFIG.history_file))
    readline.set_history_length(1000)
    atexit.register(readline.write_history_file, str(CONFIG.history_file))
    
    # Tab completion
    def completer(text: str, state: int) -> Optional[str]:
        options = REGISTRY.get_completions(text)
        if state < len(options):
            return options[state]
        return None
    
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

# ══════════════════════════════════════════════════════════════
# MAIN LOOP
# ══════════════════════════════════════════════════════════════

def main() -> None:
    """Main entry point"""
    register_commands()
    
    # Handle single command mode
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        args = sys.argv[2:]
        
        result = REGISTRY.execute(cmd, args)
        if result is None and cmd not in REGISTRY.commands and cmd not in REGISTRY.aliases:
            # Pass through to shell
            subprocess.run(" ".join(sys.argv[1:]), shell=True)
        return
    
    # Interactive mode
    setup_readline()
    show_banner()
    
    while True:
        try:
            line = input(get_prompt()).strip()
            
            if not line:
                continue
            
            parts = line.split()
            cmd = parts[0]
            args = parts[1:]
            
            # Try registered command
            result = REGISTRY.execute(cmd, args)
            
            # Fall through to shell
            if result is None and cmd not in REGISTRY.commands and cmd not in REGISTRY.aliases:
                subprocess.run(line, shell=True)
        
        except KeyboardInterrupt:
            print(f"\n{C.DIM}(Ctrl+C - type 'exit' to quit){C.RESET}")
        except EOFError:
            cmd_exit([])
        except Exception as e:
            print(f"{C.ERROR}Error: {e}{C.RESET}")

if __name__ == "__main__":
    main()
