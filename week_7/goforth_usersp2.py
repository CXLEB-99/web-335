"""
Title: <yourLastName>_usersp2.py
Author: Caleb Goforth 
Date: 2/23/2025
Description: Hands-On 5.2 - CRUD operations in MongoDB using Python
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to the database
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client['web335DB']

# Step 3: Create a new user document
new_user = {
    "firstName": "John",
    "lastName": "Doe",
    "employeeId": "1020",
    "email": "johndoe@example.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
new_user_id = db.users.insert_one(new_user).inserted_id
print(f"User created with ID: {new_user_id}")

# Step 4: Prove the document was created
print("Document created:")
print(db.users.find_one({"employeeId": "1020"}))

# Step 5: Update the email address of the document
db.users.update_one(
    {"employeeId": "1020"},
    {
        "$set": {
            "email": "john.doe@newdomain.com"
        }
    }
)

# Step 6: Prove the document was updated
print("Document after update:")
print(db.users.find_one({"employeeId": "1020"}))

# Step 7: Delete the document
result = db.users.delete_one({"employeeId": "1020"})
print(f"Deleted {result.deleted_count} document(s).")

# Step 8: Prove the document was deleted
print("Document after deletion:")
print(db.users.find_one({"employeeId": "1020"}))
