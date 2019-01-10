# -*-coding=utf-8-*-

from  threading import Thread
from multiprocessing import Process
import os
def work( ns ):
    global n  #引进主进程全局数据
    n = ns

if __name__ == '__main__':
    # n=100
    # p=Process(target=work)
    # p.start()
    # p.join()
    # print('主',n) #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100


    n=1
    t=Thread(target=work,args=(3,))
    t.start()
    t.join()
    print '主',n #查看结果为0,因为同一进程内的线程之间共享进程内的数据