#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Gemini Code Analyzer
Analyze code for bugs, race conditions, and issues using Gemini 3 Pro
"""

import os
from typing import Optional
from google import genai
from google.genai import types

class GeminiCodeAnalyzer:
    """Analyze code using Gemini 3 Pro"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini Code Analyzer

        Args:
            api_key: Your Gemini API key. If not provided, uses GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not set. Get one from: https://aistudio.google.com/app/api-keys\n"
                "Then set it: export GEMINI_API_KEY='your-key'"
            )

        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key

        self.client = genai.Client()

    def analyze_code(self, code: str, language: str = "auto",
                     analysis_type: str = "race_conditions") -> str:
        """
        Analyze code for issues

        Args:
            code: Code to analyze
            language: Programming language (auto-detected if "auto")
            analysis_type: Type of analysis (race_conditions, bugs, security, performance)

        Returns:
            Analysis results
        """
        prompts = {
            "race_conditions": f"Find the race condition in this multi-threaded {language} snippet: {code}",
            "bugs": f"Find all bugs and issues in this {language} code: {code}",
            "security": f"Find security vulnerabilities in this {language} code: {code}",
            "performance": f"Analyze performance issues and optimizations for this {language} code: {code}",
            "general": f"Analyze this {language} code and provide improvements: {code}"
        }

        prompt = prompts.get(analysis_type, prompts["general"])

        try:
            response = self.client.models.generate_content(
                model="gemini-3-pro-preview",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def find_race_conditions(self, code: str, language: str = "C++") -> str:
        """Find race conditions in multi-threaded code"""
        return self.analyze_code(code, language, "race_conditions")

    def find_bugs(self, code: str, language: str = "auto") -> str:
        """Find bugs in code"""
        return self.analyze_code(code, language, "bugs")

    def find_security_issues(self, code: str, language: str = "auto") -> str:
        """Find security vulnerabilities"""
        return self.analyze_code(code, language, "security")

    def analyze_performance(self, code: str, language: str = "auto") -> str:
        """Analyze performance issues"""
        return self.analyze_code(code, language, "performance")

    def analyze_file(self, file_path: str, analysis_type: str = "general") -> str:
        """Analyze code from a file"""
        try:
            with open(file_path, 'r') as f:
                code = f.read()

            # Detect language from extension
            ext = file_path.split('.')[-1]
            language_map = {
                'py': 'Python',
                'cpp': 'C++',
                'c': 'C',
                'java': 'Java',
                'js': 'JavaScript',
                'ts': 'TypeScript',
                'swift': 'Swift',
                'go': 'Go',
                'rs': 'Rust'
            }
            language = language_map.get(ext, "auto")

            return self.analyze_code(code, language, analysis_type)
        except Exception as e:
            return f"Error reading file: {e}"

# Usage example
if __name__ == "__main__":
    try:
        analyzer = GeminiCodeAnalyzer()

        # Example: Analyze C++ code for race conditions
        cpp_code = """
        #include <thread>
        #include <iostream>

        int counter = 0;

        void increment() {
            for (int i = 0; i < 100000; i++) {
                counter++;
            }
        }

        int main() {
            std::thread t1(increment);
            std::thread t2(increment);
            t1.join();
            t2.join();
            std::cout << counter << std::endl;
            return 0;
        }
        """

        print("🔍 Analyzing code for race conditions...\n")
        result = analyzer.find_race_conditions(cpp_code, "C++")
        print(result)

    except ValueError as e:
        print(f"❌ {e}")
        print("\n📋 Quick Setup:")
        print("  1. Get API key: https://aistudio.google.com/app/api-keys")
        print("  2. Set it: export GEMINI_API_KEY='your-key'")
        print("  3. Install SDK: pip install -q -U google-genai")
    except Exception as e:
        print(f"❌ Error: {e}")

