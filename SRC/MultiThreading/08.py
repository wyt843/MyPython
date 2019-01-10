#_*_coding=utf-8_*_

import threading

sum = 0
loopSum = 100
lock = threading.Lock()

def myAdd():
    global  sum,loopSum,lock
    for i in range(1,loopSum):
        # 加锁
        lock.acquire()
        # 业务逻辑处理
        sum += 1
        # 释放锁
        lock.release()

def myMinu():
    global sum, loopSum,lock
    for i in range(1, loopSum):
        # 加锁
        lock.acquire()
        # 业务逻辑处理
        sum -= 1
        # 释放锁
        lock.release()

if __name__ == "__main__":

    print "Starting......{}".format(sum)

    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())

    t1.start()
    t2.start()

    print "Done.....{}".format(sum)