# -*-coding=utf-8-*-
# 通过继承threading.Thread来启动一个线程

from threading import Thread
import time

class SayHi(Thread):

    def __init__(self,name):
        super(SayHi, self).__init__()
        self.name = name

    def run(self):
        #延迟2秒
        time.sleep(2)
        print ("%s say hello" %self.name )

if __name__ == '__main__':
    t = SayHi("thread")
    t.start()
    print "主线程打印"