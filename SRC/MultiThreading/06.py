#_*_coding=utf-8_*_

from threading import Thread
import time
import os

def foo():
    print("Daemon start")
    time.sleep(6) #等待时间 超过所有非守护线程执行时间，则下边的print 语句不会被输出
    print("Daemon  pid:{}").format(os.getpid())

def too():
    print("守护线程 开始")
    time.sleep(3)
    print("守护线程 结束  pid:{}").format(os.getpid())

def bar():
    print(456)
    time.sleep(3)
    print("end456  pid:{}").format(os.getpid())


t1=Thread(target=foo)
t2=Thread(target=too)
t3=Thread(target=bar)

# t1 ,t2 设置为主线程,设置主线程必须在start之前设置
# 守护线程在t1,t2 在所有的非守护线程t3结束时立即结束，即使code没有被完全执行
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
time.sleep(2)
t3.start()
print("main-------  PID:{}").format(os.getpid())