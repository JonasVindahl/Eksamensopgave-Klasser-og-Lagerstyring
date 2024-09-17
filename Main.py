from Storage_module import Storage, load, storage_objects, edit_storage_item  # Updated import
import random
import os

def clear_screen():
    # Clear screen command based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n--- Storage Management System ---")
    print("1. Create New Storage Item")
    print("2. List All Storage Items")
    print("3. Edit Storage Item")
    print("4. Exit")

def create_new_storage():
    clear_screen()
    try:
        while True:
            id = int(input("Enter Storage ID (Leave blank for random): ") or random.randint(1000, 9999))
            if any(storage.get_id() == id for storage in storage_objects):
                print("ID already exists. Please enter a different ID.")
                continue

            name = input("Enter Storage Name: ")
            capacity = int(input("Enter Capacity: " or 0))
            price = float(input("Enter Price: " or 0.0))

            new_storage = Storage()
            message = new_storage.create_storage(id, name, capacity, price)
            print(message)
            break  # Exit the loop after successful creation
    except ValueError:
        print("Invalid input. Please enter the correct data type.")

def list_all_storage_items():
    clear_screen()
    if not storage_objects:
        print("No storage items found.")
    else:
        print("\n--- List of All Storage Items ---")
        # Print table headers
        print(f"{'ID':<10}{'Name':<20}{'In Stock':<15}{'Price':<10}")
        print("-" * 70)
        
        # Print each storage object's details
        for storage in storage_objects:
            print(f"{storage.get_id():<10}{storage.get_name():<20}{storage.get_capacity():<15}{storage.get_price():<10.2f}")

def main():
    while True:
        display_menu()
        user_choice = input("Select an option (1-4): ")

        try:
            choice = int(user_choice)
            if choice == 1:
                create_new_storage()
            elif choice == 2:
                list_all_storage_items()
            elif choice == 3:
                edit_storage_item()
            elif choice == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()





