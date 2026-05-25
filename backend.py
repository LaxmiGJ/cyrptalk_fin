from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

messages = []

class Message(BaseModel):
    sender: str
    receiver: str
    encrypted: str
    key: str
    nonce: str
    sender_lang: str
    receiver_lang: str
    emotion: str
    tagged_text: str

@app.post("/send")
def send_message(msg: Message):
    messages.append(msg.dict())
    return {"status": "stored"}

@app.get("/get/{receiver}")
def get_message(receiver: str):
    for msg in reversed(messages):
        if msg["receiver"].lower() == receiver.lower():
            return msg
    return {"error": "no message"}
