# coding=UTF-8

import threading

# 自定义线程类
class myThread(threading.Thread):
    # 重写__init__构造函数
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = 0
    # 重写run方法
    def run(self):
        threadLock.acquire()
        while self.counter < 3:
            self.counter += 1
            print('%s called %d times' %(self.name, self.counter))
        threadLock.release()

#创建线程锁
threadLock = threading.Lock()

# 创建新线程
thread1 = myThread("Thread1")
thread2 = myThread("Thread2")

# 启动线程
thread1.start()
thread2.start()

# 等待线程退出
thread1.join()
thread2.join()

print('Main thread called')