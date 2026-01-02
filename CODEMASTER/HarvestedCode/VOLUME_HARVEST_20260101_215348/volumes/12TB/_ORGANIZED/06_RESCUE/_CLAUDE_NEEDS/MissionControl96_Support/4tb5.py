import concurrent.futures
import os
import requests
import subprocess
import threading
import time

# --- 11 Labs Sarah TTS ---
def sarah_11labs_speak(text, api_key, voice_id):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.ok:
            with open("sarah_output.mp3", "wb") as f:
                f.write(response.content)
            subprocess.run(["afplay", "sarah_output.mp3"])
        else:
            print("Error with 11 Labs TTS:", response.text)
    except Exception as e:
        print("TTS execution failed:", e)

# --- Example Task Function ---
def agent_task(task_id, api_key, voice_id):
    message = f"Agent {task_id} completed its task."
    sarah_11labs_speak(message, api_key, voice_id)
    return message

# --- Run 96 Agents in Parallel ---
def run_96_agents_on_task(api_key, voice_id):
    with concurrent.futures.ThreadPoolExecutor(max_workers=96) as executor:
        futures = [executor.submit(agent_task, i+1, api_key, voice_id) for i in range(96)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

# --- Main Entry Point ---
if __name__ == "__main__":
    # Replace with your actual API key and Sarah voice ID
    api_key = "YOUR_11LABS_API_KEY"
    voice_id = "YOUR_SARAH_VOICE_ID"
    print("Running 96 agents on every task...")
    run_96_agents_on_task(api_key, voice_id)
