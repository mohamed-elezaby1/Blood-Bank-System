import sqlite3
import os

def init_db():
    # Remove old DB to ensure clean update
    if os.path.exists('blood_bank.db'):
        os.remove('blood_bank.db')
    
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    
    # 1. System Users
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
    
    # 2. Donors Records
    cursor.execute('CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, b_type TEXT)')
    
    # 3. Inventory Stock
    cursor.execute('CREATE TABLE IF NOT EXISTS inventory (blood_type TEXT PRIMARY KEY, count INTEGER)')
    
    # Starting Stock Values
    initial_stock = [('A+', 15), ('O-', 4), ('B+', 8), ('AB+', 10), ('A-', 5), ('B-', 3), ('O+', 12), ('AB-', 2)]
    cursor.executemany("INSERT INTO inventory VALUES (?,?)", initial_stock)
    
    conn.commit()
    conn.close()
    print("Database Reset & Initialized Successfully!")

if __name__ == "__main__":
    init_db()