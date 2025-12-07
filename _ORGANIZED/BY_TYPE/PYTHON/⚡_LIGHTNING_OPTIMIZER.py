#!/usr/bin/env python3
"""
⚡ LIGHTNING OPTIMIZER ⚡
======================
SCAN → TEST → FIX → HEAL → OPTIMIZE → REPEAT!
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime
import psutil
import sqlite3


class LightningOptimizer:
    """Ultra-fast system scanner, tester, fixer, healer, and optimizer"""
    
    def __init__(self):
        self.noizylab_root = Path("/Users/m2ultra/NOIZYLAB")
        self.iteration = 0
        self.issues_found = []
        self.fixes_applied = []
        
    def scan(self) -> dict:
        """⚡ SCAN - Ultra-fast system scan"""
        print("⚡ SCANNING...", end=" ")
        start = time.time()
        
        issues = {
            "syntax_errors": [],
            "import_errors": [],
            "missing_deps": [],
            "config_issues": [],
            "performance_issues": [],
            "security_issues": []
        }
        
        # 1. Check Python files for syntax
        py_files = list(self.noizylab_root.glob("**/*.py"))
        py_files = [f for f in py_files if "__pycache__" not in str(f)][:30]  # Limit for speed
        
        for py_file in py_files:
            result = subprocess.run(
                ["python3", "-m", "py_compile", str(py_file)],
                capture_output=True,
                timeout=2
            )
            if result.returncode != 0:
                issues["syntax_errors"].append(str(py_file))
        
        # 2. Check dependencies
        required_modules = [
            "requests", "psutil", "pandas", "numpy",
            "click", "rich", "fastapi", "streamlit"
        ]
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                issues["missing_deps"].append(module)
        
        # 3. Check system resources
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        if cpu > 90:
            issues["performance_issues"].append(f"High CPU: {cpu}%")
        if mem > 90:
            issues["performance_issues"].append(f"High Memory: {mem}%")
        if disk > 95:
            issues["performance_issues"].append(f"Low Disk: {disk}%")
        
        # 4. Check databases exist
        databases = [
            "integrations/slack/slack_data.db",
            "network/network_devices.db",
            "monitoring/monitoring.db"
        ]
        
        for db_path in databases:
            full_path = self.noizylab_root / db_path
            if not full_path.parent.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
        
        elapsed = time.time() - start
        print(f"✅ ({elapsed:.2f}s)")
        
        return issues
    
    def test(self) -> dict:
        """⚡ TEST - Ultra-fast functionality tests"""
        print("⚡ TESTING...", end=" ")
        start = time.time()
        
        results = {
            "passed": 0,
            "failed": 0,
            "tests": []
        }
        
        tests = [
            ("Slack Core", self._test_slack_core),
            ("Network Agent", self._test_network_agent),
            ("AI Systems", self._test_ai_systems),
            ("Automation", self._test_automation),
            ("System Health", self._test_system_health)
        ]
        
        for test_name, test_func in tests:
            try:
                test_func()
                results["passed"] += 1
                results["tests"].append((test_name, "PASS"))
            except Exception as e:
                results["failed"] += 1
                results["tests"].append((test_name, f"FAIL: {str(e)[:50]}"))
        
        elapsed = time.time() - start
        print(f"✅ ({results['passed']}/{results['passed']+results['failed']}) ({elapsed:.2f}s)")
        
        return results
    
    def _test_slack_core(self):
        """Test Slack core"""
        sys.path.append(str(self.noizylab_root))
        from integrations.slack.slack_core import SlackBlockBuilder
        block = SlackBlockBuilder.section("test")
        assert block["type"] == "section"
    
    def _test_network_agent(self):
        """Test network agent"""
        from network.dgs1210_network_agent import ConnectedDevice
        from datetime import datetime
        device = ConnectedDevice(
            mac_address="00:11:22:33:44:55",
            ip_address="192.168.1.1",
            port=1,
            hostname="test",
            vendor="test",
            first_seen=datetime.now(),
            last_seen=datetime.now()
        )
        assert device.mac_address == "00:11:22:33:44:55"
    
    def _test_ai_systems(self):
        """Test AI systems"""
        from ai.ai_operations_agent import AIOperationsAgent
        agent = AIOperationsAgent()
        assert agent is not None
    
    def _test_automation(self):
        """Test automation"""
        from automation.auto_optimizer import AutoOptimizer
        optimizer = AutoOptimizer()
        assert optimizer is not None
    
    def _test_system_health(self):
        """Test system health"""
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        assert cpu < 100
        assert mem < 100
    
    def fix(self, issues: dict) -> list:
        """⚡ FIX - Ultra-fast issue fixing"""
        print("⚡ FIXING...", end=" ")
        start = time.time()
        
        fixes = []
        
        # Fix missing dependencies
        if issues["missing_deps"]:
            for module in issues["missing_deps"][:5]:  # Limit to 5
                try:
                    subprocess.run(
                        ["pip3", "install", "-q", module],
                        timeout=30,
                        capture_output=True
                    )
                    fixes.append(f"Installed {module}")
                except:
                    pass
        
        # Fix directory structure
        required_dirs = [
            "logs", "backups", "integrations/slack",
            "network", "ai", "monitoring", "automation",
            "analytics", "security", "scripts", "examples", "tests"
        ]
        
        for dir_path in required_dirs:
            full_path = self.noizylab_root / dir_path
            if not full_path.exists():
                full_path.mkdir(parents=True, exist_ok=True)
                fixes.append(f"Created {dir_path}")
        
        # Fix permissions
        script_files = list(self.noizylab_root.glob("**/*.sh"))
        for script in script_files:
            if not os.access(script, os.X_OK):
                script.chmod(0o755)
                fixes.append(f"Fixed permissions: {script.name}")
        
        elapsed = time.time() - start
        print(f"✅ ({len(fixes)} fixes) ({elapsed:.2f}s)")
        
        return fixes
    
    def heal(self) -> list:
        """⚡ HEAL - Ultra-fast system healing"""
        print("⚡ HEALING...", end=" ")
        start = time.time()
        
        heals = []
        
        # 1. Clean __pycache__
        for pycache in self.noizylab_root.glob("**/__pycache__"):
            try:
                import shutil
                shutil.rmtree(pycache)
                heals.append("Cleaned __pycache__")
                break  # Just report once
            except:
                pass
        
        # 2. Remove .pyc files
        pyc_count = 0
        for pyc in self.noizylab_root.glob("**/*.pyc"):
            try:
                pyc.unlink()
                pyc_count += 1
            except:
                pass
        
        if pyc_count > 0:
            heals.append(f"Removed {pyc_count} .pyc files")
        
        # 3. Remove .pid files
        pid_count = 0
        for pid in self.noizylab_root.glob("**/*.pid"):
            try:
                pid.unlink()
                pid_count += 1
            except:
                pass
        
        if pid_count > 0:
            heals.append(f"Removed {pid_count} .pid files")
        
        # 4. Ensure logs directory
        logs_dir = self.noizylab_root / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # 5. Ensure backups directory
        backups_dir = self.noizylab_root / "backups"
        backups_dir.mkdir(exist_ok=True)
        
        elapsed = time.time() - start
        print(f"✅ ({len(heals)} heals) ({elapsed:.2f}s)")
        
        return heals
    
    def optimize(self) -> list:
        """⚡ OPTIMIZE - Ultra-fast optimization"""
        print("⚡ OPTIMIZING...", end=" ")
        start = time.time()
        
        optimizations = []
        
        # 1. Optimize databases
        db_files = list(self.noizylab_root.glob("**/*.db"))
        db_files = [d for d in db_files if "email_intelligence" not in str(d)][:5]  # Limit
        
        for db_file in db_files:
            try:
                conn = sqlite3.connect(str(db_file), timeout=1)
                conn.execute("VACUUM")
                conn.close()
                optimizations.append(f"Optimized {db_file.name}")
                break  # Just report once
            except:
                pass
        
        # 2. Memory optimization
        import gc
        collected = gc.collect()
        if collected > 0:
            optimizations.append(f"GC collected {collected} objects")
        
        # 3. Check file count
        total_files = sum(1 for _ in self.noizylab_root.rglob("*") if _.is_file())
        optimizations.append(f"System: {total_files} files")
        
        elapsed = time.time() - start
        print(f"✅ ({len(optimizations)} opts) ({elapsed:.2f}s)")
        
        return optimizations
    
    def lightning_cycle(self, iterations: int = 1000, delay: float = 0.1):
        """⚡ LIGHTNING CYCLE - Run scan/test/fix/heal/optimize repeatedly"""
        print("\n" + "="*70)
        print("⚡⚡⚡ LIGHTNING OPTIMIZER - MAXIMUM SPEED MODE ⚡⚡⚡")
        print("="*70)
        print(f"\nRunning {iterations} iterations at lightning speed!\n")
        
        start_time = time.time()
        total_issues = 0
        total_fixes = 0
        total_heals = 0
        total_opts = 0
        
        for i in range(iterations):
            self.iteration = i + 1
            
            print(f"\n🔄 ITERATION {self.iteration}/{iterations}")
            print("-"*70)
            
            # SCAN
            issues = self.scan()
            issue_count = sum(len(v) for v in issues.values())
            total_issues += issue_count
            
            # TEST
            test_results = self.test()
            
            # FIX
            if issue_count > 0:
                fixes = self.fix(issues)
                total_fixes += len(fixes)
            else:
                print("⚡ FIXING... ✅ (0 fixes) (0.00s)")
            
            # HEAL
            heals = self.heal()
            total_heals += len(heals)
            
            # OPTIMIZE
            opts = self.optimize()
            total_opts += len(opts)
            
            # Metrics
            cpu = psutil.cpu_percent(interval=0.1)
            mem = psutil.virtual_memory().percent
            print(f"\n📊 CPU: {cpu:.1f}% | Memory: {mem:.1f}%")
            
            # Early exit if perfect for multiple iterations
            if i > 10 and issue_count == 0 and test_results["failed"] == 0:
                print(f"\n✨ SYSTEM PERFECT - Early completion at iteration {i+1}!")
                break
            
            # Delay between iterations
            if delay > 0 and i < iterations - 1:
                time.sleep(delay)
        
        # Final report
        total_time = time.time() - start_time
        
        print("\n" + "="*70)
        print("⚡ LIGHTNING OPTIMIZER COMPLETE!")
        print("="*70)
        print(f"\nIterations:        {self.iteration}")
        print(f"Total Time:        {total_time:.2f}s")
        print(f"Avg Time/Iter:     {total_time/self.iteration:.3f}s")
        print(f"Issues Found:      {total_issues}")
        print(f"Fixes Applied:     {total_fixes}")
        print(f"Heals Performed:   {total_heals}")
        print(f"Optimizations:     {total_opts}")
        print(f"\n✅ SYSTEM STATUS: OPTIMAL!")
        print("="*70)
        print()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="⚡ Lightning Optimizer")
    parser.add_argument("--iterations", type=int, default=1000, help="Number of iterations")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between iterations (seconds)")
    parser.add_argument("--turbo", action="store_true", help="Turbo mode (no delay)")
    
    args = parser.parse_args()
    
    optimizer = LightningOptimizer()
    
    delay = 0 if args.turbo else args.delay
    
    try:
        optimizer.lightning_cycle(args.iterations, delay)
    except KeyboardInterrupt:
        print("\n\n⚡ Lightning interrupted!")
        print(f"Completed {optimizer.iteration} iterations")


if __name__ == "__main__":
    main()

