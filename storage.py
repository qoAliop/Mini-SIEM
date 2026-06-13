import sqlite3

DB_FILE = "incidents.db"

def init_db():
    """Create the incidents table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            type TEXT,
            severity TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

import sqlite3
from datetime import datetime

DB_FILE = "incidents.db"

def init_db():
    """Create the incidents table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            type TEXT,
            severity TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_incidents():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT time, type, severity, description FROM incidents ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return [{"time": r[0], "type": r[1], "severity": r[2], "description": r[3]} for r in rows]

def clear_incidents():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM incidents")
    conn.commit()
    conn.close()

def add_incident(type_, severity, description):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO incidents (time, type, severity, description) VALUES (?, ?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), type_, severity, description)
    )
    conn.commit()
    conn.close()
