#!/usr/bin/env python3
"""
Gemini AI Integration - Google's Gemini AI
Complete integration with Google Gemini
"""

import json
import os
from pathlib import Path

class GeminiIntegration:
    """Google Gemini AI integration"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.gemini_db = self.base_dir / "gemini_database"
        self.gemini_db.mkdir(exist_ok=True)
        self.api_key = os.getenv('GEMINI_API_KEY', '')

    def create_gemini_config(self):
        """Create Gemini configuration"""
        print("\n" + "="*80)
        print("🤖 GEMINI AI INTEGRATION")
        print("="*80)

        config = {
            "api_key": self.api_key or "YOUR_API_KEY_HERE",
            "models": {
                "gemini_pro": "gemini-pro",
                "gemini_pro_vision": "gemini-pro-vision",
                "gemini_ultra": "gemini-ultra"
            },
            "features": {
                "text_generation": True,
                "image_understanding": True,
                "code_generation": True,
                "problem_solving": True,
                "multimodal": True,
                "streaming": True
            },
            "endpoints": {
                "chat": "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                "stream": "https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent"
            }
        }

        config_file = self.gemini_db / "gemini_config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)

        print("\n✅ Gemini Configuration Created")
        print(f"  • API Key: {'✅ Set' if self.api_key else '⏳ Not set'}")
        print("  • Models: Gemini Pro, Pro Vision, Ultra")
        print("  • Features: Text, Image, Code, Multimodal")

        return config

    def create_gemini_code(self):
        """Create Gemini integration code"""
        print("\n📝 Creating Gemini Code...")

        # Python code
        python_code = '''#!/usr/bin/env python3
"""
Gemini AI Integration - Python
Use Google Gemini AI in your system
"""

import json
import os
import requests
from typing import Optional, List, Dict

class GeminiAI:
    """Google Gemini AI integration"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set. Get one from: https://makersuite.google.com/app/apikey")

    def generate_text(self, prompt: str, model: str = "gemini-pro") -> str:
        """Generate text using Gemini"""
        url = f"{self.base_url}/models/{model}:generateContent"

        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "key": self.api_key
        }

        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }

        try:
            response = requests.post(url, headers=headers, params=params, json=data)
            response.raise_for_status()
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Error: {e}"

    def solve_problem(self, problem: str) -> str:
        """Solve a problem using Gemini"""
        prompt = f"""You are an expert IT repair technician. Solve this problem:

{problem}

Provide:
1. Diagnosis
2. Step-by-step solution
3. Alternative solutions if needed
4. Prevention tips

Be clear, concise, and actionable."""

        return self.generate_text(prompt)

    def analyze_image(self, image_path: str, question: str) -> str:
        """Analyze image using Gemini Pro Vision"""
        import base64

        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        url = f"{self.base_url}/models/gemini-pro-vision:generateContent"

        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}

        data = {
            "contents": [{
                "parts": [
                    {"text": question},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_data
                        }
                    }
                ]
            }]
        }

        try:
            response = requests.post(url, headers=headers, params=params, json=data)
            response.raise_for_status()
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Error: {e}"

# Usage example
if __name__ == "__main__":
    # Set your API key
    # os.environ['GEMINI_API_KEY'] = 'your-api-key-here'

    gemini = GeminiAI()

    # Solve a problem
    problem = "My MacBook won't turn on"
    solution = gemini.solve_problem(problem)
    print(solution)
'''

        python_file = self.gemini_db / "gemini_ai.py"
        with open(python_file, 'w') as f:
            f.write(python_code)

        # Swift code for iOS
        swift_code = '''//
// GeminiAI.swift
// Gemini AI Integration for iOS
//

import Foundation

class GeminiAI {
    private let apiKey: String
    private let baseURL = "https://generativelanguage.googleapis.com/v1beta"

    init(apiKey: String) {
        self.apiKey = apiKey
    }

    func generateText(prompt: String, model: String = "gemini-pro") async throws -> String {
        let url = URL(string: "\\(baseURL)/models/\\(model):generateContent?key=\\(apiKey)")!

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body: [String: Any] = [
            "contents": [[
                "parts": [["text": prompt]]
            ]]
        ]

        request.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (data, _) = try await URLSession.shared.data(for: request)
        let response = try JSONDecoder().decode(GeminiResponse.self, from: data)

        return response.candidates[0].content.parts[0].text
    }

    func solveProblem(_ problem: String) async throws -> String {
        let prompt = """
        You are an expert IT repair technician. Solve this problem:

        \\(problem)

        Provide:
        1. Diagnosis
        2. Step-by-step solution
        3. Alternative solutions
        4. Prevention tips
        """

        return try await generateText(prompt: prompt)
    }
}

struct GeminiResponse: Codable {
    let candidates: [Candidate]

    struct Candidate: Codable {
        let content: Content
    }

    struct Content: Codable {
        let parts: [Part]
    }

    struct Part: Codable {
        let text: String
    }
}
'''

        swift_file = self.gemini_db / "GeminiAI.swift"
        with open(swift_file, 'w') as f:
            f.write(swift_code)

        print("  ✅ Python code: gemini_ai.py")
        print("  ✅ Swift code: GeminiAI.swift")

        return python_file, swift_file

    def create_setup_guide(self):
        """Create setup guide"""
        guide = {
            "setup_steps": [
                "1. Get API key from https://aistudio.google.com/app/api-keys",
                "2. Set environment variable: export GEMINI_API_KEY='your-key'",
                "3. Or add to .env file: GEMINI_API_KEY=your-key",
                "4. Install requests: pip install requests",
                "5. Use GeminiAI class in your code"
            ],
            "usage": {
                "python": "from gemini_ai import GeminiAI; ai = GeminiAI(); result = ai.solve_problem('problem')",
                "swift": "let ai = GeminiAI(apiKey: 'key'); let result = try await ai.solveProblem('problem')"
            },
            "models": {
                "gemini-pro": "Text generation, problem solving",
                "gemini-pro-vision": "Image understanding, multimodal",
                "gemini-ultra": "Most advanced (when available)"
            }
        }

        guide_file = self.gemini_db / "setup_guide.json"
        with open(guide_file, 'w') as f:
            json.dump(guide, f, indent=2)

        print("\n✅ Setup guide created")
        return guide

    def create_example_usage(self):
        """Create example usage"""
        example = '''# Example Usage

from gemini_ai import GeminiAI

# Initialize
gemini = GeminiAI(api_key="your-api-key")

# Solve a problem
problem = "My iPhone screen is cracked"
solution = gemini.solve_problem(problem)
print(solution)

# Generate text
text = gemini.generate_text("Explain how to fix a MacBook")
print(text)

# Analyze image (requires gemini-pro-vision)
analysis = gemini.analyze_image("device_photo.jpg", "What device is this?")
print(analysis)
'''

        example_file = self.gemini_db / "example_usage.py"
        with open(example_file, 'w') as f:
            f.write(example)

        print("  ✅ Example usage created")

    def run_setup(self):
        """Run complete setup"""
        print("\n" + "="*80)
        print("🤖 GEMINI AI INTEGRATION SETUP")
        print("="*80)

        config = self.create_gemini_config()
        python_file, swift_file = self.create_gemini_code()
        guide = self.create_setup_guide()
        self.create_example_usage()

        print("\n" + "="*80)
        print("✅ GEMINI INTEGRATION COMPLETE!")
        print("="*80)

        print("\n📋 Next Steps:")
        print("  1. Get API key: https://aistudio.google.com/app/api-keys")
        print("  2. Set API key: export GEMINI_API_KEY='your-key'")
        print("  3. Use in your code:")
        print("     from gemini_ai import GeminiAI")
        print("     ai = GeminiAI()")
        print("     result = ai.solve_problem('your problem')")

        print("\n📁 Files Created:")
        print(f"  • {python_file.name} - Python integration")
        print(f"  • {swift_file.name} - Swift integration")
        print("  • setup_guide.json - Setup instructions")
        print("  • example_usage.py - Usage examples")

        print("\n🚀 Ready to use Gemini AI!")
        print("="*80)

if __name__ == "__main__":
    gemini = GeminiIntegration()
    gemini.run_setup()

