import os, requests, json

def ask(model:str, prompt:str):
    if model.lower() == "openai":
        url = "https://api.openai.com/v1/chat/completions"
        data = {"model":"gpt-4o", "messages":[{"role":"user","content":prompt}]}
        headers = {"Authorization":f"Bearer {os.getenv('OPENAI_API_KEY')}"}
        r = requests.post(url, headers=headers, json=data)
        return r.json()["choices"][0]["message"]["content"]

    elif model.lower() == "anthropic":
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
            "content-type":"application/json"
        }
        data = {"model":"claude-3-5-sonnet-20240620",
                "messages":[{"role":"user","content":prompt}]}
        r = requests.post(url, headers=headers, json=data)
        return r.json()["content"][0]["text"]

    elif model.lower() == "copilot":
        # Copilot uses GitHub API (limited public endpoints)
        return "Copilot handled inline completions inside VS Code; no REST call needed."

    else:
        raise ValueError("Unknown model")

if __name__ == "__main__":
    print(ask("openai", "Write a short haiku about Noizy.ai"))