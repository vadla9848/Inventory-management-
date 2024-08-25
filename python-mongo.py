from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['InventoryDB']
collection = db['Inventory']

# Ensure the 'item_id' field is unique by creating an index (if not already created)
collection.create_index("item_id", unique=True)

def add_item(item_id, name, quantity, price, category):
    item = {
        "item_id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    }
    try:
        collection.insert_one(item)
        print(f"Item {name} added successfully.")
    except DuplicateKeyError:
        print(f"Item with item_id {item_id} already exists. Please use a unique item_id.")
    except PyMongoError as e:
        print(f"An error occurred: {e}")

def view_items():
    try:
        items = collection.find()
        for item in items:
            print(item)
    except PyMongoError as e:
        print(f"An error occurred: {e}")

def update_item(item_id, update_data):
    try:
        result = collection.update_one({"item_id": item_id}, {"$set": update_data})
        if result.matched_count > 0:
            print(f"Item {item_id} updated successfully.")
        else:
            print(f"Item with item_id {item_id} not found.")
    except PyMongoError as e:
        print(f"An error occurred: {e}")

def delete_item(item_id):
    try:
        result = collection.delete_one({"item_id": item_id})
        if result.deleted_count > 0:
            print(f"Item {item_id} deleted successfully.")
        else:
            print(f"Item with item_id {item_id} not found.")
    except PyMongoError as e:
        print(f"An error occurred: {e}")

def search_item(query):
    try:
        results = collection.find(query)
        for result in results:
            print(result)
    except PyMongoError as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Add new items
    add_item(1, "Laptop", 10, 800, "electronics")
    add_item(2, "Shirt", 50, 20, "clothing")
    add_item(3, "bike", 80, 50000, "bike electronics")
    
    
    # View all items
    print("\nInventory Items:")
    view_items()
    
    # Update an item
    update_item(1, {"quantity": 15, "price": 750})
    update_item(2, {"quantity": 18, "price": 800})
    update_item(3, {"quantity": 30, "price": 200})
    
    # View all items after update
    print("\nUpdated Inventory Items:")
    view_items()
    
    # Search for an item by category
    print("\nSearch Results:")
    search_item({"category": "electronics"})
    
    # Delete an item
    delete_item(3)
    
    # View all items after deletion
    print("\nFinal Inventory Items:")
    view_items()


