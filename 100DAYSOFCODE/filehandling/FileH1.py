file_path = "feedback.txt"
def read_feedback():
    with open(file_path, 'r') as file:
        feedback = file.readlines()
    print("\nCustomer Feedback:")
    for entry in feedback:
        print(entry.strip())
def add_feedback():
    new_feedback = input("\nEnter your feedback: ")
    with open(file_path, 'a') as file:
        file.write(new_feedback + '\n')
    print("Feedback added successfully!")
def analyze_feedback():
    feedback = read_feedback()
    print(f"\nTotal Feedback Entries: {len(feedback)}")
def main():
    while True:
        print("\n--- Customer Feedback Manager ---")
        print("1. Read Feedback")
        print("2. Add Feedback")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            read_feedback()
        elif choice == '2':
            add_feedback()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





    








































