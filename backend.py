from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "messages.json"

# ALWAYS ensure file exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

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
    return {"status": "CrypTalk Backend Running"}


@app.post("/send")
def send_message(msg: Message):

    try:
        with open(DB_FILE, "r") as f:
            messages = json.load(f)
    except:
        messages = []

    messages.append(msg.dict())

    with open(DB_FILE, "w") as f:
        json.dump(messages, f)

    return {"status": "stored", "count": len(messages)}


@app.get("/get/{receiver}")
def get_message(receiver: str):

    try:
        with open(DB_FILE, "r") as f:
            messages = json.load(f)
    except:
        return {"error": "db error"}

    for msg in reversed(messages):
        if msg["receiver"].strip().lower() == receiver.strip().lower():
            return msg

    return {"error": "no message"}
