import tkinter as tk
from tkinter import messagebox
from datetime import datetime
tasks = []
# Function to add a new task
def add_task():
    task_name = task_entry.get()
    task_deadline = deadline_entry.get()
    if not task_name or not task_deadline:
        messagebox.showwarning("Input Error", "Please provide both task and deadline.")
        return
    try:
        deadline_date = datetime.strptime(task_deadline, "%d/%m/%Y %H:%M")
        tasks.append((task_name, deadline_date))
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        update_task_list()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter the deadline in 'DD/MM/YYYY HH:MM' format.")
def update_task_list():
    task_list.delete(0, tk.END)
    now = datetime.now()
    for task, deadline in tasks:
        remaining_time = deadline - now
        task_list.insert(tk.END, f"{task} - {deadline.strftime('%d/%m/%Y %H:%M')} ({remaining_time})")
# Function to check for upcoming deadlines
def check_deadlines():
    now = datetime.now()
    upcoming_tasks = [task for task, deadline in tasks if 0 < (deadline - now).total_seconds() < 3600]
    if upcoming_tasks:
        messagebox.showinfo("Reminder", f"Upcoming Tasks:\n" + "\n".join(upcoming_tasks))
    root.after(60000, check_deadlines)  # Check every minute
# Set up the GUI
root = tk.Tk()
root.title("Task Reminder App")
# Task entry field
tk.Label(root, text="Task:").grid(row=0, column=0, padx=10, pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=10, pady=5)
# Deadline entry field
tk.Label(root, text="Deadline (DD/MM/YYYY HH:MM):").grid(row=1, column=0, padx=10, pady=5)
deadline_entry = tk.Entry(root, width=30)
deadline_entry.grid(row=1, column=1, padx=10, pady=5)
# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=2, column=1, pady=10)
# Task list
task_list = tk.Listbox(root, width=50, height=10)
task_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
# Check deadlines periodically
root.after(60000, check_deadlines)  # Check deadlines every minute
# Start the GUI
root.mainloop()
