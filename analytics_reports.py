import tkinter as tk
import sqlite3

def open_reports():
    win = tk.Toplevel()
    win.title("System Reports")
    win.geometry("300x200")
    conn = sqlite3.connect('blood_bank.db')
    count = conn.execute("SELECT COUNT(*) FROM donors").fetchone()[0]
    total = conn.execute("SELECT SUM(count) FROM inventory").fetchone()[0]
    conn.close()
    tk.Label(win, text=f"Total Donors: {count}", font=("Arial", 12)).pack(pady=10)
    tk.Label(win, text=f"Total Bags: {total}", font=("Arial", 12)).pack(pady=10)