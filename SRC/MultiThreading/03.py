# -*-coding=utf-8-*-
# 通过继承threading.Thread来启动一个线程

from threading import Thread
import time
import os

class SayHi(Thread):

    def __init__(self,name):
        super(SayHi,self).__init__()
        self.name = name

    def run(self):
        # 同一进程的不同线程，其进程ID 一样
        print "进程id:{}   run {} begin at:{}".format(os.getpid(),self.name,time.asctime())
        # 延迟2秒
        time.sleep(2)
        print ("%s say hello" %self.name )
        print "run {} end at :{}".format(self.name,time.asctime())

if __name__ == '__main__':
    t1 = SayHi("thread1")
    t2 = SayHi("thread2")
    t3 = SayHi("thread3")

    t1.start()
    t2.start()
    t3.start()
    print
    print "主线程打印"
    print "主进程id:{}    main end at:{}".format(os.getpid(),time.asctime())