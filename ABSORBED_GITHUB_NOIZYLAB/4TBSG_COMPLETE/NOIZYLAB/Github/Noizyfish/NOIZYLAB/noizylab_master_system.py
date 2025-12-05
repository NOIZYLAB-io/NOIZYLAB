#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

#!/usr/bin/env python3
"""
NOIZYLAB Master System - Ultimate AI Training & Problem Solving
Combines AI Trainer + Universal Problem Solver for complete repair team training
"""


class NOIZYLABMasterSystem:
    """Master system combining all capabilities"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.config_file = self.base_dir / "master_system_config.json"
        self.load_config()

    def load_config(self):
        """Load master configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "version": "1.0",
                "systems": {
                    "ai_trainer": "Training for ALL devices",
                    "problem_solver": "Solutions for ANY problem",
                    "email_system": "Complete email management"
                },
                "capabilities": {
                    "devices": "ALL Apple, Windows, PC devices ever created",
                    "problems": "ANY software or hardware problem",
                    "solutions": "Solutions and workarounds for everything",
                    "training": "Complete repair team training"
                }
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def main_menu(self):
        """Master system menu"""
        while True:
            print("\n" + "="*80)
            print("🚀 NOIZYLAB MASTER SYSTEM - ULTIMATE AI PLATFORM")
            print("="*80)
            print("\n🎯 Capabilities:")
            print("  • Train repair teams for ALL devices")
            print("  • Solve ANY software/hardware problem")
            print("  • Provide solutions & workarounds")
            print("  • Complete email management")

            print("\n" + "="*80)
            print("🔥 MAIN SYSTEMS")
            print("="*80)
            print("  1. 🤖 AI Trainer (Repair Team Training)")
            print("  2. 🌍 Universal Problem Solver")
            print("  3. 📧 Email Master Control")
            print("  4. 🎓 Complete Training Program")
            print("  5. 🔧 Quick Problem Solver")
            print("  6. 📊 System Dashboard")
            print("  0. Exit")
            print("="*80)

            choice = input("\nSelect system: ").strip()

            if choice == "1":
                self.launch_ai_trainer()
            elif choice == "2":
                self.launch_problem_solver()
            elif choice == "3":
                self.launch_email_system()
            elif choice == "4":
                self.complete_training_program()
            elif choice == "5":
                self.quick_problem_solver()
            elif choice == "6":
                self.system_dashboard()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def launch_ai_trainer(self):
        """Launch AI Trainer"""
        print("\n🚀 Launching AI Trainer...")
        try:
            subprocess.run([sys.executable, str(self.base_dir / "noizylab_ai_trainer.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def launch_problem_solver(self):
        """Launch Universal Problem Solver"""
        print("\n🌍 Launching Universal Problem Solver...")
        try:
            subprocess.run([sys.executable, str(self.base_dir / "universal_problem_solver.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def launch_email_system(self):
        """Launch Email System"""
        print("\n📧 Launching Email Master Control...")
        try:
            subprocess.run([sys.executable, str(self.base_dir / "email_master_control.py")])
        except Exception as e:
            print(f"❌ Error: {e}")

    def complete_training_program(self):
        """Complete training program"""
        print("\n" + "="*80)
        print("🎓 COMPLETE TRAINING PROGRAM")
        print("="*80)

        print("\nThis program includes:")
        print("  1. Device Knowledge (ALL devices)")
        print("  2. Problem Solving (ANY problem)")
        print("  3. Repair Procedures (Remote & On-Site)")
        print("  4. Diagnostic Tools")
        print("  5. Solutions & Workarounds")

        print("\n🚀 Starting training...")
        self.launch_ai_trainer()

    def quick_problem_solver(self):
        """Quick problem solver"""
        print("\n" + "="*80)
        print("🔧 QUICK PROBLEM SOLVER")
        print("="*80)

        problem = input("\nDescribe the problem: ").strip()

        if problem:
            print("\n🤖 Analyzing...")
            print("💡 Solutions:")
            print("  1. Restart device/application")
            print("  2. Update software/drivers")
            print("  3. Check for error messages")
            print("  4. Try safe mode")
            print("  5. Reinstall if software issue")
            print("  6. Check connections if hardware")

            print("\n🔍 For detailed solutions, use Universal Problem Solver")
            use_detailed = input("Use detailed solver? (y/n): ").strip().lower()
            if use_detailed == 'y':
                self.launch_problem_solver()

    def system_dashboard(self):
        """System dashboard"""
        print("\n" + "="*80)
        print("📊 SYSTEM DASHBOARD")
        print("="*80)

        systems = {
            "AI Trainer": (self.base_dir / "noizylab_ai_trainer.py").exists(),
            "Problem Solver": (self.base_dir / "universal_problem_solver.py").exists(),
            "Email System": (self.base_dir / "email_master_control.py").exists(),
            "Knowledge Bases": (self.base_dir / "knowledge_base").exists(),
            "Solutions DB": (self.base_dir / "solutions_database").exists()
        }

        print("\n✅ System Status:")
        for system, exists in systems.items():
            status = "✅" if exists else "⏳"
            print(f"  {status} {system}")

        all_ready = all(systems.values())
        if all_ready:
            print("\n🎉 All systems operational!")
        else:
            print("\n⚠️  Some systems not ready")

if __name__ == "__main__":
    master = NOIZYLABMasterSystem()
    master.main_menu()

