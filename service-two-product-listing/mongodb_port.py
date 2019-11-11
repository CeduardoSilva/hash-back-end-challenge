import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost/TestCollection")
mydb = myclient["TestDB"]
mycol = mydb["testUsersCollection"]

def insert(data, collectionName, dbName):
    myclient[dbName][collectionName].insert_one(data)

def findOne(query, collectionName, dbName):
    return myclient[dbName][collectionName].find(query)

def findAll(collectionName, dbName):
    products = myclient[dbName][collectionName].find({})
    response = []
    for product in products:
        product["_id"] = str(product["_id"])
        response.append(product)
    return response