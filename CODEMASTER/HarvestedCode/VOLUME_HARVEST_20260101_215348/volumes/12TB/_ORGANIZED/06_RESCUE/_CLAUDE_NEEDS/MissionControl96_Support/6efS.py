from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/speak")
def speak(message: Message):
    # Here you would call ElevenLabs Sarah TTS
    return {"response": f"Sarah says: {message.text}"}
