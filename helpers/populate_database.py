# Populates the data base with products and users

import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost/TestCollection")
db = client["TestDB"]
testProductsCollection = db["testProductsCollection"]
testUsersCollection = db["testUsersCollection"]

print(client.list_database_names())
print(db.list_collection_names())

with open('products.json', 'r') as file:
    products = json.load(file)
    for product in products:
        testProductsCollection.insert_one(product)

with open('users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        testUsersCollection.insert_one(user)

allUsers = testUsersCollection.find({})
allProducts = testProductsCollection.find({})

for user in allUsers:
    print(user)

for product in allProducts:
    print(product)

print("DONE")