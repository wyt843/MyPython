# coding:utf-8

#直接使用生成器
l = [x*x for x in range(1,6)] #列表生成器
g = (x*x for x in range(1,6)) #生成器
print(type(l))
print(type(g))

next()
