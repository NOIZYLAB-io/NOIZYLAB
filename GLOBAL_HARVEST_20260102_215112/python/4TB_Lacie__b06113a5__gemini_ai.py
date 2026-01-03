#!/usr/bin/env python3
"""
Gemini AI Integration - Python
Use Google Gemini AI in your system
Official SDK: https://ai.google.dev/gemini-api/docs/quickstart
"""

import os
from typing import Optional
from google import genai

class GeminiAI:
    """Google Gemini AI integration using official SDK"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini AI client

        Args:
            api_key: Your Gemini API key. If not provided, uses GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not set. Get one from: https://aistudio.google.com/app/api-keys\n"
                "Then set it: export GEMINI_API_KEY='your-key'"
            )

        # Initialize client with API key
        # The SDK automatically uses GEMINI_API_KEY env var, but we can also pass it
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key

        self.client = genai.Client()

    def generate_text(self, prompt: str, model: str = "gemini-2.5-flash") -> str:
        """
        Generate text using Gemini

        Args:
            prompt: Text prompt to send to Gemini
            model: Model to use (default: gemini-2.5-flash)

        Returns:
            Generated text response
        """
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def solve_problem(self, problem: str) -> str:
        """
        Solve an IT problem using Gemini

        Args:
            problem: Description of the problem to solve

        Returns:
            Detailed solution with diagnosis, steps, alternatives, and prevention
        """
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
        """
        Analyze image using Gemini Pro Vision

        Args:
            image_path: Path to image file
            question: Question about the image

        Returns:
            Analysis of the image
        """
        try:
            from google.genai import types

            # Read image file
            with open(image_path, 'rb') as f:
                image_data = f.read()

            # Create image part
            image_part = types.Part.from_bytes(
                image_data,
                mime_type="image/jpeg"
            )

            # Generate content with text and image
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    question,
                    image_part
                ]
            )

            return response.text
        except Exception as e:
            return f"Error: {e}"

# Usage example
if __name__ == "__main__":
    # Option 1: Set environment variable
    # export GEMINI_API_KEY='your-api-key-here'

    # Option 2: Pass API key directly
    # gemini = GeminiAI(api_key='your-api-key-here')

    try:
        gemini = GeminiAI()

        # Solve a problem
        print("🤖 Solving problem with Gemini AI...\n")
        problem = "My MacBook won't turn on"
        solution = gemini.solve_problem(problem)
        print(solution)

        # Generate text
        print("\n" + "="*60)
        print("📝 Generating text...\n")
        text = gemini.generate_text("Explain how to fix an iPhone in 3 steps")
        print(text)

    except ValueError as e:
        print(f"❌ {e}")
        print("\n📋 Quick Setup:")
        print("  1. Get API key: https://aistudio.google.com/app/api-keys")
        print("  2. Set it: export GEMINI_API_KEY='your-key'")
        print("  3. Install SDK: pip install -q -U google-genai")
