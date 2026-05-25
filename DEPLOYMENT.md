# 🚀 CrypTalk - Streamlit Cloud Deployment Guide

## What We've Done

✅ Refactored codebase to use SQLite database (no backend needed)
✅ Removed FastAPI/Uvicorn dependencies
✅ Both sender and receiver apps share the same SQLite database
✅ Ready for cloud deployment on Streamlit Cloud

## Files Changed

- `sender.py` → Now uses SQLite via `db.py`
- `receiver.py` → Now uses SQLite via `db.py`
- `db.py` → NEW: SQLite database module
- `requirements.txt` → Simplified (no fastapi, uvicorn)
- `backend.py` → No longer needed (can be deleted)
- `Procfile` → No longer needed (can be deleted)
- `runtime.txt` → No longer needed (can be deleted)

## Local Testing

### Test Sender & Receiver Locally

```bash
# Terminal 1
streamlit run sender.py

# Terminal 2 (new terminal)
streamlit run receiver.py --server.port 8502
```

Then:
1. Send a message from Sender (http://localhost:8501)
2. Receive on Receiver (http://localhost:8502)
3. Check that message appears in `cryptalk_messages.db`

## Deployment to Streamlit Cloud (FREE)

### Step 1: Push Code to GitHub

```bash
cd c:\Users\Laxmi\Downloads\cryptalk
git add .
git commit -m "Refactor to SQLite - remove FastAPI backend"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

#### Deploy SENDER App:

1. Go to https://streamlit.io/cloud
2. Click **"New app"**
3. Fill in:
   - **Repository:** `LaxmiGJ/cyrptalk_fin`
   - **Branch:** `main`
   - **Main file path:** `sender.py`
4. Click **Deploy**
5. Wait for deployment (2-3 minutes)
6. Copy the URL (e.g., `https://cryptalk-sender.streamlit.app`)

#### Deploy RECEIVER App:

1. Click **"New app"** again
2. Fill in:
   - **Repository:** `LaxmiGJ/cyrptalk_fin`
   - **Branch:** `main`
   - **Main file path:** `receiver.py`
3. Click **Deploy**
4. Copy the URL (e.g., `https://cryptalk-receiver.streamlit.app`)

## Your Final URLs

| Component | URL |
|-----------|-----|
| **Sender** | https://cryptalk-sender.streamlit.app |
| **Receiver** | https://cryptalk-receiver.streamlit.app |

## How to Use

1. **Send Message:** Open Sender URL
   - Enter your name (sender)
   - Enter recipient name (receiver)
   - Select language
   - Type message
   - Click "Send"

2. **Receive Message:** Open Receiver URL
   - Enter your name
   - Click "Receive"
   - Message appears decrypted with emotion

## Important Notes

✅ **Database File:** SQLite database is stored on Streamlit Cloud's filesystem
✅ **No Auth Needed:** Anyone with the links can use it
✅ **Message Sharing:** Both apps share the same database
✅ **Free Forever:** Streamlit Cloud has a generous free tier

## Troubleshooting

**"No message found"**
- Make sure receiver name matches exactly
- Message was sent to that receiver name

**App won't deploy**
- Check that all files are on GitHub
- Ensure `db.py` is included
- Check requirements.txt has no errors

**Connection issues**
- Streamlit Cloud has 30-min timeout for free tier
- Refresh the page and try again

## Need to Update?

Just push changes to GitHub:
```bash
git add .
git commit -m "Fix: ..."
git push origin main
```

Streamlit Cloud will auto-redeploy!

## Clean Up (Optional)

These files are no longer needed (can delete):
- `backend.py`
- `Procfile`
- `runtime.txt`

---

🎉 Your CrypTalk app is now live on the cloud!
