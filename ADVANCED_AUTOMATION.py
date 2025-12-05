#!/usr/bin/env python3
"""
Advanced Automation System
Intelligent workflows, monitoring, and automation for NOIZYLAB
"""

import os
import json
import subprocess
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
AUTO_CONFIG = NOIZYLAB / ".automation_config.json"

class AdvancedAutomation:
    def __init__(self):
        self.noizylab = NOIZYLAB
        self.config_file = AUTO_CONFIG
        self.load_config()
    
    def load_config(self):
        """Load automation configuration"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            self.config = {
                'scheduled_tasks': [],
                'monitors': [],
                'workflows': {},
                'last_run': {}
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def setup_daily_cleanup(self):
        """Setup daily automated cleanup"""
        print("🔧 Setting up daily cleanup automation...")
        
        cleanup_task = {
            'name': 'daily_cleanup',
            'type': 'cleanup',
            'schedule': 'daily',
            'time': '02:00',
            'actions': [
                {'type': 'remove_dsstore', 'enabled': True},
                {'type': 'clean_pycache', 'enabled': True},
                {'type': 'optimize_databases', 'enabled': True},
                {'type': 'rotate_logs', 'enabled': True, 'keep_days': 7}
            ]
        }
        
        # Add to scheduled tasks
        if not any(t['name'] == 'daily_cleanup' for t in self.config['scheduled_tasks']):
            self.config['scheduled_tasks'].append(cleanup_task)
            self.save_config()
            print("✅ Daily cleanup scheduled")
        else:
            print("ℹ️  Daily cleanup already configured")
    
    def setup_health_monitoring(self):
        """Setup project health monitoring"""
        print("🔧 Setting up health monitoring...")
        
        monitor = {
            'name': 'project_health',
            'type': 'health_check',
            'interval': 3600,  # 1 hour
            'checks': [
                {'type': 'disk_space', 'threshold': 90, 'action': 'alert'},
                {'type': 'large_files', 'threshold_mb': 100, 'action': 'report'},
                {'type': 'duplicate_projects', 'action': 'report'},
                {'type': 'stale_projects', 'days': 90, 'action': 'archive_suggestion'}
            ]
        }
        
        if not any(m['name'] == 'project_health' for m in self.config['monitors']):
            self.config['monitors'].append(monitor)
            self.save_config()
            print("✅ Health monitoring configured")
        else:
            print("ℹ️  Health monitoring already configured")
    
    def create_workflow(self, name: str, steps: List[Dict]):
        """Create a custom workflow"""
        workflow = {
            'name': name,
            'steps': steps,
            'created': datetime.now().isoformat(),
            'last_run': None,
            'run_count': 0
        }
        
        self.config['workflows'][name] = workflow
        self.save_config()
        print(f"✅ Workflow '{name}' created with {len(steps)} steps")
    
    def run_workflow(self, name: str):
        """Run a workflow"""
        if name not in self.config['workflows']:
            print(f"❌ Workflow '{name}' not found")
            return
        
        workflow = self.config['workflows'][name]
        print(f"🚀 Running workflow: {name}")
        print("=" * 80)
        
        for i, step in enumerate(workflow['steps'], 1):
            print(f"\n[{i}/{len(workflow['steps'])}] {step.get('name', f'Step {i}')}")
            
            action = step.get('action')
            if action == 'cleanup':
                self._run_cleanup()
            elif action == 'analyze':
                self._run_analysis()
            elif action == 'organize':
                self._run_organize()
            elif action == 'optimize':
                self._run_optimize()
            elif action == 'custom':
                self._run_custom_command(step.get('command'))
            
            time.sleep(0.5)  # Small delay between steps
        
        # Update workflow stats
        workflow['last_run'] = datetime.now().isoformat()
        workflow['run_count'] = workflow.get('run_count', 0) + 1
        self.save_config()
        
        print("\n" + "=" * 80)
        print(f"✅ Workflow '{name}' completed!")
    
    def _run_cleanup(self):
        """Run cleanup actions"""
        print("  🧹 Running cleanup...")
        subprocess.run(['bash', str(self.noizylab / 'FAST_CLEANUP.sh')], 
                      capture_output=True)
    
    def _run_analysis(self):
        """Run analysis"""
        print("  📊 Running analysis...")
        if (self.noizylab / 'CHECK_AGENTS.py').exists():
            subprocess.run(['python3', str(self.noizylab / 'CHECK_AGENTS.py')],
                          capture_output=True)
    
    def _run_organize(self):
        """Run organization"""
        print("  📦 Running organization...")
        if (self.noizylab / 'QUICK_ORGANIZE.py').exists():
            subprocess.run(['python3', str(self.noizylab / 'QUICK_ORGANIZE.py')],
                          capture_output=True)
    
    def _run_optimize(self):
        """Run optimization"""
        print("  ⚡ Running optimization...")
        # Optimize databases, etc.
        for db in self.noizylab.rglob('*.db'):
            try:
                subprocess.run(['sqlite3', str(db), 'VACUUM; ANALYZE;'],
                             capture_output=True, timeout=10)
            except:
                pass
    
    def _run_custom_command(self, command: str):
        """Run custom command"""
        if command:
            print(f"  🔧 Running: {command}")
            subprocess.run(command, shell=True, cwd=str(self.noizylab))
    
    def setup_default_workflows(self):
        """Setup default workflows"""
        print("🔧 Setting up default workflows...")
        
        # Weekly maintenance workflow
        weekly_maintenance = [
            {'name': 'Cleanup', 'action': 'cleanup'},
            {'name': 'Analysis', 'action': 'analyze'},
            {'name': 'Optimize', 'action': 'optimize'}
        ]
        self.create_workflow('weekly_maintenance', weekly_maintenance)
        
        # Full organization workflow
        full_org = [
            {'name': 'Cleanup', 'action': 'cleanup'},
            {'name': 'Organize', 'action': 'organize'},
            {'name': 'Analysis', 'action': 'analyze'},
            {'name': 'Optimize', 'action': 'optimize'}
        ]
        self.create_workflow('full_organization', full_org)
    
    def list_workflows(self):
        """List all workflows"""
        print("\n📋 Available Workflows:")
        print("=" * 80)
        
        if not self.config['workflows']:
            print("  No workflows configured")
            return
        
        for name, workflow in self.config['workflows'].items():
            print(f"\n  🔄 {name}")
            print(f"     Steps: {len(workflow['steps'])}")
            print(f"     Runs: {workflow.get('run_count', 0)}")
            if workflow.get('last_run'):
                print(f"     Last run: {workflow['last_run']}")
    
    def show_status(self):
        """Show automation status"""
        print("\n🤖 Automation Status:")
        print("=" * 80)
        
        print(f"\n📅 Scheduled Tasks: {len(self.config['scheduled_tasks'])}")
        for task in self.config['scheduled_tasks']:
            print(f"  • {task['name']} ({task.get('schedule', 'manual')})")
        
        print(f"\n👁️  Monitors: {len(self.config['monitors'])}")
        for monitor in self.config['monitors']:
            print(f"  • {monitor['name']} (interval: {monitor.get('interval', 'N/A')}s)")
        
        print(f"\n🔄 Workflows: {len(self.config['workflows'])}")
        for name in self.config['workflows']:
            print(f"  • {name}")

def main():
    print("=" * 80)
    print(" " * 20 + "ADVANCED AUTOMATION SYSTEM")
    print("=" * 80)
    
    auto = AdvancedAutomation()
    
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'setup':
            auto.setup_daily_cleanup()
            auto.setup_health_monitoring()
            auto.setup_default_workflows()
            print("\n✅ Automation setup complete!")
        
        elif command == 'workflows':
            auto.list_workflows()
        
        elif command == 'run':
            if len(sys.argv) > 2:
                auto.run_workflow(sys.argv[2])
            else:
                print("Usage: python3 ADVANCED_AUTOMATION.py run <workflow_name>")
        
        elif command == 'status':
            auto.show_status()
        
        else:
            print(f"Unknown command: {command}")
            print("\nUsage:")
            print("  python3 ADVANCED_AUTOMATION.py setup        # Setup automation")
            print("  python3 ADVANCED_AUTOMATION.py workflows    # List workflows")
            print("  python3 ADVANCED_AUTOMATION.py run <name>   # Run workflow")
            print("  python3 ADVANCED_AUTOMATION.py status       # Show status")
    else:
        print("\n🔧 Quick Setup:")
        print("  python3 ADVANCED_AUTOMATION.py setup")
        print("\n📋 List Workflows:")
        print("  python3 ADVANCED_AUTOMATION.py workflows")
        print("\n🚀 Run Workflow:")
        print("  python3 ADVANCED_AUTOMATION.py run weekly_maintenance")

if __name__ == "__main__":
    main()

