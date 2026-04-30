import tkinter as tk
from login_auth import open_login
from donor_mgmt import open_donor_mgmt
from inventory_mgmt import open_inventory
from search_matching import open_search
from blood_request import open_requests
from analytics_reports import open_reports

root = tk.Tk()
root.title("Blood Bank System")
root.geometry("400x500")

def show_dashboard():
    tk.Label(root, text="MAIN DASHBOARD", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Donor Management", width=25, command=open_donor_mgmt).pack(pady=5)
    tk.Button(root, text="Inventory View", width=25, command=open_inventory).pack(pady=5)
    tk.Button(root, text="Search & Matching", width=25, command=open_search).pack(pady=5)
    tk.Button(root, text="Blood Request", width=25, command=open_requests).pack(pady=5)
    tk.Button(root, text="System Reports", width=25, command=open_reports).pack(pady=5)

tk.Button(root, text="START SYSTEM (Login Required)", command=lambda: open_login(show_dashboard), bg="red", fg="white").pack(expand=True)

root.mainloop()