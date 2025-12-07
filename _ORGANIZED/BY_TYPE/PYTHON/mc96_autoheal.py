#!/usr/bin/env python3
"""
MC96ECOUNIVERSE AUTO-HEALING SYSTEM
Automatically detects and fixes network performance issues
Created by CB_01 for ROB - GORUNFREE! 🚀
"""

import json
import subprocess
import time
import os
from datetime import datetime
from typing import Dict, List, Tuple

class MC96AutoHeal:
    """Automatic Network Optimization & Self-Healing"""
    
    def __init__(self):
        self.interface = 'en0'
        self.optimal_mtu = 9000
        self.optimal_tcp_send = 262144
        self.optimal_tcp_recv = 262144
        self.optimal_tcp_mss = 1440
        self.issues_found = []
        self.fixes_applied = []
        
    def check_mtu(self) -> Tuple[bool, str, int]:
        """Check if MTU is optimal"""
        try:
            result = subprocess.run(
                ['ifconfig', self.interface],
                capture_output=True,
                text=True
            )
            import re
            match = re.search(r'mtu (\d+)', result.stdout)
            if match:
                current_mtu = int(match.group(1))
                if current_mtu < self.optimal_mtu:
                    return False, f"MTU too low: {current_mtu} (should be {self.optimal_mtu})", current_mtu
                return True, f"MTU optimal: {current_mtu}", current_mtu
        except Exception as e:
            return False, f"Error checking MTU: {e}", 0
        return False, "Could not determine MTU", 0
    
    def check_tcp_buffers(self) -> Tuple[bool, str]:
        """Check if TCP buffers are optimal"""
        try:
            send = int(subprocess.run(
                ['sysctl', '-n', 'net.inet.tcp.sendspace'],
                capture_output=True, text=True
            ).stdout.strip())
            
            recv = int(subprocess.run(
                ['sysctl', '-n', 'net.inet.tcp.recvspace'],
                capture_output=True, text=True
            ).stdout.strip())
            
            if send < self.optimal_tcp_send or recv < self.optimal_tcp_recv:
                return False, f"TCP buffers suboptimal: send={send}, recv={recv}"
            return True, f"TCP buffers optimal: send={send}, recv={recv}"
        except Exception as e:
            return False, f"Error checking TCP buffers: {e}"
    
    def check_interface_status(self) -> Tuple[bool, str]:
        """Check if interface is up and active"""
        try:
            result = subprocess.run(
                ['ifconfig', self.interface],
                capture_output=True,
                text=True
            )
            if 'status: active' in result.stdout:
                return True, "Interface active"
            return False, "Interface not active"
        except Exception as e:
            return False, f"Error checking interface: {e}"
    
    def check_interface_errors(self) -> Tuple[bool, str, Dict]:
        """Check for interface errors"""
        try:
            result = subprocess.run(
                ['netstat', '-I', self.interface, '-b'],
                capture_output=True,
                text=True
            )
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 2:
                parts = lines[1].split()
                if len(parts) >= 10:
                    ierrs = int(parts[5])
                    oerrs = int(parts[8])
                    
                    if ierrs > 0 or oerrs > 0:
                        return False, f"Interface errors detected: {ierrs} input, {oerrs} output", {'ierrs': ierrs, 'oerrs': oerrs}
                    return True, "No interface errors", {'ierrs': 0, 'oerrs': 0}
        except Exception as e:
            return False, f"Error checking interface errors: {e}", {}
        return False, "Could not check errors", {}
    
    def check_gateway_connectivity(self) -> Tuple[bool, str, float]:
        """Check gateway connectivity and latency"""
        try:
            # Get gateway
            result = subprocess.run(
                ['netstat', '-rn'],
                capture_output=True,
                text=True
            )
            gateway = None
            for line in result.stdout.split('\n'):
                if 'default' in line and self.interface in line:
                    gateway = line.split()[1]
                    break
            
            if not gateway:
                return False, "No gateway found", 999.0
            
            # Ping gateway
            result = subprocess.run(
                ['ping', '-c', '5', '-i', '0.2', gateway],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return False, f"Gateway {gateway} not responding", 999.0
            
            # Parse latency
            import re
            match = re.search(r'min/avg/max/stddev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)', result.stdout)
            if match:
                avg_ms = float(match.group(2))
                if avg_ms > 10.0:
                    return False, f"Gateway latency high: {avg_ms:.2f}ms", avg_ms
                return True, f"Gateway responsive: {avg_ms:.2f}ms", avg_ms
        except Exception as e:
            return False, f"Error checking gateway: {e}", 999.0
        return False, "Could not check gateway", 999.0
    
    def diagnose(self) -> Dict:
        """Run full system diagnosis"""
        print("🔍 MC96ECOUNIVERSE AUTO-HEALING DIAGNOSTICS")
        print("=" * 50)
        print()
        
        diagnosis = {
            'timestamp': datetime.now().isoformat(),
            'checks': [],
            'issues': [],
            'health_score': 100
        }
        
        # Check 1: Interface Status
        print("📡 Checking interface status...", end=' ')
        ok, msg = self.check_interface_status()
        status_emoji = "✅" if ok else "❌"
        print(f"{status_emoji} {msg}")
        diagnosis['checks'].append({'name': 'Interface Status', 'passed': ok, 'message': msg})
        if not ok:
            diagnosis['issues'].append({'severity': 'critical', 'issue': msg})
            diagnosis['health_score'] -= 30
        
        # Check 2: MTU
        print("🚀 Checking MTU (Jumbo Frames)...", end=' ')
        ok, msg, mtu = self.check_mtu()
        status_emoji = "✅" if ok else "⚠️"
        print(f"{status_emoji} {msg}")
        diagnosis['checks'].append({'name': 'MTU', 'passed': ok, 'message': msg, 'value': mtu})
        if not ok:
            diagnosis['issues'].append({'severity': 'warning', 'issue': msg, 'fix': 'optimize'})
            diagnosis['health_score'] -= 15
        
        # Check 3: TCP Buffers
        print("⚡ Checking TCP buffers...", end=' ')
        ok, msg = self.check_tcp_buffers()
        status_emoji = "✅" if ok else "⚠️"
        print(f"{status_emoji} {msg}")
        diagnosis['checks'].append({'name': 'TCP Buffers', 'passed': ok, 'message': msg})
        if not ok:
            diagnosis['issues'].append({'severity': 'warning', 'issue': msg, 'fix': 'optimize'})
            diagnosis['health_score'] -= 15
        
        # Check 4: Interface Errors
        print("🔬 Checking interface errors...", end=' ')
        ok, msg, errs = self.check_interface_errors()
        status_emoji = "✅" if ok else "⚠️"
        print(f"{status_emoji} {msg}")
        diagnosis['checks'].append({'name': 'Interface Errors', 'passed': ok, 'message': msg})
        if not ok:
            diagnosis['issues'].append({'severity': 'warning', 'issue': msg})
            diagnosis['health_score'] -= 10
        
        # Check 5: Gateway Connectivity
        print("🌐 Checking gateway connectivity...", end=' ')
        ok, msg, latency = self.check_gateway_connectivity()
        status_emoji = "✅" if ok else "⚠️"
        print(f"{status_emoji} {msg}")
        diagnosis['checks'].append({'name': 'Gateway', 'passed': ok, 'message': msg, 'latency_ms': latency})
        if not ok:
            diagnosis['issues'].append({'severity': 'high', 'issue': msg})
            diagnosis['health_score'] -= 20
        
        print()
        return diagnosis
    
    def apply_fixes(self, diagnosis: Dict) -> Dict:
        """Apply fixes for identified issues"""
        fixes = {
            'timestamp': datetime.now().isoformat(),
            'fixes_applied': [],
            'fixes_failed': []
        }
        
        # Check if we need to optimize
        needs_optimization = any(
            issue.get('fix') == 'optimize' 
            for issue in diagnosis['issues']
        )
        
        if needs_optimization:
            print("🔧 APPLYING AUTOMATIC FIXES...")
            print()
            print("⚠️  Network optimization requires sudo access.")
            print("   Please run manually: sudo ./mc96_optimize.sh")
            print()
            fixes['fixes_failed'].append({
                'fix': 'Network Optimization',
                'reason': 'Requires sudo access'
            })
        
        return fixes
    
    def print_health_report(self, diagnosis: Dict):
        """Print health report"""
        print("=" * 50)
        print("📊 MC96ECOUNIVERSE HEALTH REPORT")
        print("=" * 50)
        print()
        
        score = diagnosis['health_score']
        
        # Health score visualization
        if score >= 90:
            emoji = "🔥"
            status = "EXCELLENT"
            color = "green"
        elif score >= 75:
            emoji = "✅"
            status = "GOOD"
            color = "green"
        elif score >= 60:
            emoji = "⚠️"
            status = "FAIR"
            color = "yellow"
        else:
            emoji = "❌"
            status = "NEEDS ATTENTION"
            color = "red"
        
        print(f"   {emoji} HEALTH SCORE: {score}/100 ({status})")
        print()
        
        # Issues summary
        if diagnosis['issues']:
            print(f"   🔍 ISSUES FOUND: {len(diagnosis['issues'])}")
            for issue in diagnosis['issues']:
                severity_emoji = {
                    'critical': '🔴',
                    'high': '🟠',
                    'warning': '🟡',
                    'info': '🔵'
                }.get(issue['severity'], '⚪')
                print(f"      {severity_emoji} {issue['issue']}")
            print()
        else:
            print("   ✅ NO ISSUES FOUND - System is optimal!")
            print()
        
        # Recommendations
        if score < 90:
            print("   💡 RECOMMENDATIONS:")
            if any('MTU' in issue['issue'] for issue in diagnosis['issues']):
                print("      • Run: sudo ./mc96_optimize.sh")
            if any('TCP' in issue['issue'] for issue in diagnosis['issues']):
                print("      • Optimize TCP stack for better performance")
            if any('Gateway' in issue['issue'] for issue in diagnosis['issues']):
                print("      • Check network connectivity and router")
            print()
        
        print("=" * 50)
        print()
    
    def auto_heal_loop(self, interval: int = 60):
        """Continuous auto-healing loop"""
        print("🔄 MC96ECOUNIVERSE AUTO-HEALING SERVICE")
        print("   Running continuous health monitoring...")
        print("   Check interval: {} seconds".format(interval))
        print("   Press Ctrl+C to stop")
        print()
        time.sleep(2)
        
        try:
            iteration = 0
            while True:
                iteration += 1
                print(f"\n{'='*50}")
                print(f"🔄 AUTO-HEAL CHECK #{iteration} - {datetime.now().strftime('%H:%M:%S')}")
                print(f"{'='*50}\n")
                
                diagnosis = self.diagnose()
                
                if diagnosis['issues']:
                    print(f"\n⚠️  Found {len(diagnosis['issues'])} issues!")
                    self.apply_fixes(diagnosis)
                else:
                    print("\n✅ System healthy - no action needed")
                
                print(f"\n💤 Next check in {interval} seconds...\n")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\n👋 Auto-healing stopped. GORUNFREE! 🎸🔥\n")

def main():
    """Main execution"""
    import sys
    
    healer = MC96AutoHeal()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--service':
        # Run as continuous service
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
        healer.auto_heal_loop(interval)
    else:
        # Run single diagnostic
        diagnosis = healer.diagnose()
        healer.print_health_report(diagnosis)
        
        if diagnosis['issues']:
            healer.apply_fixes(diagnosis)
        
        print("GORUNFREE! 🎸🔥")

if __name__ == '__main__':
    main()

