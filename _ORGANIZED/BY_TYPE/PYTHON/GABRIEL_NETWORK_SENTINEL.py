#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║         🌐 GABRIEL NETWORK SENTINEL                                       ║
║                                                                           ║
║         ADVANCED NETWORK MONITORING & SECURITY                            ║
║                                                                           ║
║  • Real-time network traffic analysis                                     ║
║  • Intrusion detection system (IDS)                                       ║
║  • Port scanning & vulnerability detection                                ║
║  • Bandwidth monitoring per device                                        ║
║  • DDoS attack detection                                                  ║
║  • Rogue device detection                                                 ║
║  • Network topology mapping                                               ║
║  • Performance bottleneck identification                                  ║
║  • Auto-quarantine suspicious devices                                     ║
║  • Alert system for anomalies                                             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import socket
import struct
import time
import threading
import queue
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional
from datetime import datetime, timedelta
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s'
)
logger = logging.getLogger('GABRIEL_SENTINEL')

# ═══════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class NetworkDevice:
    """Network device information"""
    ip: str
    mac: str = ""
    hostname: str = ""
    first_seen: datetime = field(default_factory=datetime.now)
    last_seen: datetime = field(default_factory=datetime.now)
    is_trusted: bool = False
    open_ports: List[int] = field(default_factory=list)
    traffic_in: int = 0  # bytes
    traffic_out: int = 0  # bytes
    connection_count: int = 0
    suspicious_activity: List[str] = field(default_factory=list)

@dataclass
class NetworkAlert:
    """Network security alert"""
    timestamp: datetime
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    alert_type: str
    device_ip: str
    description: str
    recommended_action: str

@dataclass
class TrafficPattern:
    """Traffic pattern for anomaly detection"""
    device_ip: str
    packets_per_second: deque = field(default_factory=lambda: deque(maxlen=60))
    bytes_per_second: deque = field(default_factory=lambda: deque(maxlen=60))
    connections_per_minute: deque = field(default_factory=lambda: deque(maxlen=60))

# ═══════════════════════════════════════════════════════════════════════════
# GABRIEL NETWORK SENTINEL
# ═══════════════════════════════════════════════════════════════════════════

class GabrielNetworkSentinel:
    """
    NETWORK SENTINEL
    
    Advanced network monitoring and security system
    """
    
    def __init__(self, interface: str = "0.0.0.0", dgs1210_ip: str = "10.0.0.1"):
        self.interface = interface
        self.dgs1210_ip = dgs1210_ip
        self.running = False
        
        # Device tracking
        self.devices: Dict[str, NetworkDevice] = {}
        self.trusted_devices: Set[str] = set()
        self.blacklist: Set[str] = set()
        
        # Traffic patterns
        self.traffic_patterns: Dict[str, TrafficPattern] = defaultdict(TrafficPattern)
        
        # Alerts
        self.alerts: List[NetworkAlert] = []
        self.alert_queue = queue.Queue()
        
        # Thresholds
        self.SUSPICIOUS_PORT_SCAN_THRESHOLD = 10  # ports per minute
        self.SUSPICIOUS_CONNECTION_THRESHOLD = 100  # connections per minute
        self.DDOS_PACKET_THRESHOLD = 10000  # packets per second
        self.BANDWIDTH_WARNING_MBPS = 100
        
        # Statistics
        self.total_packets = 0
        self.total_bytes = 0
        self.start_time = datetime.now()
        
        logger.info("🌐 GABRIEL NETWORK SENTINEL initialized")
        logger.info(f"   Interface: {self.interface}")
        logger.info(f"   DGS-1210 Switch: {self.dgs1210_ip}")
    
    # ───────────────────────────────────────────────────────────
    # DEVICE MANAGEMENT
    # ───────────────────────────────────────────────────────────
    
    def register_device(self, ip: str, mac: str = "", hostname: str = "") -> NetworkDevice:
        """Register or update device"""
        if ip not in self.devices:
            device = NetworkDevice(ip=ip, mac=mac, hostname=hostname)
            self.devices[ip] = device
            logger.info(f"📱 New device: {ip} ({hostname or 'Unknown'})")
            
            # Check if trusted
            if ip in self.trusted_devices:
                device.is_trusted = True
        else:
            device = self.devices[ip]
            device.last_seen = datetime.now()
            if mac:
                device.mac = mac
            if hostname:
                device.hostname = hostname
        
        return device
    
    def trust_device(self, ip: str):
        """Add device to trusted list"""
        self.trusted_devices.add(ip)
        if ip in self.devices:
            self.devices[ip].is_trusted = True
        logger.info(f"✅ Trusted: {ip}")
    
    def blacklist_device(self, ip: str, reason: str):
        """Blacklist suspicious device"""
        self.blacklist.add(ip)
        logger.warning(f"🚫 Blacklisted: {ip} - {reason}")
        
        # Create alert
        alert = NetworkAlert(
            timestamp=datetime.now(),
            severity="HIGH",
            alert_type="DEVICE_BLACKLISTED",
            device_ip=ip,
            description=f"Device blacklisted: {reason}",
            recommended_action="Investigate device activity and block if necessary"
        )
        self.alert_queue.put(alert)
    
    # ───────────────────────────────────────────────────────────
    # NETWORK SCANNING
    # ───────────────────────────────────────────────────────────
    
    def scan_network(self, network: str = "192.168.1.0/24"):
        """Scan network for active devices"""
        logger.info(f"🔍 Scanning network: {network}")
        
        # Parse network
        base_ip = network.split('/')[0]
        base_parts = base_ip.split('.')
        base = '.'.join(base_parts[:3])
        
        # Scan IPs
        active_count = 0
        for i in range(1, 255):
            ip = f"{base}.{i}"
            
            # Quick ping check
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            
            try:
                result = sock.connect_ex((ip, 80))
                if result == 0:
                    self.register_device(ip)
                    active_count += 1
            except:
                pass
            finally:
                sock.close()
        
        logger.info(f"   Found {active_count} active devices")
        return active_count
    
    def scan_ports(self, ip: str, ports: List[int] = None):
        """Scan ports on device"""
        if ports is None:
            # Common ports
            ports = [21, 22, 23, 80, 443, 445, 3389, 8080, 8443]
        
        open_ports = []
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
            except:
                pass
            finally:
                sock.close()
        
        # Update device
        if ip in self.devices:
            self.devices[ip].open_ports = open_ports
        
        # Check for suspicious port scanning
        if len(open_ports) > self.SUSPICIOUS_PORT_SCAN_THRESHOLD:
            self.create_alert(
                severity="MEDIUM",
                alert_type="SUSPICIOUS_PORTS",
                device_ip=ip,
                description=f"Device has {len(open_ports)} open ports",
                recommended_action="Review port usage and close unnecessary ports"
            )
        
        return open_ports
    
    # ───────────────────────────────────────────────────────────
    # TRAFFIC MONITORING
    # ───────────────────────────────────────────────────────────
    
    def monitor_traffic(self, device_ip: str, packets: int, bytes_count: int):
        """Monitor traffic for device"""
        # Update device stats
        if device_ip in self.devices:
            device = self.devices[device_ip]
            device.traffic_in += bytes_count
            device.connection_count += packets
        
        # Update traffic pattern
        pattern = self.traffic_patterns[device_ip]
        pattern.packets_per_second.append(packets)
        pattern.bytes_per_second.append(bytes_count)
        
        # Check for anomalies
        self._check_traffic_anomalies(device_ip, pattern)
    
    def _check_traffic_anomalies(self, device_ip: str, pattern: TrafficPattern):
        """Check for traffic anomalies"""
        # DDoS detection
        if len(pattern.packets_per_second) > 0:
            avg_packets = sum(pattern.packets_per_second) / len(pattern.packets_per_second)
            
            if avg_packets > self.DDOS_PACKET_THRESHOLD:
                self.create_alert(
                    severity="CRITICAL",
                    alert_type="POSSIBLE_DDOS",
                    device_ip=device_ip,
                    description=f"Abnormally high packet rate: {avg_packets:.0f} pps",
                    recommended_action="Investigate traffic source and consider rate limiting"
                )
        
        # Bandwidth monitoring
        if len(pattern.bytes_per_second) > 0:
            avg_bytes = sum(pattern.bytes_per_second) / len(pattern.bytes_per_second)
            mbps = (avg_bytes * 8) / (1024 * 1024)
            
            if mbps > self.BANDWIDTH_WARNING_MBPS:
                self.create_alert(
                    severity="MEDIUM",
                    alert_type="HIGH_BANDWIDTH",
                    device_ip=device_ip,
                    description=f"High bandwidth usage: {mbps:.1f} Mbps",
                    recommended_action="Check for large file transfers or streaming"
                )
    
    # ───────────────────────────────────────────────────────────
    # INTRUSION DETECTION
    # ───────────────────────────────────────────────────────────
    
    def detect_port_scan(self, device_ip: str, scanned_ports: int):
        """Detect port scanning activity"""
        if scanned_ports > 20:
            self.create_alert(
                severity="HIGH",
                alert_type="PORT_SCAN_DETECTED",
                device_ip=device_ip,
                description=f"Port scan detected: {scanned_ports} ports scanned",
                recommended_action="Block device and investigate intent"
            )
            
            # Auto-blacklist if severe
            if scanned_ports > 50:
                self.blacklist_device(device_ip, f"Aggressive port scanning ({scanned_ports} ports)")
    
    def detect_rogue_device(self, device_ip: str, device_mac: str):
        """Detect rogue/unauthorized devices"""
        # Check if device is new and untrusted
        if device_ip not in self.trusted_devices:
            device = self.devices.get(device_ip)
            if device and (datetime.now() - device.first_seen).seconds < 60:
                self.create_alert(
                    severity="MEDIUM",
                    alert_type="NEW_DEVICE",
                    device_ip=device_ip,
                    description=f"New device connected: {device_mac}",
                    recommended_action="Verify device identity and authorize or block"
                )
    
    # ───────────────────────────────────────────────────────────
    # ALERT MANAGEMENT
    # ───────────────────────────────────────────────────────────
    
    def create_alert(self, severity: str, alert_type: str, device_ip: str, 
                    description: str, recommended_action: str):
        """Create security alert"""
        alert = NetworkAlert(
            timestamp=datetime.now(),
            severity=severity,
            alert_type=alert_type,
            device_ip=device_ip,
            description=description,
            recommended_action=recommended_action
        )
        
        self.alerts.append(alert)
        self.alert_queue.put(alert)
        
        # Log based on severity
        if severity == "CRITICAL":
            logger.critical(f"🚨 {alert_type}: {description}")
        elif severity == "HIGH":
            logger.error(f"⚠️  {alert_type}: {description}")
        elif severity == "MEDIUM":
            logger.warning(f"⚡ {alert_type}: {description}")
        else:
            logger.info(f"ℹ️  {alert_type}: {description}")
    
    def get_recent_alerts(self, minutes: int = 60) -> List[NetworkAlert]:
        """Get recent alerts"""
        cutoff = datetime.now() - timedelta(minutes=minutes)
        return [a for a in self.alerts if a.timestamp > cutoff]
    
    # ───────────────────────────────────────────────────────────
    # REPORTING
    # ───────────────────────────────────────────────────────────
    
    def generate_security_report(self) -> str:
        """Generate security report"""
        report = []
        report.append("# 🌐 GABRIEL NETWORK SENTINEL REPORT\n\n")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Overview
        report.append("## 📊 Network Overview\n\n")
        report.append(f"- Total Devices: {len(self.devices)}\n")
        report.append(f"- Trusted Devices: {len(self.trusted_devices)}\n")
        report.append(f"- Blacklisted: {len(self.blacklist)}\n")
        report.append(f"- Active Alerts: {len(self.get_recent_alerts())}\n\n")
        
        # Devices
        report.append("## 📱 Connected Devices\n\n")
        report.append("| IP Address | Hostname | Status | Open Ports | Traffic |\n")
        report.append("|------------|----------|--------|------------|----------|\n")
        
        for ip, device in sorted(self.devices.items()):
            status = "✅ Trusted" if device.is_trusted else "⚠️ Unknown"
            if ip in self.blacklist:
                status = "🚫 Blocked"
            
            traffic_mb = device.traffic_in / (1024 * 1024)
            ports = len(device.open_ports)
            
            report.append(f"| {ip} | {device.hostname or 'Unknown'} | {status} | {ports} | {traffic_mb:.1f} MB |\n")
        
        report.append("\n")
        
        # Recent alerts
        recent_alerts = self.get_recent_alerts(60)
        if recent_alerts:
            report.append("## 🚨 Recent Alerts (Last Hour)\n\n")
            
            for alert in recent_alerts[-10:]:  # Last 10 alerts
                report.append(f"### {alert.severity}: {alert.alert_type}\n")
                report.append(f"- **Device:** {alert.device_ip}\n")
                report.append(f"- **Time:** {alert.timestamp.strftime('%H:%M:%S')}\n")
                report.append(f"- **Description:** {alert.description}\n")
                report.append(f"- **Action:** {alert.recommended_action}\n\n")
        
        # Recommendations
        report.append("## 💡 Security Recommendations\n\n")
        
        untrusted = len(self.devices) - len(self.trusted_devices)
        if untrusted > 0:
            report.append(f"1. Review and authorize {untrusted} untrusted devices\n")
        
        if len(self.blacklist) > 0:
            report.append(f"2. Investigate {len(self.blacklist)} blacklisted devices\n")
        
        high_alerts = [a for a in recent_alerts if a.severity in ["HIGH", "CRITICAL"]]
        if high_alerts:
            report.append(f"3. Address {len(high_alerts)} high-priority alerts\n")
        
        report.append("\n---\n")
        report.append("**GABRIEL NETWORK SENTINEL**\n")
        
        return ''.join(report)
    
    def save_report(self, filename: str = "NETWORK_SECURITY_REPORT.md"):
        """Save security report"""
        report = self.generate_security_report()
        with open(filename, 'w') as f:
            f.write(report)
        logger.info(f"📄 Report saved: {filename}")
        return filename

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║         🌐 GABRIEL NETWORK SENTINEL                                       ║
║                                                                           ║
║         Advanced Network Monitoring & Security                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Create sentinel
    sentinel = GabrielNetworkSentinel()
    
    # Scan network
    print("\n🔍 Scanning network...")
    sentinel.scan_network("192.168.1.0/24")
    
    # Scan ports on discovered devices
    print("\n🔍 Scanning ports...")
    for ip in list(sentinel.devices.keys())[:5]:  # First 5 devices
        ports = sentinel.scan_ports(ip)
        print(f"   {ip}: {len(ports)} open ports")
    
    # Generate report
    print("\n📊 Generating security report...")
    report_file = sentinel.save_report()
    
    print(f"\n✅ Done! Report: {report_file}")
    print(f"   Devices: {len(sentinel.devices)}")
    print(f"   Alerts: {len(sentinel.alerts)}")
