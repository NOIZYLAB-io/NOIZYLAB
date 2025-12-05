#!/usr/bin/env python3
"""
SPOTIFY DISCOVERY ENGINE - FISH MUSIC INC
AI-powered music discovery and recommendation system
Find tracks based on audio features, mood, and style
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
sys.path.append('/Users/m2ultra/CB-01-FISHMUSICINC/api/integrations')
from spotify_config import SpotifyConfig
from typing import List, Dict, Optional, Tuple
import statistics

class SpotifyDiscoveryEngine:
    """Advanced music discovery and recommendation engine"""
    
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
    
    def discover_by_mood(self, mood: str, limit: int = 50) -> List[Dict]:
        """Discover tracks by mood"""
        print(f"\n🎵 DISCOVERING: {mood.upper()} MOOD")
        print("=" * 60)
        
        # Mood to audio feature mapping
        mood_profiles = {
            'happy': {'valence': (0.7, 1.0), 'energy': (0.6, 1.0)},
            'sad': {'valence': (0.0, 0.3), 'energy': (0.0, 0.4)},
            'energetic': {'energy': (0.8, 1.0), 'danceability': (0.7, 1.0)},
            'calm': {'energy': (0.0, 0.3), 'valence': (0.3, 0.7)},
            'angry': {'energy': (0.8, 1.0), 'valence': (0.0, 0.3)},
            'romantic': {'valence': (0.5, 0.8), 'energy': (0.3, 0.6), 'acousticness': (0.5, 1.0)},
            'motivated': {'energy': (0.7, 1.0), 'valence': (0.6, 1.0)},
            'relaxed': {'energy': (0.0, 0.4), 'acousticness': (0.4, 1.0)},
            'focused': {'energy': (0.3, 0.6), 'instrumentalness': (0.5, 1.0)},
            'party': {'danceability': (0.8, 1.0), 'energy': (0.8, 1.0)}
        }
        
        if mood not in mood_profiles:
            print(f"   ⚠️  Unknown mood. Available: {', '.join(mood_profiles.keys())}")
            return []
        
        profile = mood_profiles[mood]
        
        # Build search query
        genre_seeds = self._get_genre_seeds_for_mood(mood)
        
        tracks = []
        for genre in genre_seeds[:3]:  # Use top 3 genres
            try:
                # Get recommendations based on genre and mood
                results = self.sp.recommendations(
                    seed_genres=[genre],
                    limit=limit // 3,
                    target_valence=sum(profile.get('valence', (0.5, 0.5))) / 2 if 'valence' in profile else None,
                    target_energy=sum(profile.get('energy', (0.5, 0.5))) / 2 if 'energy' in profile else None,
                    target_danceability=sum(profile.get('danceability', (0.5, 0.5))) / 2 if 'danceability' in profile else None,
                    target_acousticness=sum(profile.get('acousticness', (0.5, 0.5))) / 2 if 'acousticness' in profile else None,
                    target_instrumentalness=sum(profile.get('instrumentalness', (0.5, 0.5))) / 2 if 'instrumentalness' in profile else None
                )
                
                for track in results['tracks']:
                    tracks.append({
                        'name': track['name'],
                        'artist': ', '.join([a['name'] for a in track['artists']]),
                        'album': track['album']['name'],
                        'uri': track['uri'],
                        'url': track['external_urls']['spotify'],
                        'popularity': track['popularity']
                    })
            except Exception as e:
                print(f"   ⚠️  Error with genre {genre}: {e}")
        
        print(f"\n✅ Found {len(tracks)} {mood} tracks!")
        return tracks
    
    def _get_genre_seeds_for_mood(self, mood: str) -> List[str]:
        """Get appropriate genre seeds for mood"""
        mood_genres = {
            'happy': ['pop', 'indie-pop', 'dance'],
            'sad': ['indie', 'singer-songwriter', 'acoustic'],
            'energetic': ['electronic', 'dance', 'edm'],
            'calm': ['ambient', 'chill', 'classical'],
            'angry': ['metal', 'rock', 'punk'],
            'romantic': ['r-n-b', 'soul', 'acoustic'],
            'motivated': ['electronic', 'hip-hop', 'rock'],
            'relaxed': ['ambient', 'jazz', 'chill'],
            'focused': ['ambient', 'classical', 'electronic'],
            'party': ['dance', 'electronic', 'hip-hop']
        }
        return mood_genres.get(mood, ['pop', 'indie', 'electronic'])
    
    def discover_similar_to_track(self, track_url: str, limit: int = 30) -> List[Dict]:
        """Find tracks similar to a given track"""
        print(f"\n🔍 FINDING SIMILAR TRACKS...")
        
        # Extract track ID
        track_id = track_url.split('/')[-1].split('?')[0]
        
        # Get track info
        track = self.sp.track(track_id)
        print(f"   Seed Track: {track['name']} by {track['artists'][0]['name']}")
        
        # Get audio features
        features = self.sp.audio_features(track_id)[0]
        
        # Get recommendations based on audio features
        artist_id = track['artists'][0]['id']
        
        try:
            results = self.sp.recommendations(
                seed_tracks=[track_id],
                limit=limit,
                target_tempo=features['tempo'],
                target_energy=features['energy'],
                target_danceability=features['danceability'],
                target_valence=features['valence']
            )
            
            tracks = []
            for t in results['tracks']:
                tracks.append({
                    'name': t['name'],
                    'artist': ', '.join([a['name'] for a in t['artists']]),
                    'album': t['album']['name'],
                    'uri': t['uri'],
                    'url': t['external_urls']['spotify'],
                    'popularity': t['popularity']
                })
            
            print(f"\n✅ Found {len(tracks)} similar tracks!")
            return tracks
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return []
    
    def discover_by_bpm_range(self, min_bpm: int, max_bpm: int, genres: List[str] = None, limit: int = 50) -> List[Dict]:
        """Discover tracks in specific BPM range"""
        print(f"\n🎵 DISCOVERING: {min_bpm}-{max_bpm} BPM")
        if genres:
            print(f"   Genres: {', '.join(genres)}")
        print("=" * 60)
        
        if not genres:
            genres = ['dance', 'electronic', 'pop']
        
        tracks = []
        target_tempo = (min_bpm + max_bpm) / 2
        
        for genre in genres[:3]:
            try:
                results = self.sp.recommendations(
                    seed_genres=[genre],
                    limit=limit // 3,
                    target_tempo=target_tempo,
                    min_tempo=min_bpm,
                    max_tempo=max_bpm
                )
                
                for track in results['tracks']:
                    # Verify BPM
                    features = self.sp.audio_features(track['id'])[0]
                    bpm = round(features['tempo'])
                    
                    if min_bpm <= bpm <= max_bpm:
                        tracks.append({
                            'name': track['name'],
                            'artist': ', '.join([a['name'] for a in track['artists']]),
                            'bpm': bpm,
                            'uri': track['uri'],
                            'url': track['external_urls']['spotify'],
                            'energy': round(features['energy'] * 100),
                            'danceability': round(features['danceability'] * 100)
                        })
            except Exception as e:
                print(f"   ⚠️  Error with genre {genre}: {e}")
        
        # Sort by BPM
        tracks.sort(key=lambda x: x['bpm'])
        
        print(f"\n✅ Found {len(tracks)} tracks in {min_bpm}-{max_bpm} BPM range!")
        return tracks
    
    def discover_workout_playlist(self, workout_type: str = 'cardio', duration_min: int = 45) -> List[Dict]:
        """Create workout playlist with progressive energy"""
        print(f"\n🏋️ CREATING {workout_type.upper()} WORKOUT PLAYLIST ({duration_min} min)")
        print("=" * 60)
        
        workout_profiles = {
            'cardio': {
                'warmup': {'bpm': (100, 120), 'energy': (0.5, 0.7)},
                'peak': {'bpm': (130, 150), 'energy': (0.8, 1.0)},
                'cooldown': {'bpm': (90, 110), 'energy': (0.3, 0.5)}
            },
            'strength': {
                'warmup': {'bpm': (110, 125), 'energy': (0.6, 0.8)},
                'peak': {'bpm': (120, 140), 'energy': (0.7, 0.9)},
                'cooldown': {'bpm': (95, 115), 'energy': (0.4, 0.6)}
            },
            'yoga': {
                'warmup': {'bpm': (80, 95), 'energy': (0.3, 0.5)},
                'peak': {'bpm': (90, 110), 'energy': (0.4, 0.6)},
                'cooldown': {'bpm': (70, 85), 'energy': (0.2, 0.4)}
            },
            'hiit': {
                'warmup': {'bpm': (120, 135), 'energy': (0.7, 0.8)},
                'peak': {'bpm': (140, 160), 'energy': (0.9, 1.0)},
                'cooldown': {'bpm': (100, 115), 'energy': (0.4, 0.6)}
            }
        }
        
        if workout_type not in workout_profiles:
            print(f"   ⚠️  Unknown type. Available: {', '.join(workout_profiles.keys())}")
            return []
        
        profile = workout_profiles[workout_type]
        
        # Workout phases
        warmup_min = duration_min // 5  # 20% warmup
        peak_min = duration_min * 3 // 5  # 60% peak
        cooldown_min = duration_min - warmup_min - peak_min  # 20% cooldown
        
        playlist = []
        
        # Warmup phase
        print(f"\n🔥 Phase 1: WARMUP ({warmup_min} min)")
        warmup = self._get_workout_phase_tracks(
            profile['warmup'], 
            warmup_min,
            ['electronic', 'pop', 'dance']
        )
        playlist.extend(warmup)
        
        # Peak phase
        print(f"🔥 Phase 2: PEAK INTENSITY ({peak_min} min)")
        peak = self._get_workout_phase_tracks(
            profile['peak'],
            peak_min,
            ['electronic', 'dance', 'edm']
        )
        playlist.extend(peak)
        
        # Cooldown phase
        print(f"🔥 Phase 3: COOLDOWN ({cooldown_min} min)")
        cooldown = self._get_workout_phase_tracks(
            profile['cooldown'],
            cooldown_min,
            ['chill', 'indie', 'electronic']
        )
        playlist.extend(cooldown)
        
        print(f"\n✅ Created {len(playlist)}-track workout playlist ({duration_min} min)!")
        return playlist
    
    def _get_workout_phase_tracks(self, phase_profile: Dict, duration_min: int, genres: List[str]) -> List[Dict]:
        """Get tracks for workout phase"""
        tracks_needed = max(duration_min // 3, 5)  # ~3 min per track
        
        bpm_range = phase_profile['bpm']
        energy_range = phase_profile['energy']
        
        target_tempo = sum(bpm_range) / 2
        target_energy = sum(energy_range) / 2
        
        tracks = []
        for genre in genres[:2]:
            try:
                results = self.sp.recommendations(
                    seed_genres=[genre],
                    limit=tracks_needed // 2,
                    target_tempo=target_tempo,
                    target_energy=target_energy,
                    min_tempo=bpm_range[0],
                    max_tempo=bpm_range[1]
                )
                
                for track in results['tracks']:
                    features = self.sp.audio_features(track['id'])[0]
                    tracks.append({
                        'name': track['name'],
                        'artist': ', '.join([a['name'] for a in track['artists']]),
                        'bpm': round(features['tempo']),
                        'energy': round(features['energy'] * 100),
                        'uri': track['uri'],
                        'url': track['external_urls']['spotify']
                    })
            except:
                pass
        
        return tracks[:tracks_needed]
    
    def create_discovery_playlist(self, name: str, tracks: List[Dict], description: str = None) -> Optional[str]:
        """Create playlist from discovered tracks"""
        print(f"\n📝 CREATING PLAYLIST: {name}")
        
        if not description:
            description = f"Discovered by Fish Music Inc • {len(tracks)} tracks • GORUNFREE! 🎸🔥"
        
        try:
            user = self.sp.current_user()
            playlist = self.sp.user_playlist_create(
                user=user['id'],
                name=name,
                public=True,
                description=description
            )
            
            # Add tracks
            track_uris = [t['uri'] for t in tracks]
            for i in range(0, len(track_uris), 100):
                batch = track_uris[i:i+100]
                self.sp.playlist_add_items(playlist['id'], batch)
            
            print(f"✅ Created playlist with {len(tracks)} tracks!")
            print(f"   URL: {playlist['external_urls']['spotify']}")
            
            return playlist['id']
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

def main():
    """Main execution"""
    import sys
    
    print("\n🎵 SPOTIFY DISCOVERY ENGINE - FISH MUSIC INC")
    print("=" * 70)
    
    engine = SpotifyDiscoveryEngine()
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python3 spotify_discovery_engine.py mood <mood_name>")
        print("  python3 spotify_discovery_engine.py bpm <min> <max>")
        print("  python3 spotify_discovery_engine.py similar <track_url>")
        print("  python3 spotify_discovery_engine.py workout <type> <duration_min>")
        print("\nMoods: happy, sad, energetic, calm, angry, romantic, motivated, relaxed, focused, party")
        print("Workout types: cardio, strength, yoga, hiit")
        return
    
    command = sys.argv[1]
    
    if command == 'mood' and len(sys.argv) > 2:
        mood = sys.argv[2]
        tracks = engine.discover_by_mood(mood, limit=50)
        
        if tracks:
            create = input("\nCreate playlist? (yes/no): ")
            if create.lower() == 'yes':
                name = f"Fish Music - {mood.capitalize()} Vibes"
                engine.create_discovery_playlist(name, tracks)
    
    elif command == 'bpm' and len(sys.argv) > 3:
        min_bpm = int(sys.argv[2])
        max_bpm = int(sys.argv[3])
        tracks = engine.discover_by_bpm_range(min_bpm, max_bpm, limit=50)
        
        if tracks:
            for i, t in enumerate(tracks[:10], 1):
                print(f"{i}. {t['bpm']} BPM - {t['name']} by {t['artist']}")
    
    elif command == 'similar' and len(sys.argv) > 2:
        track_url = sys.argv[2]
        tracks = engine.discover_similar_to_track(track_url, limit=30)
        
        if tracks:
            for i, t in enumerate(tracks[:10], 1):
                print(f"{i}. {t['name']} by {t['artist']}")
    
    elif command == 'workout' and len(sys.argv) > 3:
        workout_type = sys.argv[2]
        duration = int(sys.argv[3])
        tracks = engine.discover_workout_playlist(workout_type, duration)
        
        if tracks:
            create = input("\nCreate workout playlist? (yes/no): ")
            if create.lower() == 'yes':
                name = f"Fish Music - {workout_type.capitalize()} Workout ({duration}min)"
                desc = f"{workout_type.capitalize()} workout with progressive energy • {duration} minutes • Fish Music Inc 🔥"
                engine.create_discovery_playlist(name, tracks, desc)

if __name__ == '__main__':
    main()

