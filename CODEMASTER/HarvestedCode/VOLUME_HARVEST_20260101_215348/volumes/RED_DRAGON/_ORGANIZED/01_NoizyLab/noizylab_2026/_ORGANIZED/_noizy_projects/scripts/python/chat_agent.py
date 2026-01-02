from noizy_router import ask

def chat_agent(prompt, target="openai"):
    try:
        reply = ask(target, prompt)
        with open("chat_history.log","a") as f:
            f.write(f"\n[{target.upper()}]\nUSER: {prompt}\nAI: {reply}\n")
        return reply
    except Exception as e:
        return f"Chat error: {e}"