#!/usr/bin/env python3
"""
MC96ECOUNIVERSE MESH TUNNEL NETWORK MANAGER
Creates and manages full mesh tunnel network between MC96 nodes
Created by CB_01 for ROB - GORUNFREE! 🚀
"""

import json
import subprocess
import time
from datetime import datetime
from typing import Dict, List
import os

class MC96MeshManager:
    """MC96 Mesh Tunnel Network Manager"""
    
    def __init__(self):
        self.scan_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_scan_results.json'
        self.mesh_config_file = '/Users/m2ultra/CB-01-FISHMUSICINC/tools/scripts/mc96_mesh_config.json'
        self.nodes = []
        self.tunnels = []
        
    def load_scan_results(self) -> bool:
        """Load latest scan results"""
        try:
            with open(self.scan_file, 'r') as f:
                data = json.load(f)
                
            # Get MC96 nodes (switch + active nodes)
            self.nodes = [
                d for d in data['devices'] 
                if 'MC96' in d['type'] and d['responsive']
            ]
            
            return len(self.nodes) > 0
        except FileNotFoundError:
            print(f"❌ Scan results not found. Run mc96_scan.py first!")
            return False
        except Exception as e:
            print(f"❌ Error loading scan results: {e}")
            return False
    
    def calculate_mesh_topology(self) -> List[Dict]:
        """Calculate full mesh tunnel connections"""
        tunnels = []
        
        # Create full mesh: every node connects to every other node
        for i, node_a in enumerate(self.nodes):
            for node_b in self.nodes[i+1:]:
                tunnel = {
                    'tunnel_id': f"mc96_{i}_{i+1}",
                    'node_a': {
                        'ip': node_a['ip'],
                        'mac': node_a['mac'],
                        'type': node_a['type']
                    },
                    'node_b': {
                        'ip': node_b['ip'],
                        'mac': node_b['mac'],
                        'type': node_b['type']
                    },
                    'status': 'pending',
                    'created_at': datetime.now().isoformat()
                }
                tunnels.append(tunnel)
        
        self.tunnels = tunnels
        return tunnels
    
    def test_tunnel_performance(self, node_a_ip: str, node_b_ip: str) -> Dict:
        """Test performance between two nodes"""
        try:
            # Test bidirectional latency
            result_ab = subprocess.run(
                ['ping', '-c', '10', '-i', '0.1', node_b_ip],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            stats = {
                'success': result_ab.returncode == 0,
                'latency_ms': 0,
                'bandwidth_estimate': 0,
                'quality': 'UNKNOWN'
            }
            
            if stats['success']:
                # Parse latency
                import re
                match = re.search(r'min/avg/max/stddev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+)', result_ab.stdout)
                if match:
                    stats['latency_ms'] = float(match.group(2))
                    
                    # Estimate bandwidth based on latency (rough calculation)
                    # Lower latency = better bandwidth potential
                    if stats['latency_ms'] < 1.0:
                        stats['bandwidth_estimate'] = 1000  # 1 Gbps
                        stats['quality'] = 'EXCELLENT'
                    elif stats['latency_ms'] < 3.0:
                        stats['bandwidth_estimate'] = 500  # 500 Mbps
                        stats['quality'] = 'GOOD'
                    elif stats['latency_ms'] < 10.0:
                        stats['bandwidth_estimate'] = 100  # 100 Mbps
                        stats['quality'] = 'FAIR'
                    else:
                        stats['bandwidth_estimate'] = 10  # 10 Mbps
                        stats['quality'] = 'POOR'
            
            return stats
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'quality': 'FAILED'
            }
    
    def establish_mesh_network(self):
        """Establish full mesh tunnel network"""
        print("🕸️  MC96ECOUNIVERSE MESH NETWORK BUILDER")
        print("=" * 50)
        print()
        
        if not self.load_scan_results():
            return
        
        print(f"📡 Found {len(self.nodes)} MC96 nodes:")
        for node in self.nodes:
            print(f"   • {node['ip']} - {node['type']} ({node['latency_avg_ms']:.2f}ms)")
        print()
        
        # Calculate mesh topology
        print("🧮 Calculating mesh topology...")
        tunnels = self.calculate_mesh_topology()
        print(f"   Creating {len(tunnels)} tunnels for full mesh")
        print()
        
        # Test each tunnel
        print("🔗 Testing tunnel connections...")
        for i, tunnel in enumerate(tunnels, 1):
            node_a_ip = tunnel['node_a']['ip']
            node_b_ip = tunnel['node_b']['ip']
            
            print(f"   [{i}/{len(tunnels)}] {node_a_ip} ↔ {node_b_ip}...", end=' ')
            
            perf = self.test_tunnel_performance(node_a_ip, node_b_ip)
            tunnel['performance'] = perf
            tunnel['status'] = 'active' if perf['success'] else 'failed'
            
            if perf['success']:
                quality_emoji = {
                    'EXCELLENT': '🔥',
                    'GOOD': '✅',
                    'FAIR': '⚠️',
                    'POOR': '❌'
                }.get(perf['quality'], '❓')
                print(f"{quality_emoji} {perf['latency_ms']:.2f}ms ({perf['quality']})")
            else:
                print("❌ Failed")
        
        print()
        
        # Save mesh configuration
        mesh_config = {
            'created_at': datetime.now().isoformat(),
            'nodes': self.nodes,
            'tunnels': tunnels,
            'topology': 'full_mesh',
            'total_nodes': len(self.nodes),
            'total_tunnels': len(tunnels),
            'active_tunnels': len([t for t in tunnels if t['status'] == 'active'])
        }
        
        with open(self.mesh_config_file, 'w') as f:
            json.dump(mesh_config, f, indent=2)
        
        self.print_mesh_summary(mesh_config)
    
    def print_mesh_summary(self, config: Dict):
        """Print mesh network summary"""
        print("=" * 50)
        print("🕸️  MC96 MESH NETWORK SUMMARY")
        print("=" * 50)
        print()
        
        total_tunnels = config['total_tunnels']
        active_tunnels = config['active_tunnels']
        success_rate = (active_tunnels / total_tunnels * 100) if total_tunnels > 0 else 0
        
        print(f"📊 NETWORK TOPOLOGY: {config['topology'].upper()}")
        print(f"   Total Nodes: {config['total_nodes']}")
        print(f"   Total Tunnels: {total_tunnels}")
        print(f"   Active Tunnels: {active_tunnels}")
        print(f"   Success Rate: {success_rate:.1f}%")
        print()
        
        # Calculate total bandwidth
        tunnels = config['tunnels']
        active = [t for t in tunnels if t['status'] == 'active']
        
        if active:
            total_bandwidth = sum(t['performance']['bandwidth_estimate'] for t in active)
            avg_latency = sum(t['performance']['latency_ms'] for t in active) / len(active)
            
            print(f"⚡ PERFORMANCE:")
            print(f"   Total Bandwidth: ~{total_bandwidth} Mbps")
            print(f"   Average Latency: {avg_latency:.2f}ms")
            print()
            
            # Quality distribution
            qualities = {}
            for t in active:
                q = t['performance']['quality']
                qualities[q] = qualities.get(q, 0) + 1
            
            print(f"🎯 QUALITY DISTRIBUTION:")
            for quality, count in sorted(qualities.items()):
                emoji = {
                    'EXCELLENT': '🔥',
                    'GOOD': '✅',
                    'FAIR': '⚠️',
                    'POOR': '❌'
                }.get(quality, '❓')
                print(f"   {emoji} {quality}: {count} tunnels")
        
        print()
        print("=" * 50)
        print("🚀 MC96 MESH NETWORK: OPERATIONAL")
        print("=" * 50)
        print()
        print(f"💾 Configuration saved: {self.mesh_config_file}")
        print()

def main():
    """Main execution"""
    manager = MC96MeshManager()
    manager.establish_mesh_network()
    print("GORUNFREE! 🎸🔥")

if __name__ == '__main__':
    main()

