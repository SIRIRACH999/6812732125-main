import os
import sqlite3
from pathlib import Path

from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "apple.db"

INITIAL_USERS = [
    ("#", "6812732120", "นาย", "มนพระกาญจน์", "คําเลอ"),
    ("#", "6812732123", "นาย", "วายุ", "บัวศรี"),
    ("#", "6812732122", "นาย", "รฐนันท์", "วสุนันต์"),
    ("#", "6812732125", "นาย", "สิริราช", "โทนัน"),
    ("#", "6812732126", "นาย", "สิวะดล", "รักชาติ"),
    ("#", "6812732104", "นาย", "ญาณภัฒน์", "วะนิลา"),
    ("#", "6812732118", "นาย", "ภูมิรัตน์", "แซ่โง้ว"),
]

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def ensure_user_table():
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                runnumber TEXT NOT NULL DEFAULT '#',
                studentID TEXT,
                prefix TEXT,
                Firstname TEXT,
                Lastname TEXT
            )
        """)

        for runnumber, studentid, prefix, firstname, lastname in INITIAL_USERS:
            row = conn.execute(
                "SELECT 1 FROM users WHERE studentID = ?",
                (studentid,),
            ).fetchone()
            if row is None:
                conn.execute(
                    """
                    INSERT INTO users (runnumber, studentID, prefix, Firstname, Lastname)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (runnumber, studentid, prefix, firstname, lastname),
                )

        conn.commit()
    finally:
        conn.close()

def dashboard(request):
    ensure_user_table()

    conn = get_connection()
    try:
        users = conn.execute("""
            SELECT studentID, prefix, Firstname, Lastname
            FROM users
            WHERE runnumber = ?
            ORDER BY studentID
        """, ("#",)).fetchall()
    finally:
        conn.close()

    return render(request, "index.html", {"users": users})