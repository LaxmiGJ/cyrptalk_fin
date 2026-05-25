import streamlit as st
import requests
from deep_translator import GoogleTranslator
import zlib
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BACKEND_URL = "https://cyrptalk-fin.onrender.com/send""

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

# -------------------------------
# STRONG KEYWORD EMOTION MODEL
# -------------------------------

EMOTION_KEYWORDS = {
    "joy": [
        "happy", "happiness", "joy", "joyful", "excited", "great", "good", "awesome",
        "love", "loved", "like", "amazing", "wonderful", "fantastic", "best", "smile",
        "cheerful", "delighted", "pleasant", "enjoy", "enjoying"
    ],
    "sadness": [
        "sad", "cry", "crying", "depressed", "unhappy", "hurt", "pain", "lonely",
        "miss", "missing", "bad", "worst", "terrible", "upset", "heartbroken"
    ],
    "anger": [
        "angry", "mad", "furious", "annoyed", "irritated", "hate", "hated",
        "frustrated", "rage", "offended", "disgusted"
    ],
    "fear": [
        "scared", "afraid", "fear", "terrified", "panic", "worried", "anxious",
        "nervous", "frightened"
    ],
    "surprise": [
        "surprised", "shock", "shocked", "wow", "unexpected", "amazed", "astonished"
    ],
    "confusion": [
        "confused", "confusing", "unsure", "don't know", "doubt", "unclear"
    ]
}

NEGATIONS = ["not", "no", "never", "don't", "dont", "isn't", "arent", "wasn't", "wont", "cannot"]

def detect_emotion(text):

    text = text.lower()

    words = text.split()

    scores = {
        "joy": 0,
        "sadness": 0,
        "anger": 0,
        "fear": 0,
        "surprise": 0,
        "confusion": 0
    }

    # check keywords
    for i, word in enumerate(words):

        for emotion, keywords in EMOTION_KEYWORDS.items():

            if word in keywords:

                # NEGATION CHECK (previous word)
                if i > 0 and words[i - 1] in NEGATIONS:
                    scores[emotion] -= 2   # reverse meaning
                else:
                    scores[emotion] += 2

    # pick best emotion
    best_emotion = max(scores, key=scores.get)

    # if all zero → neutral
    if scores[best_emotion] == 0:
        return "neutral"

    return best_emotion

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
    emoji = EMOJI.get(emotion, "😐")

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
        st.write("Detected Emotion:", emotion)
        st.write(tagged)
    else:
        st.error("Failed to send message ❌")
