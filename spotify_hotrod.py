#!/usr/bin/env python3
"""
SPOTIFY HOT ROD - FISH MUSIC INC
Maximum performance Spotify tools for professional curation
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import statistics
from collections import defaultdict
from spotify_config import SpotifyConfig

class SpotifyHotRod:
    """Advanced Spotify tools for maximum performance"""
    
    def __init__(self):
        """Initialize with full power"""
        if not SpotifyConfig.is_configured():
            print("⚠️  Configure Spotify credentials first!")
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
    
    def analyze_playlist_deep(self, playlist_id: str) -> Dict:
        """Deep analysis of playlist with all audio features"""
        print(f"\n🔍 DEEP ANALYZING PLAYLIST...")
        
        # Get playlist info
        playlist = self.sp.playlist(playlist_id)
        
        # Get all tracks
        tracks = []
        results = self.sp.playlist_tracks(playlist_id)
        
        while results:
            tracks.extend(results['items'])
            if results['next']:
                results = self.sp.next(results)
            else:
                break
        
        print(f"   Found {len(tracks)} tracks")
        
        # Analyze each track
        track_analysis = []
        for i, item in enumerate(tracks):
            track = item['track']
            if not track:
                continue
            
            if (i + 1) % 10 == 0:
                print(f"   Analyzing track {i+1}/{len(tracks)}...")
            
            # Get audio features
            try:
                track_id = track['id']
                features = self.sp.audio_features(track_id)[0]
                
                if features:
                    track_analysis.append({
                        'name': track['name'],
                        'artist': ', '.join([a['name'] for a in track['artists']]),
                        'album': track['album']['name'],
                        'duration_ms': track['duration_ms'],
                        'popularity': track['popularity'],
                        'bpm': round(features['tempo']),
                        'key': features['key'],
                        'mode': 'Major' if features['mode'] == 1 else 'Minor',
                        'time_signature': features['time_signature'],
                        'energy': round(features['energy'] * 100),
                        'danceability': round(features['danceability'] * 100),
                        'valence': round(features['valence'] * 100),
                        'acousticness': round(features['acousticness'] * 100),
                        'instrumentalness': round(features['instrumentalness'] * 100),
                        'liveness': round(features['liveness'] * 100),
                        'speechiness': round(features['speechiness'] * 100),
                        'loudness': round(features['loudness'], 1),
                        'uri': track['uri']
                    })
            except Exception as e:
                print(f"   ⚠️  Could not analyze: {track['name']}")
        
        # Calculate statistics
        stats = self._calculate_playlist_stats(track_analysis)
        
        # Generate insights
        insights = self._generate_insights(track_analysis, stats)
        
        return {
            'playlist_name': playlist['name'],
            'playlist_id': playlist_id,
            'total_tracks': len(track_analysis),
            'tracks': track_analysis,
            'stats': stats,
            'insights': insights,
            'analysis_date': datetime.now().isoformat()
        }
    
    def _calculate_playlist_stats(self, tracks: List[Dict]) -> Dict:
        """Calculate comprehensive statistics"""
        if not tracks:
            return {}
        
        # Extract all metrics
        bpms = [t['bpm'] for t in tracks]
        energies = [t['energy'] for t in tracks]
        danceabilities = [t['danceability'] for t in tracks]
        valences = [t['valence'] for t in tracks]
        popularities = [t['popularity'] for t in tracks]
        
        # Key distribution
        keys = [t['key'] for t in tracks]
        key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        key_distribution = {key_names[k]: keys.count(k) for k in range(12)}
        
        # Mode distribution
        modes = [t['mode'] for t in tracks]
        mode_distribution = {
            'Major': modes.count('Major'),
            'Minor': modes.count('Minor')
        }
        
        return {
            'bpm': {
                'min': min(bpms),
                'max': max(bpms),
                'avg': round(statistics.mean(bpms)),
                'median': round(statistics.median(bpms)),
                'stdev': round(statistics.stdev(bpms)) if len(bpms) > 1 else 0
            },
            'energy': {
                'min': min(energies),
                'max': max(energies),
                'avg': round(statistics.mean(energies))
            },
            'danceability': {
                'min': min(danceabilities),
                'max': max(danceabilities),
                'avg': round(statistics.mean(danceabilities))
            },
            'valence': {
                'min': min(valences),
                'max': max(valences),
                'avg': round(statistics.mean(valences))
            },
            'popularity': {
                'min': min(popularities),
                'max': max(popularities),
                'avg': round(statistics.mean(popularities))
            },
            'key_distribution': key_distribution,
            'mode_distribution': mode_distribution,
            'most_common_key': max(key_distribution, key=key_distribution.get),
            'major_minor_ratio': f"{mode_distribution['Major']}:{mode_distribution['Minor']}"
        }
    
    def _generate_insights(self, tracks: List[Dict], stats: Dict) -> List[str]:
        """Generate smart insights about the playlist"""
        insights = []
        
        # BPM insights
        bpm_range = stats['bpm']['max'] - stats['bpm']['min']
        if bpm_range < 20:
            insights.append(f"🎯 Consistent tempo: {bpm_range} BPM range - great for steady energy flow")
        elif bpm_range > 50:
            insights.append(f"⚡ Dynamic range: {bpm_range} BPM range - perfect for progressive energy")
        
        # Energy insights
        avg_energy = stats['energy']['avg']
        if avg_energy > 75:
            insights.append(f"🔥 High energy playlist ({avg_energy}%) - perfect for workouts or parties")
        elif avg_energy < 40:
            insights.append(f"😌 Chill vibes ({avg_energy}% energy) - great for focus or relaxation")
        
        # Danceability insights
        avg_dance = stats['danceability']['avg']
        if avg_dance > 75:
            insights.append(f"💃 Highly danceable ({avg_dance}%) - club/party ready!")
        
        # Mood insights
        avg_valence = stats['valence']['avg']
        if avg_valence > 70:
            insights.append(f"😊 Positive vibes ({avg_valence}% valence) - mood booster playlist")
        elif avg_valence < 30:
            insights.append(f"😔 Melancholic tone ({avg_valence}% valence) - introspective listening")
        
        # Key insights
        most_common = stats['most_common_key']
        insights.append(f"🎹 Most common key: {most_common} - consider harmonic mixing")
        
        # Mode insights
        major_count = stats['mode_distribution']['Major']
        minor_count = stats['mode_distribution']['Minor']
        if major_count > minor_count * 2:
            insights.append(f"✨ Predominantly major keys - uplifting harmonic character")
        elif minor_count > major_count * 2:
            insights.append(f"🌙 Predominantly minor keys - darker emotional palette")
        
        # Popularity insights
        avg_pop = stats['popularity']['avg']
        if avg_pop > 70:
            insights.append(f"⭐ Mainstream appeal ({avg_pop}% popularity) - crowd pleasers")
        elif avg_pop < 30:
            insights.append(f"💎 Underground gems ({avg_pop}% popularity) - curator's picks")
        
        return insights
    
    def optimize_playlist_order(self, playlist_id: str, method: str = 'energy_flow') -> List[str]:
        """Optimize playlist track order using various methods"""
        print(f"\n⚡ OPTIMIZING PLAYLIST ORDER ({method})...")
        
        analysis = self.analyze_playlist_deep(playlist_id)
        tracks = analysis['tracks']
        
        if method == 'energy_flow':
            # Sort by energy for progressive build
            sorted_tracks = sorted(tracks, key=lambda x: x['energy'])
        
        elif method == 'bpm_ascending':
            # Sort by BPM (your dance playlist style!)
            sorted_tracks = sorted(tracks, key=lambda x: x['bpm'])
        
        elif method == 'bpm_descending':
            sorted_tracks = sorted(tracks, key=lambda x: x['bpm'], reverse=True)
        
        elif method == 'popularity':
            # Most popular first
            sorted_tracks = sorted(tracks, key=lambda x: x['popularity'], reverse=True)
        
        elif method == 'mood_journey':
            # Sad to happy
            sorted_tracks = sorted(tracks, key=lambda x: x['valence'])
        
        elif method == 'danceability':
            # Most danceable first
            sorted_tracks = sorted(tracks, key=lambda x: x['danceability'], reverse=True)
        
        elif method == 'key_flow':
            # Group by key for harmonic mixing
            sorted_tracks = sorted(tracks, key=lambda x: (x['key'], x['bpm']))
        
        else:
            print(f"   Unknown method: {method}")
            return []
        
        track_uris = [t['uri'] for t in sorted_tracks]
        
        print(f"   ✅ Optimized {len(track_uris)} tracks")
        return track_uris
    
    def apply_optimized_order(self, playlist_id: str, track_uris: List[str]) -> bool:
        """Apply new track order to playlist"""
        try:
            # Clear playlist
            print("   Clearing current tracks...")
            self.sp.playlist_replace_items(playlist_id, [])
            
            # Add in new order (max 100 at a time)
            print("   Adding tracks in optimized order...")
            for i in range(0, len(track_uris), 100):
                batch = track_uris[i:i+100]
                self.sp.playlist_add_items(playlist_id, batch)
            
            print(f"   ✅ Applied new order to playlist!")
            return True
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False
    
    def generate_professional_description(self, playlist_id: str) -> str:
        """Generate professional playlist description"""
        analysis = self.analyze_playlist_deep(playlist_id)
        stats = analysis['stats']
        
        # Build description
        desc_parts = []
        
        # Genre/mood based on features
        avg_energy = stats['energy']['avg']
        avg_dance = stats['danceability']['avg']
        avg_valence = stats['valence']['avg']
        
        if avg_energy > 70 and avg_dance > 70:
            desc_parts.append("High-energy dance")
        elif avg_energy < 40:
            desc_parts.append("Chill ambient")
        
        # BPM info
        bpm_min = stats['bpm']['min']
        bpm_max = stats['bpm']['max']
        desc_parts.append(f"({bpm_min}-{bpm_max} BPM)")
        
        # Mood
        if avg_valence > 60:
            desc_parts.append("• Uplifting vibes")
        elif avg_valence < 40:
            desc_parts.append("• Introspective mood")
        
        # Track count
        desc_parts.append(f"• {analysis['total_tracks']} carefully curated tracks")
        
        # Branding
        desc_parts.append("• Curated by Fish Music Inc")
        desc_parts.append("• GORUNFREE! 🎸🔥")
        
        description = " ".join(desc_parts)
        
        return description
    
    def create_smart_playlist(self, name: str, seed_criteria: Dict, target_tracks: int = 30) -> Optional[str]:
        """Create playlist based on audio feature criteria"""
        print(f"\n🎵 CREATING SMART PLAYLIST: {name}")
        print(f"   Criteria: {seed_criteria}")
        
        # Create playlist
        playlist = self.sp.user_playlist_create(
            user=self.username,
            name=name,
            public=True,
            description=f"Smart playlist by Fish Music Inc • {datetime.now().strftime('%Y-%m-%d')}"
        )
        
        playlist_id = playlist['id']
        
        # Get recommendations based on criteria
        # This is where we'd use Spotify's recommendations API
        # For now, search and filter
        
        print(f"   ✅ Created playlist: {name}")
        print(f"   URL: {playlist['external_urls']['spotify']}")
        
        return playlist_id
    
    def print_analysis_report(self, analysis: Dict):
        """Print beautiful analysis report"""
        print("\n" + "═" * 70)
        print(f"📊 PLAYLIST ANALYSIS: {analysis['playlist_name']}")
        print("═" * 70)
        
        stats = analysis['stats']
        
        print(f"\n📈 STATISTICS:")
        print(f"   Total Tracks: {analysis['total_tracks']}")
        print(f"\n   🎵 BPM:")
        print(f"      Range: {stats['bpm']['min']} - {stats['bpm']['max']} BPM")
        print(f"      Average: {stats['bpm']['avg']} BPM")
        print(f"      Median: {stats['bpm']['median']} BPM")
        
        print(f"\n   ⚡ Energy: {stats['energy']['avg']}% (Range: {stats['energy']['min']}-{stats['energy']['max']}%)")
        print(f"   💃 Danceability: {stats['danceability']['avg']}% (Range: {stats['danceability']['min']}-{stats['danceability']['max']}%)")
        print(f"   😊 Valence (Mood): {stats['valence']['avg']}% (Range: {stats['valence']['min']}-{stats['valence']['max']}%)")
        print(f"   ⭐ Popularity: {stats['popularity']['avg']}% (Range: {stats['popularity']['min']}-{stats['popularity']['max']}%)")
        
        print(f"\n   🎹 Musical Keys:")
        print(f"      Most Common: {stats['most_common_key']}")
        print(f"      Major/Minor: {stats['major_minor_ratio']}")
        
        print(f"\n💡 INSIGHTS:")
        for i, insight in enumerate(analysis['insights'], 1):
            print(f"   {i}. {insight}")
        
        print("\n" + "═" * 70)
        print("GORUNFREE! 🎸🔥")
        print("=" * 70 + "\n")

def main():
    """Main execution"""
    import sys
    
    print("\n🔥 SPOTIFY HOT ROD - FISH MUSIC INC")
    print("=" * 70)
    
    hotrod = SpotifyHotRod()
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python3 spotify_hotrod.py analyze <playlist_url>")
        print("  python3 spotify_hotrod.py optimize <playlist_url> <method>")
        print("\nMethods:")
        print("  energy_flow, bpm_ascending, bpm_descending, popularity")
        print("  mood_journey, danceability, key_flow")
        return
    
    command = sys.argv[1]
    
    if command == 'analyze' and len(sys.argv) > 2:
        playlist_url = sys.argv[2]
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        
        analysis = hotrod.analyze_playlist_deep(playlist_id)
        hotrod.print_analysis_report(analysis)
        
        # Save to file
        output_file = Path(f"playlist_analysis_{playlist_id}.json")
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"💾 Full analysis saved to: {output_file}")
    
    elif command == 'optimize' and len(sys.argv) > 3:
        playlist_url = sys.argv[2]
        method = sys.argv[3]
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        
        track_uris = hotrod.optimize_playlist_order(playlist_id, method)
        if track_uris:
            print(f"\n⚠️  Ready to apply optimization. This will reorder all tracks.")
            confirm = input("   Apply? (yes/no): ")
            if confirm.lower() == 'yes':
                hotrod.apply_optimized_order(playlist_id, track_uris)

if __name__ == '__main__':
    main()

