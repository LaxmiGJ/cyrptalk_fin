# 🚀 QUICK START - Deploy CrypTalk Now!

## 5-Minute Setup

### Option A: GitHub Desktop (No Git Command Line)

1. **Download GitHub Desktop** → https://desktop.github.com
2. Sign in with your GitHub account
3. **File** → **Clone Repository**
4. Search: `LaxmiGJ/cyrptalk_fin` → Clone
5. Copy all files from `c:\Users\Laxmi\Downloads\cryptalk\` to cloned folder
6. In GitHub Desktop:
   - Write message: `"Refactor: Use SQLite instead of FastAPI"`
   - Click **Commit to main**
   - Click **Push origin**

### Option B: Manual GitHub Upload

1. Go to https://github.com/LaxmiGJ/cyrptalk_fin
2. Click **Add file** → **Upload files**
3. Upload these files:
   ```
   sender.py
   receiver.py
   db.py
   requirements.txt
   .gitignore
   README.md
   DEPLOYMENT.md
   ```
4. Commit message: `"Refactor: Use SQLite instead of FastAPI"`

## Deploy to Streamlit Cloud

### Step 1: Go to Streamlit Cloud
https://streamlit.io/cloud

### Step 2: Deploy Sender App
- **New app**
- Repository: `LaxmiGJ/cyrptalk_fin`
- Branch: `main`
- Main file: `sender.py`
- Deploy

⏳ Wait 2-3 minutes...

**SENDER URL:** Copy this link

### Step 3: Deploy Receiver App
- **New app** again
- Repository: `LaxmiGJ/cyrptalk_fin`
- Branch: `main`
- Main file: `receiver.py`
- Deploy

⏳ Wait 2-3 minutes...

**RECEIVER URL:** Copy this link

## Test It!

1. Open **Sender URL**
   - Name: "Alice"
   - Receiver: "Bob"
   - Message: "Hello World"
   - Click Send

2. Open **Receiver URL** (in another tab)
   - Name: "Bob"
   - Click Receive
   - See encrypted message decrypted!

## Share With Others

Send both links:
- **Send messages:** [SENDER_URL]
- **Receive messages:** [RECEIVER_URL]

Anyone can use it! 🎉

## That's It!

Your CrypTalk app is live on the cloud with:
- ✅ End-to-end encryption
- ✅ Multi-language support
- ✅ Emotion detection
- ✅ Free hosting forever

---

**Questions?** See `DEPLOYMENT.md` for detailed guide
