#!/usr/bin/env python3
"""
Build Canada AI Strategy Playlist
Curated podcast episodes on Canada's AI strategy, policy, and future skills
"""

import os
import sys
from typing import List, Optional

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---------- CONFIG ----------
PLAYLIST_NAME = "Canada AI Strategy – Next Decade"
PLAYLIST_DESCRIPTION = (
    "Curated episodes on Canada's AI strategy, policy, and future skills."
)

# Search queries for each episode (Spotify will fuzzy-match these)
EPISODE_QUERIES: List[str] = [
    # BetaKit – Evolving Canada's AI Strategy
    "Evolving Canada's AI strategy with CIFAR's Elissa Strome BetaKit",
    # Ask AI – Pan-Canadian AI Strategy / $125M question
    "Ask AI Podcast What would you do with $125 million and a mandate to advance artificial intelligence research and policy in Canada",
    # C.D. Howe – Intelligent AI Policy
    "Intelligent AI Policy with Anindya Sen and Rosalie Wyonch C.D. Howe",
    # Net Positive – Future Skills (Canada + AI)
    "Conclusion and Wrap Up: Lessons Learned from AI and Future Skills Net Positive",
]

# Spotify scopes required to create & edit playlists
SCOPES = "playlist-modify-public playlist-modify-private"

# ---------- AUTH ----------
def get_spotify_client() -> spotipy.Spotify:
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    if not all([client_id, client_secret, redirect_uri]):
        print("ERROR: SPOTIPY_CLIENT_ID / SPOTIPY_CLIENT_SECRET / SPOTIPY_REDIRECT_URI not set.")
        sys.exit(1)

    auth_manager = SpotifyOAuth(
        scope=SCOPES,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        open_browser=True,
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

# ---------- CORE LOGIC ----------
def create_playlist(sp: spotipy.Spotify) -> str:
    user = sp.current_user()
    user_id = user["id"]

    # Check if playlist already exists (avoid duplicates)
    existing = sp.current_user_playlists(limit=50)
    for playlist in existing["items"]:
        if playlist["name"] == PLAYLIST_NAME:
            print(f"Playlist already exists: {PLAYLIST_NAME}")
            return playlist["id"]

    playlist = sp.user_playlist_create(
        user=user_id,
        name=PLAYLIST_NAME,
        public=True,  # set False if you want it private
        description=PLAYLIST_DESCRIPTION,
    )
    print(f"Created playlist: {PLAYLIST_NAME}")
    return playlist["id"]

def search_episode(sp: spotipy.Spotify, query: str) -> Optional[str]:
    # Search episodes only; take best match
    result = sp.search(q=query, type="episode", limit=1)
    items = result.get("episodes", {}).get("items", [])
    if not items:
        print(f"WARNING: No episode found for query:\n  {query}")
        return None

    ep = items[0]
    print(f"Matched episode:\n  {ep['name']}  |  {ep['show']['name']}")
    return ep["uri"]

def add_episodes_to_playlist(sp: spotipy.Spotify, playlist_id: str, episode_uris: List[str]) -> None:
    if not episode_uris:
        print("No episodes to add. Exiting.")
        return

    sp.playlist_add_items(playlist_id, episode_uris)
    print(f"Added {len(episode_uris)} episodes to playlist.")

def main():
    sp = get_spotify_client()

    # 1) Create (or reuse) playlist
    playlist_id = create_playlist(sp)

    # 2) Search for each target episode
    episode_uris: List[str] = []
    for q in EPISODE_QUERIES:
        uri = search_episode(sp, q)
        if uri:
            episode_uris.append(uri)

    # 3) Add them to playlist
    add_episodes_to_playlist(sp, playlist_id, episode_uris)

    print("\nDone. Open Spotify and check your playlists for:")
    print(f'  → "{PLAYLIST_NAME}"')

if __name__ == "__main__":
    main()

