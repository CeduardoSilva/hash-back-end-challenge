# Test MongoDB

# If the query finds more than one record, only the first occurrence is updated

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TestDB"]
mycol = mydb["TestCollection"]

print(myclient.list_database_names())
print(mydb.list_collection_names())

mydict = { "name": "John", "address": "4" }
x = mycol.insert_one(mydict)

myquery = { "address": "2" }
mydoc = mycol.find({})

mydelete = { "address": "4" }
mycol.delete_one(mydelete)

newvalues = { "$set": { "address": "PINTO" } }
mycol.update_one(myquery, newvalues)

for y in mydoc:
  print(y) 

print("DONE")