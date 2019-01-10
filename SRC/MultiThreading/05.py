#_*_coding=utf-8_*_

from threading import Thread
from multiprocessing import Process
import time
import os

def work(name):
    print ("进程id:{} ,name:{}").format(os.getpid(),name)

if __name__ == "__main__":
    t = Thread(target=work,args=("thread",))
    p = Process(target=work,args=("Process",))

    t.start()
    p.start()

    print ("主进程id:{}").format(os.getpid())