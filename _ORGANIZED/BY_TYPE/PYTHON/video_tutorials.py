#!/usr/bin/env python3
from pathlib import Path
import json
import webbrowser

#!/usr/bin/env python3
"""
Video Tutorials Integration
Links to repair tutorials, step-by-step videos
"""


class VideoTutorials:
    """Video tutorial integration"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.tutorials_db = self.base_dir / "tutorials_database"
        self.tutorials_db.mkdir(exist_ok=True)

    def find_tutorial(self, repair_type, device_model=None):
        """Find video tutorial for repair"""
        print("\n" + "="*80)
        print("🎥 VIDEO TUTORIAL FINDER")
        print("="*80)

        print(f"\n🔍 Searching for: {repair_type}")
        if device_model:
            print(f"📱 Device: {device_model}")

        print("\n📺 Video Sources:")
        print("  1. YouTube (Comprehensive tutorials)")
        print("  2. iFixit (Step-by-step guides)")
        print("  3. Manufacturer Videos")
        print("  4. Professional Repair Channels")

        # Generate search URL
        search_query = f"{repair_type} {device_model or ''} tutorial"
        youtube_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        ifixit_url = f"https://www.ifixit.com/Search?query={search_query.replace(' ', '+')}"

        print("\n🔗 Quick Links:")
        print(f"  • YouTube: {youtube_url}")
        print(f"  • iFixit: {ifixit_url}")

        open_video = input("\nOpen YouTube search? (y/n): ").strip().lower()
        if open_video == 'y':
            webbrowser.open(youtube_url)

    def create_tutorial_database(self):
        """Create tutorial database"""
        tutorials = {
            "screen_replacement": {
                "iphone": "https://www.youtube.com/results?search_query=iphone+screen+replacement",
                "ipad": "https://www.youtube.com/results?search_query=ipad+screen+replacement",
                "macbook": "https://www.youtube.com/results?search_query=macbook+screen+replacement",
                "laptop": "https://www.youtube.com/results?search_query=laptop+screen+replacement"
            },
            "battery_replacement": {
                "iphone": "https://www.youtube.com/results?search_query=iphone+battery+replacement",
                "laptop": "https://www.youtube.com/results?search_query=laptop+battery+replacement"
            },
            "logic_board": {
                "macbook": "https://www.youtube.com/results?search_query=macbook+logic+board+repair",
                "iphone": "https://www.youtube.com/results?search_query=iphone+logic+board+repair"
            }
        }

        tutorial_file = self.tutorials_db / "tutorial_links.json"
        with open(tutorial_file, 'w') as f:
            json.dump(tutorials, f, indent=2)

        print("✅ Tutorial database created")

if __name__ == "__main__":
    try:
        videos = VideoTutorials()
            videos.create_tutorial_database()


    except Exception as e:
        print(f"Error: {e}")
