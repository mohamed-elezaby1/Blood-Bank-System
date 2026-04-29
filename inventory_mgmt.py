import tkinter as tk
import sqlite3

def open_inventory():
    win = tk.Toplevel()
    win.title("Inventory Management")
    win.geometry("300x350")
    conn = sqlite3.connect('blood_bank.db')
    data = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    for item in data:
        tk.Label(win, text=f"Type {item[0]}: {item[1]} Bags").pack(pady=5)