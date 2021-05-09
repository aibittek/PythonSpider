import pymongo
 
client = pymongo.MongoClient(host='192.168.56.128', port=27017)
db = client["db"]
sets = db["sets"]

dict = { "name": "mongdb插入测试", "url": "https://kui.ge" }
 
x = sets.insert_one(dict)
print(x)