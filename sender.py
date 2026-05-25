import streamlit as st
import requests
from deep_translator import GoogleTranslator
import zlib
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BACKEND_URL = "http://127.0.0.1:8000/send"

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

# ----------------------------
# EMOTION DETECTION (EXTENDED RULE-BASED)
# ----------------------------

def detect_emotion(text):

    text = text.lower()

    # ----------------------------
    # PHRASES (HIGHEST ACCURACY)
    # ----------------------------
    phrase_map = {
        # SADNESS PHRASES
        "not happy": "sadness",
        "not good": "sadness",
        "feel bad": "sadness",
        "feeling bad": "sadness",
        "very sad": "sadness",
        "extremely sad": "sadness",
        "crying badly": "sadness",
        "crying a lot": "sadness",
        "feeling alone": "sadness",
        "feel alone": "sadness",
        "miss you": "sadness",
        "i miss you": "sadness",
        "heart broken": "sadness",
        "heartbroken": "sadness",
        "feeling low": "sadness",
        "feeling down": "sadness",
        "life is bad": "sadness",

        # JOY PHRASES
        "very happy": "joy",
        "so happy": "joy",
        "extremely happy": "joy",
        "feeling great": "joy",
        "feel great": "joy",
        "i am happy": "joy",
        "love this": "joy",
        "i love this": "joy",
        "so excited": "joy",
        "really excited": "joy",
        "feeling awesome": "joy",
        "this is amazing": "joy",
        "feeling good": "joy",
        "feeling wonderful": "joy",
        "best day": "joy",

        # ANGER PHRASES
        "very angry": "anger",
        "so angry": "anger",
        "extremely angry": "anger",
        "really angry": "anger",
        "i am angry": "anger",
        "i hate this": "anger",
        "want to kill": "anger",
        "so irritating": "anger",
        "very annoying": "anger",
        "pissed off": "anger",
        "so frustrated": "anger",

        # FEAR PHRASES
        "panic attack": "fear",
        "very scared": "fear",
        "extremely scared": "fear",
        "feeling unsafe": "fear",
        "i am scared": "fear",
        "i feel scared": "fear",
        "danger ahead": "fear",
        "this is dangerous": "fear",
        "feeling threatened": "fear",
        "i am worried": "fear",
        "so worried": "fear",
        "i am afraid": "fear",

        # CONFUSION PHRASES
        "i don't understand": "confusion",
        "dont understand": "confusion",
        "i am confused": "confusion",
        "so confusing": "confusion",
        "what is this": "confusion",
        "no idea": "confusion",
        "i have no idea": "confusion",
        "i don't know": "confusion",
        "why this": "confusion",
        "how is this": "confusion"
    }

    # check phrases first
    for phrase, emotion in phrase_map.items():
        if phrase in text:
            return emotion

    # ----------------------------
    # KEYWORDS (EXPANDED)
    # ----------------------------
    EMOTION_KEYWORDS = {
        "joy": [
            "happy", "happiness", "joy", "joyful", "excited", "great", "good",
            "awesome", "amazing", "wonderful", "fantastic", "best", "nice",
            "love", "loved", "like", "smile", "cheerful", "delighted",
            "enjoy", "enjoying", "super", "brilliant", "cool", "excellent",
            "positive", "pleased", "thrilled", "glad", "content", "satisfied"
        ],

        "sadness": [
            "sad", "cry", "crying", "depressed", "unhappy", "hurt", "pain",
            "lonely", "miss", "missing", "bad", "worst", "terrible",
            "upset", "heartbroken", "alone", "suffer", "suffering",
            "hopeless", "worthless", "regret", "grief", "sorrow"
        ],

        "anger": [
            "angry", "mad", "furious", "annoyed", "irritated", "hate",
            "frustrated", "rage", "offended", "disgusted", "kill",
            "destroy", "furious", "livid", "enraged", "outraged",
            "pissed", "madness", "boiling", "aggressive"
        ],

        "fear": [
            "scared", "afraid", "fear", "terrified", "panic", "worried",
            "anxious", "nervous", "frightened", "danger", "unsafe",
            "threat", "threatened", "phobia", "stress", "stressed",
            "alarm", "horror", "panic", "dread", "uneasy"
        ],

        "surprise": [
            "surprised", "shock", "shocked", "wow", "unexpected",
            "amazed", "astonished", "unbelievable", "sudden",
            "unexpectedly", "stunned", "mindblown", "crazy"
        ],

        "confusion": [
            "confused", "confusing", "unsure", "don't know",
            "doubt", "unclear", "what", "why", "how",
            "puzzled", "lost", "misunderstand", "uncertain",
            "question", "thinking"
        ]
    }

    NEGATIONS = [
        "not", "no", "never", "don't", "dont", "isn't",
        "arent", "wasn't", "wont", "cannot", "can't"
    ]

    words = text.split()

    scores = {
        "joy": 0,
        "sadness": 0,
        "anger": 0,
        "fear": 0,
        "surprise": 0,
        "confusion": 0
    }

    for i, word in enumerate(words):

        for emotion, keywords in EMOTION_KEYWORDS.items():

            if word in keywords:

                # NEGATION handling
                if i > 0 and words[i - 1] in NEGATIONS:
                    scores[emotion] -= 3
                else:
                    scores[emotion] += 2

                # intensity boost
                if i > 0 and words[i - 1] in ["very", "so", "extremely", "really"]:
                    scores[emotion] += 1

    best = max(scores, key=scores.get)

    if scores[best] <= 0:
        return "neutral"

    return best


# ----------------------------
# ENCRYPTION
# ----------------------------
def encrypt(data):
    key = AESGCM.generate_key(bit_length=128)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    enc = aes.encrypt(nonce, data, None)
    return enc, key, nonce


# ----------------------------
# UI
# ----------------------------
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
        st.write("Emotion:", emotion)
        st.write(tagged)
    else:
        st.error("Failed to send message ❌")
