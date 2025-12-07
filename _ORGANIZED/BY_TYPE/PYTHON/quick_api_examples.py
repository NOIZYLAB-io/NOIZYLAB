#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick API Examples - How to Call Gemini API
All the different ways to use the API
"""

import os

# ============================================================================
# METHOD 1: Official SDK (Direct)
# ============================================================================

def example_official_sdk():
    """Example using official Google SDK"""
    from google import genai

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents="Explain how AI works in simple terms"
    )

    print("Official SDK Response:")
    print(response.text)
    print()


# ============================================================================
# METHOD 2: Our Wrapper (Easier)
# ============================================================================

def example_wrapper():
    """Example using our wrapper class"""
    from gemini_ai import GeminiAI

    gemini = GeminiAI()

    # Simple generation
    result = gemini.generate_text("What is Python?")
    print("Wrapper Response:")
    print(result)
    print()

    # Solve problem
    solution = gemini.solve_problem("My MacBook won't turn on")
    print("Problem Solution:")
    print(solution)
    print()


# ============================================================================
# METHOD 3: Advanced Features
# ============================================================================

def example_advanced():
    """Example using advanced features"""
    from gemini_advanced import GeminiAdvanced

    gemini = GeminiAdvanced()

    # Streaming
    print("Streaming Response:")
    for chunk in gemini.stream_generate("Count to 10"):
        print(chunk, end="", flush=True)
    print("\n")

    # Code generation
    code = gemini.code_generation("Create a hello world function", "python")
    print("Generated Code:")
    print(code)
    print()


# ============================================================================
# METHOD 4: Code Analysis
# ============================================================================

def example_code_analysis():
    """Example using code analyzer"""
    from gemini_code_analyzer import GeminiCodeAnalyzer

    analyzer = GeminiCodeAnalyzer()

    # Example C++ code
    cpp_code = """
    #include <thread>
    int counter = 0;
    void increment() { counter++; }
    """

    result = analyzer.find_race_conditions(cpp_code, "C++")
    print("Code Analysis:")
    print(result)
    print()


# ============================================================================
# METHOD 5: REST API (Web Interface)
# ============================================================================

def example_rest_api():
    """Example using REST API"""
    import requests

    # Start web interface first: python3 gemini_web_interface.py
    url = "http://localhost:5000/solve"

    data = {
        "problem": "My iPhone won't charge"
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()
        print("REST API Response:")
        print(result.get('solution', 'No solution'))
    except Exception as e:
        print(f"REST API Error: {e}")
        print("Make sure web interface is running:")
        print("  python3 gemini_web_interface.py")
    print()


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run all examples"""
    print("="*80)
    print("🔌 GEMINI API - QUICK EXAMPLES")
    print("="*80)
    print()

    # Check API key
    if not os.getenv('GEMINI_API_KEY'):
        print("❌ GEMINI_API_KEY not set!")
        print("\n📋 Setup:")
        print("  1. Get API key: https://aistudio.google.com/app/api-keys")
        print("  2. Set it: export GEMINI_API_KEY='your-key'")
        print("  3. Install: pip install -q -U google-genai")
        return

    print("✅ API Key found!")
    print()

    # Run examples
    try:
        print("1️⃣  Official SDK Example:")
        example_official_sdk()
    except Exception as e:
        print(f"   ⚠️  Error: {e}")
        print("   Install: pip install -q -U google-genai")
        print()

    try:
        print("2️⃣  Wrapper Example:")
        example_wrapper()
    except Exception as e:
        print(f"   ⚠️  Error: {e}")
        print()

    try:
        print("3️⃣  Advanced Example:")
        example_advanced()
    except Exception as e:
        print(f"   ⚠️  Error: {e}")
        print()

    try:
        print("4️⃣  Code Analysis Example:")
        example_code_analysis()
    except Exception as e:
        print(f"   ⚠️  Error: {e}")
        print()

    print("5️⃣  REST API Example:")
    example_rest_api()

    print("="*80)
    print("✅ All examples complete!")
    print("="*80)

if __name__ == "__main__":
    main()

