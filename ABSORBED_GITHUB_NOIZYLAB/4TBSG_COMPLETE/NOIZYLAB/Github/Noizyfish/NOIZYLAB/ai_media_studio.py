import os
import openai
import requests
import ffmpeg
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
SORA_API_KEY = os.getenv('SORA_API_KEY')
SORA_API_URL = os.getenv('SORA_API_URL', 'https://api.sora.openai.com/v1/video')

MEDIA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../media'))
SCRIPTS_DIR = os.path.join(MEDIA_DIR, 'scripts')
VIDEOS_DIR = os.path.join(MEDIA_DIR, 'videos')
AUDIO_DIR = os.path.join(MEDIA_DIR, 'audio')

os.makedirs(SCRIPTS_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_script(prompt, output_path):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    script = response.choices[0].message['content']
    with open(output_path, 'w') as f:
        f.write(script)
    print(f"Script saved to {output_path}")
    return output_path

def create_video(script_path, output_path):
    with open(script_path, 'r') as f:
        script = f.read()
    headers = {'Authorization': f'Bearer {SORA_API_KEY}'}
    data = {'script': script}
    response = requests.post(SORA_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Video saved to {output_path}")
        return output_path
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def convert_audio(input_path, output_path, format='mp3'):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, format=format)
            .run(overwrite_output=True)
        )
        print(f"Converted {input_path} to {output_path}")
        return output_path
    except ffmpeg.Error as e:
        print(f"Error: {e}")
        return None

def main():
    print("Welcome to the AI Media Studio!")
    prompt = input("Enter a prompt for your scene or script: ")
    script_file = os.path.join(SCRIPTS_DIR, 'generated_script.txt')
    video_file = os.path.join(VIDEOS_DIR, 'generated_video.mp4')
    audio_file = os.path.join(AUDIO_DIR, 'audio_from_video.mp3')

    # Step 1: Generate script
    generate_script(prompt, script_file)

    # Step 2: Create video
    create_video(script_file, video_file)

    # Step 3: Convert video to audio (optional demo)
    convert_audio(video_file, audio_file, 'mp3')

if __name__ == "__main__":
    main()
