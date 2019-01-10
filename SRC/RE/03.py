#! 3
#!/usr/bin/python
# coding:utf-8

import re

# 生成一个pattern对象
p = re.compile(r"([a-z]+) ([a-z]+)")

s = "hello 123 wang 456 python 34234,abd edf"
rst = p.sub("sub", s)
print(rst)

# 中文匹配
# 大部分中文的表示范围是[u4e00-u9fa5],不包含全角符号
title = u"世界，你好，hello python 中国"
p = re.compile(r"[\u4e00-\u9fa5]+")
rst = p.findall(title)
print(rst)

# 贪婪和非贪婪
# 贪婪 尽可能多的匹配：*
# 非贪婪:找到符合条件的最小内容即可：？
# 正则中默认使用贪婪匹配

title = u"<div>name</div><div>age</div></div>"

p1 = re.compile(r"<div>.*</div>") # 贪婪
p2 = re.compile(r"<div>.*?</div>")  # 非贪婪

m1 = p1.search(title)
print("贪婪模式匹配结果:{}".format(m1.group()))

m2 = p2.search(title)
print("非贪婪模式匹配结果:{}".format(m2.group()))

