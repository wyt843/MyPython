#! /usr/bin/python
#! 3
# coding:utf-8

'''
Client 端流程
        - 1.建立socket
        - 2.发送内容到server
        - 3.接受server的反馈内容
'''

import socket

def clientFunc():

    # 1、建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、发送数据
    text = "i'm studying python"
    data = text.encode()
    addr = ("127.0.0.1", 65432)
    sock.sendto(data, addr)

    # 3、接受数据
    data, addr = sock.recvfrom(100)
    text = data.decode()
    print("content:{content}  address:{address}".format(content=text, address=addr))


if __name__ == '__main__':
    clientFunc()
