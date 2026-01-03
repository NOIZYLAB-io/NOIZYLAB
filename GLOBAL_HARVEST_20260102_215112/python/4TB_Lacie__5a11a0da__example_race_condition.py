#!/usr/bin/env python3
"""
Example: Using Gemini to find race conditions
Based on the official Gemini API pattern
"""

import os
from google import genai
from google.genai import types

# Set your API key
# os.environ['GEMINI_API_KEY'] = 'your-api-key-here'

def analyze_race_condition():
    """Example of analyzing code for race conditions"""

    # Initialize client
    client = genai.Client()

    # Example C++ code with potential race condition
    code_snippet = """
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

    # Analyze using Gemini 3 Pro
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=f"Find the race condition in this multi-threaded C++ snippet: {code_snippet}"
    )

    print("🔍 RACE CONDITION ANALYSIS:")
    print("=" * 80)
    print(response.text)
    print("=" * 80)

if __name__ == "__main__":
    try:
        analyze_race_condition()
    except ValueError as e:
        print(f"❌ {e}")
        print("\n📋 Setup:")
        print("  1. Get API key: https://aistudio.google.com/app/api-keys")
        print("  2. Set it: export GEMINI_API_KEY='your-key'")
        print("  3. Install: pip install -q -U google-genai")
    except Exception as e:
        print(f"❌ Error: {e}")

