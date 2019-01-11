#! /usr/bin/python
#! 3
# coding:utf-8

import  socket

def tcp_ser():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr = ("127.0.0.1", 8889)
    sock.bind(addr)
    # 监听
    sock.listen()

    while True:
        # 接受client访问的socket
        sock_client, addr_client = sock.accept()

        # 接受数据
        msg = sock_client.recv(1000)

        # 解码
        msg = msg.decode()

        # 打印接受内容
        rst = "Received msg:{0} from {1}".format(msg,addr_client)
        print(rst)

        # 发送反馈
        sock_client.send(rst.encode())

        # 关闭连接通路
        sock_client.close()

if __name__ == '__main__':
    tcp_ser()