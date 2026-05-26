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
    return {
        "status": "backend running",
        "messages_count": len(messages),
        "messages": messages
    }

@app.post("/send")
def send_message(msg: Message):

    print("MESSAGE RECEIVED")

    messages.append(msg.dict())

    print(messages)

    return {
        "status": "stored",
        "count": len(messages)
    }

@app.get("/get/{receiver}")
def get_message(receiver: str):

    print("SEARCHING FOR:", receiver)

    for msg in reversed(messages):

        print("CHECKING:", msg["receiver"])

        if msg["receiver"].strip().lower() == receiver.strip().lower():

            print("FOUND MESSAGE")

            return msg

    return {
        "error": "no message",
        "stored_messages": messages
    }
