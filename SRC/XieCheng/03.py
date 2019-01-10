# coding:utf-8

from time import ctime

# 函数案例
def odd():
    print("Step1")
    print("Step2")
    print("Step3")
    return None

#odd()

# 生成器案例
def odd2():
    for i in range(1,10):
        print("Step{}".format(i))
        yield i

odd_ = odd2()
od = odd_
for i in od:
    print(ctime())
    print i