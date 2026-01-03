"""
NOIZYVOICE Configuration
"""
from functools import lru_cache
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings"""

    # App
    app_name: str = "NOIZYVOICE"
    app_version: str = "0.1.0"
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1

    # Paths
    models_dir: Path = Path("models")
    voices_dir: Path = Path("voices")
    cache_dir: Path = Path("cache")

    # TTS Models
    default_model: str = "xtts-v2"
    xtts_model_path: Optional[str] = None
    styletts_model_path: Optional[str] = None

    # Voice Cloning
    min_clone_duration: float = 3.0  # seconds
    max_clone_duration: float = 30.0  # seconds
    voice_embedding_dim: int = 512

    # Audio
    sample_rate: int = 24000
    output_sample_rate: int = 48000
    audio_format: str = "wav"
    normalize_audio: bool = True

    # Streaming
    stream_chunk_size: int = 1024
    stream_latency_target: float = 0.075  # 75ms
    websocket_ping_interval: float = 20.0

    # GPU
    device: str = "cuda"  # cuda, cpu, mps
    gpu_memory_fraction: float = 0.9
    enable_flash_attention: bool = True

    # Cache
    enable_cache: bool = True
    cache_ttl: int = 3600  # 1 hour
    max_cache_size: int = 1000  # MB

    # Rate Limiting
    enable_rate_limit: bool = True
    rate_limit_requests: int = 100
    rate_limit_window: int = 60  # seconds

    # API Keys
    api_key_required: bool = False
    admin_api_key: Optional[str] = None

    # Storage
    storage_backend: str = "local"  # local, s3, r2
    s3_bucket: Optional[str] = None
    s3_region: Optional[str] = None

    # Redis
    redis_url: str = "redis://localhost:6379"

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    class Config:
        env_prefix = "NOIZY_"
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


# Supported languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "pl": "Polish",
    "tr": "Turkish",
    "ru": "Russian",
    "nl": "Dutch",
    "cs": "Czech",
    "ar": "Arabic",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "hu": "Hungarian",
    "hi": "Hindi",
}

# Supported emotions
EMOTIONS = [
    "neutral",
    "happy",
    "sad",
    "angry",
    "fearful",
    "surprised",
    "disgusted",
    "calm",
    "excited",
]

# Audio tags
AUDIO_TAGS = {
    "whispers": {"intensity": 0.3, "pitch_shift": -0.1},
    "shouts": {"intensity": 1.5, "pitch_shift": 0.2},
    "laughs": {"effect": "laugh", "duration": 1.0},
    "sighs": {"effect": "sigh", "duration": 0.8},
    "cries": {"effect": "cry", "intensity": 0.7},
    "excited": {"speed": 1.2, "pitch_shift": 0.15},
    "sad": {"speed": 0.85, "pitch_shift": -0.1},
    "angry": {"speed": 1.1, "intensity": 1.3},
    "scared": {"speed": 1.15, "pitch_shift": 0.2, "tremolo": True},
}
