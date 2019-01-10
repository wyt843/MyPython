# #!/usr/bin/env python3
# coding: utf-8
'''
多线程案例：
    线程持续活动，除非手工关闭
'''
import multiprocessing
import os
from time import sleep,ctime

def clock(interval):
    while True:
        print ("Pid:{} The sleep time is {}" .format(os.getpid(),interval))
        sleep(interval)

if __name__ == "__main__":
    print ("main start...........")
    p = multiprocessing.Process(target=clock,args=(1,))
    p.start()