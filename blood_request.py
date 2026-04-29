import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_requests():
    win = tk.Toplevel()
    win.title("Blood Request")
    win.geometry("300x200")
    tk.Label(win, text="Request Type:").pack()
    ent = tk.Entry(win)
    ent.pack()

    def process():
        t = ent.get().upper()
        conn = sqlite3.connect('blood_bank.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE inventory SET count = count - 1 WHERE blood_type=? AND count > 0", (t,))
        if cursor.rowcount > 0:
            conn.commit()
            messagebox.showinfo("Success", "Request Dispatched")
        else:
            messagebox.showerror("Error", "Out of Stock")
        conn.close()

    tk.Button(win, text="Process Order", command=process).pack(pady=10)
    