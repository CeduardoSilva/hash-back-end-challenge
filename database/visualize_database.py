# Populates the main data base and the test data base with products and users

import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["MainDB"]
#testDB = client["TestDB"]

productsCollection = db["productsCollection"]
usersCollection = db["usersCollection"]

#testProductsCollection = testDB["testProductsCollection"]
#testUsersCollection = testDB["testUsersCollection"]

allUsers = usersCollection.find({})
allProducts = productsCollection.find({})

#allTestUsers = testUsersCollection.find({})
#allTestProducts = testProductsCollection.find({})

print("MainDB")
for user in allUsers:
    print(user)

for product in allProducts:
    print(product)

#print("TestDB")
#for user in allTestUsers:
#    print(user)

#for product in allTestProducts:
#    print(product)

print("DONE")