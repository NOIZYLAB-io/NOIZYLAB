#!/usr/bin/env python3
"""
NOIZYLAB UNIFIED SYSTEM
All systems synthesized into one powerful interface
"""

import os
import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "gemini_database"))

class NOIZYLABUnified:
    """Unified NOIZYLAB system"""
    
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY', '')
        self.base_dir = Path(__file__).parent
        
        # Initialize systems
        self._init_systems()
    
    def _init_systems(self):
        """Initialize all systems"""
        try:
            from gemini_database.gemini_ai import GeminiAI
            self.gemini = GeminiAI() if self.api_key else None
        except:
            self.gemini = None
        
        try:
            from universal_problem_solver import UniversalProblemSolver
            self.problem_solver = UniversalProblemSolver()
        except:
            self.problem_solver = None
    
    def solve(self, problem: str):
        """Solve any problem using all systems"""
        solutions = []
        
        if self.gemini:
            try:
                solution = self.gemini.solve_problem(problem)
                solutions.append(("Gemini AI", solution))
            except:
                pass
        
        if self.problem_solver:
            try:
                solution = self.problem_solver.solve_problem(problem)
                solutions.append(("Problem Solver", solution))
            except:
                pass
        
        return solutions
    
    def analyze_code(self, code: str, language: str = "auto"):
        """Analyze code"""
        if not self.gemini:
            return "Gemini AI not available"
        
        try:
            from gemini_database.gemini_code_analyzer import GeminiCodeAnalyzer
            analyzer = GeminiCodeAnalyzer()
            return analyzer.find_bugs(code)
        except Exception as e:
            return f"Error: {e}"

def main():
    """Main entry point"""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║  🏢 NOIZYLAB UNIFIED SYSTEM 🏢                        ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    
    system = NOIZYLABUnified()
    
    while True:
        print("\n🎯 Options:")
        print("  1. Solve Problem")
        print("  2. Analyze Code")
        print("  3. System Status")
        print("  0. Exit")
        
        choice = input("\n👉 Choose: ").strip()
        
        if choice == "1":
            problem = input("\n📝 Problem: ")
            solutions = system.solve(problem)
            for name, solution in solutions:
                print(f"\n✅ {name}:\n{solution[:300]}...")
        
        elif choice == "2":
            code = input("\n💻 Code: ")
            result = system.analyze_code(code)
            print(f"\n✅ Analysis:\n{result}")
        
        elif choice == "3":
            print("\n📊 System Status:")
            print(f"   Gemini AI: {'✅' if system.gemini else '❌'}")
            print(f"   Problem Solver: {'✅' if system.problem_solver else '❌'}")
        
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
