#!/usr/bin/env python3
"""
GABRIEL Application Controller Agent (APPCON)
Agent #21 - OPERATIONS DIVISION

Controls, monitors, and optimizes all installed applications on the system.
Provides unified interface for launching, managing, and integrating apps with GABRIEL.

Author: GABRIEL AI FAMILY
Date: November 12, 2025
"""

import os
import subprocess
import psutil
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class AppCategory(Enum):
    """Application categories"""
    MUSIC_PRODUCTION = "music_production"
    AUDIO_PLUGINS = "audio_plugins"
    VIDEO_EDITING = "video_editing"
    GRAPHICS_DESIGN = "graphics_design"
    AI_TOOLS = "ai_tools"
    DEVELOPMENT = "development"
    PRODUCTIVITY = "productivity"
    UTILITIES = "utilities"
    COMMUNICATION = "communication"
    BROWSER = "browser"
    SYSTEM = "system"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


class AppStatus(Enum):
    """Application running status"""
    RUNNING = "running"
    STOPPED = "stopped"
    CRASHED = "crashed"
    UNKNOWN = "unknown"


class Application:
    """Represents a single application"""
    
    def __init__(self, name: str, path: str, category: AppCategory):
        self.name = name
        self.path = path
        self.category = category
        self.version = None
        self.bundle_id = None
        self.cpu_usage = 0.0
        self.memory_usage = 0
        self.pid = None
        self.status = AppStatus.STOPPED
        self.launch_count = 0
        self.total_runtime = 0
        self.last_launched = None
        self.automation_capable = False
        self.gabriel_integrated = False
        
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'name': self.name,
            'path': self.path,
            'category': self.category.value,
            'version': self.version,
            'bundle_id': self.bundle_id,
            'status': self.status.value,
            'cpu_usage': self.cpu_usage,
            'memory_usage': self.memory_usage,
            'pid': self.pid,
            'launch_count': self.launch_count,
            'total_runtime': self.total_runtime,
            'last_launched': self.last_launched,
            'automation_capable': self.automation_capable,
            'gabriel_integrated': self.gabriel_integrated
        }


class ApplicationControllerAgent:
    """
    APPCON - Application Controller Agent
    
    Manages all installed applications on the system.
    """
    
    def __init__(self):
        self.name = "APPCON"
        self.division = "OPERATIONS"
        self.role = "Application Controller & System Optimizer"
        
        # Application registry
        self.applications: Dict[str, Application] = {}
        self.applications_dir = Path("/Applications")
        
        # Statistics
        self.stats = {
            'total_apps': 0,
            'running_apps': 0,
            'launches_today': 0,
            'total_cpu_usage': 0.0,
            'total_memory_usage': 0,
            'apps_scanned': 0,
            'scan_time': None
        }
        
        # Application database (key apps with metadata)
        self.app_database = self._initialize_app_database()
        
        # Performance thresholds
        self.performance_thresholds = {
            'cpu_high': 80.0,  # % CPU
            'memory_high': 2048,  # MB
            'response_slow': 5.0  # seconds
        }
        
        print(f"🎮 {self.name} - Application Controller Agent initialized")
        
    def _initialize_app_database(self) -> Dict[str, Dict]:
        """Initialize database of known applications with metadata"""
        return {
            # Music Production
            'Logic Pro': {
                'category': AppCategory.MUSIC_PRODUCTION,
                'automation': True,
                'bundle_id': 'com.apple.logic10',
                'scripting': 'AppleScript',
                'integration_priority': 'HIGH'
            },
            'Pro Tools': {
                'category': AppCategory.MUSIC_PRODUCTION,
                'automation': True,
                'bundle_id': 'com.avid.ProTools',
                'scripting': 'EUCON',
                'integration_priority': 'HIGH'
            },
            'Ableton Live': {
                'category': AppCategory.MUSIC_PRODUCTION,
                'automation': True,
                'bundle_id': 'com.ableton.live',
                'scripting': 'MIDI/OSC',
                'integration_priority': 'HIGH'
            },
            'Studio One': {
                'category': AppCategory.MUSIC_PRODUCTION,
                'automation': True,
                'bundle_id': 'com.presonus.studioone',
                'integration_priority': 'HIGH'
            },
            'FL Studio': {
                'category': AppCategory.MUSIC_PRODUCTION,
                'automation': True,
                'bundle_id': 'com.image-line.flstudio',
                'scripting': 'MIDI',
                'integration_priority': 'MEDIUM'
            },
            
            # AI Tools
            'Claude': {
                'category': AppCategory.AI_TOOLS,
                'automation': False,
                'bundle_id': 'com.anthropic.claude',
                'integration_priority': 'HIGH'
            },
            'ChatGPT': {
                'category': AppCategory.AI_TOOLS,
                'automation': False,
                'bundle_id': 'com.openai.chatgpt',
                'integration_priority': 'HIGH'
            },
            'Copilot': {
                'category': AppCategory.AI_TOOLS,
                'automation': False,
                'bundle_id': 'com.github.copilot',
                'integration_priority': 'HIGH'
            },
            
            # Development
            'Visual Studio Code': {
                'category': AppCategory.DEVELOPMENT,
                'automation': True,
                'bundle_id': 'com.microsoft.VSCode',
                'scripting': 'Extension API',
                'integration_priority': 'CRITICAL'
            },
            'Xcode': {
                'category': AppCategory.DEVELOPMENT,
                'automation': True,
                'bundle_id': 'com.apple.dt.Xcode',
                'scripting': 'xcodebuild',
                'integration_priority': 'HIGH'
            },
            'Docker': {
                'category': AppCategory.DEVELOPMENT,
                'automation': True,
                'bundle_id': 'com.docker.docker',
                'scripting': 'CLI',
                'integration_priority': 'HIGH'
            },
            
            # Browsers
            'Google Chrome': {
                'category': AppCategory.BROWSER,
                'automation': True,
                'bundle_id': 'com.google.Chrome',
                'scripting': 'ChromeDriver',
                'integration_priority': 'HIGH'
            },
            'Safari': {
                'category': AppCategory.BROWSER,
                'automation': True,
                'bundle_id': 'com.apple.Safari',
                'scripting': 'AppleScript',
                'integration_priority': 'MEDIUM'
            },
            
            # Video/Graphics
            'Blender': {
                'category': AppCategory.GRAPHICS_DESIGN,
                'automation': True,
                'bundle_id': 'org.blenderfoundation.blender',
                'scripting': 'Python API',
                'integration_priority': 'MEDIUM'
            },
            'Adobe Premiere Pro': {
                'category': AppCategory.VIDEO_EDITING,
                'automation': True,
                'bundle_id': 'com.adobe.PremierePro',
                'scripting': 'ExtendScript',
                'integration_priority': 'HIGH'
            },
            'DaVinci Resolve': {
                'category': AppCategory.VIDEO_EDITING,
                'automation': True,
                'bundle_id': 'com.blackmagic-design.DaVinciResolve',
                'scripting': 'Python API',
                'integration_priority': 'HIGH'
            },
            
            # Productivity
            'Keynote': {
                'category': AppCategory.PRODUCTIVITY,
                'automation': True,
                'bundle_id': 'com.apple.iWork.Keynote',
                'scripting': 'AppleScript',
                'integration_priority': 'MEDIUM'
            },
            'Microsoft Word': {
                'category': AppCategory.PRODUCTIVITY,
                'automation': True,
                'bundle_id': 'com.microsoft.Word',
                'scripting': 'VBA',
                'integration_priority': 'MEDIUM'
            }
        }
    
    def scan_applications(self) -> Dict:
        """Scan /Applications directory and catalog all apps"""
        print(f"\n🔍 Scanning applications in {self.applications_dir}...")
        scan_start = datetime.now()
        
        try:
            # Get all .app bundles
            app_bundles = list(self.applications_dir.glob("*.app"))
            
            for app_path in app_bundles:
                app_name = app_path.stem
                
                # Determine category
                category = self._categorize_app(app_name)
                
                # Create Application object
                app = Application(app_name, str(app_path), category)
                
                # Enhance with database info if available
                if app_name in self.app_database:
                    db_info = self.app_database[app_name]
                    app.category = db_info['category']
                    app.bundle_id = db_info.get('bundle_id')
                    app.automation_capable = db_info.get('automation', False)
                    app.gabriel_integrated = db_info.get('integration_priority') in ['CRITICAL', 'HIGH']
                
                # Try to get bundle info
                self._get_app_info(app)
                
                # Check if running
                self._check_app_status(app)
                
                self.applications[app_name] = app
                self.stats['apps_scanned'] += 1
            
            scan_end = datetime.now()
            self.stats['scan_time'] = (scan_end - scan_start).total_seconds()
            self.stats['total_apps'] = len(self.applications)
            
            print(f"✅ Scanned {self.stats['apps_scanned']} applications in {self.stats['scan_time']:.2f}s")
            
            return {
                'success': True,
                'apps_found': self.stats['total_apps'],
                'scan_time': self.stats['scan_time']
            }
            
        except Exception as e:
            print(f"❌ Error scanning applications: {e}")
            return {'success': False, 'error': str(e)}
    
    def _categorize_app(self, app_name: str) -> AppCategory:
        """Categorize application by name"""
        name_lower = app_name.lower()
        
        # Music production keywords
        if any(kw in name_lower for kw in ['logic', 'pro tools', 'ableton', 'fl studio', 'cubase', 
                                              'studio one', 'reaper', 'reason', 'bitwig']):
            return AppCategory.MUSIC_PRODUCTION
        
        # Audio plugins
        if any(kw in name_lower for kw in ['kontakt', 'omnisphere', 'keyscape', 'arcade', 
                                              'nexus', 'serum', 'massive', 'spitfire']):
            return AppCategory.AUDIO_PLUGINS
        
        # Video/Graphics
        if any(kw in name_lower for kw in ['premiere', 'after effects', 'davinci', 'final cut',
                                              'photoshop', 'illustrator', 'blender']):
            return AppCategory.VIDEO_EDITING if 'premiere' in name_lower or 'final' in name_lower else AppCategory.GRAPHICS_DESIGN
        
        # AI Tools
        if any(kw in name_lower for kw in ['claude', 'chatgpt', 'copilot', 'perplexity', 'ai']):
            return AppCategory.AI_TOOLS
        
        # Development
        if any(kw in name_lower for kw in ['xcode', 'visual studio', 'docker', 'terminal', 
                                              'iterm', 'github', 'sourcetree']):
            return AppCategory.DEVELOPMENT
        
        # Browsers
        if any(kw in name_lower for kw in ['chrome', 'safari', 'firefox', 'edge', 'brave']):
            return AppCategory.BROWSER
        
        # Communication
        if any(kw in name_lower for kw in ['slack', 'discord', 'zoom', 'teams', 'messenger']):
            return AppCategory.COMMUNICATION
        
        # Productivity
        if any(kw in name_lower for kw in ['keynote', 'pages', 'numbers', 'word', 'excel', 
                                              'powerpoint', 'notion', 'evernote']):
            return AppCategory.PRODUCTIVITY
        
        return AppCategory.OTHER
    
    def _get_app_info(self, app: Application):
        """Get application info from Info.plist"""
        try:
            plist_path = Path(app.path) / "Contents" / "Info.plist"
            if plist_path.exists():
                # Use plutil to read plist
                result = subprocess.run(
                    ['plutil', '-convert', 'json', '-o', '-', str(plist_path)],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if result.returncode == 0:
                    info = json.loads(result.stdout)
                    app.bundle_id = info.get('CFBundleIdentifier')
                    app.version = info.get('CFBundleShortVersionString') or info.get('CFBundleVersion')
        except Exception:
            pass  # Silent fail, optional info
    
    def _check_app_status(self, app: Application):
        """Check if application is currently running"""
        try:
            for proc in psutil.process_iter(['name', 'pid', 'cpu_percent', 'memory_info']):
                if proc.info['name'] and app.name in proc.info['name']:
                    app.status = AppStatus.RUNNING
                    app.pid = proc.info['pid']
                    app.cpu_usage = proc.info['cpu_percent'] or 0.0
                    app.memory_usage = (proc.info['memory_info'].rss / 1024 / 1024) if proc.info['memory_info'] else 0  # MB
                    self.stats['running_apps'] += 1
                    break
        except Exception:
            pass  # Process may have terminated
    
    def launch_app(self, app_name: str) -> Dict:
        """Launch an application"""
        if app_name not in self.applications:
            return {'success': False, 'error': f'Application {app_name} not found'}
        
        app = self.applications[app_name]
        
        try:
            print(f"🚀 Launching {app_name}...")
            subprocess.Popen(['open', '-a', app.path])
            
            app.launch_count += 1
            app.last_launched = datetime.now().isoformat()
            self.stats['launches_today'] += 1
            
            return {
                'success': True,
                'app': app_name,
                'message': f'{app_name} launched successfully'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def quit_app(self, app_name: str, force: bool = False) -> Dict:
        """Quit an application"""
        if app_name not in self.applications:
            return {'success': False, 'error': f'Application {app_name} not found'}
        
        app = self.applications[app_name]
        
        if app.status != AppStatus.RUNNING:
            return {'success': False, 'error': f'{app_name} is not running'}
        
        try:
            print(f"🛑 Quitting {app_name}...")
            
            if force:
                subprocess.run(['killall', '-9', app_name], check=True)
            else:
                subprocess.run(['osascript', '-e', f'quit app "{app_name}"'], check=True)
            
            app.status = AppStatus.STOPPED
            app.pid = None
            
            return {
                'success': True,
                'app': app_name,
                'message': f'{app_name} quit successfully'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_running_apps(self) -> List[Dict]:
        """Get list of currently running applications"""
        running = []
        
        for app in self.applications.values():
            if app.status == AppStatus.RUNNING:
                running.append(app.to_dict())
        
        return running
    
    def get_apps_by_category(self, category: AppCategory) -> List[Dict]:
        """Get applications by category"""
        return [
            app.to_dict() 
            for app in self.applications.values() 
            if app.category == category
        ]
    
    def get_performance_stats(self) -> Dict:
        """Get system-wide performance statistics"""
        # Update stats
        self.stats['total_cpu_usage'] = sum(app.cpu_usage for app in self.applications.values())
        self.stats['total_memory_usage'] = sum(app.memory_usage for app in self.applications.values())
        
        return {
            'total_apps': self.stats['total_apps'],
            'running_apps': len(self.get_running_apps()),
            'total_cpu_usage': f"{self.stats['total_cpu_usage']:.1f}%",
            'total_memory_usage': f"{self.stats['total_memory_usage']:.0f} MB",
            'launches_today': self.stats['launches_today']
        }
    
    def optimize_performance(self) -> Dict:
        """Identify and optimize performance issues"""
        issues = []
        
        for app in self.applications.values():
            if app.status == AppStatus.RUNNING:
                # Check CPU usage
                if app.cpu_usage > self.performance_thresholds['cpu_high']:
                    issues.append({
                        'app': app.name,
                        'issue': 'high_cpu',
                        'value': f"{app.cpu_usage:.1f}%",
                        'recommendation': 'Consider restarting or closing'
                    })
                
                # Check memory usage
                if app.memory_usage > self.performance_thresholds['memory_high']:
                    issues.append({
                        'app': app.name,
                        'issue': 'high_memory',
                        'value': f"{app.memory_usage:.0f} MB",
                        'recommendation': 'Memory leak possible, restart recommended'
                    })
        
        return {
            'issues_found': len(issues),
            'issues': issues,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_automation_capable_apps(self) -> List[Dict]:
        """Get list of apps that support automation"""
        return [
            app.to_dict() 
            for app in self.applications.values() 
            if app.automation_capable
        ]
    
    def get_gabriel_integrated_apps(self) -> List[Dict]:
        """Get list of apps integrated with GABRIEL"""
        return [
            app.to_dict() 
            for app in self.applications.values() 
            if app.gabriel_integrated
        ]
    
    def create_workflow(self, workflow_name: str, steps: List[Dict]) -> Dict:
        """Create automation workflow across multiple apps"""
        workflow = {
            'name': workflow_name,
            'steps': steps,
            'created': datetime.now().isoformat()
        }
        
        # Validate workflow
        for step in steps:
            app_name = step.get('app')
            if app_name not in self.applications:
                return {'success': False, 'error': f'App {app_name} not found'}
            
            if not self.applications[app_name].automation_capable:
                return {'success': False, 'error': f'App {app_name} does not support automation'}
        
        return {
            'success': True,
            'workflow': workflow,
            'message': f'Workflow "{workflow_name}" created with {len(steps)} steps'
        }
    
    def get_status(self) -> Dict:
        """Get agent status"""
        return {
            'agent': self.name,
            'division': self.division,
            'role': self.role,
            'statistics': self.get_performance_stats(),
            'categories': {cat.value: len(self.get_apps_by_category(cat)) for cat in AppCategory},
            'automation_ready': len(self.get_automation_capable_apps()),
            'gabriel_integrated': len(self.get_gabriel_integrated_apps())
        }
    
    def display_status(self):
        """Display formatted status"""
        status = self.get_status()
        
        print("\n" + "="*70)
        print(f"🎮 {self.name} - APPLICATION CONTROLLER STATUS")
        print("="*70)
        print(f"Division: {self.division}")
        print(f"Role: {self.role}")
        print(f"\n📊 Statistics:")
        print(f"   Total Applications: {status['statistics']['total_apps']}")
        print(f"   Currently Running: {status['statistics']['running_apps']}")
        print(f"   Automation Capable: {status['automation_ready']}")
        print(f"   GABRIEL Integrated: {status['gabriel_integrated']}")
        print(f"   CPU Usage: {status['statistics']['total_cpu_usage']}")
        print(f"   Memory Usage: {status['statistics']['total_memory_usage']}")
        print(f"   Launches Today: {status['statistics']['launches_today']}")
        
        print(f"\n📁 Categories:")
        for cat, count in status['categories'].items():
            if count > 0:
                print(f"   {cat}: {count}")
        
        print("="*70 + "\n")


def main():
    """Main function for testing"""
    print("🌟 GABRIEL Application Controller Agent")
    print("=" * 70)
    
    # Initialize agent
    appcon = ApplicationControllerAgent()
    
    # Scan applications
    result = appcon.scan_applications()
    
    if result['success']:
        # Display status
        appcon.display_status()
        
        # Show running apps
        running = appcon.get_running_apps()
        if running:
            print("\n🟢 Currently Running Applications:")
            for app in running[:10]:  # Show first 10
                print(f"   • {app['name']} - CPU: {app['cpu_usage']:.1f}% | RAM: {app['memory_usage']:.0f} MB")
        
        # Show automation-capable apps
        auto_apps = appcon.get_automation_capable_apps()
        if auto_apps:
            print(f"\n🤖 Automation-Capable Apps ({len(auto_apps)}):")
            for app in auto_apps[:10]:
                print(f"   • {app['name']} ({app['category']})")
        
        # Check performance
        perf = appcon.optimize_performance()
        if perf['issues_found'] > 0:
            print(f"\n⚠️  Performance Issues Found: {perf['issues_found']}")
            for issue in perf['issues']:
                print(f"   • {issue['app']}: {issue['issue']} - {issue['value']}")
                print(f"     → {issue['recommendation']}")


if __name__ == "__main__":
    main()
