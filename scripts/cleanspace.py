#!/usr/bin/env python3
"""
🧹 NOIZYLAB CLEANSPACE - DIAGNOSTIC ENGINE
═══════════════════════════════════════════════════════════════
The Universal Problem Sourcer for NOIZYLAB

When something breaks and can't be fixed automatically,
this system captures EVERYTHING needed to source the problem.

CLEANSPACE FEATURES:
- Stack trace analysis
- Log aggregation  
- System state snapshot
- Network diagnostics
- Dependency analysis
- Git state capture
- Environment diff
- AI-powered root cause analysis
- Cross-machine diagnostics (M2 Ultra, HP-OMEN, Mac Pro)

Usage:
    cleanspace diag              # Interactive diagnostic menu
    cleanspace wtf <cmd>         # Run command with error capture
    cleanspace report            # Generate full system report
    cleanspace heal              # Auto-fix common issues
═══════════════════════════════════════════════════════════════
"""

import os
import sys
import json
import socket
import subprocess
import traceback
import platform
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum
import shutil

# ══════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════

class DiagnosticLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    FATAL = "fatal"

class ProblemCategory(Enum):
    UNKNOWN = "unknown"
    NETWORK = "network"
    FILESYSTEM = "filesystem"
    PERMISSION = "permission"
    DEPENDENCY = "dependency"
    CONFIGURATION = "configuration"
    RUNTIME = "runtime"
    MEMORY = "memory"
    HARDWARE = "hardware"
    EXTERNAL_SERVICE = "external_service"
    CODE_BUG = "code_bug"
    ENVIRONMENT = "environment"

@dataclass
class CleanspaceConfig:
    """CLEANSPACE configuration"""
    # Paths - NOIZYLAB root level
    noizylab_root: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB")
    report_dir: Path = field(default_factory=lambda: Path.home() / ".noizylab" / "cleanspace" / "diagnostics")
    log_dir: Path = field(default_factory=lambda: Path.home() / ".noizylab" / "cleanspace" / "logs")
    
    # Limits
    max_reports: int = 100
    max_log_size_mb: int = 50
    
    # Features
    capture_env: bool = True
    capture_logs: bool = True
    capture_network: bool = True
    capture_git: bool = True
    ai_analysis: bool = True
    auto_heal: bool = False
    
    # Network - NOIZYLAB cluster
    machines: Dict[str, str] = field(default_factory=lambda: {
        "m2ultra": "localhost",
        "hp-omen": "192.168.1.100",
        "mac-pro": "192.168.1.101"
    })

CONFIG = CleanspaceConfig()

# ══════════════════════════════════════════════════════════════
# ANSI COLORS - CLEANSPACE THEME
# ══════════════════════════════════════════════════════════════

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # Cleanspace palette
    CLEAN = "\033[92m"      # Green - all good
    WARN = "\033[93m"       # Yellow - warning
    DIRTY = "\033[91m"      # Red - problem
    INFO = "\033[96m"       # Cyan - info
    ACCENT = "\033[95m"     # Magenta - accent
    WHITE = "\033[97m"
    
    # Semantic
    SUCCESS = CLEAN
    ERROR = DIRTY
    WARNING = WARN

# ══════════════════════════════════════════════════════════════
# PROBLEM REPORT
# ══════════════════════════════════════════════════════════════

@dataclass
class ProblemReport:
    """Comprehensive problem report"""
    # Identity
    id: str = ""
    timestamp: str = ""
    hostname: str = ""
    machine_type: str = ""  # m2ultra, hp-omen, mac-pro
    
    # Problem info
    title: str = ""
    description: str = ""
    category: str = "unknown"
    level: str = "error"
    
    # Error details
    error_type: str = ""
    error_message: str = ""
    stack_trace: str = ""
    
    # Location
    file_path: str = ""
    line_number: int = 0
    function_name: str = ""
    code_context: List[str] = field(default_factory=list)
    
    # System state
    system_info: Dict[str, Any] = field(default_factory=dict)
    environment: Dict[str, str] = field(default_factory=dict)
    processes: List[Dict[str, Any]] = field(default_factory=list)
    
    # Dependencies
    python_version: str = ""
    installed_packages: Dict[str, str] = field(default_factory=dict)
    missing_packages: List[str] = field(default_factory=list)
    
    # Network
    network_state: Dict[str, Any] = field(default_factory=dict)
    cluster_status: Dict[str, str] = field(default_factory=dict)
    
    # Git state
    git_state: Dict[str, Any] = field(default_factory=dict)
    
    # Logs
    recent_logs: List[str] = field(default_factory=list)
    
    # Analysis
    probable_causes: List[str] = field(default_factory=list)
    suggested_fixes: List[str] = field(default_factory=list)
    auto_fixable: bool = False
    fix_commands: List[str] = field(default_factory=list)
    
    # Resolution
    resolved: bool = False
    resolution_notes: str = ""

# ══════════════════════════════════════════════════════════════
# CLEANSPACE ENGINE
# ══════════════════════════════════════════════════════════════

class CleanspaceEngine:
    """NOIZYLAB CLEANSPACE Diagnostic Engine"""
    
    def __init__(self, config: Optional[CleanspaceConfig] = None):
        self.config = config or CONFIG
        self.config.report_dir.mkdir(parents=True, exist_ok=True)
        self.config.log_dir.mkdir(parents=True, exist_ok=True)
        self._detect_machine()
    
    def _detect_machine(self) -> str:
        """Detect which NOIZYLAB machine we're on"""
        hostname = socket.gethostname().lower()
        if "m2" in hostname or "ultra" in hostname:
            self.machine_type = "m2ultra"
        elif "omen" in hostname or "hp" in hostname:
            self.machine_type = "hp-omen"
        elif "mac-pro" in hostname or "macpro" in hostname:
            self.machine_type = "mac-pro"
        else:
            self.machine_type = hostname
        return self.machine_type
    
    # ─────────────────────────────────────────────────────────
    # MAIN API
    # ─────────────────────────────────────────────────────────
    
    def diagnose(
        self,
        error: Optional[Exception] = None,
        title: str = "",
        description: str = "",
        context: Optional[Dict[str, Any]] = None
    ) -> ProblemReport:
        """Create comprehensive diagnostic report"""
        report = ProblemReport(
            id=self._generate_id(),
            timestamp=datetime.now().isoformat(),
            hostname=socket.gethostname(),
            machine_type=self.machine_type,
            title=title or "Unknown Problem",
            description=description
        )
        
        # Capture error details
        if error:
            self._capture_error(report, error)
        else:
            self._capture_current_context(report)
        
        # Capture system state
        self._capture_system_info(report)
        
        if self.config.capture_env:
            self._capture_environment(report)
        
        if self.config.capture_network:
            self._capture_network(report)
            self._check_cluster(report)
        
        if self.config.capture_git:
            self._capture_git_state(report)
        
        if self.config.capture_logs:
            self._capture_logs(report)
        
        # Capture dependencies
        self._capture_dependencies(report)
        
        # Analyze and categorize
        self._analyze_problem(report)
        report.category = self._categorize_problem(report)
        
        # Check if auto-fixable
        self._check_auto_fix(report)
        
        # Save report
        self._save_report(report)
        
        return report
    
    def quick_diagnose(self, error: Exception) -> str:
        """Quick one-liner diagnosis"""
        report = self.diagnose(error)
        return self.format_summary(report)
    
    def heal(self, report: Optional[ProblemReport] = None) -> bool:
        """Attempt to auto-fix the problem"""
        if report is None:
            # Get most recent report
            reports = sorted(self.config.report_dir.glob("CLEAN-*.json"), reverse=True)
            if not reports:
                print(f"{C.WARN}No reports to heal{C.RESET}")
                return False
            with open(reports[0]) as f:
                data = json.load(f)
                report = ProblemReport(**data)
        
        if not report.auto_fixable or not report.fix_commands:
            print(f"{C.WARN}This problem cannot be auto-fixed{C.RESET}")
            print(f"{C.INFO}Manual fixes suggested:{C.RESET}")
            for fix in report.suggested_fixes:
                print(f"  • {fix}")
            return False
        
        print(f"{C.INFO}🔧 Attempting auto-heal...{C.RESET}\n")
        
        for cmd in report.fix_commands:
            print(f"{C.DIM}$ {cmd}{C.RESET}")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{C.SUCCESS}✓ Success{C.RESET}")
            else:
                print(f"{C.ERROR}✗ Failed: {result.stderr}{C.RESET}")
                return False
        
        report.resolved = True
        report.resolution_notes = "Auto-healed by CLEANSPACE"
        self._save_report(report)
        
        print(f"\n{C.SUCCESS}✓ Problem healed!{C.RESET}")
        return True
    
    # ─────────────────────────────────────────────────────────
    # ERROR CAPTURE
    # ─────────────────────────────────────────────────────────
    
    def _capture_error(self, report: ProblemReport, error: Exception) -> None:
        """Capture exception details"""
        report.error_type = type(error).__name__
        report.error_message = str(error)
        report.stack_trace = traceback.format_exc()
        
        # Extract location from traceback
        tb = traceback.extract_tb(error.__traceback__) if error.__traceback__ else []
        if tb:
            last_frame = tb[-1]
            report.file_path = last_frame.filename
            report.line_number = last_frame.lineno
            report.function_name = last_frame.name
            
            # Get code context
            try:
                with open(last_frame.filename, 'r') as f:
                    lines = f.readlines()
                    start = max(0, last_frame.lineno - 5)
                    end = min(len(lines), last_frame.lineno + 5)
                    report.code_context = [
                        f"{i+1:4d} {'>>>' if i+1 == last_frame.lineno else '   '} {lines[i].rstrip()}"
                        for i in range(start, end)
                    ]
            except Exception:
                pass
    
    def _capture_current_context(self, report: ProblemReport) -> None:
        """Capture context without an exception"""
        stack = traceback.extract_stack()
        if len(stack) > 2:
            caller = stack[-3]
            report.file_path = caller.filename
            report.line_number = caller.lineno
            report.function_name = caller.name
    
    # ─────────────────────────────────────────────────────────
    # SYSTEM CAPTURE
    # ─────────────────────────────────────────────────────────
    
    def _capture_system_info(self, report: ProblemReport) -> None:
        """Capture system information"""
        report.system_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "os_release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "noizylab_machine": self.machine_type,
        }
        
        # Memory (macOS)
        try:
            result = subprocess.run(["sysctl", "-n", "hw.memsize"],
                capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                total_mem = int(result.stdout.strip())
                report.system_info["total_memory_gb"] = round(total_mem / (1024**3), 1)
        except Exception:
            pass
        
        # Disk
        try:
            result = subprocess.run(["df", "-h", "/"],
                capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    parts = lines[1].split()
                    report.system_info["disk_usage"] = {
                        "total": parts[1] if len(parts) > 1 else "?",
                        "used": parts[2] if len(parts) > 2 else "?",
                        "available": parts[3] if len(parts) > 3 else "?",
                        "percent": parts[4] if len(parts) > 4 else "?",
                    }
        except Exception:
            pass
    
    def _capture_environment(self, report: ProblemReport) -> None:
        """Capture environment variables (redacting secrets)"""
        sensitive = ['KEY', 'SECRET', 'TOKEN', 'PASSWORD', 'CREDENTIAL', 'AUTH']
        for key, value in os.environ.items():
            if any(p in key.upper() for p in sensitive):
                report.environment[key] = "***REDACTED***"
            else:
                report.environment[key] = value
    
    def _capture_network(self, report: ProblemReport) -> None:
        """Capture network state"""
        report.network_state = {
            "hostname": socket.gethostname(),
            "interfaces": [],
            "dns_resolution": {},
            "ports_listening": [],
            "connectivity": {}
        }
        
        # DNS tests
        test_hosts = ["google.com", "github.com", "localhost"]
        for host in test_hosts:
            try:
                ip = socket.gethostbyname(host)
                report.network_state["dns_resolution"][host] = ip
            except socket.gaierror:
                report.network_state["dns_resolution"][host] = "FAILED"
        
        # Key ports
        key_ports = [
            (22, "SSH"), (80, "HTTP"), (443, "HTTPS"),
            (5174, "MC96"), (50051, "gRPC"), (8888, "Dashboard")
        ]
        for port, name in key_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    result = s.connect_ex(('127.0.0.1', port))
                    report.network_state["ports_listening"].append({
                        "port": port, "name": name, "open": result == 0
                    })
            except Exception:
                pass
        
        # Internet
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            report.network_state["connectivity"]["internet"] = True
        except Exception:
            report.network_state["connectivity"]["internet"] = False
    
    def _check_cluster(self, report: ProblemReport) -> None:
        """Check NOIZYLAB cluster status"""
        for name, ip in self.config.machines.items():
            try:
                if ip == "localhost":
                    report.cluster_status[name] = "ONLINE (local)"
                else:
                    socket.create_connection((ip, 22), timeout=2)
                    report.cluster_status[name] = "ONLINE"
            except Exception:
                report.cluster_status[name] = "OFFLINE"
    
    def _capture_git_state(self, report: ProblemReport) -> None:
        """Capture git state"""
        report.git_state = {"is_repo": False}
        try:
            result = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                capture_output=True, text=True, timeout=5)
            if result.returncode != 0:
                return
            
            report.git_state["is_repo"] = True
            
            for cmd, key in [
                (["git", "branch", "--show-current"], "branch"),
                (["git", "rev-parse", "--short", "HEAD"], "commit"),
                (["git", "remote", "get-url", "origin"], "remote")
            ]:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                report.git_state[key] = result.stdout.strip()
            
            result = subprocess.run(["git", "status", "--porcelain"],
                capture_output=True, text=True, timeout=5)
            changes = result.stdout.strip().split('\n') if result.stdout.strip() else []
            report.git_state["dirty"] = len(changes) > 0
            report.git_state["changes"] = changes[:10]
        except Exception:
            pass
    
    def _capture_logs(self, report: ProblemReport) -> None:
        """Capture recent logs"""
        log_locations = [
            self.config.log_dir / "cleanspace.log",
            self.config.noizylab_root / "GABRIEL" / "logs" / "gabriel.log",
            Path("/var/log/system.log"),
        ]
        for log_path in log_locations:
            if log_path.exists():
                try:
                    with open(log_path, 'r') as f:
                        lines = f.readlines()[-20:]
                        report.recent_logs.extend([
                            f"[{log_path.name}] {line.strip()}" for line in lines
                        ])
                except Exception:
                    pass
    
    def _capture_dependencies(self, report: ProblemReport) -> None:
        """Capture Python dependencies"""
        report.python_version = platform.python_version()
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--format=json"],
                capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                packages = json.loads(result.stdout)
                report.installed_packages = {p["name"]: p["version"] for p in packages}
        except Exception:
            pass
        
        # Check for missing packages from error
        if "ModuleNotFoundError" in report.error_type or "ImportError" in report.error_type:
            match = re.search(r"No module named '([^']+)'", report.error_message)
            if match:
                report.missing_packages.append(match.group(1))
    
    # ─────────────────────────────────────────────────────────
    # ANALYSIS
    # ─────────────────────────────────────────────────────────
    
    def _analyze_problem(self, report: ProblemReport) -> None:
        """Analyze and suggest fixes"""
        et = report.error_type
        em = report.error_message.lower()
        
        # ModuleNotFoundError
        if "ModuleNotFoundError" in et or "ImportError" in et:
            module = report.missing_packages[0] if report.missing_packages else "unknown"
            report.probable_causes.append(f"Python package '{module}' not installed")
            report.suggested_fixes.append(f"pip3 install {module}")
            report.suggested_fixes.append("pip3 install -r requirements.txt")
            report.auto_fixable = True
            report.fix_commands.append(f"pip3 install {module}")
        
        # FileNotFoundError
        elif "FileNotFoundError" in et:
            report.probable_causes.append("Required file/directory doesn't exist")
            report.suggested_fixes.append("Check file path is correct")
            report.suggested_fixes.append("Verify working directory")
        
        # PermissionError
        elif "PermissionError" in et:
            report.probable_causes.append("Insufficient permissions")
            report.suggested_fixes.append(f"chmod +x {report.file_path}")
            report.suggested_fixes.append("Check file ownership")
            if report.file_path:
                report.auto_fixable = True
                report.fix_commands.append(f"chmod +x {report.file_path}")
        
        # ConnectionError
        elif any(x in et for x in ["ConnectionError", "ConnectionRefused", "TimeoutError"]):
            report.probable_causes.append("Network/service connectivity issue")
            report.suggested_fixes.append("Check network connection")
            report.suggested_fixes.append("Verify target service is running")
            report.suggested_fixes.append("Check firewall settings")
        
        # MemoryError
        elif "MemoryError" in et:
            report.probable_causes.append("Insufficient memory")
            report.suggested_fixes.append("Close other applications")
            report.suggested_fixes.append("Process data in smaller chunks")
        
        # Default
        if not report.probable_causes:
            report.probable_causes.append("Unknown error - manual investigation needed")
            report.suggested_fixes.append("Review stack trace")
            report.suggested_fixes.append("Search error message online")
    
    def _categorize_problem(self, report: ProblemReport) -> str:
        """Categorize the problem"""
        et = report.error_type
        
        if "ModuleNotFoundError" in et or "ImportError" in et:
            return ProblemCategory.DEPENDENCY.value
        if "FileNotFoundError" in et:
            return ProblemCategory.FILESYSTEM.value
        if "PermissionError" in et:
            return ProblemCategory.PERMISSION.value
        if any(x in et for x in ["ConnectionError", "socket", "Timeout"]):
            return ProblemCategory.NETWORK.value
        if "MemoryError" in et:
            return ProblemCategory.MEMORY.value
        if any(x in et for x in ["TypeError", "ValueError", "AttributeError"]):
            return ProblemCategory.CODE_BUG.value
        
        return ProblemCategory.UNKNOWN.value
    
    def _check_auto_fix(self, report: ProblemReport) -> None:
        """Determine if problem is auto-fixable"""
        # Already set in _analyze_problem
        pass
    
    # ─────────────────────────────────────────────────────────
    # STORAGE & FORMATTING
    # ─────────────────────────────────────────────────────────
    
    def _generate_id(self) -> str:
        """Generate unique report ID"""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        h = hashlib.md5(str(datetime.now().timestamp()).encode()).hexdigest()[:6]
        return f"CLEAN-{ts}-{h}"
    
    def _save_report(self, report: ProblemReport) -> Path:
        """Save report to disk"""
        path = self.config.report_dir / f"{report.id}.json"
        with open(path, 'w') as f:
            json.dump(asdict(report), f, indent=2, default=str)
        
        # Cleanup old
        reports = sorted(self.config.report_dir.glob("CLEAN-*.json"))
        if len(reports) > self.config.max_reports:
            for old in reports[:-self.config.max_reports]:
                old.unlink()
        
        return path
    
    def format_summary(self, report: ProblemReport) -> str:
        """Format human-readable summary"""
        healable = f"{C.SUCCESS}[AUTO-FIXABLE]{C.RESET}" if report.auto_fixable else ""
        
        summary = f"""
{C.ERROR}{'═' * 70}{C.RESET}
{C.BOLD}{C.ERROR}🧹 NOIZYLAB CLEANSPACE - DIAGNOSTIC REPORT{C.RESET} {healable}
{C.ERROR}{'═' * 70}{C.RESET}

{C.WARN}REPORT ID:{C.RESET}    {report.id}
{C.WARN}MACHINE:{C.RESET}      {report.machine_type} ({report.hostname})
{C.WARN}TIMESTAMP:{C.RESET}    {report.timestamp}
{C.WARN}CATEGORY:{C.RESET}     {report.category.upper()}

{C.ERROR}{'─' * 70}{C.RESET}
{C.BOLD}ERROR:{C.RESET}
{C.ERROR}{report.error_type}: {report.error_message}{C.RESET}

{C.INFO}{'─' * 70}{C.RESET}
{C.BOLD}LOCATION:{C.RESET}
  File:     {report.file_path}
  Line:     {report.line_number}
  Function: {report.function_name}

{C.DIM}Code Context:{C.RESET}
"""
        for line in report.code_context:
            if '>>>' in line:
                summary += f"  {C.ERROR}{line}{C.RESET}\n"
            else:
                summary += f"  {C.DIM}{line}{C.RESET}\n"
        
        summary += f"""
{C.SUCCESS}{'─' * 70}{C.RESET}
{C.BOLD}PROBABLE CAUSES:{C.RESET}
"""
        for i, cause in enumerate(report.probable_causes, 1):
            summary += f"  {i}. {cause}\n"
        
        summary += f"""
{C.ACCENT}{'─' * 70}{C.RESET}
{C.BOLD}SUGGESTED FIXES:{C.RESET}
"""
        for i, fix in enumerate(report.suggested_fixes, 1):
            summary += f"  {i}. {C.SUCCESS}{fix}{C.RESET}\n"
        
        if report.auto_fixable:
            summary += f"""
{C.INFO}{'─' * 70}{C.RESET}
{C.BOLD}🔧 AUTO-HEAL AVAILABLE:{C.RESET}
  Run: {C.SUCCESS}cleanspace heal{C.RESET}
  Commands that will run:
"""
            for cmd in report.fix_commands:
                summary += f"    $ {cmd}\n"
        
        summary += f"""
{C.INFO}{'─' * 70}{C.RESET}
{C.BOLD}CLUSTER STATUS:{C.RESET}
"""
        for machine, status in report.cluster_status.items():
            icon = "🟢" if "ONLINE" in status else "🔴"
            summary += f"  {icon} {machine}: {status}\n"
        
        summary += f"""
{C.DIM}Report saved: {self.config.report_dir / f"{report.id}.json"}{C.RESET}
{C.ERROR}{'═' * 70}{C.RESET}
"""
        return summary
    
    def format_for_ai(self, report: ProblemReport) -> str:
        """Format for AI assistant analysis"""
        return f"""
NOIZYLAB CLEANSPACE DIAGNOSTIC REPORT
=====================================
Machine: {report.machine_type} ({report.hostname})
Error: {report.error_type}: {report.error_message}

Location: {report.file_path}:{report.line_number} in {report.function_name}

Stack Trace:
{report.stack_trace}

Code Context:
{chr(10).join(report.code_context)}

System: {report.system_info.get('os')} {report.system_info.get('os_release')}
Python: {report.python_version}
Missing Packages: {', '.join(report.missing_packages) or 'None'}
Cluster: {report.cluster_status}

Please analyze and provide:
1. Root cause
2. Step-by-step fix
3. Prevention recommendations
"""

# ══════════════════════════════════════════════════════════════
# GLOBAL API
# ══════════════════════════════════════════════════════════════

_engine: Optional[CleanspaceEngine] = None

def get_engine() -> CleanspaceEngine:
    global _engine
    if _engine is None:
        _engine = CleanspaceEngine()
    return _engine

def diagnose(error: Optional[Exception] = None, title: str = "", description: str = "") -> ProblemReport:
    """Quick diagnose function"""
    return get_engine().diagnose(error, title, description)

def wtf(error: Exception) -> None:
    """The WTF function - full diagnostic report"""
    engine = get_engine()
    report = engine.diagnose(error)
    print(engine.format_summary(report))

def heal(report: Optional[ProblemReport] = None) -> bool:
    """Attempt auto-heal"""
    return get_engine().heal(report)

def capture_and_continue(func):
    """Decorator for non-fatal error capture"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            report = diagnose(e, title=f"Error in {func.__name__}")
            print(f"{C.WARN}⚠️ Non-fatal error: {report.id}{C.RESET}")
            return None
    return wrapper

def install_global_handler() -> None:
    """Install as global exception handler"""
    def handler(exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        exc_value.__traceback__ = exc_tb
        wtf(exc_value)
    
    sys.excepthook = handler
    print(f"{C.SUCCESS}✓ CLEANSPACE installed as global error handler{C.RESET}")

# ══════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════

def cmd_list(args: List[str]) -> None:
    """List diagnostic reports"""
    engine = get_engine()
    reports = sorted(engine.config.report_dir.glob("CLEAN-*.json"), reverse=True)
    
    if not reports:
        print(f"{C.WARN}No diagnostic reports found.{C.RESET}")
        return
    
    print(f"\n{C.INFO}{'═' * 70}{C.RESET}")
    print(f"{C.BOLD}🧹 CLEANSPACE DIAGNOSTIC REPORTS{C.RESET}")
    print(f"{C.INFO}{'═' * 70}{C.RESET}\n")
    
    for path in reports[:20]:
        try:
            with open(path) as f:
                d = json.load(f)
                healable = f"{C.SUCCESS}[HEALABLE]{C.RESET}" if d.get('auto_fixable') else ""
                print(f"  {C.WARN}{d['id']}{C.RESET} {healable}")
                print(f"    {C.DIM}{d['timestamp']} | {d.get('machine_type', '?')}{C.RESET}")
                print(f"    {C.ERROR}{d['error_type']}: {d['error_message'][:50]}...{C.RESET}\n")
        except Exception:
            pass

def cmd_show(args: List[str]) -> None:
    """Show specific report"""
    if not args:
        print(f"{C.ERROR}Usage: cleanspace show <report-id>{C.RESET}")
        return
    
    engine = get_engine()
    for path in engine.config.report_dir.glob("CLEAN-*.json"):
        if args[0] in path.name:
            with open(path) as f:
                report = ProblemReport(**json.load(f))
                print(engine.format_summary(report))
                return
    
    print(f"{C.ERROR}Report not found: {args[0]}{C.RESET}")

def cmd_last(args: List[str]) -> None:
    """Show most recent report"""
    engine = get_engine()
    reports = sorted(engine.config.report_dir.glob("CLEAN-*.json"), reverse=True)
    if reports:
        cmd_show([reports[0].stem])
    else:
        print(f"{C.WARN}No reports found{C.RESET}")

def cmd_heal_cli(args: List[str]) -> None:
    """Heal most recent or specified report"""
    engine = get_engine()
    if args:
        for path in engine.config.report_dir.glob("CLEAN-*.json"):
            if args[0] in path.name:
                with open(path) as f:
                    report = ProblemReport(**json.load(f))
                    engine.heal(report)
                    return
        print(f"{C.ERROR}Report not found: {args[0]}{C.RESET}")
    else:
        engine.heal()

def cmd_test(args: List[str]) -> None:
    """Test diagnostic system"""
    print(f"{C.INFO}Testing CLEANSPACE...{C.RESET}\n")
    try:
        raise ValueError("Test error for CLEANSPACE diagnostic")
    except Exception as e:
        wtf(e)

def main() -> None:
    """CLI entry point"""
    if len(sys.argv) < 2:
        print(f"""
{C.INFO}🧹 NOIZYLAB CLEANSPACE - Problem Sourcer{C.RESET}

Usage:
    cleanspace list              List all diagnostic reports
    cleanspace show <id>         Show specific report
    cleanspace last              Show most recent report
    cleanspace heal [id]         Auto-fix problem
    cleanspace test              Test diagnostic system
    cleanspace install           Install global handler

In Python:
    from cleanspace import wtf, diagnose, heal
    
    try:
        risky_code()
    except Exception as e:
        wtf(e)  # Full diagnostic
        heal()  # Auto-fix if possible
""")
        return
    
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    commands = {
        "list": cmd_list,
        "show": cmd_show,
        "last": cmd_last,
        "heal": cmd_heal_cli,
        "test": cmd_test,
        "install": lambda _: install_global_handler(),
    }
    
    if cmd in commands:
        commands[cmd](args)
    else:
        print(f"{C.ERROR}Unknown command: {cmd}{C.RESET}")

if __name__ == "__main__":
    main()
