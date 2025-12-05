"""
SPOTIFY INTEGRATION - FISH MUSIC INC
Configuration and credentials management
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import os
from pathlib import Path

class SpotifyConfig:
    """Spotify API configuration for Fish Music Inc"""
    
    # Fish Music Inc Spotify Profile
    SPOTIFY_USERNAME = "fishmusicinc"
    SPOTIFY_PROFILE_URL = "https://open.spotify.com/user/fishmusicinc?si=cdd28a96eef94a65"
    
    # API Credentials (set via environment variables)
    CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID', 'YOUR_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET', 'YOUR_CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI', 'http://localhost:8888/callback')
    
    # Scopes needed for Fish Music Inc operations
    SCOPES = [
        'user-library-read',           # Read saved tracks
        'user-library-modify',         # Modify saved tracks
        'playlist-read-private',       # Read private playlists
        'playlist-read-collaborative', # Read collaborative playlists
        'playlist-modify-public',      # Create/modify public playlists
        'playlist-modify-private',     # Create/modify private playlists
        'user-read-private',           # Read user profile
        'user-read-email',             # Read user email
        'user-top-read',               # Read top artists/tracks
        'user-read-recently-played',   # Read recently played
        'user-follow-read',            # Read followed artists
        'user-follow-modify',          # Modify followed artists
    ]
    
    SCOPE_STRING = ' '.join(SCOPES)
    
    # Cache settings
    CACHE_PATH = Path.home() / '.cache' / 'fishmusicinc_spotify_token'
    
    @classmethod
    def is_configured(cls) -> bool:
        """Check if Spotify credentials are configured"""
        return (
            cls.CLIENT_ID != 'YOUR_CLIENT_ID' and
            cls.CLIENT_SECRET != 'YOUR_CLIENT_SECRET' and
            cls.CLIENT_ID and
            cls.CLIENT_SECRET
        )
    
    @classmethod
    def get_auth_url(cls) -> str:
        """Get Spotify authorization URL"""
        return f"https://accounts.spotify.com/authorize?client_id={cls.CLIENT_ID}&response_type=code&redirect_uri={cls.REDIRECT_URI}&scope={cls.SCOPE_STRING}"
    
    @classmethod
    def setup_instructions(cls) -> str:
        """Return setup instructions"""
        return """
        🎵 SPOTIFY API SETUP INSTRUCTIONS
        ═══════════════════════════════════════
        
        1. Go to: https://developer.spotify.com/dashboard
        2. Log in with your Spotify account (fishmusicinc)
        3. Click "Create app"
        4. Fill in:
           - App name: Fish Music Inc
           - App description: Fish Music Inc Spotify Integration
           - Redirect URI: http://localhost:8888/callback
        5. Check the box agreeing to terms
        6. Click "Save"
        7. Copy your Client ID and Client Secret
        8. Set environment variables:
        
           export SPOTIPY_CLIENT_ID="your_actual_client_id"
           export SPOTIPY_CLIENT_SECRET="your_actual_client_secret"
           export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"
        
        9. Or add to your shell config (~/.zshrc or ~/.bashrc):
        
           echo 'export SPOTIPY_CLIENT_ID="your_client_id"' >> ~/.zshrc
           echo 'export SPOTIPY_CLIENT_SECRET="your_secret"' >> ~/.zshrc
           echo 'export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"' >> ~/.zshrc
           source ~/.zshrc
        
        Then run: python3 spotify_manager.py --setup
        
        GORUNFREE! 🎸🔥
        """

# Fish Music Inc Brand
BRAND = {
    'name': 'Fish Music Inc',
    'spotify_username': 'fishmusicinc',
    'profile_url': 'https://open.spotify.com/user/fishmusicinc?si=cdd28a96eef94a65',
    'email': 'rp@fishmusicinc.com',
    'website': 'fishmusicinc.com',
    'motto': 'GORUNFREE! 🎸🔥'
}

