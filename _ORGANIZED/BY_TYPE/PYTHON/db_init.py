"""
Database initialization script
GORUNFREE! 🎸🔥
"""

import os
from pathlib import Path
from sqlalchemy import create_engine
from main import Base, DATA_PATH

def init_db():
    """Initialize database with tables"""

    # Ensure data directory exists
    DATA_PATH.mkdir(exist_ok=True)

    # Create database
    DB_URL = f"sqlite:///{DATA_PATH / 'healtheworld.db'}"
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

    # Create all tables
    Base.metadata.create_all(bind=engine)

    print(f"✅ Database initialized: {DATA_PATH / 'healtheworld.db'}")

if __name__ == "__main__":
    init_db()
