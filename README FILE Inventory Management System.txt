# Inventory Management System

## Overview

This is a Python-based Inventory Management System that interacts with a MongoDB database to perform CRUD (Create, Read, Update, Delete) operations.

## Requirements

- Python 3.x
- MongoDB
- `pymongo` library

## Setup Instructions

1. **Install MongoDB:**
   - Download and install MongoDB from the [official website](https://www.mongodb.com/try/download/community).
   
2. **Start MongoDB Server:**
   - Run `mongod` in your terminal or command prompt to start the MongoDB server.

3. **Create Database and Collection:**
   - Start the MongoDB shell with `mongo`.
   - Create a database: `use InventoryDB`
   - Create a collection: `db.createCollection("Inventory")`

4. **Install Python Dependencies:**
   - Install the required Python library using pip: `pip install pymongo`

## Running the Script

1. Clone this repository or download the `inventory_management.py` script.

2. Run the script using Python: python inventory_management.py


