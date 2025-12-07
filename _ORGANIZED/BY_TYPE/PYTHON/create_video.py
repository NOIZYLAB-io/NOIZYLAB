import os
import requests
from dotenv import load_dotenv

load_dotenv()
SORA_API_KEY = os.getenv('SORA_API_KEY')
SORA_API_URL = os.getenv('SORA_API_URL', 'https://api.sora.openai.com/v1/video')

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
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    script_file = "../media/scripts/generated_script.txt"
    output_file = "../media/videos/generated_video.mp4"
    create_video(script_file, output_file)
