# 🔐 CrypTalk - Encrypted Messaging Application

CrypTalk is a secure, end-to-end encrypted messaging application with multi-language support and emotion detection. Send encrypted messages with automatic language translation and emotional tagging.

## Features

✨ **Key Features:**
- 🔐 End-to-end encryption using AES-256-GCM
- 🌍 Multi-language support (English, Hindi, Kannada, Tamil, Telugu, Malayalam)
- 😊 Emotion detection (joy, sadness, anger, fear, surprise, confusion, neutral)
- 📧 SQLite database for persistent message storage
- 🎯 Real-time message delivery
- ☁️ Single-app cloud deployment on Streamlit Cloud

## Project Structure

```
cryptalk/
├── sender.py           # Streamlit app for sending encrypted messages
├── receiver.py         # Streamlit app for receiving encrypted messages
├── db.py              # SQLite database module
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

1. Clone the repository:
```bash
git clone https://github.com/LaxmiGJ/cyrptalk_fin.git
cd cyrptalk_fin
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

### Terminal 1 - Start Sender App
```bash
streamlit run sender.py
```
→ http://localhost:8501

### Terminal 2 - Start Receiver App
```bash
streamlit run receiver.py --server.port 8502
```
→ http://localhost:8502

Both apps share the same SQLite database.

## Cloud Deployment - Streamlit Cloud (FREE!)

### Quick Setup

1. **Push to GitHub** - Ensure all files including `db.py` are committed
2. **Deploy Sender:**
   - Go to https://streamlit.io/cloud
   - New App → `LaxmiGJ/cyrptalk_fin` → `sender.py` → Deploy
3. **Deploy Receiver:**
   - New App → `LaxmiGJ/cyrptalk_fin` → `receiver.py` → Deploy

### Access Your Apps
- **Sender:** `https://cryptalk-sender.streamlit.app`
- **Receiver:** `https://cryptalk-receiver.streamlit.app`

Share these links with anyone!

## How It Works

### Sending
1. Enter sender/receiver name & message
2. Select language
3. Message is encrypted, tagged with emotion, compressed
4. Stored in SQLite database

### Receiving
1. Enter your name
2. Latest encrypted message is retrieved
3. Decrypted, decompressed, translated
4. Emotion detected from sender

## Security

- 🔐 AES-256-GCM encryption
- 🔑 128-bit random keys
- 🎲 12-byte random nonces
- 📦 zlib compression

## Technologies

- Streamlit (frontend)
- SQLite (database)
- cryptography (AES-256-GCM)
- deep-translator (Google Translate)

## Dependencies

```
streamlit
requests
cryptography
deep-translator
```

---

Made with ❤️ for secure communication
