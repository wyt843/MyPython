# coding:utf-8

#委派生成器 案例

from collections import namedtuple
'''
解释：
1、外层for循环每次迭代会新建一个grouper 实例，赋值给coroutine变量：grouper是委派生成器
2、调用next(coroutine),预激委派生成器grouper，此时进入 while True 循环，调用子生成器averager
3、内层for 循环调用 coroutine.send(value),直接把值传递给子生成器averager，同时，当前的grouper
4、内层循环结束后，grouper实例依旧在yield from表达式处暂停，因此，grouper函数定义提中
5、coroutine.send(None)终止averager子生成器，子生成器抛出StopIteration异常病返回的
'''
ResClass = namedtuple('Res', 'count average')

# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return ResClass(count,average)

# 委派生成器
def grouper(storages,key):
    while True:
        # 获取averager()返回值
        storages[key] = yield from averager()

# 客户端代码
def client():
    process_data = {
        "boys_2": [12.3, 45.6, 78.1, 34.5, 66.7],
        "boys_1": [21.2, 23.4, 34.5, 43.6, 44.4]
    }

    storages = {}
    for k, v in process_data.items():
        # 获取协程
        coroutine = grouper(storages, k)

        # 预激协程
        next(coroutine)

        # 发送数据到协程
        for dt in v:
            coroutine.send(dt)

        # 终止协程
        coroutine.send(None)
    print(storages)

# run
client()