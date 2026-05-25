"""
CrypTalk - Main entry point for Streamlit Cloud deployment
This file allows easy deployment on Streamlit Cloud
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# You can use URL parameters to decide which app to show
# Example: ?app=sender or ?app=receiver

import streamlit as st

st.set_page_config(
    page_title="CrypTalk",
    page_icon="🔐",
    layout="centered"
)

# Show home page or redirect to specific app
st.title("🔐 CrypTalk - Encrypted Messaging")

col1, col2 = st.columns(2)

with col1:
    if st.button("📤 Send Message", use_container_width=True, key="send_btn"):
        st.switch_page("pages/sender.py")

with col2:
    if st.button("📩 Receive Message", use_container_width=True, key="receive_btn"):
        st.switch_page("pages/receiver.py")

st.markdown("---")

st.info("""
### About CrypTalk
CrypTalk is a secure, end-to-end encrypted messaging application with:
- 🔐 AES-256-GCM encryption
- 🌍 Multi-language support
- 😊 Emotion detection
- ✨ Automatic translation

**Your messages are encrypted end-to-end. Only the intended recipient can decrypt them.**
""")
