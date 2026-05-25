from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/")
def home():
    return {"status": "running", "stored_messages": len(messages)}

@app.post("/send")
def send(msg: Message):
    print("RECEIVED MESSAGE:", msg)
    messages.append(msg.dict())
    print("TOTAL MESSAGES:", len(messages))
    return {"status": "stored", "count": len(messages)}

@app.get("/get/{receiver}")
def get(receiver: str):

    print("LOOKING FOR:", receiver)
    print("DATABASE:", messages)

    for msg in reversed(messages):
        if msg["receiver"].strip().lower() == receiver.strip().lower():
            return msg

    return {"error": "no message", "available_receivers": [m["receiver"] for m in messages]}
