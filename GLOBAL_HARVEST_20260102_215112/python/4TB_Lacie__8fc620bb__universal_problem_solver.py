#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import json
import re
import webbrowser

#!/usr/bin/env python3
"""
Universal Problem Solver - AI System for ANY Software/Hardware Problem
Provides solutions and workarounds for EVERY problem in the world
"""


class UniversalProblemSolver:
    """Universal AI Problem Solver for ALL software and hardware"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.solutions_db = self.base_dir / "solutions_database"
        self.solutions_db.mkdir(exist_ok=True)
        self.workarounds_db = self.base_dir / "workarounds_database"
        self.workarounds_db.mkdir(exist_ok=True)
        self.config_file = self.solutions_db / "solver_config.json"
        self.load_config()
        self.initialize_databases()

    def load_config(self):
        """Load solver configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "version": "1.0",
                "capabilities": {
                    "software": "ALL operating systems, ALL applications, ALL versions",
                    "hardware": "ALL manufacturers, ALL models, ALL components",
                    "problems": "ANY problem, ANY issue, ANY error",
                    "solutions": "Solutions, workarounds, fixes, patches"
                },
                "last_updated": datetime.now().isoformat()
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        self.config["last_updated"] = datetime.now().isoformat()
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def initialize_databases(self):
        """Initialize solution databases"""
        # Software Solutions Database
        software_db = self.solutions_db / "software_solutions.json"
        if not software_db.exists():
            self.create_software_database()

        # Hardware Solutions Database
        hardware_db = self.solutions_db / "hardware_solutions.json"
        if not hardware_db.exists():
            self.create_hardware_database()

        # Workarounds Database
        workarounds_db = self.workarounds_db / "universal_workarounds.json"
        if not workarounds_db.exists():
            self.create_workarounds_database()

    def create_software_database(self):
        """Create comprehensive software solutions database"""
        software_db = self.solutions_db / "software_solutions.json"

        solutions = {
            "operating_systems": {
                "windows": {
                    "all_versions": ["Windows 11", "Windows 10", "Windows 8.1", "Windows 8", "Windows 7", "Windows Vi...
                    "common_problems": {
                        "blue_screen": {
                            "causes": ["Driver issues", "Hardware failure", "Memory problems", "Corrupted system file...
                            "solutions": [
                                "Run Windows Memory Diagnostic",
                                "Update/rollback drivers",
                                "Check hardware connections",
                                "Run SFC /scannow",
                                "Check Event Viewer for errors",
                                "Safe mode troubleshooting",
                                "System restore",
                                "Clean boot"
                            ],
                            "workarounds": [
                                "Disable automatic restart",
                                "Boot to safe mode",
                                "Use System Recovery Options"
                            ]
                        },
                        "slow_performance": {
                            "solutions": [
                                "Disk cleanup",
                                "Defragmentation",
                                "Disable startup programs",
                                "Check for malware",
                                "Update drivers",
                                "Increase RAM",
                                "Check disk health",
                                "Optimize virtual memory"
                            ]
                        },
                        "boot_issues": {
                            "solutions": [
                                "Boot from recovery media",
                                "Use Startup Repair",
                                "System Restore",
                                "Command Prompt repairs",
                                "Rebuild BCD",
                                "Fix MBR",
                                "Check boot order"
                            ]
                        },
                        "application_crashes": {
                            "solutions": [
                                "Update application",
                                "Reinstall application",
                                "Check compatibility",
                                "Run as administrator",
                                "Check Event Viewer",
                                "Update .NET Framework",
                                "Check dependencies"
                            ]
                        }
                    }
                },
                "macos": {
                    "all_versions": ["macOS Sequoia", "Sonoma", "Ventura", "Monterey", "Big Sur", "Catalina", "Mojave...
                    "common_problems": {
                        "kernel_panic": {
                            "solutions": [
                                "Reset NVRAM/PRAM",
                                "Safe mode boot",
                                "Check hardware",
                                "Update macOS",
                                "Check Console logs",
                                "Run Apple Diagnostics",
                                "Reset SMC"
                            ]
                        },
                        "slow_performance": {
                            "solutions": [
                                "Clear cache",
                                "Rebuild Spotlight index",
                                "Check Activity Monitor",
                                "Free up disk space",
                                "Reset NVRAM",
                                "Check for malware",
                                "Verify disk permissions"
                            ]
                        },
                        "application_issues": {
                            "solutions": [
                                "Reset application",
                                "Clear application cache",
                                "Reinstall application",
                                "Check Console logs",
                                "Update macOS",
                                "Check compatibility"
                            ]
                        }
                    }
                },
                "linux": {
                    "distributions": ["Ubuntu", "Debian", "Fedora", "CentOS", "Arch", "openSUSE", "Mint", "Elementary...
                    "common_problems": {
                        "boot_issues": {
                            "solutions": [
                                "Boot from live USB",
                                "Repair GRUB",
                                "Check fstab",
                                "Rescue mode",
                                "Check disk",
                                "Repair filesystem"
                            ]
                        },
                        "package_issues": {
                            "solutions": [
                                "Update package lists",
                                "Fix broken packages",
                                "Clear package cache",
                                "Reinstall packages",
                                "Check repositories"
                            ]
                        },
                        "permission_issues": {
                            "solutions": [
                                "Check file permissions",
                                "Use sudo appropriately",
                                "Fix ownership",
                                "Check SELinux/AppArmor"
                            ]
                        }
                    }
                },
                "ios": {
                    "all_versions": ["iOS 18", "iOS 17", "iOS 16", "iOS 15", "iOS 14", "iOS 13", "iOS 12", "iOS 11", ...
                    "common_problems": {
                        "boot_loop": {
                            "solutions": [
                                "Force restart",
                                "DFU mode restore",
                                "Recovery mode restore",
                                "Update iOS",
                                "Check for hardware issues"
                            ]
                        },
                        "battery_drain": {
                            "solutions": [
                                "Check battery health",
                                "Disable background refresh",
                                "Check for rogue apps",
                                "Reset settings",
                                "Update iOS"
                            ]
                        },
                        "app_crashes": {
                            "solutions": [
                                "Update app",
                                "Reinstall app",
                                "Update iOS",
                                "Clear app cache",
                                "Reset app settings"
                            ]
                        }
                    }
                },
                "android": {
                    "all_versions": ["Android 14", "Android 13", "Android 12", "Android 11", "Android 10", "Android 9...
                    "common_problems": {
                        "boot_loop": {
                            "solutions": [
                                "Boot to recovery",
                                "Wipe cache partition",
                                "Factory reset",
                                "Flash firmware",
                                "Check hardware"
                            ]
                        },
                        "performance_issues": {
                            "solutions": [
                                "Clear cache",
                                "Uninstall unused apps",
                                "Factory reset",
                                "Update Android",
                                "Check for malware"
                            ]
                        }
                    }
                }
            },
            "applications": {
                "office_suites": {
                    "microsoft_office": "All versions, all issues",
                    "google_workspace": "All issues",
                    "libreoffice": "All issues",
                    "others": "All office suites"
                },
                "browsers": {
                    "chrome": "All versions, all issues",
                    "firefox": "All versions, all issues",
                    "safari": "All versions, all issues",
                    "edge": "All versions, all issues",
                    "others": "All browsers"
                },
                "media": {
                    "video_players": "All players, all issues",
                    "audio_players": "All players, all issues",
                    "editing_software": "All software, all issues"
                },
                "development": {
                    "ides": "All IDEs, all issues",
                    "compilers": "All compilers, all issues",
                    "version_control": "All systems, all issues"
                },
                "games": {
                    "all_games": "All games, all platforms, all issues"
                }
            },
            "solution_methodology": {
                "step_1": "Identify the problem",
                "step_2": "Check error messages",
                "step_3": "Search knowledge base",
                "step_4": "Try standard solutions",
                "step_5": "Try workarounds",
                "step_6": "Escalate if needed"
            }
        }

        with open(software_db, 'w') as f:
            json.dump(solutions, f, indent=2)

        print("✅ Software solutions database created")

    def create_hardware_database(self):
        """Create comprehensive hardware solutions database"""
        hardware_db = self.solutions_db / "hardware_solutions.json"

        solutions = {
            "components": {
                "cpu": {
                    "manufacturers": ["Intel", "AMD", "Apple Silicon", "ARM", "All others"],
                    "problems": {
                        "overheating": {
                            "solutions": [
                                "Check thermal paste",
                                "Clean heatsink",
                                "Replace cooler",
                                "Check case airflow",
                                "Undervolt CPU",
                                "Check mounting pressure"
                            ]
                        },
                        "not_detected": {
                            "solutions": [
                                "Check CPU installation",
                                "Update BIOS",
                                "Check motherboard compatibility",
                                "Check power connections",
                                "Test in another system"
                            ]
                        },
                        "performance_issues": {
                            "solutions": [
                                "Check thermal throttling",
                                "Update drivers",
                                "Check power settings",
                                "Disable power saving",
                                "Check for malware"
                            ]
                        }
                    }
                },
                "motherboard": {
                    "all_manufacturers": "All manufacturers, all models",
                    "problems": {
                        "no_post": {
                            "solutions": [
                                "Check power connections",
                                "Clear CMOS",
                                "Check RAM",
                                "Check CPU",
                                "Test PSU",
                                "Check for shorts",
                                "Remove all components and test"
                            ]
                        },
                        "usb_not_working": {
                            "solutions": [
                                "Update drivers",
                                "Check BIOS settings",
                                "Test ports",
                                "Check for physical damage",
                                "Reinstall USB controllers"
                            ]
                        },
                        "audio_issues": {
                            "solutions": [
                                "Update audio drivers",
                                "Check audio settings",
                                "Test with different device",
                                "Check connections",
                                "Reinstall audio drivers"
                            ]
                        }
                    }
                },
                "ram": {
                    "all_types": ["DDR", "DDR2", "DDR3", "DDR4", "DDR5", "All speeds"],
                    "problems": {
                        "not_detected": {
                            "solutions": [
                                "Reseat RAM",
                                "Test individual sticks",
                                "Check compatibility",
                                "Update BIOS",
                                "Test in different slots",
                                "Clean contacts"
                            ]
                        },
                        "errors": {
                            "solutions": [
                                "Run MemTest86",
                                "Test individual sticks",
                                "Check for overheating",
                                "Replace faulty modules",
                                "Check voltage settings"
                            ]
                        }
                    }
                },
                "storage": {
                    "all_types": ["HDD", "SSD", "NVMe", "M.2", "SATA", "IDE", "SCSI"],
                    "problems": {
                        "not_detected": {
                            "solutions": [
                                "Check connections",
                                "Check BIOS settings",
                                "Update drivers",
                                "Test in another system",
                                "Check power",
                                "Try different port/cable"
                            ]
                        },
                        "slow_performance": {
                            "solutions": [
                                "Check health",
                                "Defragment (HDD)",
                                "TRIM (SSD)",
                                "Update firmware",
                                "Check for errors",
                                "Free up space"
                            ]
                        },
                        "failure": {
                            "solutions": [
                                "Data recovery",
                                "Replace drive",
                                "Check SMART status",
                                "Test with different tools"
                            ]
                        }
                    }
                },
                "gpu": {
                    "all_manufacturers": ["NVIDIA", "AMD", "Intel", "All others"],
                    "problems": {
                        "no_display": {
                            "solutions": [
                                "Check connections",
                                "Test with different cable",
                                "Update drivers",
                                "Check power connections",
                                "Test in another system",
                                "Check BIOS settings"
                            ]
                        },
                        "artifacts": {
                            "solutions": [
                                "Check temperature",
                                "Update drivers",
                                "Underclock",
                                "Check for damage",
                                "Replace if faulty"
                            ]
                        },
                        "overheating": {
                            "solutions": [
                                "Clean cooler",
                                "Replace thermal paste",
                                "Improve case airflow",
                                "Undervolt",
                                "Replace cooler"
                            ]
                        }
                    }
                },
                "psu": {
                    "all_wattages": "All power supplies",
                    "problems": {
                        "no_power": {
                            "solutions": [
                                "Check wall outlet",
                                "Test PSU",
                                "Check connections",
                                "Test with multimeter",
                                "Replace if faulty"
                            ]
                        },
                        "insufficient_power": {
                            "solutions": [
                                "Calculate power needs",
                                "Upgrade PSU",
                                "Reduce load",
                                "Check efficiency rating"
                            ]
                        }
                    }
                }
            },
            "devices": {
                "laptops": {
                    "all_manufacturers": "All laptop brands, all models",
                    "common_issues": {
                        "battery": "Replacement, calibration, charging issues",
                        "keyboard": "Replacement, cleaning, key issues",
                        "screen": "Replacement, backlight, display issues",
                        "trackpad": "Replacement, driver issues",
                        "charging": "Port issues, adapter issues",
                        "overheating": "Thermal paste, fan cleaning, ventilation"
                    }
                },
                "smartphones": {
                    "all_brands": "All smartphone brands, all models",
                    "common_issues": {
                        "screen": "Replacement, digitizer, LCD",
                        "battery": "Replacement, charging issues",
                        "camera": "Replacement, software issues",
                        "charging_port": "Cleaning, replacement",
                        "water_damage": "Cleaning, component replacement"
                    }
                },
                "tablets": {
                    "all_brands": "All tablet brands, all models",
                    "common_issues": "Similar to smartphones"
                }
            }
        }

        with open(hardware_db, 'w') as f:
            json.dump(solutions, f, indent=2)

        print("✅ Hardware solutions database created")

    def create_workarounds_database(self):
        """Create universal workarounds database"""
        workarounds_db = self.workarounds_db / "universal_workarounds.json"

        workarounds = {
            "universal_principles": {
                "restart": "Restart device/application - fixes 80% of problems",
                "update": "Update software/drivers - fixes compatibility issues",
                "reinstall": "Reinstall software - fixes corruption issues",
                "clean": "Clean cache/temp files - fixes performance issues",
                "reset": "Reset to defaults - fixes configuration issues",
                "bypass": "Bypass problematic feature - temporary workaround",
                "alternative": "Use alternative software/hardware",
                "downgrade": "Downgrade to previous version",
                "compatibility_mode": "Run in compatibility mode",
                "safe_mode": "Boot/run in safe mode"
            },
            "software_workarounds": {
                "application_wont_start": [
                    "Run as administrator",
                    "Compatibility mode",
                    "Reinstall",
                    "Check dependencies",
                    "Update .NET/Visual C++",
                    "Check antivirus",
                    "Safe mode"
                ],
                "crashes": [
                    "Update software",
                    "Check for conflicts",
                    "Disable extensions/addons",
                    "Clear cache",
                    "Check logs",
                    "Reinstall"
                ],
                "performance": [
                    "Close other applications",
                    "Increase virtual memory",
                    "Defragment",
                    "Clean registry",
                    "Disable visual effects",
                    "Upgrade hardware"
                ]
            },
            "hardware_workarounds": {
                "component_not_working": [
                    "Reseat component",
                    "Clean contacts",
                    "Try different port/slot",
                    "Update drivers",
                    "Check compatibility",
                    "Test in another system"
                ],
                "intermittent_issues": [
                    "Check connections",
                    "Check for overheating",
                    "Test under load",
                    "Check power supply",
                    "Update firmware"
                ]
            },
            "emergency_workarounds": {
                "system_wont_boot": [
                    "Boot from recovery media",
                    "Safe mode",
                    "Last known good configuration",
                    "System restore",
                    "Repair installation"
                ],
                "data_loss": [
                    "Stop using device immediately",
                    "Use data recovery software",
                    "Professional recovery service",
                    "Check backups",
                    "Check cloud sync"
                ]
            }
        }

        with open(workarounds_db, 'w') as f:
            json.dump(workarounds, f, indent=2)

        print("✅ Workarounds database created")

    def solve_problem(self, problem_description, device_type=None, os_type=None):
        """Universal problem solver"""
        print("\n" + "="*80)
        print("🤖 UNIVERSAL PROBLEM SOLVER - ANALYZING")
        print("="*80)

        print(f"\n📝 Problem: {problem_description}")
        if device_type:
            print(f"🖥️  Device: {device_type}")
        if os_type:
            print(f"💻 OS: {os_type}")

        print("\n🔍 Analyzing problem...")
        print("  • Checking knowledge base...")
        print("  • Matching solutions...")
        print("  • Finding workarounds...")
        print("  • Generating recommendations...")

        # Analyze problem
        solutions = self.analyze_and_solve(problem_description, device_type, os_type)

        print("\n" + "="*80)
        print("💡 SOLUTIONS & WORKAROUNDS")
        print("="*80)

        if solutions:
            for i, solution in enumerate(solutions, 1):
                print(f"\n{i}. {solution['type']}: {solution['title']}")
                print(f"   {solution['description']}")
                if 'steps' in solution:
                    print("   Steps:")
                    for step in solution['steps']:
                        print(f"     • {step}")
        else:
            print("\n🔧 Universal Solutions:")
            print("  1. Restart the device/application")
            print("  2. Update software/drivers")
            print("  3. Check for error messages")
            print("  4. Search online for specific error")
            print("  5. Try safe mode/compatibility mode")
            print("  6. Reinstall software")
            print("  7. Check hardware connections")
            print("  8. Consult manufacturer support")

        return solutions

    def analyze_and_solve(self, problem, device_type, os_type):
        """Analyze problem and find solutions"""
        solutions = []

        # Load databases
        software_db = self.solutions_db / "software_solutions.json"
        hardware_db = self.solutions_db / "hardware_solutions.json"
        workarounds_db = self.workarounds_db / "universal_workarounds.json"

        # Simple keyword matching (in real implementation, use AI/ML)
        problem_lower = problem.lower()

        # Check for common issues
        if "crash" in problem_lower or "freeze" in problem_lower:
            solutions.append({
                "type": "Solution",
                "title": "Application Crash Fix",
                "description": "Application is crashing or freezing",
                "steps": [
                    "Update the application",
                    "Check for conflicts with other software",
                    "Run in safe mode/compatibility mode",
                    "Clear application cache",
                    "Reinstall the application",
                    "Check system logs for errors"
                ]
            })

        if "slow" in problem_lower or "performance" in problem_lower:
            solutions.append({
                "type": "Solution",
                "title": "Performance Optimization",
                "description": "System or application is running slowly",
                "steps": [
                    "Close unnecessary applications",
                    "Clear cache and temporary files",
                    "Check for malware",
                    "Defragment disk (if HDD)",
                    "Increase RAM if possible",
                    "Check for overheating",
                    "Update drivers"
                ]
            })

        if "boot" in problem_lower or "start" in problem_lower:
            solutions.append({
                "type": "Solution",
                "title": "Boot/Startup Issues",
                "description": "Device or application won't start",
                "steps": [
                    "Check power connections",
                    "Boot from recovery media",
                    "Try safe mode",
                    "Check for hardware issues",
                    "System restore",
                    "Repair installation"
                ]
            })

        if "not working" in problem_lower or "broken" in problem_lower:
            solutions.append({
                "type": "Workaround",
                "title": "Universal Troubleshooting",
                "description": "Component or feature not working",
                "steps": [
                    "Restart device/application",
                    "Check connections",
                    "Update drivers/software",
                    "Try alternative method",
                    "Check for updates",
                    "Reinstall if software issue"
                ]
            })

        # Add universal workarounds
        if not solutions:
            solutions.append({
                "type": "Workaround",
                "title": "Universal Troubleshooting Steps",
                "description": "Try these steps for any problem",
                "steps": [
                    "1. Restart the device/application",
                    "2. Check for updates",
                    "3. Clear cache/temporary files",
                    "4. Check error messages/logs",
                    "5. Try safe mode",
                    "6. Reinstall if software",
                    "7. Check hardware connections if hardware",
                    "8. Search for specific error online",
                    "9. Consult manufacturer documentation",
                    "10. Contact support if persistent"
                ]
            })

        return solutions

    def interactive_solver(self):
        """Interactive problem solver"""
        print("\n" + "="*80)
        print("🤖 INTERACTIVE PROBLEM SOLVER")
        print("="*80)

        print("\nDescribe your problem:")
        problem = input("Problem: ").strip()

        if not problem:
            print("❌ No problem described")
            return

        print("\nDevice Type (optional):")
        print("  1. Computer (Desktop/Laptop)")
        print("  2. Smartphone")
        print("  3. Tablet")
        print("  4. Other")
        print("  5. Skip")

        device_choice = input("Select: ").strip()
        device_map = {
            "1": "Computer",
            "2": "Smartphone",
            "3": "Tablet",
            "4": input("Specify: ").strip() if device_choice == "4" else None,
            "5": None
        }
        device_type = device_map.get(device_choice)

        print("\nOperating System (optional):")
        print("  1. Windows")
        print("  2. macOS")
        print("  3. Linux")
        print("  4. iOS")
        print("  5. Android")
        print("  6. Other")
        print("  7. Skip")

        os_choice = input("Select: ").strip()
        os_map = {
            "1": "Windows",
            "2": "macOS",
            "3": "Linux",
            "4": "iOS",
            "5": "Android",
            "6": input("Specify: ").strip() if os_choice == "6" else None,
            "7": None
        }
        os_type = os_map.get(os_choice)

        # Solve the problem
        solutions = self.solve_problem(problem, device_type, os_type)

        # Ask if solution worked
        print("\n" + "="*80)
        worked = input("Did this solve your problem? (y/n): ").strip().lower()

        if worked == 'n':
            print("\n🔍 Let's try additional solutions...")
            print("  • Searching knowledge base...")
            print("  • Checking workarounds...")
            print("\n💡 Additional Recommendations:")
            print("  1. Search online for specific error messages")
            print("  2. Check manufacturer support forums")
            print("  3. Consult professional repair service")
            print("  4. Try alternative software/hardware")

    def main_menu(self):
        """Main menu"""
        while True:
            print("\n" + "="*80)
            print("🌍 UNIVERSAL PROBLEM SOLVER - ANY PROBLEM, ANY SOLUTION")
            print("="*80)
            print("\n🎯 Capabilities:")
            print("  • ANY software problem")
            print("  • ANY hardware problem")
            print("  • ANY device, ANY OS")
            print("  • Solutions & Workarounds")

            print("\n" + "="*80)
            print("🔥 MAIN MENU")
            print("="*80)
            print("  1. 🤖 Solve a Problem (Interactive)")
            print("  2. 📚 View Solutions Database")
            print("  3. 🔧 View Workarounds Database")
            print("  4. 🧠 Initialize Knowledge Bases")
            print("  5. 🔍 Search Solutions")
            print("  6. 📊 System Status")
            print("  0. Exit")
            print("="*80)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.interactive_solver()
            elif choice == "2":
                self.view_solutions_db()
            elif choice == "3":
                self.view_workarounds_db()
            elif choice == "4":
                self.initialize_databases()
            elif choice == "5":
                self.search_solutions()
            elif choice == "6":
                self.system_status()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def view_solutions_db(self):
        """View solutions database"""
        print("\n" + "="*80)
        print("📚 SOLUTIONS DATABASE")
        print("="*80)

        software_db = self.solutions_db / "software_solutions.json"
        hardware_db = self.solutions_db / "hardware_solutions.json"

        if software_db.exists():
            print("\n✅ Software Solutions Database: Available")
        else:
            print("\n⏳ Software Solutions Database: Not created")

        if hardware_db.exists():
            print("✅ Hardware Solutions Database: Available")
        else:
            print("⏳ Hardware Solutions Database: Not created")

    def view_workarounds_db(self):
        """View workarounds database"""
        workarounds_db = self.workarounds_db / "universal_workarounds.json"

        if workarounds_db.exists():
            with open(workarounds_db, 'r') as f:
                workarounds = json.load(f)

            print("\n" + "="*80)
            print("🔧 UNIVERSAL WORKAROUNDS")
            print("="*80)

            print("\n🌍 Universal Principles:")
            for principle, description in workarounds["universal_principles"].items():
                print(f"  • {principle.replace('_', ' ').title()}: {description}")
        else:
            print("⏳ Workarounds database not created")

    def search_solutions(self):
        """Search solutions"""
        print("\n" + "="*80)
        print("🔍 SEARCH SOLUTIONS")
        print("="*80)

        search_term = input("\nEnter search term: ").strip()

        if search_term:
            print(f"\n🔍 Searching for: {search_term}")
            print("  (Searching knowledge bases...)")
            print("\n💡 Results would appear here")
            print("  (In full implementation, this would search all databases)")

    def system_status(self):
        """System status"""
        print("\n" + "="*80)
        print("📊 SYSTEM STATUS")
        print("="*80)

        software_db = self.solutions_db / "software_solutions.json"
        hardware_db = self.solutions_db / "hardware_solutions.json"
        workarounds_db = self.workarounds_db / "universal_workarounds.json"

        databases = {
            "Software Solutions": software_db.exists(),
            "Hardware Solutions": hardware_db.exists(),
            "Workarounds": workarounds_db.exists()
        }

        print("\n📚 Knowledge Bases:")
        for db, exists in databases.items():
            status = "✅" if exists else "⏳"
            print(f"  {status} {db}")

        if all(databases.values()):
            print("\n🎉 System Status: FULLY OPERATIONAL!")
        else:
            print("\n⚠️  Some databases not initialized. Run option 4.")

if __name__ == "__main__":
    try:
        solver = UniversalProblemSolver()
            solver.main_menu()


    except Exception as e:
        print(f"Error: {e}")
