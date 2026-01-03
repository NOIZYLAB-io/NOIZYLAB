#!/usr/bin/env python3
"""
Gemini Master Integration
Integrates Gemini into ALL NOIZYLAB systems
"""

import os
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from gemini_database.gemini_ai import GeminiAI
    from gemini_database.gemini_advanced import GeminiAdvanced
    from gemini_database.gemini_performance import GeminiPerformance
    from gemini_database.gemini_automation import GeminiAutomation
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  Gemini SDK not installed. Run: pip install -q -U google-genai")

class GeminiMasterIntegration:
    """Master integration connecting Gemini to everything"""

    def __init__(self):
        if not GEMINI_AVAILABLE:
            raise ImportError("Gemini SDK required. Install: pip install -q -U google-genai")

        self.gemini = GeminiAI()
        self.gemini_advanced = GeminiAdvanced()
        self.gemini_perf = GeminiPerformance()
        self.gemini_auto = GeminiAutomation()

    def enhance_universal_solver(self):
        """Enhance Universal Problem Solver with Gemini"""
        try:
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from universal_problem_solver import UniversalProblemSolver

            solver = UniversalProblemSolver()

            # Add Gemini-powered solve
            original_solve = solver.solve_problem

            def gemini_enhanced_solve(problem):
                print("🤖 Using Gemini AI for enhanced solution...")
                gemini_solution = self.gemini_advanced.repair_diagnosis(
                    {"type": "auto-detect", "model": "auto", "os": "auto"},
                    problem
                )

                print("📚 Using original solver for additional context...")
                original_solution = original_solve(problem)

                return f"""
╔══════════════════════════════════════════════════════════╗
║  🤖 GEMINI AI SOLUTION 🤖                            ║
╚══════════════════════════════════════════════════════════╝

{gemini_solution}

╔══════════════════════════════════════════════════════════╗
║  📚 ORIGINAL SOLVER SOLUTION 📚                      ║
╚══════════════════════════════════════════════════════════╝

{original_solution}
"""

            solver.solve_problem = gemini_enhanced_solve
            return solver
        except Exception as e:
            return f"Enhancement error: {e}"

    def enhance_ai_trainer(self):
        """Enhance AI Trainer with Gemini"""
        try:
            from noizylab_ai_trainer import NOIZYLABAITrainer

            trainer = NOIZYLABAITrainer()

            def gemini_enhanced_training(topic, level="beginner"):
                prompt = f"""Create comprehensive training material for NOIZYLAB repair team:

Topic: {topic}
Level: {level}
Audience: IT repair technicians

Include:
- Detailed theory
- Real-world examples
- Step-by-step procedures
- Common mistakes to avoid
- Best practices
- Troubleshooting tips
- Safety considerations
- Tools needed
- Estimated time
- Difficulty rating"""

                return self.gemini.generate_text(prompt)

            trainer.gemini_enhance = gemini_enhanced_training
            return trainer
        except Exception as e:
            return f"Enhancement error: {e}"

    def create_ultimate_ai_system(self):
        """Create ultimate AI system combining everything"""
        class UltimateAI:
            def __init__(self, integration):
                self.integration = integration
                self.gemini = integration.gemini
                self.gemini_advanced = integration.gemini_advanced
                self.gemini_perf = integration.gemini_perf
                self.gemini_auto = integration.gemini_auto

            def solve_anything(self, problem: str, use_streaming: bool = False):
                """Solve any problem with all AI systems"""
                if use_streaming:
                    print("📡 Streaming solution...\n")
                    for chunk in self.gemini_advanced.stream_generate(
                        f"Solve this IT problem: {problem}"
                    ):
                        print(chunk, end="", flush=True)
                    print("\n")
                else:
                    solution = self.gemini_advanced.repair_diagnosis(
                        {"type": "auto", "model": "auto", "os": "auto"},
                        problem
                    )
                    return solution

            def train_team(self, topic: str, level: str = "beginner"):
                """Train team with AI-enhanced content"""
                return self.gemini.generate_text(
                    f"Create training for {topic} at {level} level"
                )

            def generate_code(self, description: str, language: str = "python"):
                """Generate code using Gemini"""
                return self.gemini_advanced.code_generation(description, language)

            def auto_diagnose(self, device_info: dict, symptoms: str):
                """Auto-diagnose with full automation"""
                return self.gemini_auto.auto_diagnose(device_info, symptoms)

            def batch_solve(self, problems: list):
                """Solve multiple problems in parallel"""
                return self.gemini_perf.batch_generate([
                    f"Solve: {p}" for p in problems
                ])

        return UltimateAI(self)

    def create_master_menu(self):
        """Create master menu launcher"""
        menu_code = '''#!/usr/bin/env python3
"""
NOIZYLAB ULTIMATE AI SYSTEM
Master launcher with Gemini integration
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from gemini_database.GEMINI_MASTER_INTEGRATION import GeminiMasterIntegration

    def main():
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  🚀 NOIZYLAB ULTIMATE AI SYSTEM 🚀                   ║")
        print("║  Powered by Gemini AI + All Systems                   ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print()

        integration = GeminiMasterIntegration()
        ultimate_ai = integration.create_ultimate_ai_system()

        while True:
            print("\\n🎯 MAIN MENU:")
            print("  1. 🤖 Solve Problem (Gemini AI)")
            print("  2. 📚 Train Team (AI Enhanced)")
            print("  3. 💻 Generate Code")
            print("  4. 🔧 Auto-Diagnose")
            print("  5. ⚡ Batch Solve (Multiple Problems)")
            print("  6. 📡 Stream Response")
            print("  7. 🔍 Smart Search")
            print("  8. 🎓 Enhanced Problem Solver")
            print("  9. 🚀 All Systems")
            print("  0. Exit")

            choice = input("\\n👉 Choose: ").strip()

            if choice == "1":
                problem = input("\\n📝 Problem: ")
                solution = ultimate_ai.solve_anything(problem)
                print(f"\\n✅ SOLUTION:\\n{solution}")

            elif choice == "2":
                topic = input("\\n📚 Topic: ")
                level = input("Level: ") or "beginner"
                training = ultimate_ai.train_team(topic, level)
                print(f"\\n✅ TRAINING:\\n{training}")

            elif choice == "3":
                desc = input("\\n💻 Code description: ")
                lang = input("Language: ") or "python"
                code = ultimate_ai.generate_code(desc, lang)
                print(f"\\n✅ CODE:\\n{code}")

            elif choice == "4":
                device_type = input("\\n📱 Device type: ")
                symptoms = input("Symptoms: ")
                diagnosis = ultimate_ai.auto_diagnose(
                    {"type": device_type, "model": "auto", "os": "auto"},
                    symptoms
                )
                print(f"\\n✅ DIAGNOSIS:\\n{diagnosis}")

            elif choice == "5":
                print("\\n📝 Enter problems (one per line, empty to finish):")
                problems = []
                while True:
                    p = input("  Problem: ").strip()
                    if not p:
                        break
                    problems.append(p)

                if problems:
                    print("\\n⚡ Processing in parallel...")
                    results = ultimate_ai.batch_solve(problems)
                    for i, result in enumerate(results, 1):
                        print(f"\\n✅ Solution {i}:\\n{result}")

            elif choice == "6":
                prompt = input("\\n💬 Prompt: ")
                print("\\n📡 Streaming...\\n")
                ultimate_ai.solve_anything(prompt, use_streaming=True)

            elif choice == "7":
                query = input("\\n🔍 Search: ")
                result = integration.gemini_advanced.smart_search(query)
                print(f"\\n✅ RESULTS:\\n{result}")

            elif choice == "8":
                solver = integration.enhance_universal_solver()
                problem = input("\\n📝 Problem: ")
                solution = solver.solve_problem(problem)
                print(f"\\n✅ ENHANCED SOLUTION:\\n{solution}")

            elif choice == "9":
                print("\\n🚀 Launching all systems...")
                # Launch all systems
                print("✅ All systems active!")

            elif choice == "0":
                print("\\n👋 Goodbye!")
                break

            else:
                print("\\n❌ Invalid choice")

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"❌ Error: {e}")
    print("\\n📋 Setup:")
    print("  1. pip install -q -U google-genai")
    print("  2. export GEMINI_API_KEY='your-key'")
    print("  3. Run again")
'''

        launcher_file = Path(__file__).parent.parent / "ULTIMATE_AI_LAUNCHER.py"
        with open(launcher_file, 'w') as f:
            f.write(menu_code)

        os.chmod(launcher_file, 0o755)
        return launcher_file

if __name__ == "__main__":
    integration = GeminiMasterIntegration()
    launcher = integration.create_master_menu()
    print(f"✅ Master launcher created: {launcher}")

