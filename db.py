"""
Database module for CrypTalk using SQLite
Handles message storage and retrieval
"""

import sqlite3
import os
from datetime import datetime
import json

DB_PATH = "cryptalk_messages.db"

def init_db():
    """Initialize the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            encrypted TEXT NOT NULL,
            key TEXT NOT NULL,
            nonce TEXT NOT NULL,
            sender_lang TEXT,
            receiver_lang TEXT,
            emotion TEXT,
            tagged_text TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def store_message(sender, receiver, encrypted, key, nonce, sender_lang, receiver_lang, emotion, tagged_text):
    """Store a message in the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO messages 
        (sender, receiver, encrypted, key, nonce, sender_lang, receiver_lang, emotion, tagged_text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (sender, receiver, encrypted, key, nonce, sender_lang, receiver_lang, emotion, tagged_text))
    
    conn.commit()
    conn.close()
    return True

def get_latest_message(receiver):
    """Get the latest message for a receiver"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT sender, receiver, encrypted, key, nonce, sender_lang, receiver_lang, emotion, tagged_text, timestamp
        FROM messages
        WHERE receiver = ?
        ORDER BY timestamp DESC
        LIMIT 1
    ''', (receiver,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            "sender": result[0],
            "receiver": result[1],
            "encrypted": result[2],
            "key": result[3],
            "nonce": result[4],
            "sender_lang": result[5],
            "receiver_lang": result[6],
            "emotion": result[7],
            "tagged_text": result[8],
            "timestamp": result[9]
        }
    return None

def get_all_messages_for_receiver(receiver):
    """Get all messages for a receiver"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT sender, receiver, encrypted, key, nonce, sender_lang, receiver_lang, emotion, tagged_text, timestamp
        FROM messages
        WHERE receiver = ?
        ORDER BY timestamp DESC
    ''', (receiver,))
    
    results = cursor.fetchall()
    conn.close()
    
    messages = []
    for result in results:
        messages.append({
            "sender": result[0],
            "receiver": result[1],
            "encrypted": result[2],
            "key": result[3],
            "nonce": result[4],
            "sender_lang": result[5],
            "receiver_lang": result[6],
            "emotion": result[7],
            "tagged_text": result[8],
            "timestamp": result[9]
        })
    return messages

def delete_message(sender, receiver):
    """Delete a message after reading (optional)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM messages
        WHERE sender = ? AND receiver = ?
    ''', (sender, receiver))
    
    conn.commit()
    conn.close()
    return True

# Initialize database on module import
init_db()
