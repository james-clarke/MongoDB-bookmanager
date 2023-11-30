# pip install pymongo
# pip install dnspython

import pymongo

dbname = "bookmanager"
collection = "Book"
publisher_collection = "Publisher"

myclient = pymongo.MongoClient("mongodb://root:password@127.0.0.1:27017/")
# print(myclient.list_database_names())

mydb = myclient[dbname]

# Get a collection
collection = mydb[collection]
publisher_collection = mydb[publisher_collection]
