#!/usr/bin/env python3
"""
MC96ECOUNIVERSE DEVICE SCANNER
Detects, fingerprints, and manages MC96 devices on the network
Created by CB_01 for ROB - GORUNFREE! 🚀
"""

import subprocess
import re
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple

class MC96Scanner:
    """MC96 Network Device Scanner and Manager"""
    
    def __init__(self, interface: str = "en0"):
        self.interface = interface
        self.devices = {}
        self.gateway = None
        self.local_ip = None
        
    def get_network_info(self) -> Tuple[str, str]:
        """Get local IP and gateway"""
        try:
            # Get local IP
            result = subprocess.run(
                ['ifconfig', self.interface],
                capture_output=True,
                text=True
            )
            ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', result.stdout)
            self.local_ip = ip_match.group(1) if ip_match else None
            
            # Get gateway
            result = subprocess.run(
                ['netstat', '-rn'],
                capture_output=True,
                text=True
            )
            for line in result.stdout.split('\n'):
                if 'default' in line and self.interface in line:
                    parts = line.split()
                    self.gateway = parts[1]
                    break
                    
            return self.local_ip, self.gateway
        except Exception as e:
            print(f"❌ Error getting network info: {e}")
            return None, None
    
    def get_arp_table(self) -> Dict[str, str]:
        """Get ARP table with IP -> MAC mappings"""
        devices = {}
        try:
            result = subprocess.run(
                ['arp', '-a'],
                capture_output=True,
                text=True
            )
            for line in result.stdout.split('\n'):
                # Parse: ? (10.0.0.1) at aa:bb:cc:dd:ee:ff on en0 ifscope [ethernet]
                match = re.search(r'\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-f:]+)\s+on\s+(\w+)', line)
                if match:
                    ip, mac, iface = match.groups()
                    if iface == self.interface:
                        devices[ip] = mac
        except Exception as e:
            print(f"❌ Error reading ARP table: {e}")
        return devices
    
    def ping_device(self, ip: str, count: int = 3, timeout: int = 1) -> Dict:
        """Ping device and return statistics"""
        try:
            result = subprocess.run(
                ['ping', '-c', str(count), '-W', str(timeout * 1000), ip],
                capture_output=True,
                text=True,
                timeout=count * timeout + 2
            )
            
            # Parse ping statistics
            stats = {
                'ip': ip,
                'responsive': result.returncode == 0,
                'packet_loss': 100.0,
                'min_ms': 0,
                'avg_ms': 0,
                'max_ms': 0,
                'stddev_ms': 0
            }
            
            if stats['responsive']:
                # Extract packet loss
                loss_match = re.search(r'(\d+\.?\d*)% packet loss', result.stdout)
                if loss_match:
                    stats['packet_loss'] = float(loss_match.group(1))
                
                # Extract latency stats
                latency_match = re.search(
                    r'min/avg/max/stddev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)', 
                    result.stdout
                )
                if latency_match:
                    stats['min_ms'] = float(latency_match.group(1))
                    stats['avg_ms'] = float(latency_match.group(2))
                    stats['max_ms'] = float(latency_match.group(3))
                    stats['stddev_ms'] = float(latency_match.group(4))
            
            return stats
        except Exception as e:
            return {
                'ip': ip,
                'responsive': False,
                'error': str(e)
            }
    
    def identify_device_type(self, ip: str, mac: str, ping_stats: Dict) -> str:
        """Identify device type based on characteristics"""
        avg_latency = ping_stats.get('avg_ms', 999)
        stddev = ping_stats.get('stddev_ms', 999)
        
        # Device classification based on performance
        if avg_latency < 1.0 and stddev < 0.1:
            return "MC96_SWITCH_DGS1210"
        elif avg_latency < 2.0 and stddev < 1.5:
            return "MC96_NODE_WIRED"
        elif avg_latency < 5.0:
            return "MC96_NODE_WIRELESS"
        elif avg_latency < 20.0:
            return "NETWORK_DEVICE"
        else:
            return "UNKNOWN"
    
    def get_device_vendor(self, mac: str) -> str:
        """Get device vendor from MAC address OUI"""
        # Common OUI prefixes (first 3 octets)
        oui_database = {
            '6c:02:e0': 'D-Link',
            '00:26:08': 'Apple',
            '48:9e:bd': 'Generic',
            'a4:fc:14': 'Apple',
            'c0:94:35': 'Apple',
        }
        
        mac_prefix = ':'.join(mac.split(':')[:3]).lower()
        return oui_database.get(mac_prefix, 'Unknown')
    
    def scan_network(self) -> Dict:
        """Full network scan and device detection"""
        print("🔍 MC96ECOUNIVERSE DEVICE SCANNER")
        print("=" * 50)
        print()
        
        # Get network info
        print("📡 Getting network information...")
        local_ip, gateway = self.get_network_info()
        print(f"   Local IP: {local_ip}")
        print(f"   Gateway: {gateway}")
        print()
        
        # Get ARP table
        print("📋 Reading ARP table...")
        arp_devices = self.get_arp_table()
        print(f"   Found {len(arp_devices)} devices")
        print()
        
        # Scan each device
        print("🧪 Testing device performance...")
        results = {
            'scan_time': datetime.now().isoformat(),
            'interface': self.interface,
            'local_ip': local_ip,
            'gateway': gateway,
            'devices': []
        }
        
        for ip, mac in sorted(arp_devices.items()):
            if ip == local_ip:
                continue  # Skip self
                
            print(f"   Testing {ip}...", end=' ')
            
            ping_stats = self.ping_device(ip, count=5)
            device_type = self.identify_device_type(ip, mac, ping_stats)
            vendor = self.get_device_vendor(mac)
            
            device_info = {
                'ip': ip,
                'mac': mac,
                'vendor': vendor,
                'type': device_type,
                'responsive': ping_stats['responsive'],
                'latency_avg_ms': ping_stats.get('avg_ms', 0),
                'latency_min_ms': ping_stats.get('min_ms', 0),
                'latency_max_ms': ping_stats.get('max_ms', 0),
                'latency_stddev_ms': ping_stats.get('stddev_ms', 0),
                'packet_loss_pct': ping_stats.get('packet_loss', 100),
                'quality': self._calculate_quality(ping_stats)
            }
            
            results['devices'].append(device_info)
            
            if device_info['responsive']:
                quality_emoji = self._get_quality_emoji(device_info['quality'])
                print(f"{quality_emoji} {device_info['latency_avg_ms']:.2f}ms - {device_type}")
            else:
                print("❌ No response")
        
        print()
        return results
    
    def _calculate_quality(self, ping_stats: Dict) -> str:
        """Calculate connection quality rating"""
        if not ping_stats.get('responsive'):
            return 'OFFLINE'
        
        avg_ms = ping_stats.get('avg_ms', 999)
        loss = ping_stats.get('packet_loss', 100)
        
        if loss > 5:
            return 'POOR'
        elif avg_ms < 1.0:
            return 'EXCELLENT'
        elif avg_ms < 3.0:
            return 'GOOD'
        elif avg_ms < 10.0:
            return 'FAIR'
        else:
            return 'POOR'
    
    def _get_quality_emoji(self, quality: str) -> str:
        """Get emoji for quality rating"""
        return {
            'EXCELLENT': '🔥',
            'GOOD': '✅',
            'FAIR': '⚠️',
            'POOR': '❌',
            'OFFLINE': '💤'
        }.get(quality, '❓')
    
    def print_summary(self, results: Dict):
        """Print scan summary"""
        devices = results['devices']
        
        print()
        print("=" * 50)
        print("📊 MC96ECOUNIVERSE NETWORK SUMMARY")
        print("=" * 50)
        print()
        
        # Count by type
        mc96_switches = [d for d in devices if 'SWITCH' in d['type']]
        mc96_nodes = [d for d in devices if 'NODE' in d['type'] and d['responsive']]
        other_devices = [d for d in devices if 'MC96' not in d['type']]
        
        print(f"🔥 MC96 SWITCH: {len(mc96_switches)} detected")
        for device in mc96_switches:
            print(f"   • {device['ip']} ({device['mac']}) - {device['latency_avg_ms']:.2f}ms")
        print()
        
        print(f"⚡ MC96 NODES: {len(mc96_nodes)} active")
        for device in sorted(mc96_nodes, key=lambda x: x['latency_avg_ms']):
            emoji = self._get_quality_emoji(device['quality'])
            print(f"   {emoji} {device['ip']} - {device['latency_avg_ms']:.2f}ms ({device['type']})")
        print()
        
        print(f"📱 OTHER DEVICES: {len(other_devices)}")
        print()
        
        # Performance stats
        responsive = [d for d in devices if d['responsive']]
        if responsive:
            avg_latencies = [d['latency_avg_ms'] for d in responsive]
            best_latency = min(avg_latencies)
            avg_latency = sum(avg_latencies) / len(avg_latencies)
            
            print("🎯 PERFORMANCE METRICS:")
            print(f"   Best Latency: {best_latency:.2f}ms")
            print(f"   Average Latency: {avg_latency:.2f}ms")
            print(f"   Devices Online: {len(responsive)}/{len(devices)}")
        
        print()
        print("=" * 50)
        print("🚀 MC96 MESH NETWORK: READY")
        print("=" * 50)
        print()

def main():
    """Main execution"""
    scanner = MC96Scanner()
    results = scanner.scan_network()
    scanner.print_summary(results)
    
    # Save results to JSON
    output_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_scan_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"💾 Results saved to: {output_file}")
    print()
    print("GORUNFREE! 🎸🔥")

if __name__ == '__main__':
    main()

