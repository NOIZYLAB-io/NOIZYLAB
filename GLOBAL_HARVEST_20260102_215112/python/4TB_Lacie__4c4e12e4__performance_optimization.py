#!/usr/bin/env python3
"""
Performance Optimization Module for IT Genius
System performance tuning and optimization for macOS and Windows
"""

import platform
import subprocess
import psutil
from typing import Dict

class PerformanceOptimization:
    """Performance optimization tools"""
    
    def __init__(self, system_info: Dict):
        self.system_info = system_info
        self.os_type = system_info.get("os", platform.system())
        self.is_macos = self.os_type == "Darwin"
        self.is_windows = self.os_type == "Windows"
    
    def show_menu(self):
        """Display performance optimization menu"""
        while True:
            print("\n" + "="*70)
            print("PERFORMANCE OPTIMIZATION")
            print("="*70)
            print("1. Performance Analysis")
            print("2. Startup Optimization")
            print("3. Memory Optimization")
            print("4. Disk Optimization")
            print("5. CPU Optimization")
            print("6. Network Optimization")
            print("7. Application Performance")
            print("8. System Cleanup")
            print("9. Advanced Tuning")
            print("0. Back to Main Menu")
            print("="*70)
            
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.performance_analysis()
            elif choice == "2":
                self.startup_optimization()
            elif choice == "3":
                self.memory_optimization()
            elif choice == "4":
                self.disk_optimization()
            elif choice == "5":
                self.cpu_optimization()
            elif choice == "6":
                self.network_optimization()
            elif choice == "7":
                self.app_performance()
            elif choice == "8":
                self.system_cleanup()
            elif choice == "9":
                self.advanced_tuning()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def performance_analysis(self):
        """Analyze current system performance"""
        print("\n" + "="*70)
        print("PERFORMANCE ANALYSIS")
        print("="*70)
        
        try:
            # CPU Analysis
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
            cpu_avg = sum(cpu_percent) / len(cpu_percent)
            print(f"\n🔧 CPU Usage: {cpu_avg:.1f}%")
            if cpu_avg > 80:
                print("   ⚠️  CPU usage is high - consider closing applications")
            elif cpu_avg > 50:
                print("   ⚠️  CPU usage is moderate")
            else:
                print("   ✅ CPU usage is normal")
            
            # Memory Analysis
            memory = psutil.virtual_memory()
            print(f"\n💾 Memory Usage: {memory.percent}%")
            print(f"   Available: {self._format_bytes(memory.available)}")
            if memory.percent > 90:
                print("   ⚠️  Memory is critically low!")
            elif memory.percent > 80:
                print("   ⚠️  Memory usage is high")
            else:
                print("   ✅ Memory usage is normal")
            
            # Disk Analysis
            disk = psutil.disk_usage('/')
            print(f"\n💿 Disk Usage: {disk.percent}%")
            print(f"   Free: {self._format_bytes(disk.free)}")
            if disk.percent > 90:
                print("   ⚠️  Disk space is critically low!")
            elif disk.percent > 80:
                print("   ⚠️  Disk space is getting low")
            else:
                print("   ✅ Disk space is adequate")
            
            # Top Processes
            print(f"\n📊 Top CPU Processes:")
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    proc.info['cpu_percent'] = proc.cpu_percent(interval=0.1)
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
            print(f"{'Process':<30} {'CPU %':<10} {'Memory %':<10}")
            print("-" * 70)
            for proc in processes[:10]:
                print(f"{proc['name'][:28]:<30} {proc.get('cpu_percent', 0):<10.1f} {proc.get('memory_percent', 0):<10.1f}")
            
        except Exception as e:
            print(f"❌ Error analyzing performance: {e}")
        
        print("\n" + "="*70)
    
    def startup_optimization(self):
        """Optimize startup programs"""
        print("\n" + "="*70)
        print("STARTUP OPTIMIZATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Startup Items:")
            print("\n1. Login Items:")
            print("   System Settings → General → Login Items")
            print("   Remove unnecessary startup applications")
            
            print("\n2. Launch Agents/Daemons:")
            print("   ~/Library/LaunchAgents/")
            print("   /Library/LaunchAgents/")
            print("   /Library/LaunchDaemons/")
            print("   Review and remove unnecessary items")
            
            print("\n3. Check Startup Items:")
            print("   # List login items")
            print("   osascript -e 'tell application \"System Events\" to get the name of every login item'")
            
        elif self.is_windows:
            print("\n🪟 Windows Startup Items:")
            print("\n1. Task Manager:")
            print("   Ctrl+Shift+Esc → Startup tab")
            print("   Disable unnecessary startup programs")
            
            print("\n2. Startup Folder:")
            print("   Windows + R → shell:startup")
            print("   Remove shortcuts from startup folder")
            
            print("\n3. Services:")
            print("   Windows + R → services.msc")
            print("   Set unnecessary services to 'Manual'")
            
            print("\n4. Registry (Advanced):")
            print("   Windows + R → regedit")
            print("   HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
            print("   HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
        
        print("\n💡 Startup Optimization Tips:")
        print("   • Only keep essential apps in startup")
        print("   • Disable unused services")
        print("   • Use SSD for faster boot times")
        print("   • Keep system updated")
        print("   • Remove bloatware")
        
        print("\n" + "="*70)
    
    def memory_optimization(self):
        """Memory optimization techniques"""
        print("\n" + "="*70)
        print("MEMORY OPTIMIZATION")
        print("="*70)
        
        print("\n💾 Memory Optimization Techniques:")
        print("\n1. Close Unused Applications:")
        print("   • Quit applications you're not using")
        print("   • Check Activity Monitor (macOS) or Task Manager (Windows)")
        
        print("\n2. Disable Memory-Intensive Features:")
        if self.is_macos:
            print("   • Reduce visual effects")
            print("   • Disable unnecessary widgets")
            print("   • Close browser tabs")
        elif self.is_windows:
            print("   • Disable visual effects")
            print("   • Reduce background apps")
            print("   • Close browser tabs")
        
        print("\n3. Virtual Memory/Swap:")
        if self.is_macos:
            print("   • System automatically manages swap")
            print("   • Ensure adequate disk space for swap")
        elif self.is_windows:
            print("   • System Properties → Advanced → Performance Settings")
            print("   • Advanced → Virtual memory → Change")
            print("   • Set custom size or let system manage")
        
        print("\n4. Memory Cleanup:")
        if self.is_macos:
            print("   # Clear memory cache (use with caution)")
            print("   sudo purge")
        elif self.is_windows:
            print("   # Clear standby memory")
            print("   EmptyStandbyList.exe (third-party tool)")
        
        print("\n5. Upgrade RAM:")
        print("   • Check current RAM usage")
        print("   • Consider upgrading if consistently >80%")
        print("   • Check system maximum RAM capacity")
        
        print("\n💡 Memory Best Practices:")
        print("   • Monitor memory usage regularly")
        print("   • Close unused browser tabs")
        print("   • Restart system periodically")
        print("   • Use memory-efficient applications")
        print("   • Consider RAM upgrade if needed")
        
        print("\n" + "="*70)
    
    def disk_optimization(self):
        """Disk optimization and cleanup"""
        print("\n" + "="*70)
        print("DISK OPTIMIZATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Disk Optimization:")
            print("\n1. Disk Utility:")
            print("   Applications → Utilities → Disk Utility")
            print("   First Aid → Verify/Repair Disk")
            
            print("\n2. Clean Up Storage:")
            print("   Apple menu → About This Mac → Storage → Manage")
            print("   • Optimize storage")
            print("   • Empty Trash")
            print("   • Reduce clutter")
            print("   • Review large files")
            
            print("\n3. Terminal Commands:")
            print("   # Check disk usage")
            print("   du -sh ~/*")
            print("   # Find large files")
            print("   find ~ -type f -size +100M")
            print("   # Clear system caches (use with caution)")
            print("   sudo rm -rf ~/Library/Caches/*")
            
        elif self.is_windows:
            print("\n🪟 Windows Disk Optimization:")
            print("\n1. Disk Cleanup:")
            print("   Windows + R → cleanmgr")
            print("   Select drive → Clean up system files")
            
            print("\n2. Disk Defragmentation:")
            print("   Windows + R → dfrgui")
            print("   Optimize drives (SSD: TRIM, HDD: Defragment)")
            
            print("\n3. Storage Sense:")
            print("   Settings → System → Storage")
            print("   Configure Storage Sense")
            print("   • Delete temporary files")
            print("   • Clean up downloads")
            
            print("\n4. PowerShell Commands:")
            print("   # Check disk usage")
            print("   Get-ChildItem -Recurse | Measure-Object -Property Length -Sum")
            print("   # Find large files")
            print("   Get-ChildItem -Recurse | Where-Object {$_.Length -gt 100MB}")
        
        print("\n💡 Disk Optimization Tips:")
        print("   • Regularly empty Trash/Recycle Bin")
        print("   • Remove unused applications")
        print("   • Clear browser cache")
        print("   • Delete temporary files")
        print("   • Move large files to external storage")
        print("   • Use disk cleanup tools")
        print("   • Defragment HDDs (not SSDs)")
        
        print("\n" + "="*70)
    
    def cpu_optimization(self):
        """CPU optimization techniques"""
        print("\n" + "="*70)
        print("CPU OPTIMIZATION")
        print("="*70)
        
        print("\n🔧 CPU Optimization Techniques:")
        print("\n1. Close CPU-Intensive Processes:")
        print("   • Identify high CPU processes")
        print("   • Close unnecessary applications")
        print("   • End background processes if safe")
        
        print("\n2. Power Management:")
        if self.is_macos:
            print("   System Settings → Battery")
            print("   • Optimize for performance")
            print("   • Disable Power Nap if not needed")
        elif self.is_windows:
            print("   Control Panel → Power Options")
            print("   • Select 'High Performance' plan")
            print("   • Adjust advanced power settings")
        
        print("\n3. CPU Affinity (Windows):")
        print("   Task Manager → Details → Right-click process")
        print("   Set Affinity → Select CPU cores")
        
        print("\n4. Thermal Management:")
        print("   • Ensure proper cooling")
        print("   • Clean dust from fans")
        print("   • Check thermal paste (if applicable)")
        print("   • Monitor CPU temperature")
        
        print("\n5. Background Processes:")
        print("   • Disable unnecessary background apps")
        print("   • Reduce startup programs")
        print("   • Limit background updates")
        
        print("\n💡 CPU Best Practices:")
        print("   • Monitor CPU temperature")
        print("   • Keep system cool")
        print("   • Close unused applications")
        print("   • Update drivers")
        print("   • Use efficient software")
        
        print("\n" + "="*70)
    
    def network_optimization(self):
        """Network performance optimization"""
        print("\n" + "="*70)
        print("NETWORK OPTIMIZATION")
        print("="*70)
        
        print("\n🌐 Network Optimization:")
        print("\n1. DNS Optimization:")
        print("   • Use fast DNS servers (1.1.1.1, 8.8.8.8)")
        print("   • Enable DNS over HTTPS")
        print("   • Flush DNS cache regularly")
        
        print("\n2. WiFi Optimization:")
        print("   • Use 5GHz band when possible")
        print("   • Position router optimally")
        print("   • Update router firmware")
        print("   • Change WiFi channel if congested")
        print("   • Use wired connection when possible")
        
        print("\n3. Browser Optimization:")
        print("   • Clear browser cache")
        print("   • Disable unnecessary extensions")
        print("   • Use ad blockers")
        print("   • Enable browser caching")
        
        print("\n4. Network Settings:")
        if self.is_macos:
            print("   System Settings → Network")
            print("   • Configure TCP/IP settings")
            print("   • Optimize MTU size")
        elif self.is_windows:
            print("   Network Settings → Advanced options")
            print("   • Configure TCP/IP settings")
            print("   • Optimize MTU size")
        
        print("\n5. Bandwidth Management:")
        print("   • Limit background downloads")
        print("   • Prioritize important traffic")
        print("   • Use QoS settings on router")
        
        print("\n💡 Network Best Practices:")
        print("   • Use wired connection for stability")
        print("   • Update network drivers")
        print("   • Monitor network usage")
        print("   • Use VPN only when needed")
        print("   • Keep router firmware updated")
        
        print("\n" + "="*70)
    
    def app_performance(self):
        """Application performance optimization"""
        print("\n" + "="*70)
        print("APPLICATION PERFORMANCE")
        print("="*70)
        
        print("\n📱 Application Optimization:")
        print("\n1. Update Applications:")
        print("   • Keep apps updated")
        print("   • Update drivers")
        print("   • Install latest versions")
        
        print("\n2. Close Unused Apps:")
        print("   • Quit applications not in use")
        print("   • Check background processes")
        print("   • Disable auto-start apps")
        
        print("\n3. Application Settings:")
        print("   • Reduce visual effects")
        print("   • Lower quality settings if needed")
        print("   • Disable unnecessary features")
        print("   • Clear app caches")
        
        print("\n4. Browser Optimization:")
        print("   • Limit open tabs")
        print("   • Disable unused extensions")
        print("   • Clear cache and cookies")
        print("   • Use efficient browsers")
        
        print("\n5. Resource Allocation:")
        print("   • Prioritize important applications")
        print("   • Adjust process priorities (advanced)")
        print("   • Allocate more RAM if needed")
        
        print("\n💡 Application Best Practices:")
        print("   • Use lightweight alternatives")
        print("   • Close apps when done")
        print("   • Monitor app resource usage")
        print("   • Update regularly")
        print("   • Remove unused applications")
        
        print("\n" + "="*70)
    
    def system_cleanup(self):
        """System cleanup procedures"""
        print("\n" + "="*70)
        print("SYSTEM CLEANUP")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Cleanup:")
            print("\n1. Storage Management:")
            print("   Apple menu → About This Mac → Storage → Manage")
            print("   • Optimize storage")
            print("   • Empty Trash")
            print("   • Reduce clutter")
            
            print("\n2. Clean Up:")
            print("   • Remove unused applications")
            print("   • Clear Downloads folder")
            print("   • Delete old files")
            print("   • Clear browser cache")
            
            print("\n3. Terminal Cleanup:")
            print("   # Remove old logs")
            print("   sudo rm -rf /private/var/log/*")
            print("   # Clear user caches (use with caution)")
            print("   rm -rf ~/Library/Caches/*")
            print("   # Remove old iOS backups")
            print("   rm -rf ~/Library/Application\\ Support/MobileSync/Backup/*")
            
        elif self.is_windows:
            print("\n🪟 Windows Cleanup:")
            print("\n1. Disk Cleanup:")
            print("   Windows + R → cleanmgr")
            print("   Select all cleanup options")
            
            print("\n2. Remove Programs:")
            print("   Settings → Apps → Apps & features")
            print("   Uninstall unused applications")
            
            print("\n3. Clean Up:")
            print("   • Clear Recycle Bin")
            print("   • Delete temp files")
            print("   • Clear browser cache")
            print("   • Remove old Windows updates")
            
            print("\n4. PowerShell Cleanup:")
            print("   # Clean Windows Update files")
            print("   Dism.exe /online /Cleanup-Image /StartComponentCleanup")
            print("   # Remove old Windows versions")
            print("   Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase")
        
        print("\n💡 Cleanup Best Practices:")
        print("   • Regular cleanup (monthly)")
        print("   • Backup before major cleanup")
        print("   • Use built-in cleanup tools")
        print("   • Review before deleting")
        print("   • Empty Trash/Recycle Bin regularly")
        
        print("\n" + "="*70)
    
    def advanced_tuning(self):
        """Advanced performance tuning"""
        print("\n" + "="*70)
        print("ADVANCED PERFORMANCE TUNING")
        print("="*70)
        
        print("\n⚠️  WARNING: Advanced settings may affect system stability.")
        print("   Only apply if you understand the implications.\n")
        
        if self.is_macos:
            print("🍎 macOS Advanced Tuning:")
            print("\n1. Disable Visual Effects:")
            print("   System Settings → Accessibility → Display")
            print("   • Reduce motion")
            print("   • Reduce transparency")
            
            print("\n2. Kernel Parameters:")
            print("   # Increase shared memory (use with caution)")
            print("   sudo sysctl -w kern.sysv.shmmax=1073741824")
            
            print("\n3. Spotlight Indexing:")
            print("   System Settings → Siri & Spotlight")
            print("   • Exclude unnecessary locations")
            print("   • Reduce indexing scope")
            
        elif self.is_windows:
            print("🪟 Windows Advanced Tuning:")
            print("\n1. Visual Effects:")
            print("   System Properties → Advanced → Performance Settings")
            print("   • Adjust for best performance")
            
            print("\n2. Registry Tweaks (Advanced):")
            print("   • Disable unnecessary services")
            print("   • Optimize page file")
            print("   • Adjust network parameters")
            
            print("\n3. Group Policy (Pro/Enterprise):")
            print("   gpedit.msc")
            print("   • Configure performance policies")
        
        print("\n💡 Advanced Tips:")
        print("   • Benchmark before/after changes")
        print("   • Document all changes")
        print("   • Create restore point before changes")
        print("   • Research before applying")
        print("   • Test stability after changes")
        
        print("\n" + "="*70)
    
    def _format_bytes(self, bytes_value):
        """Format bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.2f} PB"

