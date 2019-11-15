import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost/TestCollection")
mydb = myclient["TestDB"]
mycol = mydb["testUsersCollection"]

def insert(data, collectionName, dbName):
    """Inserts the data dict into the collection and data base received

    Args:
        arg1 (dict): Data to be inserted
        arg2 (string): Collection Name
        arg3 (string): Data Base Name

    """
    myclient[dbName][collectionName].insert_one(data)

def findOne(query, collectionName, dbName):
    """Returns a dict from the collection, database and query provided.

    Args:
        arg1 (dict): Query data
        arg2 (string): Collection Name
        arg3 (string): Data Base Name
    Returns:
        dict: Dict from Data Base
    """
    return myclient[dbName][collectionName].find(query)

def findAll(collectionName, dbName):
    """Returns a list of all objects from the collection and database provided.

    Args:
        arg1 (dict): Query data
        arg2 (string): Collection Name
        arg3 (string): Data Base Name
    Returns:
        list: List of objects from Data Base
    """
    products = myclient[dbName][collectionName].find({})
    response = []
    for product in products:
        del product["_id"]
        response.append(product)
    return response