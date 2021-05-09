# coding=utf-8

from queue import Queue
import threading

# 输入数据的线程类
class inputThread(threading.Thread):
    # 重写__init__构造函数
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    # 重写run方法
    def run(self):
        dataList = ["One", "Two", "Three", "Four", "Five", 'Exit']
        for data in dataList:
            self.q.put(data)

# 输出数据的线程类
class outputThread(threading.Thread):
    # 重写__init__构造函数
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    # 重写run方法
    def run(self):
        while True:
            data = q.get()
            if (data == 'Exit'):
                break
            print('%s get data:%s' %(self.name, data))

# 创建队列
q = Queue(10)

# 创建1个输入线程和两个输出线程
inputThread1 = inputThread("inputThread1", q)
outputThread1 = outputThread("outputThread1", q)

# 启动线程
inputThread1.start()
outputThread1.start()

# 等待线程退出
inputThread1.join()
outputThread1.join()

print('Main thread called')