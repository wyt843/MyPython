# -*-coding=utf-8-*-
# 通过threading.Thread.start() 启动

from threading import Thread
import time

def sayhi(name):
    # 延迟两秒
    time.sleep(2)
    print ("%s say hello" %name)

if  __name__ == '__main__':
    t = Thread( target = sayhi, args = ('thread',) )
    t.setName("threadname")
    t.start()
    #等待线程结束后
    t.join()
    print "主线程打印"
