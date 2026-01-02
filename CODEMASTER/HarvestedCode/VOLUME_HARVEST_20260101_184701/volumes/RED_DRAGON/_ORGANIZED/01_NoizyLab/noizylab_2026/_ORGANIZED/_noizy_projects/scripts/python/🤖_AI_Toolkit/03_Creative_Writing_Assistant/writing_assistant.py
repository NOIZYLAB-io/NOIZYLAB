#!/usr/bin/env python3
"""
Creative Writing Assistant - NoizyFish Edition
AI-powered writing helper for lyrics, documentation, stories, and creative content
"""

import os
import openai
from typing import List, Dict, Optional, Tuple
import json
import argparse
from datetime import datetime
import random

class CreativeWritingAssistant:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Creative Writing Assistant"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.writing_styles = {
            'lyrics': "You are a professional songwriter and lyricist.",
            'story': "You are a creative fiction writer.",
            'documentation': "You are a technical writer who creates clear, comprehensive documentation.",
            'poetry': "You are a poet who crafts meaningful, rhythmic verse.",
            'marketing': "You are a creative copywriter and marketing specialist.",
            'script': "You are a screenwriter and dialogue specialist."
        }
    
    def generate_lyrics(self, theme: str, genre: str = "general", mood: str = "upbeat", 
                       structure: str = "verse-chorus-verse-chorus-bridge-chorus") -> str:
        """Generate song lyrics based on parameters"""
        prompt = f"""
        Write song lyrics with these specifications:
        - Theme: {theme}
        - Genre: {genre}
        - Mood: {mood}
        - Structure: {structure}
        
        Requirements:
        - Create engaging, memorable lyrics
        - Use appropriate rhyme schemes
        - Match the mood and genre
        - Include emotional depth
        - Make it singable and rhythmic
        
        Format the output clearly with section labels (Verse 1, Chorus, etc.)
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['lyrics']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    def improve_lyrics(self, existing_lyrics: str, feedback: str = "") -> str:
        """Improve existing lyrics"""
        prompt = f"""
        Improve these lyrics based on the feedback provided:
        
        Original lyrics:
        {existing_lyrics}
        
        Feedback/Areas to improve:
        {feedback if feedback else "General improvement for flow, rhythm, and emotional impact"}
        
        Provide:
        1. Improved version of the lyrics
        2. Explanation of changes made
        3. Alternative lines or phrases where applicable
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['lyrics']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        
        return response.choices[0].message.content
    
    def write_story(self, prompt: str, length: str = "short", genre: str = "general") -> str:
        """Generate creative stories"""
        length_guide = {
            'flash': "100-300 words",
            'short': "500-1500 words", 
            'medium': "1500-3000 words",
            'long': "3000+ words"
        }
        
        story_prompt = f"""
        Write a {genre} story based on this prompt:
        {prompt}
        
        Length: {length_guide.get(length, length)}
        
        Requirements:
        - Engaging opening that hooks the reader
        - Well-developed characters
        - Clear plot progression
        - Vivid descriptions and dialogue
        - Satisfying conclusion
        - Appropriate tone for {genre} genre
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['story']},
                {"role": "user", "content": story_prompt}
            ],
            temperature=0.8
        )
        
        return response.choices[0].message.content
    
    def write_documentation(self, topic: str, audience: str = "developers", 
                          doc_type: str = "guide") -> str:
        """Generate technical documentation"""
        prompt = f"""
        Create {doc_type} documentation for: {topic}
        
        Target audience: {audience}
        Document type: {doc_type}
        
        Include:
        - Clear, concise explanations
        - Step-by-step instructions where appropriate
        - Code examples (if technical)
        - Best practices
        - Troubleshooting tips
        - Proper formatting with headers and sections
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['documentation']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def write_poetry(self, theme: str, style: str = "free verse", 
                    length: str = "medium") -> str:
        """Generate poetry"""
        prompt = f"""
        Write a {style} poem about: {theme}
        
        Length: {length}
        Style: {style}
        
        Create poetry that:
        - Captures the essence of the theme
        - Uses vivid imagery and metaphors
        - Has appropriate rhythm and flow
        - Evokes emotion
        - Demonstrates mastery of the chosen style
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['poetry']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    def brainstorm_ideas(self, topic: str, content_type: str = "general", 
                        count: int = 10) -> List[str]:
        """Generate creative ideas for writing"""
        prompt = f"""
        Brainstorm {count} creative ideas for {content_type} content about: {topic}
        
        Provide diverse, interesting, and unique angles or approaches.
        Each idea should be distinct and offer potential for development.
        Format as a numbered list with brief descriptions.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative ideation expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        
        content = response.choices[0].message.content
        # Extract ideas from the response
        lines = content.split('\n')
        ideas = [line.strip() for line in lines if line.strip() and any(char.isdigit() for char in line[:3])]
        
        return ideas
    
    def continue_writing(self, existing_text: str, direction: str = "") -> str:
        """Continue or expand existing writing"""
        prompt = f"""
        Continue this writing piece:
        
        {existing_text}
        
        Direction for continuation: {direction if direction else "Continue naturally"}
        
        Maintain the same style, tone, and voice while expanding the content meaningfully.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a skilled writer who can seamlessly continue existing work."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        
        return response.choices[0].message.content
    
    def edit_and_improve(self, text: str, improvement_focus: str = "general") -> str:
        """Edit and improve existing writing"""
        prompt = f"""
        Edit and improve this text with focus on: {improvement_focus}
        
        Original text:
        {text}
        
        Provide:
        1. Improved version
        2. Summary of changes made
        3. Suggestions for further improvement
        
        Focus areas: grammar, clarity, flow, engagement, style consistency
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional editor and writing coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def generate_marketing_copy(self, product: str, audience: str, 
                              copy_type: str = "general") -> str:
        """Generate marketing and promotional copy"""
        prompt = f"""
        Create {copy_type} marketing copy for: {product}
        
        Target audience: {audience}
        Copy type: {copy_type}
        
        Create compelling copy that:
        - Grabs attention immediately
        - Highlights key benefits
        - Addresses audience pain points
        - Includes clear call-to-action
        - Uses persuasive language
        - Matches the tone for {copy_type}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.writing_styles['marketing']},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        
        return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Creative Writing Assistant")
    parser.add_argument("--type", choices=["lyrics", "story", "docs", "poetry", "marketing", "brainstorm", "continue", "edit"], 
                       required=True, help="Type of writing to generate")
    parser.add_argument("--prompt", required=True, help="Writing prompt or topic")
    parser.add_argument("--genre", help="Genre or style")
    parser.add_argument("--mood", help="Mood or tone")
    parser.add_argument("--length", help="Length specification")
    parser.add_argument("--audience", help="Target audience")
    parser.add_argument("--file", help="File containing existing text to continue/edit")
    parser.add_argument("--output", help="Output file name")
    
    args = parser.parse_args()
    
    assistant = CreativeWritingAssistant()
    
    try:
        # Read existing text if file provided
        existing_text = ""
        if args.file:
            with open(args.file, 'r') as f:
                existing_text = f.read()
        
        result = ""
        
        if args.type == "lyrics":
            result = assistant.generate_lyrics(
                args.prompt, 
                args.genre or "general", 
                args.mood or "upbeat"
            )
        elif args.type == "story":
            result = assistant.write_story(
                args.prompt,
                args.length or "short",
                args.genre or "general"
            )
        elif args.type == "docs":
            result = assistant.write_documentation(
                args.prompt,
                args.audience or "general"
            )
        elif args.type == "poetry":
            result = assistant.write_poetry(
                args.prompt,
                args.genre or "free verse",
                args.length or "medium"
            )
        elif args.type == "marketing":
            result = assistant.generate_marketing_copy(
                args.prompt,
                args.audience or "general",
                args.genre or "general"
            )
        elif args.type == "brainstorm":
            ideas = assistant.brainstorm_ideas(args.prompt)
            result = "\n".join(ideas)
        elif args.type == "continue":
            if not existing_text:
                raise ValueError("--file required for continue mode")
            result = assistant.continue_writing(existing_text, args.prompt)
        elif args.type == "edit":
            if not existing_text:
                raise ValueError("--file required for edit mode")
            result = assistant.edit_and_improve(existing_text, args.prompt)
        
        print(f"\n{'='*60}")
        print(f"CREATIVE WRITING ASSISTANT - {args.type.upper()}")
        print(f"{'='*60}\n")
        print(result)
        print(f"\n{'='*60}")
        
        # Save result
        if args.output:
            output_file = args.output
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"{args.type}_{timestamp}.md"
        
        with open(output_file, 'w') as f:
            f.write(f"# {args.type.title()} - {args.prompt}\n\n")
            f.write(f"**Generated:** {datetime.now()}\n")
            if args.genre:
                f.write(f"**Genre:** {args.genre}\n")
            if args.mood:
                f.write(f"**Mood:** {args.mood}\n")
            f.write(f"\n---\n\n")
            f.write(result)
        
        print(f"Saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()