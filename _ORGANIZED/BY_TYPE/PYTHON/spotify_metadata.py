import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 🔑 Spotify Developer credentials
client_id = "92612591d2c74d4586b20a5679f8cd4b"
client_secret = "5766aa3c182e497e992fc2abec551e0d"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track_metadata(track_ids):
    """
    Fetch track metadata (name + artist) + audio features
    """
    features = sp.audio_features(track_ids)
    metadata = sp.tracks(track_ids)["tracks"]

    rows = []
    for f, m in zip(features, metadata):
        if f and m:  # make sure both exist
            row = {
                "id": f["id"],
                "name": m["name"],
                "artists": ", ".join([artist["name"] for artist in m["artists"]]),
                "danceability": f["danceability"],
                "energy": f["energy"],
                "key": f["key"],
                "loudness": f["loudness"],
                "mode": f["mode"],
                "speechiness": f["speechiness"],
                "acousticness": f["acousticness"],
                "instrumentalness": f["instrumentalness"],
                "liveness": f["liveness"],
                "valence": f["valence"],
                "tempo": f["tempo"],
                "duration_ms": f["duration_ms"],
                "time_signature": f["time_signature"]
            }
            rows.append(row)
    return rows

def save_to_csv(track_ids, filename="noizybeast_metadata.csv"):
    rows = get_track_metadata(track_ids)
    if not rows:
        print("⚠️ No data found.")
        return
    
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"✅ Catalog saved to {filename}")

# 🎵 Example tracks (replace with your own)
track_ids = [
    "2takcwOaAZWiXQijPHIx7B",
    "3n3Ppam7vgaVa1iaRUc9Lp",
    "7ouMYWpwJ422jRcDASZB7P"
]

save_to_csv(track_ids)




























import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 🔑 Spotify Developer credentials
client_id = "92612591d2c74d4586b20a5679f8cd4b"
client_secret = “5766aa3c182e497e992fc2abec551e0d”

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track_metadata(track_ids):
    """
    Fetch track metadata (name + artist) + audio features
    """
    features = sp.audio_features(track_ids)
    metadata = sp.tracks(track_ids)["tracks"]

    rows = []
    for f, m in zip(features, metadata):
        if f and m:  # make sure both exist
            row = {
                "id": f["id"],
                "name": m["name"],
                "artists": ", ".join([artist["name"] for artist in m["artists"]]),
                "danceability": f["danceability"],
                "energy": f["energy"],
                "key": f["key"],
                "loudness": f["loudness"],
                "mode": f["mode"],
                "speechiness": f["speechiness"],
                "acousticness": f["acousticness"],
                "instrumentalness": f["instrumentalness"],
                "liveness": f["liveness"],
                "valence": f["valence"],
                "tempo": f["tempo"],
                "duration_ms": f["duration_ms"],
                "time_signature": f["time_signature"]
            }
            rows.append(row)
    return rows

def save_to_csv(track_ids, filename="noizybeast_metadata.csv"):
    rows = get_track_metadata(track_ids)
    if not rows:
        print("⚠️ No data found.")
        return
    
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"✅ Catalog saved to {filename}")

# 🎵 Example tracks (replace with your own)
track_ids = [
    "2takcwOaAZWiXQijPHIx7B",
    "3n3Ppam7vgaVa1iaRUc9Lp",
    "7ouMYWpwJ422jRcDASZB7P"
]

save_to_csv(track_ids)























import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 🔑 Spotify Developer credentials
client_id = "92612591d2c74d4586b20a5679f8cd4b"
client_secret = "5766aa3c182e497e992fc2abec551e0d"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_audio_features(track_ids):
    """
    Fetch audio features for a list of Spotify track IDs
    """
    features = sp.audio_features(track_ids)
    return [f for f in features if f]  # filter out None results

def save_to_csv(track_ids, filename="noizybeast_metadata.csv"):
    """
    Fetch features and save them to CSV
    """
    features = get_audio_features(track_ids)
    if not features:
        print("⚠️ No features found.")
        return
    
    df = pd.DataFrame(features)
    df.to_csv(filename, index=False)
    print(f"✅ Metadata saved to {filename}")

# 🎵 Example usage
track_ids = [
    "2takcwOaAZWiXQijPHIx7B",  # Replace with your own Spotify track IDs
    "3n3Ppam7vgaVa1iaRUc9Lp",
    "7ouMYWpwJ422jRcDASZB7P"
]

save_to_csv(track_ids)







import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 🔑 Spotify Developer credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_audio_features(track_ids):
    features = sp.audio_features(track_ids)
    return [f for f in features if f]

def save_to_csv(track_ids, filename="noizybeast_metadata.csv"):
    features = get_audio_features(track_ids)
    if not features:
        print("⚠️ No features found.")
        return
    
    df = pd.DataFrame(features)
    df.to_csv(filename, index=False)
    print(f"✅ Metadata saved to {filename}")

# 🎵 Example tracks (replace with your own)
track_ids = [
    "2takcwOaAZWiXQijPHIx7B",
    "3n3Ppam7vgaVa1iaRUc9Lp",
    "7ouMYWpwJ422jRcDASZB7P"
]

save_to_csv(track_ids)

