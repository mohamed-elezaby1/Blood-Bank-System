import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_login(on_success):
    win = tk.Toplevel()
    win.title("Login")
    win.geometry("300x250")
    tk.Label(win, text="Username:").pack(pady=5)
    u_ent = tk.Entry(win)
    u_ent.pack()
    tk.Label(win, text="Password:").pack(pady=5)
    p_ent = tk.Entry(win, show="*")
    p_ent.pack()

    def check():
        conn = sqlite3.connect('blood_bank.db')
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (u_ent.get(), p_ent.get())).fetchone()
        conn.close()
        if user:
            messagebox.showinfo("Success", "Welcome Admin!")
            win.destroy()
            on_success()
        else:
            messagebox.showerror("Error", "Wrong Credentials")

    tk.Button(win, text="Login", command=check, bg="blue", fg="white").pack(pady=20)
    