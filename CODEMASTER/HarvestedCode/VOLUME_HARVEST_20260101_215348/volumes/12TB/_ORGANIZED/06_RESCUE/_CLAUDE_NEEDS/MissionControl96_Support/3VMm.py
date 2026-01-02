import os
from pathlib import Path

def setup_dirs():
    output_dir = Path(os.getenv("OUTPUT_DIR", "~/Documents/NoizyFish/Webador_migrate/output")).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Output directory ready at {output_dir}")

def main():
    print("🚀 Bootstrapping Webador migration workspace...")
    setup_dirs()
    print("✅ Bootstrap complete. Ready for migration scripts!")

if __name__ == "__main__":
    main()