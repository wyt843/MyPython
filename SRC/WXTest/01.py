#! /usr/bin/python3
# coding:utf-8

from wxpy import *

# 初始化机器人
bot = Bot(True)

# 输出所有群聊组
for group in bot.groups():
    print(group)

me = bot.search("无语")[0]
me.send("这是python 测试消息")





