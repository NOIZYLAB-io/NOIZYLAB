#!/usr/bin/env python3
#!/usr/bin/env python3
"""
System Diagnostics Module for IT Genius
Provides system health checks and diagnostics
"""

import platform
import subprocess
import psutil
from typing import Dict

class SystemDiagnostics:
    """System diagnostics and health checks"""
    
    def __init__(self, system_info: Dict):
        self.system_info = system_info
        self.os_type = system_info.get("os", platform.system())
    
    def display_menu(self):
        """Display diagnostics menu"""
        print("\n" + "="*70)
        print("SYSTEM DIAGNOSTICS")
        print("="*70)
        print("1. System Overview")
        print("2. CPU Information")
        print("3. Memory (RAM) Information")
        print("4. Disk Space Analysis")
        print("5. Network Status")
        print("6. Running Processes")
        print("7. System Health Check")
        print("0. Back to Main Menu")
        print("="*70)
    
    def system_overview(self):
        """Display system overview"""
        print("\n" + "="*70)
        print("SYSTEM OVERVIEW")
        print("="*70)
        
        try:
            print(f"\n🖥️  Operating System: {self.system_info['os']}")
            print(f"📦 Version: {self.system_info['os_version']}")
            print(f"🏗️  Architecture: {self.system_info['architecture']}")
            print(f"💻 Hostname: {self.system_info['hostname']}")
            print(f"⚙️  Processor: {self.system_info['processor']}")
            
            # CPU Info
            cpu_count = psutil.cpu_count(logical=True)
            cpu_physical = psutil.cpu_count(logical=False)
            cpu_percent = psutil.cpu_percent(interval=1)
            print(f"\n🔧 CPU:")
            print(f"   Physical Cores: {cpu_physical}")
            print(f"   Logical Cores: {cpu_count}")
            print(f"   Current Usage: {cpu_percent}%")
            
            # Memory Info
            memory = psutil.virtual_memory()
            print(f"\n💾 Memory (RAM):")
            print(f"   Total: {self._format_bytes(memory.total)}")
            print(f"   Available: {self._format_bytes(memory.available)}")
            print(f"   Used: {self._format_bytes(memory.used)} ({memory.percent}%)")
            
            # Disk Info
            disk = psutil.disk_usage('/')
            print(f"\n💿 Disk:")
            print(f"   Total: {self._format_bytes(disk.total)}")
            print(f"   Used: {self._format_bytes(disk.used)} ({disk.percent}%)")
            print(f"   Free: {self._format_bytes(disk.free)}")
            
        except Exception as e:
            print(f"❌ Error getting system info: {e}")
        
        print("\n" + "="*70)
    
    def cpu_info(self):
        """Display detailed CPU information"""
        print("\n" + "="*70)
        print("CPU INFORMATION")
        print("="*70)
        
        try:
            cpu_count = psutil.cpu_count(logical=True)
            cpu_physical = psutil.cpu_count(logical=False)
            cpu_freq = psutil.cpu_freq()
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
            
            print(f"\n🔧 CPU Details:")
            print(f"   Physical Cores: {cpu_physical}")
            print(f"   Logical Cores: {cpu_count}")
            if cpu_freq:
                print(f"   Current Frequency: {cpu_freq.current:.2f} MHz")
                print(f"   Min Frequency: {cpu_freq.min:.2f} MHz")
                print(f"   Max Frequency: {cpu_freq.max:.2f} MHz")
            
            print(f"\n📊 Per-Core Usage:")
            for i, usage in enumerate(cpu_percent):
                print(f"   Core {i}: {usage:.1f}%")
            
            print(f"\n📈 Overall CPU Usage: {sum(cpu_percent)/len(cpu_percent):.1f}%")
            
        except Exception as e:
            print(f"❌ Error getting CPU info: {e}")
        
        print("\n" + "="*70)
    
    def memory_info(self):
        """Display memory information"""
        print("\n" + "="*70)
        print("MEMORY (RAM) INFORMATION")
        print("="*70)
        
        try:
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            print(f"\n💾 Physical Memory:")
            print(f"   Total: {self._format_bytes(memory.total)}")
            print(f"   Available: {self._format_bytes(memory.available)}")
            print(f"   Used: {self._format_bytes(memory.used)} ({memory.percent}%)")
            print(f"   Free: {self._format_bytes(memory.free)}")
            
            print(f"\n💿 Swap Memory:")
            print(f"   Total: {self._format_bytes(swap.total)}")
            print(f"   Used: {self._format_bytes(swap.used)} ({swap.percent}%)")
            print(f"   Free: {self._format_bytes(swap.free)}")
            
            # Top memory consuming processes
            print(f"\n📊 Top Memory Consuming Processes:")
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
                try:
                    processes.append((
                        proc.info['pid'],
                        proc.info['name'],
                        proc.info['memory_info'].rss
                    ))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            processes.sort(key=lambda x: x[2], reverse=True)
            for pid, name, mem in processes[:10]:
                print(f"   {name} (PID: {pid}): {self._format_bytes(mem)}")
            
        except Exception as e:
            print(f"❌ Error getting memory info: {e}")
        
        print("\n" + "="*70)
    
    def disk_info(self):
        """Display disk space information"""
        print("\n" + "="*70)
        print("DISK SPACE ANALYSIS")
        print("="*70)
        
        try:
            partitions = psutil.disk_partitions()
            
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    print(f"\n💿 {partition.device}")
                    print(f"   Mountpoint: {partition.mountpoint}")
                    print(f"   Filesystem: {partition.fstype}")
                    print(f"   Total: {self._format_bytes(usage.total)}")
                    print(f"   Used: {self._format_bytes(usage.used)} ({usage.percent}%)")
                    print(f"   Free: {self._format_bytes(usage.free)}")
                    
                    if usage.percent > 90:
                        print(f"   ⚠️  WARNING: Disk space is critically low!")
                    elif usage.percent > 80:
                        print(f"   ⚠️  WARNING: Disk space is getting low")
                except PermissionError:
                    print(f"\n💿 {partition.device} (Access Denied)")
                except Exception as e:
                    print(f"\n💿 {partition.device} (Error: {e})")
            
        except Exception as e:
            print(f"❌ Error getting disk info: {e}")
        
        print("\n" + "="*70)
    
    def network_status(self):
        """Display network status"""
        print("\n" + "="*70)
        print("NETWORK STATUS")
        print("="*70)
        
        try:
            net_io = psutil.net_io_counters()
            print(f"\n📡 Network Statistics:")
            print(f"   Bytes Sent: {self._format_bytes(net_io.bytes_sent)}")
            print(f"   Bytes Received: {self._format_bytes(net_io.bytes_recv)}")
            print(f"   Packets Sent: {net_io.packets_sent:,}")
            print(f"   Packets Received: {net_io.packets_recv:,}")
            print(f"   Errors In: {net_io.errin}")
            print(f"   Errors Out: {net_io.errout}")
            
            print(f"\n🌐 Network Interfaces:")
            net_if_addrs = psutil.net_if_addrs()
            net_if_stats = psutil.net_if_stats()
            
            for interface, addrs in net_if_addrs.items():
                if interface in net_if_stats:
                    stats = net_if_stats[interface]
                    print(f"\n   {interface}:")
                    print(f"      Status: {'Up' if stats.isup else 'Down'}")
                    print(f"      Speed: {stats.speed} Mbps" if stats.speed > 0 else "      Speed: Unknown")
                    for addr in addrs:
                        print(f"      {addr.family.name}: {addr.address}")
            
        except Exception as e:
            print(f"❌ Error getting network info: {e}")
        
        print("\n" + "="*70)
    
    def running_processes(self):
        """Display running processes"""
        print("\n" + "="*70)
        print("RUNNING PROCESSES")
        print("="*70)
        
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    proc.info['cpu_percent'] = proc.cpu_percent(interval=0.1)
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
            
            print(f"\n{'PID':<8} {'Name':<30} {'CPU %':<10} {'Memory %':<10}")
            print("-" * 70)
            for proc in processes[:20]:
                print(f"{proc['pid']:<8} {proc['name'][:28]:<30} {proc.get('cpu_percent', 0):<10.1f} {proc.get('memory_percent', 0):<10.1f}")
            
        except Exception as e:
            print(f"❌ Error getting processes: {e}")
        
        print("\n" + "="*70)
    
    def health_check(self):
        """Run comprehensive system health check"""
        print("\n" + "="*70)
        print("SYSTEM HEALTH CHECK")
        print("="*70)
        
        issues = []
        warnings = []
        
        try:
            # Check CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            if cpu_percent > 90:
                issues.append(f"⚠️  CPU usage is very high: {cpu_percent:.1f}%")
            elif cpu_percent > 80:
                warnings.append(f"⚠️  CPU usage is high: {cpu_percent:.1f}%")
            else:
                print(f"✅ CPU usage: {cpu_percent:.1f}% (Normal)")
            
            # Check Memory
            memory = psutil.virtual_memory()
            if memory.percent > 90:
                issues.append(f"⚠️  Memory usage is critical: {memory.percent}%")
            elif memory.percent > 80:
                warnings.append(f"⚠️  Memory usage is high: {memory.percent}%")
            else:
                print(f"✅ Memory usage: {memory.percent}% (Normal)")
            
            # Check Disk
            disk = psutil.disk_usage('/')
            if disk.percent > 90:
                issues.append(f"⚠️  Disk space is critical: {disk.percent}% used")
            elif disk.percent > 80:
                warnings.append(f"⚠️  Disk space is getting low: {disk.percent}% used")
            else:
                print(f"✅ Disk space: {disk.percent}% used (Normal)")
            
            # Check Network
            net_io = psutil.net_io_counters()
            if net_io.errin > 1000 or net_io.errout > 1000:
                warnings.append(f"⚠️  Network errors detected: {net_io.errin + net_io.errout} errors")
            else:
                print(f"✅ Network: No significant errors detected")
            
            # Display issues and warnings
            if warnings:
                print("\n⚠️  WARNINGS:")
                for warning in warnings:
                    print(f"   {warning}")
            
            if issues:
                print("\n❌ CRITICAL ISSUES:")
                for issue in issues:
                    print(f"   {issue}")
            
            if not issues and not warnings:
                print("\n✅ System health check passed! No issues detected.")
            
        except Exception as e:
            print(f"❌ Error during health check: {e}")
        
        print("\n" + "="*70)
    
    def _format_bytes(self, bytes_value):
        """Format bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.2f} PB"
    
    def run(self):
        """Run diagnostics menu"""
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.system_overview()
            elif choice == "2":
                self.cpu_info()
            elif choice == "3":
                self.memory_info()
            elif choice == "4":
                self.disk_info()
            elif choice == "5":
                self.network_status()
            elif choice == "6":
                self.running_processes()
            elif choice == "7":
                self.health_check()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")

