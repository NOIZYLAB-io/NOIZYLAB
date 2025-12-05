def ensure_directory_exists(directory: str) -> None:
    """Ensure that a directory exists; create it if it does not."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def file_checksum(file_path: str) -> str:
    """Calculate the checksum of a file."""
    import hashlib
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def is_audio_file(file_path: str) -> bool:
    """Check if a file is an audio file based on its extension."""
    audio_extensions = {'.mp3', '.wav', '.flac', '.aac', '.ogg'}
    return os.path.splitext(file_path)[1].lower() in audio_extensions

def probe_audio_file(file_path: str) -> dict:
    """Probe an audio file and return its metadata."""
    from mutagen import File
    audio = File(file_path)
    return {
        'duration': audio.info.length,
        'bitrate': audio.info.bitrate,
        'channels': audio.info.channels,
        'sample_rate': audio.info.sample_rate,
    } if audio else {}