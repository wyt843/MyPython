# coding:utf-8

# 导入所需包
from multiprocessing import Process
from os import getppid,getpid
from time import sleep,ctime

def info(title):
    print(title)
    print("module name :", __name__)
    # 父进程id
    print("parent process:", getppid())

    # 子进程id
    print("process id:", getpid())

if __name__ == "__main__":
    p = Process(target=info,args=("子进程",))
    p.start()


