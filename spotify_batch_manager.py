#!/usr/bin/env python3
"""
SPOTIFY BATCH MANAGER - FISH MUSIC INC
Manage multiple playlists at scale
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List, Dict
from spotify_config import SpotifyConfig
from spotify_hotrod import SpotifyHotRod

class SpotifyBatchManager:
    """Manage multiple playlists efficiently"""
    
    def __init__(self):
        if not SpotifyConfig.is_configured():
            print("⚠️  Configure Spotify credentials first!")
            return
        
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SpotifyConfig.CLIENT_ID,
            client_secret=SpotifyConfig.CLIENT_SECRET,
            redirect_uri=SpotifyConfig.REDIRECT_URI,
            scope=SpotifyConfig.SCOPE_STRING,
            cache_path=str(SpotifyConfig.CACHE_PATH)
        ))
        
        self.hotrod = SpotifyHotRod()
        self.username = SpotifyConfig.SPOTIFY_USERNAME
    
    def get_all_my_playlists(self) -> List[Dict]:
        """Get all user playlists"""
        playlists = []
        results = self.sp.current_user_playlists()
        
        while results:
            playlists.extend(results['items'])
            if results['next']:
                results = self.sp.next(results)
            else:
                break
        
        return playlists
    
    def batch_update_descriptions(self, auto_generate: bool = True):
        """Update descriptions for all playlists"""
        print("\n🔄 BATCH UPDATING PLAYLIST DESCRIPTIONS...")
        
        playlists = self.get_all_my_playlists()
        
        for playlist in playlists:
            print(f"\n📝 {playlist['name']}")
            
            if auto_generate:
                desc = self.hotrod.generate_professional_description(playlist['id'])
                print(f"   Generated: {desc[:100]}...")
                
                # Update playlist
                self.sp.playlist_change_details(
                    playlist['id'],
                    description=desc
                )
                print(f"   ✅ Updated!")
            else:
                print(f"   Current: {playlist['description']}")
        
        print(f"\n✅ Updated {len(playlists)} playlists!")
    
    def batch_analyze_all(self) -> Dict:
        """Analyze all playlists"""
        print("\n🔍 ANALYZING ALL PLAYLISTS...")
        
        playlists = self.get_all_my_playlists()
        analyses = {}
        
        for playlist in playlists:
            print(f"\n📊 Analyzing: {playlist['name']}")
            analysis = self.hotrod.analyze_playlist_deep(playlist['id'])
            analyses[playlist['id']] = analysis
        
        return analyses
    
    def create_playlist_collection(self, templates: List[Dict]):
        """Create multiple playlists from templates"""
        print("\n🎵 CREATING PLAYLIST COLLECTION...")
        
        for template in templates:
            print(f"\n   Creating: {template['name']}")
            
            playlist = self.sp.user_playlist_create(
                user=self.username,
                name=template['name'],
                public=template.get('public', True),
                description=template.get('description', '')
            )
            
            print(f"   ✅ Created: {playlist['external_urls']['spotify']}")
    
    def suggest_new_playlists(self) -> List[Dict]:
        """Suggest new playlists based on current collection"""
        suggestions = [
            {
                'name': 'Fish Music - Ambient Focus',
                'description': 'Atmospheric soundscapes for deep work and creativity • By Fish Music Inc 🎸',
                'criteria': {'energy': (0, 40), 'instrumentalness': (50, 100)},
                'public': True
            },
            {
                'name': 'Fish Music - Workout Energy',
                'description': 'High-energy tracks for maximum performance • 120-140 BPM • Fish Music Inc 🔥',
                'criteria': {'bpm': (120, 140), 'energy': (70, 100)},
                'public': True
            },
            {
                'name': 'Fish Music - Creative Flow',
                'description': 'Perfect background music for creative work • Fish Music Inc • GORUNFREE! 🎸',
                'criteria': {'energy': (30, 60), 'valence': (40, 70)},
                'public': True
            },
            {
                'name': 'Fish Music - Uplifting Vibes',
                'description': 'Positive energy to boost your mood • Curated by Fish Music Inc ✨',
                'criteria': {'valence': (70, 100), 'energy': (60, 90)},
                'public': True
            },
            {
                'name': 'Fish Music - Night Drive',
                'description': 'Smooth electronic vibes for late-night journeys • Fish Music Inc 🌙',
                'criteria': {'energy': (40, 70), 'danceability': (50, 80)},
                'public': True
            },
        ]
        
        return suggestions

# PROFESSIONAL PLAYLIST TEMPLATES FOR FISH MUSIC INC
FISH_MUSIC_PLAYLIST_TEMPLATES = [
    {
        'name': 'Fish Music - Original Tracks',
        'description': 'Original compositions by Fish Music Inc • GORUNFREE! 🎸🔥',
        'public': True
    },
    {
        'name': 'Fish Music - Client Showcase',
        'description': 'Professional work for FUEL, McDonald\'s, Microsoft & more • Fish Music Inc',
        'public': False  # Private until ready
    },
    {
        'name': 'Fish Music - Production Music',
        'description': 'Production-ready tracks for film, TV & media • Fish Music Inc',
        'public': True
    },
    {
        'name': 'Fish Music - Sound Design',
        'description': 'Innovative sound design and audio art • Fish Music Inc 🎵',
        'public': True
    },
]

def main():
    """Main execution"""
    print("\n🔥 SPOTIFY BATCH MANAGER - FISH MUSIC INC")
    print("=" * 70)
    
    manager = SpotifyBatchManager()
    
    # Show menu
    print("\nOptions:")
    print("  1. View all playlists")
    print("  2. Analyze all playlists")
    print("  3. Update all descriptions")
    print("  4. Suggest new playlists")
    print("  5. Create Fish Music playlist collection")
    
    choice = input("\nSelect option (1-5): ")
    
    if choice == '1':
        playlists = manager.get_all_my_playlists()
        print(f"\n📝 YOUR PLAYLISTS ({len(playlists)}):\n")
        for p in playlists:
            status = "🌍" if p['public'] else "🔒"
            print(f"   {status} {p['name']} ({p['tracks']['total']} tracks)")
            print(f"      {p['external_urls']['spotify']}")
    
    elif choice == '2':
        analyses = manager.batch_analyze_all()
        print(f"\n✅ Analyzed {len(analyses)} playlists!")
    
    elif choice == '3':
        manager.batch_update_descriptions(auto_generate=True)
    
    elif choice == '4':
        suggestions = manager.suggest_new_playlists()
        print(f"\n💡 SUGGESTED PLAYLISTS:\n")
        for s in suggestions:
            print(f"   • {s['name']}")
            print(f"     {s['description']}")
            print()
    
    elif choice == '5':
        manager.create_playlist_collection(FISH_MUSIC_PLAYLIST_TEMPLATES)

if __name__ == '__main__':
    main()

