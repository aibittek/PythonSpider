import pymongo
 
client = pymongo.MongoClient(host='45.67.223.227', port=27017)
db = client["db"]
sets = db["sets"]

sets.drop()