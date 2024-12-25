def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: ₹"))
    with open("expenses.txt", "a") as file:
        file.write(f"{description},{amount}\n")
    print("Expense added successfully!")
def view_expenses():
    total = 0
    print("\nExpenses:")
    print("-" * 20)
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                description, amount = line.strip().split(",")
                print(f"{description}: ₹{amount}")
                total += float(amount)
    except FileNotFoundError:
        print("No expenses recorded yet.")
    print("-" * 20)
    print(f"Total: ₹{total}\n")
while True:
    print("1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting Expense Tracker.Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")







