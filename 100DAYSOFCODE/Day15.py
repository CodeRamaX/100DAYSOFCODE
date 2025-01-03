from tkinter import Tk, Label, Button

def increase_count():
    global count
    count += 1
    count_label.config(text=f"Count: {count}")

def reset_count():
    global count
    count = 0
    count_label.config(text=f"Count: {count}")

root = Tk()
root.title("Click Counter")

count = 0

count_label = Label(root, text=f"Count: {count}", font=("Arial", 24))
count_label.pack(pady=20)

click_button = Button(root, text="Click Me!", font=("Arial", 14), command=increase_count)
click_button.pack(pady=10)

reset_button = Button(root, text="Reset", font=("Arial", 14), command=reset_count)
reset_button.pack(pady=10)

root.geometry("300x200")

root.mainloop()












