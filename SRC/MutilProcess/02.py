# coding:utf-8

# 导入所需包
import multiprocessing
import os
from time import sleep,ctime

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
        1.__init__函数
        2.run 函数
    '''

    def __init__(self,interval):
        super(ClockProcess,self).__init__()
        self.interval = interval

    def run(self):
        while True:
            print ("{}   sleeping {} seconds......".format(ctime(),self.interval))
            sleep(self.interval)

if __name__ == "__main__":
    p = ClockProcess(1)
    p.start()


