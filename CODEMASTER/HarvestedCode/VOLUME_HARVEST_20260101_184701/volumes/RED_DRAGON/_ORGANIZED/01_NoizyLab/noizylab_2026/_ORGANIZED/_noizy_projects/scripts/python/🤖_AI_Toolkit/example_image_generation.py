# 🎨 Example: Generate Album Cover

import sys
import os
sys.path.append('/Users/rsp_ms/NoizyFish_Aquarium/🤖 AI_Toolkit/04_Image_Generation')
from image_generator import ImageGenerator

def example_album_cover():
    """Example: Generate an album cover for NoizyFish"""
    
    # Initialize generator
    generator = ImageGenerator()
    
    try:
        print("🎨 Generating album cover...")
        
        result = generator.generate_album_cover(
            album_title="Aquarium Dreams",
            artist_name="NoizyFish",
            genre="Electronic Ambient",
            mood="Mystical and Underwater",
            style="surreal digital art"
        )
        
        print(f"\n{'='*60}")
        print("ALBUM COVER GENERATED")
        print(f"{'='*60}")
        print(f"File: {result['filename']}")
        print(f"Album: {result['album_title']}")
        print(f"Artist: {result['artist_name']}")
        print(f"Genre: {result['genre']}")
        print(f"Style: {result['style']}")
        print(f"Location: {result['filepath']}")
        
        if 'revised_prompt' in result:
            print(f"\nAI Enhanced Prompt:")
            print(result['revised_prompt'])
        
        print(f"\n✅ Album cover saved successfully!")
        
    except Exception as e:
        print(f"Error: {e}")

def example_logo():
    """Example: Generate a logo for NoizyFish Studios"""
    
    generator = ImageGenerator()
    
    try:
        print("🏢 Generating logo...")
        
        result = generator.generate_logo(
            company_name="NoizyFish Studios",
            business_type="Music Production & Audio Engineering",
            style="modern minimalist",
            colors="ocean blues and teals"
        )
        
        print(f"\n{'='*60}")
        print("LOGO GENERATED")
        print(f"{'='*60}")
        print(f"File: {result['filename']}")
        print(f"Company: {result['company_name']}")
        print(f"Type: {result['business_type']}")
        print(f"Style: {result['style']}")
        print(f"Location: {result['filepath']}")
        
        print(f"\n✅ Logo saved successfully!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Choose an example:")
    print("1. Generate Album Cover")
    print("2. Generate Logo")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        example_album_cover()
    elif choice == "2":
        example_logo()
    else:
        print("Running both examples...")
        example_album_cover()
        print("\n" + "="*80 + "\n")
        example_logo()