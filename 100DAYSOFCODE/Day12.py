import tkinter as tk
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()

    if amount.isdigit() and category:
        expenses_listbox.insert(tk.END, f"{category}: ₹{amount}")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        error_label.config(text="Please enter valid data!")
root = tk.Tk()
root.title("Simple Expense Tracker")
amount_label = tk.Label(root, text="Expense Amount (₹):")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()
category_label = tk.Label(root, text="Category:")
category_label.pack()
category_entry = tk.Entry(root)
category_entry.pack()
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()
expenses_listbox = tk.Listbox(root, width=80)
expenses_listbox.pack()
error_label = tk.Label(root, text="", fg="red")
error_label.pack()
root.mainloop()




