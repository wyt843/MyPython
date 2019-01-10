# _*_coding=utf-8_*_

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def func1():

    print "func1 start........."
    lockFlag = False
    while not lockFlag:
        rst = lock1.acquire(False)
        if rst:
            print ("func1 Lock1 加锁成功")
            time.sleep(2)
            print ("func1 Lock1 等待Lock2....")
            rst = lock2.acquire(False)
            if rst:
                print ("func1 Lock1 lock2 加锁成功")
                lockFlag = True  # 加锁成功，则退出
            else:
                lock1.release()
                print ("func1 Lock2 加锁失败，Lock1 释放资源，休息后继续加锁")
                time.sleep(1)
        else:
            print ("func1 Lock1 加锁失败")


    lock2.release()
    print ("func1 Lock2 解锁成功")
    lock1.release()
    print ("func1 Lock1 解锁成功")


def func2():
    print ("func2 start.........")

    lockFlag = False
    while not lockFlag:
        rst = lock2.acquire(False)
        if rst:
            print ("func2 Lock2 加锁成功")
            time.sleep(2)
            print ("func2 Lock2 等待Lock1....")

            if lock1.acquire(False):
                print ("func2 Lock2 lock1 加锁成功")
                lockFlag = True  # 加锁成功则退出
            else:
                lock2.release()
                print ("func2 Lock1 加锁失败，先释放 Lock2 锁，然后休息后再加锁")
                time.sleep(3)
        else:
            print ("func2 Lock2 加锁失败,然后休息后再加锁")

    lock1.release()
    print ("func2 Lock1 解锁成功")
    lock2.release()
    print ("func2 Lock2 解锁成功")


if __name__ == "__main__":

    print ("主进程开始........")

    t1 = threading.Thread(target=func1, args=())
    t2 = threading.Thread(target=func2, args=())

    t1.start()
    t2.start()

# 等待子线程结束
    t1.join()
    t2.join()

    print ("主进程结束........")