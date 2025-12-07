import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

SORA_API_KEY = os.getenv('SORA_API_KEY')
SORA_API_URL = os.getenv('SORA_API_URL', 'https://api.sora.openai.com/v1/video')  # Replace with actual endpoint if needed

headers = {
    'Authorization': f'Bearer {SORA_API_KEY}'
}

def image_to_video(image_path, prompt, output_path):
    files = {'image': open(image_path, 'rb')}
    data = {'prompt': prompt}
    response = requests.post(SORA_API_URL, headers=headers, files=files, data=data)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Video saved to {output_path}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python sora_image_to_video.py <image_path> <prompt> <output_video>")
        exit(1)
    image_path = sys.argv[1]
    prompt = sys.argv[2]
    output_video = sys.argv[3]
    image_to_video(image_path, prompt, output_video)
