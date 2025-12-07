#!/usr/bin/env python3
# Example Usage

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
