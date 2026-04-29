import tkinter as tk
from tkinter import messagebox

def open_search():
    win = tk.Toplevel()
    win.title("Compatibility Check")
    win.geometry("300x200")
    tk.Label(win, text="Patient Blood Type:").pack()
    ent = tk.Entry(win)
    ent.pack()

    def check():
        res = "Matches: O-, " + ent.get().upper()
        messagebox.showinfo("Matching Result", res)

    tk.Button(win, text="Check Match", command=check).pack(pady=10)