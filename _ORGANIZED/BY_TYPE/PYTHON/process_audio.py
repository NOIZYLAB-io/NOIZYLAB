import ffmpeg
import sys
import os

def convert_audio(input_path, output_path, format='mp3'):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, format=format)
            .run(overwrite_output=True)
        )
        print(f"Converted {input_path} to {output_path}")
    except ffmpeg.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_audio.py <input_file> <output_file> [format]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    fmt = sys.argv[3] if len(sys.argv) > 3 else 'mp3'
    convert_audio(input_file, output_file, fmt)
