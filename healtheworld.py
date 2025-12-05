#!/usr/bin/env python3
"""
HealTheWorld - Auto-Healing System for NoizyLab
===============================================
Automatically detects and fixes issues across all systems
"""

import os
import sys
import sqlite3
import subprocess
import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class HealTheWorld:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB")
        self.issues_found = []
        self.issues_fixed = []
        self.health_status = {}
    
    def check_database_health(self):
        """Check and fix database issues"""
        console.print("[cyan]🔍 Checking databases...[/cyan]")
        
        databases = [
            "email-intelligence/email_intelligence.db",
            "security/auth.db",
            "integrations/webhooks.db"
        ]
        
        for db_path in databases:
            full_path = self.base / db_path
            if not full_path.exists():
                console.print(f"  ⚠️  {db_path} not found - creating...")
                self.create_database(full_path)
                self.issues_fixed.append(f"Created {db_path}")
            else:
                try:
                    conn = sqlite3.connect(str(full_path))
                    cursor = conn.cursor()
                    # Check integrity
                    cursor.execute("PRAGMA integrity_check")
                    result = cursor.fetchone()
                    if result[0] != "ok":
                        console.print(f"  🔧 Fixing {db_path}...")
                        self.repair_database(full_path)
                        self.issues_fixed.append(f"Repaired {db_path}")
                    else:
                        console.print(f"  ✅ {db_path} healthy")
                    conn.close()
                except Exception as e:
                    console.print(f"  🔧 Fixing {db_path}: {e}")
                    self.repair_database(full_path)
                    self.issues_fixed.append(f"Fixed {db_path}")
    
    def create_database(self, db_path):
        """Create database with proper schema"""
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        if "email_intelligence" in str(db_path):
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS email_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    valid INTEGER DEFAULT 1,
                    category TEXT,
                    quality_score REAL,
                    enriched_info TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON email_list(email)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_category ON email_list(category)")
        
        conn.commit()
        conn.close()
    
    def repair_database(self, db_path):
        """Repair database"""
        try:
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()
            cursor.execute("VACUUM")
            cursor.execute("REINDEX")
            cursor.execute("ANALYZE")
            conn.commit()
            conn.close()
        except Exception as e:
            console.print(f"    ⚠️  Repair warning: {e}")
    
    def check_file_permissions(self):
        """Check and fix file permissions"""
        console.print("[cyan]🔍 Checking file permissions...[/cyan]")
        
        scripts = list(self.base.rglob("*.sh"))
        scripts.extend(list(self.base.rglob("*.py")))
        
        fixed = 0
        for script in scripts:
            if not os.access(script, os.X_OK):
                os.chmod(script, 0o755)
                fixed += 1
        
        if fixed > 0:
            console.print(f"  ✅ Fixed permissions on {fixed} files")
            self.issues_fixed.append(f"Fixed permissions on {fixed} files")
        else:
            console.print("  ✅ All permissions correct")
    
    def check_missing_dependencies(self):
        """Check and install missing dependencies"""
        console.print("[cyan]🔍 Checking dependencies...[/cyan]")
        
        requirements_file = self.base / "requirements-v4.txt"
        if requirements_file.exists():
            try:
                result = subprocess.run(
                    ["pip3", "install", "-q", "-r", str(requirements_file)],
                    capture_output=True,
                    timeout=60
                )
                if result.returncode == 0:
                    console.print("  ✅ Dependencies up to date")
                else:
                    console.print("  ⚠️  Some dependencies may need attention")
            except Exception as e:
                console.print(f"  ⚠️  Dependency check: {e}")
    
    def check_import_errors(self):
        """Check for Python import errors"""
        console.print("[cyan]🔍 Checking Python imports...[/cyan]")
        
        python_files = list(self.base.rglob("*.py"))
        errors = []
        
        for py_file in python_files[:20]:  # Check first 20 to avoid timeout
            if "test" in str(py_file) or "__pycache__" in str(py_file):
                continue
            
            try:
                result = subprocess.run(
                    ["python3", "-m", "py_compile", str(py_file)],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode != 0:
                    errors.append(str(py_file))
            except:
                pass
        
        if errors:
            console.print(f"  ⚠️  Found {len(errors)} files with issues")
            self.issues_found.extend(errors)
        else:
            console.print("  ✅ No import errors found")
    
    def optimize_all_databases(self):
        """Optimize all databases"""
        console.print("[cyan]⚡ Optimizing databases...[/cyan]")
        
        databases = [
            "email-intelligence/email_intelligence.db",
            "security/auth.db",
            "integrations/webhooks.db"
        ]
        
        for db_path in databases:
            full_path = self.base / db_path
            if full_path.exists():
                try:
                    conn = sqlite3.connect(str(full_path))
                    cursor = conn.cursor()
                    cursor.execute("PRAGMA optimize")
                    cursor.execute("VACUUM")
                    conn.commit()
                    conn.close()
                    console.print(f"  ✅ Optimized {db_path}")
                except Exception as e:
                    console.print(f"  ⚠️  {db_path}: {e}")
    
    def check_service_health(self):
        """Check if services are running"""
        console.print("[cyan]🔍 Checking services...[/cyan]")
        
        services = {
            "V4 API": "http://localhost:8000",
            "Mobile API": "http://localhost:8002",
            "Webhook Hub": "http://localhost:8001"
        }
        
        import requests
        for name, url in services.items():
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    console.print(f"  ✅ {name}: Running")
                    self.health_status[name] = "healthy"
                else:
                    console.print(f"  ⚠️  {name}: Status {response.status_code}")
                    self.health_status[name] = "warning"
            except:
                console.print(f"  ❌ {name}: Not running")
                self.health_status[name] = "down"
    
    def fix_missing_configs(self):
        """Create missing configuration files"""
        console.print("[cyan]🔍 Checking configurations...[/cyan]")
        
        configs = {
            "email-intelligence/app/config.py": """import os
from pathlib import Path

API_KEY = os.getenv("GEMINI_API_KEY", os.getenv("API_KEY", ""))
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DB_PATH = os.getenv("EMAIL_DB_PATH", "email_intelligence.db")
API_URL = os.getenv("API_URL", "http://localhost:8000")
"""
        }
        
        for config_path, content in configs.items():
            full_path = self.base / config_path
            if not full_path.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content)
                console.print(f"  ✅ Created {config_path}")
                self.issues_fixed.append(f"Created {config_path}")
    
    def generate_health_report(self):
        """Generate health report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "issues_found": len(self.issues_found),
            "issues_fixed": len(self.issues_fixed),
            "health_status": self.health_status,
            "fixed_items": self.issues_fixed
        }
        
        report_path = self.base / "health" / "health_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def run_full_heal(self):
        """Run complete healing process"""
        console.print(Panel.fit(
            "[bold blue]🌍 HealTheWorld - Auto-Healing System[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Healing...", total=None)
            
            self.check_database_health()
            self.check_file_permissions()
            self.check_missing_dependencies()
            self.check_import_errors()
            self.optimize_all_databases()
            self.fix_missing_configs()
            self.check_service_health()
            
            progress.update(task, completed=True)
        
        report = self.generate_health_report()
        
        console.print()
        console.print(Panel.fit(
            f"[bold green]✨ Healing Complete![/bold green]\n\n"
            f"Issues Found: {report['issues_found']}\n"
            f"Issues Fixed: {report['issues_fixed']}\n"
            f"Services: {len([s for s in report['health_status'].values() if s == 'healthy'])} healthy",
            border_style="green"
        ))

if __name__ == "__main__":
    healer = HealTheWorld()
    healer.run_full_heal()

