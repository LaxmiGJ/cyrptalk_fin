import streamlit as st
from deep_translator import GoogleTranslator
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import zlib
from db import get_latest_message, get_all_messages_for_receiver

LANG = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

def decrypt(enc, key, nonce):
    aes = AESGCM(bytes.fromhex(key))
    return aes.decrypt(bytes.fromhex(nonce), bytes.fromhex(enc), None)

st.title("📩 CrypTalk Receiver")

receiver_name = st.text_input("Enter Receiver Name")
chosen_lang = st.selectbox("Choose Output Language", list(LANG.keys()))

if st.button("Receive"):

    data = get_latest_message(receiver_name)

    if data is None:
        st.warning("No message found ❌")
        st.stop()

    decrypted = decrypt(
        data["encrypted"],
        data["key"],
        data["nonce"]
    )

    text = zlib.decompress(decrypted).decode()

    if "] " in text:
        tag, msg = text.split("] ", 1)
    else:
        tag, msg = "", text

    translated = GoogleTranslator(
        source="en",
        target=LANG[chosen_lang]
    ).translate(msg)

    st.subheader("📨 Message Output")

    st.write("Sender:", data["sender"])
    st.write("Emotion:", data["emotion"])

    st.markdown("---")

    st.write("Original:")
    st.success(msg)

    st.write("Translated:")
    st.info(f"{tag}] {translated}" if tag else translated)
