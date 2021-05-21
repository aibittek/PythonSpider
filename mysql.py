import pymysql

# 连接数据库连接
db = pymysql.connect(host="192.168.204.100",
    user="root",
    password="123456",
    database="test", 
    port=3306)

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = """UPDATE student SET nick_name='100',interest='200' WHERE name = '3'"""
# 执行sql语句
cursor.execute(sql)

# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()