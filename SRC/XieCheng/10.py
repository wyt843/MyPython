# coding:utf-8

import threading
# 引入异步IO包
import  asyncio

# 使用协程
@asyncio.coroutine
def wget(host):
   print("wget {}".format(host))
   connect = asyncio.open_connection(host,80)
   reader, writer = yield from connect
   header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' %host
   writer.write(header.encode("utf-8"))
   yield from writer.drain()
   while True:
       line = yield from reader.readline()
       # http协议使用\r\n换行
       if line == b'\r\n':
           break
       s = '%s header >>> %s' % (host, line.decode("utf-8").rstrip())
       print( s )
    # Ingore the body,close the socket
   writer.close()

# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [wget(host) for host in ['www.baidu.com','www.sina.com','www.sohu.com']]
# asyncio 使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
# 关闭消息循环
loop.close()