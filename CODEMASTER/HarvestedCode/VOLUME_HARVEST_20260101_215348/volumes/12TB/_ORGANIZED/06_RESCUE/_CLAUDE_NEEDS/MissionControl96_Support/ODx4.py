#!/usr/bin/env python3
"""
Mission Control 96 - Perfectionist Agent
Advanced Diagnostic Healing and System Optimization

This script provides comprehensive system analysis, automatic issue detection,
and intelligent healing capabilities for maintaining perfect system health.
"""

import os
import subprocess
import json
import psutil
import shutil
import glob
from pathlib import Path
from datetime import datetime, timedelta
import re
import sqlite3
import hashlib

class PerfectionistAgent:
    def __init__(self):
        self.scan_results = {}
        self.healing_log = []
        self.optimization_score = 0
        self.issues_found = []
        self.auto_fixes_applied = []
        
    def comprehensive_diagnostic_scan(self):
        """Perform deep system diagnostic scan"""
        print("🔍 Starting Perfectionist Diagnostic Scan...")
        
        scan_results = {
            "timestamp": datetime.now().isoformat(),
            "system_health": self._check_system_health(),
            "storage_analysis": self._analyze_storage(),
            "security_audit": self._security_audit(),
            "performance_metrics": self._performance_metrics(),
            "application_health": self._check_applications(),
            "network_diagnostics": self._network_diagnostics(),
            "file_system_integrity": self._check_file_integrity(),
            "memory_optimization": self._memory_analysis(),
            "startup_optimization": self._startup_analysis()
        }
        
        self.scan_results = scan_results
        return scan_results
    
    def _check_system_health(self):
        """Check overall system health"""
        health_checks = {
            "cpu_temperature": self._get_cpu_temp(),
            "disk_health": self._check_disk_health(),
            "memory_pressure": self._check_memory_pressure(),
            "system_logs": self._analyze_system_logs(),
            "process_analysis": self._analyze_processes()
        }
        return health_checks
    
    def _get_cpu_temp(self):
        """Get CPU temperature if available"""
        try:
            # macOS system temperature check
            result = subprocess.run(
                ["sudo", "powermetrics", "--samplers", "smc", "-n", "1"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0 and "CPU die temperature" in result.stdout:
                temp_match = re.search(r'CPU die temperature: ([\d.]+)', result.stdout)
                if temp_match:
                    return {"temperature_c": float(temp_match.group(1)), "status": "monitored"}
            return {"temperature_c": None, "status": "unavailable"}
        except:
            return {"temperature_c": None, "status": "error"}
    
    def _check_disk_health(self):
        """Check disk health and SMART status"""
        try:
            disk_info = []
            for partition in psutil.disk_partitions():
                if 'disk' in partition.device:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append({
                        "device": partition.device,
                        "mountpoint": partition.mountpoint,
                        "fstype": partition.fstype,
                        "total_gb": round(usage.total / (1024**3), 2),
                        "used_gb": round(usage.used / (1024**3), 2),
                        "free_gb": round(usage.free / (1024**3), 2),
                        "usage_percent": round((usage.used / usage.total) * 100, 1),
                        "health_status": "healthy" if usage.percent < 85 else "warning"
                    })
            return disk_info
        except Exception as e:
            return {"error": str(e)}
    
    def _check_memory_pressure(self):
        """Analyze memory pressure and swap usage"""
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return {
            "memory_total_gb": round(memory.total / (1024**3), 2),
            "memory_available_gb": round(memory.available / (1024**3), 2),
            "memory_percent": memory.percent,
            "swap_total_gb": round(swap.total / (1024**3), 2) if swap.total else 0,
            "swap_used_gb": round(swap.used / (1024**3), 2) if swap.used else 0,
            "pressure_level": "high" if memory.percent > 85 else "normal"
        }
    
    def _analyze_system_logs(self):
        """Analyze system logs for errors and warnings"""
        log_analysis = {
            "critical_errors": 0,
            "warnings": 0,
            "recent_issues": [],
            "crash_reports": 0
        }
        
        try:
            # Check for crash reports
            crash_dir = Path.home() / "Library" / "Logs" / "CrashReporter"
            if crash_dir.exists():
                recent_crashes = list(crash_dir.glob("*.crash"))
                log_analysis["crash_reports"] = len(recent_crashes)
            
            # Analyze console logs (simplified)
            result = subprocess.run(
                ["log", "show", "--predicate", 'eventType == "logEvent"', 
                 "--last", "1h", "--style", "compact"],
                capture_output=True, text=True, timeout=30
            )
            
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'error' in line.lower():
                        log_analysis["critical_errors"] += 1
                    elif 'warning' in line.lower():
                        log_analysis["warnings"] += 1
                        
        except Exception as e:
            log_analysis["error"] = str(e)
        
        return log_analysis
    
    def _analyze_processes(self):
        """Analyze running processes for issues"""
        suspicious_processes = []
        high_cpu_processes = []
        memory_hogs = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > 50:
                    high_cpu_processes.append({
                        "name": proc.info['name'],
                        "pid": proc.info['pid'],
                        "cpu_percent": proc.info['cpu_percent']
                    })
                
                if proc.info['memory_percent'] > 10:
                    memory_hogs.append({
                        "name": proc.info['name'],
                        "pid": proc.info['pid'],
                        "memory_percent": round(proc.info['memory_percent'], 2)
                    })
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        return {
            "high_cpu_processes": high_cpu_processes[:5],
            "memory_intensive": memory_hogs[:5],
            "total_processes": len(list(psutil.process_iter()))
        }
    
    def _analyze_storage(self):
        """Comprehensive storage analysis"""
        storage_analysis = {
            "cache_cleanup_potential": self._calculate_cache_cleanup(),
            "duplicate_files": self._find_duplicate_files(),
            "large_files": self._find_large_files(),
            "trash_analysis": self._analyze_trash(),
            "downloads_cleanup": self._analyze_downloads()
        }
        return storage_analysis
    
    def _calculate_cache_cleanup(self):
        """Calculate potential cache cleanup space"""
        cache_dirs = [
            Path.home() / "Library" / "Caches",
            Path("/System/Library/Caches"),
            Path("/Library/Caches"),
            Path("/private/var/folders")
        ]
        
        total_cache_size = 0
        cleanable_caches = []
        
        for cache_dir in cache_dirs:
            if cache_dir.exists():
                try:
                    for item in cache_dir.rglob("*"):
                        if item.is_file():
                            size = item.stat().st_size
                            total_cache_size += size
                            
                            # Only suggest cleaning if file is older than 7 days
                            if (datetime.now() - datetime.fromtimestamp(item.stat().st_mtime)).days > 7:
                                cleanable_caches.append({
                                    "path": str(item),
                                    "size_mb": round(size / (1024**2), 2),
                                    "age_days": (datetime.now() - datetime.fromtimestamp(item.stat().st_mtime)).days
                                })
                except PermissionError:
                    continue
        
        return {
            "total_cache_size_gb": round(total_cache_size / (1024**3), 2),
            "cleanable_items": len(cleanable_caches),
            "potential_space_gb": round(sum(item["size_mb"] for item in cleanable_caches) / 1024, 2)
        }
    
    def _find_duplicate_files(self):
        """Find duplicate files by hash"""
        duplicates = {}
        file_hashes = {}
        
        # Check common directories for duplicates
        search_dirs = [
            Path.home() / "Desktop",
            Path.home() / "Downloads",
            Path.home() / "Documents"
        ]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                for file_path in search_dir.rglob("*"):
                    if file_path.is_file() and file_path.stat().st_size > 1024:  # Files > 1KB
                        try:
                            file_hash = self._calculate_file_hash(file_path)
                            if file_hash in file_hashes:
                                if file_hash not in duplicates:
                                    duplicates[file_hash] = [file_hashes[file_hash]]
                                duplicates[file_hash].append(str(file_path))
                            else:
                                file_hashes[file_hash] = str(file_path)
                        except:
                            continue
        
        return {
            "duplicate_sets": len(duplicates),
            "duplicate_files": sum(len(files) - 1 for files in duplicates.values()),
            "examples": dict(list(duplicates.items())[:3])  # Show first 3 examples
        }
    
    def _calculate_file_hash(self, file_path):
        """Calculate SHA-256 hash of file"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _find_large_files(self):
        """Find largest files on system"""
        large_files = []
        
        # Search in user directories
        search_dirs = [Path.home()]
        
        for search_dir in search_dirs:
            for file_path in search_dir.rglob("*"):
                if file_path.is_file():
                    try:
                        size = file_path.stat().st_size
                        if size > 100 * 1024 * 1024:  # Files > 100MB
                            large_files.append({
                                "path": str(file_path),
                                "size_mb": round(size / (1024**2), 2),
                                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                            })
                    except:
                        continue
        
        # Sort by size and return top 10
        large_files.sort(key=lambda x: x["size_mb"], reverse=True)
        return large_files[:10]
    
    def _analyze_trash(self):
        """Analyze trash/bin contents"""
        trash_path = Path.home() / ".Trash"
        if trash_path.exists():
            total_size = 0
            item_count = 0
            
            for item in trash_path.rglob("*"):
                if item.is_file():
                    total_size += item.stat().st_size
                    item_count += 1
            
            return {
                "items": item_count,
                "total_size_mb": round(total_size / (1024**2), 2),
                "can_empty": item_count > 0
            }
        return {"items": 0, "total_size_mb": 0, "can_empty": False}
    
    def _analyze_downloads(self):
        """Analyze Downloads folder"""
        downloads_path = Path.home() / "Downloads"
        if downloads_path.exists():
            old_files = []
            total_size = 0
            
            for item in downloads_path.iterdir():
                if item.is_file():
                    age_days = (datetime.now() - datetime.fromtimestamp(item.stat().st_mtime)).days
                    size = item.stat().st_size
                    total_size += size
                    
                    if age_days > 30:  # Files older than 30 days
                        old_files.append({
                            "name": item.name,
                            "size_mb": round(size / (1024**2), 2),
                            "age_days": age_days
                        })
            
            return {
                "total_files": len(list(downloads_path.iterdir())),
                "total_size_mb": round(total_size / (1024**2), 2),
                "old_files": len(old_files),
                "cleanup_potential_mb": round(sum(f["size_mb"] for f in old_files), 2)
            }
        return {"total_files": 0, "total_size_mb": 0, "old_files": 0}
    
    def _security_audit(self):
        """Perform security audit"""
        return {
            "firewall_status": self._check_firewall(),
            "gatekeeper_status": self._check_gatekeeper(),
            "sip_status": self._check_sip(),
            "user_permissions": self._check_permissions(),
            "suspicious_files": self._scan_suspicious_files()
        }
    
    def _check_firewall(self):
        """Check macOS firewall status"""
        try:
            result = subprocess.run(
                ["sudo", "pfctl", "-s", "info"],
                capture_output=True, text=True, timeout=10
            )
            return {"enabled": "Status: Enabled" in result.stdout, "details": result.stdout[:200]}
        except:
            return {"enabled": "unknown", "details": "Could not check firewall status"}
    
    def _check_gatekeeper(self):
        """Check Gatekeeper status"""
        try:
            result = subprocess.run(
                ["spctl", "--status"],
                capture_output=True, text=True, timeout=10
            )
            return {"enabled": "assessments enabled" in result.stdout.lower()}
        except:
            return {"enabled": "unknown"}
    
    def _check_sip(self):
        """Check System Integrity Protection"""
        try:
            result = subprocess.run(
                ["csrutil", "status"],
                capture_output=True, text=True, timeout=10
            )
            return {"enabled": "enabled" in result.stdout.lower(), "status": result.stdout.strip()}
        except:
            return {"enabled": "unknown", "status": "Could not check SIP"}
    
    def _check_permissions(self):
        """Check file permissions on critical directories"""
        critical_paths = [
            "/System",
            "/Applications",
            "/Library",
            str(Path.home() / "Library")
        ]
        
        permission_issues = []
        for path in critical_paths:
            if Path(path).exists():
                try:
                    stat = Path(path).stat()
                    mode = oct(stat.st_mode)[-3:]
                    if path == "/System" and mode != "755":
                        permission_issues.append(f"{path} has unusual permissions: {mode}")
                except:
                    permission_issues.append(f"Could not check permissions for {path}")
        
        return {"issues": permission_issues, "critical_paths_checked": len(critical_paths)}
    
    def _scan_suspicious_files(self):
        """Scan for potentially suspicious files"""
        suspicious_patterns = [
            "*.exe", "*.scr", "*.bat", "*.vbs", "*.js"
        ]
        
        suspicious_files = []
        search_dirs = [Path.home() / "Downloads", Path.home() / "Desktop"]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                for pattern in suspicious_patterns:
                    suspicious_files.extend(list(search_dir.glob(pattern)))
        
        return {
            "suspicious_files_found": len(suspicious_files),
            "files": [str(f) for f in suspicious_files[:5]]  # Show first 5
        }
    
    def _performance_metrics(self):
        """Collect performance metrics"""
        return {
            "boot_time": psutil.boot_time(),
            "cpu_count": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            "load_average": os.getloadavg(),
            "network_io": psutil.net_io_counters()._asdict(),
            "disk_io": psutil.disk_io_counters()._asdict() if psutil.disk_io_counters() else None
        }
    
    def _check_applications(self):
        """Check application health"""
        apps_dir = Path("/Applications")
        user_apps_dir = Path.home() / "Applications"
        
        app_analysis = {
            "total_applications": 0,
            "broken_applications": [],
            "duplicate_applications": [],
            "large_applications": []
        }
        
        app_names = {}
        
        for apps_path in [apps_dir, user_apps_dir]:
            if apps_path.exists():
                for app in apps_path.glob("*.app"):
                    app_analysis["total_applications"] += 1
                    
                    # Check for duplicates
                    app_name = app.stem
                    if app_name in app_names:
                        app_analysis["duplicate_applications"].append({
                            "name": app_name,
                            "paths": [app_names[app_name], str(app)]
                        })
                    else:
                        app_names[app_name] = str(app)
                    
                    # Check size
                    try:
                        size = sum(f.stat().st_size for f in app.rglob("*") if f.is_file())
                        if size > 1024**3:  # > 1GB
                            app_analysis["large_applications"].append({
                                "name": app.name,
                                "size_gb": round(size / (1024**3), 2)
                            })
                    except:
                        continue
        
        return app_analysis
    
    def _network_diagnostics(self):
        """Perform network diagnostics"""
        return {
            "connectivity": self._test_connectivity(),
            "dns_resolution": self._test_dns(),
            "network_interfaces": self._get_network_interfaces(),
            "open_connections": self._get_open_connections()
        }
    
    def _test_connectivity(self):
        """Test internet connectivity"""
        test_hosts = ["8.8.8.8", "1.1.1.1", "google.com"]
        connectivity_results = {}
        
        for host in test_hosts:
            try:
                result = subprocess.run(
                    ["ping", "-c", "3", host],
                    capture_output=True, text=True, timeout=10
                )
                connectivity_results[host] = result.returncode == 0
            except:
                connectivity_results[host] = False
        
        return connectivity_results
    
    def _test_dns(self):
        """Test DNS resolution"""
        try:
            import socket
            socket.gethostbyname("google.com")
            return {"status": "working", "test_domain": "google.com"}
        except:
            return {"status": "failed", "test_domain": "google.com"}
    
    def _get_network_interfaces(self):
        """Get network interface information"""
        interfaces = {}
        for interface, addrs in psutil.net_if_addrs().items():
            interfaces[interface] = [addr._asdict() for addr in addrs]
        return interfaces
    
    def _get_open_connections(self):
        """Get open network connections"""
        connections = []
        for conn in psutil.net_connections():
            if conn.status == 'ESTABLISHED':
                connections.append({
                    "local": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "unknown",
                    "remote": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "unknown",
                    "status": conn.status
                })
        return connections[:10]  # Return first 10
    
    def _check_file_integrity(self):
        """Check file system integrity"""
        return {
            "spotlight_index": self._check_spotlight(),
            "file_permissions": self._check_critical_file_permissions(),
            "symlink_integrity": self._check_symlinks()
        }
    
    def _check_spotlight(self):
        """Check Spotlight indexing status"""
        try:
            result = subprocess.run(
                ["mdutil", "-s", "/"],
                capture_output=True, text=True, timeout=10
            )
            return {"status": result.stdout.strip(), "healthy": "Indexing enabled" in result.stdout}
        except:
            return {"status": "unknown", "healthy": False}
    
    def _check_critical_file_permissions(self):
        """Check permissions on critical system files"""
        critical_files = [
            "/etc/hosts",
            "/etc/passwd", 
            "/System/Library/CoreServices/Finder.app"
        ]
        
        permission_check = {}
        for file_path in critical_files:
            if Path(file_path).exists():
                try:
                    stat = Path(file_path).stat()
                    permission_check[file_path] = oct(stat.st_mode)[-3:]
                except:
                    permission_check[file_path] = "error"
        
        return permission_check
    
    def _check_symlinks(self):
        """Check for broken symbolic links"""
        broken_links = []
        
        # Check common directories for broken symlinks
        check_dirs = [
            Path("/usr/local/bin"),
            Path("/Applications"),
            Path.home() / "Applications"
        ]
        
        for check_dir in check_dirs:
            if check_dir.exists():
                for item in check_dir.rglob("*"):
                    if item.is_symlink() and not item.exists():
                        broken_links.append(str(item))
        
        return {"broken_symlinks": broken_links[:10]}
    
    def _memory_analysis(self):
        """Analyze memory usage and optimization opportunities"""
        return {
            "memory_pressure": self._check_memory_pressure(),
            "swap_usage": psutil.swap_memory()._asdict(),
            "memory_by_process": self._get_memory_by_process()
        }
    
    def _get_memory_by_process(self):
        """Get memory usage by process"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                if proc.info['memory_percent'] > 1:  # Processes using > 1% memory
                    processes.append(proc.info)
            except:
                continue
        
        return sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:10]
    
    def _startup_analysis(self):
        """Analyze startup items and boot performance"""
        startup_items = []
        
        # Check LaunchAgents
        launch_paths = [
            Path.home() / "Library" / "LaunchAgents",
            Path("/Library/LaunchAgents"),
            Path("/System/Library/LaunchAgents")
        ]
        
        for launch_path in launch_paths:
            if launch_path.exists():
                for plist in launch_path.glob("*.plist"):
                    startup_items.append({
                        "name": plist.stem,
                        "path": str(plist),
                        "type": "LaunchAgent"
                    })
        
        return {
            "startup_items": len(startup_items),
            "items": startup_items[:20],  # Show first 20
            "boot_time_seconds": time.time() - psutil.boot_time()
        }
    
    def auto_heal_system(self, scan_results=None):
        """Automatically heal detected issues"""
        if scan_results is None:
            scan_results = self.scan_results
        
        healing_actions = []
        
        # Auto-fix permissions
        healing_actions.extend(self._fix_permissions())
        
        # Clean caches if needed
        healing_actions.extend(self._auto_clean_caches())
        
        # Optimize memory
        healing_actions.extend(self._optimize_memory())
        
        # Fix broken symlinks
        healing_actions.extend(self._fix_broken_symlinks())
        
        # Update system maintenance
        healing_actions.extend(self._run_maintenance_scripts())
        
        self.healing_log.extend(healing_actions)
        return {
            "actions_taken": len(healing_actions),
            "healing_log": healing_actions,
            "timestamp": datetime.now().isoformat()
        }
    
    def _fix_permissions(self):
        """Fix common permission issues"""
        actions = []
        try:
            # Reset permissions on user Library
            library_path = Path.home() / "Library"
            if library_path.exists():
                subprocess.run(["chmod", "-R", "755", str(library_path)], check=False)
                actions.append("Fixed permissions on user Library directory")
        except:
            actions.append("Could not fix Library permissions")
        
        return actions
    
    def _auto_clean_caches(self):
        """Automatically clean safe cache files"""
        actions = []
        
        # Clean user caches (safe ones)
        cache_dir = Path.home() / "Library" / "Caches"
        if cache_dir.exists():
            try:
                cleaned_size = 0
                for cache_subdir in cache_dir.iterdir():
                    if cache_subdir.is_dir():
                        # Only clean specific safe caches
                        safe_caches = ["com.apple.Safari", "com.google.Chrome"]
                        if any(safe in cache_subdir.name for safe in safe_caches):
                            for cache_file in cache_subdir.rglob("*"):
                                if cache_file.is_file():
                                    try:
                                        size = cache_file.stat().st_size
                                        cache_file.unlink()
                                        cleaned_size += size
                                    except:
                                        continue
                
                if cleaned_size > 0:
                    actions.append(f"Cleaned {round(cleaned_size / (1024**2), 2)}MB of cache files")
            except:
                actions.append("Could not clean cache files")
        
        return actions
    
    def _optimize_memory(self):
        """Optimize memory usage"""
        actions = []
        
        try:
            # Force memory pressure relief
            subprocess.run(["sudo", "purge"], check=False)
            actions.append("Forced memory purge to optimize RAM usage")
        except:
            actions.append("Could not force memory optimization")
        
        return actions
    
    def _fix_broken_symlinks(self):
        """Remove broken symbolic links"""
        actions = []
        
        check_dirs = [Path.home() / "Applications"]
        
        for check_dir in check_dirs:
            if check_dir.exists():
                for item in check_dir.rglob("*"):
                    if item.is_symlink() and not item.exists():
                        try:
                            item.unlink()
                            actions.append(f"Removed broken symlink: {item}")
                        except:
                            continue
        
        return actions
    
    def _run_maintenance_scripts(self):
        """Run system maintenance scripts"""
        actions = []
        
        maintenance_commands = [
            (["sudo", "periodic", "daily"], "Ran daily maintenance"),
            (["sudo", "periodic", "weekly"], "Ran weekly maintenance"),
            (["atsutil", "databases", "-remove"], "Reset font cache")
        ]
        
        for command, description in maintenance_commands:
            try:
                result = subprocess.run(command, capture_output=True, timeout=60)
                if result.returncode == 0:
                    actions.append(description)
            except:
                continue
        
        return actions
    
    def generate_health_report(self):
        """Generate comprehensive health report"""
        if not self.scan_results:
            self.comprehensive_diagnostic_scan()
        
        # Calculate overall health score
        health_score = self._calculate_health_score()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "overall_health_score": health_score,
            "scan_results": self.scan_results,
            "issues_found": self.issues_found,
            "recommendations": self._generate_recommendations(),
            "healing_log": self.healing_log,
            "next_scan_recommended": (datetime.now() + timedelta(hours=24)).isoformat()
        }
        
        return report
    
    def _calculate_health_score(self):
        """Calculate overall system health score (0-100)"""
        score = 100
        
        # Deduct points for various issues
        if self.scan_results:
            # CPU and memory issues
            if self.scan_results.get("system_health", {}).get("memory_pressure", {}).get("pressure_level") == "high":
                score -= 15
            
            # Storage issues
            storage = self.scan_results.get("storage_analysis", {})
            if storage.get("cache_cleanup_potential", {}).get("potential_space_gb", 0) > 5:
                score -= 10
            
            # Security issues
            security = self.scan_results.get("security_audit", {})
            if not security.get("firewall_status", {}).get("enabled", True):
                score -= 20
            
            # Application issues
            apps = self.scan_results.get("application_health", {})
            if apps.get("broken_applications"):
                score -= 5
            
            # Performance issues
            if len(self.scan_results.get("system_health", {}).get("process_analysis", {}).get("high_cpu_processes", [])) > 3:
                score -= 10
        
        return max(0, min(100, score))
    
    def _generate_recommendations(self):
        """Generate recommendations based on scan results"""
        recommendations = []
        
        if not self.scan_results:
            return ["Run diagnostic scan first"]
        
        # Storage recommendations
        storage = self.scan_results.get("storage_analysis", {})
        if storage.get("cache_cleanup_potential", {}).get("potential_space_gb", 0) > 2:
            recommendations.append("Clean cache files to free up storage space")
        
        if storage.get("duplicate_files", {}).get("duplicate_sets", 0) > 0:
            recommendations.append("Remove duplicate files to save space")
        
        # Memory recommendations
        memory = self.scan_results.get("system_health", {}).get("memory_pressure", {})
        if memory.get("pressure_level") == "high":
            recommendations.append("Close unnecessary applications to reduce memory pressure")
        
        # Security recommendations
        security = self.scan_results.get("security_audit", {})
        if not security.get("firewall_status", {}).get("enabled", True):
            recommendations.append("Enable macOS firewall for better security")
        
        # Performance recommendations
        processes = self.scan_results.get("system_health", {}).get("process_analysis", {})
        if len(processes.get("high_cpu_processes", [])) > 2:
            recommendations.append("Monitor high CPU usage processes")
        
        return recommendations

def main():
    """Main function for command-line usage"""
    perfectionist = PerfectionistAgent()
    
    print("🎯 Mission Control 96 - Perfectionist Agent")
    print("=" * 50)
    
    # Run comprehensive scan
    print("Starting comprehensive diagnostic scan...")
    scan_results = perfectionist.comprehensive_diagnostic_scan()
    
    # Auto-heal issues
    print("\nApplying automatic healing...")
    healing_results = perfectionist.auto_heal_system()
    
    # Generate report
    print("\nGenerating health report...")
    health_report = perfectionist.generate_health_report()
    
    # Display summary
    print(f"\n✅ Health Score: {health_report['overall_health_score']}/100")
    print(f"🔧 Healing Actions: {healing_results['actions_taken']}")
    print(f"💡 Recommendations: {len(health_report['recommendations'])}")
    
    # Save detailed report
    report_file = Path.home() / "Desktop" / f"perfectionist_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(health_report, f, indent=2)
    
    print(f"📄 Detailed report saved: {report_file}")

if __name__ == "__main__":
    main()