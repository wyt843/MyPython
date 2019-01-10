# 线程的替代方案
- subprocess
    - 完全跳过线程，直接使用进程
    - 是派生进程的主要方案，python2.4后进入

- mutilprocessing
    - 使用threading派生，使用子进程
    - 允许多核或者多个cpu派生进程，接口和threading非常相似
    - ptyhon2.6后引入

- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2引入
# 多进程
- 进程之间的通讯(InterProcessCommunication,IPC)
- 进程之间无任何共享状态
- 进程创建
    - 直接生产Process实例对象， 案例：01.py
    - 派生子类，案例：02.py
- 在os中可查看pid,ppid的关系
    - 案例03.py

- 生产者消费者模型
    - JoinableQueue
    - 队列中哨兵
    - 案例 04.py