import os
import sys

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
        self.save()
        storage_objects.append(self)
        return name + " er nu oprettet som: " + str(id)
    
    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_price(self):
        return self.price


    def set_id(self, id):
        self.id = id
        self.save()
        return "ID er nu sat til: " + str(id)

    def set_name(self, name):
        self.name = name
        self.save()
        return "Navn er nu sat til: " + name

    def set_capacity(self, capacity):
        self.capacity = capacity
        self.save()
        return "Kapacitet er nu sat til: " + str(capacity)

    def set_price(self, price):
        self.price = price
        self.save()
        return "Pris er nu sat til: " + str(price)

    def save(self):
        with open("storage.txt", "a") as file:
            file.write(f"{self.id},{self.name},{self.capacity},{self.price}\n")

    def __str__(self):
        return f"{self.id},{self.name},{self.capacity},{self.price}"


def load():
    storage_objects = []  # Ensure the storage_objects list is initialized empty
    try:
        with open("storage.txt", "r") as file:
            for line in file:
                # Remove any extra whitespace or newlines
                data = line.strip().split(",")

                # Check if data length matches the number of expected fields
                if len(data) == 4:  
                    storage_obj = Storage()
                    storage_obj.set_id(int(data[0]))
                    storage_obj.set_name(data[1])
                    storage_obj.set_capacity(int(data[2]))
                    storage_obj.set_price(float(data[3]))
                    storage_objects.append(storage_obj)
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    except Exception as e:
        print(f"Error loading storage data: {e}")
    return storage_objects


# Example usage:
# Load storage objects from file
storage_objects = load()

# Create a new storage object
new_storage = Storage()
