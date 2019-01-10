# coding:utf-8

def simple_coroutine(a):
    print("->start")

    b = yield a
    print("->recived",a,b)

    c = yield a + b
    print("->recived", a, b, c)

    yield a + b + c

# rum=n
sc = simple_coroutine(5)
aa = next(sc)
print(aa)
bb = sc.send(6)
print(bb)
cc = sc.send(7)
print(cc)

range(5)