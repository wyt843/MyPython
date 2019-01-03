# --*coding=utf-8*--
import importlib

tuling = importlib.import_module('01')
stu = tuling.Student()
stu.say()
tuling.sayhello()