# database.py
import sqlite3

DB_NAME = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def add_expense(date, description, amount, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, description, amount, category)
        VALUES (?, ?, ?, ?)
    """, (date, description, amount, category))
    conn.commit()
    conn.close()

def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows
