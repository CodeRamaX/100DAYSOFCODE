import tkinter as tk
from tkinter import ttk
def save_registration():
    name = name_entry.get()
    reg_no = reg_no_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    sport = sport_combobox.get()

    if name and reg_no and email and phone and sport:
        with open("student_registration.txt", "a") as file:
            file.write(f"Name: {name}, Registration No: {reg_no}, Email: {email}, Phone: {phone}, Sport: {sport}\n")
        status_label.config(text="Registration saved successfully!", fg="green")
        name_entry.delete(0, tk.END)
        reg_no_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        sport_combobox.set('')
    else:
        status_label.config(text="Please fill all fields!", fg="red")

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")

title_label = tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

name_label = tk.Label(root, text="Name:", font=("Arial", 12))
name_label.pack(anchor="w", padx=20, pady=5)
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(padx=20)

reg_no_label = tk.Label(root, text="Registration No:", font=("Arial", 12))
reg_no_label.pack(anchor="w", padx=20, pady=5)
reg_no_entry = tk.Entry(root, width=30, font=("Arial", 12))
reg_no_entry.pack(padx=20)

email_label = tk.Label(root, text="Email:", font=("Arial", 12))
email_label.pack(anchor="w", padx=20, pady=5)
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack(padx=20)

phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12))
phone_label.pack(anchor="w", padx=20, pady=5)
phone_entry = tk.Entry(root, width=30, font=("Arial", 12))
phone_entry.pack(padx=20)

sport_label = tk.Label(root, text="Sport of Interest:", font=("Arial", 12))
sport_label.pack(anchor="w", padx=20, pady=5)
sport_combobox = ttk.Combobox(root, values=["Cricket", "Football", "Basketball", "Tennis", "Badminton"], font=("Arial", 12))
sport_combobox.pack(padx=20)

submit_button = tk.Button(root, text="Submit", command=save_registration, font=("Arial", 12), bg="lightblue")
submit_button.pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack()

root.mainloop()


