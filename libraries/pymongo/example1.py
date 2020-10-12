# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:33:16 2020

@author: Naga
"""

from pymongo import MongoClient

# Connecting to db server
client = MongoClient('localhost', 27017)


# Getting admin database
db = client.testdb

# Getting collection
test_collection = db.test_collection

# Getting one value
dictionary = test_collection.find_one(
    {'users': ['Mickael', 'MR.Ahmed', 'Moree', 'Foo']})
print(f"find_one: {dictionary}")
print()

# Inserting into collection
data = {"username": "John", "fullName": "John Wick"}
test_collection.insert_one(data)

data = {"username": "John1", "fullName": "John Wick"}
test_collection.insert_one(data)

# Updating: rename
new_data = {"$set": {"username": "Foo"}}
test_collection.update_one(data, update=new_data)

# updating: insert
#query = collection.find_one()
#new_data = {"$addToSet": {"users": {"$each": ['Mickael', "Moree", "Foo"]}}}
#print("Modified:", collection.update_one(query, update=new_data).modified_count)
# Update all
# queries = collection.find() # fetch all documents
#new_data = {"$addToSet": {"users": {"$each": ['Mickael', "Foo"]}}}
# print()
# for _query in queries:
#    print(_query)
#    print("Modified:", collection.update_one(_query, update=new_data).modified_count)


# Creat databse
new_db = client["new_database"]
# New collectin
if new_db.list_collection_names().count("new_collection") == 0:
    new_db.create_collection("new_collection")

new_collection = new_db.new_collection
new_collection.insert_one(data)

# Deleting
# Delete one
test_collection.delete_one({"username": "John1"})
# delete all matching
print("Delete count:", test_collection.delete_many(
    {"username": "John1"}).deleted_count)
