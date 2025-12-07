#!/usr/bin/env python3
"""
🎵 VECTOR DATABASE MUSIC SEARCH - FISH MUSIC INC
Semantic search for tracks using AI embeddings - FIND MUSIC BY VIBE!
"""

import chromadb
from chromadb.config import Settings
import json
import os
from pathlib import Path

class MusicVectorSearch:
    """AI-powered semantic music search using vector embeddings"""
    
    def __init__(self, db_path="./music_vector_db"):
        """Initialize ChromaDB (100% FREE!)"""
        self.client = chromadb.PersistentClient(path=db_path)
        
        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name="fish_music_tracks",
            metadata={"description": "Fish Music Inc track catalog with AI embeddings"}
        )
        
        print(f"✅ Vector DB initialized: {db_path}")
    
    def add_track(self, track_id, track_name, genre, description, tags=None, metadata=None):
        """Add track to vector database"""
        
        # Create rich text representation for embedding
        text_for_embedding = f"{track_name} {genre} {description}"
        if tags:
            text_for_embedding += f" {' '.join(tags)}"
        
        # Metadata for filtering
        track_metadata = {
            "track_name": track_name,
            "genre": genre,
            "description": description,
            **(metadata or {})
        }
        
        if tags:
            track_metadata["tags"] = ",".join(tags)
        
        # Add to collection (ChromaDB auto-generates embeddings!)
        self.collection.add(
            documents=[text_for_embedding],
            metadatas=[track_metadata],
            ids=[str(track_id)]
        )
        
        print(f"✅ Added track: {track_name} (ID: {track_id})")
    
    def search_by_vibe(self, query, n_results=5):
        """
        Search for tracks by VIBE/feeling/description
        
        Examples:
        - "energetic upbeat summer vibes"
        - "dark cinematic emotional"
        - "chill lo-fi beats for studying"
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        tracks = []
        if results['metadatas']:
            for i, metadata in enumerate(results['metadatas'][0]):
                distance = results['distances'][0][i] if results['distances'] else None
                tracks.append({
                    'id': results['ids'][0][i],
                    'metadata': metadata,
                    'similarity': 1 - distance if distance else None
                })
        
        return tracks
    
    def search_by_genre(self, genre, n_results=10):
        """Find tracks by genre"""
        results = self.collection.query(
            query_texts=[genre],
            n_results=n_results,
            where={"genre": genre}
        )
        
        return self._format_results(results)
    
    def recommend_similar(self, track_id, n_results=5):
        """Find similar tracks to a given track"""
        # Get the track
        track = self.collection.get(ids=[str(track_id)])
        
        if not track['documents']:
            return []
        
        # Search for similar
        results = self.collection.query(
            query_texts=track['documents'],
            n_results=n_results + 1  # +1 because it includes itself
        )
        
        # Remove the original track from results
        return self._format_results(results)[1:]
    
    def _format_results(self, results):
        """Format search results"""
        tracks = []
        if results['metadatas']:
            for i, metadata in enumerate(results['metadatas'][0]):
                distance = results['distances'][0][i] if results['distances'] else None
                tracks.append({
                    'id': results['ids'][0][i],
                    'track_name': metadata.get('track_name'),
                    'genre': metadata.get('genre'),
                    'description': metadata.get('description'),
                    'similarity': round((1 - distance) * 100, 1) if distance else None
                })
        return tracks
    
    def get_all_tracks(self):
        """Get all tracks in database"""
        results = self.collection.get()
        
        tracks = []
        if results['metadatas']:
            for i, metadata in enumerate(results['metadatas']):
                tracks.append({
                    'id': results['ids'][i],
                    **metadata
                })
        
        return tracks
    
    def get_stats(self):
        """Get database statistics"""
        count = self.collection.count()
        
        return {
            'total_tracks': count,
            'collection_name': self.collection.name,
            'ready_for_search': count > 0
        }

# DEMO DATA LOADER
def load_demo_tracks(db):
    """Load demo tracks for Fish Music"""
    
    demo_tracks = [
        {
            'track_id': 1,
            'track_name': 'Epic Cinematic Theme',
            'genre': 'Orchestral',
            'description': 'Dramatic orchestral piece with soaring strings and powerful brass. Perfect for trailers and emotional moments.',
            'tags': ['cinematic', 'epic', 'dramatic', 'orchestral', 'emotional'],
            'metadata': {'duration': '3:45', 'bpm': 120, 'key': 'C minor'}
        },
        {
            'track_id': 2,
            'track_name': 'Urban Beat',
            'genre': 'Hip Hop',
            'description': 'Hard-hitting trap beat with 808s and crisp hi-hats. Modern urban energy.',
            'tags': ['trap', 'urban', 'beats', 'hip-hop', 'modern'],
            'metadata': {'duration': '2:30', 'bpm': 140, 'key': 'F minor'}
        },
        {
            'track_id': 3,
            'track_name': 'Ambient Soundscape',
            'genre': 'Electronic',
            'description': 'Ethereal ambient textures with subtle pads and atmospheric elements. Relaxing and meditative.',
            'tags': ['ambient', 'electronic', 'chill', 'atmospheric', 'relaxing'],
            'metadata': {'duration': '4:20', 'bpm': 80, 'key': 'A major'}
        },
        {
            'track_id': 4,
            'track_name': 'Corporate Motivational',
            'genre': 'Corporate',
            'description': 'Uplifting corporate track with piano, guitars, and steady drums. Professional and inspiring.',
            'tags': ['corporate', 'motivational', 'uplifting', 'professional', 'inspiring'],
            'metadata': {'duration': '2:15', 'bpm': 125, 'key': 'G major'}
        },
        {
            'track_id': 5,
            'track_name': 'Retro Synthwave',
            'genre': 'Electronic',
            'description': '80s inspired synthwave with nostalgic melodies and driving basslines. Neon dreams.',
            'tags': ['synthwave', '80s', 'retro', 'electronic', 'nostalgic'],
            'metadata': {'duration': '3:30', 'bpm': 110, 'key': 'D minor'}
        }
    ]
    
    for track in demo_tracks:
        db.add_track(
            track['track_id'],
            track['track_name'],
            track['genre'],
            track['description'],
            track.get('tags'),
            track.get('metadata')
        )
    
    print(f"\n✅ Loaded {len(demo_tracks)} demo tracks")

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("🎵 FISH MUSIC VECTOR SEARCH")
    print("=" * 60)
    print()
    
    db = MusicVectorSearch()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Load demo tracks:
    python3 VECTOR_DB_MUSIC_SEARCH.py load-demo
  
  Search by vibe:
    python3 VECTOR_DB_MUSIC_SEARCH.py search "energetic upbeat summer"
  
  Find similar to track:
    python3 VECTOR_DB_MUSIC_SEARCH.py similar <track_id>
  
  List all tracks:
    python3 VECTOR_DB_MUSIC_SEARCH.py list
  
  Add new track:
    python3 VECTOR_DB_MUSIC_SEARCH.py add <id> <name> <genre> <description>
  
  Database stats:
    python3 VECTOR_DB_MUSIC_SEARCH.py stats

FEATURES:
  - 🎯 Search by VIBE/feeling (not just keywords!)
  - 🔍 Find similar tracks automatically
  - 🎵 Recommend tracks to customers
  - 💡 Smart playlist generation
  - 🚀 Works with ANY number of tracks
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "load-demo":
        load_demo_tracks(db)
    
    elif command == "search":
        query = " ".join(sys.argv[2:])
        print(f"🔍 Searching for: '{query}'")
        print()
        
        results = db.search_by_vibe(query)
        
        for i, track in enumerate(results, 1):
            print(f"{i}. {track['track_name']}")
            print(f"   Genre: {track['genre']}")
            print(f"   Description: {track['description']}")
            print(f"   Similarity: {track['similarity']}%")
            print()
    
    elif command == "similar":
        track_id = sys.argv[2]
        print(f"🎵 Finding tracks similar to ID {track_id}...")
        print()
        
        results = db.recommend_similar(track_id)
        
        for i, track in enumerate(results, 1):
            print(f"{i}. {track['track_name']}")
            print(f"   Genre: {track['genre']}")
            print(f"   Similarity: {track['similarity']}%")
            print()
    
    elif command == "list":
        tracks = db.get_all_tracks()
        print(f"📊 Total Tracks: {len(tracks)}")
        print()
        
        for track in tracks:
            print(f"ID {track['id']}: {track['track_name']} ({track['genre']})")
    
    elif command == "add":
        track_id = sys.argv[2]
        track_name = sys.argv[3]
        genre = sys.argv[4]
        description = " ".join(sys.argv[5:])
        
        db.add_track(track_id, track_name, genre, description)
    
    elif command == "stats":
        stats = db.get_stats()
        print(f"📊 Database Statistics:")
        print(f"  Total Tracks: {stats['total_tracks']}")
        print(f"  Collection: {stats['collection_name']}")
        print(f"  Ready: {'✅' if stats['ready_for_search'] else '❌'}")
    
    else:
        print(f"❌ Unknown command: {command}")

