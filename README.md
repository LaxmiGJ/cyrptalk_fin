# 🔐 CrypTalk - Encrypted Messaging Application

CrypTalk is a secure, end-to-end encrypted messaging application with multi-language support and emotion detection. Send encrypted messages with automatic language translation and emotional tagging.

## Features

✨ **Key Features:**
- 🔐 End-to-end encryption using AES-256-GCM
- 🌍 Multi-language support (English, Hindi, Kannada, Tamil, Telugu, Malayalam)
- 😊 Emotion detection (joy, sadness, anger, fear, surprise, confusion, neutral)
- 📧 Compressed message storage
- 🎯 Real-time message delivery

## Project Structure

```
cryptalk/
├── backend.py          # FastAPI backend server for message storage
├── sender.py           # Streamlit app for sending encrypted messages
├── receiver.py         # Streamlit app for receiving encrypted messages
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. Clone the repository:
```bash
git clone https://github.com/LaxmiGJ/cyrptalk_fin.git
cd cyrptalk_fin
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Running Locally

### Terminal 1 - Start Backend Server
```bash
python -m uvicorn backend:app --reload --port 8000
```
Backend will run at: `http://127.0.0.1:8000`

### Terminal 2 - Start Sender App
```bash
streamlit run sender.py
```
Sender will run at: `http://localhost:8501`

### Terminal 3 - Start Receiver App
```bash
streamlit run receiver.py --server.port 8502
```
Receiver will run at: `http://localhost:8502`

## Cloud Deployment

### Deploy on Heroku (Backend)

1. Create a Procfile with:
```
web: uvicorn backend:app --host 0.0.0.0 --port $PORT
```

2. Push to Heroku:
```bash
heroku create cryptalk-backend
git push heroku main
```

### Deploy on Streamlit Cloud (Frontend)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository, branch, and main file
5. Deploy sender and receiver as separate apps

**Sender App URL:**
- Repository: `LaxmiGJ/cyrptalk_fin`
- Main file: `sender.py`

**Receiver App URL:**
- Repository: `LaxmiGJ/cyrptalk_fin`
- Main file: `receiver.py`

## Configuration

### For Streamlit Cloud Deployment

Update backend URL in `sender.py` and `receiver.py`:

```python
# Replace localhost with your Heroku backend URL
BACKEND_URL = "https://your-heroku-backend.herokuapp.com/send"
```

## How It Works

### Sending a Message

1. User enters sender name and receiver name
2. Selects sender's language and receiver's output language
3. Types message
4. Message is:
   - Translated to English
   - Emotion is detected from translated text
   - Tagged with emotion and emoji
   - Compressed using zlib
   - Encrypted using AES-256-GCM
   - Sent to backend server

### Receiving a Message

1. User enters their name
2. Selects output language
3. Backend retrieves encrypted message
4. Message is:
   - Decrypted using stored key and nonce
   - Decompressed
   - Translated to selected language
   - Emotion and emoji are displayed

## Security

- **Encryption:** AES-256-GCM (AEAD cipher)
- **Key Generation:** 128-bit random keys
- **Nonce:** 12-byte random nonces (prevent replay attacks)
- **Message Compression:** zlib compression before encryption

## Technologies Used

- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit
- **Encryption:** cryptography library (AESGCM)
- **Translation:** deep-translator (Google Translate API)
- **Compression:** zlib

## Dependencies

See `requirements.txt` for complete list:
- streamlit
- requests
- fastapi
- uvicorn
- cryptography
- deep-translator

## Demo

### Local Demo
1. Run all three components (Backend, Sender, Receiver)
2. Open Sender at http://localhost:8501
3. Open Receiver at http://localhost:8502
4. Send an encrypted message from Sender
5. Receive and decrypt on Receiver app

### Cloud Demo (After Deployment)
- Sender: `https://[sender-app-name].streamlit.app`
- Receiver: `https://[receiver-app-name].streamlit.app`

## Limitations

- Messages stored in memory (not persistent)
- Single recipient per message
- No authentication/user management yet
- Limited emotion detection keywords

## Future Enhancements

- [ ] Database persistence (PostgreSQL)
- [ ] User authentication
- [ ] Message history
- [ ] File sharing
- [ ] Group messaging
- [ ] ML-based emotion detection
- [ ] Push notifications

## License

This project is open source and available under the MIT License.

## Author

**Laxmi** - [GitHub Profile](https://github.com/LaxmiGJ)

## Support

For issues or questions, please create an issue on [GitHub](https://github.com/LaxmiGJ/cyrptalk_fin/issues)

---

Made with ❤️ for secure communication
