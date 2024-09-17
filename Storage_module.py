import os

# A global list to store all storage objects
storage_objects = []

class Storage:
    def __init__(self):
        self.id = int()
        self.name = str()
        self.capacity = int()
        self.price = float()

    def get_id(self):
        return self.id

    def create_storage(self, id, name, capacity, price):
        # Check if the item already exists
        for obj in storage_objects:
            if obj.get_id() == id:
                return "Allerede eksisterende"
        
        self.id = id
        self.name = name
        self.capacity = capacity
        self.price = price
        storage_objects.append(self)
        self.save_all()  # Save all objects to the file after appending
        return name + " er nu oprettet som: " + str(id)
    
    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_price(self):
        return self.price

    def set_id(self, id):
        self.id = id
        self.save_all()  # Save all objects after setting
        return "ID er nu sat til: " + str(id)

    def set_name(self, name):
        self.name = name
        self.save_all()  # Save all objects after setting
        return "Navn er nu sat til: " + name

    def set_capacity(self, capacity):
        self.capacity = capacity
        self.save_all()  # Save all objects after setting
        return "Kapacitet er nu sat til: " + str(capacity)

    def set_price(self, price):
        self.price = price
        self.save_all()  # Save all objects after setting
        return "Pris er nu sat til: " + str(price)

    def save_all(self):
        """Save all storage objects to the file."""
        with open("storage.txt", "w") as file:
            for obj in storage_objects:
                file.write(f"{obj.id},{obj.name},{obj.capacity},{obj.price}\n")

    def __str__(self):
        return f"{self.id},{self.name},{self.capacity},{self.price}"

def load():
    global storage_objects  # Ensure we modify the global list
    storage_objects.clear()  # Clear the global list before loading
    try:
        with open("storage.txt", "r") as file:
            for line in file:
                # Remove any extra whitespace or newlines
                data = line.strip().split(",")

                # Check if data length matches the number of expected fields
                if len(data) == 4:  
                    storage_obj = Storage()
                    storage_obj.id = int(data[0])
                    storage_obj.name = data[1]
                    storage_obj.capacity = int(data[2])
                    storage_obj.price = float(data[3])
                    storage_objects.append(storage_obj)
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    except Exception as e:
        print(f"Error loading storage data: {e}")
    return storage_objects

def edit_storage_item():
    # List all storage items before editing
    if not storage_objects:
        print("No storage items found.")
        return

    print("\n--- List of All Storage Items ---")
    # Print table headers
    print(f"{'ID':<10}{'Name':<20}{'In Stock':<15}{'Price':<10}")
    print("-" * 70)

    # Print each storage object's details
    for storage in storage_objects:
        print(f"{storage.get_id():<10}{storage.get_name():<20}{storage.get_capacity():<15}{storage.get_price():<10.2f}")

    try:
        id_to_edit = int(input("Enter the ID of the storage item you want to edit: "))

        # Find the storage object with the given ID
        for storage in storage_objects:
            if storage.get_id() == id_to_edit:
                # Allow the user to edit each attribute
                new_name = input(f"Enter new name (current: {storage.get_name()}): ") or storage.get_name()
                new_capacity = input(f"Enter new capacity (current: {storage.get_capacity()}): ") or storage.get_capacity()
                new_price = input(f"Enter new price (current: {storage.get_price()}): ") or storage.get_price()

                # Update the storage object with the new values
                storage.set_name(new_name)
                storage.set_capacity(int(new_capacity))
                storage.set_price(float(new_price))

                # Confirm the update
                print(f"Storage item with ID {id_to_edit} has been updated.")
                return

        print("Storage item with the given ID not found.")

    except ValueError:
        print("Invalid input. Please enter the correct data type.")

# Load storage objects from file when the module is loaded
storage_objects = load()


# +------------------+
# |      Storage     |   <-- Hovedklasse til at repræsentere et lagerobjekt
# +------------------+
# | - id: int        |   <-- Attributter (private egenskaber)
# | - name: str      |
# | - capacity: int  |
# | - price: float   |
# +------------------+
# | + get_id(): int  |   <-- Offentlige metoder
# | + get_name(): str|
# | + get_capacity():int|
# | + get_price(): float|
# | + set_id(id: int): str|
# | + set_name(name: str): str|
# | + set_capacity(capacity: int): str|
# | + set_price(price: float): str|
# | + save_all(): void|
# +------------------+