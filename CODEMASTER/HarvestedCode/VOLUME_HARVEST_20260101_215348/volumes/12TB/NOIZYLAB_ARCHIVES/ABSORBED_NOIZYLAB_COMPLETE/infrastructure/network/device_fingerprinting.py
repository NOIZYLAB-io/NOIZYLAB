#!/usr/bin/env python3
"""
Advanced Device Fingerprinting & Classification
================================================
Intelligent device identification and classification system
"""

import socket
import subprocess
import re
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
import requests
from pathlib import Path
import json


@dataclass
class DeviceFingerprint:
    """Complete device fingerprint"""
    mac_address: str
    ip_address: str
    hostname: Optional[str]
    vendor: Optional[str]
    device_type: str
    os_type: Optional[str]
    os_version: Optional[str]
    open_ports: List[int]
    services: Dict[str, str]
    confidence: float  # 0.0 to 1.0


class DeviceClassifier:
    """Intelligent device classification system"""
    
    def __init__(self):
        self.oui_database = self._load_oui_database()
        self.classification_rules = self._load_classification_rules()
    
    def _load_oui_database(self) -> Dict[str, str]:
        """Load MAC vendor database"""
        return {
            "00:1a:2b": "Apple, Inc.",
            "00:50:56": "VMware, Inc.",
            "08:00:27": "Oracle VirtualBox",
            "00:0c:29": "VMware, Inc.",
            "00:16:3e": "Xen Virtual Network",
            "52:54:00": "QEMU Virtual Network",
            "00:1b:21": "Intel Corporate",
            "00:23:6c": "Apple, Inc.",
            "28:cf:e9": "Apple, Inc.",
            "3c:22:fb": "Apple, Inc.",
            "a4:83:e7": "Apple, Inc.",
            "00:0a:95": "Apple, Inc.",
            "f4:5c:89": "Apple, Inc.",
            "88:66:5a": "Apple, Inc.",
            "dc:a6:32": "Raspberry Pi Foundation",
            "b8:27:eb": "Raspberry Pi Foundation",
            "d0:50:99": "Micro-Star International",
            "00:e0:4c": "Realtek Semiconductor",
            "00:e0:7d": "D-Link Corporation",
        }
    
    def _load_classification_rules(self) -> Dict[str, Dict]:
        """Load device classification rules"""
        return {
            "mc96": {
                "ports": [8080, 8443],
                "services": ["http", "https"],
                "paths": ["/api/status", "/api/info"],
                "confidence": 0.95
            },
            "macbook": {
                "vendors": ["Apple"],
                "os_hints": ["Darwin", "macOS"],
                "ports": [22, 88, 548, 5900],
                "confidence": 0.85
            },
            "iphone": {
                "vendors": ["Apple"],
                "ports": [62078],
                "hostname_patterns": ["iphone", "ios"],
                "confidence": 0.85
            },
            "ipad": {
                "vendors": ["Apple"],
                "hostname_patterns": ["ipad"],
                "confidence": 0.85
            },
            "raspberry_pi": {
                "vendors": ["Raspberry Pi"],
                "ports": [22],
                "hostname_patterns": ["raspberrypi", "pi"],
                "confidence": 0.90
            },
            "server": {
                "ports": [22, 80, 443, 3306, 5432],
                "services": ["ssh", "http", "https"],
                "confidence": 0.75
            },
            "printer": {
                "ports": [9100, 515, 631],
                "services": ["printer", "ipp"],
                "hostname_patterns": ["printer", "hp", "canon", "epson"],
                "confidence": 0.80
            },
            "nas": {
                "ports": [139, 445, 2049, 5000],
                "services": ["smb", "nfs"],
                "hostname_patterns": ["nas", "synology", "qnap"],
                "confidence": 0.85
            },
            "router": {
                "ports": [80, 443, 8080],
                "hostname_patterns": ["router", "gateway", "dgs", "dlink"],
                "confidence": 0.80
            },
            "switch": {
                "ports": [80, 161, 162],
                "services": ["snmp"],
                "hostname_patterns": ["switch", "dgs", "dlink"],
                "confidence": 0.85
            }
        }
    
    def fingerprint_device(self, ip: str, mac: Optional[str] = None) -> DeviceFingerprint:
        """
        Create complete device fingerprint
        
        Args:
            ip: IP address
            mac: MAC address (optional)
        
        Returns:
            DeviceFingerprint
        """
        # Get hostname
        hostname = self._get_hostname(ip)
        
        # Get vendor from MAC
        vendor = None
        if mac:
            vendor = self._lookup_vendor(mac)
        
        # Scan ports
        open_ports = self._scan_ports(ip)
        
        # Identify services
        services = self._identify_services(ip, open_ports)
        
        # Detect OS
        os_type, os_version = self._detect_os(ip, services)
        
        # Classify device
        device_type, confidence = self._classify_device(
            hostname, vendor, open_ports, services, os_type
        )
        
        return DeviceFingerprint(
            mac_address=mac or "unknown",
            ip_address=ip,
            hostname=hostname,
            vendor=vendor,
            device_type=device_type,
            os_type=os_type,
            os_version=os_version,
            open_ports=open_ports,
            services=services,
            confidence=confidence
        )
    
    def _get_hostname(self, ip: str) -> Optional[str]:
        """Resolve hostname from IP"""
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            return hostname
        except:
            return None
    
    def _lookup_vendor(self, mac: str) -> Optional[str]:
        """Lookup vendor from MAC address"""
        prefix = ':'.join(mac.split(':')[:3]).lower()
        return self.oui_database.get(prefix)
    
    def _scan_ports(self, ip: str, ports: List[int] = None) -> List[int]:
        """Scan for open ports"""
        if ports is None:
            # Common ports
            ports = [22, 80, 443, 445, 515, 631, 3306, 5000, 5432, 5900, 8080, 8443, 9100]
        
        open_ports = []
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                sock.close()
                
                if result == 0:
                    open_ports.append(port)
            except:
                pass
        
        return open_ports
    
    def _identify_services(self, ip: str, open_ports: List[int]) -> Dict[str, str]:
        """Identify services on open ports"""
        services = {}
        
        service_map = {
            22: "ssh",
            80: "http",
            443: "https",
            445: "smb",
            515: "lpd",
            631: "ipp",
            3306: "mysql",
            5000: "upnp",
            5432: "postgresql",
            5900: "vnc",
            8080: "http-alt",
            8443: "https-alt",
            9100: "jetdirect"
        }
        
        for port in open_ports:
            service = service_map.get(port, f"unknown-{port}")
            
            # Try to get service banner
            banner = self._get_service_banner(ip, port)
            if banner:
                service = f"{service} ({banner})"
            
            services[str(port)] = service
        
        return services
    
    def _get_service_banner(self, ip: str, port: int) -> Optional[str]:
        """Get service banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, port))
            
            if port in [80, 8080]:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            sock.close()
            
            # Extract useful info from banner
            if "Server:" in banner:
                server = re.search(r'Server:\s*(.+)', banner)
                if server:
                    return server.group(1).strip()
            
            return banner[:30] if banner else None
        except:
            return None
    
    def _detect_os(self, ip: str, services: Dict[str, str]) -> Tuple[Optional[str], Optional[str]]:
        """Detect operating system"""
        # Check for macOS/Darwin
        for service in services.values():
            if any(x in service.lower() for x in ["darwin", "macos", "apple"]):
                return "macOS", None
        
        # Check for Linux
        if "22" in services:  # SSH commonly on Linux
            banner = self._get_service_banner(ip, 22)
            if banner and "ubuntu" in banner.lower():
                return "Linux", "Ubuntu"
            elif banner and "debian" in banner.lower():
                return "Linux", "Debian"
        
        # Check for Windows
        if "445" in services:  # SMB
            return "Windows", None
        
        return None, None
    
    def _classify_device(self, hostname: Optional[str], vendor: Optional[str],
                        open_ports: List[int], services: Dict[str, str],
                        os_type: Optional[str]) -> Tuple[str, float]:
        """
        Classify device type based on all available information
        
        Returns:
            (device_type, confidence)
        """
        scores = {}
        
        for device_type, rules in self.classification_rules.items():
            score = 0.0
            matches = 0
            total_checks = 0
            
            # Check ports
            if "ports" in rules:
                total_checks += 1
                rule_ports = set(rules["ports"])
                device_ports = set(open_ports)
                if rule_ports & device_ports:  # Any matching ports
                    matches += 1
                    score += 0.3
            
            # Check vendor
            if "vendors" in rules and vendor:
                total_checks += 1
                if any(v.lower() in vendor.lower() for v in rules["vendors"]):
                    matches += 1
                    score += 0.3
            
            # Check hostname patterns
            if "hostname_patterns" in rules and hostname:
                total_checks += 1
                if any(p.lower() in hostname.lower() for p in rules["hostname_patterns"]):
                    matches += 1
                    score += 0.3
            
            # Check OS hints
            if "os_hints" in rules and os_type:
                total_checks += 1
                if any(h.lower() in os_type.lower() for h in rules["os_hints"]):
                    matches += 1
                    score += 0.1
            
            # Normalize score
            if total_checks > 0:
                confidence = (score / total_checks) * rules.get("confidence", 0.5)
                scores[device_type] = confidence
        
        # Return highest scoring device type
        if scores:
            best_type = max(scores.items(), key=lambda x: x[1])
            return best_type[0], best_type[1]
        
        # Default classification
        if vendor and "apple" in vendor.lower():
            return "apple_device", 0.5
        elif vendor and "raspberry pi" in vendor.lower():
            return "raspberry_pi", 0.7
        elif 22 in open_ports:
            return "server", 0.4
        
        return "unknown", 0.0
    
    def classify_as_mc96(self, ip: str) -> Tuple[bool, float]:
        """
        Specifically check if device is MC96
        
        Returns:
            (is_mc96, confidence)
        """
        # Check for MC96 API endpoints
        mc96_endpoints = [
            "/api/status",
            "/api/info",
            "/api/version"
        ]
        
        for port in [8080, 8443]:
            for endpoint in mc96_endpoints:
                try:
                    protocol = "https" if port == 8443 else "http"
                    response = requests.get(
                        f"{protocol}://{ip}:{port}{endpoint}",
                        timeout=2,
                        verify=False
                    )
                    
                    if response.status_code == 200:
                        # Try to parse response
                        try:
                            data = response.json()
                            if "mc96" in json.dumps(data).lower():
                                return True, 0.95
                        except:
                            pass
                        
                        # Endpoint exists, likely MC96
                        return True, 0.80
                except:
                    continue
        
        return False, 0.0


def main():
    """Test fingerprinting"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python device_fingerprinting.py <ip_address> [mac_address]")
        sys.exit(1)
    
    ip = sys.argv[1]
    mac = sys.argv[2] if len(sys.argv) > 2 else None
    
    classifier = DeviceClassifier()
    
    print(f"\n🔍 Fingerprinting device: {ip}")
    print("=" * 50)
    
    fingerprint = classifier.fingerprint_device(ip, mac)
    
    print(f"\n📋 Device Information:")
    print(f"  IP Address: {fingerprint.ip_address}")
    print(f"  MAC Address: {fingerprint.mac_address}")
    print(f"  Hostname: {fingerprint.hostname or '—'}")
    print(f"  Vendor: {fingerprint.vendor or '—'}")
    print(f"  Device Type: {fingerprint.device_type}")
    print(f"  OS: {fingerprint.os_type or '—'}")
    if fingerprint.os_version:
        print(f"  OS Version: {fingerprint.os_version}")
    print(f"  Confidence: {fingerprint.confidence * 100:.1f}%")
    
    if fingerprint.open_ports:
        print(f"\n🔓 Open Ports:")
        for port in fingerprint.open_ports:
            service = fingerprint.services.get(str(port), "unknown")
            print(f"  {port}: {service}")
    
    # Check if MC96
    is_mc96, mc96_confidence = classifier.classify_as_mc96(ip)
    if is_mc96:
        print(f"\n🎯 MC96 Detected! (Confidence: {mc96_confidence * 100:.1f}%)")
    
    print()


if __name__ == "__main__":
    main()

