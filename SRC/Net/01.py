#! /usr/bin/python
#! 3
# coding:utf-8

'''
服务器端流程：
        1、建立socket,socket是负责具体通讯的一个实例
        2、绑定，为创建的scoket指定固定的端口和IP
        3、接受client发送的内容
        4、给对client发送反馈，此步骤为非必须步骤
'''

import socket

def serverFunc() -> object:

    # 1、建立socket
    # socket.AF_INET:使用IPV4 协议族
    # socket.SOCK_DGRAM:使用UDP通讯
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定 ip 和 port
    # 地址是一个tuple类型，(ip,port)
    addr = ("127.0.0.1", 65432)
    sock.bind(addr)

    while True:
        # 3、接受Client消息
        # 接受返回一个元祖值，前一项表示数据，后一项表示地址
        # 参数 bufsize 接受数据的大小
        data, addr_client = sock.recvfrom(1000)
        print(type(data))
        # 发送过来的数据是解码
        data = data.decode() # 默认utf-8
        print("地址{address} 接受的数据为:{content}".format(address=addr_client, content=data))

        # 4、给Client反馈消息
        rsp = "Ich hab keine Hunge"
        # 编码----->字符串转为bytes
        data = rsp.encode()

        sock.sendto(data, addr_client) # 发送给指定主机
        # sock.send(data) # 发送给

if __name__ == "__main__":
    # 启动
    try:
        serverFunc( )
    catch Exception as e:
        print(e)
    finally:
        print("结束了")


