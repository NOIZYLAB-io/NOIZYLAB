#!/usr/bin/env python3
"""
FISH MUSIC INC - RELEASE AUTOMATION SYSTEM
Automate music release workflow from prep to distribution
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List

class ReleaseAutomation:
    """Automate complete music release workflow"""
    
    def __init__(self):
        self.base_path = Path('/Users/m2ultra/CB-01-FISHMUSICINC')
        self.releases_path = self.base_path / 'releases'
        self.templates_path = self.base_path / 'tools' / 'templates'
        
    def create_release_template(self, release_type: str = 'single') -> Dict:
        """Create release checklist template"""
        
        base_template = {
            'release_info': {
                'title': '',
                'artist': 'Fish Music Inc',
                'release_date': '',
                'type': release_type,
                'genres': [],
                'mood_tags': [],
                'bpm': 0,
                'key': '',
                'isrc': '',
                'upc': ''
            },
            'files': {
                'master_wav': {'path': '', 'status': 'pending'},
                'master_mp3_320': {'path': '', 'status': 'pending'},
                'master_mp3_256': {'path': '', 'status': 'pending'},
                'artwork_3000x3000': {'path': '', 'status': 'pending'},
                'artwork_1400x1400': {'path': '', 'status': 'pending'}
            },
            'metadata': {
                'title': '',
                'artist': 'Fish Music Inc',
                'album': '',
                'composer': '',
                'lyricist': '',
                'producer': 'Fish Music Inc',
                'year': datetime.now().year,
                'copyright': f'© {datetime.now().year} Fish Music Inc',
                'description': ''
            },
            'distribution': {
                'spotify': {'status': 'pending', 'url': ''},
                'apple_music': {'status': 'pending', 'url': ''},
                'youtube_music': {'status': 'pending', 'url': ''},
                'soundcloud': {'status': 'pending', 'url': ''},
                'bandcamp': {'status': 'pending', 'url': ''}
            },
            'marketing': {
                'announcement_date': '',
                'pre_save_campaign': False,
                'social_media_posts': [],
                'press_release': {'status': 'pending'},
                'playlist_pitching': {'status': 'pending'}
            },
            'timeline': self._generate_timeline(release_type)
        }
        
        return base_template
    
    def _generate_timeline(self, release_type: str) -> List[Dict]:
        """Generate release timeline"""
        today = datetime.now()
        
        if release_type == 'single':
            # Single release: 4 weeks
            timeline = [
                {'week': -4, 'date': (today + timedelta(weeks=-4)).strftime('%Y-%m-%d'), 'task': 'Master finalized', 'status': 'pending'},
                {'week': -3, 'date': (today + timedelta(weeks=-3)).strftime('%Y-%m-%d'), 'task': 'Artwork completed', 'status': 'pending'},
                {'week': -2, 'date': (today + timedelta(weeks=-2)).strftime('%Y-%m-%d'), 'task': 'Metadata & distribution setup', 'status': 'pending'},
                {'week': -1, 'date': (today + timedelta(weeks=-1)).strftime('%Y-%m-%d'), 'task': 'Pre-save campaign launch', 'status': 'pending'},
                {'week': 0, 'date': today.strftime('%Y-%m-%d'), 'task': 'RELEASE DAY!', 'status': 'pending'},
                {'week': 1, 'date': (today + timedelta(weeks=1)).strftime('%Y-%m-%d'), 'task': 'Playlist pitching', 'status': 'pending'},
                {'week': 2, 'date': (today + timedelta(weeks=2)).strftime('%Y-%m-%d'), 'task': 'Performance analysis', 'status': 'pending'}
            ]
        elif release_type == 'ep':
            # EP release: 8 weeks
            timeline = [
                {'week': -8, 'date': (today + timedelta(weeks=-8)).strftime('%Y-%m-%d'), 'task': 'All tracks mastered', 'status': 'pending'},
                {'week': -6, 'date': (today + timedelta(weeks=-6)).strftime('%Y-%m-%d'), 'task': 'Artwork & branding complete', 'status': 'pending'},
                {'week': -4, 'date': (today + timedelta(weeks=-4)).strftime('%Y-%m-%d'), 'task': 'Lead single release', 'status': 'pending'},
                {'week': -2, 'date': (today + timedelta(weeks=-2)).strftime('%Y-%m-%d'), 'task': 'Pre-save campaign', 'status': 'pending'},
                {'week': 0, 'date': today.strftime('%Y-%m-%d'), 'task': 'EP RELEASE DAY!', 'status': 'pending'},
                {'week': 2, 'date': (today + timedelta(weeks=2)).strftime('%Y-%m-%d'), 'task': 'Second single push', 'status': 'pending'},
                {'week': 4, 'date': (today + timedelta(weeks=4)).strftime('%Y-%m-%d'), 'task': 'Performance review', 'status': 'pending'}
            ]
        else:  # album
            # Album release: 12 weeks
            timeline = [
                {'week': -12, 'date': (today + timedelta(weeks=-12)).strftime('%Y-%m-%d'), 'task': 'Album mastered', 'status': 'pending'},
                {'week': -10, 'date': (today + timedelta(weeks=-10)).strftime('%Y-%m-%d'), 'task': 'Artwork & packaging', 'status': 'pending'},
                {'week': -8, 'date': (today + timedelta(weeks=-8)).strftime('%Y-%m-%d'), 'task': 'First single release', 'status': 'pending'},
                {'week': -6, 'date': (today + timedelta(weeks=-6)).strftime('%Y-%m-%d'), 'task': 'Second single release', 'status': 'pending'},
                {'week': -4, 'date': (today + timedelta(weeks=-4)).strftime('%Y-%m-%d'), 'task': 'Album pre-save campaign', 'status': 'pending'},
                {'week': -2, 'date': (today + timedelta(weeks=-2)).strftime('%Y-%m-%d'), 'task': 'Press release & media', 'status': 'pending'},
                {'week': 0, 'date': today.strftime('%Y-%m-%d'), 'task': 'ALBUM RELEASE DAY!', 'status': 'pending'},
                {'week': 4, 'date': (today + timedelta(weeks=4)).strftime('%Y-%m-%d'), 'task': 'Post-release analysis', 'status': 'pending'}
            ]
        
        return timeline
    
    def generate_social_media_posts(self, release_info: Dict) -> List[Dict]:
        """Generate social media post templates"""
        title = release_info['release_info']['title']
        release_date = release_info['release_info']['release_date']
        
        posts = [
            {
                'platform': 'all',
                'timing': '-2 weeks',
                'content': f'🎵 NEW MUSIC ALERT! 🎵\n\n"{title}" drops {release_date}!\n\nThis one\'s special... Pre-save link coming soon!\n\n#FishMusicInc #NewMusic #ComingSoon 🔥',
                'media': 'teaser_video'
            },
            {
                'platform': 'all',
                'timing': '-1 week',
                'content': f'ONE WEEK until "{title}" 🎸\n\nPre-save now and be the first to hear it!\n\nLink in bio 👆\n\n#FishMusicInc #NewRelease #{title.replace(" ", "")}',
                'media': 'artwork_reveal'
            },
            {
                'platform': 'all',
                'timing': '-1 day',
                'content': f'TOMORROW! 🔥\n\n"{title}" releases everywhere!\n\nSet your alarms... This is the one.\n\n#FishMusicInc #MusicRelease #CountdownMode 🚀',
                'media': 'countdown_graphic'
            },
            {
                'platform': 'all',
                'timing': 'release day',
                'content': f'IT\'S HERE! 🎉\n\n"{title}" is NOW LIVE on all platforms!\n\nStream it, share it, make it yours!\n\n🎧 Spotify: [LINK]\n🍎 Apple Music: [LINK]\n🎵 All platforms: [LINK]\n\n#FishMusicInc #OutNow #{title.replace(" ", "")} 🔥',
                'media': 'artwork_final'
            },
            {
                'platform': 'all',
                'timing': '+3 days',
                'content': f'THANK YOU! 🙏\n\nThe response to "{title}" has been incredible!\n\nIf you haven\'t heard it yet, check it out! Link in bio.\n\nWhat\'s your favorite moment? Drop a comment! 👇\n\n#FishMusicInc #{title.replace(" ", "")}',
                'media': 'listener_stats'
            }
        ]
        
        return posts
    
    def create_press_release_template(self, release_info: Dict) -> str:
        """Generate press release template"""
        title = release_info['release_info']['title']
        release_date = release_info['release_info']['release_date']
        release_type = release_info['release_info']['type'].upper()
        
        template = f"""
FOR IMMEDIATE RELEASE

Fish Music Inc Announces New {release_type}: "{title}"

[CITY, DATE] - Fish Music Inc, the innovative music production company with 40 years 
of creative excellence, today announced the release of "{title}", a new {release_type} 
available on all major streaming platforms starting {release_date}.

[ADD 2-3 PARAGRAPHS ABOUT THE RELEASE]
- What inspired this music
- The creative process
- What makes it unique
- Key themes or messages

"{title}" showcases Fish Music Inc's signature blend of [GENRE] with cutting-edge 
production techniques, featuring [KEY CHARACTERISTICS].

The {release_type} is now available on Spotify, Apple Music, YouTube Music, and all 
major streaming platforms.

About Fish Music Inc:
Fish Music Inc is a professional music production company specializing in original 
compositions, sound design, and music curation. With over 40 years of experience and 
major clients including FUEL, McDonald's, Microsoft, and Deadwood, Fish Music Inc 
continues to push the boundaries of creative innovation.

For more information:
Email: rp@fishmusicinc.com
Spotify: @fishmusicinc
Website: fishmusicinc.com

###

GORUNFREE! 🎸🔥
"""
        return template
    
    def save_release_plan(self, release: Dict, filename: str):
        """Save release plan to JSON file"""
        output_path = self.releases_path / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(release, f, indent=2)
        
        print(f"\n💾 Release plan saved to: {output_path}")
        return output_path
    
    def load_release_plan(self, filename: str) -> Dict:
        """Load release plan from JSON file"""
        file_path = self.releases_path / filename
        
        if not file_path.exists():
            print(f"❌ Release plan not found: {filename}")
            return {}
        
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def generate_distribution_checklist(self) -> List[str]:
        """Generate distribution platform checklist"""
        return [
            "☐ Spotify for Artists account verified",
            "☐ Apple Music for Artists access set up",
            "☐ YouTube Music channel claimed",
            "☐ SoundCloud Pro account active",
            "☐ Bandcamp artist page configured",
            "☐ DistroKid / TuneCore / CD Baby account ready",
            "☐ ISRC codes obtained",
            "☐ UPC code obtained",
            "☐ Splits and royalties configured",
            "☐ Publishing rights registered (SOCAN/ASCAP/BMI)",
            "☐ Copyright registration filed",
            "☐ Backup of all master files created"
        ]
    
    def save_release_plan(self, release: Dict, filename: str):
        """Save release plan to JSON file"""
        output_path = self.releases_path / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(release, f, indent=2)
        
        print(f"\n💾 Release plan saved to: {output_path}")
        return output_path
    
    def load_release_plan(self, filename: str) -> Dict:
        """Load release plan from JSON file"""
        file_path = self.releases_path / filename
        
        if not file_path.exists():
            print(f"❌ Release plan not found: {filename}")
            return {}
        
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def print_release_dashboard(self, release: Dict):
        """Print beautiful release dashboard"""
        print("\n" + "═" * 70)
        print("🎵 FISH MUSIC INC - RELEASE DASHBOARD")
        print("═" * 70)
        
        info = release['release_info']
        print(f"\n📀 Title: {info['title'] or '[Not Set]'}")
        print(f"   Artist: {info['artist']}")
        print(f"   Type: {info['type'].upper()}")
        print(f"   Release Date: {info['release_date'] or '[Not Set]'}")
        
        print(f"\n📁 FILES:")
        for file_name, file_info in release['files'].items():
            status_icon = "✅" if file_info['status'] == 'complete' else "⏳"
            print(f"   {status_icon} {file_name}: {file_info['status']}")
        
        print(f"\n📊 DISTRIBUTION:")
        for platform, platform_info in release['distribution'].items():
            status_icon = "✅" if platform_info['status'] == 'live' else "⏳"
            print(f"   {status_icon} {platform.replace('_', ' ').title()}: {platform_info['status']}")
        
        print(f"\n📅 TIMELINE:")
        for item in release['timeline'][:5]:
            print(f"   Week {item['week']:+3d} ({item['date']}): {item['task']}")
        
        print("\n" + "═" * 70)
        print("GORUNFREE! 🎸🔥")
        print("=" * 70)

def main():
    """Main execution"""
    print("\n🎵 FISH MUSIC INC - RELEASE AUTOMATION")
    print("=" * 70)
    
    automation = ReleaseAutomation()
    
    # Create single release template
    release = automation.create_release_template('single')
    release['release_info']['title'] = 'Example Track'
    release['release_info']['release_date'] = (datetime.now() + timedelta(weeks=4)).strftime('%Y-%m-%d')
    
    # Show dashboard
    automation.print_release_dashboard(release)
    
    # Generate social media posts
    print("\n📱 SOCIAL MEDIA POST TEMPLATES:")
    posts = automation.generate_social_media_posts(release)
    for i, post in enumerate(posts[:3], 1):
        print(f"\n   Post {i} ({post['timing']}):")
        print(f"   {post['content'][:100]}...")
    
    # Show checklist
    print("\n✅ DISTRIBUTION CHECKLIST:")
    checklist = automation.generate_distribution_checklist()
    for item in checklist[:6]:
        print(f"   {item}")
    
    print("\n" + "═" * 70)
    print("💡 Save your release plan:")
    print("   automation.save_release_plan('my_track_name.json')")
    print("═" * 70)

if __name__ == '__main__':
    main()

