#! 3
#!/usr/bin/python
# coding:utf-8

import re

# 生成一个pattern对象
p = re.compile(r"\d+")

m = p.search("one1two2three3four4")
print(m.group())

# 查找所有匹配结果
rst = p.findall("one1two2three3four4")
print(type(rst))
print(rst)
