# Populates the data base with products and users

import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost/TestCollection")

db = client["TestDB"]
businessLogicDB = client["BusinessLogicDB"]

testProductsCollection = db["testProductsCollection"]
testUsersCollection = db["testUsersCollection"]

specialDaysCollection = businessLogicDB["specialDaysCollection"]
discountParametersCollection = businessLogicDB["discountParametersCollection"]

with open('products.json', 'r') as file:
    products = json.load(file)
    for product in products:
        testProductsCollection.insert_one(product)

with open('users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        testUsersCollection.insert_one(user)

with open('discountparameters.json', 'r') as file:
    parameters = json.load(file)
    for parameter in parameters:
        discountParametersCollection.insert_one(parameter)

with open('specialdays.json', 'r') as file:
    specialDays = json.load(file)
    for day in specialDays:
        specialDaysCollection.insert_one(day)

allUsers = testUsersCollection.find({})
allProducts = testProductsCollection.find({})
allParameters = discountParametersCollection.find({})
allSpecialDays = specialDaysCollection.find({})

for user in allUsers:
    print(user)

for product in allProducts:
    print(product)

for day in allSpecialDays:
    print(day)

for parameter in allParameters:
    print(parameter)

print("DONE")