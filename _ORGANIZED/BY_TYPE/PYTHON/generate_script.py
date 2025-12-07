import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_script(prompt, output_path):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    script = response.choices[0].message['content']
    with open(output_path, 'w') as f:
        f.write(script)
    print(f"Script saved to {output_path}")

if __name__ == "__main__":
    user_prompt = input("Enter a prompt for your scene or script: ")
    output_file = "../media/scripts/generated_script.txt"
    generate_script(user_prompt, output_file)
