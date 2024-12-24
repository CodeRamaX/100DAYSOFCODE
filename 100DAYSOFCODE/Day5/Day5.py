def process_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as filename:
            numbers = []
            for line in filename:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Skipping invalid data: {line.strip()}")
        result = sum(numbers)
        with open(output_file, 'w') as outfile:
            outfile.write(f"Sum of numbers: {result}\n")
        print(f"Result written to {output_file}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Example usage
process_numbers("numbers.txt", "output.txt")



def inventory_management(file):
    try:
        while True:
            print("\nInventory Management")
            print("1. View Inventory\n2. Add Item\n3. Remove Item\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                with open(file, 'r') as f:
                    inventory = f.read().strip()
                    print("\nCurrent Inventory:\n" + (inventory if inventory else "No items"))
            elif choice == '2':
                item = input("Enter the item to add: ")
                with open(file, 'a') as f:
                    f.write(item + '\n')
                print(f"{item} added to inventory.")
            elif choice == '3':
                item = input("Enter the item to remove: ")
                with open(file, 'r') as f:
                    items = f.readlines()
                if item + '\n' in items:
                    items.remove(item + '\n')
                    with open(file, 'w') as f:
                        f.writelines(items)
                    print(f"{item} removed from inventory.")
                else:
                    print(f"Error: {item} not found in the inventory.")
            elif choice == '4':
                print("Exiting inventory management.")
                break
            else:
                print("Invalid option. Please try again.")
    except FileNotFoundError:
        print(f"Error: {file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Example usage
inventory_management("inventory.txt")




