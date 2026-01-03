#!/usr/bin/env python3
"""
Gemini Integration with NOIZYLAB Systems
Connects Gemini AI to all existing systems
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from .gemini_ai import GeminiAI
from .gemini_advanced import GeminiAdvanced

class NOIZYLABGeminiIntegration:
    """Integrate Gemini with all NOIZYLAB systems"""

    def __init__(self):
        self.gemini = GeminiAI()
        self.gemini_advanced = GeminiAdvanced()
        self.base_dir = Path(__file__).parent.parent

    def integrate_with_problem_solver(self):
        """Integrate with Universal Problem Solver"""
        try:
            from universal_problem_solver import UniversalProblemSolver
            solver = UniversalProblemSolver()

            # Enhance solver with Gemini
            original_solve = solver.solve_problem

            def enhanced_solve(problem):
                # Try Gemini first
                gemini_solution = self.gemini.solve_problem(problem)
                # Then use original solver
                original_solution = original_solve(problem)
                return f"GEMINI AI SOLUTION:\n{gemini_solution}\n\nORIGINAL SOLVER:\n{original_solution}"

            solver.solve_problem = enhanced_solve
            return solver
        except Exception as e:
            return f"Integration error: {e}"

    def integrate_with_ai_trainer(self):
        """Integrate with AI Trainer"""
        try:
            from noizylab_ai_trainer import NOIZYLABAITrainer
            trainer = NOIZYLABAITrainer()

            # Enhance training with Gemini
            def gemini_enhanced_training(topic, level):
                prompt = f"""Create comprehensive training material for:
Topic: {topic}
Level: {level}

Include:
- Theory
- Practical examples
- Step-by-step guides
- Common mistakes
- Best practices"""

                training_content = self.gemini.generate_text(prompt)
                return training_content

            trainer.gemini_enhance = gemini_enhanced_training
            return trainer
        except Exception as e:
            return f"Integration error: {e}"

    def create_unified_ai_system(self):
        """Create unified AI system combining all capabilities"""
        class UnifiedAI:
            def __init__(self, gemini_integration):
                self.gemini = gemini_integration.gemini
                self.gemini_advanced = gemini_integration.gemini_advanced
                self.integration = gemini_integration

            def solve_anything(self, problem: str):
                """Solve any problem using all AI systems"""
                # Use Gemini advanced repair diagnosis
                solution = self.gemini_advanced.repair_diagnosis(
                    {"type": "auto-detect", "model": "auto", "os": "auto"},
                    problem
                )
                return solution

            def train_team(self, topic: str, level: str = "beginner"):
                """Train team with AI-enhanced content"""
                return self.integration.integrate_with_ai_trainer()

            def generate_code(self, description: str, language: str = "python"):
                """Generate code using Gemini"""
                return self.gemini_advanced.code_generation(description, language)

            def stream_response(self, prompt: str):
                """Stream real-time responses"""
                return self.gemini_advanced.stream_generate(prompt)

        return UnifiedAI(self)

    def create_master_ai_launcher(self):
        """Create master launcher for all AI systems"""
        launcher_code = '''#!/usr/bin/env python3
"""
NOIZYLAB Master AI Launcher
Unified access to all AI systems including Gemini
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from gemini_integration import NOIZYLABGeminiIntegration

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║  🤖 NOIZYLAB MASTER AI SYSTEM 🤖                    ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    integration = NOIZYLABGeminiIntegration()
    unified_ai = integration.create_unified_ai_system()

    while True:
        print("\\n🎯 OPTIONS:")
        print("  1. Solve Problem (Gemini AI)")
        print("  2. Train Team (AI Enhanced)")
        print("  3. Generate Code")
        print("  4. Stream Response")
        print("  5. Advanced Repair Diagnosis")
        print("  6. Smart Search")
        print("  7. Exit")

        choice = input("\\n👉 Choose: ").strip()

        if choice == "1":
            problem = input("\\n📝 Problem: ")
            solution = unified_ai.solve_anything(problem)
            print(f"\\n✅ SOLUTION:\\n{solution}")

        elif choice == "2":
            topic = input("\\n📚 Topic: ")
            level = input("Level (beginner/intermediate/advanced): ")
            training = unified_ai.train_team(topic, level)
            print(f"\\n✅ TRAINING READY")

        elif choice == "3":
            desc = input("\\n💻 Code description: ")
            lang = input("Language (python/swift/javascript): ") or "python"
            code = unified_ai.generate_code(desc, lang)
            print(f"\\n✅ CODE:\\n{code}")

        elif choice == "4":
            prompt = input("\\n💬 Prompt: ")
            print("\\n📡 Streaming response...\\n")
            for chunk in unified_ai.stream_response(prompt):
                print(chunk, end="", flush=True)
            print()

        elif choice == "5":
            symptoms = input("\\n🔧 Symptoms: ")
            solution = integration.gemini_advanced.repair_diagnosis(
                {"type": "auto", "model": "auto", "os": "auto"},
                symptoms
            )
            print(f"\\n✅ DIAGNOSIS:\\n{solution}")

        elif choice == "6":
            query = input("\\n🔍 Search query: ")
            result = integration.gemini_advanced.smart_search(query)
            print(f"\\n✅ RESULTS:\\n{result}")

        elif choice == "7":
            print("\\n👋 Goodbye!")
            break

        else:
            print("\\n❌ Invalid choice")

if __name__ == "__main__":
    main()
'''

        launcher_file = self.base_dir / "MASTER_AI_LAUNCHER.py"
        with open(launcher_file, 'w') as f:
            f.write(launcher_code)

        os.chmod(launcher_file, 0o755)
        return launcher_file

