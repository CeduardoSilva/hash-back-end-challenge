# Populates the data base with products and users

import pymongo
import json

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client["MainDB"]
    productsCollection = db["productsCollection"]
    usersCollection = db["usersCollection"]

    with open('./products.json', 'r') as file:
        products = json.load(file)
        for product in products:
            productsCollection.insert_one(product)

    with open('./users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            usersCollection.insert_one(user)

    allUsers = usersCollection.find({})
    allProducts = productsCollection.find({})

    for user in allUsers:
        print(user)

    for product in allProducts:
        print(product)

    print("DONE")

if __name__ == '__main__':
    main()