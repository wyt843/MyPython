#! 3
# coding:utf-8
'''
 map 案例
'''
import time, re
import os, datetime
from concurrent import futures

data = ['1', '2', '3', '4', '5', '6' ,'7']

def wait_on(arg):
    print("{}---------->{}".format(time.ctime(), arg))
    seconds = int(arg)
    time.sleep(seconds)
    return "ok"+arg

# 当多余最大并行进程数时，查看执行结果
ex = futures.ThreadPoolExecutor(max_workers=3)
for i in ex.map(wait_on, data):
    print("{}---------->result={}".format(time.ctime(), i))