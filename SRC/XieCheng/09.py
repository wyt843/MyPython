# coding:utf-8

import threading
# 引入异步IO包
import  asyncio

# 使用协程
@asyncio.coroutine
def hello():
    print("hello world!{}".format(threading.currentThread()))
    print("start.....{}".format(threading.currentThread()))
    yield from asyncio.sleep(10)
    print("Done......{}".format(threading.currentThread()))
    print("Hello again!{}".format(threading.currentThread()))

# 启动消息循环
loop = asyncio.get_event_loop()

# 定义任务
tasks = [hello(),hello()]

# asyncio 使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))

# 关闭消息循环
loop.close()