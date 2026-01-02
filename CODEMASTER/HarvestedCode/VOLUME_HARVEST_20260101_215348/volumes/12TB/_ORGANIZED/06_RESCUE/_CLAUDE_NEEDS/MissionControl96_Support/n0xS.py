#!/usr/bin/env python3
"""
AI Code Assistant - NoizyFish Edition
Advanced coding helper with OpenAI GPT integration
"""

import os
import openai
from typing import List, Dict, Optional
import json
import argparse
from datetime import datetime

class CodeAssistant:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AI Code Assistant"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.conversation_history = []
        
    def analyze_code(self, code: str, language: str = "python") -> str:
        """Analyze code for improvements, bugs, and suggestions"""
        prompt = f"""
        Please analyze this {language} code and provide:
        1. Code quality assessment
        2. Potential bugs or issues
        3. Performance improvements
        4. Best practices recommendations
        5. Security considerations
        
        Code:
        ```{language}
        {code}
        ```
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert code reviewer and software architect."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    def generate_code(self, description: str, language: str = "python") -> str:
        """Generate code based on description"""
        prompt = f"""
        Generate clean, well-documented {language} code for:
        {description}
        
        Requirements:
        - Include proper error handling
        - Add comprehensive docstrings/comments
        - Follow best practices for {language}
        - Include example usage if applicable
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an expert {language} developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def refactor_code(self, code: str, language: str = "python") -> str:
        """Refactor code for better structure and readability"""
        prompt = f"""
        Refactor this {language} code to improve:
        - Readability and maintainability
        - Performance
        - Code structure and organization
        - Error handling
        - Documentation
        
        Original code:
        ```{language}
        {code}
        ```
        
        Provide the refactored code with explanations of changes made.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior software engineer specializing in code refactoring."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    def explain_code(self, code: str, language: str = "python") -> str:
        """Explain what the code does in plain English"""
        prompt = f"""
        Explain this {language} code in clear, simple terms:
        
        ```{language}
        {code}
        ```
        
        Include:
        - What the code does overall
        - How each main section works
        - Any algorithms or patterns used
        - Potential use cases
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a technical educator who explains code clearly."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def debug_code(self, code: str, error_message: str, language: str = "python") -> str:
        """Help debug code issues"""
        prompt = f"""
        Debug this {language} code that's producing an error:
        
        Error message:
        {error_message}
        
        Code:
        ```{language}
        {code}
        ```
        
        Please provide:
        1. Explanation of what's causing the error
        2. Fixed version of the code
        3. Prevention tips for similar issues
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert debugger and problem solver."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("--mode", choices=["analyze", "generate", "refactor", "explain", "debug"], 
                       required=True, help="Assistant mode")
    parser.add_argument("--code", help="Code to analyze (or file path)")
    parser.add_argument("--description", help="Description for code generation")
    parser.add_argument("--error", help="Error message for debugging")
    parser.add_argument("--language", default="python", help="Programming language")
    parser.add_argument("--file", help="Read code from file")
    
    args = parser.parse_args()
    
    assistant = CodeAssistant()
    
    # Read code from file if specified
    if args.file:
        with open(args.file, 'r') as f:
            code = f.read()
    else:
        code = args.code
    
    try:
        if args.mode in ["analyze", "refactor", "explain", "debug"]:
            if not code:
                raise ValueError("No code provided. Use --code or --file to supply code input.")
        if args.mode == "analyze":
            result = assistant.analyze_code(code, args.language)
        elif args.mode == "generate":
            if not args.description:
                raise ValueError("No description provided. Use --description for code generation.")
            result = assistant.generate_code(args.description, args.language)
        elif args.mode == "refactor":
            result = assistant.refactor_code(code, args.language)
        elif args.mode == "explain":
            result = assistant.explain_code(code, args.language)
        elif args.mode == "debug":
            if not args.error:
                raise ValueError("No error message provided. Use --error for debugging.")
            result = assistant.debug_code(code, args.error, args.language)
        
        print(f"\n{'='*60}")
        print(f"AI CODE ASSISTANT - {args.mode.upper()} MODE")
        print(f"{'='*60}\n")
        print(result)
        print(f"\n{'='*60}")
        
        # Save result to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"ai_assistant_{args.mode}_{timestamp}.md"
        with open(output_file, 'w') as f:
            f.write(f"# AI Code Assistant - {args.mode.title()}\n\n")
            f.write(f"**Timestamp:** {datetime.now()}\n\n")
            f.write(result)
        
        print(f"Result saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()