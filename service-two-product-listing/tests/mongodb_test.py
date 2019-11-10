# Test MongoDB

# If the query finds more than one record, only the first occurrence is updated

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost/TestCollection")
mydb = myclient["TestDB"]
mycol = mydb["testUsersCollection"]

print(myclient.list_database_names())
print(mydb.list_collection_names())

#mydict = { "name": "John", "address": "4" }
#x = mycol.insert_one(mydict)

myquery = { "id": "ID1" }
#mydoc = mycol.find({})

#mydelete = { "address": "4" }
#mycol.delete_one(mydelete)

newvalues = { "$set": { "date_of_birth": "11/09" } }
mycol.update_one(myquery, newvalues)

mydoc = mycol.find({})
for y in mydoc:
  print(y) 

print("DONE")