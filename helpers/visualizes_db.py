import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost/TestCollection")
db = client["TestDB"]
testProductsCollection = db["testProductsCollection"]
testUsersCollection = db["testUsersCollection"]

allUsers = testUsersCollection.find({})
allProducts = testProductsCollection.find({})

print("USERS")
for user in allUsers:
    print(user)

print("PRODUCTS")
for product in allProducts:
    print(product)

#testProductsCollection.drop()
#testUsersCollection.drop()

print("DONE")