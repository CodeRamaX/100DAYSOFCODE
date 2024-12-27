tasks = []
def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added!")
def view_tasks():
    if not tasks:
        print("Your To-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def mark_task_completed():
    view_tasks()
    task_number = int(input("\nEnter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] += " (Completed)"
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number!")
def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            print("Exiting!")
            break
        else:
            print("Invalid option. Please choose a valid number.")
if __name__ == "__main__":
    main()

    



