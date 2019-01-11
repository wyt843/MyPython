#! /usr/bin/python
#! 3
# coding:utf-8

import  socket

def tcp_cli():

    # 建立socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 连接服务器
    addr = ("127.0.0.1", 8889)
    sock.connect(addr)

    # 发送数据
    msg = "i'm studying python"
    sock.send(msg.encode())

    # 接受反馈数据
    rst = sock.recv(1000)
    print(rst.decode())

    # 关闭链接通路
    sock.close()

if __name__ == "__main__":
    tcp_cli()