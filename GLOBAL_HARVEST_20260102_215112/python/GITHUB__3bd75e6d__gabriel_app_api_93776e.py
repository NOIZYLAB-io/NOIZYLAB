#!/usr/bin/env python3
"""
GABRIEL Unified Application API
Central API layer for controlling all applications through GABRIEL

Author: GABRIEL AI FAMILY
Date: November 12, 2025
"""

from application_controller_agent import ApplicationControllerAgent, Application
from workflow_automation_system import WorkflowAutomationSystem, WorkflowAction, ActionType
from performance_monitor_agent import PerformanceMonitorAgent
from typing import Dict, List, Optional
from datetime import datetime


class GabrielApplicationAPI:
    """
    Unified API for GABRIEL application control
    
    Provides single interface to launch, control, monitor, and automate
    all applications on the system.
    """
    
    def __init__(self):
        self.name = "GABRIEL_APP_API"
        
        # Initialize subsystems
        print("🚀 Initializing GABRIEL Application API...")
        self.appcon = ApplicationControllerAgent()
        self.workflow = WorkflowAutomationSystem()
        self.perfmon = PerformanceMonitorAgent()
        
        # Scan applications on startup
        print("📡 Scanning applications...")
        self.appcon.scan_applications()
        
        print("✅ GABRIEL Application API ready!\n")
    
    # === Application Control ===
    
    def launch(self, app_name: str) -> Dict:
        """Launch an application"""
        return self.appcon.launch_app(app_name)
    
    def quit(self, app_name: str, force: bool = False) -> Dict:
        """Quit an application"""
        return self.appcon.quit_app(app_name, force)
    
    def list_apps(self, category: Optional[str] = None) -> List[Dict]:
        """List all applications, optionally filtered by category"""
        if category:
            from application_controller_agent import AppCategory
            try:
                cat = AppCategory(category)
                return self.appcon.get_apps_by_category(cat)
            except ValueError:
                return {'error': f'Invalid category: {category}'}
        return [app.to_dict() for app in self.appcon.applications.values()]
    
    def get_running_apps(self) -> List[Dict]:
        """Get all currently running applications"""
        return self.appcon.get_running_apps()
    
    def get_app_info(self, app_name: str) -> Optional[Dict]:
        """Get detailed information about an application"""
        if app_name in self.appcon.applications:
            return self.appcon.applications[app_name].to_dict()
        return None
    
    # === Workflow Automation ===
    
    def run_workflow(self, workflow_name: str, dry_run: bool = False) -> Dict:
        """Execute a predefined workflow"""
        return self.workflow.execute_workflow(workflow_name, dry_run)
    
    def list_workflows(self) -> List[str]:
        """List all available workflows"""
        return self.workflow.list_workflows()
    
    def get_workflow_info(self, workflow_name: str) -> Dict:
        """Get information about a workflow"""
        return self.workflow.get_workflow_info(workflow_name)
    
    def create_custom_workflow(self, name: str, actions: List[Dict]) -> Dict:
        """
        Create a custom workflow
        
        Example:
            actions = [
                {'type': 'launch_app', 'target': 'Visual Studio Code'},
                {'type': 'wait', 'target': '3'},
                {'type': 'launch_app', 'target': 'iTerm'}
            ]
        """
        workflow_actions = []
        for action in actions:
            action_type = ActionType(action['type'])
            workflow_actions.append(WorkflowAction(
                action_type=action_type,
                target=action['target'],
                parameters=action.get('parameters', {})
            ))
        
        return self.workflow.create_workflow(name, workflow_actions)
    
    # === Performance Monitoring ===
    
    def get_system_metrics(self) -> Dict:
        """Get current system performance metrics"""
        return self.perfmon.collect_system_metrics()
    
    def get_process_metrics(self) -> List[Dict]:
        """Get metrics for all running processes"""
        return self.perfmon.collect_process_metrics()
    
    def get_health_score(self) -> int:
        """Get system health score (0-100)"""
        metrics = self.perfmon.collect_system_metrics()
        return self.perfmon.get_system_health_score(metrics)
    
    def get_performance_alerts(self) -> List[Dict]:
        """Get active performance alerts"""
        metrics = self.perfmon.collect_system_metrics()
        alerts = self.perfmon.analyze_performance(metrics)
        return [alert.to_dict() for alert in alerts]
    
    def get_optimization_recommendations(self) -> List[str]:
        """Get system optimization recommendations"""
        metrics = self.perfmon.collect_system_metrics()
        processes = self.perfmon.collect_process_metrics()
        return self.perfmon.get_optimization_recommendations(metrics, processes)
    
    # === Quick Actions ===
    
    def start_music_production(self) -> Dict:
        """Quick start: Launch music production environment"""
        return self.run_workflow('music_production_setup')
    
    def start_development(self) -> Dict:
        """Quick start: Launch development environment"""
        return self.run_workflow('dev_environment_setup')
    
    def start_content_creation(self) -> Dict:
        """Quick start: Launch content creation suite"""
        return self.run_workflow('content_creation_setup')
    
    def start_ai_research(self) -> Dict:
        """Quick start: Launch AI research session"""
        return self.run_workflow('ai_research_session')
    
    def optimize_system(self) -> Dict:
        """Run system optimization workflow"""
        return self.run_workflow('system_optimization')
    
    def backup_system(self) -> Dict:
        """Run daily backup workflow"""
        return self.run_workflow('daily_backup')
    
    # === Smart Features ===
    
    def auto_quit_high_resource_apps(self, cpu_threshold: float = 90.0) -> List[Dict]:
        """Automatically quit apps using excessive resources"""
        results = []
        processes = self.perfmon.collect_process_metrics()
        
        for proc in processes:
            if proc['cpu_percent'] > cpu_threshold:
                app_name = proc['name']
                if app_name in self.appcon.applications:
                    result = self.quit(app_name)
                    results.append({
                        'app': app_name,
                        'reason': f"High CPU usage: {proc['cpu_percent']:.1f}%",
                        'result': result
                    })
        
        return results
    
    def launch_app_suite(self, suite_name: str) -> Dict:
        """Launch a suite of related applications"""
        suites = {
            'music': ['Logic Pro', 'iZotope RX 11 Audio Editor', 'Arcade'],
            'dev': ['Visual Studio Code', 'iTerm', 'Docker', 'GitHub Desktop'],
            'content': ['Adobe Premiere Pro', 'Adobe Photoshop', 'Blender'],
            'ai': ['Claude', 'ChatGPT', 'Copilot', 'Perplexity'],
            'productivity': ['Keynote', 'Pages', 'Numbers', 'Google Chrome']
        }
        
        if suite_name not in suites:
            return {'success': False, 'error': f'Unknown suite: {suite_name}'}
        
        results = []
        for app_name in suites[suite_name]:
            result = self.launch(app_name)
            results.append(result)
        
        return {
            'success': True,
            'suite': suite_name,
            'apps_launched': len(results),
            'results': results
        }
    
    def get_automation_suggestions(self) -> List[Dict]:
        """Analyze usage patterns and suggest automation opportunities"""
        suggestions = []
        
        # Check frequently running apps
        running = self.get_running_apps()
        
        if len(running) >= 5:
            suggestions.append({
                'type': 'workflow',
                'description': f'You have {len(running)} apps running. Create a workflow to launch this combination?',
                'apps': [app['name'] for app in running]
            })
        
        # Check performance issues
        alerts = self.get_performance_alerts()
        if alerts:
            suggestions.append({
                'type': 'optimization',
                'description': f'{len(alerts)} performance issues detected. Run optimization workflow?',
                'alerts': alerts
            })
        
        # Check resource hogs
        processes = self.get_process_metrics()
        high_cpu = [p for p in processes if p['cpu_percent'] > 50]
        if high_cpu:
            suggestions.append({
                'type': 'resource_management',
                'description': f'{len(high_cpu)} apps using high CPU. Consider automating cleanup?',
                'processes': [p['name'] for p in high_cpu[:5]]
            })
        
        return suggestions
    
    # === Status & Reporting ===
    
    def get_comprehensive_status(self) -> Dict:
        """Get complete system status across all subsystems"""
        return {
            'timestamp': datetime.now().isoformat(),
            'system_health': self.get_health_score(),
            'applications': {
                'total': len(self.appcon.applications),
                'running': len(self.get_running_apps()),
                'automation_capable': len(self.appcon.get_automation_capable_apps())
            },
            'workflows': {
                'available': len(self.workflow.workflows),
                'executed': self.workflow.stats['workflows_executed']
            },
            'performance': {
                'alerts': len(self.get_performance_alerts()),
                'samples_collected': self.perfmon.stats['samples_collected']
            },
            'quick_actions': [
                'start_music_production',
                'start_development',
                'start_content_creation',
                'start_ai_research',
                'optimize_system',
                'backup_system'
            ]
        }
    
    def display_dashboard(self):
        """Display comprehensive dashboard"""
        status = self.get_comprehensive_status()
        metrics = self.get_system_metrics()
        health = self.get_health_score()
        
        print("\n" + "="*70)
        print("🌟 GABRIEL APPLICATION API - DASHBOARD")
        print("="*70)
        
        # System Health
        health_emoji = "🟢" if health >= 80 else "🟡" if health >= 60 else "🔴"
        print(f"\n{health_emoji} System Health: {health}/100")
        print(f"   CPU: {metrics['cpu']['percent']:.1f}%")
        print(f"   Memory: {metrics['memory']['percent']:.1f}%")
        print(f"   Disk: {metrics['disk']['percent']:.1f}%")
        
        # Applications
        print(f"\n📱 Applications:")
        print(f"   Total: {status['applications']['total']}")
        print(f"   Running: {status['applications']['running']}")
        print(f"   Automation Ready: {status['applications']['automation_capable']}")
        
        # Workflows
        print(f"\n⚡ Workflows:")
        print(f"   Available: {status['workflows']['available']}")
        print(f"   Executed Today: {status['workflows']['executed']}")
        
        # Performance
        alerts = self.get_performance_alerts()
        if alerts:
            print(f"\n⚠️  Active Alerts ({len(alerts)}):")
            for alert in alerts[:3]:
                emoji = "🔴" if alert['level'] == 'critical' else "🟡"
                print(f"   {emoji} {alert['message']}")
        
        # Running Apps
        running = self.get_running_apps()
        if running:
            print(f"\n🟢 Running Apps ({len(running)}):")
            for app in running[:5]:
                print(f"   • {app['name']} - CPU: {app['cpu_percent']:.1f}%")
        
        # Quick Actions
        print(f"\n🚀 Quick Actions:")
        for action in status['quick_actions']:
            print(f"   • {action}()")
        
        # Suggestions
        suggestions = self.get_automation_suggestions()
        if suggestions:
            print(f"\n💡 Automation Suggestions:")
            for sug in suggestions[:3]:
                print(f"   • {sug['description']}")
        
        print("\n" + "="*70 + "\n")


# === Convenience Functions ===

def init_api():
    """Initialize the GABRIEL Application API"""
    return GabrielApplicationAPI()


def quick_launch(*app_names):
    """Quick launch multiple applications"""
    api = init_api()
    results = []
    for app in app_names:
        results.append(api.launch(app))
    return results


def quick_quit(*app_names):
    """Quick quit multiple applications"""
    api = init_api()
    results = []
    for app in app_names:
        results.append(api.quit(app))
    return results


def main():
    """Main function for testing"""
    print("🌟 GABRIEL Unified Application API")
    print("=" * 70)
    
    # Initialize API
    api = GabrielApplicationAPI()
    
    # Display dashboard
    api.display_dashboard()
    
    # Show available workflows
    print("\n📋 Available Workflows:")
    for workflow in api.list_workflows():
        info = api.get_workflow_info(workflow)
        print(f"   • {workflow} ({info['actions']} actions)")
    
    # Show automation suggestions
    print("\n💡 Checking for automation opportunities...")
    suggestions = api.get_automation_suggestions()
    for sug in suggestions:
        print(f"   🔔 {sug['description']}")
    
    print("\n✅ API ready for use!")
    print("\nExample usage:")
    print("  api.launch('Visual Studio Code')")
    print("  api.start_music_production()")
    print("  api.get_health_score()")
    print("  api.optimize_system()")


if __name__ == "__main__":
    main()
