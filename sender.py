import streamlit as st
import requests
from deep_translator import GoogleTranslator
import zlib
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BACKEND_URL = "https://cyrptalk-fin.onrender.com"

LANG = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

EMOJI = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "confusion": "😕",
    "neutral": "😐"
}

def detect_emotion(text):

    text = text.lower()

    if any(w in text for w in ["happy", "good", "great", "love"]):
        return "joy"

    if any(w in text for w in ["sad", "cry", "bad"]):
        return "sadness"

    if "angry" in text:
        return "anger"

    if "scared" in text:
        return "fear"

    if "?" in text:
        return "confusion"

    return "neutral"

def encrypt(data):

    key = AESGCM.generate_key(bit_length=128)

    aes = AESGCM(key)

    nonce = os.urandom(12)

    enc = aes.encrypt(nonce, data, None)

    return enc, key, nonce

st.title("🔐 CrypTalk Sender")

sender = st.text_input("Sender Name")

receiver = st.text_input("Receiver Name")

s_lang = st.selectbox("Sender Language", list(LANG.keys()))

r_lang = st.selectbox("Receiver Language", list(LANG.keys()))

msg = st.text_area("Message")

if st.button("Send"):

    translated = GoogleTranslator(
        source=LANG[s_lang],
        target="en"
    ).translate(msg)

    emotion = detect_emotion(translated)

    emoji = EMOJI[emotion]

    tagged = f"[{emotion.upper()} {emoji}] {translated}"

    compressed = zlib.compress(tagged.encode())

    enc, key, nonce = encrypt(compressed)

    payload = {
        "sender": sender,
        "receiver": receiver,
        "encrypted": enc.hex(),
        "key": key.hex(),
        "nonce": nonce.hex(),
        "sender_lang": s_lang,
        "receiver_lang": r_lang,
        "emotion": emotion,
        "tagged_text": tagged
    }

    r = requests.post(BACKEND_URL, json=payload)

    if r.status_code == 200:
        st.success("Message Sent ✅")
        st.write(tagged)

    else:
        st.error("Backend connection failed ❌")
