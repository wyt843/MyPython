#! 3
# coding:utf-8
'''
关于 concurrent的案例
'''

from concurrent.futures import ThreadPoolExecutor
import time

def return_future(msg):
    time.sleep(2)
    return msg

# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)

# 往线程池里加2个task
f1 = pool.submit(return_future, 'Hello World')
f2 = pool.submit(return_future, 'Hello Python')

# 等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())

# 打印结果
print(f1.result())
print(f2.result())

