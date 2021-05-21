import redis

# 1、连接redis服务器
r = redis.Redis(host='192.168.204.100', port=6379)

# 2、写入键值对信息到redis数据库
# r.set('304930490', '李奎')

# 3. 写入一个列表
# r.lpush('name', 1, 2, 3, 4, 5)
r.rpush('name', 1, 2, 3, 4, 5)

# 作业：使用集合的方式写入redis数据库，
# key是你的名字，value是你在食堂最喜欢吃的一些食物
# 192.168.204.100:8082
# 账号：admin
# 密码：pass
# 作业还是提交到gakataka，以自己的名字提交