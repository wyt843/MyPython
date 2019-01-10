#_*_coding=utf-8_*_

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def func1():
    print "func1 start........."
    lock1.acquire()
    print "func1 Lock1 加锁成功"
    time.sleep(4)
    print "func1 Lock1 等待Lock2...."
    lock2.acquire()
    print "func1 Lock1 lock2 加锁成功"

    lock2.release()
    print "func1 Lock2 解锁成功"
    lock1.release()
    print "func1 Lock1 解锁成功"


def func2():
    print "func2 start........."
    lock2.acquire()
    print "func2 Lock2 加锁成功"
    time.sleep(4)
    print "func2 Lock2 等待Lock1...."
    lock1.acquire()
    print "func2 Lock2 lock1 加锁成功"

    lock1.release()
    print "func2 Lock1 解锁成功"
    lock2.release()
    print "func2 Lock2 解锁成功"

if __name__ == "__main__":

    print "主进程开始........"

    t1 = threading.Thread(target=func1,args=())
    t2 = threading.Thread(target=func2,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print "主进程结束........"