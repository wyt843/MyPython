# 协程
- 参考资料
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    - https://segmentfault.com/a/11900000097816

# 迭代器
- 可迭代（Iterable）：直接作用于for 循环
- 迭代器（Iterator）：不仅可作用域for循环，还可被next调用
    - list 是典型的可迭代对象，但不是迭代器
- 通过instance判断
- Iterable 和 Iterator转化
    - 通过iter()函数
- 案例01.py

# 生成器
- gererator：一边循环一边计算下一个元素的机制/算法
- 满足3个条件:
    - 每次调用都产生for循环需要的下一个元素
    - 如果达到最后一个后，报出StopIteration(）异常
    - 可以被next函数调用
- 如何生成一个生成器
    - 直接使用
        - 案例02.py
    - 如果函数中包含yield，则这个函数叫生成器
    - next函数调用，遇到yield返回
    - yield创建生成器案例 03.py

# 协程
- 历史进程
    - 3.4 引入协程，用yield实现
    - 3.5 引入协程语法
    - 实现协程比较好的包邮asyncio，tornado，gevent
- 定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口在不同位置盯着or开始执行程序
- 从技术角度，协程就是一个你可以暂停执行的函数，或者干脆把协程理解为生成器
- 协程实现：
    - yield 返回
    - send 调用
    - 协程代码案例 05.py
- 协程的四个状态
    - inspect，getgeneratorstate(...) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED:等待开始执行
    - GEN_RUNNING:解释器正在执行
    - GEN_SUSPENED:在yield表达式暂停
    - GEN_CLOSED:执行结束
    - next 预激(prime)
    - 案例 06.py
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给next函数或者send方法的调用方（即触发协程的地方）
    - 终止协程的一种方式：方法送某个哨兵值，让协程退出，内置的None和Ellipsis等常量经常用作哨兵值
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopInteration异常，异常对象的value属性保存在返回值
    - yield from 从内部捕获StopInteration异常
    - 案例 07.py
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式暂停，调用方可以直接把数据发送给子生成器
        - 子生成器把产生的值发给调用方
        - 案例 08.py
- 异步i/o asyncio 案例09.py 10.py
# async and await
- 为了更好的表示异步I/O
- python3.5 引入
- 让协程代码更简洁
- 使用上，可以鉴定单的进行替换
    - 用async替代 @asyncio.coroutine
    - await 替代 yield from
    - 案例 11.py
# aiohttp
- asyncio 实现单线程并发io,在客户端用处不大
- 在服务器端可以asyncio+coroutine配合，因为http是I/O操作
- asyncio实现了TCP,UDP,SSL等协议
- aiohttp 是asyncio实现的http框架
- 使用pip 安装
- 案例12.py

# concurrent.futures
- python3 新增功能
- 类似其他语言的线程池
- 利用multiprocessing实现真正的并行计算
- 核心原理：以子进程的形式，并运行多个python解释器
- concurrent.futures.Executor
    - ThreadPoolExecutor
    - ProcessPoolExecutor
    - 执行的时候需要自行选择
- submit(fn, args, kwargs)
    - fn:异步执行函数
    - args, kwargs 参数
    - 案例 13.py

# current中的map函数
- map(fn, \*iterables, timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout:设置超时时间
    - 案例 14.py