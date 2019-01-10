#! 3
#!/usr/bin/python
# coding:utf-8

import re

# 生成一个pattern对象
p = re.compile(r"\d")

# 返回一个Match对象
m = p.match("123d")
print(m.group()) # 匹配的组数
print(m.start()) # 开始位置
print(m.end())   # 结束位置
print(m.span())
print(p.match("dd123d"))

# 两组小写字符串，组中间 空格
p = re.compile(r"([a-z]+) ([a-z]+)")

m = p.match("i am study python")
print(m.groups()) # 返回所有匹配
print(m.group())
print(m.start(1))
print(m.end(2))
print(m)
