#!/usr/bin/env python3
"""
Enhanced AI Engine - Multi-Model AI with Advanced Features
==========================================================
"""

import google.generativeai as genai
from anthropic import Anthropic
import os
from typing import Dict, List, Optional
from rich.console import Console

console = Console()

class EnhancedAIEngine:
    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")
        self.claude_key = os.getenv("ANTHROPIC_API_KEY", "")
        
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key)
            self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.gemini_model = None
        
        if self.claude_key:
            self.claude_client = Anthropic(api_key=self.claude_key)
        else:
            self.claude_client = None
    
    def analyze_email(self, email_data: Dict) -> Dict:
        """Analyze email with multiple AI models"""
        prompt = f"Analyze this email data and provide insights: {email_data}"
        
        results = {}
        
        # Gemini analysis
        if self.gemini_model:
            try:
                response = self.gemini_model.generate_content(prompt)
                results["gemini"] = {
                    "analysis": response.text,
                    "confidence": 0.9
                }
            except Exception as e:
                results["gemini"] = {"error": str(e)}
        
        # Claude analysis
        if self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}]
                )
                results["claude"] = {
                    "analysis": response.content[0].text,
                    "confidence": 0.9
                }
            except Exception as e:
                results["claude"] = {"error": str(e)}
        
        # Combine results
        return {
            "analyses": results,
            "ensemble_confidence": 0.95 if len(results) > 1 else 0.9,
            "recommendations": self._generate_recommendations(results)
        }
    
    def _generate_recommendations(self, analyses: Dict) -> List[str]:
        """Generate recommendations from analyses"""
        recommendations = []
        
        if "gemini" in analyses and "error" not in analyses["gemini"]:
            recommendations.append("Gemini analysis available")
        
        if "claude" in analyses and "error" not in analyses["claude"]:
            recommendations.append("Claude analysis available")
        
        if len(analyses) > 1:
            recommendations.append("Multi-model ensemble provides high confidence")
        
        return recommendations
    
    def generate_email_content(self, purpose: str, tone: str = "professional") -> Dict:
        """Generate email content using AI"""
        prompt = f"Generate a {tone} email for: {purpose}"
        
        if self.gemini_model:
            try:
                response = self.gemini_model.generate_content(prompt)
                return {
                    "subject": "AI Generated Subject",
                    "body": response.text,
                    "tone": tone
                }
            except Exception as e:
                return {"error": str(e)}
        
        return {"error": "No AI models configured"}

if __name__ == "__main__":
    engine = EnhancedAIEngine()
    console.print("[bold blue]Enhanced AI Engine[/bold blue]")
    console.print("✅ Ready for multi-model AI analysis")

