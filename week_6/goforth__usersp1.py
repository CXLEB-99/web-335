"""
Title: <yourLastName>_usersp1.py
Author: <Your Name>
Date: <Current Date>
Description: Python program to connect to MongoDB and perform queries on the users collection.
"""

# Import the necessary library
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.js88e.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the database
db = client['web335DB']

# Access the users collection
users_collection = db['users']

# Display all documents in the users collection
print("\n--- All Users ---")
for user in users_collection.find({}, {"firstName": 1, "lastName": 1, "_id": 0}):
    print(user)

# Display a document where employeeId is 1011
print("\n--- User with employeeId 1011 ---")
user_1011 = users_collection.find_one({"employeeId": "1011"})
print(user_1011)

# Display a document where lastName is Mozart
print("\n--- User with lastName 'Mozart' ---")
user_mozart = users_collection.find_one({"lastName": "Mozart"})
print(user_mozart)
