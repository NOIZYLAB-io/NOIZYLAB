#!/usr/bin/env python3
"""
SPOTIFY MANAGER - FISH MUSIC INC
Complete Spotify integration and playlist management
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from spotify_config import SpotifyConfig, BRAND

class FishMusicSpotify:
    """Fish Music Inc Spotify Manager"""
    
    def __init__(self):
        """Initialize Spotify connection"""
        if not SpotifyConfig.is_configured():
            print("⚠️  Spotify credentials not configured!")
            print(SpotifyConfig.setup_instructions())
            return
        
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SpotifyConfig.CLIENT_ID,
            client_secret=SpotifyConfig.CLIENT_SECRET,
            redirect_uri=SpotifyConfig.REDIRECT_URI,
            scope=SpotifyConfig.SCOPE_STRING,
            cache_path=str(SpotifyConfig.CACHE_PATH)
        ))
        
        self.username = SpotifyConfig.SPOTIFY_USERNAME
        self.profile_url = SpotifyConfig.SPOTIFY_PROFILE_URL
        
    def get_profile(self) -> Dict:
        """Get user profile information"""
        try:
            profile = self.sp.current_user()
            return {
                'id': profile['id'],
                'display_name': profile.get('display_name', 'N/A'),
                'email': profile.get('email', 'N/A'),
                'followers': profile['followers']['total'],
                'url': profile['external_urls']['spotify'],
                'country': profile.get('country', 'N/A')
            }
        except Exception as e:
            print(f"❌ Error getting profile: {e}")
            return {}
    
    def get_all_playlists(self) -> List[Dict]:
        """Get all user playlists"""
        try:
            playlists = []
            results = self.sp.current_user_playlists()
            
            while results:
                for playlist in results['items']:
                    playlists.append({
                        'id': playlist['id'],
                        'name': playlist['name'],
                        'tracks': playlist['tracks']['total'],
                        'public': playlist['public'],
                        'collaborative': playlist['collaborative'],
                        'url': playlist['external_urls']['spotify'],
                        'description': playlist.get('description', '')
                    })
                
                # Get next page
                if results['next']:
                    results = self.sp.next(results)
                else:
                    results = None
            
            return playlists
        except Exception as e:
            print(f"❌ Error getting playlists: {e}")
            return []
    
    def get_playlist_tracks(self, playlist_id: str) -> List[Dict]:
        """Get all tracks from a playlist"""
        try:
            tracks = []
            results = self.sp.playlist_tracks(playlist_id)
            
            while results:
                for item in results['items']:
                    track = item['track']
                    if track:  # Sometimes tracks can be None
                        tracks.append({
                            'name': track['name'],
                            'artist': ', '.join([artist['name'] for artist in track['artists']]),
                            'album': track['album']['name'],
                            'duration_ms': track['duration_ms'],
                            'duration_min': round(track['duration_ms'] / 60000, 2),
                            'url': track['external_urls']['spotify'],
                            'uri': track['uri'],
                            'added_at': item['added_at']
                        })
                
                # Get next page
                if results['next']:
                    results = self.sp.next(results)
                else:
                    results = None
            
            return tracks
        except Exception as e:
            print(f"❌ Error getting playlist tracks: {e}")
            return []
    
    def analyze_track_features(self, track_uri: str) -> Dict:
        """Get audio features for a track (BPM, energy, etc.)"""
        try:
            track_id = track_uri.split(':')[-1]
            features = self.sp.audio_features(track_id)[0]
            
            if features:
                return {
                    'bpm': round(features['tempo']),
                    'energy': round(features['energy'] * 100),
                    'danceability': round(features['danceability'] * 100),
                    'valence': round(features['valence'] * 100),  # Positivity
                    'key': features['key'],
                    'mode': 'Major' if features['mode'] == 1 else 'Minor',
                    'time_signature': features['time_signature'],
                    'acousticness': round(features['acousticness'] * 100),
                    'instrumentalness': round(features['instrumentalness'] * 100),
                    'liveness': round(features['liveness'] * 100),
                    'speechiness': round(features['speechiness'] * 100),
                    'loudness': round(features['loudness'], 1)
                }
            return {}
        except Exception as e:
            print(f"⚠️  Could not analyze track: {e}")
            return {}
    
    def analyze_playlist_bpm(self, playlist_id: str) -> Dict:
        """Analyze BPM distribution in a playlist"""
        try:
            tracks = self.get_playlist_tracks(playlist_id)
            
            bpm_data = []
            for track in tracks:
                features = self.analyze_track_features(track['uri'])
                if features:
                    bpm_data.append({
                        'track': track['name'],
                        'artist': track['artist'],
                        'bpm': features['bpm'],
                        'energy': features['energy'],
                        'danceability': features['danceability']
                    })
            
            # Sort by BPM
            bpm_data.sort(key=lambda x: x['bpm'])
            
            # Calculate stats
            bpms = [t['bpm'] for t in bpm_data]
            avg_bpm = sum(bpms) / len(bpms) if bpms else 0
            min_bpm = min(bpms) if bpms else 0
            max_bpm = max(bpms) if bpms else 0
            
            return {
                'tracks': bpm_data,
                'stats': {
                    'total_tracks': len(bpm_data),
                    'avg_bpm': round(avg_bpm),
                    'min_bpm': min_bpm,
                    'max_bpm': max_bpm,
                    'bpm_range': max_bpm - min_bpm
                }
            }
        except Exception as e:
            print(f"❌ Error analyzing playlist: {e}")
            return {}
    
    def create_playlist(self, name: str, description: str = '', public: bool = True) -> Optional[str]:
        """Create a new playlist"""
        try:
            playlist = self.sp.user_playlist_create(
                user=self.username,
                name=name,
                public=public,
                description=description
            )
            print(f"✅ Created playlist: {name}")
            print(f"   URL: {playlist['external_urls']['spotify']}")
            return playlist['id']
        except Exception as e:
            print(f"❌ Error creating playlist: {e}")
            return None
    
    def add_tracks_to_playlist(self, playlist_id: str, track_uris: List[str]) -> bool:
        """Add tracks to a playlist"""
        try:
            # Spotify allows max 100 tracks per request
            for i in range(0, len(track_uris), 100):
                batch = track_uris[i:i+100]
                self.sp.playlist_add_items(playlist_id, batch)
            
            print(f"✅ Added {len(track_uris)} track(s) to playlist")
            return True
        except Exception as e:
            print(f"❌ Error adding tracks: {e}")
            return False
    
    def search_tracks(self, query: str, limit: int = 10) -> List[Dict]:
        """Search for tracks"""
        try:
            results = self.sp.search(q=query, type='track', limit=limit)
            
            tracks = []
            for track in results['tracks']['items']:
                tracks.append({
                    'name': track['name'],
                    'artist': ', '.join([artist['name'] for artist in track['artists']]),
                    'album': track['album']['name'],
                    'url': track['external_urls']['spotify'],
                    'uri': track['uri']
                })
            
            return tracks
        except Exception as e:
            print(f"❌ Error searching: {e}")
            return []
    
    def print_profile_summary(self):
        """Print Fish Music Inc Spotify profile summary"""
        print("\n🎵 FISH MUSIC INC - SPOTIFY PROFILE")
        print("=" * 60)
        
        profile = self.get_profile()
        if profile:
            print(f"\n👤 Profile:")
            print(f"   Username: {profile['id']}")
            print(f"   Display Name: {profile['display_name']}")
            print(f"   Followers: {profile['followers']:,}")
            print(f"   URL: {profile['url']}")
        
        playlists = self.get_all_playlists()
        print(f"\n📝 Playlists: {len(playlists)}")
        for playlist in playlists:
            status = "🌍 PUBLIC" if playlist['public'] else "🔒 PRIVATE"
            print(f"   {status} {playlist['name']} ({playlist['tracks']} tracks)")
            if playlist['description']:
                print(f"      Description: {playlist['description']}")
            print(f"      URL: {playlist['url']}")
        
        print("\n" + "=" * 60)
        print("GORUNFREE! 🎸🔥\n")

def main():
    """Main execution"""
    import sys
    
    print("\n🎵 FISH MUSIC INC - SPOTIFY MANAGER")
    print("=" * 60)
    
    manager = FishMusicSpotify()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == '--setup':
            print(SpotifyConfig.setup_instructions())
        elif command == '--profile':
            manager.print_profile_summary()
        elif command == '--playlists':
            playlists = manager.get_all_playlists()
            for p in playlists:
                print(f"\n📝 {p['name']} ({p['tracks']} tracks)")
                print(f"   {p['url']}")
        else:
            print(f"Unknown command: {command}")
    else:
        # Default: show profile summary
        manager.print_profile_summary()

if __name__ == '__main__':
    main()

