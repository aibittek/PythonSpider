import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

pool = redis.ConnectionPool(host='192.168.56.128', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'kuili', ex=10)
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))