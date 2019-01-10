# coding:utf-8

import  multiprocessing
from time import ctime,sleep

def consumer(input_q):
    print("Into consumer:{}".format(ctime()))
    while True:
        # 处理项
        item = input_q.get()
        if item != None:
            print("pull {} out of q".format(item))   #
            input_q.task_done()             # 此处发出信号，任务完成
        else:
            break
    print("Out of consumer:{}".format(ctime()))

def producer(sequence,output_q):
    print ("Into prodocer:{}".format(ctime()))
    for item in sequence:
        output_q.put(item)
        print ("put  {} into q".format(item))
    print ("Out of producer:{}".format(ctime()))

if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()
    sequence = [1,2,3,4]
    producer(sequence,q)
    # 队列中增加哨兵(无用值，表示队列结束)
    q.put(None)
    # 等待消费者消费完
    cons_p.join()