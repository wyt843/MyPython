# --*coding=utf-8*--
# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():

    def __init__(self,name="NoneName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print "My name is {}".format(self.name)

def sayhello():
    print "Hi,python 学习爱好者"

# 此判断语句建议一直作为程序入口
if __name__ == '__main__':
    print "这是一个输出语句"
    print __name__

