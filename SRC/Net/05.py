#! /usr/bin/python
# coding:utf-8

import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB"
FILE = "README"

# 1、连接远程FTP服务器
try:
    f = ftplib.FTP()
    # 通过设置调试级别的可以方便调试
    f.set_debuglevel(2)

    f.connect(HOST)
    print("connected to host:{}".format(HOST))
except Exception as e:
    print(e)
    exit()

# 登录
try:
    f.login() #
    print("登录成功")
except Exception as e:
    print(e)
    exit()

# 更改目录
try:
    f.cwd(DIR)
    print("目录切换到{}".format(DIR))
except Exception as e:
    print(e)
    exit()

try:
    f.retrbinary("RETR {0}".format(FILE),open(FILE,'wb').write())
    print("文件下载成功")
except Exception as e:
    print(e)
    exit()

try:
    f.close()
except Exception as e:
    exit()