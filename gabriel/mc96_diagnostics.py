#!/usr/bin/env python3
"""
🔍 MC96 DIAGNOSTIC ENGINE - PROBLEM SOURCER
═══════════════════════════════════════════════════════════════
When something breaks and can't be fixed automatically,
this system captures EVERYTHING needed to source the problem.

Features:
- Stack trace analysis
- Log aggregation
- System state snapshot
- Network diagnostics
- Dependency analysis
- Git state capture
- Environment diff
- AI-powered root cause analysis
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
    """Severity levels"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    FATAL = "fatal"

class ProblemCategory(Enum):
    """Problem categories"""
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
class DiagnosticConfig:
    """Diagnostic configuration"""
    report_dir: Path = field(default_factory=lambda: Path.home() / ".mc96" / "diagnostics")
    max_reports: int = 50
    capture_env: bool = True
    capture_logs: bool = True
    capture_network: bool = True
    capture_git: bool = True
    ai_analysis: bool = True
    verbose: bool = False

CONFIG = DiagnosticConfig()

# ══════════════════════════════════════════════════════════════
# ANSI COLORS
# ══════════════════════════════════════════════════════════════

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

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
    
    # Git state
    git_state: Dict[str, Any] = field(default_factory=dict)
    
    # Logs
    recent_logs: List[str] = field(default_factory=list)
    
    # Analysis
    probable_causes: List[str] = field(default_factory=list)
    suggested_fixes: List[str] = field(default_factory=list)
    related_issues: List[str] = field(default_factory=list)
    
    # Resolution
    resolved: bool = False
    resolution_notes: str = ""

# ══════════════════════════════════════════════════════════════
# DIAGNOSTIC ENGINE
# ══════════════════════════════════════════════════════════════

class DiagnosticEngine:
    """Main diagnostic engine"""
    
    def __init__(self, config: Optional[DiagnosticConfig] = None):
        self.config = config or CONFIG
        self.config.report_dir.mkdir(parents=True, exist_ok=True)
    
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
        """
        Create a comprehensive diagnostic report.
        Call this when something breaks!
        """
        report = ProblemReport(
            id=self._generate_id(),
            timestamp=datetime.now().isoformat(),
            hostname=socket.gethostname(),
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
        
        if self.config.capture_git:
            self._capture_git_state(report)
        
        if self.config.capture_logs:
            self._capture_logs(report)
        
        # Capture dependencies
        self._capture_dependencies(report)
        
        # Analyze the problem
        self._analyze_problem(report)
        
        # Categorize
        report.category = self._categorize_problem(report)
        
        # Save report
        self._save_report(report)
        
        return report
    
    def quick_diagnose(self, error: Exception) -> str:
        """Quick one-liner diagnosis"""
        report = self.diagnose(error)
        return self.format_summary(report)
    
    # ─────────────────────────────────────────────────────────
    # ERROR CAPTURE
    # ─────────────────────────────────────────────────────────
    
    def _capture_error(self, report: ProblemReport, error: Exception) -> None:
        """Capture exception details"""
        report.error_type = type(error).__name__
        report.error_message = str(error)
        report.stack_trace = traceback.format_exc()
        
        # Extract location from traceback
        tb = traceback.extract_tb(error.__traceback__)
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
        # Get caller info
        stack = traceback.extract_stack()
        if len(stack) > 2:
            caller = stack[-3]  # Skip this function and diagnose()
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
            "python_implementation": platform.python_implementation(),
        }
        
        # Memory info (macOS)
        try:
            result = subprocess.run(
                ["sysctl", "-n", "hw.memsize"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                total_mem = int(result.stdout.strip())
                report.system_info["total_memory_gb"] = round(total_mem / (1024**3), 1)
        except Exception:
            pass
        
        # Disk info
        try:
            result = subprocess.run(
                ["df", "-h", "/"],
                capture_output=True, text=True, timeout=5
            )
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
        
        # Top processes
        try:
            result = subprocess.run(
                ["ps", "aux", "--sort=-%mem"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[:6]  # Header + top 5
                report.processes = [{"raw": line} for line in lines]
        except Exception:
            pass
    
    def _capture_environment(self, report: ProblemReport) -> None:
        """Capture environment variables"""
        # Filter sensitive vars
        sensitive_patterns = ['KEY', 'SECRET', 'TOKEN', 'PASSWORD', 'CREDENTIAL', 'AUTH']
        
        for key, value in os.environ.items():
            if any(p in key.upper() for p in sensitive_patterns):
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
        
        # Get interfaces
        try:
            result = subprocess.run(
                ["ifconfig"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                # Parse interfaces
                current_if = None
                for line in result.stdout.split('\n'):
                    if line and not line.startswith('\t'):
                        current_if = line.split(':')[0]
                    elif current_if and 'inet ' in line:
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            report.network_state["interfaces"].append({
                                "name": current_if,
                                "ip": parts[1]
                            })
        except Exception:
            pass
        
        # DNS resolution tests
        test_hosts = ["google.com", "github.com", "localhost"]
        for host in test_hosts:
            try:
                ip = socket.gethostbyname(host)
                report.network_state["dns_resolution"][host] = ip
            except socket.gaierror:
                report.network_state["dns_resolution"][host] = "FAILED"
        
        # Check key ports
        key_ports = [
            (22, "SSH"),
            (80, "HTTP"),
            (443, "HTTPS"),
            (5174, "MC96"),
            (50051, "gRPC"),
        ]
        for port, name in key_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    result = s.connect_ex(('127.0.0.1', port))
                    report.network_state["ports_listening"].append({
                        "port": port,
                        "name": name,
                        "open": result == 0
                    })
            except Exception:
                pass
        
        # Internet connectivity
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            report.network_state["connectivity"]["internet"] = True
        except Exception:
            report.network_state["connectivity"]["internet"] = False
    
    def _capture_git_state(self, report: ProblemReport) -> None:
        """Capture git repository state"""
        report.git_state = {
            "is_repo": False,
            "branch": "",
            "commit": "",
            "dirty": False,
            "changes": [],
            "remote": ""
        }
        
        try:
            # Check if in git repo
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode != 0:
                return
            
            report.git_state["is_repo"] = True
            
            # Current branch
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True, text=True, timeout=5
            )
            report.git_state["branch"] = result.stdout.strip()
            
            # Current commit
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True, text=True, timeout=5
            )
            report.git_state["commit"] = result.stdout.strip()
            
            # Check if dirty
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, timeout=5
            )
            changes = result.stdout.strip().split('\n') if result.stdout.strip() else []
            report.git_state["dirty"] = len(changes) > 0
            report.git_state["changes"] = changes[:10]  # Limit to 10
            
            # Remote URL
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True, text=True, timeout=5
            )
            report.git_state["remote"] = result.stdout.strip()
            
        except Exception:
            pass
    
    def _capture_logs(self, report: ProblemReport) -> None:
        """Capture recent log entries"""
        log_locations = [
            Path.home() / ".mc96" / "mc96.log",
            Path.home() / "NOIZYLAB" / "GABRIEL" / "logs" / "gabriel.log",
            Path("/var/log/system.log"),
        ]
        
        for log_path in log_locations:
            if log_path.exists():
                try:
                    with open(log_path, 'r') as f:
                        lines = f.readlines()
                        # Get last 20 lines
                        report.recent_logs.extend([
                            f"[{log_path.name}] {line.strip()}"
                            for line in lines[-20:]
                        ])
                except Exception:
                    pass
    
    def _capture_dependencies(self, report: ProblemReport) -> None:
        """Capture Python dependencies"""
        report.python_version = platform.python_version()
        
        # Get installed packages
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--format=json"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                packages = json.loads(result.stdout)
                report.installed_packages = {
                    pkg["name"]: pkg["version"] for pkg in packages
                }
        except Exception:
            pass
        
        # Check for common missing packages based on error
        if "ModuleNotFoundError" in report.error_type or "ImportError" in report.error_type:
            # Extract module name from error message
            match = re.search(r"No module named '([^']+)'", report.error_message)
            if match:
                report.missing_packages.append(match.group(1))
    
    # ─────────────────────────────────────────────────────────
    # ANALYSIS
    # ─────────────────────────────────────────────────────────
    
    def _analyze_problem(self, report: ProblemReport) -> None:
        """Analyze the problem and suggest fixes"""
        error_type = report.error_type
        error_msg = report.error_message.lower()
        
        # ModuleNotFoundError
        if "ModuleNotFoundError" in error_type or "ImportError" in error_type:
            module = report.missing_packages[0] if report.missing_packages else "unknown"
            report.probable_causes.append(f"Python package '{module}' is not installed")
            report.suggested_fixes.append(f"pip3 install {module}")
            report.suggested_fixes.append(f"pip3 install -r requirements.txt")
        
        # FileNotFoundError
        elif "FileNotFoundError" in error_type:
            report.probable_causes.append("Required file or directory does not exist")
            report.suggested_fixes.append("Check file path is correct")
            report.suggested_fixes.append("Ensure working directory is correct")
        
        # PermissionError
        elif "PermissionError" in error_type:
            report.probable_causes.append("Insufficient permissions to access resource")
            report.suggested_fixes.append(f"chmod +x {report.file_path}")
            report.suggested_fixes.append("Run with sudo if appropriate")
            report.suggested_fixes.append("Check file ownership")
        
        # ConnectionError / Network
        elif any(x in error_type for x in ["ConnectionError", "ConnectionRefused", "TimeoutError"]):
            report.probable_causes.append("Network connectivity issue")
            report.probable_causes.append("Target service may be down")
            report.suggested_fixes.append("Check network connection")
            report.suggested_fixes.append("Verify service is running")
            report.suggested_fixes.append("Check firewall settings")
        
        # Memory errors
        elif "MemoryError" in error_type or "killed" in error_msg:
            report.probable_causes.append("Insufficient memory")
            report.suggested_fixes.append("Free up memory by closing other applications")
            report.suggested_fixes.append("Increase swap space")
            report.suggested_fixes.append("Process data in smaller chunks")
        
        # JSON/Syntax errors
        elif any(x in error_type for x in ["JSONDecodeError", "SyntaxError"]):
            report.probable_causes.append("Malformed data or code syntax error")
            report.suggested_fixes.append("Validate JSON/code syntax")
            report.suggested_fixes.append("Check for missing quotes, brackets, or commas")
        
        # Type errors
        elif "TypeError" in error_type:
            report.probable_causes.append("Incorrect data type passed to function")
            report.probable_causes.append("API change or version mismatch")
            report.suggested_fixes.append("Check function signature and argument types")
            report.suggested_fixes.append("Update dependencies to compatible versions")
        
        # Value errors
        elif "ValueError" in error_type:
            report.probable_causes.append("Invalid value or format")
            report.suggested_fixes.append("Validate input data")
            report.suggested_fixes.append("Check for empty or null values")
        
        # Key errors
        elif "KeyError" in error_type:
            report.probable_causes.append("Missing key in dictionary/configuration")
            report.suggested_fixes.append("Verify all required config keys are present")
            report.suggested_fixes.append("Use .get() with default value")
        
        # Attribute errors
        elif "AttributeError" in error_type:
            report.probable_causes.append("Object doesn't have expected attribute")
            report.probable_causes.append("Possible None value")
            report.suggested_fixes.append("Add null check before accessing attribute")
            report.suggested_fixes.append("Verify object type is correct")
        
        # Generic analysis if nothing specific found
        if not report.probable_causes:
            report.probable_causes.append("Unknown error - requires manual investigation")
            report.suggested_fixes.append("Review stack trace for clues")
            report.suggested_fixes.append("Search error message online")
            report.suggested_fixes.append("Check related documentation")
    
    def _categorize_problem(self, report: ProblemReport) -> str:
        """Categorize the problem"""
        error_type = report.error_type
        error_msg = report.error_message.lower()
        
        if "ModuleNotFoundError" in error_type or "ImportError" in error_type:
            return ProblemCategory.DEPENDENCY.value
        
        if "FileNotFoundError" in error_type:
            return ProblemCategory.FILESYSTEM.value
        
        if "PermissionError" in error_type:
            return ProblemCategory.PERMISSION.value
        
        if any(x in error_type for x in ["ConnectionError", "socket", "Timeout"]):
            return ProblemCategory.NETWORK.value
        
        if "MemoryError" in error_type:
            return ProblemCategory.MEMORY.value
        
        if any(x in error_msg for x in ["config", "setting", "environment"]):
            return ProblemCategory.CONFIGURATION.value
        
        if any(x in error_type for x in ["TypeError", "ValueError", "AttributeError"]):
            return ProblemCategory.CODE_BUG.value
        
        return ProblemCategory.UNKNOWN.value
    
    # ─────────────────────────────────────────────────────────
    # STORAGE & FORMATTING
    # ─────────────────────────────────────────────────────────
    
    def _generate_id(self) -> str:
        """Generate unique report ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        random_hash = hashlib.md5(str(datetime.now().timestamp()).encode()).hexdigest()[:6]
        return f"MC96-{timestamp}-{random_hash}"
    
    def _save_report(self, report: ProblemReport) -> Path:
        """Save report to disk"""
        report_path = self.config.report_dir / f"{report.id}.json"
        
        with open(report_path, 'w') as f:
            json.dump(asdict(report), f, indent=2, default=str)
        
        # Cleanup old reports
        self._cleanup_old_reports()
        
        return report_path
    
    def _cleanup_old_reports(self) -> None:
        """Remove old reports beyond max limit"""
        reports = sorted(self.config.report_dir.glob("MC96-*.json"))
        if len(reports) > self.config.max_reports:
            for old_report in reports[:-self.config.max_reports]:
                old_report.unlink()
    
    def format_summary(self, report: ProblemReport) -> str:
        """Format a human-readable summary"""
        summary = f"""
{C.RED}{'═' * 70}{C.RESET}
{C.BOLD}{C.RED}🔍 MC96 DIAGNOSTIC REPORT{C.RESET}
{C.RED}{'═' * 70}{C.RESET}

{C.YELLOW}REPORT ID:{C.RESET}    {report.id}
{C.YELLOW}TIMESTAMP:{C.RESET}    {report.timestamp}
{C.YELLOW}CATEGORY:{C.RESET}     {report.category.upper()}
{C.YELLOW}SEVERITY:{C.RESET}     {report.level.upper()}

{C.RED}{'─' * 70}{C.RESET}
{C.BOLD}ERROR:{C.RESET}
{C.RED}{report.error_type}: {report.error_message}{C.RESET}

{C.CYAN}{'─' * 70}{C.RESET}
{C.BOLD}LOCATION:{C.RESET}
  File:     {report.file_path}
  Line:     {report.line_number}
  Function: {report.function_name}

{C.DIM}Code Context:{C.RESET}
"""
        for line in report.code_context:
            if '>>>' in line:
                summary += f"  {C.RED}{line}{C.RESET}\n"
            else:
                summary += f"  {C.DIM}{line}{C.RESET}\n"
        
        summary += f"""
{C.GREEN}{'─' * 70}{C.RESET}
{C.BOLD}PROBABLE CAUSES:{C.RESET}
"""
        for i, cause in enumerate(report.probable_causes, 1):
            summary += f"  {i}. {cause}\n"
        
        summary += f"""
{C.MAGENTA}{'─' * 70}{C.RESET}
{C.BOLD}SUGGESTED FIXES:{C.RESET}
"""
        for i, fix in enumerate(report.suggested_fixes, 1):
            summary += f"  {i}. {C.GREEN}{fix}{C.RESET}\n"
        
        summary += f"""
{C.BLUE}{'─' * 70}{C.RESET}
{C.BOLD}SYSTEM STATE:{C.RESET}
  OS:       {report.system_info.get('os', '?')} {report.system_info.get('os_release', '')}
  Python:   {report.python_version}
  Memory:   {report.system_info.get('total_memory_gb', '?')} GB
  Internet: {'✓' if report.network_state.get('connectivity', {}).get('internet') else '✗'}
  Git:      {report.git_state.get('branch', 'N/A')} @ {report.git_state.get('commit', 'N/A')}

{C.DIM}Full report saved to: {self.config.report_dir / f"{report.id}.json"}{C.RESET}
{C.RED}{'═' * 70}{C.RESET}
"""
        return summary
    
    def format_for_ai(self, report: ProblemReport) -> str:
        """Format report for AI assistant analysis"""
        return f"""
DIAGNOSTIC REPORT FOR AI ANALYSIS
=================================

ERROR TYPE: {report.error_type}
ERROR MESSAGE: {report.error_message}

LOCATION:
- File: {report.file_path}
- Line: {report.line_number}
- Function: {report.function_name}

STACK TRACE:
{report.stack_trace}

CODE CONTEXT:
{chr(10).join(report.code_context)}

SYSTEM INFO:
- OS: {report.system_info.get('os')} {report.system_info.get('os_release')}
- Python: {report.python_version}
- Memory: {report.system_info.get('total_memory_gb')} GB

GIT STATE:
- Branch: {report.git_state.get('branch')}
- Commit: {report.git_state.get('commit')}
- Dirty: {report.git_state.get('dirty')}

MISSING PACKAGES: {', '.join(report.missing_packages) if report.missing_packages else 'None detected'}

NETWORK:
- Internet: {report.network_state.get('connectivity', {}).get('internet', 'unknown')}
- DNS: {report.network_state.get('dns_resolution', {})}

Please analyze this error and provide:
1. Root cause analysis
2. Step-by-step fix
3. Prevention recommendations
"""

# ══════════════════════════════════════════════════════════════
# GLOBAL INSTANCE & HELPERS
# ══════════════════════════════════════════════════════════════

_engine: Optional[DiagnosticEngine] = None

def get_engine() -> DiagnosticEngine:
    """Get or create diagnostic engine"""
    global _engine
    if _engine is None:
        _engine = DiagnosticEngine()
    return _engine

def diagnose(
    error: Optional[Exception] = None,
    title: str = "",
    description: str = ""
) -> ProblemReport:
    """Quick diagnose function"""
    return get_engine().diagnose(error, title, description)

def wtf(error: Exception) -> None:
    """
    The "WTF" function - when you don't know what went wrong.
    Prints a full diagnostic report.
    """
    engine = get_engine()
    report = engine.diagnose(error)
    print(engine.format_summary(report))

def capture_and_continue(func):
    """
    Decorator that captures errors but allows program to continue.
    Useful for non-critical operations.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            report = diagnose(e, title=f"Error in {func.__name__}")
            print(f"{C.YELLOW}⚠️  Non-fatal error captured: {report.id}{C.RESET}")
            return None
    return wrapper

def install_global_handler() -> None:
    """
    Install as global exception handler.
    All uncaught exceptions will generate a diagnostic report.
    """
    def global_handler(exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        
        error = exc_value
        error.__traceback__ = exc_tb
        wtf(error)
    
    sys.excepthook = global_handler
    print(f"{C.GREEN}✓ MC96 Diagnostic Engine installed as global handler{C.RESET}")

# ══════════════════════════════════════════════════════════════
# CLI INTERFACE
# ══════════════════════════════════════════════════════════════

def cmd_list_reports(args: List[str]) -> None:
    """List all diagnostic reports"""
    engine = get_engine()
    reports = sorted(engine.config.report_dir.glob("MC96-*.json"), reverse=True)
    
    if not reports:
        print(f"{C.YELLOW}No diagnostic reports found.{C.RESET}")
        return
    
    print(f"\n{C.CYAN}{'═' * 70}{C.RESET}")
    print(f"{C.BOLD}📋 DIAGNOSTIC REPORTS{C.RESET}")
    print(f"{C.CYAN}{'═' * 70}{C.RESET}\n")
    
    for report_path in reports[:20]:  # Show last 20
        try:
            with open(report_path) as f:
                data = json.load(f)
                print(f"  {C.YELLOW}{data['id']}{C.RESET}")
                print(f"    {C.DIM}{data['timestamp']}{C.RESET}")
                print(f"    {C.RED}{data['error_type']}: {data['error_message'][:50]}...{C.RESET}")
                print()
        except Exception:
            pass

def cmd_show_report(args: List[str]) -> None:
    """Show a specific report"""
    if not args:
        print(f"{C.RED}Usage: diag show <report-id>{C.RESET}")
        return
    
    engine = get_engine()
    report_id = args[0]
    
    # Find matching report
    for report_path in engine.config.report_dir.glob("MC96-*.json"):
        if report_id in report_path.name:
            with open(report_path) as f:
                data = json.load(f)
                report = ProblemReport(**data)
                print(engine.format_summary(report))
                return
    
    print(f"{C.RED}Report not found: {report_id}{C.RESET}")

def cmd_test(args: List[str]) -> None:
    """Test the diagnostic system"""
    print(f"{C.CYAN}Testing MC96 Diagnostic Engine...{C.RESET}\n")
    
    # Trigger a test error
    try:
        x = 1 / 0
    except Exception as e:
        wtf(e)

def main() -> None:
    """CLI entry point"""
    if len(sys.argv) < 2:
        print(f"""
{C.CYAN}🔍 MC96 DIAGNOSTIC ENGINE{C.RESET}

Usage:
    diag list              List all diagnostic reports
    diag show <id>         Show specific report
    diag test              Test diagnostic system
    diag install           Install global exception handler

In Python:
    from mc96_diagnostics import wtf, diagnose
    
    try:
        something_risky()
    except Exception as e:
        wtf(e)  # Full diagnostic report
""")
        return
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    commands = {
        "list": cmd_list_reports,
        "show": cmd_show_report,
        "test": cmd_test,
        "install": lambda _: install_global_handler(),
    }
    
    if command in commands:
        commands[command](args)
    else:
        print(f"{C.RED}Unknown command: {command}{C.RESET}")

if __name__ == "__main__":
    main()
