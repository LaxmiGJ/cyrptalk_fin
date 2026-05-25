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

# ----------------------------
# IN-MEMORY DATABASE (FIX)
# ----------------------------
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
    return {"status": "CrypTalk Backend Running"}

@app.post("/send")
def send_message(msg: Message):
    messages.append(msg.dict())
    return {"status": "stored", "total_messages": len(messages)}

@app.get("/get/{receiver}")
def get_message(receiver: str):

    for msg in reversed(messages):
        if msg["receiver"].strip().lower() == receiver.strip().lower():
            return msg

    return {"error": "no message"}
