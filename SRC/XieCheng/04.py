# coding:utf-8

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n +=1
    # yield b
    # 生成器中有return返回，在python3中则会出现一个StopIteration异常
    # 生成器中有return返回，在python2中return后不能带任何参数，则正常返回
    return

g = fib(5)
for i in g:
    print i