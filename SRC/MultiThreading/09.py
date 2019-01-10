#_*_coding=utf-8_*_

import threading
import time
import os
from Queue import Queue
# python3
# import queue

#生产者
class Producer(threading.Thread):

    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 100:
                for i in range(10):
                    count += 1
                    msg = self.name+ "生成产品"+str(i)
                    queue.put(msg) # 产品放入队列
                    print msg
            time.sleep(0.5)

class Consumer(threading.Thread):

    def run(self):
        global queue
        while True:
            if queue.qsize() > 10:
                for i in range(3):
                    msg = self.name + "消费了"+ queue.get()
                    print msg
            time.sleep(1)

if __name__ == "__main__":
    queue = Queue()

    # 初始
    for i in range(100):
        queue.put("初始产品"+str(i))

    # 生产2个生产者
    for i in range(1,3):
        p = Producer()
        p.setName("生产者"+str(i))
        p.start()

    # 生成3个消费者
    for i in range(1,4):
        c = Consumer()
        c.setName("消费者"+str(i))
        c.start()


