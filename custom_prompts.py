import requests
import json
import constants
from ipc import IPC


ipc_ = IPC.connect()


async def create_prompt(prompt, name):
    url = constants.cloud + "/prompts/create"
    headers = {
        "X-Session": ipc_.get("current_session"),
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json={"prompt": prompt, "name": name})
    return response.json()


async def get_prompt(prompt_id):
    url = constants.cloud + "/prompts/get/one"
    headers = {
        "X-Session": ipc_.get("current_session"),
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json={"prompt_id": prompt_id})
    return response.json()


async def get_prompts_all():
    url = constants.cloud + "/prompts/get/all"
    headers = {
        "X-Session": ipc_.get("current_session"),
        "Content-Type": "application/json",
    }

    print(f"headers: {headers}")

    response = requests.post(url, headers=headers, json={})
    return response.json()

async def edit_prompt(prompt, name, prompt_id):
    url = constants.cloud + "/prompts/edit"
    headers = {
        "X-Session": ipc_.get("current_session"),
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json={"name": name, "prompt": prompt, "prompt_id": prompt_id})
    return response.json()


async def delete_prompt(prompt_id):
    url = constants.cloud + "/prompts/delete"
    headers = {
        "X-Session": ipc_.get("current_session"),
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json={"prompt_id": prompt_id})
    return response.json()