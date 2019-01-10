# coding:utf-8

def simple_coroutine():
    print("->start")
    x = yield
    print("->recived",x)
    # return
    yield

# 主线程
sc = simple_coroutine()
print("1111")
# 可以使用sc.send(None),效果一样
#next(sc) # 预览
sc.send(None)
print("222")
sc.send("xie cheng")