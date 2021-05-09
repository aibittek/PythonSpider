import pymysql

# 连接数据库连接
db = pymysql.connect(host="192.168.56.128",user="root",password="123456",database="test", port=3306)

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句import pymongo
 
client = pymongo.MongoClient(host='45.67.223.227', port=27017)
db = client["db"]
sets = db["sets"]

dict = { "name": "mongdb插入测试", "url": "https://kui.ge" }
 
x = sets.insert_one(dict)
print(x)
sql = """INSERT INTO student(name, nick_name, interest)
         VALUES ('小王', '大王', '老王')"""
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()