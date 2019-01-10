# coding:utf-8

#可迭代
l = [i for i in range(10)]

for i in l:
    print(i)

# isinstance 案例
# 判断某个标量是否是一个实例

from collections import Iterable,Iterator
l1 = [1,2,3,4,5]
print("判断list 是否是可迭代{}".format(isinstance(l1,Iterable)))#判断List是否是可迭代
print("判断list 是否是迭代器{}".format(isinstance(l1,Iterator)))#判断List是否是迭代器

# Iter函数
s = "i love python"
print("字符串是否可迭代{}".format(isinstance(s,Iterable)))
print("字符串是否迭代器{}".format(isinstance(s,Iterator)))

s1 = iter(s)
print("字符串iter()转化后是否可迭代{}".format(isinstance(s1,Iterable)))
print("字符串iter()转化后是否迭代器{}".format(isinstance(s1,Iterator)))
