#!/usr/bin/env python3
"""
Image Generation Tool - NoizyFish Artwork Edition
Generate artwork, album covers, and visual content using OpenAI DALL-E
"""

import os
import openai
from pathlib import Path
import argparse
from datetime import datetime
import json
import requests
from typing import List, Dict, Optional
import base64

class ImageGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Image Generator"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.output_dir = Path("generated_images")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_image(self, prompt: str, size: str = "1024x1024", 
                      quality: str = "standard", style: str = "vivid",
                      num_images: int = 1) -> List[Dict]:
        """Generate images using DALL-E"""
        print(f"Generating {num_images} image(s) with prompt: {prompt}")
        
        valid_sizes = ["1024x1024", "1792x1024", "1024x1792"]
        if size not in valid_sizes:
            raise ValueError(f"Size must be one of: {valid_sizes}")
        
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            style=style,
            n=1  # DALL-E 3 only supports n=1
        )
        
        results = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, image_data in enumerate(response.data):
            # Download and save image
            image_url = image_data.url
            response_img = requests.get(image_url)
            
            filename = f"generated_{timestamp}_{i+1}.png"
            filepath = self.output_dir / filename
            
            with open(filepath, 'wb') as f:
                f.write(response_img.content)
            
            result = {
                'prompt': prompt,
                'filename': filename,
                'filepath': str(filepath),
                'size': size,
                'quality': quality,
                'style': style,
                'revised_prompt': image_data.revised_prompt if hasattr(image_data, 'revised_prompt') else None,
                'url': image_url,
                'timestamp': timestamp
            }
            results.append(result)
            
            print(f"✅ Saved: {filename}")
        
        return results
    
    def generate_album_cover(self, album_title: str, artist_name: str, 
                           genre: str, mood: str, style: str = "artistic") -> Dict:
        """Generate album cover artwork"""
        prompt = f"""
        Create a {style} album cover for:
        Album: "{album_title}"
        Artist: {artist_name}
        Genre: {genre}
        Mood: {mood}
        
        Design requirements:
        - Professional album cover quality
        - Visually striking and memorable
        - Appropriate for {genre} music
        - Conveys {mood} emotion
        - High artistic value
        - Album title and artist name integrated naturally
        - Square format suitable for streaming platforms
        """
        
        result = self.generate_image(prompt, "1024x1024", "hd", "vivid")[0]
        
        # Save metadata
        metadata = {
            'type': 'album_cover',
            'album_title': album_title,
            'artist_name': artist_name,
            'genre': genre,
            'mood': mood,
            'style': style,
            **result
        }
        
        metadata_file = self.output_dir / f"album_cover_{result['timestamp']}_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
    
    def generate_logo(self, company_name: str, business_type: str, 
                     style: str = "modern", colors: str = "any") -> Dict:
        """Generate logo designs"""
        prompt = f"""
        Design a {style} logo for:
        Company: {company_name}
        Business type: {business_type}
        Color preference: {colors}
        
        Logo requirements:
        - Clean, professional design
        - Scalable and memorable
        - Appropriate for {business_type}
        - {style} aesthetic
        - Works in various sizes
        - Brand-appropriate colors
        - No background, transparent if possible
        """
        
        result = self.generate_image(prompt, "1024x1024", "hd")[0]
        
        metadata = {
            'type': 'logo',
            'company_name': company_name,
            'business_type': business_type,
            'style': style,
            'colors': colors,
            **result
        }
        
        metadata_file = self.output_dir / f"logo_{result['timestamp']}_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
    
    def generate_artwork_series(self, theme: str, style: str, count: int = 3) -> List[Dict]:
        """Generate a series of related artworks"""
        base_prompt = f"""
        Create artistic {style} artwork with theme: {theme}
        
        Requirements:
        - High artistic quality
        - Cohesive with {theme} theme
        - {style} artistic style
        - Unique and creative interpretation
        - Gallery-worthy composition
        """
        
        results = []
        
        for i in range(count):
            # Add variation to each piece
            variations = [
                "with dramatic lighting",
                "with vibrant colors",
                "with minimalist composition",
                "with abstract elements",
                "with realistic details",
                "with surreal touches"
            ]
            
            variation = variations[i % len(variations)]
            full_prompt = f"{base_prompt}\n- {variation}"
            
            result = self.generate_image(full_prompt, "1024x1024", "hd", "vivid")[0]
            
            metadata = {
                'type': 'artwork_series',
                'series_theme': theme,
                'series_style': style,
                'piece_number': i + 1,
                'total_pieces': count,
                'variation': variation,
                **result
            }
            
            results.append(metadata)
        
        # Save series metadata
        series_metadata = {
            'series_theme': theme,
            'series_style': style,
            'total_pieces': count,
            'created': datetime.now().isoformat(),
            'pieces': results
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        series_file = self.output_dir / f"artwork_series_{timestamp}_metadata.json"
        with open(series_file, 'w') as f:
            json.dump(series_metadata, f, indent=2)
        
        return results
    
    def enhance_prompt(self, basic_prompt: str, enhancement_type: str = "artistic") -> str:
        """Enhance a basic prompt using AI"""
        enhancement_prompts = {
            'artistic': "Enhance this image prompt to be more artistic and visually striking:",
            'professional': "Enhance this image prompt to be more professional and polished:",
            'creative': "Enhance this image prompt to be more creative and unique:",
            'detailed': "Enhance this image prompt with more specific details and descriptions:"
        }
        
        system_prompt = enhancement_prompts.get(enhancement_type, enhancement_prompts['artistic'])
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert at creating detailed, effective prompts for AI image generation."},
                {"role": "user", "content": f"{system_prompt}\n\nBasic prompt: {basic_prompt}"}
            ],
            temperature=0.6
        )
        
        return response.choices[0].message.content
    
    def analyze_generated_image(self, image_path: str) -> str:
        """Analyze a generated image and provide feedback"""
        # Note: This would require image analysis capabilities
        # For now, we'll provide a placeholder that analyzes based on metadata
        
        try:
            # Try to find associated metadata
            image_file = Path(image_path)
            metadata_file = image_file.parent / f"{image_file.stem}_metadata.json"
            
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                
                analysis_prompt = f"""
                Analyze this AI-generated image based on its creation metadata:
                
                Original prompt: {metadata.get('prompt', 'Unknown')}
                Revised prompt: {metadata.get('revised_prompt', 'Not available')}
                Style: {metadata.get('style', 'Unknown')}
                Quality: {metadata.get('quality', 'Unknown')}
                
                Provide analysis on:
                1. How well the image likely matches the prompt
                2. Artistic quality and composition
                3. Potential improvements for future generations
                4. Suggestions for variations or series
                """
                
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an art critic and AI image generation expert."},
                        {"role": "user", "content": analysis_prompt}
                    ],
                    temperature=0.4
                )
                
                return response.choices[0].message.content
            else:
                return "No metadata found for this image. Cannot provide detailed analysis."
                
        except Exception as e:
            return f"Error analyzing image: {e}"
    
    def create_variations(self, original_prompt: str, variation_count: int = 3) -> List[Dict]:
        """Create variations of an original prompt"""
        # First, get variation suggestions
        variation_prompt = f"""
        Create {variation_count} creative variations of this image prompt:
        "{original_prompt}"
        
        Each variation should:
        - Maintain the core concept
        - Add unique elements or perspectives
        - Explore different artistic styles or moods
        - Be distinct from the others
        
        Format as numbered list with just the prompt text.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative prompt designer."},
                {"role": "user", "content": variation_prompt}
            ],
            temperature=0.7
        )
        
        variations_text = response.choices[0].message.content
        
        # Extract individual variations
        lines = variations_text.split('\n')
        variations = []
        for line in lines:
            if line.strip() and any(char.isdigit() for char in line[:3]):
                # Remove numbering and clean up
                clean_prompt = line.split('.', 1)[1].strip() if '.' in line else line.strip()
                variations.append(clean_prompt)
        
        # Generate images for each variation
        results = []
        for i, var_prompt in enumerate(variations[:variation_count]):
            try:
                result = self.generate_image(var_prompt)[0]
                result['variation_number'] = i + 1
                result['original_prompt'] = original_prompt
                results.append(result)
            except Exception as e:
                print(f"Error generating variation {i+1}: {e}")
        
        return results

def main():
    parser = argparse.ArgumentParser(description="AI Image Generation Tool")
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--type", choices=["general", "album", "logo", "series", "variations"], 
                       default="general", help="Type of image to generate")
    parser.add_argument("--size", choices=["1024x1024", "1792x1024", "1024x1792"], 
                       default="1024x1024", help="Image size")
    parser.add_argument("--quality", choices=["standard", "hd"], default="standard", help="Image quality")
    parser.add_argument("--style", choices=["vivid", "natural"], default="vivid", help="Image style")
    parser.add_argument("--count", type=int, default=1, help="Number of images to generate")
    parser.add_argument("--enhance", action="store_true", help="Enhance the prompt with AI")
    parser.add_argument("--analyze", help="Analyze an existing image file")
    
    # Album cover specific
    parser.add_argument("--album", help="Album title (for album covers)")
    parser.add_argument("--artist", help="Artist name (for album covers)")
    parser.add_argument("--genre", help="Music genre (for album covers)")
    parser.add_argument("--mood", help="Mood/emotion (for album covers)")
    
    # Logo specific
    parser.add_argument("--company", help="Company name (for logos)")
    parser.add_argument("--business", help="Business type (for logos)")
    parser.add_argument("--colors", help="Color preferences (for logos)")
    
    args = parser.parse_args()
    
    generator = ImageGenerator()
    
    try:
        if args.analyze:
            # Analyze existing image
            analysis = generator.analyze_generated_image(args.analyze)
            print(f"\n{'='*60}")
            print("IMAGE ANALYSIS")
            print(f"{'='*60}")
            print(analysis)
            return
        
        prompt = args.prompt
        
        # Enhance prompt if requested
        if args.enhance:
            enhanced = generator.enhance_prompt(prompt)
            print(f"Enhanced prompt: {enhanced}")
            prompt = enhanced
        
        results = []
        
        if args.type == "album":
            if not all([args.album, args.artist, args.genre, args.mood]):
                print("Album covers require --album, --artist, --genre, and --mood")
                return
            
            result = generator.generate_album_cover(
                args.album, args.artist, args.genre, args.mood, prompt
            )
            results = [result]
            
        elif args.type == "logo":
            if not all([args.company, args.business]):
                print("Logos require --company and --business")
                return
            
            result = generator.generate_logo(
                args.company, args.business, prompt, args.colors or "any"
            )
            results = [result]
            
        elif args.type == "series":
            results = generator.generate_artwork_series(prompt, args.style, args.count)
            
        elif args.type == "variations":
            results = generator.create_variations(prompt, args.count)
            
        else:  # general
            for i in range(args.count):
                result = generator.generate_image(
                    prompt, args.size, args.quality, args.style
                )[0]
                results.append(result)
        
        print(f"\n{'='*60}")
        print(f"IMAGE GENERATION COMPLETE")
        print(f"{'='*60}")
        print(f"Generated {len(results)} image(s)")
        
        for result in results:
            print(f"✅ {result['filename']}")
            if 'revised_prompt' in result and result['revised_prompt']:
                print(f"   Revised: {result['revised_prompt'][:100]}...")
        
        print(f"\nImages saved to: {generator.output_dir}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()